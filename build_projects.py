#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import shutil
import pypandoc
import yaml

import github


namehash = {}
namehash['exe'] = "Windows"
namehash['dmg'] = "OS X"
namehash['pkg'] = "OS X"
namehash['run'] = "Linux"
namehash['deb'] = "Ubuntu"
namehash['rpm'] = "Linux"

gh = github.Github()
org = gh.get_organization("parallaxinc")
repos = org.get_repos()

print gh.get_rate_limit().rate.remaining


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

    # readme
    try:
        readme = repo.get_readme()
        readmetext = unicode(readme.decoded_content,'utf8')
        ext = os.path.splitext(readme.name)[1].replace('.','')

        if not ext == 'md':
            print "Converting",readme.name, ext
            readmetext = pypandoc.convert(readmetext,'md',format=ext)

        output += readmetext+"\n"

    except github.UnknownObjectException:
#        print "README for",repo.name,"not found"
        pass

    return output

outpath = '_projects'

shutil.rmtree(outpath, True)
os.mkdir(outpath)

for repo in repos:
    if not repo.name.endswith("-docs"):
        print repo.name

        filename = os.path.join(outpath,repo.name.lower()+".md")
    
        f = open(filename,'w')
        f.write(render_page(repo).encode('utf8'))
        f.close()

