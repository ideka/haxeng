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


class File(object):
    def __init__(self, id_=None):
        self.id_ = id_


class FileSpawner(File):
    def __init__(self, name, quantity, id_=None):
        File.__init__(self, id_)
        self.name = name
        self.quantity = quantity