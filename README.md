# parallaxinc.github.io

[developer.parallax.com](http://developer.parallax.com) is the home page for Parallax open-source development efforts.

- PropellerIDE
- BlocklyProp
- OpenSpin
- PropGCC

This website automatically pulls its content from the projects in the `parallaxinc` organization, so you can push changes to the site just by editing your project.

### How can I participate?

Making your project look presentable is as easy as three steps.

#### Step 1: Add a README

Make a nice, preferably markdown-formatted README for your project. It's rendered to the page HTML so you want it to look good.

#### Step 2: Add a `site.yml` config to your project root

Add an absolute link to your project logo:

    image: icons/logo.png
    
Categorize your application:

    type: tools
    
Use more than one category with the pipe character (`"|"`):

    type tools|libraries

Links are automatically added to the top of every page. `Code` and `Releases` point to the main repository and GitHub Releases page for a project. An `Issues` link is added if the project uses GitHub Issues.

You can also add custom links:

    links:
        Docs: /docs/propellermanager/html
        Some Other Thing: www.google.com

Put it all together:

    image: icons/logo.png
    type: tools|libraries

    links:
        Docs: /docs/propellermanager/html
        Some Other Thing: www.google.com

If your project contains Github Releases, this site will automatically publish the latest release that is *not* marked as *draft* or *prerelease*.

Step 3: Wait

The site will be updated to reflect your changes in a day or so, or submit an issue requesting a rebuild for faster turnaround.
