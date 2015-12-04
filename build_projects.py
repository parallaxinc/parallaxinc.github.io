#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import shutil
#import pickle
import pypandoc
import yaml

import github

#f = open("bleh.txt")
#repos = pickle.load(f)
#f.close()

gh = github.Github()
org = gh.get_organization("parallaxinc")
repos = org.get_repos()

print gh.get_rate_limit().rate.remaining

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

    output += "links:\n"

    for l in links.keys():
        output += "    "+l+": "+links[l]+"\n"


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

