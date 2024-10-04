#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    """
    determine the winner of the game after x rounds
    """
    m_score = 0
    b_score = 0

    while x:
        x -= 1
        Maria = True
        Ben = False

        # round one:
        if nums[x] == 1:
            # by default Ben wins
            b_score += 1
        else:
            # create a list of numbers in range nums[x]
            numbers = [n for n in range(1, nums[x] + 1)]

            while numbers:
                i = 0
                # Maria's turn to play
                if Maria:
                    if len(numbers) == 1 and numbers[i] == 1:
                        # Ben wins
                        b_score += 1
                        return
                    else:
                        if numbers:
                            pm = numbers[i]
                            numbers = setTemp(numbers, pm)
                            Maria = False
                            Ben = True

                if Ben:
                    # Ben's turn to play
                    if len(numbers) == 1 and numbers[i] == 1:
                        # Maria wins
                        m_score += 1
                        return
                    else:
                        if numbers:
                            pm = numbers[i]
                            numbers = setTemp(numbers, pm)
                            Maria = True
                            Ben = False

    if m_score > b_score:
        return "Maria"
    elif b_score > m_score:
        return "Ben"
    else:
        return None


def setTemp(n, pm):
    l = []
    if n:
        for i in n:
            if i != pm and i % pm != 0:
                l.append(n)
    return l
