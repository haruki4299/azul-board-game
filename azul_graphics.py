import tkinter as tk

class AzulGUI:
    def __init__(self, root, nPlayers: int):
        self.root = root
        self.root.title("Azul Game Board")
        
        self.nPlayers = nPlayers

        # Create canvas to draw on
        self.canvas = tk.Canvas(root, width=1200, height=800, bg="green")
        self.canvas.pack()

        # Draw dividing lines
        self.draw_dividing_lines()
        
        self.draw_factory()

        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_dividing_lines(self):
        # Draw vertical line separating left and right areas
        self.canvas.create_line(600, 0, 600, 350, fill="black", width=2)
        self.canvas.create_line(600, 450, 600, 800, fill="black", width=2)

        # Draw horizontal line separating top and bottom areas
        self.canvas.create_line(0, 350, 1200, 350, fill="black", width=2)
        self.canvas.create_line(0, 450, 1200, 450, fill="black", width=2)

    def draw_factory(self):
        self.draw_middle()
        if self.nPlayers == 4:
            for i in range(9):
                self.draw_factory_display(i)
        
    def draw_factory_display(self, num:int):
        start = 160 + 100 * num
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
        self.canvas.create_line(13, 353, 13, 397, fill="red", width=2)
        self.canvas.create_line(57, 353, 57, 397, fill="red", width=2)
        self.canvas.create_line(13, 353, 57, 353, fill="red", width=2)
        self.canvas.create_line(13, 397, 57, 397, fill="red", width=2)
        
        # Square for Orange
        self.canvas.create_line(13, 403, 13, 447, fill="orange", width=2)
        self.canvas.create_line(57, 403, 57, 447, fill="orange", width=2)
        self.canvas.create_line(13, 403, 57, 403, fill="orange", width=2)
        self.canvas.create_line(13, 447, 57, 447, fill="orange", width=2)
        
        # Square for Black
        self.canvas.create_line(63, 353, 63, 397, fill="black", width=2)
        self.canvas.create_line(107, 353, 107, 397, fill="black", width=2)
        self.canvas.create_line(63, 353, 107, 353, fill="black", width=2)
        self.canvas.create_line(63, 397, 107, 397, fill="black", width=2)
        
        # Square for Blue
        self.canvas.create_line(63, 403, 63, 447, fill="blue", width=2)
        self.canvas.create_line(107, 403, 107, 447, fill="blue", width=2)
        self.canvas.create_line(63, 403, 107, 403, fill="blue", width=2)
        self.canvas.create_line(63, 447, 107, 447, fill="blue", width=2)
        
        # Square for Light Blue
        self.canvas.create_line(113, 353, 113, 397, fill="light blue", width=2)
        self.canvas.create_line(157, 353, 157, 397, fill="light blue", width=2)
        self.canvas.create_line(113, 353, 157, 353, fill="light blue", width=2)
        self.canvas.create_line(113, 397, 157, 397, fill="light blue", width=2)
        
        # Square for Light Blue
        self.canvas.create_line(113, 403, 113, 447, fill="white", width=2)
        self.canvas.create_line(157, 403, 157, 447, fill="white", width=2)
        self.canvas.create_line(113, 403, 157, 403, fill="white", width=2)
        self.canvas.create_line(113, 447, 157, 447, fill="white", width=2)
        

    def on_canvas_click(self, event):
        # Event handler for mouse click on the canvas
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        print(f"Clicked at coordinates: ({x}, {y})")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    azul_gui = AzulGUI(root, 4)
    azul_gui.run()
