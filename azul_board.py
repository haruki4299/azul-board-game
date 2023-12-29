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
    
    # Score 
    def place_tile_points(self, row: int, col: int) -> int:
        # Count vertical runs
        vertical_runs = 1
        for i in range(row - 1, -1, -1):
            if self.wall[i][col][1] == 1:
                vertical_runs += 1
            else:
                break

        for i in range(row + 1, 5):
            if self.wall[i][col][1] == 1:
                vertical_runs += 1
            else:
                break

        # Count horizontal runs
        horizontal_runs = 1
        for i in range(col - 1, -1, -1):
            if self.wall[row][i][1] == 1:
                horizontal_runs += 1
            else:
                break

        for i in range(col + 1, 5):
            if self.wall[row][i][1] == 1:
                horizontal_runs += 1
            else:
                break

        # Calculate total points
        if horizontal_runs > 1 and vertical_runs > 1:
            # Then we count the middle twice
            total_points = vertical_runs + horizontal_runs
        else:
            # There is only one of horizontal or vertical connections or the tile is by itself
            total_points = max(vertical_runs, horizontal_runs)

        return total_points
    
    # Add a tile to the wall
    # This should always be successful with correct validation
    def add_tile(self, row: int, type: int) -> (bool, int):
        for i in range(5):
            if type == self.wall[row][i][0]:
                if self.wall[row][i][1] == 1:
                    # Tile already there
                    break
                self.wall[row][i][1] = 1
                points = self.place_tile_points(row, i)
                return True, points
        
        return False, 0
    
    # If the tile already exists in the wall we cannot place that tile in the pattern line
    # Checks if the tile already exists in the row and returns False if so (putting it in the patternline is not valid)
    def check_valid_move(self, type: int, row: int) -> bool:
        for i in range(5):
            # we just want to check the square with the same type as we are trying to place
            if self.wall[row][i][0] == type:
                if self.wall[row][i][1] == 1:
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
    
    # Calculate Extra Points at the End of the game
    # Find horizontal (2 points), vertical (5 points), and all of one type (10 points) 
    def calculate_points(self) -> int:
        # Horizontal Line
        h_lines = 0
        for i in range(5):
            count = 0
            for j in range(5):
                if self.wall[i][j][1] == 0:
                    break
                else:
                    count += 1
            if count == 5:
                h_lines += 1
                
        # Vertical Line
        v_lines = 0
        for i in range(5):
            count = 0
            for j in range(5):
                if self.wall[j][i][1] == 0:
                    break
                else:
                    count += 1
            if count == 5:
                v_lines += 1
                
        # Each type
        total_points = 0
        num_tile_on_wall = [0, 0, 0, 0, 0] # type 0 - 4
        for i in range(5):
            for j in range(5):
                if self.wall[i][j][0] == 0 and self.wall[i][j][1] == 1:
                    num_tile_on_wall[0] += 1
                elif self.wall[i][j][0] == 1 and self.wall[i][j][1] == 1:
                    num_tile_on_wall[1] += 1
                elif self.wall[i][j][0] == 2 and self.wall[i][j][1] == 1:
                    num_tile_on_wall[2] += 1
                elif self.wall[i][j][0] == 3 and self.wall[i][j][1] == 1:
                    num_tile_on_wall[3] += 1
                elif self.wall[i][j][0] == 4 and self.wall[i][j][1] == 1:
                    num_tile_on_wall[4] += 1
        for num in num_tile_on_wall:
            if num == 5:
                total_points += 10
                
        # Add the rest
        total_points += (h_lines * 2 + v_lines * 5)
        
        return total_points

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
    def __init__(self) -> None:
        self.wall = Wall()
        self.pattern_line = PatternLines()
        self.floor = FloorLine()
        
        self.point_tally = 0
        
    def place_tile(self, row: int, type: int, number_of_tiles: int) -> None:
        # First check if placing the tile there is a valid move
        if self.pattern_line.check_valid_move(type, row) and self.wall.check_valid_move(type, row):
            overflow_tiles = self.pattern_line.add_tiles(row, type, number_of_tiles)
        else:
            # If not valid move place them all to the floor line
            overflow_tiles = number_of_tiles
            
        # Add any overflow tiles to the floor line
        for i in range(overflow_tiles):
            suc = self.floor.add_to_floor(type)
            print("Adding to Floor ", suc) # Later do something to keep track of tiles if we were not able to add to floor -> goes in box irl
      
    # Calculate Extra Points at the End of the game
    # Find horizontal (2 points), vertical (5 points), and all of one type (10 points) 
    def calculate_points(self) -> None:
        wall_points = self.wall.calculate_points()
        deductions = self.floor.calculate_floor_points()
        
        self.point_tally += (wall_points + deductions)
        
    def move_tiles(self) -> list[int]:
        unused_tiles = [0, 0, 0, 0, 0]
        total_points = 0
        
        for i in range(5):
            type = self.pattern_line.pattern_line[i][0]
            if type != -1 and self.pattern_line.pattern_line[i][1] == self.pattern_line.pattern_line[i][2]:
                success, point = self.wall.add_tile(i, type)
                total_points += point
            
                if success == False:
                    # Should never happen
                    print("Error Failed to add tile to Wall")
                    
                unused_tiles[type] += (self.pattern_line.pattern_line[i][2] - 1)
            elif type != -1:
                unused_tiles[type] += self.pattern_line.pattern_line[i][2]
        
        self.point_tally += total_points
        
        return unused_tiles
    
    # One Horizontal Line is Game End
    def check_end_game(self) -> None:
        # Check each row
        for i in range(5):
            count = 0
            for j in range(5):
                count += self.wall.wall[i][j][1]
            if count == 5:
                return True
        return False
        
    def print_board(self) -> None:
        print("Pattern Line:")
        self.pattern_line.print_pattern_line()
        print("Wall:")
        self.wall.print_wall()
        print("Floor Line:")
        self.floor.print_floor()
        print("Points Total: ", self.point_tally, end="\n\n")