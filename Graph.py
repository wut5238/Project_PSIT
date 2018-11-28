import matplotlib.pyplot as plt
"""Graph"""

    x_val = [x[0] for x in top_10_20xx]
    y_val = [x[1] for x in top_10_20xx]
    plt.plot(x_val,y_val)
    plt.plot(x_val,y_val,'or')
    plt.show()

    