from board import Board
from game import Game
from strategy import ComputerStrategy

from exceptions import *
import texttable
class UI():
    def __init__(self,game: Game, strategy: ComputerStrategy):
        self.__game = game
        self.__strategy = strategy
    def start(self):
        self.print_board()
        computers_x,computers_y = -1,-1

        #---------------------------------placing phase---------------------------------
        #TODO replace with 9
        for f in range(9):
            playerStepped = False
            while not playerStepped:
                try:
                    print("Place a peace to a free field!")
                    players_x = int(input("Enter x: "))
                    players_y = int(input("Enter y: "))
                    self.__game.board.place_player(players_x,players_y)
                    playerStepped = True
                except PlacePeaceException as e:
                    print(e)
                    continue
                except ValueError:
                    print("Invalid input")
                    continue
            self.print_board()

            #check if player has a mill
            if self.__game.board.check_mill(players_x,players_y):
                self.__select_to_remove()
                
            #computer steps
            print("Computer steps:")
            computers_x,computers_y=self.__strategy.place()
            self.print_board()

            #check if computer has a mill
            if self.__game.board.check_mill(computers_x,computers_y):
                self.__computer_remove_peace()
            #print how many pieces are left to place
            print("You have ",9-f-1," pieces left to place")

        #-----------------------------------moving phase-----------------------------------
        print("Moving phase started!\n")
        while True:
            #player steps
            if self.__game.board.can_player_jump():
                print("You can jump with a peace!")
                playerStepped = False
                while not playerStepped:
                    try:
                        print("Choose a peace to jump with")
                        players_x = int(input("Enter x: "))
                        players_y = int(input("Enter y: "))
                        des_x = int(input("Enter destination x: "))
                        des_y = int(input("Enter destination y: "))
                        self.__game.board.jump_peace(players_x,players_y, des_x, des_y)
                        players_x,players_y = des_x,des_y
                        playerStepped = True
                    except JumpPeaceException as e:
                        print(e)
                        continue
                    except ValueError:
                        print("Invalid input")
                        continue
            else:
                playerStepped = False
                while not playerStepped:
                    try:
                        print("Choose a peace to move")
                        players_x = int(input("Enter x: "))
                        players_y = int(input("Enter y: "))
                        direction = input("Enter direction (up/down/left/right): ")
                        self.__game.board.move_peace(players_x,players_y, direction)
                        players_x,players_y = self.__game.board.get_neighbour(players_x,players_y,direction)
                        playerStepped = True
                    except MovePeaceException as e:
                        print(e)
                        continue
                    except ValueError:
                        print("Invalid input")
                        continue
            self.print_board()
            #check if player has a mill
            if self.__game.board.check_mill(players_x,players_y):
                self.__select_to_remove()
                if self.__game.board.check_player_won():
                    print("You won!")
                    break
                
            #computer steps
            print("Computer steps:")
            if self.__game.board.can_computer_jump():
                computers_x,computers_y=self.__strategy.jump()
            else:
                computers_x,computers_y=self.__strategy.move()
            self.print_board()
            #check if computer has a mill
            if self.__game.board.check_mill(computers_x,computers_y):
                self.__computer_remove_peace()
                if self.__game.board.check_computer_won():
                    print("Computer won!")
                    break
        
            
    def print_board(self):
        t = texttable.Texttable()
        for i in range(7):
            row = []
            for j in range(7):
                if self.__game.board.get_board()[j][i]=='_':
                    row.append('')
                elif self.__game.board.get_board()[j][i]==1:
                    row.append('⚪')
                elif self.__game.board.get_board()[j][i]==-1:
                    row.append('⚫')
                else:
                    row.append('0')
            t.add_row(row)
        print(t.draw())

    def __select_to_remove(self):
        print("You have a mill. Select a peace to remove!")
        selected = False
        while not selected:
            try:
                x = int(input("Enter x: "))
                y = int(input("Enter y: "))
                self.__game.board.remove_peace(x,y,-1)
                print("Peace removed")
                self.print_board()
                selected = True
            except RemovePeaceException as e:
                print(e)
                
            except ValueError:
                print("Invalid input")
    def __computer_remove_peace(self):
        print("Computer has a mill, and removes a peace:")
        self.__strategy.remove_peace()
        self.print_board()
                        
        
