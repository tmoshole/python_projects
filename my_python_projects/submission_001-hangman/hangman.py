#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    short_words = open(file_name,"r") #we opening file and asighning it a variable called fn
    lines = short_words.readlines() #the variable fn contains words that we read in lines
    short_words.close() #we closing our file
    return lines #we returning lines
    
    


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_key = random.randint(0,len(words)-1)
    random_word = words[random_key]
    random_index = random.randint(0,len(random_word)-1)
    random_letter = random_word[random_index]
    print("Guess the word: " + random_word.replace(random_letter,'_'))
    return random_word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    answer = input("Guess the missing letter: ")
    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

