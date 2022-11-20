# bitcoin halving

def convert(bitcoin):
    satoshi = bitcoin * 1000000
    return satoshi

def bitcoin():
    blockReward = 50
    years = 2008
    numberOfHalv = 0
    while blockReward >= 0.0002 and years <= 2080 :
        blockReward = blockReward / 2
        years += 4
        numberOfHalv += 1
        if blockReward < 0.01:
                print('')
                print(str(numberOfHalv)+'th','₿itcoin halving year:',years,'block reward reduced to:',blockReward,'\nsatoshi =',convert(blockReward))
        else: print(str(numberOfHalv)+'th','₿itcoin halving year:' ,years,'block reward reduced to:',blockReward)
    return blockReward and years

bitcoin()










print(convert(1))