word = input("What word would you like me to spell? ")
letter = len(word)
length = len(word)
while letter> 0:
    print(word[length - letter])
    letter -= 1