'''
Week 1 Checkpoint Heart Rate
Calculates the key minimum and maximum heart rate for cardio exercise
Apr 22 2022
'''
given_age = int(input("Gimme ur age: "))
max_rate = int((220 - given_age) * .85)
min_rate = int((220 - given_age) * .65)


print(f"Keep your heart rate between {min_rate} and {max_rate}.")
