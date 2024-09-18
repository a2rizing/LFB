import tkinter as tk

class MazeBuilder:
    def __init__(self, master, rows, cols, cell_size):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # Create canvas to draw the maze
        self.canvas = tk.Canvas(master, width=cols * cell_size, height=rows * cell_size)
        self.canvas.pack()

        # Draw grid lines
        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

        self.canvas.bind("<Button-1>", self.mark_path)
        
        self.done_button = tk.Button(master, text="Done", command=self.finalize_maze)
        self.done_button.pack()

    def mark_path(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if self.grid[row][col] == 0:
            self.grid[row][col] = 1
            self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                         (col + 1) * self.cell_size, (row + 1) * self.cell_size, 
                                         fill="green")
        else:
            self.grid[row][col] = 0
            self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                         (col + 1) * self.cell_size, (row + 1) * self.cell_size, 
                                         fill="white")

    def finalize_maze(self):
        print("Final Maze Layout (1 = Path, 0 = Wall):")
        for row in self.grid:
            for i in row:
                print(i, " ", end=" ")
            print()
        self.master.quit()
root = tk.Tk()
root.title("Custom Maze Builder")
maze_builder = MazeBuilder(root, 5, 5, 20)
root.mainloop()
