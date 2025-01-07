import math
import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt

def generate_d1(num_points, x_range=(-10, 10), y_range=(-10, 10), angle1=np.pi/4, angle2=3*np.pi/4):
    x = np.linspace(x_range[0], x_range[1], int(np.sqrt(num_points)))
    y = np.linspace(y_range[0], y_range[1], int(np.sqrt(num_points)))
    X, Y = np.meshgrid(x, y)
    X, Y = X.flatten(), Y.flatten()

    theta = np.arctan2(Y, X)

    theta = np.mod(theta, 2 * np.pi)
    angle1 = np.mod(angle1, 2 * np.pi)
    angle2 = np.mod(angle2, 2 * np.pi)

    if angle1 < angle2:
        mask = (theta >= angle1) & (theta <= angle2)
    else:
        mask = (theta >= angle1) | (theta <= angle2)

    return X[mask], Y[mask]

def generate_upper_half_plane(num_points, x_range=(-10, 10), y_range=(0, 10)):
    x = np.linspace(x_range[0], x_range[1], int(np.sqrt(num_points)))
    y = np.linspace(y_range[0], y_range[1], int(np.sqrt(num_points)))
    X, Y = np.meshgrid(x, y)
    X, Y = X.flatten(), Y.flatten()

    return X, Y

def generate_points_in_circle(num_points, radius):
    x = np.random.uniform(-radius, radius, num_points)
    y = np.random.uniform(-radius, radius, num_points)

    r = np.sqrt(x**2 + y**2)
    mask = r <= radius

    return x[mask], y[mask]

def generate_points_out_circle(num_points, radius):
    x = np.random.uniform(-5, 5, num_points)
    y = np.random.uniform(-5, 5, num_points)

    r = np.sqrt(x**2 + y**2)
    mask = r >= radius

    return x[mask], y[mask]

def conform():
    e = math.e
    num_points = 5000
    plt.figure(figsize=(10, 10))

    # ---- D1 ----
    X, Y = generate_d1(num_points, x_range=(-10, 10), y_range=(-10, 10), angle1=np.pi / 4, angle2=3 * np.pi / 4)

    plt.subplot(2, 3, 1)
    plt.scatter(X, Y, s=1, color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("D_1 = { z: 3π/4 <= arg(z) <= π/4 }")

    # ---- Upper Half-Plane ----
    X_pi, Y_pi = generate_upper_half_plane(num_points, x_range=(-10, 10), y_range=(0, 10))

    plt.subplot(2, 3, 2)
    plt.scatter(X_pi, Y_pi, s=1, color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("w = z^2")

    # ---- in Circle R = 1 ----
    radius_1 = 1
    X_circle1, Y_circle1 = generate_points_in_circle(num_points, radius_1)

    plt.subplot(2, 3, 4)
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.plot(radius_1 * np.cos(theta), radius_1 * np.sin(theta), color='red')
    plt.scatter(X_circle1, Y_circle1, s=1, color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))

    plt.title("w = (z-1)/(z+1)")

    # ---- in Circle R = e ----
    radius_e = e
    X_circle2, Y_circle2 = generate_points_in_circle(num_points, radius_e)

    plt.subplot(2, 3, 5)
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.plot(radius_e * np.cos(theta), radius_e * np.sin(theta), color='red')
    plt.scatter(X_circle2, Y_circle2, s=1, color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))

    plt.title("w = z / e")

    # ---- D2 ----
    X_circle3, Y_circle3 = generate_points_out_circle(num_points, radius_e)

    plt.subplot(2, 3, 6)
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.plot(radius_e * np.cos(theta), radius_e * np.sin(theta), color='red')
    plt.scatter(X_circle3, Y_circle3, s=1, color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.xticks(np.arange(-5, 6, step=1))
    plt.yticks(np.arange(-5, 6, step=1))

    plt.title("w = e / z")


    plt.tight_layout()
    plt.show()

conform()



