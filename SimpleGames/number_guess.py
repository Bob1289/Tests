import random

if __name__ == '__main__':

    num_range = int(input("What range would you like to do? From 0 to _?"))
    number = random.randint(0,num_range)
    guess = None

    while guess != number:
        guess = int(input("What is your guess?"))

        if guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")

    print("Congrats on guessing {}".format(number))
        

    