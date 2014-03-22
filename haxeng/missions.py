# {{{   Copyright 2010, 2014 Gerardo Marset <gammer1994@gmail.com>
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
# }}}

from enum import Enum
from filesystem import File, FileSpawner
from mission import Mission, Objective
from email import EMail


FileID = Enum(
    "virus_idk",
    "telnet_log",
    "c23",
    "tajo1",
    "tajo2",
    "tajo3",
    "trojan_client_v3",
    "inst",
    "info_vip",
    "hash_md5",
    "bnc_hacker",
    "redek_profile"
)


missions = (
# {{{ Mission 0
    Mission(
        EMail(
            "Holas :)",
            "Ideka",
            "ideka@ideka.web",
            """Hola, {name}.
Vos no me conocés, pero yo a vos si te conozco muy bien. Sé que acabás de volver de la prisión.
Seguro no lo sabés, pero sos un hacker, uno de los mejores, y aunque te soltaron rápido porque fue la primera vez que te atraparon hackeando a alguien (y no hiciste más que robar un par de archivos), la información que robaste era confidencial, por lo que te lavaron el cerebro y te borraron la memoria. Me tenés que creer, porque eras el mejor hacker de L33tC0re, nuestra organización, y si no te recuperamos, no sé si vamos a poder conseguir esa información devuelta ya que hace un rato hackeé tu PC y la información no está ahí, seguramente fue borrada.
Por eso, me encargaron a mí para que recupere tu memoria, y no pienso fallar.

Muy bien {name}, ¿listo para ownear?
Tengo un servidor en casa que ya no uso; que quiero que lo hackees. Cuando estés dentro, quiero que descargues el archivo virus_idk.exe, que está en el directorio Proyectos. Es el ejecutable de mi primer virus, estoy orgulloso de él XD.
Acá te dejo información que vas a necesitar:
La IP de mi servidor: {remote_ip}
Un puerto que acabo de abrir para que puedas entrar: {port}
Mi nombre de usuario: {user}
Y mi password: {password}
Para poder entrar tenés que usar telnet con la IP y el puerto:
telnet {remote_ip} {port}
Después, si todo fue bien, te van a pedir un usuario y un password, poné los que te dí. También podés escribir dc para desconectarte del servidor.
Cuando hayas hecho eso vas a estar adentro de mi servidor. Lo que tenés que hacer es usar el comando dir para que te muestre todos los archivos y directorios. Después tenés que usar cd con el directorio proyectos, así:
cd Proyectos
Con eso vas a haber entrado al directorio proyectos. Ahí volvé a usar dir para comprobar que el archivo virus_idk.exe está ahí, y después bajalo con el comando dl:
dl virus_idk.exe
Cuando termines podés desconectarte con el comando dc. Por cierto, para ir al directorio anterior tenés que escribir "cd..".
Una última cosa. Mientras estés en mi computadora, o cualquier otra que no sea la tuya, vas a ser rastrado. O mejor dicho, tu IP va a ser rastrada. Usá el comando track para ver como va el rastreo de tu IP. Cuando lo hagas se va a mostrar una IP, cuanto más parecida sea esta IP a tu IP, menos tiempo va a faltar para que te atrapen. Por ahora no te preocupes demasiado, deberían tardar mucho en atraparte esta vez porque la seguridad de ese servidor es pésima, pero por las dudas usá track de vez en cuando y desconectate si pensás que te van a atrapar. Si no sabés tu IP, es esta: {local_ip}. También podés usar el comando ipconfig para verla cuando estés en tu PC.
Bueno, creo que eso es todo. ¡Suerte, {name}!

    -Ideka :)"""
        ),
        " @@@@    @@@@@@@@@@         @@@@@@@@@@@@   @@@@     @@@@           @@@\n"
        " @@@@    @@@@@@@@@@@@@@     @@@@@@@@@@@@   @@@@    @@@@           @@@@@\n"
        " @@@@    @@@@       @@@@    @@@@           @@@@  @@@@@           @@@@@@@\n"
        " @@@@    @@@@        @@@@   @@@@           @@@@ @@@@            @@@@ @@@@\n"
        " @@@@    @@@@        @@@@   @@@@@@@@@@@@   @@@@@@@@@           @@@@   @@@@\n"
        " @@@@    @@@@        @@@@   @@@@           @@@@ @@@@@         @@@@     @@@@\n"
        " @@@@    @@@@       @@@@    @@@@           @@@@   @@@@@      @@@@@@@@@@@@@@@\n"
        " @@@@    @@@@@@@@@@@@@@     @@@@@@@@@@@@   @@@@    @@@@@    @@@@         @@@@\n"
        " @@@@    @@@@@@@@@@         @@@@@@@@@@@@   @@@@      @@@@@ @@@@           @@@@\n"
        "                             Knows what he's doing",
        {
            "C:": {
                "WINDOWS": {
                    "windows.sys": File()
                },
                "telnet": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 4)
                },
                "Python-2.3.6": {
                    "setup.py": File(),
                    ".cvsignore": File(),
                    "aclocal.m4": File(),
                    "configure.in": File(),
                    "makefile.pre.in": File(),
                    "pyconfig.h.in": File(),
                    "www.python.org": File()
                },
                "Proyectos": {
                    "virus_idk.py": File(),
                    "virus_idk.exe": File(FileID.virus_idk),
                    "Z:EEDD.gmd": File()
                },
                "autorun.bat": File(),
                "options.ini": File()
            }
        },
        {
            FileID.virus_idk: Objective.download
        },
        1
    ),
# }}}

# {{{ Mission 1
    Mission(
        EMail(
            "Muy bien :)",
            "Ideka",
            "ideka@ideka.web",
            """Genial, {name}, sabía que podías hacerlo :). Espero que estés recuperando tus habilidades.
Tengo otro trabajito para vos. Deberías tener el archivo virus_idk.exe en tu PC, en el directorio Descargas. Quiero que entres a la PC de mi vecino y lo subas, que le hace falta disciplina a ese tipo. Siempre anda haciendo quilombo, se reune con un montón de gente y cantan canciones raras de "cerveza melorto" o algo así y... bueno, mejor no sigo.
El virus_idk.exe está programado para arrancar al momento en el que te desconectes.
Te dejo la información necesaria:
IP      : {remote_ip}
Puerto  : {port}
Usuario : {user}
Password: {password}
Para subir el archivo tenés que usar el comando ul, así:
ul C:\\Descargas\\virus_idk.exe
Por cierto, MUY IMPORTANTE, es IMPERATIVO que también borres el archivo {local_ip} en el directorio telnet con el comando "del". Cuando entrás a un servidor por telnet, un archivo se crea en el directorio de logs de telnet con el nombre de tu IP. Si no lo borrás antes de desconectarte, vas a ser atrapado. NO BORRES EL DIRECTORIO ENTERO, eso sería muy obvio y te encontrarían, borrá solo el archivo {local_ip}. La vez pasada no importó porque era mi propia PC y yo no te voy a delatar, pero de ahora en adelante hacelo siempre que no se te diga lo contrario.

    -Ideka :)"""
        ),
        "............            ...........            ...........            .........\n"
        "..@@@@@@@..@@@     @@@@@@..........            ...........            .........\n"
        "...@@.......@@      @@  @@...@@@...         @@@........... @@@@    @@@...@@@...\n"
        "...@@@@@....@@      @@@@@@....@@@..@ @@@     @@@...@.@@...@  @@   @@  .@@...@@.\n"
        "...@@.......@@      @@  @@..@@..@.. @@ @@  @@  @...@@.@@..@@@     @@  .@@...@@.\n"
        "..@@@@@@@...@@     @@@@@@...@@@@@@. @@ @@  @@@@@@..@@.@@.. @@@@@  @@  ...@@@...\n"
        "            ............           ............           ............\n"
        "            ............           ............           ............\n"
        "            ............           ..........@@@          ............\n"
        "            ........@@@.   @@@   @@@.@@@.......    @@@    ............\n"
        "            .......@@@.. @@   @@  @...@......@@@ @@   @@  ............\n"
        "............         @@@.@@...@@...@@@        @@.@@...@@...            ........\n"
        "............       @@@  ...@@@..... @         @@...@@@.....            ........\n"
        "............            ..........@@           ............            ........\n"
        "............            ...........            ............            ........",
        {
            "E:": {
                "WIDNOWS": {
                    "windows.sys": File()
                },
                "telnet": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 4)
                },
                "web": {
                    "videos": {
                        "sofanatico.wmv": File(),
                        "ricardo.wmv": File(),
                        "megapanza.wmv": File()
                    },
                    "index.html": File()
                },
                "VC_RED.MSI": File()
            }
        },
        {
            FileID.telnet_log: Objective.delete,
            FileID.virus_idk: Objective.upload
        },
        1
    ),
# }}}

# {{{ Mission 2
    Mission(
        EMail(
            "¡Lo lograste!",
            "Ideka",
            "ideka@ideka.web",
            """Veo que lo lograste, {name}. A ver si empieza a ahorrar para reparar el daño y se deja de joder ese pesado.
Bueno, {name}, te va a alegrar saber que te reincorporé en la lista de hackers de la organización, lo que significa que volvés a ser un hacker oficial de L33tC0re y por lo tanto puede que personas que no conozcas te contacten pidiéndote ayuda, y ayudándolos vas a recuperar tu memoria más rápido. El primer trabajo te lo voy a dar yo :).
Mirá, resulta que tengo que hacer una tarea de C++ y entregarla mañana, pero la verdad prefiero usar el tiempo siguiendo con otros proyectos más importantes que los del colegio, así que te voy a pedir que entres en la PC de un compañero de clase y le robes la tarea. Vas a tener que buscarla porque no sé donde la tiene guardada, pero sé que el nombre del archivo es algo así como "C23.cpp" ó "C23.c".
El tío tiene IP dinámica, la actual podría ser cualquiera de estas:
{random_ip}
{random_ip}
{remote_ip}
{random_ip}
Para encontrar la IP correcta lo recomendable sería usar ping, así:
ping 127.0.0.1
(Esa es una IP de ejemplo.)
Hacé ping con todas hasta que encuentres la correcta. El puerto es definitivamente {port}, estoy seguro de que ese está abierto.
El usuario y la password son {user} y {password}.
Suerte, y no te olvides de borrar el log de telnet.

    -Ideka :)"""
        ),
        "       @@@@@@@@@@@@@@                     @@@@@@@@@@@@@@\n"
        "    @@@              @@@               @@@              @@@\n"
        "  @@@                  @@@  .ooooo.  @@@                  @@@\n"
        "@@@                     @@@O       O@@@                     @@@\n"
        "@@                       @@         @@                       @@\n"
        "@@                       @@         @@                       @@\n"
        "@@@                     @@@         @@@                     @@@\n"
        " @@@                   @@@           @@@                   @@@\n"
        "   @@@               @@@               @@@               @@@\n"
        "      @@@@@@@@@@@@@@@     Nerd Powah!     @@@@@@@@@@@@@@@",
        {
            "C:": {
                "WIN": {
                    "windows.sys": File(),
                    "regedit.exe": File(),
                    "cmd.exe": File(),
                    "NOTEPAD.EXE": File(),
                    "system.ini": File()
                },
                "telnet": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 5)
                },
                "colegio": {
                    "foto2k1.jpg": File(),
                    "foto2k2.jpg": File(),
                    "foto2k3.jpg": File(),
                    "foto2k4.jpg": File(),
                    "foto2k5.jpg": File(),
                    "foto2k6.jpg": File(),
                    "foto2k7.jpg": File(),
                    "foto2k8.jpg": File(),
                    "foto2k9.jpg": File()
                },
                "Dev-Cpp": {
                    "Projects": {
                        "C22.cpp": File(),
                        "C20.cpp": File(),
                        "build.bat": File(),
                        "clean.bat": File(),
                        "Makefule.ntf": File(),
                        "C21.cpp": File(),
                        "C23.c": File(FileID.c23)
                    },
                    "template": {
                        "clean.bat": File(),
                        "build.bat": File(),
                        "Makefile.ntf": File()
                    },
                    "Dev-Cpp.exe": File()
                }
            }
        },
        {
            FileID.telnet_log, Objective.delete,
            FileID.c23, Objective.download
        },
        1
    ),
# }}}

# {{{ Mission 3
    Mission(
        EMail(
            "Hey",
            "Yacko",
            "yacko@coldmail.web",
            """Hola, {name}. Anduve buscando buenos hackers y parece que vos sos lo suficientemente bueno.
Mirá, mi banda favorita, Tajo, va a sacar un nuevo álbum en unos meses, pero los boludos lo podrían sacar mucho antes si quisieran porque está casi completo, pero quieren más tiempo para hacer publicidad y esas cosas. Sé que los tipos están en el estudio de grabación ahora mismo, así que antes de que se vayan, podés obtener las canciones que lleven y tengan terminadas.
La IP del estudio es {remote_ip} y el otro día abrí el puerto {port}, espero que no se hayan dado cuenta. Podés loguearte con mi usuario {user} y mi password {password}. Yo no sé nada de hacking, pero te pido que no dejes huellas porque si no nos cagan a los dos."""
        ),
        "           @@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@\n"
        "           @@##############@@@@                @@@@##############@@\n"
        "           @@##############@@ @@              @@ @@##############@@\n"
        "           @@##############@@  @@            @@  @@##############@@\n"
        "           @@##############@@   @@          @@   @@##############@@\n"
        "           @@     ____     @@    @@        @@    @@     ____     @@\n"
        "           @@    /    \    @@    @@        @@    @@    /    \    @@\n"
        "           @@    | () |    @@    @@@@@@@@@@@@    @@    | () |    @@\n"
        "           @@    \____/    @@    @ @@[]|>@@ @    @@    \____/    @@\n"
        "           @@              @@  ,/  @@()||@@  \.  @@              @@\n"
        "           @@@@@@@@@@@@@@@@@@o´    @@@@@@@@    `o@@@@@@@@@@@@@@@@@@",
        {
            "C:": {
                "Audacity": {
                    "audacity.exe": File(),
                    "unins000.exe": File(),
                    "unins000.dat": File()
                },
                "pnp": {
                    "Tajo_PuebloPodrido.mp3": File(FileID.tajo1),
                    "Tajo_YALCDD.mp3": File(FileID.tajo2),
                    "Tajo_NSLatinos.mp3": File(FileID.tajo3)
                },
                "tuxguitar-1.0": {
                    "tuxguitar.exe": File(),
                    "msvcr.dll": File(),
                    "tuxguitar.bat": File(),
                    "bttr.thn": File(),
                    "gtr.pro": File()
                },
                "logs": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 6)
                },
                "windows.sys": File()
            }
        },
        {
            FileID.telnet_log, Objective.delete,
            FileID.tajo1, Objective.download,
            FileID.tajo2, Objective.download,
            FileID.tajo3, Objective.download
        },
        3
    ),
# }}}

# {{{ Mission 4
    Mission(
        EMail(
            "Algo grande",
            "Ideka",
            "ideka@ideka.web",
            """¿Qué hay, {name}? ¿Ya anduviste haciendo trabajos para otras personas? Es hora de hacer algo grande, {name}. Hasta ahora todo lo que hiciste fueron cosas menores, esta vez vamos a hacer algo muy interesante. Primero que nada, vas a tener que entrar a mi PC y llevarte un archivo. Te dejo los datos:
IP      : {remote_ip}
Puerto  : {port}
Usuario : {user}
Password: {password}
No te preocupes, voy a minimizar la seguridad y eso, no deberías tener ni un sólo problema. El archivo que necesitás es trojan_client_V3.exe, acordate bien del nombre. Es otro virus que yo creé. También vas a necestiar el archivo inst.py, no te olvides. Bajá esos dos archivos y desconectate, no tenés que borrar los logs.
Cuando termines esperá a más instrucciones.

    -Ideka :)"""
        ),
        " @@@@    @@@@@@@@@@         @@@@@@@@@@@@   @@@@     @@@@           @@@\n"
        " @@@@    @@@@@@@@@@@@@@     @@@@@@@@@@@@   @@@@    @@@@           @@@@@\n"
        " @@@@    @@@@       @@@@    @@@@           @@@@  @@@@@           @@@@@@@\n"
        " @@@@    @@@@        @@@@   @@@@           @@@@ @@@@            @@@@ @@@@\n"
        " @@@@    @@@@        @@@@   @@@@@@@@@@@@   @@@@@@@@@           @@@@   @@@@\n"
        " @@@@    @@@@        @@@@   @@@@           @@@@ @@@@@         @@@@     @@@@\n"
        " @@@@    @@@@       @@@@    @@@@           @@@@   @@@@@      @@@@@@@@@@@@@@@\n"
        " @@@@    @@@@@@@@@@@@@@     @@@@@@@@@@@@   @@@@    @@@@@    @@@@         @@@@\n"
        " @@@@    @@@@@@@@@@         @@@@@@@@@@@@   @@@@      @@@@@ @@@@           @@@@\n"
        "                                  Or does he?",
        {
            "C:": {
                "Python25": {
                    "python.exe": File(),
                    "pythonw.exe": File(),
                    "w9xpopen.exe": File()
                },
                "Python26": {
                    "python.exe": File(),
                    "pythonw.exe": File(),
                    "w9xpopen.exe": File(),
                    "trojan_client_V3.exe": File(FileID.trojan_client_v3),
                    "inst.py": File(FileID.inst)
                },
                "telnet_logs": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 1)
                },
                "windows.sks": File(),
                "microsoft.sks": File(),
                "autoestopista_galactico.mp4": File()
            }
        },
        {
            FileID.trojan_client_v3: Objective.download,
            FileID.inst: Objective.download
        },
        1
    ),
# }}}

# {{{ Mission 5
    Mission(
        EMail(
            "Me hackearon ):<",
            "El masi",
            "masi@hmail.web",
            """¿Que andás, {name}? ¿Sos un hacker, no? Bueno, necesito tu ayuda. Unos tipos me acaban de hackear y robaron mucha información importante. ¿Podés entrar a su PC y borrarles todo? Borrá todos los directorios, y si podés meteles algún virus que tengas para que se jodan por imbéciles.
Conseguí la siguiente información:
IP: {remote_ip}
Puerto: {port}
Usuario: {user}
Pass: {password}
ROMPELES TODO PL0X."""
        ),
        "          ................................................@@@@@@@@@@@@\n"
        "          .............................................@@@@@@@@@@@@@@@\n"
        "          ...........................................@@@   @@@@@@@@@@@\n"
        "          ........................................@@@@   @@  @@@@@@@@@\n"
        "          .....................................@@@@@@@  @   @@@ @@@@@.\n"
        "          .................................@@@@@@@@@@@@   @@@@@@@@@...\n"
        "          ..............................@@@@@@@ @@@@@@@@@  @@@@@......\n"
        "          ............................@@   @@@ O @@@@@@@@@@@..........\n"
        "          .........................@@@@@@   @@   @   @@@@@............\n"
        "          ......................@@@@@@@@@@    @     @@@...............\n"
        "          ...................@@@@@@@@@@@   @   @@@@@..................\n"
        "          ................@@@@@  @@@@@@@@@   @@@@.....................\n"
        "          .............@@@@   `   @@@@ @@@@@@@........................\n"
        "          ..........@@@@@@@@  @@@   @@@@@@@...........................\n"
        "          .......@@@@   @@@@@  @@@@@@@@@..............................\n"
        "          ....@@@@@   @@@@@@@@@  @@@@.................................\n"
        "          .@@@@@@@@   @@@  @@ @@@@....................................\n"
        "          @@@@@@@@@@      @@@@@.......................................\n"
        "          @@@@@@@@@@@@@@@@@@..........................................\n"
        "          @@@@@@@@@@@@@@@.............................................\n"
        "                            Club Nacional de Fútbol",
        {
            "C:": {
                "web": {
                    "index.html": File(),
                    "copas.html": File(),
                    "cancha.html": File(),
                    "estadio.html": File(),
                    "copas.gif": File(),
                    "estadio.gif": File(),
                    "bandera.bmp": File()
                },
                "telnet": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 7)
                },
                "programas": {
                    "gallina.exe": File(),
                    "vigilante.exe": File()
                },
                "windows": {
                    "sistema.sys": File()
                }
            }
        },
        {
            None: lambda system: system.filesystem["C:"].values() == [FileID.virus_idk]
        },
        5
    ),
# }}}

# {{{ Mission 6
    Mission(
        EMail(
            "2da parte de nuestra misión",
            "Ideka",
            "ideka@ideka.web",
            """Hola, {name}. Llegó el momento de la segunda parte de nuestra misión. No te voy a decir dónde te vas a meter ahora. No te preocupes, no creo que haya buena seguridad.
La IP es {remote_ip}, el puerto {port}, el usuario es {user} y la password {password}. Quiero que me consigas el archivo info.vip. Ese contiene el usuario y la password de nuestra siguiente víctima, por eso lo necesito, pero seguramente está encriptado, así que también necesito el archivo hash.md5 para decriptarlo.
Suerte, {name}.

    -Ideka :)"""
        ),
        "                   o@@@@@@@@@O.                    :8@@@@@8c\n"
        "               C@@@@@@@@@@@@@@@@@@.           .@@@@@@@@@@@@@@@@@o\n"
        "             @@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@\n"
        "          C@@@@@@@@@@@@@@@@@@@@@@@@@@@@  C@@@@@@@@@@@@@@@@@@@@@@@@@@@C\n"
        "         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.\n"
        "      o@@@@@@@@@@@@@@@O    @@@@@@@@@@@@@@@@@@@@@@@@@@o   8@@@@@@@@@@@@@@@8\n"
        "      O@@@@@@@@@@@@@@@     c@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@\n"
        "      c@@@@@@@@@@@@@@@@o .@@@@@@@@@@@@@@@@@@@@@@@@@@@o   O@@@@@@@@@@@@@@@8\n"
        "       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.\n"
        "       O@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "         C@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "           @@@@@@@@@@@@@@@@@@@@@@@@@@8   :@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        "             8@@@@@@@@@@@@@@@@@@@@@@ oO    :@@@@@@@@@@@@@@@@@@@@@@@\n"
        "                8@@@@@@@@@@@@@@@C   O .@:     o@@@@@@@@@@@@@@@@@:\n"
        "                       ...  @@@@@@@C 8O :@: @@@@@@@@@@oooc.\n"
        "                            @@@@@@@@@@@@@@@@@@@@@@@@@C @\n"
        "               @@@O         C@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@O\n"
        "             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@o\n"
        "             8@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@C\n"
        "              @@@@@@ @@c  @O @@@@@@@@@@@@@@@@@@@@@@@@@@@.@8:\n"
        "                Co   :    o8@@@@@@@@@@@@@@@@@@@@@@@@@@C   .\n"
        "                     O8:...:.8::@@@@@@@@@@@@@@@@@@@@OOO@@@@@@@@@\n"
        "                                @@@@@@@@@@@@@@@@@@@@\n"
        "                                @@@@@@@@@@@@@@@@@@O:\n"
        "                                  @@@@@@@@@@@@@@@o\n"
        "                              .o@@@@@@@@@@@@@@@@@@@:\n"
        "                              @@ o@@@ :@@@@@O@@@c@o\n"
        "                             O@ @@@@.  @@  @ @@@@ @@\n"
        "                            @  @@@    @@@  @@ @@@@ @\n"
        "                          c@ @@@@      @@  @8  o@@@.@\n"
        "                         C@8@@@C       @@  @@   o@@@C@c\n"
        "                        .@@@@@O        @@  @@    @@@@@@:\n"
        "                               Director Topsy Kret",
        {
            "C:": {
                "private": {
                    "thunder_axe": {
                        "gibson_les_paul.gtr": File(),
                        "jackson_randy_rhoads.gtr": File(),
                        "fender_stratocaster.gtr": File()
                    },
                    "foto1.jpg": File(),
                    "foto2.jpg": File(),
                    "foto3.jpg": File(),
                    "info.vip": File(FileID.info_vip)
                },
                "guion": {
                    "Importante": {
                        "hash.crc": File(),
                        "hash.md5": File(FileID.hash_md5),
                        "hash.wrl": File(),
                        "hash.md4": File()
                    },
                    "parte1.txt": File(),
                    "parte2.txt": File(),
                    "parte3.txt": File()
                },
                "logs": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 5)
                },
                "windows.sys": File(),
                "winold.sys": File()
            }
        },
        {
            FileID.telnet_log: Objective.delete,
            FileID.info_vip: Objective.download,
            FileID.hash_md5: Objective.download
        },
        5
    ),
# }}}

# {{{ Mission 7
    Mission(
        EMail(
            "Tirapiedrash",
            "Pako Loko",
            "zapako@yipee.web",
            """Hey, {name}.
Hace un tiempo me hackearon. Estoy seguro de quien fue, y sé que algún hacker experimentado los ayudó porque no pude recuperar la IP, pero tengo la IP de los que me hackearon, entre otras cosas. ¿Podés entrar a su PC y borrar todas las carpetas y archivos que veas como me hicieron a mi?
Acá te dejo la info:
IP: {remote_ip}
Puerto: {port}
User: {user}
Password: {password}
Ah, y si tenés algún virus, metelo para joderlos."""
        ),
        "\n"
        "             *     *     *\n"
        "                             :::::::::::::::::::::::::::::::::::::::::\n"
        "                *     *      :::::::::::::::::::::::::::::::::::::::::\n"
        "\n"
        "                   *\n"
        "                             :::::::::::::::::::::::::::::::::::::::::\n"
        "                *     *      :::::::::::::::::::::::::::::::::::::::::\n"
        "\n"
        "             *     *     *\n"
        "          ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
        "          ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
        "\n"
        "\n"
        "          ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
        "          ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
        "                             Club Atlético Peñarol",
        {
            "C:": {
                "www": {
                    "Menu": {
                        "noticias.php": File(),
                        "copas.php": File(),
                        "foro.php": File()
                    },
                    "Estilos": {
                        "penarol0.css": File(),
                        "penarol1.css": File(),
                        "penarol2.css": File(),
                        "penadoy.css": File(),
                        "lo-fi.css": File()
                    },
                    "Imagenes": {
                        "foto.jpg": File(),
                        "foto2.jpg": File(),
                        "bandera.png": File()
                    },
                    "index.php": File(),
                    "conectar.php": File(),
                    "desconectar.php": File()
                },
                "Programas": {
                    "its.a.secret.to.everybody": File()
                },
                "TelNet": {
                    "{local_ip}": File(FileID.virus_idk),
                    "*": FileSpawner("{random_ip}", 5)
                }
            }
        },
        {
            None: lambda system: system.filesystem["C:"].values() == [FileID.virus_idk]
        },
        6
    ),
# }}}

# {{{ Mission 8
    Mission(
        EMail(
            "Sigamos con nuestro asunto",
            "Ideka",
            "ideka@ideka.web",
            """Hola, {name} :). Vamos a continuar, ¿OK?
Hasta ahora no te dí ninguna explicación de qué es lo que estamos haciendo exactamente. Bueno, si hacés bien esto que te voy a pedir ahora, te informo en detalle :). No te voy a mentir, esta vez la cosa va a ser peligrosa.
Mirá, resulta que hay una banda de rock que se llama Blessed N Cursed (es en español a pesar del nombre en inglés) y dentro de poco van a sacar un álbum nuevo, llamado "Hacker". Varias canciones de ese álbum van a aparecer en el soundtrack de una película, entre ellas está un single cuyo nombre lleva el álbum, "Hacker". Necesitamos esa canción antes de que salga el álbum. No sé si Blessed N Cursed va a estar contento o no de lo que vamos a hacer, pero me importa poco, ahora sólo quiero recuperar tus habilidades y divertirme un poco en el proceso :).
Bueno, para conseguir la canción, vas a entrar en uno de los servidores de un estudio cinematográfico. La IP es {remote_ip}, el puerto {port} y gracias a los archivos que me conseguiste antes y que conseguí decriptar, estoy seguro de que el usuario es {user} y la password es {password}.

    -Ideka :)"""
        ),
        "                                                  _.·´`·._\n"
        "                                              _.·´        `.\n"
        "                                          _.·´@@@@     _.·´\n"
        "                                      _.·´      @@@@.·´\n"
        "                                  _.·´@@@@     _.·´\n"
        "                              _.·´      @@@@.·´\n"
        "                          _.·´@@@@     _.·´\n"
        "                      _.·´      @@@@.·´\n"
        "                  _.·´@@@@     _.·´\n"
        "              _.·´      @@@@.·´\n"
        "             |·_       _.·´\n"
        "             |  `·._.·´___________________________________________\n"
        "             |      `·._    @@@@@     @@@@@     @@@@@     @@@@@   |\n"
        "             |          )    @@@@@     @@@@@     @@@@@     @@@@@  |\n"
        "             |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |                                                    |\n"
        "             |____________________________________________________|",
        {
            "G:": {
                "LVD_Chuck_Norris": {
                    "Soundtrack": {
                        "placeholder.mp3": File()
                    },
                    "guion.txt": File(),
                    "escenas.ecf": File()
                },
                "Rio_D": {
                    "Soundtrack": {
                        "BNC_Shadtheif.mp3": File(),
                        "BNC_Sinfonia_Roja.mp3": File(),
                        "BNC_Hacker.mp3": File(FileID.bnc_hacker)
                    },
                    "guion.txt": File(),
                    "escenas.ecf": File()
                },
                "Pajaros_Pintados": {
                    "Soundtrack": {
                        "placeholder.mp3": File()
                    },
                    "guion.txt": File(),
                    "escenas.ecf": File()
                },
                "logs0": {
                    "*": FileSpawner("{random_ip}", 8)
                },
                "logs1": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 7)
                },
                "windows": {
                    "windows.sys": File()
                },
                "auto.bat": File()
            }
        },
        {
            FileID.telnet_log: Objective.delete,
            FileID.bnc_hacker: Objective.download
        },
        4
    ),
# }}}

# {{{ Mission 9
    Mission(
        EMail(
            "Ayuda urgente",
            "Redek",
            "k@l33tc0re.web",
            """Sos un hacker, ¿no? Necesito tu ayuda urgentemente, {name}.
Entrá a este server y borrá el archivo perfil_redek.dbt.
La IP es {remote_ip}, el puerto es {port}, el usuario {user} y la password {password}.
Es peligroso, pero por favor, necesito que lo hagas. Cuento contigo."""
        ),
        "            @@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@     @@@@@@@@@@@\n"
        "              @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@   @@@@@@@@@@@\n"
        "              @@@@@@        @@@@    @@@@@       @@@@@@     @@@@@ \n"
        "              @@@@@@   @@@   @@@    @@@@@       @@@@@      @@@@@\n"
        "              @@@@@@  @@@@          @@@@@@@@@@@@@@@@       @@@@@\n"
        "              @@@@@@@@@@@@          @@@@@@@@@@@@@@@@       @@@@@\n"
        "              @@@@@@  @@@@          @@@@@      @@@@@@@     @@@@@\n"
        "              @@@@@@   @@@          @@@@@       @@@@@@     @@@@@\n"
        "              @@@@@@                @@@@@       @@@@@@    o@@@@@o\n"
        "            @@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@\n"
        "            @@@@@@@@@@           @@@@@@@@@@@@@@@@@      @@@@@@@@@@@\n"
        "                                  [DB0042281]",
        {
            "C:": {
                "windows": {
                    "windows.sys": File(),
                    "windows.bat": File(),
                    "explorer.exe": File()
                },
                "telnet0": {
                    "*": FileSpawner("{random_ip}", 8)
                },
                "telnet1": {
                    "{local_ip}": File(FileID.telnet_log),
                    "*": FileSpawner("{random_ip}", 7)
                },
                "telnet2": {
                    "*": FileSpawner("{random_ip}", 6)
                },
                "CRIMINAL_DATABASE": {
                    "DBT.EXE": File(),
                    "perfil_usamabinladen.dbt": File(),
                    "perfil_fhadalquso.dbt": File(),
                    "perfil_criskuredara.dbt": File(),
                    "perfil_aliatwa.dbt": File(),
                    "perfil_redek.dbt": File(FileID.redek_profile),
                    "perfil_colato.dbt": File(),
                    "perfil_mughassil.dbt": File(),
                    "perfil_fazul.dbt": File(),
                    "perfil_couchet.dbt": File(),
                    "perfil_yahiye.dbt": File()
                }
            }
        },
        {
            FileID.telnet_log: Objective.delete,
            FileID.redek_profile: Objective.delete
        },
        7
    ),
# }}}

# {{{ Mission 10
    Mission(
        EMail(
            "El siguiente paso",
            "Ideka",
            "ideka@ideka.web",
            """Muy bien, {name}, veo que lo lograste, así que como te prometí, te voy a dar más información.
El troyano que descargaste de mi PC, simplemente ejecuta un código. Ese código está en el archivo inst.py que también descargaste de mi PC, y me da a mí control sobre el servidor donde se ejecuta. Lo que vas a hacer ahora, es subir al servidor que te voy a dar esos dos archivos junto con la canción "Hacker" que conseguiste antes. Después vas a tener que vovlerlo a hacer en otro servidor, y cuando termines yo voy a hacer unas cosas mediante en troyano, y el resultado va a ser la canción "Hacker" escuchándose en todas las emisoras de radio del país día y noche una y otra vez :).
El servidor al que te vas a infiltrar esta vez es de una investigación o algo así... lo que importa es que tiene instalada una radio que puede enviar ondas de amplitud modulada, y descubrí que puedo usarlo para enviar la canción "Hacker" a todas las radios AM.
La IP: {remote_ip}
El puerto: {port}
Usuario: {user}
Password: {password}

    -Ideka :)"""
        ),
        "                      @@@@@@          @@@@@@@@@@      @@@@@@@@@@\n"
        "                     o@@@@@@@           @@@@@@@@@    o@@@@@@@@\n"
        "                     @@@@@@@@@          @@@@@@@@@o   @@@@@@@@@\n"
        "                    @@@@ @@@@@@         @@@@ @@@@@  o@@@ @@@@@\n"
        "                   @@@@   @@@@@o        @@@@ @@@@@o @@@  @@@@@\n"
        "                  o@@@    @@@@@@        @@@@  @@@@@o@@@  @@@@@\n"
        "                  @@@@@@@@@@@@@@@       @@@@  @@@@@@@@   @@@@@\n"
        "                 @@@@       @@@@@@      @@@@   @@@@@@    @@@@@\n"
        "                @@@@         @@@@@o     @@@@    @@@@@    @@@@@\n"
        "              @@@@@@@@    @@@@@@@@@@@ @@@@@@@@  @@@@   @@@@@@@@@\n"
        "              @@@@@@@@    @@@@@@@@@@@ @@@@@@@@   @@@   @@@@@@@@@",
        {
            "C:": {
                "windows": {
                    "windows.sys": File(),
                    "WIN32.sys": File()
                },
                "RAM": {
                    "RAM.exe": File(),
                    "RAM.DAT": File(),
                    "unis000.dat": File(),
                    "unis000.exe": File()
                },
                "telnet": {
                    "{local_ip}": File(),
                    "{random_ip}": FileSpawner("{random_ip}", 7)
                }
            }
        },
        {
            FileID.telnet_log: Objective.delete,
            FileID.trojan_client_v3: Objective.upload,
            FileID.inst: Objective.upload,
            FileID.bnc_hacker: Objective.upload
        },
        3
    ),
# }}}

# {{{ Mission 11
    Mission(
        EMail(
            "¡El final!",
            "Ideka",
            "ideka@ideka.web",
            """Holaaaaa, {name} :DDD. Hoy estoy de muy buen humor, ¿sabés por qué? Porque hoy vamos a ownear a todas las radios del país =PP.
Como la vez anterior, lo que tenés que hacer es subir la canción, el trojan_client_V3.exe y el script inst.py.
Te dejo la info necesaria:
IP: {remote_ip}
Puerto: {port}
Usuario: {user}
Password: {password}

    -Ideka :)"""
        ),
        "                @@@@@@@@@@@@@@@@@@@   @@@@@@@@@@      @@@@@@@@@@\n"
        "                   @@@@@      @@@@@@    @@@@@@@@@    o@@@@@@@@\n"
        "                   @@@@@        @@@@    @@@@@@@@@o   @@@@@@@@@\n"
        "                   @@@@@   @@@    @     @@@@ @@@@@  o@@@ @@@@@\n"
        "                   @@@@@@@@@@@          @@@@ @@@@@o @@@  @@@@@\n"
        "                   @@@@@@@@@@@          @@@@  @@@@@o@@@  @@@@@\n"
        "                   @@@@@   @@@          @@@@  @@@@@@@@   @@@@@\n"
        "                   @@@@@   @@@          @@@@   @@@@@@    @@@@@\n"
        "                   @@@@@                @@@@    @@@@@    @@@@@\n"
        "                @@@@@@@@@@@           @@@@@@@@  @@@@   @@@@@@@@@\n"
        "                @@@@@@@@@@@           @@@@@@@@   @@@   @@@@@@@@@",
        {
            "C:": {
                "windows": {
                    "windows.sys": File(),
                    "WIN32.sys": File()
                },
                "RAM": {
                    "RAM.exe": File(),
                    "RAM.DAT": File(),
                    "unis000.dat": File(),
                    "unis000.exe": File()
                },
                "telnet": {
                    "{local_ip}": File(),
                    "*": FileSpawner("{random_ip}", 7)
                }
            }
        },
        {
            FileID.telnet_log: Objective.delete,
            FileID.trojan_client_v3: Objective.upload,
            FileID.inst: Objective.upload,
            FileID.bnc_hacker: Objective.upload
        },
        4
    ),
# }}}

# {{{ Mission X
    Mission(
        EMail(
            "SUBJECT",
            "SENDER",
            "MAIL",
            """"""
        ),
        "ASCII ART",
        {
            "C:": {
            }
        },
        {
            FileID.telnet_log: Objective.delete,
        },
        1
    ),
# }}}
)

# vim: fdm=marker
