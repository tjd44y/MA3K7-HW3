import numpy as np
import random

hat_contents = list(range(1, 5))

print('The intitial contents of the hat are', hat_contents)

while len(hat_contents) > 1:
    choices = random.sample(hat_contents, 2)
    print('The random choices are', choices)
    print('Their positive difference is', abs(choices[0]-choices[1]))
    hat_contents.remove(choices[0])        
    hat_contents.remove(choices[1])
    hat_contents.append(abs(choices[0]-choices[1]))
    if len(hat_contents) == 1:
        print('The final number is', hat_contents)
    else:
        print('The contents of the hat are', hat_contents)
