# Create a tuple named zoo that contains your favorite animals.
zoo = ("Armadillo", "Turtle", "Hedgehog", "Tree Frog")

# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("Hedgehog"))

# Determine if an animal is in your tuple by using for value in tuple.

if "Koala" in zoo:
    print(zoo.index("Koala"))
else:
    print("zoo does not contain this animal")

# Create a variable for each of the animals in your tuple with this cool feature of Python.

(animal1, animal2, animal3, animal4) = zoo
print(animal1)

# Convert your tuple into a list.
zoo_list = list(zoo)
print(zoo_list)

# Use extend() to add three more animals to your zoo.
zoo_list.extend(["Koala", "Bushbaby", "Giraffe"])
print(zoo_list)

# Convert the list back into a tuple.
zoo_tuple = tuple(zoo_list)
print(zoo_tuple)
