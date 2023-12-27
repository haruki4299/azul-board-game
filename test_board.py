from azul_board import Board, Wall, FloorLine

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
    
    
    # Test Floor
    floor = FloorLine()
    floor.print_floor()
    
    floor.add_to_floor(5)
    floor.add_to_floor(2)
    floor.add_to_floor(2)
    print(floor.calculate_floor_points()) # Should be -1 + -1 + -2 = -4
    floor.add_to_floor(1)
    floor.add_to_floor(1)
    floor.add_to_floor(4)
    floor.add_to_floor(3)
    print(floor.add_to_floor(2))
    floor.print_floor()
    print(floor.calculate_floor_points()) # Should be -14
    
main()