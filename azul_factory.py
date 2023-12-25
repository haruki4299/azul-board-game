import random

class Tile:
    def __init__(self, type) -> None:
        self.type = type # Types: Red, Orange, Black, Blue, Light Blue, First
        
class Bag:
    def __init__(self) -> None:
        self.contents = []
        self.size = 100
        
        # Add 20 of each tile
        for i in range(20):
            self.contents.append(Tile("Red"))
            self.contents.append(Tile("Orange"))
            self.contents.append(Tile("Black"))
            self.contents.append(Tile("Blue"))
            self.contents.append(Tile("Light Blue"))
        
        # Shuffle the contents
        random.shuffle(self.contents)
        
    # Draw a tile from the bag
    def draw_tile(self) -> Tile:
        if self.size == 0:
            # Should reset tile size 
            return None

        return self.contents.pop()
    
class FactoryMiddle:
    def __init__(self) -> None:
        self.tiles = []
        self.size = 0
        
        tile = Tile("First")
        self.tiles.append(tile)
        self.size += 1
        
    def add_tile(self, tile: Tile):
        self.tiles.append(tile)
        self.size += 1
        
    def remove_tiles(self, type) -> (int, bool):
        count = 0
        isFirst = False
        updated_tiles = []
        
        for tile in self.tiles:
            if tile.type == type:
                count += 1
            elif tile.type == "First":
                isFirst = True
            else:
                updated_tiles.append(tile)
            
        self.tiles = updated_tiles
        self.size = len(updated_tiles)
        
        return count, isFirst        
        
class FactoryTile:
    def __init__(self) -> None:
        self.tiles = []
        self.size = 0

class FactoryDisplay:
    def __init__(self,  nPlayers: int) -> None:
        self.displays = []
        self.numDisplays= 0
        self.middle = FactoryMiddle()
        
        if nPlayers == 2:
            self.numDisplays = 5
            for i in range(self.numDisplays):
                tile = FactoryTile()
                self.displays.append(tile)
        elif nPlayers == 3:
            self.numDisplays = 7
            for i in range(self.numDisplays):
                tile = FactoryTile()
                self.displays.append(tile)
        else: # nPlayers == 4 / Default to 4 players if invalid input
            self.numDisplays = 9
            for i in range(self.numDisplays):
                tile = FactoryTile()
                self.displays.append(tile)
        
    def fill_display():
        pass
    
    def remove_tiles():
        pass