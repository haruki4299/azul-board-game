from azul_factory import Factory, Bag

def main():
    # Test Bag
    bag = Bag()
    print(bag.size)
    print(bag.contents)
    
    for i in range(10):
        print(bag.draw_tile())
    
    print(bag.size)
    print(bag.contents)
    
    for i in range(90):
        bag.draw_tile()
        
    print(bag.size)
    print(bag.contents)
    
    bag.refill_bag([15, 15, 15, 17, 19])
    
    print(bag.size)
    print(bag.contents)
    
    # Test with Four Players
    print("Testing with four players\n")
    factory = Factory(4)
    factory.fill_display()
    print(factory.bag.size)
    factory.print_displays()
    factory.reserve_tiles = [10, 10, 10, 12, 2]
    
    while not factory.check_end():
        which_display = int(input("Enter Display: "))
        type = int(input("Enter Type: "))
        num_tiles = factory.remove_tile(which_display, type)
        print("Number of Tiles: ", num_tiles)
        factory.print_displays()
        
    factory.fill_display()
    print(factory.bag.size)
    factory.print_displays()
    
    while not factory.check_end():
        which_display = int(input("Enter Display: "))
        type = int(input("Enter Type: "))
        num_tiles = factory.remove_tile(which_display, type)
        print("Number of Tiles: ", num_tiles)
        factory.print_displays()
        
    factory.fill_display()
    print(factory.bag.size)
    factory.print_displays()
    

if __name__ == '__main__':
    main()