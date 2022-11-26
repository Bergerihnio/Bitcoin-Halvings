import matplotlib.pyplot as plt
import numpy as np

def values():
    x = []
    y = []
    blockReward = 100
    currentBlock = 0
    print('')
    while blockReward >= 0.0002:
        blockReward /= 2
        y.append(blockReward)
        currentBlock += 21000
        x.append(currentBlock)
    plt.title('BTC emission')
    plt.grid()
    plt.xlabel('Number of block')
    plt.ylabel('BTC block reward')
    plt.plot(x, y)
    plt.show()

values()






