from board import Board
from game import Game
from strategy import ComputerStrategy
from exceptions import *
from ui import UI

def board_test():
    try:
        board = Board()
        
        board.place_player(0, 0)
        board.place_player(3, 0)
        board.place_player(6, 0)

        assert board.get_board()[0][0] == 1 and board.get_board()[3][0] == 1 and board.get_board()[6][0] == 1, "Test failed. Error placing peace"
        assert board.check_mill(3, 0) == True, "Test failed. Error checking mill"

        board.remove_peace(3,0,1)
        assert board.get_board()[3][0] == 0, "Test failed. Error removing peace"
        assert board.check_mill(0, 0) == False, "Test failed. Error checking mill"

        assert len(board.get_last_for_mills())==1, "Test failed. Error computing last for mills"
        assert board.get_last_for_mills()[0]==(3,0,1), "Test failed. Error computing last for mills"

        board.place_player(0,6)
        board.place_player(6,6)
        
        assert len(board.get_last_for_mills())==4, "Test failed. Error computing last for mills"
        
        board.move_peace(0, 0, "down")
        
        assert board.get_board()[0][3] == 1, "Test failed. Error moving peace"
        assert board.get_board()[0][0] == 0, "Test failed. Error moving peace"

        board.clear_board()

        board.place_player(0, 0)
        board.place_player(3, 0)
        board.place_player(6, 3)
        board.move_peace(6,3,"up")
        assert board.check_mill(6,3) == False, "Test failed. Error checking mill after moving peace"
        x,y=board.get_neighbour(6,3,"up")
        assert board.check_mill(x,y) == True, "Test failed. Error checking mill after moving peace"
    except AssertionError as e:
        print(e)
        return


    
    
    print("Board tests passed")
def game_test():
    try:
        game = Game()
        
        game.board.place_player(0, 0)
        assert game.board.get_board()[0][0] == 1, "Test failed. Error placing peace"
    except AssertionError as e:
        print(e)
        return
    
    print("Game tests passed")
 
def strategy_test():
    try:
        game=Game()
        strategy = ComputerStrategy(game.board)
        game.board.place_player(0, 0)
        strategy.place()
        game.board.place_player(3, 0)
        strategy.place()
        assert game.board.check_mill(3, 0) == False, "Test failed. Error blocking player's mill"

        game.board.clear_board()
        game.board.place_computer(6, 0)
        game.board.place_computer(6, 6)
        game.board.place_computer(5, 3)
        game.board.place_computer(0, 3)
        strategy.move()
        assert game.board.get_board()[6][3]==-1, "Test 1 failed. Computer didn't moved peace to make a mill"
        assert game.board.check_mill(6, 3) == True, "Test 1 failed. Moved wrong peace to make a mill"

        game.board.clear_board()
        game.board.place_player(0, 0)
        strategy.place()
        game.board.place_player(1, 1)
        strategy.place()
        game.board.place_player(1, 5)
        strategy.place()
        game.board.place_player(2, 3)
        strategy.place()
        game.board.move_peace(2, 3, "down")
        strategy.move()
        assert game.board.get_board()[2][3]==-1, "Test failed. Computer didn't moved peace to make a mill"
        assert game.board.check_mill(2, 3) == True, "Test failed. Moved wrong peace to make a mill"

        game.board.clear_board()
        game.board.place_player(3, 0)
        strategy.place()
        game.board.place_player(0,3)
        strategy.place()
        game.board.place_player(1,1)
        strategy.place()
        game.board.remove_peace(0,3,1)
        strategy.move()
        assert game.board.get_board()[0][3]==-1, "Test failed. Computer didn't moved peace to make a mill"
        assert game.board.check_mill(0, 3) == True, "Test failed. Moved wrong peace to make a mill"
        
        game.board.clear_board()
        game.board.place_computer(0, 0)
        game.board.place_computer(0, 3)
        game.board.place_computer(1, 1)
        strategy.jump()
        assert game.board.get_board()[0][6]==-1, "Test failed. Computer didn't jumped peace to make a mill"
        assert game.board.check_mill(0, 6) == True, "Test failed. Jumped wrong peace to make a mill"

        game.board.clear_board()
        game.board.place_player(0, 0)
        strategy.place()
        game.board.place_player(6,6)
        strategy.place()
        game.board.place_player(6,0)
        strategy.place()
        strategy.jump()
        assert game.board.get_board()[6][3]==-1, "Test failed. Computer didn't jumped peace to block a mill"
    except AssertionError as e:
        print(e)
        return

    print("Strategy tests passed")


           
board_test()
game_test()
strategy_test()
