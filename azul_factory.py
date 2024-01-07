import random

# Represent tiles on display as an array of integers with index representing how many of the type
# example [Red, Orange, Black, Blue, Light Blue, First] --> [0, 3, 1, 0, 0, 0] = 3 oranges and 1 black
# Tile type => "Red": 0, "Orange": 1, "Black": 2, "Blue": 3, "Light Blue": 4, "First": 5

# Class representing the bag in which we draw tiles to the factory from
class Bag:
    def __init__(self) -> None:
        self.contents = [20, 20, 20, 20, 20] # init with 20 of each tile
        self.size = 100
        
    # Draw a random tile from the bag
    # Return integer representing the tile type
    def draw_tile(self) -> int:
        if self.size == 0:
            # Should never happen => always call refill_bag before
            return -1
        
        # Choose a random number until it corresponds to a tile that is still in the bag
        while True:
            index = random.randint(0, 4)
            if self.contents[index] != 0:
                self.contents[index] -= 1
                self.size -= 1
                return index
    
    # If there is nothing in the bag, refill the bag with the tiles out of the game
    def refill_bag(self, reserve_tiles: list[int]) -> None:
        # Only Refill if there are no more in the bag
        if self.size == 0:
            print("Refilling Bag")
            for i in range(5):
                self.contents[i] = reserve_tiles[i]
                self.size += reserve_tiles[i]
                reserve_tiles[i] = 0

# The middle of the factory. Tiles that were not taken on the display go here. "First" tile goes here at start
class FactoryMiddle:
    def __init__(self) -> None:
        # Initialize with just the first marker tile
        self.tiles = [0, 0, 0, 0, 0, 1]
        self.size = 0 # do not count the first marker 
        
    # Once tiles are taken from a factory display get list of remaining tiles
    # all of the rest of the tiles get put in the middle
    def add_tiles(self, tile_array: list[int]) -> None:
        for i, tile in enumerate(tile_array):
            self.tiles[i] += tile
            self.size += tile
       
    # Remove one type of tile from the middle
    # If this is the first time a tile is taken from the middle 
    # return true so that the first marker can also be taken
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
    
    def get_middle(self):
        return self.tiles
                
        
# Represents a single factory display
class FactoryDisplay:
    def __init__(self) -> None:
        self.tiles = [0, 0, 0, 0, 0]
        self.size = 0
    
    # Add a single tile to the display (four max)
    # Return Bool indicating whether we were able to add or not
    def add_tile(self, type: int) -> bool:
        if self.size <= 4:
            self.tiles[type] += 1
            self.size += 1
        else:
            return False
    
    # Remove a single type of tile from the display
    # Return the number of tiles taken and list indicating the types and number of tiles to go into the middle
    # If unable to remove the tile return -1
    def remove_tile(self, type: int) -> (int, list[int]):
        unused_tiles = [0, 0, 0, 0, 0]
        num_tiles = self.tiles[type]
        
        if num_tiles == 0:
            return num_tiles, unused_tiles
        else:
            self.tiles[type] = 0
            self.size = 0
            
        for i in range(5):
            unused_tiles[i] = self.tiles[i]
            self.tiles[i] = 0
            
        return num_tiles, unused_tiles
    
    def get_display(self):
        return self.tiles
        
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
                
    def get_tile_color(self, display_num, tile_num):
        if display_num == -1:
            return tile_num
        else:
            display = self.displays[display_num]
            for i in range(5):
                tile_num -= display.tiles[i]
                if tile_num < 0:
                    return i
        # error: should return before this
        return -1
            
        
    # Fill display with 4 tiles each from the bag
    def fill_display(self) -> None:
        for display in self.displays:
            # Four tiles per display
            for i in range(4):
                self.bag.refill_bag(self.reserve_tiles) # Only refills if the bag is empty
                tile = self.bag.draw_tile()
                display.add_tile(tile)
        
        self.middle.tiles[5] = 1
    
    # Remove one type of tile from a factory display
    # Returns how many tiles were found of the type and a list of the rest of the tiles
    # If we took first from the middle (-1) return True as well
    def remove_tile(self, which_display: int, type: int) -> (int, bool):
        first = False
        if which_display == -1:
            num_tiles, first = self.middle.remove_tiles(type)
        else:
            display = self.displays[which_display]
            num_tiles, unused_tiles = display.remove_tile(type)

            # Move unused tiles to the middle
            self.middle.add_tiles(unused_tiles)
        
        return num_tiles, first
    
    # Checks if we are at the end of the round. 
    # Which is when we don't have anymore tiles in the factory
    def check_end_round(self) -> bool:
        if self.middle.size == 0:
            for display in self.displays:
                if display.size != 0:
                    return False
            return True
        return False
    
    def update_reserve_tiles(self, tile_array: list[int]) -> None:
        for i in range(5):
            self.reserve_tiles[i] += tile_array[i]
    
    # Print what is in the display
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
        
    def get_displays(self):
        displays = []
        for display in self.displays:
            displays.append(display.get_display())
            
        middle = self.middle.get_middle()
        
        return displays, middle