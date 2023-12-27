# Placing tiles on the wall counts for points
# "Red": 0, "Orange": 1, "Black": 2, "Blue": 3, "Light Blue": 4, "First": 5
class Wall:
    def __init__(self) -> None:
        # initialize wall array
        # each element represents a square on the wall
        # [x, y] where x is the type of tile to be placed and y is 0/1 if the tile is there or not
        self.wall = [[[3, 0], [1, 0], [0, 0], [2, 0], [4, 0]],
                     [[4, 0], [3, 0], [1, 0], [0, 0], [2, 0]],
                     [[2, 0], [4, 0], [3, 0], [1, 0], [0, 0]],
                     [[0, 0], [2, 0], [4, 0], [3, 0], [1, 0]],
                     [[1, 0], [0, 0], [2, 0], [4, 0], [3, 0]]]
        
    # Add a tile to the wall
    # This should always be successful with correct validation
    def add_tile(self, row: int, type: int) -> bool:
        for i in range(5):
            if type == self.wall[row][i][0]:
                self.wall[row][i][1] = 1
                return True
        
        return False
    
    # If the tile already exists in the wall we cannot place that tile in the pattern line
    # Checks if the tile already exists in the row and returns False if so (putting it in the patternline is not valid)
    def check_valid_move(self, type: int, row: int) -> bool:
        for i in range(5):
            # we just want to check the square with the same type as we are trying to place
            if self.wall[row][0] == type:
                if self.wall[row][1] == 1:
                    # Already exists so cannot be in the pattern line
                    return False
                else:
                    return True
    
    # Print the contents of the wall
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
        # [type, capacity, length]
        self.pattern_line = [[-1,1,0],[-1,2,0],[-1,3,0],[-1,4,0],[-1,5,0]]
        
    # attempts to place <number> tiles of type <type> into the <row>
    # Returns the number of tiles that overflowed
    # With error return -1
    def add_tiles(self, row: int, type: int, number: int) -> int:
        if number <= 0:
            # Should never triggers
            print("Attempting to Add No Tiles to Pattern Line")
            return -1
        
        if type == self.pattern_line[row][0] or self.pattern_line[row][0] == -1:
            if self.pattern_line[row][1] <= self.pattern_line[row][2]:
                # Already at capacity => error
                return -1
            else:
                self.pattern_line[row][2] += number
                self.pattern_line[row][0] = type
                if self.pattern_line[row][1] < self.pattern_line[row][2]:
                    # More tiles than can fit
                    overflow = self.pattern_line[row][2] - self.pattern_line[row][1]
                    self.pattern_line[row][2] = self.pattern_line[row][1]
                    return overflow
                else:
                    # No over flow
                    return 0
        else:
            # Different type of tile already in the line
            return -1
            
    
    # Check if we can place a tile in a specifics row
    def check_valid_move(self, type: int, row: int) -> bool:
        if self.pattern_line[row][0] != -1 and self.pattern_line[row][0] != type:
            return False
        
        if self.pattern_line[row][1] <= self.pattern_line[row][2]:
            return False
        
        return True

    # Print the each of the pattern lines
    def print_pattern_line(self) -> None:
        color = ["Red       ", "Orange    ", "Black     ", "Blue      ", "Light-Blue"]
        for i in range(5):
            print("Pattern Line", i, end=": ")
            filled = self.pattern_line[i][2]
            for j in range(self.pattern_line[i][1]):
                if filled > 0:
                    print(color[self.pattern_line[i][0]], end=" ")
                    filled -= 1
                else:
                    print("Empty     ", end=" ")
            print()
        print()
            

# Surplus tiles are put in the floor line and count for negative points
class FloorLine:
    def __init__(self) -> None:
        self.floor = [-1, -1, -1, -1, -1, -1, -1] # -1 represents an empty space
        self.points = [-1, -1, -2, -2, -2, -3, -3] # How many points you lose for having a tile there
        self.length = 0
        
    # Add a tile to the floor line (max 7)
    def add_to_floor(self, type: int) -> bool:
        if self.length == 7:
            # already full
            return False
        
        # find the next open spot and insert the tile
        for i in range(7):
            if self.floor[i] == -1:
                # Fill empty space and return true
                self.length += 1
                self.floor[i] = type
                return True
            
        # Should Never Reach this
        return False
                
    # Caluclate the number of negative points you get from the floor line
    def calculate_floor_points(self) -> int:
        total = 0
        for i in range(7):
            if self.floor[i] != -1:
                total += self.points[i]
            else:
                break
        return total
    
    # Print the floor line
    def print_floor(self) -> None:
        color = ["Red", "Orange", "Black", "Blue", "Light-Blue", "First"]
        print("Floor Line: ", end="")
        for i in range(7):
            if self.floor[i] != -1:
                print(color[self.floor[i]], end=" ")
            else:
                print("Empty ", end="")
        print("\n")
    
class Board:
    def __init__(self, player: int) -> None:
        self.player = player
        self.wall = Wall()
        self.pattern_line = PatternLines()
        self.floor = FloorLine()