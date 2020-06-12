# -*- coding: utf-8 -*-
"""
Testing Monte Hall's paradox for three choices.
"""

import matplotlib.pyplot as plt
import random
import numpy as np
import sys

def keep_choice(trials,basket_size):
    hist = []
    for i in range(trials):
        baskets = np.zeros((1,basket_size))#make baskets
        baskets[:,random.randint(0,basket_size-1)] = 1#plant gold bullion
        if baskets[:,random.randint(0,basket_size-1)] == True:#pick basket and record win/loss
            hist.append(1)
        else:
            hist.append(0)
    prob = np.sum(np.asarray(hist))/trials
    return prob
    
def switch_choice(trials,basket_size):
    hist = []
    for i in range(trials):
        baskets = np.zeros((1,basket_size))#make baskets
        baskets[:,random.randint(0,basket_size-1)] = 1#plant gold bullion
        pick = random.randint(0,basket_size-1) #pick basket
        
        snakes = 0#Track number of snakes revealed.
        snakes_coord = []#Track indices of revealed snakes.
        for i in range(basket_size):#Revealing N-2 snakes
            if i != pick and baskets[:,i] == False:#Ensure we skip our first choice and the bullion.
                snakes_coord.append(i)
                snakes+=1
            if snakes  == basket_size-2:#Break the loop when we unconvered enough snakes.
                break
        snakes_coord.append(pick)#We will switch our first choice anyway. Therefore we assume it has a snake.
        
        for i in range(basket_size):#Switching choice.
            if i in snakes_coord:
                continue
            else:
                pick = i
                
        if baskets[:,pick] == True:#open basket and record win/loss
            hist.append(1)
        else:
            hist.append(0)
    prob = np.sum(np.asarray(hist))/trials
    return prob#Record outcome
        
'''
Program Begins Here
'''           


prob_stay = []
prob_switch = []

trials = range(99)#Indicate number of trials.
baskets = 3#Indicate number of baskets.

for i in trials:
    prob_stay.append(keep_choice(i+1,baskets))
    prob_switch.append(switch_choice(i+1,baskets))


plt.plot(trials,prob_stay,marker="o",label='keep choice')
plt.plot(trials,prob_switch,marker="o",label='switch choice')
plt.xlabel('Number of trials')
plt.ylabel('Probability')
plt.legend()
plt.show()