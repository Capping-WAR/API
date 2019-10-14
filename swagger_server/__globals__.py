#!/usr/bin/env python3

from orm import ORM

class Globals:
    def __init__(self):
        self.orm = ORM()


_globals = Globals()