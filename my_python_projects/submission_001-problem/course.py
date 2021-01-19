

def create_outline():
    print("Course Topics:")
    topics = set(["* Introduction to Python", 
    "* Tools of the Trade", 
    "* How to make decisions", 
    "* How to repeat code", 
    "* How to structure data", 
    "* Functions", 
    "* Modules"])
    sort = list(topics)
    sort.sort()
    for i in sort:
        print(i)
   
    print('Problems:')
    new_dict = dict()
    for i in topics:
        new_dict[i] = [' Problem 1, Problem 2, Problem 3']

    for x, y in new_dict.items():
        print(x, end = '')
        print(" :", end='')
        for i in range(len(y)):
            print(y[i], end='')
            print(' ', end='')
        print('')
    
    print('Student Progress:')
    progress = ("1. Sam - Introduction to Python - Problem 2 [STARTED]", 
    "2. Tom - Tools of the Trade - Problem 3 [GRADED]", 
    "3. Jerry - How to make decisions - Problem 3 [GRADED]", 
    "4. Masedi - How to repeat code - Problem 1 [COMPLETED]", 
    "5. Karabo - How to structure data - Problem 2 [STARTED]", 
    "6. Naledi - Functions - Problem 1 [COMPLETED]", 
    "7. Nkele - Modules - Problem 2 [GRADED]")
    for x in progress:
        print(x)

    

        


if __name__ == "__main__":
    create_outline()
