# Placing tiles on the wall counts for points
# "Red": 0, "Orange": 1, "Black": 2, "Blue": 3, "Light Blue": 4, "First": 5
class Wall:
    def __init__(self) -> None:
        self.wall = [[[3, 0], [1, 0], [0, 0], [2, 0], [4, 0]],
                     [[4, 0], [3, 0], [1, 0], [0, 0], [2, 0]],
                     [[2, 0], [4, 0], [3, 0], [1, 0], [0, 0]],
                     [[0, 0], [2, 0], [4, 0], [3, 0], [1, 0]],
                     [[1, 0], [0, 0], [2, 0], [4, 0], [3, 0]]]
        
    def add_tile(self, row: int, type: int) -> bool:
        for i in range(5):
            if type == self.wall[row][i][0]:
                self.wall[row][i][1] = 1
                return True
        
        return False
    
    def print_wall(self) -> None:
        # color table with spacing to align for print out
        color = ["       Red", "    Orange", "     Black", "      Blue", "Light Blue"]
        
        for i in range(5):
            print("Row", i, end=" ")
            for j in range(5):
                if self.wall[i][j][1] == 1:
                    print(color[self.wall[i][j][0]], ": 1", end=" ")
                else:
                    print(color[self.wall[i][j][0]], ": 0", end=" ")
            print()
        print()

# Complete the pattern lines to move tiles to the wall for points
class PatternLines:
    def __init__(self) -> None:
        # [type, capacity, size, [list of tiles already in the wall for that row]]
        self.pattern_line = [[-1,1,0],[-1,2,0],[-1,3,0],[-1,4,0],[-1,5,0]]
        
    def add_tiles(self, row: int, type: int, number: int) -> None:
        pass
    
    # Check if we can place a tile in a specifics row
    def check_valid_move(self, type: int, row: int) -> bool:
        if self.pattern_line[row][0] != -1 and self.pattern_line[row][0] != type:
            return False
        
        if self.pattern_line[row][1] <= self.pattern_line[row][2]:
            return False
        
        return True


    def print_pattern_line(self) -> None:
        for i in range(5):
            print("Pattern Line", i, end=": ")
            

# Surplus tiles are put in the floor line and count for negative points
class FloorLine:
    def __init__(self) -> None:
        self.floor = [[-1],[-1],[-1],[-1],[-1],[-1],[-1]]
        self.length = 0
        
    def add_floor(self, tiles: list[int]) -> None:
        pass
    
class Board:
    def __init__(self, player: int) -> None:
        self.player = player
        self.wall = Wall()
        self.pattern_line = PatternLines()
        self.floor = FloorLine()