#!/usr/bin/env python3

from pgapi import PGAPI

class Globals:
    def __init__(self):
        self.pgapi = PGAPI()


_globals = Globals()