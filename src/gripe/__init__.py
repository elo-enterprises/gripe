""" gripe
"""

import os
import json
import time
import pathlib

import grip
import psutil
from flask import Flask, send_from_directory
from fleks.cli import click
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from fleks.util import lme, typing  # noqa

DEFAULT_PORT = "6149"
DEFAULT_SLEEP = 1.5  # in seconds
DEFAULT_APP_NAME = "gripe:app"
DEFAULT_LOG_FILE: str = ".tmp.gripe.log"
LOGGER = lme.get_logger(__name__)
THIS_PATH = pathlib.Path(".").absolute()

from .util import filter_pids


class PortBusy(RuntimeError):
    pass


def _current_gripe_procs() -> typing.List[psutil.Process]:
    """ """
    return filter_pids(cmdline__contains=DEFAULT_APP_NAME)


def get_port(proc):
    """"""
    conns = proc.connections()
    if conns:
        return conns[0].laddr.port
    else:
        LOGGER.critical(f"no connections found for pid@{proc.pid}")
        return None


def _used_ports():
    """ """
    return [x for x in filter(None, [get_port(p) for p in _current_gripe_procs()])]


def _do_serve(background=True, port=DEFAULT_PORT):
    """ """
    bg = "&" if background else ""
    port = int(port)
    port_used = port in _used_ports()
    if port_used:
        raise PortBusy(f"port {port} is in use!")
    cmd = f"flask --app {DEFAULT_APP_NAME} run --port {port} >> {DEFAULT_LOG_FILE} 2>&1 {bg}"
    LOGGER.critical("starting server with command:")
    LOGGER.critical(f"  '{cmd}'")
    return os.system(cmd)


def _is_my_grip(proc_dict: dict) -> bool:
    """ """
    return proc_dict["cwd"] == str(THIS_PATH)


class Server:
    """ """

    @property
    def proc(self) -> psutil.Process:
        """ """
        tmp = [proc for proc in _current_gripe_procs() if _is_my_grip(proc.as_dict())]
        if tmp:
            result = tmp[0]
            return result

    @property
    def live(self) -> bool:
        """ """
        return bool(self.proc)

    @property
    def port(self):
        """ """
        return self.proc and get_port(self.proc)

    @property
    def raw_file_server(self):
        """ """
        raw_file_server = Flask(__name__)
        raw_file_server.debug = True

        @raw_file_server.route("/<path:path>")
        def raw(path):
            raw_file_server.logger.critical(path)
            return send_from_directory(pathlib.Path(".").absolute(), path)

        return raw_file_server

    @property
    def app(self):
        """ """
        compound = Flask(__name__)
        compound.wsgi_app = DispatcherMiddleware(
            grip.create_app(user_content=True), {"/__raw__": self.raw_file_server}
        )
        return compound


server = Server()

# WARNING: this initiates real flask bootstrap,
# for which `grip` expects README.md to already be available
try:
    app = server.app
except (Exception,) as exc:
    LOGGER.critical(exc)
    app = None


def _list():
    """Lists running all running servers"""
    result = dict(local=[], foreign=[])
    for proc in _current_gripe_procs():
        key = "local" if _is_my_grip(proc.as_dict()) else "foreign"
        result[key].append(
            dict(
                pid=proc.pid,
                cwd=proc.cwd(),
                port=get_port(proc),
            )
        )
    print(json.dumps(result))
    return result


@click.flag("--fg", help="run in foreground")
@click.flag(
    "--force",
    help="force kill if already running",
)
@click.option(
    "--port",
    help="port to listen on.  (leave empty to use next available)",
    default="6149",
)
def start(
    fg: bool = None, ls: bool = None, force: bool = None, port: str = None
) -> object:
    """Starts a webserver for working-dir"""
    port = port or DEFAULT_PORT
    LOGGER.critical("trying to serve files")
    result = None
    background = not fg
    should_start = ls or True
    grips = _current_gripe_procs()
    if grips:
        LOGGER.critical(f"{len(grips)} copies of gripe are already started")
        for p in grips:
            if _is_my_grip(p.as_dict()):
                LOGGER.critical(f"gripe @ pid {p.pid} is already serving this project")
                if force:
                    LOGGER.critical("`force` was passed; killing it anyway..")
                    p.kill()
                else:
                    LOGGER.critical("Skipping startup.")
                    should_start = False
                break
        else:
            LOGGER.critical("No gripes are serving this project.")

    if should_start:
        port = int(port)
        LOGGER.warning("Starting gripe for this project..")
        used = _used_ports()
        LOGGER.warning(f"Used ports: {used}")
        if port in used:
            next_port = max(used) + 1
            LOGGER.critical(f"server port @ {port}, using next available @ {next_port}")
            port = next_port
        # NB: return is useless because system=True for launch
        error = _do_serve(port=port, background=background)
        # except (PortBusy,) as exc:
        #     LOGGER.critical(error = _do_serve(port=max(_used_ports())+1,background=background)
        if error:
            raise SystemExit(error)
        else:
            LOGGER.warning("Launched server, looking for process..")
            return True

    return result


DictMaybe = typing.Union[typing.Dict, None]


def stop(
    grip: DictMaybe = None,
    grips=[],
):
    """Stops server (if any) for this working-dir"""
    grips = grips or (grip and [grip]) or _list()["local"]
    killed = []
    if not grips:
        LOGGER.critical("No daemons for `gripe` are started here")
    else:
        for dct in grips:
            if _is_my_grip(dct):
                LOGGER.critical(f"gripe @ {dct} started here")
                LOGGER.critical("killing it..")
                for proc in _current_gripe_procs():
                    if proc.pid == dct["pid"]:
                        proc.kill()
                        killed.append(dct)
    return dict(killed=killed)


def restart():
    """Restarts server for this working-dir"""
    _list()
    stop()
    time.sleep(DEFAULT_SLEEP)
    start()


list = _list
