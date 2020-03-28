import random

#Uppercase range 65-91
#lowercase range 97-123
#numbers range 48-58
#special range 33-48, 58-65, 91, 93-97, 123-127
#all 33-127
UPPER = list(range(65,91))
LOWER = list(range(97,123))
NUMBER = list(range(48,58))
SPECIAL = (list(range(33,48))  
   + list(range(58,65))  
   + list(range(91,92))  
   + list(range(93,97))  
   + list(range(123-127)))
length = 16

for i in range(length):
    print(chr(random.choices(
            [random.choice(UPPER), 
                random.choice(LOWER),
                random.choice(NUMBER),
                random.choice(SPECIAL)],
            weights=[0.29, 0.29, 0.29, 0.13],
            k=1)[0]), end='')
print()

