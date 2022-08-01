import random
import matplotlib.pyplot as plt
import numpy as np


# a function that returns n random integer numbers from 0 to 25
def random_numbers(n):
    return random.sample(range(0, 25), n)



def hist_random_numbers_0_25(n):
    # create a histogram of the random numbers
    plt.hist(random_numbers(n), bins=25)
    plt.show()



"""Testes em pt-br"""
# uma função que descomprima um arquivo zip
def decompress_file(file_name):
    import zipfile
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()



def draw_scatter_plot():
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    plt.scatter(x, y)
    plt.show()



'''OBS: não consegui fazer o jogo rodar'''
# contrua um jogo de tic tac toe
# def tic_tac_toe():



