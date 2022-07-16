import random

if __name__ == '__main__':

    scenarios = [
        ["Tie","Lose","Win"],
        ["Win","Tie","Lose"],
        ["Lose","Win","Tie"]
        ] 

    methods = {"Rock": 0, "Paper": 1, "Scissor": 2}
    bot_methods = {0: "Rock", 1: "Paper", 2: "Scissor"}

    user_score, bot_score = 0,0

    while 1:
        bot_num = random.randint(0, 2)

        user_num = input("Rock Paper or Scissor?\n")
        result = scenarios[methods[user_num]][bot_num]

        if result == "Win":
            user_score += 1
        elif result == "Lose":
            bot_score += 1

        print("____________________________________")
        print("\nBot: {} \nYou: {}\n\nResult: {}\n\nScore:\n\nBot: {}\nYou: {}\n".format(user_num,bot_methods[bot_num],result,bot_score,user_score))
        print("____________________________________")