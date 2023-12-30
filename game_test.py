from azul_players import HumanPlayer
from azul_factory import Factory

# Simulate a game

player1 = HumanPlayer("Player1")
player2 = HumanPlayer("Player2")

factory = Factory(2)

# Game Loop
while True:
    # Reset Displays
    factory.fill_display()
    
    # Keep on taking tiles until empty (Round)
    while True:
        # Player1 chooses tiles
        print("Player1 chooses tiles")
        factory.print_displays()
        while True:
            display, color = player1.choose_tile(2)
            num_tiles, first = factory.remove_tile(display, color)
            print(num_tiles)
            if num_tiles != 0:
                break
            else:
                print("Invalid Selection. Try Again")
        if first:
            player1.board.floor.add_to_floor(5)
        player1.board.print_board()
        player1.place_tiles(color, num_tiles)
        player1.board.print_board()
        
        # check if round ends
        if factory.check_end_round():
            break
        
        print("Player2 chooses tiles")
        # Player2 chooses tiles
        factory.print_displays()
        while True:
            display, color = player2.choose_tile(2)
            num_tiles, first = factory.remove_tile(display, color)
            if num_tiles != 0:
                break
            else:
                print("Invalid Selection. Try Again")
        if first:
            player2.board.floor.add_to_floor(5)
        player2.board.print_board()
        player2.place_tiles(color, num_tiles)
        player2.board.print_board()
        
        # check if round ends
        if factory.check_end_round():
            break
        
    # Wall tiling phase
    print("Player1 Wall Tiling")
    unused = player1.wall_tiling()
    factory.update_reserve_tiles(unused)
    player1.print_board()
    
    print("Player2 Wall Tiling")
    unused = player2.wall_tiling()
    factory.update_reserve_tiles(unused)
    player2.print_board()
        
    if player1.board.check_end_game() or player2.board.check_end_game():
        print("Game End")
        break

# Final Point calculation
player1.board.calculate_points()
player2.board.calculate_points()

print("Final:")
print("Player1: ", player1.get_points())
print("Player2: ", player2.get_points())