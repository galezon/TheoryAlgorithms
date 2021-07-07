import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys

try:
    N = int( sys.argv[1] )
except IndexError:
    N = 100

def log_table_eval(n):
    """
    Evaluate log(a) + log(b) where a and b run from 1 to n

    :param n: the upper limit for a and b
    :return:  an (n + 1) x (n + 1) matrix with the function values
    """

    log_table = np.zeros((n + 1, n + 1), np.float)
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            log_table[a, b] = math.log(a,2) + math.log(b,2)
    return log_table

def log_table_draw(n):
    """
    Draw the values log(a) + log(b) where a and b run from 1 to n

    :param n:  the upper limit for a and b
    """
    log_table = log_table_eval(n)
    plt.title("log(a) + log(b)")
    plt.imshow(log_table, origin='lower')
    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(cax=cax)

def euclid(x,y,count = 0):
    if x == 0 or y == 0:
        return( max(x,y),count )
    else:
        count += 1
        return euclid( min(x,y), max(x,y)%min(x,y),count)

def euclid_steps_eval(n):
    matrix = np.zeros( (n+1,n+1) )
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            matrix[a, b] = euclid(a,b)[1]
    return matrix

def euclid_value_eval(n):
    matrix = np.zeros( (n+1,n+1) )
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            matrix[a, b] = euclid(a,b)[0]
    return matrix

def euclid_steps_draw(n):
    e_steps = euclid_steps_eval(n)
    plt.title("number of steps")
    plt.imshow(e_steps, origin='lower')
    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(cax=cax)

def euclid_value_draw(n):
    e_value = euclid_value_eval(n)
    plt.title("gcd)")
    plt.imshow(e_value, origin='lower')
    ax = plt.gca()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(cax=cax)

def main():
    plt.figure(figsize=(15,12))
    plt.subplot(131)
    log_table_draw(N)
    plt.tight_layout()
    plt.subplot(132)
    euclid_steps_draw(N)
    plt.tight_layout()
    plt.subplot(133)
    euclid_value_draw(N)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()