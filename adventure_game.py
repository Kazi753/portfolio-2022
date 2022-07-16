import time

import random  # random character from list
items = []
name_list = ['Pirate', 'Gorgon', 'Dragon', 'Wicked Fairy', 'Troll']
random_villain = random.choice(name_list)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_number_input(question):  # asking player to enter a valid entry
    while True:
        response = input(question)
        if response == '1' or response == '2':
            print("Okay!")
            return response
        else:
            print("Sorry! I don't understand.")


def valid_letter_input(question):  # asking player to enter a valid entry
    while True:
        response = input(question)
        if response == 'y' or response == 'n':
            print("Okay!")
            return response
        else:
            print("Sorry! I don't understand.")


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {random_villain} is somewhere around "
                "here, and has been terrifying the nearby. "
                "village.")
    print_pause("In front of you is a house!")
    print_pause("To your right is a dark cave!")
    print_pause("In your hand you hold your trusty"
                "(but not very effective)dagger.")


def house(items):  # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {random_villain}")
    print_pause(f"Eep! This is the {random_villain}'s house!")
    print_pause(f"The {random_villain} attacks you!")
    pick_option(items)


def cave(items):  # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    if "new_sword" in items:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
    else:
        print_pause("Your eye catches a glint of metal behind a rock. ")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        items.append("new_sword")
    print_pause("You walk back out to the field.")
    adventure_game(items)


def fight(items):  # Things that happen when the player fights
    if "new_sword" in items:
        print_pause(f"As the {random_villain} moves to attack,"
                    "you unleash your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand\n"
                    "as you brace yourself for the attack.")
        print_pause(f"But the {random_villain} takes one look at your"
                    "shiny newtoy and runs away!")
        print_pause(f"You have rid the town of the {random_villain}, You are "
                    "victorious!")
    else:
        print_pause("You do your best.")
        print_pause(f"But your dagger is not match for the {random_villain}")
        print_pause("You feel a bit under-prepared for this, with only having "
                    "a tiny dagger.")
        print_pause("You have been defeated.")

    items.append("new_sword")
    play_again(items)


def field(items):  # Things that happen when the player runs back to the field
    print_pause("You run back into the field.\n"
                "Luckily, you don't seem to have been followed.")
    adventure_game(items)


def adventure_game(items):
    print_pause("What would you like to do? Please enter 1 or 2.")
    user_choice = valid_number_input("Enter 1 to knock on the door of"
                                     "the house.\n"
                                     "Enter 2 to peer into the cave.\n")
    if user_choice == '1':
        house(items)
    elif user_choice == '2':
        cave(items)


def pick_option(items):
    print()
    print_pause("Would you like to fight or runaway")
    user_choice = valid_number_input(
        "Enter 1 to fight \n" "Enter 2 to runaway.")

    if user_choice == '1':
        fight(items)
    elif user_choice == '2':
        field(items)


def play_again(items):  # asking player to play again
    print_pause("Would you like to play again?")
    answer = valid_letter_input("y/n")
    if answer == "y":
        print("Restarting the game")
        main(items)
    elif answer == "n":
        print("Thanks for playing! See you next time.")
        exit()
    adventure_game(items)


def main(items):
    intro()
    adventure_game(items)


main(items)
