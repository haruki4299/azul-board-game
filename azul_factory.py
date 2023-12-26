import random

# Index List => "Red": 0, "Orange": 1, "Black": 2, "Blue": 3, "Light Blue": 4, "First": 5
     
class Bag:
    def __init__(self) -> None:
        self.contents = [20, 20, 20, 20, 20]
        self.size = 100
        
    # Draw a tile from the bag
    # Return integer representing the tile type
    def draw_tile(self) -> int:
        if self.size == 0:
            # Should reset tile 
            return -1
        
        while True:
            index = random.randint(0, 4)
            if self.contents[index] != 0:
                self.contents[index] -= 1
                self.size -= 1
                return index
            
    def refill_bag(self, reserve_tiles: list[int]) -> None:
        # Only Refill if there are no more in the bag
        if self.size == 0:
            print("Refilling Bag")
            for i in range(5):
                self.contents[i] = reserve_tiles[i]
                self.size += reserve_tiles[i]
                reserve_tiles[i] = 0
    
# Represent tiles on display as an array of integers with index representing how many of the type
# example [Red, Orange, Black, Blue, Light Blue, First] --> [0, 3, 1, 0, 0, 0] = 3 oranges and 1 black

class FactoryMiddle:
    def __init__(self) -> None:
        # Initialize with just the first marker tile
        self.tiles = [0, 0, 0, 0, 0, 1]
        self.size = 0
        
    # Once tiles are taken from a factory display all of the rest of the tiles get put in the middle
    def add_tiles(self, tile_array: list[int]) -> None:
        for i, tile in enumerate(tile_array):
            self.tiles[i] += tile
            self.size += tile
       
    # Remove all of one type of array 
    # If this is the first time a tile is taken from the middle return true
    def remove_tiles(self, type: int) -> (int, bool):
        num_tiles = self.tiles[type]
        # If num tiles is 0 then this is an invalid pick
        if num_tiles == 0:
            return 0, False
        
        # Remove tiles of the type 
        self.tiles[type] = 0
        self.size -= num_tiles
    
        # If num_tiles is not 0, check if this is the first time we take from the middle
        if self.tiles[5] != 0:
            self.tiles[5] = 0
            return num_tiles, True
        else:
            return num_tiles, False
                
        
# Represents a single factory display
class FactoryDisplay:
    def __init__(self) -> None:
        self.tiles = [0, 0, 0, 0, 0]
        self.size = 0
    
    # Return Bool indicating whether we were able to add or not
    def add_tile(self, type: int) -> bool:
        if self.size <= 4:
            self.tiles[type] += 1
            self.size += 1
        else:
            return False
    
    # Return a list indicating the types and number of tiles to go into the middle
    def remove_tile(self, type: int) -> (bool, list[int]):
        unused_tiles = [0, 0, 0, 0, 0]
        num_tiles = self.tiles[type]
        
        if num_tiles == 0:
            return False, unused_tiles
        else:
            self.tiles[type] = 0
            self.size = 0
            
        for i in range(5):
            unused_tiles = self.tiles[i]
            self.tiles[i] = 0
    
        return True, unused_tiles
        
# Represents all of the factory: includes factory display, middle area, and the bag of tiles
class Factory:
    def __init__(self,  nPlayers: int) -> None:
        self.displays = [] #List of factory displays
        self.numDisplays= 0
        self.middle = FactoryMiddle()
        self.bag = Bag()
        self.reserve_tiles = [0, 0, 0, 0, 0] # Keep Track of tiles that are currently out of the game for when we need to refill the bag
        
        # Set number of displays based on number of players
        if nPlayers == 2:
            self.numDisplays = 5
            for i in range(self.numDisplays):
                display = FactoryDisplay()
                self.displays.append(display)
        elif nPlayers == 3:
            self.numDisplays = 7
            for i in range(self.numDisplays):
                display = FactoryDisplay()
                self.displays.append(display)
        else: # nPlayers == 4 / Default to 4 players if invalid input
            self.numDisplays = 9
            for i in range(self.numDisplays):
                display = FactoryDisplay()
                self.displays.append(display)
        
    def fill_display(self) -> None:
        for display in self.displays:
            # Four tiles per display
            for i in range(4):
                self.bag.refill_bag(self.reserve_tiles) # Only refills if the bag is empty
                tile = self.bag.draw_tile()
                display.add_tile(tile)
    
    # Remove one type of tile from a factory display
    # Returns how many tiles were found of the type and a list of the rest of the tiles
    def remove_tile(self, which_display: int, type: int) -> (int, list[int]):
        unused_tiles = [0, 0, 0, 0, 0]
        display = self.displays[which_display]
        num_tiles = display.tiles[type]
        
        if num_tiles == 0:
            return num_tiles, unused_tiles

        display.tiles[type] = 0
        display.size = 0
        # Move unused tiles to the middle
        self.middle.add_tiles(display.tiles)
        
        return num_tiles, unused_tiles
    
    def remove_tile_from_game(self, unused_tiles: list[int]):
        for i, num in enumerate(unused_tiles):
            self.reserve_tiles[i] += num
    
    def print_displays(self):
        color = ["Red", "Orange", "Black", "Blue", "Light Blue"]
        for i, display in enumerate(self.displays):
            print("Display", i, " ", end="")
            if display.size != 0:
                for j, tile in enumerate(display.tiles):
                    print(color[j], ":", tile, end=" ")
            else:
                print("Empty", end="")
            print()
        
        print("Middle ", end="")
        for i, tile in enumerate(self.middle.tiles):
            if i != 5:
                print(color[i], ":", tile, end=" ")
            else:
                print("First: ", tile, end=" ")
        print()