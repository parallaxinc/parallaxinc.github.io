---
layout: project
title: Cloud-Session
tagline: Server for managing user information, rate limiting and sending email
type: other
links:
    Code: https://github.com/parallaxinc/Cloud-Session
    Issues: https://github.com/parallaxinc/Cloud-Session/issues
    Releases: https://github.com/parallaxinc/Cloud-Session/releases
---
# Cloud-Session
Authentication system for cloud-compiled projects, and also provides a configurable rate limiting system.

All services are provided as rest services that return json. They should not be called by the users browser or client side application but by the servers on a private network.

## Terminology
- Local user: registered using an email and password. They'll have to confirm their email address and request password reset tokens.
- OAuth user: users registered through a third party authentication service. They cannot change their password through this server, nor have to confirm their email address.


## Manuals
### Installation
Preferably in a virtualenv:
pip install -r requirements.txt

In case you get: EnvironmentError: mysql_config not found
sudo apt-get install libmysqlclient-dev

In case you get: /usr/bin/ld: cannot find -lz
sudo apt-get install zlib1g-dev

### Mysql setup
Create a schema and if wanted a user and import the [table definitions](cloudsession-schema.sql).

A different database can be used, but the sql might need to be changed and configuration will be needed.

### Configuration
Create a text file with the name **cloudsession.properties** and put in configurations as described in the [configuration manual](CONFIGURATION.md).

### Deployment
Set the generated or downloaded war into the webapps directory of your tomcat and start it.

