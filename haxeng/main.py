#!/usr/bin/python3
#
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

from game import Game


def main():
    game = Game()
    game.main_loop()

if __name__ == "__main__":
    main()
