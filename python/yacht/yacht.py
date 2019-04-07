# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    result = 0

    if category == YACHT:
        if dice.count(dice[0]) == 5:    #Checks for yacht-all same number
            result = 50
    
    if category == ONES:
        result = 1 * dice.count(1)
    
    if category == TWOS:
        result = 2 * dice.count(2)

    if category == THREES:
        result = 3 * dice.count(3)

    if category == FOURS:
        result = 4 * dice.count(4)

    if category == FIVES:
        result = 5 * dice.count(5)

    if category == SIXES:
        result = 6 * dice.count(6)

    if category == FULL_HOUSE:  #2 unique values; one repeated thrice; other repeated twice
        #Check for the number of uniq vals
        uniq_val = list()
        for i in dice:
            if i not in uniq_val:
                uniq_val.append(i)
        
        #Check number of occurance of unique 
        if len(uniq_val) == 2:
            if dice.count(uniq_val[0]) == 2 and dice.count(uniq_val[1]) == 3 or dice.count(uniq_val[0]) == 3 and dice.count(uniq_val[1]) == 2:
                result = sum(dice)

    if category == FOUR_OF_A_KIND: # 2 uniq val; one repeated four times
        uniq_val = list()
        for i in dice:
            if i not in uniq_val:
                uniq_val.append(i)

        if len(uniq_val) == 2:
            if dice.count(uniq_val[0]) == 4:
                result = uniq_val[0] * 4     

            if dice.count(uniq_val[1]) == 4:
                result = uniq_val[1] * 4
        
        if len(uniq_val) == 1:  #Yacht can be scored as a four of a kind
            result = uniq_val[0]*4

    if category == LITTLE_STRAIGHT: # dice is 1,2,3,4,5
        if list(range(1,6)) == sorted(dice):
            result = 30

    if category == BIG_STRAIGHT:      # dice is 2,3,4,5,6
        if list(range(2,7)) == sorted(dice):
            result = 30

    if category == CHOICE:
        result = sum(dice)
    
    return result

