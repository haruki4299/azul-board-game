from azul_board import Board, Wall

def main():
    print("Testing the board Functionality")
    
    # Test the wall
    wall = Wall()
    wall.print_wall()
    
    wall.add_tile(0, 2)
    wall.add_tile(0, 1)
    wall.add_tile(0, 3)
    wall.add_tile(1, 3)
    wall.print_wall()
    
    
main()