import azul_factory

def main():
    bag = azul_factory.Bag()
    print(bag.draw_tile().type)

if __name__ == '__main__':
    main()