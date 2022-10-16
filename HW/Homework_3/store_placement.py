import numpy as np
import matplotlib.pyplot as plt


class city():
    def __init__(self,x_dim=5,y_dim=5,pop_density=0.5):
        self.pop_density = pop_density
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.house_x = []
        self.house_y = []
        self.store_pos = []
        self.list_of_dists = []
        self.add_houses()

    def add_houses(self):
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                if np.random.uniform() < self.pop_density:
                    self.house_x.append(x)
                    self.house_y.append(y)
        self.house_x = np.array(self.house_x)
        self.house_y = np.array(self.house_y)

    def get_homes_served(self,dist_to_point):
        homes_served = np.ones_like(self.house_x)
        for kk in range(len(self.list_of_dists)):
            close_houses = dist_to_point < self.list_of_dists[kk]
            homes_served = np.logical_and(homes_served,close_houses)
        return homes_served

    def get_distance_to_point(self,x,y):
        return np.hypot(x-self.house_x,y-self.house_y)

    def find_best_store_loc(self):
        best_position = []
        best_homes_served = 0
        best_distance = np.inf
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                dist_to_point = self.get_distance_to_point(x,y)
                if len(self.store_pos) > 0:
                    homes_served  = self.get_homes_served(dist_to_point)
                    if sum(homes_served) > best_homes_served:
                        best_position = [x,y]
                        best_homes_served = sum(homes_served)
                else:
                    if np.sum(dist_to_point) < best_distance:
                        best_distance = np.sum(dist_to_point)
                        best_position = [x,y]
        self.store_pos.append(best_position)
        self.list_of_dists.append(self.get_distance_to_point(best_position[0],best_position[1]))

    def draw(self):
        store_x,store_y = list(zip(*self.store_pos))
        plt.plot(self.house_x,self.house_y,markersize=8,color="tab:blue",marker="s",linestyle="None")
        plt.plot(store_x,store_y ,color='tab:red',markersize=25,marker=".",linestyle="None")
        plt.show()


