# services

Each folder contains a services that is part or can be spawned by the platform.

## overview

This is a schematic of how services are interconnected:

[![service-web](../docs/img/service-web.svg)](http://interactive.blockdiag.com/?compression=deflate&src=eJxdjs0KwjAQhO99imXPFtNbpcYXkR7ys2hw6UqSKiK-uymxiF7nm28Yy-IuPpgTPBsAvJPdOg40ZYRjOpsr6UkyjUOB_tEmirfgKH0YaEDHMnsshX993x5qsEgUyx4bS6x3qu824IQlastz3f4pFtGHSC5LXCXsleqw3ljRUvteGprXG1PtQR0)


### localhost deploy (dev)

- [web](http://127.0.0.1:9081/)
  - [webapi doc](http://127.0.0.1:9081/webapi/doc)
  - [webapi version 0](http://127.0.0.1:9081/v0/)
- [portainer](http://127.0.0.1:9000/#/auth): swarm (you set your own pass)
- [adminer](http://127.0.0.1:18080/?pgsql=postgres&username=simcore&db=simcoredb&ns=): database content
- [minio](http://127.0.0.1:9001): storage management
  - ``user=12345678, password=12345678``
- [traefik](http://172.0.0.1:8080/dashboard/): reverse proxy dashboard
  - [whoami](http://127.0.0.1:8080/whoami): test service to check traefik

See details in [docker-compose.local.yml](docker-compose.local.yml).

----

A quick description of each service.

### director

The director is responsible for making dynamic services and computational services available in a docker registry to the workbench application.
It is also responsible for starting and stopping such a service on demand. A service may be composed of 1 to N connected docker images.

### web

This is a service that provides the server/client infrastructure of the the workbench application.

## Architecture

### workbench

The association of the web, authentication and director services creates the so-called workbench application. It provides the main entry point for the user.

### workbench nodes

The other services are made available through a docker registry to the workbench application.
When a node is created in the workbench frontend, the director starts the respective services accordingly.
The started services are dispatched on the available cluster and connected to the workbench application.
When the user closes a node or disconnects, any running service will be automatically closed.

## Development Workflow

To build images for development

```!bash
  make build-devel
  make up-devel
```

To build images for production

```!bash
  make build tag-version
  make up-version
```

## Deploying Services

To build and tag these images:

```!bash
  make build tag-version tag-latest
```

To deploy the application in a single-node swarm

```!bash
  make up-latest
```
## Credentials

Rename `.env-devel` to `.env` in order to get the stack up and running.
