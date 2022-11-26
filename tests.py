import matplotlib.pyplot as plt
import numpy as np

# import matplotlib as plt
#
# x = [50,10]
# y = [1050, 1575, 1837, 1968, 2033.5,2066.25, 2082.625]
# plt.plot(x,y)
# plt.ylabel('BTC emission')
# plt.show()

# def next():
#     number = 0
#     list = []
#     while number <= 800:
#         number += 21
#         list.append(number)
#         plt.plot(list)
#     plt.ylabel('Numbers:')
#     plt.show()
#     return list

x = np.linspace()
y = 10**x

plt.yscale('log')
plt.plot(x,y)
plt.show()

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
    plt.hot()
    plt.xlabel('Number of block')
    plt.ylabel('BTC block reward')
    x = np.linspace(blockReward)
    y = 10**x
    plt.plot(x,y)
    plt.show()







