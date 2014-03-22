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

import os.path
import random
import signal

TERM_WIDTH = 79
DEBUG = True

original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, lambda a, b: None)


def random_ip():
    return ".".join([str(random.randrange(193, 255))] +
                    [str(random.randrange(1, 255)) for i in range(3)])


def random_port():
    return str(random.randint(2000, 4000))


def random_user():
    return random.sample(
        ["user",
         "default",
         "root",
         "admin",
         "administrador",
         "usuario"],
        1)[0]


def random_password():
    return random.sample(
        ["123456",
         "password",
         "qwerty",
         "abc123",
         "iloveyou",
         "123123",
         "admin",
         "letmein",
         "monkey",
         "shadow",
         "sunshine",
         "password1",
         "princess",
         "azerty",
         "trustno1",
         "root",
         "secret"],
        1)[0]


def fix_slashes(path):
    return path.replace("\\", os.path.sep).replace("/", os.path.sep)


def format_dirlist(dirlist):
    return "\\".join(dirlist) + "\\" * (len(dirlist) == 1)


def formatted(text, width):  # TODO: Properly name this function.
    text_list = list(text)

    w = 0
    for i in range(len(text_list)):
        if w == width:
            for j in range(len(text_list[:i])):
                if text_list[i - j] == "\n":
                    break
                if text_list[i - j] == " ":
                    text_list[i - j] = "\n"
                    w = j
                    break
        w += 1
        if text_list[i] == "\n":
            w = 0

    return "".join(text_list)


def iinput(*args, **kwargs):
    def inner(prompt, no_interrupt=True, no_eof=False):
        while True:
            try:
                response = input(prompt)
            except KeyboardInterrupt:
                if not no_interrupt:
                    raise
                else:
                    print()
            except EOFError:
                if not no_eof:
                    raise
                else:
                    print()
            else:
                return response
    signal.signal(signal.SIGINT, original_sigint)
    response = inner(*args, **kwargs)
    signal.signal(signal.SIGINT, lambda a, b: None)
    return response


def yn(prompt, default=None):
    while True:
        response = iinput("{} ({}/{}) ".format(prompt,
                                               "yY"[default is True],
                                               "nN"[default is False]),
                          no_eof=True).lower()
        if response not in "yn" or response == "":
            if default is not None:
                return default
        else:
            return response == "y"
