import random
while True:
    user_input = input("Choose any one: rock, paper, scissor:")
    user_input = user_input.lower()

    if user_input == "quit":
        break

    if user_input != "rock" and user_input != "paper" and user_input != "scissor":
        print("Choose the correct option")
        continue
    
    computer_choice = random.choice(["rock", "paper", "scissor"])
    print(f"computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("You Tied")
        continue

    elif user_input == "rock" and computer_choice == "scissor":
        print("You Win")
        break

    elif user_input == "rock" and computer_choice == "paper":
        print("You win")
        break

    elif user_input == "scissor" and computer_choice == "paper":
        print("You Win")
        break
    
    elif user_input == "scissor" and computer_choice == "rock":
        print("You Hit")
        continue

    elif user_input == "paper" and computer_choice == "scissor":
        print("You Hit")
        continue

    elif user_input == "paper" and computer_choice == "rock":
        print("You Hit")
        continue

    else:
        print("You lost")
