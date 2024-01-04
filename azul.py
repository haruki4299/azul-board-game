from azul_players import HumanPlayer
from azul_factory import Factory
from azul_graphics import AzulGUI
import tkinter as tk

def main():
    print("Welcome to Azul.")
    nPlayers = int(input("How many players would you like to play with?: "))
    if nPlayers not in [2, 3, 4]:
        nPlayers = 4
        
    players = []
    scores = [0,0,0,0]
    for i in range(nPlayers):
        name = input(f"Name of Player {i+1}: ")
        player = HumanPlayer(name)
        players.append(player)
        
    factory = Factory(nPlayers)
        
    root = tk.Tk()
    azul_gui = AzulGUI(root, nPlayers)
    
    # Game Loop
    while True:
        # Reset Displays
        factory.fill_display()
        displays, middle = factory.get_displays()
        azul_gui.update_factory_displays(displays)
        azul_gui.update_factory_middle(middle)
        
        turn = 0
        while True:
            turn = turn % nPlayers
            player = players[turn]
            
            # Player with turn gets red high light on text
            azul_gui.update_player_texts(turn, scores, nPlayers)
            
            # Loop until valid input
            while True:
                display, color = player.choose_tile(nPlayers)
                num_tiles, first = factory.remove_tile(display, color)
                if num_tiles != 0:
                    break
                else:
                    print("Invalid Selection. Try Again")
                    
            displays, middle = factory.get_displays()
            azul_gui.update_factory_displays(displays)
            azul_gui.update_factory_middle(middle)
            
            if first:
                player.board.floor.add_to_floor(5)
                
            player.place_tiles(color, num_tiles)
            pattern_line = player.board.pattern_line.get_pattern_line()
            azul_gui.update_pattern_line(turn, pattern_line)
            floor_line = player.board.floor.get_floor()
            azul_gui.update_floor_line(turn, floor_line)
            
            # check if round ends
            if factory.check_end_round():
                break
            
            turn += 1
        
        scores = []
        # Wall Tiling Phase
        for i in range(nPlayers):
            player = players[i]
            unused = player.wall_tiling()
            factory.update_reserve_tiles(unused)
            
            # Update The Graphics
            wall = player.board.wall.get_wall()
            azul_gui.update_wall_color(i, wall)

            azul_gui.reset_pattern_line(i)
            
            floor_line = player.board.floor.get_floor()
            azul_gui.update_floor_line(i, floor_line)
            
            scores.append(player.board.point_tally)
            
        azul_gui.update_player_texts(turn, scores, nPlayers)

if __name__ == '__main__':
    main()