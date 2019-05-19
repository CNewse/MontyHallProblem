"""

CNewse
19/05/2019

Attempting to simulate the monty hall problem.

It's based on a game show where the contestant is shown 3 doors and
told that behind 2 of the doors are goats, the other door has a car behind it.
based on wanting to win the car. The contestant picks a door.
The host then reveals one door behind which is a goat and asks if you
would like to change your door choice.

The theory is that the contestant should always change doors after one
goat is revealed. This is because in theory the odds of winning after one goat
has been revealed increase from one in three before to two in three.

I will simulate this event a number of times below and visualise the
results to test the theory.

"""

import random

def sim_swap():
    #setup the doors and random allocation of goats and car to the doors
    doors = {
        "door1": "goat",
        "door2": "goat",
        "door3": "goat"
    }

    car_door = random.randint(1,3)
    doors["door{}".format(car_door)] = "car"

    #print(doors)

    #Contestant pcik
    door_picked = random.randint(1,3)
    #print("Contestant picked door {}".format(door_picked))


    #Check what contestant initially has, if car then remove any other door.
    #If goat then remove other goat

    removed_door = [1,2,3]

    if door_picked == car_door:
        removed_door.remove(car_door)
        removed_door.remove(random.choice(removed_door))
        #print("reveal door {} as goat".format(removed_door[0]))
    if door_picked !=  car_door:
        removed_door.remove(door_picked)
        removed_door.remove(car_door)
        #print("reveal door {} as goat".format(removed_door[0]))

    remaining_door = [1,2,3]
    remaining_door.remove(removed_door[0])
    remaining_door.remove(door_picked)

    #print("player swaps to door {}".format(remaining_door[0]))

    #records result
    if doors["door{}".format(remaining_door[0])] == "car":
        return 1
    else:
        return 0

def no_swap():
    # setup the doors and random allocation of goats and car to the doors
    doors = {
        "door1": "goat",
        "door2": "goat",
        "door3": "goat"
    }

    car_door = random.randint(1, 3)
    doors["door{}".format(car_door)] = "car"

    # print(doors)

    # Contestant pick
    door_picked = random.randint(1, 3)

    if door_picked == car_door:
        return 1
    else:
        return 0


swap_results = []
no_swap_results = []
for i in range(100000):
    swap_results.append(sim_swap())
    no_swap_results.append(no_swap())
    #print(results[i])

print("the player who swapped doors after the reveal, won {} times - {} percent".format(
    sum(swap_results),
    (sum(swap_results)/len(swap_results)*100)))

print("the player who stuck with their original choice of door after the reveal, won {} times - {} percent".format(
    sum(no_swap_results),
    (sum(no_swap_results)/len(no_swap_results)*100)))