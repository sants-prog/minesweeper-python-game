from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Override the settings of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Python Minesweeper Game')
root.resizable(False, False)
root.configure(bg='black')

top_frame = Frame(
    root,
    bg='black', # 'red' for testing purposes only
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black', # 'blue' for testing purposes only
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black', # 'green' for testing purposes only
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=50, y=50
)

# Run the window
Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)
root.mainloop()


arv = list()
