from azul_board import Board, Wall, FloorLine, PatternLines

def main():
    print("Testing the board Functionality")
    """
    # Test the wall
    wall = Wall()
    wall.print_wall()
    
    
    print(wall.add_tile(0, 0)) # 1 point
    print(wall.add_tile(1, 0)) # 1 point
    print(wall.add_tile(1, 2)) # 2 points
    print(wall.add_tile(3, 4)) # 1 point
    print(wall.add_tile(4, 2)) # 2 points
    print(wall.add_tile(2, 4)) # 1 point
    print(wall.add_tile(2, 1)) # 2 points
    print(wall.add_tile(2, 3)) # 6 points
    
    wall.print_wall()
    print("---------------------------------")
   
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
    print("---------------------------------\n")
    
    # Test Pattern Line
    pattern = PatternLines()
    pattern.print_pattern_line()
    print(pattern.pattern_line)
    
    print(pattern.add_tiles(0, 1, 2)) # Should print 1
    print(pattern.add_tiles(0, 1, 2)) # Should print -1
    print(pattern.pattern_line)
    
    print(pattern.add_tiles(1, 1, 2)) # Should print 0
    print(pattern.add_tiles(2, 3, 2)) # Should print 0
    print(pattern.add_tiles(2, 2, 2)) # Should print -1
    print(pattern.add_tiles(3, 4, 4)) # Should print 0
    print(pattern.add_tiles(4, 2, 3)) # Should print 0
    
    pattern.print_pattern_line()
    """
    # Overall integration
    board = Board()
    
    board.print_board()
    
    board.place_tile(0, 1, 2)
    board.place_tile(0, 2, 1)
    board.place_tile(1, 2, 2)
    board.place_tile(3, 4, 4)
    
    board.print_board()
    
    board.move_tiles()
    
    board.print_board()
    
main()