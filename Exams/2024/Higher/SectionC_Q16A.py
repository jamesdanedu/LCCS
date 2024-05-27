# Question 16(a)
# Examination Number:
from random import choice

fruits = ['apple', 'cherry', 'orange']
random_fruit_1 = choice(fruits) 


# part (i)
print ("Random fruit 1:", random_fruit_1)

#part (ii)
random_fruit_2 = choice(fruits)
random_fruit_3 = choice(fruits)
print ("Random fruit 2:", random_fruit_2)
print ("Random fruit 3:", random_fruit_3)

#part (iii)
if random_fruit_1 == 'cherry':
    print("First fruit is cherry")

#part (iv)
if random_fruit_1 == random_fruit_2:
    print("First pair match")

## part (v)
if random_fruit_1 == 'cherry' and random_fruit_1 == random_fruit_2:
    print("First pair are cherries")


# part (iv)
if random_fruit_1 == random_fruit_2 or random_fruit_1 == random_fruit_3 or random_fruit_2 == random_fruit_3:
    print("Matching pair")
    
fruitList = []
for i in range(0,100):
    fruitList.append(choice(fruits))
    
print(len(fruitList))

print('cherry', fruitList.count('cherry'))
print('apple', fruitList.count('apple'))
print('orange', fruitList.count('orange'))

    
   
