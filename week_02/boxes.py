'''
Week 2 Checkpoint Boxes
Calculates how many boxes the user will need for x items per box.
Apr 27 2021
'''
import math

total_item = int(input('Enter the number of items: '))
item_per_box = int(input('Enter the number of items per box: '))

total_box = math.ceil(total_item / item_per_box)

print(total_box)
