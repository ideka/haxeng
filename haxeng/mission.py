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

import copy
import random

from enum import Enum
from filesystem import File, FileSpawner
import system
import tools

DIFFICULTY = 3  # Must be at least 1.
TRACKER_UPDATE_INTERVAL = 1  # In seconds.

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
        self.ip_tracker = IPTracker(security)

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

    def is_complete(self):
        for key, value in self.objectives.items():
            if key is not None or not value(self.system):
                return False
        return True

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


class IPTracker(object):
    def __init__(self, speed):
        assert(speed > 0)
        self.speed = speed
        self.ip = None
        self.time = 0

    def generate_first_ip(self, towards):
        ip = []
        quotients = list(range(1, 5))
        random.shuffle(quotients)
        for octet, quotient in zip(towards.split("."), quotients):
            octet = int(octet) + 1
            if octet > 127:
                octet -= 128 // quotient
            else:
                octet += 128 // quotient
            ip.append(octet)

        return ".".join(map(str, ip))

    def update(self, time, towards):
        self.time += time
        while self.time >= 1:
            if self.step(towards):
                return True
            self.time -= 1
        return False

    def step(self, towards):
        assert(DIFFICULTY > 0)
        if self.ip is None:
            self.ip = self.generate_first_ip(towards)

        fromip = list(map(int, self.ip.split(".")))
        toip = list(map(int, towards.split(".")))

        nlist = list(range(len(fromip)))
        random.shuffle(nlist)
        for n in nlist:
            if fromip[n] != toip[n]:
                break
        fromip[n] = tools.approach(fromip[n], toip[n], tools.dice(self.speed,
                                                                  DIFFICULTY))
        self.ip = ".".join(map(str, fromip))
        #x = 0
        #for fromoctet, tooctet in zip(fromip, toip):
        #    x += abs(fromoctet - tooctet)
        return fromip == toip
