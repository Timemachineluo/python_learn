from test import RandomWalk
import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)
    plt.plot(0, 0, c='green', linewidth=10) 
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', linewidth=10)
    plt.axes().get_xaxis().set_visible(False) 
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n': 
        break