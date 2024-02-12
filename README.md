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
      Opinionated extensions for the `grip` utility.  <br/>
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

The <a href=https://pypi.org/project/grip/>grip utility</a> provides rendering/serving local markdown files written in github-flavored markdown.  Gripe extends it, allowing for serving more types of local files, as well as intelligent management for multiple `grip` daemons.


-------------------------------------------------------------------------------

## Features

### Support for Multiple Projects

Working with multiple projects simultaneously is supported.  (This works by managing multiple daemons with a per-project port)

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
### Starting and Stopping Servers 

-------------------------------------------------------------------------------

## Usage (API)

### Listing Servers 
### Starting and Stopping Servers 

```pycon
>>> import gripe 
```
