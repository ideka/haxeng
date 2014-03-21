#       Copyright 2010, 2014 Gerardo Marset <gammer1994@gmail.com>
#
#       This file is part of Haxxor Engine.
#
#       system.py is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       system.py is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with system.py; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sys
import os.path
import random
import time

from filesystem import File
import tools

DEBUG = True
TERM_WIDTH = 79


class CLI(object):
    commands = {}

    def __init__(self, system, game):
        self._system = None

        self.dirlist = []

        self.system = system
        self.game = game

    @staticmethod
    def command(cmd):
        CLI.commands[cmd.__name__[4:]] = cmd

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
            self.commands[args[0]](self, args[1:])
        else:
            print("betch: comando desconocido: {}".format(args[0]))

    def prompt(self):
        try:
            self.parse_input(tools.iinput(self.pwd + ">"))
        except EOFError:
            print()
            if DEBUG or tools.yn("¿Seguro que querés salir?", False):
                self.game.running = False
        except Exception as e:
            if DEBUG:
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
    syntax = ""
    number_of_arguments = []

    @classmethod
    def print_help(cls):
        print("{}: {}".format(cls.name, cls.description))

    @classmethod
    def try_to_run(cls, cli, args):
        if "/?" in args:
            cls.print_help()
            return
        if cls.number_of_arguments == [] or \
           len(args) not in cls.number_of_arguments:
            cls.print_syntax()
            return
        cls.run(cli, args)

    @classmethod
    def run(cls, cli, args):
        raise(NotImplementedError)


@CLI.command
def cmd_help(cli, args):
    if "/?" in args:
        print("help:      Muestra la ayuda de todos los comandos.")
        return

    for command in cli.commands.values():
        command(cli, ["/?"])


@CLI.command
def cmd_dir(cli, args):
    if "/?" in args:
        print("dir:       Muestra el contenido del directorio actual.")
        return
    if len(args) > 1:
        print("sintaxis:")
        print("dir [DIRECTORIO]")
        return

    if len(args) == 1:
        dirlist = cli.system.abs_dirlist(cli.dirlist[:],
                                         tools.fix_slashes(args[0]).
                                         split(os.path.sep))
    else:
        dirlist = cli.dirlist[:]

    elements = cli.system.listdir(dirlist)
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
def cmd_cd(cli, args):
    if len(args) == 0:
        print(cli.pwd)
        return
    if "/?" in args:
        print("cd:        Cambia el directorio actual.")
        return
    if len(args) > 1:
        print("sintaxis:")
        print("cd DIRECTORIO")
        return

    relative_dirlist = tools.fix_slashes(args[0]).split(os.path.sep)
    dirlist = cli.system.abs_dirlist(cli.dirlist[:], relative_dirlist)

    if cli.system.is_file(dirlist):
        print("cd: no es un directorio:", args[0])
    elif not cli.system.is_directory(dirlist):
        print("cd: archivo o directorio no encontrado:", args[0])
    else:
        cli.dirlist = dirlist


@CLI.command
def cmd_del(cli, args):
    if "/?" in args:
        print("del:       Borra el archivo o directorio dado.")
        return
    if len(args) != 1:
        print("sintaxis:")
        print("del ARCHIVO/DIRECTORIO")
        return

    # TODO: Remove this constraint.
    if not DEBUG and cli.system.is_local:
        print("del: no podés borrar cosas de tu propio sistema")
        return

    relative_dirlist = tools.fix_slashes(args[0]).split(os.path.sep)

    try:
        cli.system.delete(cli.system.abs_dirlist(cli.dirlist[:],
                                                 relative_dirlist))
    except KeyError:
        print("del: archivo o directorio no encontrado:", args[0])
        return

    print("del: ok")

    if not cli.system.is_directory(cli.dirlist):
        print("del: el directorio actual fue borrado, volviendo a la raíz")
        cli.dirlist = cli.dirlist[:1]


@CLI.command
def cmd_ping(cli, args):
    if "/?" in args:
        print("ping:      Comprueba mediante ping si un host está online.")
        return
    if len(args) != 1:
        print("sintaxis:")
        print("ping HOST")
        return

    ip = args[0]
    valid = ip in cli.game.valid_hosts
    print()
    print("Haciendo ping a {} con 32 bytes de datos:".format(ip))
    print()
    for i in range(4):
        time.sleep(.5)
        if valid:
            print("Respuesta desde {}: bytes=32 tiempo<1m TTL=64".format(ip))
        else:
            print("Tiempo de espera agotado para esta solicitud.")
    print()
    print("Estadísticas de ping para {}:".format(ip))
    print("    Paquetes: enviados = 4, recibidos = {}, perdidos = {}".
          format(valid * 4, 4 - valid * 4))
    print("    ({}% perdidos),".format(100 - valid * 100))
    print()


@CLI.command
def cmd_telnet(cli, args):
    if "/?" in args:
        print("ping:      Comprueba mediante ping si un host está online.")
        return
    if len(args) == 0 or len(args) > 2:
        print("sintaxis:")
        print("telnet HOST [PUERTO]")
        return

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
        print("telnet: no se puede abrir la conexión al host, en puerto {}".
              format(port))
        #return

    cli.clear()
    for i in range(random.randint(10000, 30000)):
        print(random.randint(0, 1), end=" ", flush=True)
        time.sleep(0.00001)
    print()
    cli.game.telnet_start()


@CLI.command
def cmd_cls(cli, args):
    if "/?" in args:
        print("cls:       Borra el texto en la pantalla.")
        return

    cli.clear()


@CLI.command
def cmd_dl(cli, args):
    if "/?" in args:
        print("dl:        Descarga un archivo durante una sesión de telnet.")
        return
    if len(args) != 1:
        print("sintaxis:")
        print("dl ARCHIVO")
        return


@CLI.command
def cmd_ul(cli, args):
    pass


@CLI.command
def cmd_info(cli, args):
    pass


@CLI.command
def cmd_mail(cli, args):
    if "/?" in args:
        print("mail:      Muestra el último e-mail recibido.")
        return
    if not cli.system.is_local:
        print("mail: no hay e-mails nuevos")
        print()
        return

    email = cli.game.mission.email
    print(" " + "_" * (TERM_WIDTH - 2))
    print("|{}|".format("De: {} ({})".
                        format(email.sender, email.sender_email).
                        center(TERM_WIDTH - 2)))
    print("|" + "-" * (TERM_WIDTH - 2) + "|")
    print("|{}|".format("Asunto: {}".
                        format(email.subject).center(TERM_WIDTH - 2)))
    print(" " + "¯" * (TERM_WIDTH - 2))
    print(tools.formatted(email.message, TERM_WIDTH))
    print("-" * TERM_WIDTH)


@CLI.command
def cmd_dc(cli, args):
    if "/?" in args:
        print("dc:        Termina una sesión de telnet.")
        return

    if cli.system.is_local:
        print("dc: no estás en una sesión de telnet")
        return

    cli.game.telnet_end()


@CLI.command
def cmd_save(cli, args):
    if "/?" in args:
        print("save:      Guarda la partida.")
        return

    cli.game.save()
    print("save: partida guardada correctamente")


@CLI.command
def cmd_track(cli, args):
    pass


@CLI.command
def cmd_ipconfig(cli, args):
    if "/?" in args:
        print("ipconfig:  Muestra tu configuración de IP.")
        return
    ip = cli.system.ip

    print()
    print("Configuración IP:")
    print()
    print("        Sufijo de conexión específica DNS :")
    print("        Dirección IP. . . . . . . . . . . :", ip)
    print("        Máscara de subred . . . . . . . . : 255.255.255.255")
    print("        Puerta de enlace predeterminada . :", ip)
    print()


@CLI.command
def cmd_alias(cli, args):
    if "/?" in args:
        print("alias:     Crea un alias a un comando.")
        return
    if len(args) == 1:
        print("sintaxis:")
        print("alias NOMBRE COMANDO")
        return
    if len(args) == 0:
        for name, command in sorted(cli.game.aliases.items()):
            print("{}='{}'".format(name, command))
        return

    cli.game.aliases[args[0]] = " ".join(args[1:])
    print("alias: ok")


@CLI.command
def cmd_unalias(cli, args):
    if "/?" in args:
        print("unalias:   Elimina un alias.")
        return
    if len(args) != 1:
        print("sintaxis:")
        print("unalias NOMBRE")
        return

    try:
        del cli.game.aliases[args[0]]
    except KeyError:
        print("unalias: alias no encontrado:", args[0])
    else:
        print("unalias: ok")
