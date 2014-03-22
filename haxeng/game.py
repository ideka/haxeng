#       Copyright 2010, 2014 Gerardo Marset <gammer1994@gmail.com>
#
#       This file is part of Haxxor Engine.
#
#       Haxxor Engine is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       Haxxor Engine is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with Haxxor Engine.  If not, see <http://www.gnu.org/licenses/>.

import os
import time
import json

import tools
from filesystem import File
import cli
import system
import missions

SAVEGAME = "{}.sav"


class Game(object):
    def __init__(self):
        self.running = True

        print("Bienvenido a Haxxor Engine.")
        try:
            self.name = "test"  # ask_for_name()
        except EOFError:
            self.running = False
            return

        self.clear()

        if os.path.isfile(SAVEGAME.format(self.name)):
            self.load()
            print("Juego cargado.")
        else:
            self.aliases = default_aliases()
            self.mission_id = 0
            self.system = system.default_local_system()
            self.save()
            print("Una nueva partida fue creada para {}.".format(self.name))
            print("Escribí \"help\" para ver la lista de comandos.")

        self.start_mission()
        self.cli = cli.CLI(self.system, self)

    @property
    def valid_hosts(self):
        return ["127.0.0.1", "localhost", self.system.ip,
                self.mission.system.ip]

    def start_mission(self, restart=None):
        self.mission = (missions.missions[self.mission_id].
                        get_prepared_copy(self, restart))
        print("Tenés un e-mail. Escribí \"mail\" para verlo.")

    def main_loop(self):
        while self.running:
            ms = time.time()

            self.cli.prompt()

            if not self.cli.system.is_local:
                if self.mission.ip_tracker.update(time.time() - ms,
                                                  self.system.ip):
                    self.telnet_end()

    def load(self):
        with open(SAVEGAME.format(self.name), "r") as f:
            load_dict = json.loads(f.read())
        self.aliases = load_dict["aliases"]
        self.mission_id = load_dict["mission_id"]

        filesystem = load_dict["filesystem"]
        ip = load_dict["ip"]

        def recursive_loop(directory):
            for name, value in directory.items():
                if isinstance(value, dict):
                    for element in recursive_loop(value):
                        pass
                else:
                    directory[name] = File(value)
                    yield name
        for element in recursive_loop(filesystem):
            pass
        self.system = system.System(filesystem, ip, True)

    def save(self):
        with open(SAVEGAME.format(self.name), "w") as f:
            f.write(json.dumps({
                "aliases": self.aliases,
                "mission_id": self.mission_id,
                "filesystem": self.system.filesystem,
                "ip": self.system.ip
            }, indent=4, default=lambda o: o.id_))

    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name in ("nt", "dos", "ce"):
            os.system("cls")
        else:
            print("\n" * 300)

    def telnet_start(self):
        self.cli.system = self.mission.system
        self.clear()
        print(self.mission.asciiart)
        if not self.cli.telnet_login():
            self.telnet_end()

    def telnet_end(self):
        self.cli.system = self.system
        self.clear()
        print("Conexión cerrada.")
        self.start_mission(self.mission)


def default_aliases():
    return {
        "cd..": "cd ..",
        "ls": "dir",
        "rm": "del",
        "clear": "cls"
    }


def ask_for_name():
    while True:
        name = tools.iinput("¿Cuál es tu nombre? ")

        if name == "":
            print("Escribí tu nombre.")
            continue

        if not all(ord(c) < 128 for c in name):
            print("Solo se permiten caracteres ASCII.")
            continue

        if not name.isalnum():
            print("Solo se permiten caracteres alfanuméricos.")
            continue
        break
    return name
