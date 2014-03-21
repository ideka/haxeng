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

import tools
from filesystem import File


class System(object):
    def __init__(self, filesystem, ip, is_local):
        self.filesystem = filesystem
        self.ip = ip
        self.is_local = is_local

    def retrieve(self, dirlist):
        fs = self.filesystem
        for dir_ in dirlist:
            fs = fs[dir_]
        return fs

    def is_file(self, dirlist):
        try:
            element = self.retrieve(dirlist)
        except KeyError:
            return False
        return isinstance(element, File)

    def is_directory(self, dirlist):
        try:
            element = self.retrieve(dirlist)
        except KeyError:
            return False
        return not isinstance(element, File)

    def listdir(self, dirlist):
        directory = self.retrieve(dirlist)
        return [element for element in directory.items()]

    def delete(self, dirlist):
        targets = []
        if len(dirlist) == 1:
            parent = self.retrieve(dirlist[:1])
            targets = list(self.filesystem[dirlist[0]].keys())
        else:
            parent = self.retrieve(dirlist[:-1])
            targets = [dirlist[-1]]

        for target in targets:
            del parent[target]


def abs_dirlist(dirlist, relative_dirlist):
    for dir_ in relative_dirlist:
        if dir_ == ".":
            continue
        if dir_ == "..":
            if len(dirlist) <= 1:
                continue
            dirlist.pop()
            continue
        dirlist.append(dir_)
    return dirlist


def default_local_system():
    filesystem = {
        "C:": {
            "Musica": {
                "Guns_N_Roses": {
                    "Estranged.mp3": File(),
                    "Dont_Cry.mp3": File(),
                    "Sweet_Child_O_Mine.mp3": File(),
                    "Bad_Apples.mp3": File(),
                    "Bad_Obsession.mp3": File()
                },
                "ACDC": {
                    "Back_in_Black.mp3": File(),
                    "Its_a_Long_Way_to_the_Top.mp3": File()
                },
                "Freebird.mp3": File(),
                "Mr_Crowley.mp3": File()
            },
            "Marcadores": {
                "universomario.foros.ws": File(),
                "www.ideka.ideka": File(),
                "www.chaozz.nl": File()
            },
            "Proyectos": {
            },
            "Descargas": {
            },
            "lolcat.jpg": File(),
            "tarea.cpp": File(),
            "tarea2.cpp": File()
        }
    }
    ip = tools.random_ip()

    return System(filesystem, ip, True)
