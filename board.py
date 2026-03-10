from exceptions import *
class Board:
    def __init__(self):
        self.__board = []
        self.__last_for_mills=[]
        for i in range(7):
            self.__board.append([0] * 7)
        for i in range(7):
            for j in range(7):
                if self.check_valid_place(i,j)==False:
                    self.__board[i][j] = '_'
    def place_player(self, x, y):
        """
        Places a peace for the player on the board
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        """
        if self.check_valid_place(x,y)==False:
            raise PlacePeaceException("Invalid move")
        if self.__board[x][y] == 0:
            self.__board[x][y] = 1
            self.__build_last_for_mills()
                
            return
        else:
            raise PlacePeaceException("Invalid move")
    def place_computer(self, x, y):
        """
        Places a peace for the computer on the board
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        """
        if self.__board[x][y] == 0:
            self.__board[x][y] = -1
            self.__build_last_for_mills()
            return
 
    def distance_from_center (self, x, y):
        """
        Returns the distance of the peace at x,y from the center of the board
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        return -distance
        """
        return max(abs(x-3),abs(y-3))

    def check_valid_place(self, x,y):
        """
        Checks if the place x,y is part of the board
        x - the x coordinate of the place
        y - the y coordinate of the place
        return True if the place is part of the board, False otherwise"""
        if x<0 or x>6 or y<0 or y>6:
            return False
        if (x==y or x+y==6 or x==3 or y==3) and ( x!=3 or y!=3):
            return True
        return False
    
    
    
    def check_mill(self, x, y):
        """
        Checks if the peace at x,y is part of a mill.
        x- the x coordinate of the peace
        y- the y coordinate of the peace
        return True if the peace is part of a mill, False otherwise
        """
        d=self.distance_from_center(x,y)
        if x!=3 and y!=3:
            if self.__board[3-d][y]==self.__board[3][y] and self.__board[3][y]==self.__board[3+d][y] and self.__board[3-d][y]!=0:
                return True
            if self.__board[x][3-d]==self.__board[x][3] and self.__board[x][3]==self.__board[x][3+d] and self.__board[x][3-d]!=0:
                return True
        if x==3:
            if self.__board[3-d][y]==self.__board[3][y] and self.__board[3][y]==self.__board[3+d][y] and self.__board[3-d][y]!=0:
                return True
            if y<3:
                if self.__board[x][0]==self.__board[x][1] and self.__board[x][1]==self.__board[x][2] and self.__board[x][2]!=0:
                    return True
            else:
                if self.__board[x][4]==self.__board[x][5] and self.__board[x][5]==self.__board[x][6] and self.__board[x][4]!=0:
                    return True
        if y==3:
            if self.__board[x][3-d]==self.__board[x][3] and self.__board[x][3]==self.__board[x][3+d] and self.__board[x][3-d]!=0:
                return True
            if x<3:
                if self.__board[0][y]==self.__board[1][y] and self.__board[1][y]==self.__board[2][y] and self.__board[2][y]!=0:
                    return True
            else:
                if self.__board[4][y]==self.__board[5][y] and self.__board[5][y]==self.__board[6][y] and self.__board[4][y]!=0:
                    return True
        return False
        
    
    
    def remove_peace(self,x,y,c):
        """
        Removes a peace from the board
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        c - the color of the peaces that can be removed (1 for player, -1 for computer)
        """
        if self.check_valid_place(x,y)==False:
            raise RemovePeaceException("Invalid field")
        if self.__board[x][y] !=c:
            raise RemovePeaceException("Can't remove this piece. Select another one")
        if self.check_mill(x,y) and self.is_peace_to_remove(c): 
            raise RemovePeaceException("The peace is part of a mill. Select another one")
        else:
            self.__board[x][y]=0
            self.__build_last_for_mills()
            return
    def is_peace_to_remove(self,c):
        """
        Returns True if there is a peace not part of a mill for the player with color c
        """
        for i in range(7):
            for j in range(7):
                if self.__board[i][j]==c and not self.check_mill(i,j):
                    return True
        return False
    
    #-----------------------------last for mills-------------------------------------
    def __add_last_for_mill(self, x,y,c):
        """
        Adds a peace to the list of last peaces for mills
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        c - the color of the peace that if placed on x,y would form a mill"""
        if (x,y,c) not in self.__last_for_mills:
            self.__last_for_mills.append((x,y,c))

    def __build_last_for_mills(self):
        """
        Builds the list of last peaces for mills
        """
        self.__last_for_mills.clear()
        for i in range(7):
            for j in range(7):
                if self.__board[i][j]!='_':
                    self.one_step_from_mill(i,j)
                    

    def one_step_from_mill(self,x,y):
        """
        Checks if we would place a peace on x,y it would form a mill.
        If it would, it adds the last peace for the mill to the list
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        """
        if x==-1 or y==-1:
            return -1
        d=self.distance_from_center(x,y)
        if x!=3 and y!=3:
            if abs(self.__board[3-d][y] + self.__board[3][y] + self.__board[3+d][y]) == 2:
                if self.__board[3-d][y]==0:
                    self.__add_last_for_mill(3-d,y,self.__board[3][y])
                if self.__board[3][y]==0:
                    self.__add_last_for_mill(3,y,self.__board[3-d][y])
                if self.__board[3+d][y]==0:
                    self.__add_last_for_mill(3+d,y,self.__board[3][y])
            if abs(self.__board[x][3-d] + self.__board[x][3] + self.__board[x][3+d]) == 2:
                if self.__board[x][3-d]==0:
                    self.__add_last_for_mill(x,3-d,self.__board[x][3])
                if self.__board[x][3]==0:
                    self.__add_last_for_mill(x,3,self.__board[x][3-d])
                if self.__board[x][3+d]==0:
                    self.__add_last_for_mill(x,3+d,self.__board[x][3])
        if x==3:
            if abs(self.__board[3-d][y] + self.__board[3][y] + self.__board[3+d][y]) == 2:
                if self.__board[3-d][y]==0:
                    self.__add_last_for_mill(3-d,y,self.__board[3][y])
                if self.__board[3][y]==0:
                    self.__add_last_for_mill(3,y,self.__board[3-d][y])
                if self.__board[3+d][y]==0:
                    self.__add_last_for_mill(3+d,y,self.__board[3][y])
            if y<3:
                if abs(self.__board[x][0] + self.__board[x][1] + self.__board[x][2]) == 2:
                    if self.__board[x][0]==0:
                        self.__add_last_for_mill(x,0, self.__board[x][1])
                    if self.__board[x][1]==0:
                        self.__add_last_for_mill(x,1, self.__board[x][0])
                    if self.__board[x][2]==0:
                        self.__add_last_for_mill(x,2, self.__board[x][1])
            else:
                if abs(self.__board[x][4] + self.__board[x][5] + self.__board[x][6]) == 2:
                    if self.__board[x][4]==0:
                        self.__add_last_for_mill(x,4, self.__board[x][5])
                    if self.__board[x][5]==0:
                        self.__add_last_for_mill(x,5, self.__board[x][4])
                    if self.__board[x][6]==0:
                        self.__add_last_for_mill(x,6, self.__board[x][5])
        if y==3:
            if abs(self.__board[x][3-d] + self.__board[x][3] + self.__board[x][3+d]) == 2:
                if self.__board[x][3-d]==0:
                    self.__add_last_for_mill(x,3-d,self.__board[x][3])
                if self.__board[x][3]==0:
                    self.__add_last_for_mill(x,3,self.__board[x][3-d])
                if self.__board[x][3+d]==0:
                    self.__add_last_for_mill(x,3+d,self.__board[x][3])
            if x<3:
                if abs(self.__board[0][y] + self.__board[1][y] + self.__board[2][y]) == 2:
                    if self.__board[0][y]==0:
                        self.__add_last_for_mill(0,y,self.__board[1][y])
                    if self.__board[1][y]==0:
                        self.__add_last_for_mill(1,y,self.__board[0][y])
                    if self.__board[2][y]==0:
                        self.__add_last_for_mill(2,y,self.__board[1][y])
            else:
                if abs(self.__board[4][y] + self.__board[5][y] + self.__board[6][y]) == 2:
                    if self.__board[4][y]==0:
                        self.__add_last_for_mill(4,y,self.__board[5][y])
                    if self.__board[5][y]==0:
                        self.__add_last_for_mill(5,y,self.__board[4][y])
                    if self.__board[6][y]==0:
                        self.__add_last_for_mill(6,y,self.__board[5][y])      
        return
    
    def get_last_for_mills(self):
        return self.__last_for_mills
    
    #-----------------------------moving phase---------------------------------------

    def move_peace(self,x,y,direction):
        """
        Moves a peace from x,y to new_x,new_y
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        direction - the direction in which to move the peace
        """
        c = self.__board[x][y]
        
        if c==0:
            raise MovePeaceException("Invalid move: the field is empty")
        if direction == "up":
            if self.upper_neighbour(x,y)==None:
                raise MovePeaceException("Invalid move: destination field does not exist")
            new_x,new_y = self.upper_neighbour(x,y)
        elif direction == "down":
            if self.lower_neighbour(x,y)==None:
                raise MovePeaceException("Invalid move: destination field does not exist")
            new_x,new_y = self.lower_neighbour(x,y)
        elif direction == "left":
            if self.left_neighbour(x,y)==None:
                raise MovePeaceException("Invalid move: destination field does not exist")
            new_x,new_y = self.left_neighbour(x,y)
        elif direction == "right":
            if self.right_neighbour(x,y)==None:
                raise MovePeaceException("Invalid move: destination field does not exist")
            new_x,new_y = self.right_neighbour(x,y)
        else:
            raise MovePeaceException("Invalid move: invalid direction")
        
        if self.__board[new_x][new_y]!=0:
            raise MovePeaceException("Invalid move: destination is not empty")
        
        self.__board[x][y]=0
        self.__board[new_x][new_y]=c
        self.__build_last_for_mills()
        return
        
       
    def upper_neighbour(self, x, y):
        """
        Returns the coordinates of the upper neighbour of the peace at x,y
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        return - the coordinates of the upper neighbour or None
        """
        d=self.distance_from_center(x,y)
        if y-3+d==0 and x!=3:
            return None
        else:
            if x==3:
                if y==4 or y==0:
                    return None
                return (x,y-1)
            return (x,y-d)
        
    def lower_neighbour(self, x, y):
        """
        Returns the coordinates of the lower neighbour of the peace at x,y
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        return - the coordinates of the lower neighbour or None"""
        d=self.distance_from_center(x,y)
        if y+3-d==6 and x!=3:
            return None
        else:
            if x==3:
                if y==2 or y==6:
                    return None
                return (x,y+1)
            return (x,y+d)
    def left_neighbour(self, x, y):
        """
        Returns the coordinates of the left neighbour of the peace at x,y
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        return - the coordinates of the left neighbour or None
        """
        d=self.distance_from_center(x,y)
        if x-3+d==0 and y!=3:
            return None
        else:
            if y==3:
                if x==4 or x==0:
                    return None
                return (x-1,y)
            return (x-d,y)
    def right_neighbour(self, x, y):
        """
        Returns the coordinates of the right neighbour of the peace at x,y
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        return - the coordinates of the right neighbour or None
        """
        d=self.distance_from_center(x,y)
        if x+3-d==6 and y!=3:
            return None
        else:
            if y==3:
                if x==2 or x==6:
                    return None
                return (x+1,y)
            return (x+d,y)
    def get_neighbour(self, x, y,dir):
        """
        Returns the coordinates of the neighbour of the peace at x,y in the direction dir
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        dir - the direction in which to find the neighbour
        return - the coordinates of the neighbour
        """
        if dir=="up":
            return self.upper_neighbour(x,y)
        if dir=="down":
            return self.lower_neighbour(x,y)
        if dir=="left":
            return self.left_neighbour(x,y)
        if dir=="right":
            return self.right_neighbour(x,y)
        
    def get_board(self):
        return self.__board
    def clear_board(self):
        """
        Clears the board
        """
        for i in range(7):
            for j in range(7):
                if self.__board[i][j]!='_':
                    self.__board[i][j]=0
        self.__build_last_for_mills()
        return
    
    #-----------------------------jumping phase---------------------------------------
    def jump_peace(self,x,y,new_x,new_y):
        """
        Jumps a peace from x,y to new_x,new_y
        x - the x coordinate of the peace
        y - the y coordinate of the peace
        new_x - the x coordinate of the destination
        new_y - the y coordinate of the destination
        """
        c = self.__board[x][y]
        if c==0:
            raise JumpPeaceException("Invalid move: the field is empty")
        if self.__board[new_x][new_y]!=0:
            raise JumpPeaceException("Invalid move: destination is not empty")
        self.__board[x][y]=0
        self.__board[new_x][new_y]=c
        self.__build_last_for_mills()
        return
    def count_peaces(self,c):
        """
        Returns the number of peaces of color c
        c - the color of the peaces
        """
        count=0
        for i in range(7):
            for j in range(7):
                if self.__board[i][j]==c:
                    count+=1
        return count
    def can_player_jump(self):
        """
        Returns True if the player can jump
        """
        if self.count_peaces(1)==3:
            return 1
        return False
    def can_computer_jump(self):
        """
        Returns True if the computer can jump
        """
        if self.count_peaces(-1)==3:
            return 1
        return False
    def check_player_won(self):
        """
        Returns True if the player won
        """
        if self.count_peaces(-1)<3:
            return True
        return False
    def check_computer_won(self):
        """
        Returns True if the computer won
        """
        if self.count_peaces(1)<3:
            return True
        return False
    
