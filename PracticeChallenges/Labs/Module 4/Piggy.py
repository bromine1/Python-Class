import random

print("Please read this nursery rhyme,")
# define function
def pig(action):
    return("this little Piggy " + action)
# setup lists
actions = ["went to the market.", "stayed home.", "had roast beef.", "had none.", "Went all the way home"]
happened = []

done = False
while done == False:
    x = random.randint(0, len(actions)-1)
    if actions[x] in happened:
        continue
    happened.append(actions[x])
    print(pig(actions[x]))
    if len(happened) == len(actions):
        break