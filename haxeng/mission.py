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

import copy

from enum import Enum
from filesystem import File, FileSpawner
import system
import tools


Objective = Enum(
    "download",
    "upload",
    "delete"
)


class Mission(object):
    def __init__(self, email, asciiart, filesystem, objectives, security):
        self._system = None
        self._port = None
        self._user = None
        self._password = None

        self.email = email
        self.asciiart = asciiart
        self.filesystem = filesystem
        self.objectives = objectives
        self.security = security

        self.downloads = []

    def get_prepared_copy(self, game, model=None):
        mission_copy = copy.deepcopy(self)
        if model is not None:
            mission_copy.system.ip = model.system.ip
            mission_copy._port = model.port
            mission_copy._user = model.user
            mission_copy._password = model.password
        mission_copy.prepare(game)
        return mission_copy

    def prepare(self, game):
        self.email.subject = self.substitute(game, self.email.subject)
        self.email.sender = self.substitute(game, self.email.sender)
        self.email.sender_email = self.substitute(game,
                                                  self.email.sender_email)
        self.email.message = self.substitute(game, self.email.message)
        self.asciiart = self.substitute(game, self.asciiart)
        self.prepare_filesystem(game)
        #import json
        #print(json.dumps(self.filesystem, indent=4, default=lambda o: o.id_))

    def prepare_filesystem(self, game, s=None):
        if s is None:
            s = self.filesystem
        for key in list(s.keys()):
            old_key = key
            key = self.substitute(game, key)
            s[key] = s.pop(old_key)
            if not isinstance(s[key], File):
                self.prepare_filesystem(game, s[key])
                continue
            if isinstance(s[key], FileSpawner):
                spawner = s[key]
                del s[key]
                for i in range(spawner.quantity):
                    s[self.substitute(game, spawner.name)] = File(spawner.id_)

    def substitute(self, game, text):
        while text.find("{random_ip}") != -1:
            text = text.replace("{random_ip}", tools.random_ip(), 1)

        text = text.format(
            name=game.name,
            local_ip=game.system.ip,
            remote_ip=self.system.ip,
            port=self.port,
            user=self.user,
            password=self.password
        )
        return text

    @property
    def system(self):
        if self._system is None:
            self._system = system.System(self.filesystem, tools.random_ip(),
                                         False)
        return self._system

    @property
    def port(self):
        if self._port is None:
            self._port = tools.random_port()
        return self._port

    @property
    def user(self):
        if self._user is None:
            self._user = tools.random_user()
        return self._user

    @property
    def password(self):
        if self._password is None:
            self._password = tools.random_password()
        return self._password
