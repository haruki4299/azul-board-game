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
        display, color = player1.choose_tile()
        num_tiles, first = factory.remove_tile(display, color)
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
        display, color = player2.choose_tile()
        num_tiles, first = factory.remove_tile(display, color)
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

    