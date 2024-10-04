#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    '''
    determine the winner of the game
    '''
    maria = 0
    ben = 0
    for i in range(x):
        m = True
        b = False
        original = [num for num in nums]
        print(original)
        temp = []
        for j in original:
            if j == 1 and len(original) == 1:
                # if the number is one and the range is one, Ben wins
                ben += 1
            elif j != 1:
                temp.append(j)

        print(temp)

        for t in temp:
            n = [b for b in range(t)]
            n.pop(0)
            print(temp)
            print(n)
            for i in n:
                ranTemp = []
                print(i)
                if m:
                    print("maria", m)
                    print("ben", b)
                    # select number
                    print(i)
                    if n and n[i] != 1:
                        pm = n[i]
                    else:
                        return
                    # remove the prime number and it's multiples
                    ranTemp = setTemp(n, pm)
                    # switch to ben

                    m = False
                    b = True
                    # return temp, b, m
                if b:
                    print("maria", m)
                    print("ben", b)
                    if n and n[i] != 1:
                        pm = n[i]
                    else:
                        break
                    # remove the prime number selected and its multiples
                    ranTemp = setTemp(n, pm)
                    # switch player
                    m = True
                    b = False
                    # return temp, b, m
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None


def setTemp(numbers, k):
    l = []
    if numbers:
        for i in numbers:
            if i != k and i % k != 0:
                l.append(i)
    return l
