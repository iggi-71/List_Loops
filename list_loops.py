songs = ["ROCKSTAR", "Do It", "For The Night"]

#Question 1
print(songs[1])

#Question 2
print(songs[1:3])

#Question 3
songs[-1] = "Goin Baby"
print(songs)

#Question 4
songs.append("Mood Swings")
songs.extend(["For the Night"])
songs.insert(0, "Bop")
print(songs)

#Question 4
songs.pop(1)
print(songs)

#Question 5
print("Option 1 is prints from the list")
print("Option 2 is displaying the indexes of the list")

#Question 6 a
animals = ["Cat", "Dog", "Bird"]
#Question 6 b
animals.append("Snake")
#Question 6 c
print(animals)
#Question 6 d
print(animals[2])
#Question 6 e
animals.pop(0)
#Question 6 f
for animals in animals:
    print(animals)
