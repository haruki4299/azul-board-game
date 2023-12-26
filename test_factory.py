from azul_factory import Factory

def main():
    factory = Factory(2)
    factory.fill_display()
    factory.print_displays()
    
    which_display = int(input("Enter Display: "))
    type = int(input("Enter Type: "))
    num_tiles, unused_tiles = factory.remove_tile(which_display, type)
    print("Number of Tiles: ", num_tiles)
    
    factory.print_displays()
    
    type = int(input("Enter Type: "))
    factory.middle.remove_tiles(type)
    
    factory.print_displays()

if __name__ == '__main__':
    main()