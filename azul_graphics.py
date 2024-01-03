import tkinter as tk

class tile_display:
    def __init__(self, canvas, x1, y1, x2, y2, fill):
        self.canvas = canvas
        self.rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill)
        self.text_id = None
        
    def add_text(self, text, font=("Arial", 12), fill="white"):
        # Get the coordinates of the center of the rectangle
        x1, y1, x2, y2 = self.canvas.coords(self.rect_id)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # Create text and associate it with the rectangle
        self.text_id = self.canvas.create_text(center_x, center_y, text=text, font=font, fill=fill)

    def update_text(self, new_text):
        if self.text_id:
            # Update the text content
            self.canvas.itemconfig(self.text_id, text=new_text)

class AzulGUI:
    def __init__(self, root, nPlayers: int, pattern_lines: list[list[list[int]]], walls: list[list[list[list[int]]]], floor: list[int], scores: list[int]):
        self.root = root
        self.root.title("Azul Game Board")
        
        self.nPlayers = nPlayers
        
        self.player_pattern_line = []
        self.player_wall = []
        self.player_floor = []
        self.player_points = []

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
        
        self.update_color(pattern_lines, walls, floor, scores)

        tile = tile_display(self.canvas, 100, 100, 200, 200, "black")
        tile.add_text("1")

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
        text_id = self.canvas.create_text(topLeftx + 450, topLefty + 280, text=f"Player {player}: {0} points", font=("Arial", 24), fill="white")
        self.player_points.append(text_id)

    def draw_factory(self):
        self.draw_middle()
        if self.nPlayers == 4:
            for i in range(9):
                self.draw_factory_display(i)
        
    def draw_factory_display(self, num: int):
        start = 180 + 110 * num

        # Draw first square
        self.canvas.create_rectangle(start + 3, 353, start + 47, 397, outline="black", width=2)
        # Draw second square
        self.canvas.create_rectangle(start + 3, 403, start + 47, 447, outline="black", width=2)
        # Draw third square
        self.canvas.create_rectangle(start + 53, 353, start + 97, 397, outline="black", width=2)
        # Draw fourth square
        self.canvas.create_rectangle(start + 53, 403, start + 97, 447, outline="black", width=2)
        
    def draw_middle(self):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        start_x = [23, 23, 73, 73, 123, 123]
        start_y = [353, 403, 353, 403, 353, 403]

        for i in range(len(colors)):
            x1, y1 = start_x[i], start_y[i]
            x2, y2 = x1 + 44, y1 + 44  # Width and height set to 44 for consistency

            self.canvas.create_rectangle(x1, y1, x2, y2, outline=colors[i], width=2)

    def update_factory(self, factory_tiles):
        pass
        
    def update_color(self, pattern_lines, walls, floor_line, scores):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        
        fill_color = 0
        # Update Pattern Lines
        for i in range(4):
            num_tiles = pattern_lines[i][0][2]
            fill_color = pattern_lines[i][0][0]
            for j in range(num_tiles):
                square_id = self.player_pattern_line[i][j]
                self.canvas.itemconfig(square_id, fill=colors[fill_color])
            num_tiles = pattern_lines[i][1][2]
            fill_color = pattern_lines[i][1][0]
            for j in range(num_tiles):
                square_id = self.player_pattern_line[i][1+j]
                self.canvas.itemconfig(square_id, fill=colors[fill_color])
            num_tiles = pattern_lines[i][2][2]
            fill_color = pattern_lines[i][2][0]
            for j in range(num_tiles):
                square_id = self.player_pattern_line[i][3+j]
                self.canvas.itemconfig(square_id, fill=colors[fill_color])
            num_tiles = pattern_lines[i][3][2]
            fill_color = pattern_lines[i][3][0]
            for j in range(num_tiles):
                square_id = self.player_pattern_line[i][6+j]
                self.canvas.itemconfig(square_id, fill=colors[fill_color])
            num_tiles = pattern_lines[i][4][2]
            fill_color = pattern_lines[i][4][0]
            for j in range(num_tiles):
                square_id = self.player_pattern_line[i][10+j]
                self.canvas.itemconfig(square_id, fill=colors[fill_color])
                
        # Update Wall Color
        for i in range(4):
            for j in range(25):
                square_id = self.player_wall[i][j]
                fill_color = walls[i][j//5][j%5][0]
                if walls[i][j//5][j%5][1]:
                    self.canvas.itemconfig(square_id, fill=colors[fill_color])
                    
        # Update Floor Line
        for i in range(4):
            for j in range(7):
                square_id = self.player_floor[i][j]
                fill_color = floor_line[i][j]
                if fill_color != -1:
                    self.canvas.itemconfig(square_id, fill=colors[fill_color])
                    
        # Update Points Text
        for i in range(4):
            text_id = self.player_points[i]
            point = scores[i]
            self.canvas.itemconfig(text_id, text=f"Player {i+1}: {point} points")
            
        # Update Factory Displays
        

    def on_canvas_click(self, event):
        # Event handler for mouse click on the canvas
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        print(f"Clicked at coordinates: ({x}, {y})")
        
        square_id = self.player_pattern_line[1][5]
        self.canvas.itemconfig(square_id, fill="red")
        
        floor_square = self.player_floor[0][0]
        self.canvas.itemconfig(floor_square, fill="blue")
        
        floor_square = self.player_floor[0][1]
        self.canvas.itemconfig(floor_square, fill="black")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    pattern_lines = [
        [[0,1,1],[2,2,1],[4,3,3],[-1,4,0],[-1,5,0]],
        [[3,1,1],[0,2,2],[2,3,3],[-1,4,0],[-1,5,0]],
        [[0,1,1],[-1,2,0],[-1,3,0],[3,4,2],[-1,5,0]],
        [[2,1,1],[-1,2,0],[-1,3,0],[4,4,4],[3,5,5]],
    ]
    walls = [
            [[[3, 1], [1, 0], [0, 0], [2, 0], [4, 0]],
            [[4, 1], [3, 0], [1, 0], [0, 0], [2, 0]],
            [[2, 1], [4, 0], [3, 0], [1, 0], [0, 0]],
            [[0, 1], [2, 1], [4, 1], [3, 1], [1, 1]],
            [[1, 1], [0, 0], [2, 0], [4, 0], [3, 0]]],
            [[[3, 1], [1, 0], [0, 0], [2, 0], [4, 0]],
            [[4, 1], [3, 0], [1, 1], [0, 0], [2, 0]],
            [[2, 1], [4, 0], [3, 0], [1, 0], [0, 0]],
            [[0, 1], [2, 1], [4, 1], [3, 1], [1, 1]],
            [[1, 1], [0, 0], [2, 0], [4, 0], [3, 0]]],
            [[[3, 1], [1, 0], [0, 0], [2, 0], [4, 0]],
            [[4, 1], [3, 0], [1, 0], [0, 0], [2, 0]],
            [[2, 1], [4, 0], [3, 0], [1, 0], [0, 0]],
            [[0, 1], [2, 1], [4, 1], [3, 1], [1, 1]],
            [[1, 1], [0, 1], [2, 1], [4, 0], [3, 0]]],
            [[[3, 1], [1, 0], [0, 0], [2, 0], [4, 1]],
            [[4, 1], [3, 0], [1, 0], [0, 0], [2, 1]],
            [[2, 1], [4, 0], [3, 0], [1, 0], [0, 1]],
            [[0, 1], [2, 1], [4, 1], [3, 1], [1, 1]],
            [[1, 1], [0, 0], [2, 0], [4, 0], [3, 0]]]
    ]
    floor = [[0, -1, 2, 3, 4, -1, 3],
             [3, 1, -1, -1, -1, -1, -1],
             [5, -1, -1, -1, -1, -1, -1],
             [2, -1, -1, -1, -1, -1, -1]]
    scores = [1, 2, 3, 4]
    azul_gui = AzulGUI(root, 4, pattern_lines, walls, floor, scores)
    azul_gui.run()
