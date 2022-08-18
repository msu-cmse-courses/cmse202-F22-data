"""superbugs.py

Contains class definitions for modeling the evolution of bacteria in the
presence of antibiotics.
"""

# =============================================================================
# imports
# =============================================================================

# built-ins
import random

# standard imports
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# constants
# =============================================================================


# =============================================================================
# bug class
# =============================================================================

class bug():
    """Bug class. 
    
    Each bug has 3 genes in the range [0, 1) and a location (c, r) in
    a two dimensional grid.
    
    Attributes:
        genes [type: numpy array]
            List of three numbers in the range [0, 1) generated uniformly
            at random.
        
        loc [type: tuple]
            Ordered pair of coordinates specifying the bug's location.
            
        mutation_rate [type: float]
            The mutation rate for the bacterium
        
    Methods:
        __init__(c=0, r=0, mutation_rate=0.2)
            Initialize a bug with random genes and a mutation rate
            at the location (c, r)
        
        mitosis()
            Returns a new bug.
        
            Copies genes from the current bug to the new bug with probability
            equal to 1 - mutation_rate. Else, assigns new genes at random.
            
        draw()
            Draws the bug with rgb color corresponding to it's genes.
    """
    
    def __init__(self, c=0, r=0, mutation_rate=0.2):
        """Initializes a bug with random genes. Default location is (0, 0).
           Default mutation rate is 0.2.
        
        Args:
            c [type: int]
                Specifies the column of the bug in a 2d grid.
            
            r [type: int]
                Specifies the row of the bug in a 2d grid.
                
            mutation_rate [type: float]
                Probability that bacteria mutate
        """
        self.genes = np.random.rand(3)
        self.loc = (c, r)
        self.mutation_rate = mutation_rate
    
    def mitosis(self):
        """Returns a new bug.
        
        Copies genes from the current bug to the new bug with probability
        equal to 1 - mutation_rate. Else, assigns new genes at random.
        """
        newbug = bug(mutation_rate=self.mutation_rate)
        for (i, g) in enumerate(self.genes):
            if random.random() > self.mutation_rate:
                newbug.genes[i] = self.genes[i]
        return newbug
    
    def draw(self):
        """Draws the bug with rgb color corresponding to it's genes."""
        plt.scatter(self.loc[0], self.loc[1], color=self.genes)

# =============================================================================
# petri_dish class
# =============================================================================

class petri_dish():
    """petri_dish class.
    
    Generates a petridish representing the world where the bugs live. 
    Each dish has antibiotics and a list of bugs.
    
    Attributes:
        buglist [type: dict]
            dictionary of all bugs in simulation
        
        active [type: set]
            set of active (i.e., not dead) bugs
            
        antibodies [type: numpy array]
            2d grid storing the values of the antibiotics at each point
        
    Methods:
        __init__()
            Initializes the world.
        
        timestep()
            Performs one timestep of the simulation.
        
        draw()
            Draws the world as an image and plots each bug.
    """
    
    def __init__(self, n_rows=45, n_cols=90,
                 antibods=[0, 0.5, 0.75, 0.8, 0.95, 0.8, 0.75, 0.5, 0],
                 init_cols=[0, 89],
                 bug_mutation_rate=0.2):
        """Initializes the world.
        
        Args:
            n_rows [type: int]
                number of rows in world
            
            n_cols [type: int]
                number of columns in world
            
            antibods [type: list<float>]
                antibiotic values in each region of the world
                length of antibods must evenly divide n_cols
            
            init_cols [type: list<int>]
                starting columns for the antibiotics
                
            bug_mutation_rate [type: float]
                the mutation rate of the bacteria in this dish
        """
        # error check on inputs
        assert n_cols % len(antibods) == 0, \
        "ERROR: Number of anitbodies must evenly divide the number of columns"
        
        assert init_cols[0] >= 0 and init_cols[1] < n_cols, \
        "Starting columns must be greater than zero and less than the total number of columns."

        # dictionary of location, bug key value pairs
        self.buglist = dict()

        # set of active bugs
        self.active = set()

        # sets the attribute self.antibodies that stores the world info
        self._basic_setup(n_rows=n_rows, n_cols=n_cols,
                          antibods=antibods, init_cols=init_cols,
                          bug_mutation_rate=bug_mutation_rate)
    
    def _basic_setup(self, n_rows=45, n_cols=90,
                    antibods=[0, 0.5, 0.75, 0.8, 0.95, 0.8, 0.75, 0.5, 0],
                    init_cols=[0, 89],
                    bug_mutation_rate=0.2):
        """Sets up the world.
        
        Helper function for __init__ method with same arguments as __init__.
        """
        # initialize bugs
        for row in range(n_rows):
            # bugs on the left
            bl = bug(init_cols[1], row, bug_mutation_rate)

            # bugs on the left
            br = bug(init_cols[0], row, bug_mutation_rate)
            
            # add initial points to active and buglist
            self.buglist[br.loc] = br
            self.buglist[bl.loc] = bl
            self.active.add(br.loc)
            self.active.add(bl.loc)
            
        # set up the board of antibodies
        step = n_cols // len(antibods)
        self.antibodies=np.zeros((n_rows, n_cols, 3))
        for ii in range(n_cols // step):
            self.antibodies[:, ii * step: (ii + 1) * step + 1] = [antibods[ii]] * 3
        
    def timestep(self):        
        """Performs one time step of the simulation.
        
        Loops through the bugs, finds their neighbors and initiates mitosis.
        New bugs will die if their gene values are less than the corresponding
        antibiotic values.
        """
        newbugs = dict()
        n_cols = self.antibodies.shape[1]
        n_rows = self.antibodies.shape[0]

        these_bugs = self.active.copy()

        for b in these_bugs:
            c = b[0]
            r = b[1]
            parent_bug = self.buglist[b]

            neighbors = []
            for dc in range(c - 1, c + 2):
                for dr in range(r - 1, r + 2):
                    key = (dc, dr)
                    if dc >= 0 and dc < n_cols and dr >= 0 and dr < n_rows:
                        if not key in self.buglist:
                            neighbors.append(key)
            if neighbors:
                child_bug = parent_bug.mitosis()
                loc = random.choice(neighbors)

                # check if bug lives
                child_bug.loc = loc
                alive = True
                for i, g in enumerate(child_bug.genes):
                    if g < self.antibodies[loc[1], loc[0], i]:
                        alive = False
                if alive:
                    newbugs[child_bug.loc] = child_bug
            else:
                self.active.remove((c, r))

        self.buglist.update(newbugs)
        self.active.update(newbugs)

    def draw(self,background=None):
        """Draws the world as an image and plots each bug."""
        plt.imshow(1.0 - self.antibodies)
        [self.buglist[b].draw() for b in self.buglist]
