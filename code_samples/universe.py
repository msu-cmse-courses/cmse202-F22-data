"""Module of the Universe."""

import numpy as np
import matplotlib.pyplot as plt


class Universe:
    """Universe class. There is nothing otherwise."""
    _all_particles = None

    def __init__(self, width, height):
        """Create a 2D finite universe of size width x height.

        Parameters
        ----------
        width: int
            Number of imaginary pixel of the universe.

        height: int
            Number of imaginary pixel of the universe.
        """

        self.width = width
        self.height = height

        # Create empty lists for the fermions and bosons.
        self.fermions = []
        self.bosons = []

    def evolve(self):
        """Evolve the universe one step at a time.
        Move the particles, check that they didn't leave the universe,
        and check if there is any annihilation/creation of particles.
        """
        # PUT YOUR CODE HERE

    def move_particles(self):
        """I NEED A DOCSTRING!"""
        for ip in self._all_particles:
            ip.move()

    def boundary_conditions(self):
        """I NEED A DOCSTRING!"""
        for ip in self._all_particles:
            if ip.x > self.width:
                ip.x -= self.width

            if ip.y > self.height:
                ip.y -= self.height

            if ip.x < 0:
                ip.x += self.width

            if ip.y < 0:
                ip.y += self.height

    def draw(self):
        """I NEED A DOCSTRING!"""
        for ip in self.fermions:
            plt.scatter(ip.x, ip.y, marker="o", c = "b")

        for ip in self.bosons:
            plt.scatter(ip.x, ip.y, marker="*", c = "r")

    def check_interaction(self):
        """I NEED A DOCSTRING!"""

        for ip1, p1 in enumerate(self.fermions):
            for ip2, p2 in enumerate(self.fermions[ip1:]):
                if p1.x == p2.x and p1.y == p2.y and p1.is_antiparticle(ip2):
                    # QUESTION uni.1:  What do these pop do?
                    self.fermions.pop(ip1)
                    self.fermions.pop(ip2 - 1) # QUESTION uni.2: Why is there a -1 here?
                    self.bosons.append(Boson(charge=0.0, mass=0.0,spin=1.0) )
                    self.bosons[-1].place_at(coord=(p1.x, p1.y))
                    # QUESTION uni.3:  What does this continue do?
                    continue
            # QUESTION uni.4:  What does this continue do?
            continue

        # update the list
        self._all_particles = [*self.fermions, *self.bosons]
