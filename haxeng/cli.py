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

import sys
import os.path
import random
import time

import common
from filesystem import File
import system
import tools
import info


class CLI(object):
    commands = {}

    def __init__(self, system, game):
        self._system = None

        self.dirlist = []

        self.system = system
        self.game = game

    @staticmethod
    def command(cmd):
        CLI.commands[cmd.name] = cmd

    @property
    def pwd(self):
        return tools.format_dirlist(self.dirlist)

    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value
        self.dirlist = [list(self._system.filesystem.keys())[0]]

    def parse_input(self, cmd):
        if cmd == "":
            return

        cmd = cmd.strip()
        args = cmd.split(" ")
        args[0] = args[0].lower()

        if args[0] in self.game.aliases:
            args = self.game.aliases[args[0]].split(" ") + args[1:]

        if args[0] in self.commands:
            self.commands[args[0]].try_to_run(self, args[1:])
        else:
            print("betch: comando desconocido: {}".format(args[0]))

    def prompt(self):
        try:
            self.parse_input(tools.iinput(self.pwd + ">"))
        except EOFError:
            print()
            if common.DEBUG or tools.yn("¿Seguro que querés salir?", False):
                self.game.running = False
        except Exception as e:
            if common.DEBUG:
                raise
            else:
                print("betch: excepción no manejada:", sys.exc_info()[0], e)

    def clear(self):
        return self.game.clear()

    def telnet_login(self):
        print("Identifíquese o presione Ctrl+C para cancelar.")
        while True:
            try:
                user = tools.iinput("usuario: ", False, True)
                password = tools.iinput("password: ", False, True)
            except KeyboardInterrupt:
                print()
                return False

            if user == self.game.mission.user and \
               password == self.game.mission.password:
                return True

            print("Logueo incorrecto.")


class Command(object):
    name = ""
    description = ""
    parameters = []
    condition = (lambda cli: True, "")

    @classmethod
    def minimum_parameters(cls):
        # !!!: It seems this can't be a property for some reason.
        #      Probably because it's a classmethod...?
        optional = 0
        for parameter in cls.parameters:
            optional += parameter[0] == "["
        return len(cls.parameters) - optional

    @classmethod
    def print_help(cls):
        print("{}{}".format(cls.name.ljust(10, "."), cls.description))

    @classmethod
    def print_syntax(cls):
        print("sintaxis:")
        print(" ".join([cls.name] + cls.parameters))

    @classmethod
    def print_msg(cls, *error):
        print("{}: {}".format(cls.name, " ".join(error)))

    @classmethod
    def try_to_run(cls, cli, args):
        if "/?" in args:
            cls.print_help()
            return

        if not cls.condition[0](cli):
            cls.print_msg(cls.condition[1])
            return

        if not cls.minimum_parameters() <= len(args) <= len(cls.parameters):
            cls.print_syntax()
            return
        cls.run(cli, args)

    @classmethod
    def run(cls, cli, args):
        raise(NotImplementedError)


@CLI.command
class cmd_help(Command):
    name = "help"
    description = "Muestra la ayuda de todos los comandos."
    parameters = []

    @classmethod
    def run(cls, cli, args):
        for name in sorted(cli.commands):
            cli.commands[name].print_help()


@CLI.command
class cmd_dir(Command):
    name = "dir"
    description = "Muestra el contenido del directorio actual."
    parameters = ["[DIRECTORIO]"]

    @classmethod
    def run(cls, cli, args):
        if len(args) == 1:
            dirlist = system.abs_dirlist(cli.dirlist[:],
                                         tools.fix_slashes(args[0]).
                                         split(os.path.sep))
        else:
            dirlist = cli.dirlist[:]

        try:
            elements = cli.system.listdir(dirlist)
        except KeyError:
            cls.print_msg("archivo o directorio no encontrado:", args[0])
            return
        except AttributeError:
            cls.print_msg("no es un directorio:", args[0])
            return

        directories = [directory[0] for directory in elements
                       if not isinstance(directory[1], File)]
        files = [directory[0] for directory in elements
                 if isinstance(directory[1], File)]

        print()
        if dirlist != cli.dirlist:
            print("    Directorio de:", tools.format_dirlist(dirlist))
            print()
        for directory in sorted(directories):
            print("{0:32} {1}".format(directory, "<DIR>"))
        for file_ in sorted(files):
            print(file_)
        print()
        print("   ", len(files), "archivo(s).")
        print("   ", len(directories), "directorio(s).")
        print()


@CLI.command
class cmd_cd(Command):
    name = "cd"
    description = "Cambia el directorio actual."
    parameters = ["[DIRECTORIO]"]

    @classmethod
    def run(cls, cli, args):
        if len(args) == 0:
            print(cli.pwd)
            return

        dirlist = system.abs_dirlist(cli.dirlist[:],
                                     tools.fix_slashes(args[0]).
                                     split(os.path.sep))

        if cli.system.is_file(dirlist):
            cls.print_msg("no es un directorio:", args[0])
        elif not cli.system.is_directory(dirlist):
            cls.print_msg("archivo o directorio no encontrado:", args[0])
        else:
            cli.dirlist = dirlist


@CLI.command
class cmd_del(Command):
    name = "del"
    description = "Borra el archivo o directorio dado."
    parameters = ["ARCHIVO/DIRECTORIO"]
    # TODO: Remove this constraint.
    condition = (lambda cli: not cli.system.is_local,
                 "no podés borrar cosas de tu propio sistema")

    @classmethod
    def run(cls, cli, args):
        dirlist = system.abs_dirlist(cli.dirlist[:],
                                     tools.fix_slashes(args[0]).
                                     split(os.path.sep))
        try:
            system.delete(dirlist)
        except KeyError:
            cls.print_msg("archivo o directorio no encontrado:", args[0])
            return

        cls.print_msg("ok")

        if not cli.system.is_directory(cli.dirlist):
            cls.print_error("el directorio actual fue borrado, "
                            "volviendo a la raíz")
            cli.dirlist = cli.dirlist[:1]


@CLI.command
class cmd_ping(Command):
    name = "ping"
    description = "Comprueba mediante ping si un host está online."
    parameters = ["HOST"]

    @classmethod
    def run(cls, cli, args):
        ip = args[0]
        valid = ip in cli.game.valid_hosts
        print()
        print("Haciendo ping a {} con 32 bytes de datos:".format(ip))
        print()
        for i in range(4):
            time.sleep(.5)
            if valid:
                print("Respuesta desde {}: bytes=32 tiempo<1m TTL=64".
                      format(ip))
            else:
                print("Tiempo de espera agotado para esta solicitud.")
        print()
        print("Estadísticas de ping para {}:".format(ip))
        print("    Paquetes: enviados = 4, recibidos = {}, perdidos = {}".
              format(valid * 4, 4 - valid * 4))
        print("    ({}% perdidos),".format(100 - valid * 100))
        print()


@CLI.command
class cmd_telnet(Command):
    name = "telnet"
    description = "Inicializa una sesión telnet con un host."
    parameters = ["HOST", "[PUERTO]"]
    condition = (lambda cli: cli.system.is_local,
                 "ya hay una sesión telnet iniciada")

    @classmethod
    def run(cls, cli, args):
        host = args[0]
        port = args[1] if len(args) > 1 else 23
        print("Conectándose a {}".format(host), end="", flush=True)
        #time.sleep(1.5)
        for i in range(3):
            print(".", end="", flush=True)
            #time.sleep(1.5)
        print()

        if host != cli.game.mission.system.ip or \
           port != cli.game.mission.port:
            cls.print_msg("no se puede abrir la conexión al host, "
                          "en puerto {}".format(port))
            return

        cli.clear()
        for i in range(random.randint(10000, 30000)):
            print(random.randint(0, 1), end=" ", flush=True)
            time.sleep(0.00001)
        print()
        cli.game.telnet_start()


@CLI.command
class cmd_cls(Command):
    name = "cls"
    description = "Borra el texto en la pantalla."
    parameters = []

    @classmethod
    def run(cls, cli, args):
        cli.clear()


@CLI.command
class cmd_dl(Command):
    name = "dl"
    description = "Descarga un archivo durante una sesión de telnet."
    parameters = ["ARCHIVO"]
    condition = (lambda cli: not cli.system.is_local,
                 "no estás en una sesión telnet")

    @classmethod
    def run(cls, cli, args):
        DOWNLOAD_TIME = 4
        DOWNLOAD_STEPS = 20

        dirlist = system.abs_dirlist(cli.dirlist[:],
                                     tools.fix_slashes(args[0]).
                                     split(os.path.sep))

        try:
            file_ = cli.system.retrieve(dirlist)
        except KeyError:
            cls.print_msg("archivo o directorio no encontrado:", args[0])
            return
        if not isinstance(file_, File):
            cls.print_msg("no es un archivo:", args[0])
            return

        print("Descargando...")
        print(".{}.".format(" " * DOWNLOAD_STEPS))
        print(" ", end="")
        for i in range(DOWNLOAD_STEPS):
            print("¯", end="", flush=True)
            time.sleep(DOWNLOAD_TIME / DOWNLOAD_STEPS)
        print()

        cli.game.mission.downloads.append(file_)


@CLI.command
class cmd_ul(Command):
    name = "ul"
    description = "Sube un archivo durante una sesión telnet."
    parameters = ["ARCHIVO"]
    condition = (lambda cli: not cli.system.is_local,
                 "no estás en una sesión telnet")

    @classmethod
    def run(cls, cli, args):
        UPLOAD_TIME = 4
        UPLOAD_STEPS = 20

        dirlist = system.abs_dirlist([], tools.fix_slashes(args[0]).
                                     split(os.path.sep))

        try:
            file_ = cli.game.system.retrieve(dirlist)
        except KeyError:
            cls.print_msg("archivo o directorio no encontrado:", args[0])
            return
        if not isinstance(file_, File):
            cls.print_msg("no es un archivo:", args[0])
            return

        print("Subiendo...")
        print(".{}.".format(" " * UPLOAD_STEPS))
        print(" ", end="")
        for i in range(UPLOAD_STEPS):
            print("¯", end="", flush=True)
            time.sleep(UPLOAD_TIME / UPLOAD_STEPS)
        print()

        directory = cli.system.retrieve(cli.dirlist)
        directory[dirlist[-1]] = file_


@CLI.command
class cmd_info(Command):
    name = "info"
    description = "Muestra información sobre el juego."
    parameters = []

    @classmethod
    def run(cls, cli, args):
        info.print_info()


@CLI.command
class cmd_mail(Command):
    name = "mail"
    description = "Muestra el último e-mail recibido."
    parameters = []

    @classmethod
    def run(cls, cli, args):
        if not cli.system.is_local:
            cls.print_msg("no hay e-mails nuevos")
            print()
            return

        email = cli.game.mission.email
        print(" " + "_" * (common.TERM_WIDTH - 2))
        print("|{}|".format("De: {} ({})".
                            format(email.sender, email.sender_email).
                            center(common.TERM_WIDTH - 2)))
        print("|" + "-" * (common.TERM_WIDTH - 2) + "|")
        print("|{}|".format("Asunto: {}".format(email.subject).
                            center(common.TERM_WIDTH - 2)))
        print(" " + "¯" * (common.TERM_WIDTH - 2))
        print(tools.formatted(email.message, common.TERM_WIDTH))
        print("-" * common.TERM_WIDTH)


@CLI.command
class cmd_dc(Command):
    name = "dc"
    description = "Termina una sesión de telnet."
    parameters = []
    condition = (lambda cli: not cli.system.is_local,
                 "no estás en una sesión telnet")

    @classmethod
    def run(cls, cli, args):
        cli.game.telnet_end()


@CLI.command
class cmd_save(Command):
    name = "save"
    description = "Guarda la partida."
    parameters = []
    condition = (lambda cli: cli.system.is_local,
                 "no es posible guardar durante una misión")

    @classmethod
    def run(cls, cli, args):
        cli.game.save()
        cls.print_msg("partida guardada correctamente")


@CLI.command
class cmd_track(Command):
    name = "track"
    description = ""
    parameters = []

    @classmethod
    def run(cls, cli, args):
        pass


@CLI.command
class cmd_ipconfig(Command):
    name = "ipconfig"
    description = "Muestra tu configuración de IP."
    parameters = []

    @classmethod
    def run(cls, cli, args):
        print()
        print("Configuración IP:")
        print()
        print("        Sufijo de conexión específica DNS :")
        print("        Dirección IP. . . . . . . . . . . :", cli.system.ip)
        print("        Máscara de subred . . . . . . . . : 255.255.255.255")
        print("        Puerta de enlace predeterminada . :", cli.system.ip)
        print()


@CLI.command
class cmd_alias(Command):
    name = "alias"
    description = "Crea un alias a un comando."
    parameters = ["[NOMBRE]", "[COMANDO]"]

    @classmethod
    def run(cls, cli, args):
        if len(args) == 0:
            for name, command in sorted(cli.game.aliases.items()):
                print("{}='{}'".format(name, command))
            return

        if len(args) == 1:
            if args[0] not in cli.game.aliases:
                cls.print_msg("alias no encontrado:", args[0])
                return
            print("{}='{}'".format(args[0], cli.game.aliases[args[0]]))
            return

        cli.game.aliases[args[0]] = " ".join(args[1:])
        cls.print_msg("ok")


@CLI.command
class cmd_unalias(Command):
    name = "unalias"
    description = "Elimina un alias."
    parameters = ["NOMBRE"]

    @classmethod
    def run(cls, cli, args):
        try:
            del cli.game.aliases[args[0]]
        except KeyError:
            cls.print_msg("alias no encontrado:", args[0])
        else:
            cls.print_msg("ok")
