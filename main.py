from random import randint
from random import shuffle
  # random
  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
# print("random")
# dice1=randint(1,6)
# print(f'dice1 : {dice1}')
# dice2= randint(1,6)
# print(f'dice2 : {dice2}')
# rollDoubles= dice1==dice2
# if rollDoubles:
#   print('you rolled doubles')
# else:
#   print('Not doubles')  
# if dice1 ==1 and dice2 == 1:
#   print('Snake eyes')
# else:
#   print("not snake eyes")

#practice with shuffle
# my_list= range(1,51)
# print(list(my_list))

# my_list=list(my_list)
# shuffle(my_list)
# print(my_list)

#challenge
new_list=randint(1,201)
print('new list')
print(new_list)
if new_list%2==0:
  print('It is even')
else:
  print('Odd')
