#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re
import shutil
import pypandoc
import yaml

import github

import argparse

def error(*objs):
    print ' '.join(objs)
    sys.exit(1)

namehash = {}
namehash['exe'] = "Windows"
namehash['dmg'] = "OS X"
namehash['pkg'] = "OS X"
namehash['run'] = "Linux"
namehash['deb'] = "Ubuntu"
namehash['rpm'] = "Linux"

parser = argparse.ArgumentParser(description='Build Jekyll-friendly site content from your Github projects.')
parser.add_argument('-t','--token', type=str, default=None, help='use this access token for authentication')
parser.add_argument('org', type=str, metavar='NAME', help='the organization for building your site')

args = parser.parse_args()

if not args.org:
    error("No organization provided")

gh = github.Github(args.token)

try:
    org = gh.get_organization(args.org)
except github.UnknownObjectException:
    error("Organization",args.org,"not found!")
except github.BadCredentialsException:
    error("Bad credentials provided!")

repos = org.get_repos()

print "Remaining requests:", gh.get_rate_limit().rate.remaining


def fix_image_url(repo, url):

    if len(url) > 0 and not url.startswith("https://") and not url.startswith("/"):
        url = repo.html_url + "/raw/master/" + url 

    return url

def render_readme(repo):
    output = ""
    try:
        readme = repo.get_readme()
    except github.UnknownObjectException:
        return output

    readmetext = unicode(readme.decoded_content,'utf8')
    ext = os.path.splitext(readme.name)[1].replace('.','')

    if not ext == 'md':
        print "Converting",readme.name, ext
        readmetext = pypandoc.convert(readmetext,'md',format=ext)

    readmetext = re.sub(r"!\[([^\]]*?)\]\((?<!(https:))([^\)]*?)\)",
                        r"![\1]("+repo.html_url+r"/raw/master/\3)",
                        readmetext)

    output += readmetext+"\n"

    return output


def render_releases(repo):
    output = ""
    try: 
        release = repo.get_release_latest()
    except:
        return output

    output += u"tag_name: "+release.tag_name+"\n"
    output += u"tag_url:  "+release.html_url+"\n"

    output += u"platforms:\n"
    
    for a in release.assets:
        ext = os.path.splitext(a.name)[1].replace('.','')

        if ext in namehash.keys():

            platform = u""
            if ext == 'deb':
                if 'armhf' in a.name:
                    platform = "Raspbian"
                else:
                    platform = "Ubuntu"
            else:
                platform = namehash[ext]
                    
                
            output += "  - name: "+platform+"\n"
            output += "    link: "+a.browser_download_url+"\n"
            output += "    file: "+a.name+"\n\n"

    return output

def render_page(repo):
    output = unicode("---\n",'utf8')
    output += "title: "+repo.name+"\n"
    output += "tagline: "+repo.description+"\n"

    links = {}
    links["Code"] = repo.html_url
    links["Releases"] = repo.html_url+"/releases"

    if repo.has_issues:
        links["Issues"] = repo.html_url+"/issues"

    # site.yml
    try:
        siteyml = repo.get_file_contents("site.yml")
        config = yaml.load(siteyml.decoded_content)

        for c in config.keys():
            if c == "links":
                for l in config[c].keys():
                    links[l] = config[c][l]
            elif c == "image":
                output += c+": "+fix_image_url(repo, config[c])+"\n"
            else:
                output += c+": "+config[c]+"\n"
    except:
        pass


    # links
    output += "links:\n"

    for l in links.keys():
        output += "    "+l+": "+links[l]+"\n"

    output += render_releases(repo)
    output += "---\n"

    output += render_readme(repo)

    return output

outpath = '_projects'

shutil.rmtree(outpath, True)
os.mkdir(outpath)

count = 0
for r in repos:
    count += 1

print count, "repositories found"


for repo in repos:
    if not repo.name.endswith("-docs"):
        print " -",repo.name

        filename = os.path.join(outpath,repo.name.lower()+".md")
    
        f = open(filename,'w')
        f.write(render_page(repo).encode('utf8'))
        f.close()

