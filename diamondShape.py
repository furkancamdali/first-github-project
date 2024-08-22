#loops practices
def printDiamond(ran):
    for a in range(ran):
        if a==0 :
            print(' '*ran,'x')
        else:
            print(' '*(ran-a),'x',' '*(2*a-2)+'x')

    for b in range(ran):
        if b==ran:
            print(' '*ran,'x')
        else:
            print(' '*b,'x',' '*(2*(ran-b)-2)+'x')
    print(' '*ran,'x')



printDiamond(7)