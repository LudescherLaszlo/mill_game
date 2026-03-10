from ui import UI
from board import Board
from game import Game
from strategy import ComputerStrategy
def start():
    
    game = Game()
    strategy = ComputerStrategy(game.board)
    ui = UI(game,strategy)
    ui.start()


if __name__ == '__main__':
    start()
#  ⚪ ⚫