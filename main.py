#Farouk Agbaje
#Aug 8th, 2021
def mad_lib():
    #This function will take user input and place them in the story

    #--User--Input--
    adj_1 = input("Enter an adjective: ")
    adj_2 = input("Enter another adjective: ")
    type_of_bird = input("Enter a type of bird: ")
    room_in_a_house = input("Enter a room you'd find in a house: ")
    verb_past_tense_1 = input("Enter a verb in the past tense: ")
    verb_1 = input("Enter a verb: ")
    relatives_name = input("Enter the name of a relative: ")
    noun_1 = input("Enter a noun: ")
    liquid = input("Enter any liquid: ")
    verb_end_ing_1 = input("Enter a verb that ends in -ing: ")
    part_of_the_body = input("Enter a part of the body: ")
    plural_noun = input("Enter a noun in plural form: ")
    verb_end_ing_2 = input("Enter another verb that ends in -ing: ")
    noun_2 = input("Lastly, Enter another noun and I will create your story: ")

    print(f"It was a {adj_1}, cold November day.")
    print(f"I woke up to the {adj_2} smell of {type_of_bird}")
    print(f"roasting in the {room_in_a_house} downstairs.")
    print(f"I {verb_past_tense_1} down the stairs to see if I could help {verb_1} the dinner.")
    print(f"My mom said , 'See if {relatives_name} needs a fresh {noun_1}.'")
    print(f"So I carried a tray of glasses full of {liquid} into the {verb_end_ing_1} room.")
    print(f"When I got there, I couldn't believe my {part_of_the_body}!")
    print(f"There were {plural_noun} {verb_end_ing_2} on the {noun_2}!")
    print("The End!")




if __name__ == '__main__':
    print("Hello! Welcome to my Mad Libs story creator. You will get prompts to enter in words and\"")
    print(" all you have to do is type in a word and hit enter.")
    print("Enjoy!")

    play_again = True

    while play_again:

        mad_lib()

        print("Would you like to play again? The story remains the same but the words you enter can be different!")

        go_again = input("Enter Y to play again or N to exit: ").upper()
        if go_again == 'Y':
            play_again = True
        else:
            play_again = False
            print("Thank you for playing")

