import random


# TODO: Decompose into functions
def run_game():
    turns = 1
    correct = False
    code = selecting_random_numbers()
    while turns <= 12 and correct == False:     
        answer = user_input_four_digits()
        correct_digits_and_position = checking_if_user_input_is_correct(code,answer)
        correct = giving_user_feedback(correct_digits_and_position,code,turns)
        turns +=1
    print('The code was: '+str(code))


def selecting_random_numbers():
    """
    The code here is selecting random four numbers between 1 and 8.
    """
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code

def user_input_four_digits():
    """
    the code here allows the user to input a four digit code, numbers between 1 till 8.
    """
    
    answer = input("Input 4 digit code: ")
    if len(answer) != 4 or not answer.isdigit():
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    
    return answer

def checking_if_user_input_is_correct(code,answer):    
    """
    the code here checks if the user input matches the randomly selected code. 
    """    
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    return correct_digits_and_position

def giving_user_feedback(correct_digits_and_position,code,turns):
    """
    The code here provides user with feedback.
    """
    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))

    return correct

    


if __name__ == "__main__":
    run_game()
