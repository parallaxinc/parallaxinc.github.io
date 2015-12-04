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

#### Step 2: Use absolute image URLs

This site doesn't store any content locally; it pulls it all from GitHub, so if you want your images to show up, use absolute links to them.

#### Step 3: Add a `site.yml` config to your project root

Add an absolute link to your project logo:

    image: https://github.com/parallaxinc/PropellerIDE/raw/master/icons/logo.png
    
Add the preferred version number:

    version: 0.33.3
    
Categorize your application:

    type: tools

You can also add custom links at the top:

    links:
        Docs: /docs/propellermanager/html
        Some Other Thing: www.google.com
        
Put it all together:

    image: https://github.com/parallaxinc/PropellerIDE/raw/master/icons/logo.png
    version: 0.33.3
    type: tools

    links:
        Docs: /docs/propellermanager/html
        Some Other Thing: www.google.com
