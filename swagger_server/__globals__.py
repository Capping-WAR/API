#!/usr/bin/env python3

from pgapi import PGAPI

class Globals:
    def __init__(self):
        self.pgapi = PGAPI()
        self.dataset_count = None


_globals = Globals()