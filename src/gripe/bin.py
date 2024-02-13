""" gripe.bin:
        Console-script entrypoints (see `gripe --help`)
"""

from fleks.cli import click  # noqa


@click.group
def entry():
    """
    CLI for actions on gripe servers.
    """


from gripe import _list, restart, start, stop

entry.command("restart")(restart)
entry.command("stop")(stop)
entry.command("ls")(_list)
entry.command("list")(_list)
entry.command("start")(start)
