import random



def list_words():
    list_of_words = []
    with open('data/words.txt', 'r') as f:
        list_of_words = f.read().split()

    return list_of_words

def choose_randon_word():
    word = random.choice(list_words())
    return word


def correct_letter(word_answear, tries):
    print('Great, you choose the correct letter')
    print(''.join(word_answear))
    print('You have {} try'.format(tries))

def player_won(word_answear):
    print('Congratulations, you win')
    print(''.join(word_answear))

def wrong_letter(word_ansear, turns, max_turns):
    print("Bad choice!")
    print_hangman(turns, max_turns)
    if turns == max_turns:
        print('The word was {}'.format(word_ansear))

def print_hangman(turns, max_turns):
    if turns >= 1:
        print("{} turns left".format(max_turns - turns))
        print("  --------  ")
    if turns == 2:
        print("     O      ")
    if turns == 3:
        print("     O      ")
        print("     |      ")
    if turns == 4:
        print("     O      ")
        print("     |      ")
        print("    /       ")
    if turns == 5:
        print("     O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 6:
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 7:
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
    if turns == 8:
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
    if turns == 9:
        print("  --------  ")
        print("   \ O_|/   ")
        print("     |      ")
        print("    / \     ")
        print("Last breaths counting, Take care!")
    if turns == 10:
        print("     O_|    ")
        print("    /|\      ")
        print("    / \     ")
        print("You loose")
        print("You let a kind man die")


def new_game():
    word = choose_randon_word()
    word_answear = ['_' for x in range(len(word))]
    print('The word have {} characters.'.format(len(word)))
    turns = 0
    missed = len(word)
    max_turns = 10

    while turns < max_turns:
        choose = input('Choose one letter: \n')
        if choose.lower() in word.lower() and choose not in word_answear:
            for i in range(len(word)):
                if word[i].lower() == choose.lower():
                    word_answear[i] = word[i].lower()
                    missed -= 1
            if missed > 0:
                correct_letter(word_answear, (max_turns - turns))
            else:
                player_won(word_answear)
                break
        else:
            turns += 1
            wrong_letter(word, turns, max_turns)


while True:
    new_game()
    other = input("New Game? Y/N \n")
    if other.upper() != 'Y':
        break
