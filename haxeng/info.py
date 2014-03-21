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
#       along with Haxxor Engine; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from collections import OrderedDict
import tools

TERM_WIDTH = 79
ASCII_ART = """
cccc:cccccc     :::::cc  ........  ... .     .                   oooo
          .::     ::::::  ...   .     ...  ....                 @@@@@@
              ..     :::    ..         : :  :c:                 @@@@@@
   @@@  @@@   ...       .     ..       :.:   ..    :  .          @@@@
   .@.  .@. .o@@@@o   8@@ :@@. o@@. @@o::.@@@@@.o.:o@@@OCo              oooo
 ..:@@@@@@.   .ooo@.    O@@c     c@@o : o@c ::c@:  c@C..               @@@@@@
   :@.  .@. c@.  :@.   :@oO@    .@oo@.:.c@o:: c@:. .@:.                @@@@@@
 ..@@@  @@@c: @@@@ @..@@o.:8@@ @@C : @@C :@@@@@. .@@@@@@                @@@@
      ...... . ..:   ... .  .     .:.  . :cccc::.   .     oooo   oooo   oooo
               ..      .      .:: ::..cc:.:::c:::co:  .  @@@@@@ @@@@@@ @@@@@@
                              .    :  .:..  ::.  .       @@@@@@ @@@@@@ @@@@@@
                     .     .    .. .:   .  . :. :         @@@@   @@@@   @@@@
         ..  cc@ ..   @@@@@@@...       ...:...:.c.  .@:        ...       ..
         oOo    @     :@...... :c:@Oo.   :@@@@......       :c:@Oo. .. o@@@o. ..
      oOo Oco   @     :@@@@     @o  .@. :@....@o:.  @@c     @o  .@. :@ooooo@
  .@   OCo O          :@ .. ....@c  .@. o@   .@c :. :@c     @c   @: c@
    @  .O             @@@@@@@..:@o..c@c. o@@@@@o..c@@@@@.  .@o  .@c   @@@@@ ::
                              ..:  . : .      @: . c..                        .
                                   ...:.. @@@@        c
                                     ..:  ::            .
All your base are belong to... *sigh...* No puedo seguir con esto."""
SECTIONS = OrderedDict([
    (
        "Índice",
        ""
    ),
    (
        "Sobre el juego",
        """Haxxor Engine es un videojuego de simulación en el que el jugador toma el rol de un hacker y recibe por e-mail misiones que debe completar, que involucran acceder ilegalmente a otras computadoras y hacer en estas cosas como borrar datos, robar información, instalar virus, etc; todo a través de una consola de comandos."""
    ),
    (
        "Cómo jugar",
        """Empezá por escribir "mail" (sin comillas) y presionar enter. Dicho comando despliega el último e-mail recibido. En él debería estar la información que necesitás para saber qué hacer. Todos los comandos que necesites saber se te van a ir enseñando a medida que avances en el juego.
También podés escribir "help" para ver todos los comandos disponibles con un breve resumen de su utilidad."""
    ),
    (
        "Créditos",
        """La idea es robada de otro juego, HackTheGame, creado por Chaozz (<http://www.chaozz.nl/>).
Haxxor Engine y sus misiones fueron programadas y diseñadas por Gerardo Marset, aka Ideka.

En el 2009, poco después de aprender Python, decidí tratar de copiar HackTheGame para practicar el lenguaje. El resultado no fue malo, pero al revisitar el código en el 2014 no pude evitar notar que había mucho lugar para mejoras, por lo que decidí rehacerlo.

Para contactarme por bugs, comentarios, etc: gammer1994@gmail.com"""
    ),
    (
        "Renuncia de responsabilidad",
        """Haxxor Engine no fue creado para promover el hacking.
El juego entero es simulado. Las IP y los puertos son creados aleatoriamente.
Las direcciones de e-mail son ficticias, al igual que lo es la historia y todos sus personajes."""
    ),
    (
        "Copyright y eso",
        "Haxxor Engine  Copyright © 2010, 2014  Gerardo Marset"
    )
])


def print_header(title, number):
    # TODO: Make this clearer?
    print("[ ][O][ ]".ljust(TERM_WIDTH, "·"))
    print(("[ ][ ][O] " +
           ("[{}] - {}".format(number, title) if number is not None
            else title)).ljust(TERM_WIDTH - 1) + "·")
    print("[O][O][O]".ljust(TERM_WIDTH, "·"))


def print_section(text):
    left = " :     :  "
    print(left)
    lines = tools.formatted(text, TERM_WIDTH - len(left)).split("\n")
    for line in lines:
        print(left + line)
    print(left)


def print_eof():
    print("[E][O][F]".ljust(TERM_WIDTH, "·"))


def print_info():
    print(ASCII_ART)
    print()
    SECTIONS["Índice"] = ""
    for i, title in enumerate(SECTIONS.keys()):
        SECTIONS["Índice"] += "[{}] - {}\n".format(i, title)
    SECTIONS["Índice"] = SECTIONS["Índice"][:-1]
    for i, (title, text) in enumerate(SECTIONS.items()):
        print_header(title, i)
        print_section(text)
    print_eof()
