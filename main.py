# bitcoin halving

def convert(blockReward):
    satoshi = blockReward*1000000 # satoshi = 0.00000001
    return satoshi
def bitcoin():
    blockReward = 50
    years = 2008
    numberOfHalv = 0
    print('')
    while blockReward >= 0.0002 and years <= 2080 :
        blockReward = blockReward / 2
        years += 4
        numberOfHalv += 1
        if blockReward < 0.01:
                print('')
                print(str(numberOfHalv)+'th','₿itcoin halving year:',years,'block reward reduced to:',blockReward,'\nsatoshi =',convert(blockReward))
        else: print(str(numberOfHalv)+'th','₿itcoin halving year:' ,years,'block reward reduced to:',blockReward)
    print('\nTo be continue #Plan₿...')
    return blockReward and years


bitcoin()







