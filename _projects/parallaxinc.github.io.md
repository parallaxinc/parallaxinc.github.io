---
title: parallaxinc.github.io
tagline: Source repository for developer.parallax.com
links:
    Code: https://github.com/parallaxinc/parallaxinc.github.io
    Issues: https://github.com/parallaxinc/parallaxinc.github.io/issues
    Releases: https://github.com/parallaxinc/parallaxinc.github.io/releases
---
# Parallax Developer Site

[developer.parallax.com](http://developer.parallax.com) is the home page for Parallax open-source development.

This website is build by pulling content and metadata from the [parallaxinc GitHub](https://github.com/parallaxinc), so you can participate by simply editing your project.

### Step 1: Add a README

Make a nice, preferably markdown-formatted README for your project. It's rendered to the page HTML so you want it to look good.

The site builder will attempt to pull the README from the default branch in your repository. This will be used to build your project page.

If your project contains Github Releases, this site will automatically publish the latest release that is *NOT* marked as *draft* or *prerelease* in a special *Downloads* section of your project page.

### Step 2: Add a `site.yml` config to your project root

#### Description

Add the `description` key to add a longer description than the regular GitHub tagline provides.
Use the pipe character (`|`) to add a description that spans several lines.

    description: |
        This is an awesome piece of software that I use all the time in everything.
        Supporting every language under the sun, it promises to end world hunger and take
        us to the Super Bowl.

#### Image

Add a link to your project logo if available. It can be relative to the root of your repo, or an absolute URL to some magic place on the internet. Something square, in the neighborhood of 100x100 is best.

    image: icons/logo.png
    
#### Type

Specify the application type of your project. Projects that don't specify this key will appear in *Other*.

    type: tools
    
Supported types are: `tools`, `compilers`, `libraries`, `hardware`. 

#### Microcontroller

Specify the `microcontroller` key to limit the scope of your project to a specific microcontroller.

| Value     | Description       |
| --------- | ----------------- |
| `bs`      | Any Basic Stamp   |
| `bs1`     | Basic Stamp 1     |
| `b2`      | Basic Stamp 2     |
| `prop`    | Any Propeller     |
| `prop1`   | Propeller 1       |
| `prop2`   | Propeller 2       |

#### Platform

Specify the `platform` key to limit the scope of your project to a specific platform.

| Value         | Description               |
| ------------- | ------------------------- |
| `arlo`        | Arlo Robot                |
| `activitybot` | ActivityBot               |
| `elev8`       | ELEV-8 Quadcopter         |
| `spinneret`   | Spinneret Web Server      |

#### Board

Specify the `board` key to limit the scope of your project to a specific board.

| Value         | Description                   |
| ------------- | ----------------------------- |
| `boe`         | Board Of Education            |
| `pab`         | Propeller Activity Board      |
| `pabwx`       | Propeller Activity Board WX   |
| `c3`          | Propeller C3                  |

#### Language

Specify the `language` key to indicate the programming language your project is written in/for.

| Value         | Description                   |
| ------------- | ----------------------------- |
| `c`           | Propeller C                   |
| `forth`       | Tachyon Forth                 |
| `pbasic`      | PBASIC                        |
| `propbasic`   | PropBASIC                     |
| `spin`        | Propeller Spin                |

#### Multiple Values

Types, platforms, boards, languages, and microcontrollers support the use of multiple values with the pipe character (`"|"`):

    type: tools|libraries
    platform: bs2|prop1
    
If you don't see the values you need, submit an issue to request them.

#### Links

Links are automatically added to the top of every page. `Code` and `Releases` point to the main repository and GitHub Releases page for a project. An `Issues` link is added if the project uses GitHub Issues.

However, you can use the `links` key to add custom links to your project:

    links:
        Docs: /docs/propellermanager/html
        Some Other Thing: www.google.com

#### Finished `site.yml`

Put it all together:

    image: icons/logo.png
    description: |
        This is where the magic happens. Finally, a project that changes the world.
        Let's talk about it.
    type: tools|libraries
    board: c3
    language: spin
    microcontroller: prop1
    links:
        Docs: /docs/propellermanager/html
        Some Other Thing: www.google.com

### Step 3: Wait

The site will be updated to reflect your changes in a day or so, or submit an issue requesting a rebuild for faster turnaround.

