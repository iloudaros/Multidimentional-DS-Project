"""This script generates trajectory data (x, y, t) by simulating a moving object and saves them in a .csv file."""
import matplotlib.pyplot as plt
import numpy as np

# Set the physics values.

# Air drag in each direction for a sphere shaped object.
DRAG_X = 0.1
DRAG_Y = 0.1

# Gravitational acceleration.
g = 9.8


def x_acceleration(velocity):
    return -DRAG_X * velocity


def y_acceleration(velocity):
    return -DRAG_Y * velocity - g


if __name__ == "__main__":

    # Set initial velocities in each direction.
    vx = 10
    vy = 80

    # Set time step and total simulation durationg.
    dt = 0.01
    sim_duration = 25

    # Set starting positions for the object.
    x = 0.0
    y = 0.0

    x_values = [x]
    y_values = [y]
    t_values = [0]

    # Run the simulation for specified time with equal time steps.
    for t in np.arange(0.05, sim_duration, dt):

        # Update velocities.
        vx += x_acceleration(vx) * dt
        vy += y_acceleration(vy) * dt

        # Calculate new positions.
        x += vx * dt
        y += vy * dt

        x_values.append(x)
        y_values.append(y)
        t_values.append(t)

    # Plot the x and y coordinates over time.
    plt.plot(x_values, y_values)
    plt.show()

    # Save data to the file.
    with open("trajectory-data.csv", "w") as f:
        f.write("x,y,t\n")
        for i in range(len(x_values)):
            data_instance = f"{x_values[i]},{y_values[i]},{t_values[i]}"
            f.write(data_instance + "\n")
