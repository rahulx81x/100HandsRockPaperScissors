import random
hand_signs = ['r', 'p', 's']  # r=rock,p=paper,s=scissor(as if it's not obvious)

computer = []
for i in range(100):
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    z = random.randint(1, 3)
    computer.append(random.choices(hand_signs, weights=(x, y, z), k=1))
