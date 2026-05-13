# I expanded the story by adding a few more word prompts like a noun and an emotion
# to make the story longer and more fun to read.

# Sample words to test the program:
# adjective: fluffy
# animal: cat
# verb: running
# exclamation: oh my
# verb: spin
# verb: dance
# noun: umbrella
# emotion: confused

print("Please enter the following:")
print()

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
noun = input("noun: ")
emotion = input("emotion: ")

exclamation = exclamation.capitalize()

print()
print("Your story is:")
print()

print("The other day, I was really in trouble. It all started when I saw a very")
print(adjective, animal, verb1, "down the hallway. \"" + exclamation + "!\" I yelled. But all")
print("I could think to do was to", verb2, "over and over. Miraculously,")
print("that caused it to stop, but not before it tried to", verb3)
print("right in front of my family. I grabbed my", noun, "and ran away feeling very", emotion + ".")