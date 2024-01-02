import tkinter as tk

class AzulGUI:
    def __init__(self, root, nPlayers: int):
        self.root = root
        self.root.title("Azul Game Board")
        
        self.nPlayers = nPlayers
        
        self.player_pattern_line = []
        self.player_wall = []
        self.player_floor = []

        # Create canvas to draw on
        self.canvas = tk.Canvas(root, width=1200, height=800, bg="green")
        self.canvas.pack()

        # Draw dividing lines
        self.draw_dividing_lines()
        
        self.draw_factory()
        
        self.draw_player_board(1)
        self.draw_player_board(2)
        self.draw_player_board(3)
        self.draw_player_board(4)

        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_dividing_lines(self):
        # Draw vertical line separating left and right areas
        self.canvas.create_line(600, 0, 600, 350, fill="black", width=2)
        self.canvas.create_line(600, 450, 600, 800, fill="black", width=2)

    def draw_player_board(self, player: int):
        # Draw Pattern Line
        if player == 1:
            topLeftx = 20
            topLefty = 20
        elif player == 2:
            topLeftx = 620
            topLefty = 20
        elif player == 3:
            topLeftx = 20
            topLefty = 470
        elif player == 4:
            topLeftx = 620
            topLefty = 470
        
        pattern_line_squares = []
        # Pattern Line Squares
        for i in range(1,6):
            for j in range(1, i+1):
                square_id = self.canvas.create_rectangle(
                    topLeftx + 3 + 50 * (5 - j),
                    topLefty + 3 + 50 * (i - 1),
                    topLeftx + 47 + 50 * (5 - j),
                    topLefty + 47 + 50 * (i - 1),
                    outline="black",
                    width=2
                )
                pattern_line_squares.append(square_id)
        print(pattern_line_squares)
        self.player_pattern_line.append(pattern_line_squares)
                
        # Draw Wall
        wall_squares = []
        for i in range(5):
            for j in range(5):
                x1 = topLeftx + 300 + 3 + 50 * j
                y1 = topLefty + 3 + 50 * i
                x2 = topLeftx + 300 + 47 + 50 * j
                y2 = topLefty + 47 + 50 * i

                square_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
                wall_squares.append(square_id)
        self.player_wall.append(wall_squares)


        # Draw Floor
        floor_squares = []
        for i in range(7):
            x1 = topLeftx + 3 + 50 * i
            y1 = topLefty + 260 + 3
            x2 = topLeftx + 47 + 50 * i
            y2 = topLefty + 260 + 47

            square_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
            floor_squares.append(square_id)
        self.player_floor.append(floor_squares)
            
        # Display Player Name and Points
        self.canvas.create_text(topLeftx + 450, topLefty + 280, text=f"Player {player}: {0} points", font=("Arial", 24), fill="white")

    def draw_factory(self):
        self.draw_middle()
        if self.nPlayers == 4:
            for i in range(9):
                self.draw_factory_display(i)
        
    def draw_factory_display(self, num:int):
        start = 180 + 110 * num
        # Draw Four Squares
        self.canvas.create_line(start + 3, 353, start + 3, 397, fill="black", width=2)
        self.canvas.create_line(start + 47, 353, start + 47, 397, fill="black", width=2)
        self.canvas.create_line(start + 3, 353, start + 47, 353, fill="black", width=2)
        self.canvas.create_line(start + 3, 397, start + 47, 397, fill="black", width=2)
        
        self.canvas.create_line(start + 3, 403, start + 3, 447, fill="black", width=2)
        self.canvas.create_line(start + 47, 403, start + 47, 447, fill="black", width=2)
        self.canvas.create_line(start + 3, 403, start + 47, 403, fill="black", width=2)
        self.canvas.create_line(start + 3, 447, start + 47, 447, fill="black", width=2)
        
        self.canvas.create_line(start + 53, 353, start + 53, 397, fill="black", width=2)
        self.canvas.create_line(start + 97, 353, start + 97, 397, fill="black", width=2)
        self.canvas.create_line(start + 53, 353, start + 97, 353, fill="black", width=2)
        self.canvas.create_line(start + 53, 397, start + 97, 397, fill="black", width=2)
        
        self.canvas.create_line(start + 53, 403, start + 53, 447, fill="black", width=2)
        self.canvas.create_line(start + 97, 403, start + 97, 447, fill="black", width=2)
        self.canvas.create_line(start + 53, 403, start + 97, 403, fill="black", width=2)
        self.canvas.create_line(start + 53, 447, start + 97, 447, fill="black", width=2)
        
    def draw_middle(self):
        # Square for Red
        self.canvas.create_line(23, 353, 23, 397, fill="red", width=2)
        self.canvas.create_line(67, 353, 67, 397, fill="red", width=2)
        self.canvas.create_line(23, 353, 67, 353, fill="red", width=2)
        self.canvas.create_line(23, 397, 67, 397, fill="red", width=2)
        
        # Square for Orange
        self.canvas.create_line(23, 403, 23, 447, fill="orange", width=2)
        self.canvas.create_line(67, 403, 67, 447, fill="orange", width=2)
        self.canvas.create_line(23, 403, 67, 403, fill="orange", width=2)
        self.canvas.create_line(23, 447, 67, 447, fill="orange", width=2)
        
        # Square for Black
        self.canvas.create_line(73, 353, 73, 397, fill="black", width=2)
        self.canvas.create_line(117, 353, 117, 397, fill="black", width=2)
        self.canvas.create_line(73, 353, 117, 353, fill="black", width=2)
        self.canvas.create_line(73, 397, 117, 397, fill="black", width=2)
        
        # Square for Blue
        self.canvas.create_line(73, 403, 73, 447, fill="blue", width=2)
        self.canvas.create_line(117, 403, 117, 447, fill="blue", width=2)
        self.canvas.create_line(73, 403, 117, 403, fill="blue", width=2)
        self.canvas.create_line(73, 447, 117, 447, fill="blue", width=2)
        
        # Square for Light Blue
        self.canvas.create_line(123, 353, 123, 397, fill="light blue", width=2)
        self.canvas.create_line(167, 353, 167, 397, fill="light blue", width=2)
        self.canvas.create_line(123, 353, 167, 353, fill="light blue", width=2)
        self.canvas.create_line(123, 397, 167, 397, fill="light blue", width=2)
        
        # Square for Light Blue
        self.canvas.create_line(123, 403, 123, 447, fill="white", width=2)
        self.canvas.create_line(167, 403, 167, 447, fill="white", width=2)
        self.canvas.create_line(123, 403, 167, 403, fill="white", width=2)
        self.canvas.create_line(123, 447, 167, 447, fill="white", width=2)
        

    def on_canvas_click(self, event):
        # Event handler for mouse click on the canvas
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        print(f"Clicked at coordinates: ({x}, {y})")
        
        square_id = self.player_pattern_line[1][3]
        self.canvas.itemconfig(square_id, fill="red")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    azul_gui = AzulGUI(root, 4)
    azul_gui.run()
