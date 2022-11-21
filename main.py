# bitcoin halving

def convert(blockReward):
    satoshi = blockReward*1000000 # satoshi = 0.00000001
    return satoshi
def bitcoin():
    blockReward = 50
    years = 2008
    numberOfHalv = 0
    currentBlock = 0
    print('')
    while blockReward >= 0.0002 and years <= 2080 :
        blockReward = blockReward / 2
        years += 4
        numberOfHalv += 1
        currentBlock += 210000
        if blockReward < 0.01:
                print('')
                print('Number of block During:',currentBlock,str(numberOfHalv)+'th','₿itcoin halving year:',years,'block reward reduced to:',blockReward,'\nsatoshi =',convert(blockReward))
        else: print('Number of block During:',currentBlock,str(numberOfHalv)+'th','₿itcoin halving year:' ,years,'block reward reduced to:',blockReward)
    print('\nTo be continue #Plan₿...')
    return blockReward and years and currentBlock

bitcoin()







