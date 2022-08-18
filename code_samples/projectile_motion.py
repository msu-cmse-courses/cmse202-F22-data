import numpy as np
import matplotlib.pyplot as plt

def compute_trajectory(time,velocity=500,angle=60):
    # velocity is assumed to be in m s^-1
    # angle is assumed to be in degrees (and is converted to radians)
    g = 9.8 # m s^-2
    x_position = velocity*time*np.cos(np.radians(angle))
    y_position = velocity*time*np.sin(np.radians(angle)) - 0.5*g*(time**2)
    return x_position,y_position

def plot_x_vs_time(time,x_position):
    plt.figure()
    plt.plot(time,x_position)
    plt.xlabel("time (s)")
    plt.ylabel("x (meters)")
    plt.title("x vs time")
    plt.grid()
    plt.savefig("x_vs_time.png")

def main():
    t_start = 0
    t_stop = 100
    t = np.arange(t_start,t_stop,1)
    x, y = compute_trajectory(t)
    plot_x_vs_time(t,x)


if __name__== "__main__":
    main()
