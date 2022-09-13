import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

state = pd.DataFrame([0,0,0,0],index=['clock','station1','station2','customer'])
station1 = 0
station2 = 0
customer = 0
clock = 0
next_arrival = np.random.exponential(1/1.8)
next_station1_1 = 1e10
next_station1_2 = 1e10
next_station2 = 1e10
number_event = 0

for i in range(1000):
    clock = min(next_station1_1,next_station1_2,next_station2,next_arrival)

    if next_arrival == clock:
        number_event += 1
        station1 += 1
        #station2
        customer += 1
        state[number_event] = [clock,station1,station2,customer]
    elif next_station1_1 == clock:
        number_event += 1
        station1 -= 1
        station2 += 1
        #customer
        state[number_event] = [clock,station1,station2,customer]
    elif next_station1_2 == clock:
        number_event += 1
        station1 -= 1
        station2 += 1
        #customer
        state[number_event] = [clock,station1,station2,customer]
    elif next_station2 == clock:
        number_event += 1
        #station1
        station2 -= 1
        customer -= 1
        state[number_event] = [clock,station1,station2,customer]


    next_arrival = clock + np.random.exponential(1/1.8)

    if station1 >= 2:
        next_station1_1 = clock + np.random.exponential(1)
        next_station1_2 = clock + np.random.exponential(1)
    elif station1 > 0:
        next_station1_1 = clock + np.random.exponential(1)
        next_station1_2 = clock + 1e10
    else:
        next_station1_1 = clock + 1e10
        next_station1_2 = clock + 1e10

    if station2 > 0:
        next_station2 = clock + np.random.exponential(2)
    else:
        next_station2 = clock + 1e10

#%%
