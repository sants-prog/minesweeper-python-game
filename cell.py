from tkinter import Button
import random
import settings

class Cell:
    """docstring for Cell"""
    all = [] # Appending objects of the Cell class to this variable
    # We can do this dynamically inside the __init__ method, because it is called every time we create an instance
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self) # Appending the object itself

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            # text= f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.left_click_actions) # Signing a function as an event, that's why it needs 2 parameters
        btn.bind('<Button-2>', self.right_click_actions) # Macbook doesn't have right clik, so double click will act as a right click here
        # btn.bind('<Button-3>', self.right_click_actions) # This should be used when left and right click are available!
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        # I can use self.is_mine because at  the beginning of the game we are calling the randomize_mines method.
        print("left was clicked")
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def show_mine(self):
        # A logic to interrupt the game and to display a message indicating that the player lost!
        self.cell_btn_object.configure(highlightbackground='red')

    def right_click_actions(self, event):
        print("right was cliked")

    # creating a static method that doesn't belong to instance itself, rather belongs globally to the class
    @staticmethod
    def randomize_mines():
        # Avoid hardcoded mine values for grid size changes...
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
