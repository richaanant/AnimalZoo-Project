#Step 1
animals = ["dog", "cat", "bird", "fish"]
names = ["joe", "bob", "sally", "jane"]
food_kilograms = [16,7,10,12]
weight = [400,200,600,800]

print("--------------")
#Step 2
# if an animal weight is below 600 pounds
for i in range(len(animals)):
    if weight[i] < 600:
        print(names[i] + " the " + animals[i] + " is dangerous ")
print("--------------")
#Step 3
def food_amount(index):
    food_kilograms[i] = food_kilograms[i] + 2
    weight[index] = weight[i] - 5
for i in range(len(animals)):
    food_amount(i)
    print(names[i] + " the " + animals[i] + " need to eat more food " + str(food_kilograms[i]) + " but needs to lose weight " + str(weight[i]))
print("--------------")
#Step 4
def newAnimal():
    animals.append("horse")
    print(animals)
    names.append("Tom")
    print(names)
    food_kilograms.append(9)
    print(food_kilograms)
    weight.append(500)
    print(weight)
    print("New animal named " + names[4] + " is a " + animals[4])
newAnimal()
print("--------------")
#Step 5
def animalReport():
    animal_trainers = ["Tyler", "Sam", "Sarah", "Justin"]
    trainers_skill = ["big animals", "small animals", "medium animals", "huge animals"]
    print(names[0] + " the " + animals[0] + " can work with " + animal_trainers[0])
    print(names[1] + " the " + animals[1] + " can work with " + animal_trainers[2])
    print(names[2] + " the " + animals[2] + " can work with " + animal_trainers[1])
    print(names[3] + " the " + animals[3] + " can work with " + animal_trainers[1])
    print(names[4] + " the " + animals[4] + " can work with " + animal_trainers[0])
    if animals[0] != trainers_skill[1]:
        print(animals[0] + " does not match " + trainers_skill[1])
    if animals[0] != trainers_skill[3]:
        print(animals[0] + " does not match " + trainers_skill[3])
    if animals[1] != trainers_skill[0]:
        print(animals[1] + " does not match " + trainers_skill[0])
    if animals[1] != trainers_skill[3]:
        print(animals[1] + " does not match " + trainers_skill[3])
    if animals[2] != trainers_skill[0]:
        print(animals[2] + " does not match " + trainers_skill[0])
    if animals[2] != trainers_skill[2]:
        print(animals[2] + " does not match " + trainers_skill[2])
    if animals[2] != trainers_skill[3]:
        print(animals[2] + " does not match " + trainers_skill[3])
    if animals[3] != trainers_skill[0]:
        print(animals[3] + " does not match " + trainers_skill[0])
    if animals[3] != trainers_skill[2]:
        print(animals[3] + " does not match " + trainers_skill[2])
    if animals[3] != trainers_skill[3]:
        print(animals[3] + " does not match " + trainers_skill[3])
    if animals[4] != trainers_skill[1]:
        print(animals[4] + " does not match " + trainers_skill[1])
    if animals[4] != trainers_skill[2]:
        print(animals[4] + " does not match " + trainers_skill[2])
animalReport()