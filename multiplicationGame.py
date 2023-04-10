import random
points=0
mistakes=0
entry=9999


while entry != 00:
    firstValue = random.randint(1,9)
    secondValue = random.randint(1,9)
    answer = firstValue*secondValue
    print("How much is", firstValue, "times", secondValue, "?")
    entry = int(input("Answer:"))
    if entry != 00:
        if entry == answer:
            print("This is correct, the answer is:", answer)
            print()
            points+=1
        while entry != answer:
            print("That's the wrong anser, try again!", "(",firstValue,"x",secondValue,")")
            entry=int(input("Answer:"))
            print("This is correct, the answer is:", answer)
            print()
            mistakes+=1

print("You guessed", points, "right the first time and made a total of", mistakes, "mistakes.")
