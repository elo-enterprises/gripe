<table>
  <tr>
    <td colspan=2>
      <strong>gripe</strong>&nbsp;&nbsp;&nbsp;&nbsp;
      <a href=https://pypi.org/project/gripe><img src="https://img.shields.io/pypi/l/gripe.svg"></a>
      <a href=https://pypi.org/project/gripe><img src="https://badge.fury.io/py/gripe.svg"></a>
      <a href="https://github.com/elo-enterprises/gripe/actions/workflows/python-publish.yml"><img src="https://github.com/elo-enterprises/gripe/actions/workflows/python-publish.yml/badge.svg"></a><a href="https://github.com/elo-enterprises/gripe/actions/workflows/python-test.yml"><img src="https://github.com/elo-enterprises/gripe/actions/workflows/python-test.yml/badge.svg"></a>
    </td>
  </tr>
  <tr>
    <td width=15%><img src=https://raw.githubusercontent.com/elo-enterprises/gripe/master/img/icon.png style="width:150px"></td>
    <td>
      Opinionated extensions for the `grip` utility.  <br/><br/>
      The <a href=https://pypi.org/project/grip/>grip utility</a> provides rendering/serving local markdown files written in github-flavored markdown.  Gripe extends it, allowing for serving more types of local files, as well as intelligent management for multiple `grip` daemons.
      <br/>
    </td>
  </tr>
</table>

---------------------------------------------------------------------------------

  * [Overview](#overview)
  * [Features](#features)
    * [Support for Multiple Projects](#support-for-multiple-projects)
  * [Installation](#installation)
  * [Usage (CLI)](#usage-cli)
    * [Listing Servers](#listing-servers)
    * [Starting and Stopping Servers](#starting-and-stopping-servers)
  * [Usage (API)](#usage-api)
    * [Listing Servers](#listing-servers-1)
    * [Starting and Stopping Servers](#starting-and-stopping-servers-1)


---------------------------------------------------------------------------------

## Overview

The `gripe` library provides extensions for [grip](https://pypi.org/project/grip/).

The <a href=https://pypi.org/project/grip/>grip utility</a> provides rendering/serving local markdown files written in github-flavored markdown.  

Gripe extends it, allowing for serving more types of local files, as well as intelligent management for multiple `grip` daemons without thinking about server-port collisions.

-------------------------------------------------------------------------------

## Features

### Support for Multiple Projects

Working with multiple projects simultaneously is supported.  This works by managing multiple daemons with a per-project port. See [CLI Usage](#cli-usage) for more information.  

---------------------------------------------------------------------------------

## Installation

See [pypi](https://pypi.org/project/gripe/) for available releases.

```bash
$ pip install gripe
```

---------------------------------------------------------------------------------

## Usage (CLI)

The gripe library publishes a small CLI tool.

### Listing Servers 

```bash

# or `gripe ls` or `python -mgripe ls`
$ gripe list 
{"local": [], "foreign": []}
```

### Starting and Stopping Servers 

```bash

# or `python -mgripe start`
$ gripe start
INFO gripe Trying to serve files                        
DEBUG gripe Starting gripe for this project..
DEBUG gripe Used ports: []                             
INFO gripe starting server with command:
INFO gripe 'flask --app gripe:app run --port 6149 >> .tmp.gripe.log 2>&1 &'

# startup example for a 2nd server over the same project: server start is NO-OP
$ gripe start
INFO gripe Trying to serve files                     
INFO gripe 1 copies of gripe are already started     
INFO gripe gripe @ pid `10059` is already serving this project
INFO gripe Skipping startup.

# startup example for 2nd server over 2nd project: new port allocated automatically
$ gripe start
INFO gripe trying to serve files
INFO gripe 1 copies of gripe are already started
INFO gripe No gripes are serving this project.
DEBUG  gripe Starting gripe for this project..
DEBUG  gripe Used ports: [6149]
DEBUG gripe server port @ 6149, using next available @ 6150
INFO gripe starting server with command:
INFO gripe   'flask --app gripe:app run --port 6150 >> .tmp.gripe.log 2>&1 &'

$ gripe stop
INFO gripe gripe @ {'pid': 10059, 'cwd':'...', 'port': 6149} started here
INFO gripe killing it..
```

-------------------------------------------------------------------------------

## Usage (API)

### Listing Servers 

```pycon
>>> import gripe 
>>> gripe.list()
{"local": [], "foreign": []}
```

### Starting and Stopping Servers 

```pycon
>>> import gripe 

>>> servers = gripe.start(); print(servers)
{ "local": [
    { "pid": 93867, 
      "cwd": "...", 
      "port": 6149 }
  ], 
  "foreign": []
}

>>> gripe.stop(grips=servers['local'])
{
 "killed": 
   [ { "pid": 93867, 
       "cwd": "...", 
       "port": 6149 } ]
}
```
