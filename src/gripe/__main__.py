"""
"""
from fleks.cli import click  # noqa

@click.group
def entry():
    """
    CLI for actions on gripe servers.
    """
from gripe import (
    restart, stop, _list, start)
entry.command("restart")(restart)
entry.command("stop")(stop)
entry.command("ls")(_list)
entry.command("list")(_list)
entry.command("start")(start)

if __name__ == "__main__":
    entry()
