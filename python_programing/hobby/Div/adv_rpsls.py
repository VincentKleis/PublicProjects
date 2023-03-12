import random
number_to_RPSLS = {1:"Rock", 2:"Paper", 3:"Scissor", 4:"Lizard", 5:"Spock"}
RPSLS = {"Rock": 
            {"Rock" : "Rock✊ bounces of Rock✊.\n It's a Tie!", 
            "Paper": "Paper✋ encasses Rock✊.\n You Win!", 
            "Scissors": "Scissor✌️ is crushed by Rock✊.\n You Lose!",
            "Lizard": "Lizard🤏 is crushed by Rock✊.\n You Lose!",
            "Spock": "Spock🖖 dissintegrates Rock✊.\n You Win!"},
        "Paper":
            {"Rock": "Rock✊ is encased by Paper✋.\n You Lose!",
            "Paper": "Paper✋ stacks on Paper✋.\n It's a Tie!",
            "Scissor": "Scissor✌️ cuts Paper✋.\n You Win!",
            "Lizard": "Lizard🤏 eats Paper✋.\n You Win!",
            "Spock": "Spock🖖 is disprooven by Paper✋.\n You Lose!"},
        "Scissor": 
            {"Rock": "Rock✊ crushes Scissor✌️.\n You Win!",
            "Paper": "Paper✋ is cut by Scissor✌️.\n You Lose!",
            "Scissor": "Scissor✌️ scissors Scissor✌️.\n It's a Tie!",
            "Lizard": "Lizard🤏 is decapetated by Scissor✌️.\n You Lose!",
            "Spock": "Spock🖖 breakes Scissor✌️.\n You Win!"},
        "Lizard":
            {"Rock": "Rock✊ crushes Lizard🤏.\n You Win!",
            "Paper": "Paper✋ is eaten by Lizard🤏.\n You Lose!",
            "Scissor": "Scissor✌️ decapitates Lizard🤏.\n You Win!",
            "Lizard": "Lizard🤏 befrends Lizard🤏.\n It's a Tie!",
            "Spock": "Spock🖖 is poisoned by Lizard🤏.\n You Lose!"},
        "Spock":
            {"Rock": "Rock✊ is dissintegrated by Spock🖖.\n You Lose!",
            "Paper": "Paper✋ dissproves Spock🖖.\n You Win!",
            "Scissor": "Scissor✌️ is broken by Spock🖖.\n You Lose!",
            "Lizard": "Lizard🤏 poisons Spock🖖.\n You Win!",
            "Spock": "Spock🖖 is confused by an other Spock🖖.\n It's a tie!"}
        }

print("\
=================================\
rock paper scissors lizard spock!\
=================================")

computer = random.randint(1,5)

user = input("\
1) ✊\n\
2) ✋\n\
3) ✌️\n\
4) 🤏\n\
5) 🖖\n")
user = number_to_RPSLS[int(user)]
computer = number_to_RPSLS[int(computer)]

computer_dict = RPSLS[computer]
print(f"computer chose {computer}\n {computer_dict[user]}")