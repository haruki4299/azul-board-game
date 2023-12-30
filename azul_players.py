from azul_board import Board

class HumanPlayer:
    def __init__(self, name) -> None:
        self.name = name
        self.board = Board()
        
    def choose_tile(self, nPlayers: int) -> (int, int):
        while True:
            display = int(input("Which display do you want to take tiles from?"))
            color = int(input("Which type of tile will you take? (Red: 0, Orange: 1, Black: 2, Blue: 3, Light Blue: 4): "))
            
            if display >= -1 and display <= (1 + nPlayers * 2) and color >= 0 and color <= 4:
                break
            
            print("Invalid Input. Select Again.")

        return display, color
    
    def place_tiles(self, type: int, number_of_tiles: int) -> None:
        row = int(input("Which Pattern Line would you like to put the tile at?: "))
        self.board.place_tile(row, type, number_of_tiles)
        self.board.print_board()
        
    def wall_tiling(self) -> list[int]:
        # Move tiles from pattern line to the wall
        unused = self.board.move_tiles()
        
        # unused tiles should be in the box (reserve) until refill
        return unused
        
    def get_points(self) -> int:
        return self.board.point_tally
    
    def print_board(self) -> None:
        name = self.name + "'s Board"
        print(name)
        self.board.print_board()

class ComputerPlayer:
    def __init__(self) -> None:
        self.board = Board()
        self.total_points = 0