import matplotlib.pyplot as plt
import random
import numpy as np
from IPython.display import display, clear_output
import time


class Ant:
    """
    Ant class.

    Each has an x and y location in a 2D grid.
    Each ant also knows whether or not it is currently
    in possession of food.

    Attributes
    ----------

    x : int
        x position in the 2D grid

    y : int
        y position in the 2D grid

    has_food : bool
        whether or not the ant is currently in possession of food

    Methods
    -------
    __init__(x_dim, y_dim)
        Initialize an ant in a random location within
        the bounds of the grid as defined by x_dim and y_dim.
        Start the ant off without food.

    head_home()
        If the ant has any has food, it should head "home" (0,0)

    THE REST OF THIS DOCSTRING IS INCOMPLETE! You should finish it!

    """

    def __init__(self, x_dim, y_dim):
        """
        Initialize an ant in a random location within
        the bounds of the grid as defined by x_dim and y_dim.
        Start the ant off without food.
            
        Parameters
        ----------
        
        x_dim : int
            the extent of the grid in the x-direction
                
        y_dim : int
             the extent of the grid in the x-direction
        """
        self.x = np.random.randint(0, x_dim)
        self.y = np.random.randint(0, y_dim)
        self.has_food = False

    def move(self, smell, food):
        if self.has_food == True:
            smell[self.x, self.y] += 100
            self.head_home()
        else:
            self.search_for_food(smell)
        if food[self.x, self.y] > 0:
            food[self.x, self.y] -= 1
            self.has_food = True

    def head_home(self):
        x = self.x
        y = self.y

        if (x == 0) and (y == 0):
            self.has_food = False;
            return

        pick = np.zeros(x + y)
        pick[0:x] = 1
        if (np.random.choice(pick) == 1):
            x = x - 1
        else:
            y = y - 1

        if (x < 0):
            x = 0
        if (y < 0):
            y = 0

        self.x = x
        self.y = y

    def search_for_food(self, smell):
        x = self.x
        y = self.y

        x_dim = smell.shape[0]
        y_dim = smell.shape[1]

        directions = ['up', 'left', 'down', 'right']
        # First check to see if there is food up and to the right.
        g = []  # follow gradient
        m = []

        if (x + 1 < smell.shape[0]):
            if (smell[x + 1, y] > 0):
                m.append(smell[x + 1, y])
                g.append('right')
        if (y + 1 < smell.shape[1]):
            if (smell[x, y + 1] > 0):
                m.append(smell[x, y + 1])
                g.append('up')
        if (g != []):
            grad = g[m.index(max(m))]
            # print("Following smell", grad)
        else:
            # else just pick a random direction.
            grad = random.choice(directions)
            # print("Choosing ",grad)

        # move the ant
        if (grad == 'up'):
            y = y + 1
        elif (grad == 'right'):
            x = x + 1
        elif (grad == 'down'):
            y = y - 1
        elif (grad == 'left'):
            x = x - 1
        else:
            print(grad)
            print("ERROR!!a!!!!!!!!!!")

        # make sure we don't go off the grid.
        if (x < 0):
            x = 0
        if (y < 0):
            y = 0
        if (x > x_dim - 1):
            x = x_dim - 1
        if (y > y_dim - 1):
            y = y_dim - 1
        self.x = x
        self.y = y

    def draw(self):
        """ Draw the ants on the board."""
        color = 'r'
        if (self.has_food == True):
            color = 'g'
        plt.scatter(self.x, self.y, color=color)


def run(num_ants=100, x_dim=70, y_dim=30):
    smell = np.zeros((x_dim, y_dim))
    food = np.zeros((x_dim, y_dim))

    # place food
    food[45:50, 25:30] = 10
    food[45:50, 25:30] = 10
    food[65:70, 0:5] = 10

    ants = [Ant(x_dim, y_dim) for a in range(0, num_ants)]

    fig, ax = plt.subplots(figsize=(10, 5))

    # Main simulation loop
    for i in range(0, 100):

        # Loop over ants
        for a in ants:
            a.move(smell, food)

        smell = smell - 1
        smell[smell < 0] = 0

        # plot world
        plt.imshow(food.T, origin='lower', aspect='equal', cmap="magma")
        for a in range(0, num_ants):
            ants[a].draw()

        # Animaiton part (dosn't change)
        clear_output(wait=True)  # Clear output for dynamic display
        display(fig)  # Reset display
        fig.clear()  # Prevent overlapping and layered plots
        time.sleep(0.0001)  # Sleep for a fraction of a second to allow animation to catch up
