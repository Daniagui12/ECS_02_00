from enum import Enum

import pygame

class CInputCommand:
    def __init__(self, name: str, key: int, pos: tuple = None):
        self.name = name
        self.key = key
        self.pos = pos
        self.phase = CommandPhase.NA
        
class CommandPhase(Enum):
    NA = 0
    START = 1
    END = 2