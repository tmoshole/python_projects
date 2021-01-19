import random


def run_game():
    numbers_list = [] #i am defining an empty list
    
    while len(numbers_list) !=4: #i am adding the 4 randomly chosen digits to the empty list
        n = random.randint(1,8)
        if n not in numbers_list: 
            numbers_list.append(n)
    #print(numbers_list)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    guess_count = 12
    answer = []
    
    
    while len(answer) !=4 or track1 != 4:
        track1 = 0
        track2 = 0
        
        answer = input("Input 4 digit code: ")

        if len(answer) != 4 or answer.isdigit() is not True or "9" in answer or "0" in answer:
            print("Please enter exactly 4 digits.")
            continue

        #print (numbers_list)
        i = 0
        while i < 4:
            if int(answer[i]) == numbers_list[i]:    
                track1 += 1
            elif int(answer[i]) in numbers_list:
                track2 += 1
            i +=1
        print("Number of correct digits in correct place:    ", track1)
        print("Number of correct digits not in correct place:", track2)

        if track1 == 4:
            print("Congratulations! You are a codebreaker!")
        elif guess_count == 1:
            break
        else:
            guess_count = guess_count -1
            print('Turns left: '+str(guess_count))
    hi = ''
    for i in numbers_list:
        hi += str(i)
    print("The code was:", hi)
    
        
        
if __name__ == "__main__":
    run_game()
