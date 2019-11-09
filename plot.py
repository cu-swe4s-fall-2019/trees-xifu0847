import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt


if __name__ == '__main__':
    size = 3
    x = np.arange(size)

    name = ['Insert', 'Search_exist', 'Search_non_exist']
    a = [0.12591791152954102, 0.01729607582092285, 0.019687175750732422]
    b = [0.012137413024902344, 0.011729717254638672, 0.015170812606811523]
    c = [0.029813051223754883, 0.0218050479888916, 0.024309635162353516]
    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, a,  width=width, label='AVL')
    plt.bar(x + width, b, width=width, label='hash_table')
    plt.bar(x + 2 * width, c, width=width, label='binary_tree')
    plt.xticks(x + width, name)
    plt.ylabel('time / secs')
    plt.legend()
    plt.savefig('random_5000.png')
    
    
    
