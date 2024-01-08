import tkinter as tk

class tile_display:
    def __init__(self, canvas, x1, y1, x2, y2, outline):
        self.canvas = canvas
        self.rect_id = canvas.create_rectangle(x1, y1, x2, y2, outline=outline, width=2)
        
        # Get the coordinates of the center of the rectangle
        x1, y1, x2, y2 = self.canvas.coords(self.rect_id)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # Create text and associate it with the rectangle
        self.text_id = self.canvas.create_text(center_x, center_y, text="", font=("Arial", 24), fill="green")

    def update_text(self, new_text):
        if self.text_id:
            # Update the text content
            self.canvas.itemconfig(self.text_id, text=new_text)

class AzulGUI:
    def __init__(self, root, nPlayers: int):
        self.root = root
        self.root.title("Azul Game Board")
        
        self.nPlayers = nPlayers
        
        self.fact_display = []
        self.fact_middle = []
        
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
        
        for i in range(self.nPlayers):
            self.draw_player_board(i+1)

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
                tile = tile_display(self.canvas, 
                                    topLeftx + 3 + 50 * (5 - j),
                                    topLefty + 3 + 50 * (i - 1),
                                    topLeftx + 47 + 50 * (5 - j),
                                    topLefty + 47 + 50 * (i - 1), 
                                    "black")
                pattern_line_squares.append(tile)
        self.player_pattern_line.append(pattern_line_squares)
                
        # Draw Wall
        wall_colors = ['blue', 'light blue', 'black', 'red', 'orange'] # list of colors for coloring the wall out lines
        wall_squares = []
        for i in range(5):
            for j in range(5):
                x1 = topLeftx + 300 + 3 + 50 * j
                y1 = topLefty + 3 + 50 * i
                x2 = topLeftx + 300 + 47 + 50 * j
                y2 = topLefty + 47 + 50 * i

                tile = tile_display(self.canvas, x1, y1, x2, y2, wall_colors[(i-j)%5])
                wall_squares.append(tile)
        self.player_wall.append(wall_squares)


        # Draw Floor
        floor_squares = []
        for i in range(7):
            x1 = topLeftx + 3 + 50 * i
            y1 = topLefty + 260 + 3
            x2 = topLeftx + 47 + 50 * i
            y2 = topLefty + 260 + 47

            tile = tile_display(self.canvas, x1, y1, x2, y2, "black")
            floor_squares.append(tile)
        self.player_floor.append(floor_squares)
            
        # Display Player Name and Points
        text_id = self.canvas.create_text(topLeftx + 450, topLefty + 280, text=f"Player {player}: {0} points", font=("Arial", 24), fill="white")
        self.player_points.append(text_id)

    def draw_factory(self):
        self.draw_middle()
        if self.nPlayers == 4:
            for i in range(9):
                self.draw_factory_display(i)
        elif self.nPlayers == 3:
            for i in range(7):
                self.draw_factory_display(i)
        else:
            for i in range(5):
                self.draw_factory_display(i)
                
    def draw_factory_display(self, num: int):
        start = 180 + 110 * num

        # Draw first square
        tile = tile_display(self.canvas, start + 3, 353, start + 47, 397, "black")
        self.fact_display.append(tile)
        # Draw second square
        tile = tile_display(self.canvas, start + 3, 403, start + 47, 447, "black")
        self.fact_display.append(tile)
        # Draw third square
        tile = tile_display(self.canvas, start + 53, 353, start + 97, 397, "black")
        self.fact_display.append(tile)
        # Draw fourth square
        tile = tile_display(self.canvas, start + 53, 403, start + 97, 447, "black")
        self.fact_display.append(tile)
        
    def draw_middle(self):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        start_x = [23, 23, 73, 73, 123, 123]
        start_y = [353, 403, 353, 403, 353, 403]

        for i in range(len(colors)):
            x1, y1 = start_x[i], start_y[i]
            x2, y2 = x1 + 44, y1 + 44  # Width and height set to 44 for consistency

            tile = tile_display(self.canvas, x1, y1, x2, y2, colors[i])
            self.fact_middle.append(tile)

    def update_factory_middle(self, factory_middle):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        # Update Middle
        for i in range(6):
            tile = self.fact_middle[i]
            square_id = tile.rect_id
            num_tiles = factory_middle[i]
            if num_tiles:
                self.canvas.itemconfig(square_id, fill=colors[i])
                tile.update_text(str(num_tiles))
            else:
                self.canvas.itemconfig(square_id, fill="")
                tile.update_text("")
                
    def update_factory_displays(self, factory_display_tiles):  
        colors = ["red", "orange", "black", "blue", "light blue", "white"]  
        # Update Factory Displays
        if self.nPlayers == 2:
            nDisplays = 5
        elif self.nPlayers == 3:
            nDisplays = 7
        else:
            nDisplays = 9
            
        for i in range(nDisplays):
            display_count = 0
            if factory_display_tiles[i] == [0, 0, 0, 0, 0]:
                for j in range(4):
                    square_id = self.fact_display[i*4 + j].rect_id
                    self.canvas.itemconfig(square_id, fill="")
                continue
            
            for j in range(5):
                if factory_display_tiles[i][j] != 0:
                    num_tiles = factory_display_tiles[i][j]
                    for _ in range(num_tiles):
                        square_id = self.fact_display[i*4 + display_count].rect_id
                        self.canvas.itemconfig(square_id, fill=colors[j])
                        display_count += 1
    
    def reset_pattern_line(self, player_id):
        for j in range(1):
            square_id = self.player_pattern_line[player_id][j].rect_id
            self.canvas.itemconfig(square_id, fill="")
        for j in range(2):
            square_id = self.player_pattern_line[player_id][1+j].rect_id
            self.canvas.itemconfig(square_id, fill="")
        for j in range(3):
            square_id = self.player_pattern_line[player_id][3+j].rect_id
            self.canvas.itemconfig(square_id, fill="")
        for j in range(4):
            square_id = self.player_pattern_line[player_id][6+j].rect_id
            self.canvas.itemconfig(square_id, fill="")
        for j in range(5):
            square_id = self.player_pattern_line[player_id][10+j].rect_id
            self.canvas.itemconfig(square_id, fill="")
    
    def update_pattern_line(self, player_id, pattern_lines):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        # Update Pattern Lines
        num_tiles = pattern_lines[0][2]
        fill_color = pattern_lines[0][0]
        for j in range(num_tiles):
            square_id = self.player_pattern_line[player_id][j].rect_id
            self.canvas.itemconfig(square_id, fill=colors[fill_color])
        num_tiles = pattern_lines[1][2]
        fill_color = pattern_lines[1][0]
        for j in range(num_tiles):
            square_id = self.player_pattern_line[player_id][1+j].rect_id
            self.canvas.itemconfig(square_id, fill=colors[fill_color])
        num_tiles = pattern_lines[2][2]
        fill_color = pattern_lines[2][0]
        for j in range(num_tiles):
            square_id = self.player_pattern_line[player_id][3+j].rect_id
            self.canvas.itemconfig(square_id, fill=colors[fill_color])
        num_tiles = pattern_lines[3][2]
        fill_color = pattern_lines[3][0]
        for j in range(num_tiles):
            square_id = self.player_pattern_line[player_id][6+j].rect_id
            self.canvas.itemconfig(square_id, fill=colors[fill_color])
        num_tiles = pattern_lines[4][2]
        fill_color = pattern_lines[4][0]
        for j in range(num_tiles):
            square_id = self.player_pattern_line[player_id][10+j].rect_id
            self.canvas.itemconfig(square_id, fill=colors[fill_color])

    def update_wall_color(self, player_id, walls):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        
        # Update Wall Color
        for i in range(5):
            for j in range(5):
                num_sq = i * 5 + j
                square_id = self.player_wall[player_id][num_sq].rect_id
                fill_color = walls[i][j][0]
                if walls[i][j][1]:
                    self.canvas.itemconfig(square_id, fill=colors[fill_color])
    
    def update_floor_line(self, player_id, floor_line):
        colors = ["red", "orange", "black", "blue", "light blue", "white"]
        
        for i in range(7):
            square_id = self.player_floor[player_id][i].rect_id
            fill_color = floor_line[i]
            if fill_color != -1:
                self.canvas.itemconfig(square_id, fill=colors[fill_color])
            else:
                self.canvas.itemconfig(square_id, fill="")
        
    def update_player_texts(self, turn, scores, nPlayers):
        # Update Points Text
        for i in range(nPlayers):
            text_id = self.player_points[i]
            point = scores[i]
            if turn == i:
                self.canvas.itemconfig(text_id, text=f"Player {i+1}: {point} points", fill="red")
            else:
                self.canvas.itemconfig(text_id, text=f"Player {i+1}: {point} points", fill="white")
                
    def get_user_click(self):
        """
        Waits for a user click on the screen and returns the coordinates.
        """
        clicked = False
        x, y = 0, 0

        def on_click(event):
            nonlocal clicked, x, y
            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)
            clicked = True
            self.canvas.unbind("<Button-1>")  # Unbind the event here

        # Bind the event handler
        self.canvas.bind("<Button-1>", on_click)

        # Wait until a click is received
        while not clicked:
            self.root.update_idletasks()
            self.root.update()

        return x, y
    
    # Return the display -1 (middle), 1 - 9 plus which square was clicked
    def get_display_input(self) -> (int, int):
        while True:
            x, y = self.get_user_click()
            if 23 <= x <= 67:
                if 353 <= y <= 397:
                    return -1, 0
                if 403 <= y <= 447:
                    return -1, 1
            if 73 <= x <= 113:
                if 353 <= y <= 397:
                    return -1, 2
                if 403 <= y <= 447:
                    return -1, 3
            if 123 <= x <= 167:
                if 353 <= y <= 397:
                    return -1, 4
                if 403 <= y <= 447:
                    return -1, 5
                    
            if 183 <= x <= 227:
                if 353 <= y <= 397:
                    return 0, 0
                if 403 <= y <= 447:
                    return 0, 1
            if 233 <= x <= 277:
                if 353 <= y <= 397:
                    return 0, 2
                if 403 <= y <= 447:
                    return 0, 3
                    
            if 293 <= x <= 337:
                if 353 <= y <= 397:
                    return 1, 0
                if 403 <= y <= 447:
                    return 1, 1
            if 343 <= x <= 387:
                if 353 <= y <= 397:
                    return 1, 2
                if 403 <= y <= 447:
                    return 1, 3
                    
            if 403 <= x <= 447:
                if 353 <= y <= 397:
                    return 2, 0
                if 403 <= y <= 447:
                    return 2, 1
            if 453 <= x <= 497:
                if 353 <= y <= 397:
                    return 2, 2
                if 403 <= y <= 447:
                    return 2, 3
                
            if 513 <= x <= 557:
                if 353 <= y <= 397:
                    return 3, 0
                if 403 <= y <= 447:
                    return 3, 1
            if 563 <= x <= 607:
                if 353 <= y <= 397:
                    return 3, 2
                if 403 <= y <= 447:
                    return 3, 3

            if 623 <= x <= 667:
                if 353 <= y <= 397:
                    return 4, 0
                if 403 <= y <= 447:
                    return 4, 1
            if 673 <= x <= 717:
                if 353 <= y <= 397:
                    return 4, 2
                if 403 <= y <= 447:
                    return 4, 3
            
            if 733 <= x <= 777 and self.nPlayers >= 3:
                if 353 <= y <= 397:
                    return 5, 0
                if 403 <= y <= 447:
                    return 5, 1
            if 783 <= x <= 827 and self.nPlayers >= 3:
                if 353 <= y <= 397:
                    return 5, 2
                if 403 <= y <= 447:
                    return 5, 3
            
            if 843 <= x <= 887 and self.nPlayers >= 3:
                if 353 <= y <= 397:
                    return 6, 0
                if 403 <= y <= 447:
                    return 6, 1
            if 893 <= x <= 937 and self.nPlayers >= 3:
                if 353 <= y <= 397:
                    return 6, 2
                if 403 <= y <= 447:
                    return 6, 3
            
            if 953 <= x <= 997 and self.nPlayers >= 4:
                if 353 <= y <= 397:
                    return 7, 0
                if 403 <= y <= 447:
                    return 7, 1
            if 997 <= x <= 1047 and self.nPlayers >= 4:
                if 353 <= y <= 397:
                    return 7, 2
                if 403 <= y <= 447:
                    return 7, 3
            
            if 1063 <= x <= 1107 and self.nPlayers >= 4:
                if 353 <= y <= 397:
                    return 8, 0
                if 403 <= y <= 447:
                    return 8, 1
            if 1113 <= x <= 1157 and self.nPlayers >= 4:
                if 353 <= y <= 397:
                    return 8, 2
                if 403 <= y <= 447:
                    return 8, 3

    def get_pattern_line_input(self, turn):
        # Draw Pattern Line
        if turn == 0:
            topLeftx = 20
            topLefty = 20
        elif turn == 1:
            topLeftx = 620
            topLefty = 20
        elif turn == 2:
            topLeftx = 20
            topLefty = 470
        elif turn == 3:
            topLeftx = 620
            topLefty = 470
        
        while True:
            x, y = self.get_user_click()
            
            if topLeftx <= x <= topLeftx + 270 and topLefty + 3 <= y <= topLefty + 47:
                return 0
            elif topLeftx <= x <= topLeftx + 270 and topLefty + 53 <= y <= topLefty + 97:
                return 1
            elif topLeftx <= x <= topLeftx + 270 and topLefty + 103 <= y <= topLefty + 147:
                return 2
            elif topLeftx <= x <= topLeftx + 270 and topLefty + 153 <= y <= topLefty + 197:
                return 3
            elif topLeftx <= x <= topLeftx + 270 and topLefty + 203 <= y <= topLefty + 247:
                return 4
        

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    
    azul_gui = AzulGUI(root, 4)
    azul_gui.run()
