from board import Board
from exceptions import *
class ComputerStrategy:
    def __init__(self, board: Board):
        self.__board = board
    def place(self):
        """
        Decides where to places a peace for the computer,
        and places it
        x- the x cordinate of the players previous move
        y- the y cordinate of the players previous move
        return the x and y cordinates of the peace placed
        """

        for x,y,c in self.__board.get_last_for_mills():
            if c==-1:
                self.__board.place_computer (x,y)
                return (x,y)
        for x,y,c in self.__board.get_last_for_mills():
            if c==1:
                self.__board.place_computer (x,y)
                return (x,y)
            

        for i in range(7):
                    for j in range(7):
                        if self.__board.get_board()[i][j]==0:
                            self.__board.place_computer(i,j)
                            return (i,j)
        raise PlacePeaceException("No place to place a peace")
        
        
    def remove_peace(self):
        """
        Decides which peace to remove for the computer,
        and removes it
        """
        for i in range(7):
            for j in range(7):
                if self.__board.get_board()[i][j]==1 and (not self.__board.check_mill(i,j) or self.__board.is_peace_to_remove(1)==False):
                    self.__board.remove_peace(i,j,1)
                    return
        raise RemovePeaceException("No peace to remove")
        
    
    def move(self):
        """
        Decides where to move a peace for the computer,
        and moves it
        return the x and y cordinates of the peace moved
        """
        
        for x,y,c in self.__board.get_last_for_mills():
            if c==-1:
                x,y=self.__try_to_move(x,y,True)
                if x!=-1 and y!=-1:
                    return (x,y)
                
            
        for x,y,c in self.__board.get_last_for_mills():
            if c==1:
                x,y=self.__try_to_move(x,y)
                if x!=-1 and y!=-1:
                    return (x,y)
            
        for i in range(7):
            for j in range(7):
                if self.__board.get_board()[i][j]==-1:
                    for direction in ["up","down","left","right"]:
                        try:
                            self.__board.move_peace(i,j,direction)
                            return (i,j)
                        except MovePeaceException:
                            continue
        raise MovePeaceException("No peace to move")
    def jump(self):
        """
        Jumps a peace for the computer
        """
        for x,y,c in self.__board.get_last_for_mills():
            if c==-1:
                for i in range(7):
                    for j in range(7):
                        if self.__board.get_board()[i][j]==-1:
                            self.__board.jump_peace(i,j,x,y)
                            if self.__board.check_mill(x,y)==False:
                                self.__board.jump_peace(x,y,i,j)
                            else:
                                return (x,y)
                
        for x,y,c in self.__board.get_last_for_mills():
            if c==1:
                for i in range(7):
                    for j in range(7):
                        if self.__board.get_board()[i][j]==-1:
                            self.__board.jump_peace(i,j,x,y)
                            return (x,y)
                
        for i in range(7):
            for j in range(7):
                if self.__board.get_board()[i][j]==-1:
                    for x in range(7):
                        for y in range(7):
                            if self.__board.get_board()[x][y]==0:
                                self.__board.jump_peace(i,j,x,y)
                                return (x,y)
                        
        
    
    def __try_to_move(self,des_x,des_y,has_to_be_mill:bool=False):
        """
        Tries to move all neighboring computer a peace to a certain position, 
        so that the peace at that position will be in a mill, if has_to_be_mill is True
        des_x- the x cordinate of the destination
        des_y- the y cordinate of the destination
        has_to_be_mill- if the peace at the destination has to be in a mill
        return the x and y cordinates where peace was moved or (-1,-1) if no peace was moved
        """
        if self.__board.upper_neighbour(des_x,des_y)!=None:
            x,y=self.__board.upper_neighbour(des_x,des_y)
            if self.__board.get_board()[x][y]==-1:
                self.__board.move_peace(x,y,"down")
                if has_to_be_mill==True:
                    if self.__board.check_mill(des_x,des_y)==False:
                        self.__board.move_peace(des_x,des_y,"up")
                    else:
                        
                        return (des_x,des_y)
                else:
                    return (des_x,des_y)
                
        if self.__board.lower_neighbour(des_x,des_y)!=None:
            x,y=self.__board.lower_neighbour(des_x,des_y)
            if self.__board.get_board()[x][y]==-1:
                self.__board.move_peace(x,y,"up")
                if has_to_be_mill==True:
                    if self.__board.check_mill(des_x,des_y)==False:
                        self.__board.move_peace(des_x,des_y,"down")
                    else:
                        
                        return (des_x,des_y)
                else:
                    return (des_x,des_y)
                
        if self.__board.left_neighbour(des_x,des_y)!=None:
            x,y=self.__board.left_neighbour(des_x,des_y)
            if self.__board.get_board()[x][y]==-1:
                self.__board.move_peace(x,y,"right")
                if has_to_be_mill==True:
                    if self.__board.check_mill(des_x,des_y)==False:
                        self.__board.move_peace(des_x,des_y,"left")
                    else:
                        
                        return (des_x,des_y)
                else:
                    return (des_x,des_y)
                
        if self.__board.right_neighbour(des_x,des_y)!=None:
            x,y=self.__board.right_neighbour(des_x,des_y)
            if self.__board.get_board()[x][y]==-1:
                self.__board.move_peace(x,y,"left")
                if has_to_be_mill==True:
                    if self.__board.check_mill(des_x,des_y)==False:
                        self.__board.move_peace(des_x,des_y,"right")
                    else:
                        
                        return (des_x,des_y)
                else:
                    return (des_x,des_y)
        return (-1,-1)
    
            