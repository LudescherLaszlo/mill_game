from board import Board
from exceptions import *

class Game():
    def __init__(self):
        self.__board = Board()
        
    @property
    def board(self):
        return self.__board
    
            
    
    