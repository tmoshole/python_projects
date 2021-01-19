
# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint','replay',\
'reverse','replay silent','replay reversed','replay reversed silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left','sprint']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# keeping history
history = []

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    slipt_arg1 = arg1.split('-')
    digit = ''
    if " " in arg1:
        (digit, rev) = arg1.split(' ')
    


    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1)\
         or arg1.lower() == 'silent' or arg1.lower() == 'reversed' or arg1.lower() \
             == 'reversed silent' or  (is_int(slipt_arg1[0]) and  is_int(slipt_arg1[1]))\
                  or (is_int(digit) and rev == 'reversed') or (is_int(digit) and rev == 'silent'))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) +
     .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def replay_commands(robot_name,command):
    """
    this funtions replays the forward,back,left,right and sprint commands according to the order the player ran the game.
    """
    global history
    global directions
    filter_list = ['help','off','replay','replay silently','replay reversed']
    filtered_list = list(filter(lambda cmd: cmd not in filter_list, history))
    replay = [handle_command(robot_name, command) for command in filtered_list]
    return True,' > '+robot_name+' replayed '+str(len(filtered_list))+' commands.'


def replay_silent(robot_name,command):
    """
    the function replays the users commands but only prints out the
    number of commands replayed and the updates and prints the position. 
    """
    global history
    filter_list = ['help','off','replay','replay silent']
    filtered_list = list(filter(lambda cmd: cmd not in filter_list, history))
    for command in filtered_list:
        (command_name, arg) = split_command_input(command)
        if command_name == 'forward':
            (do_next, command_output) = do_forward(robot_name, int(arg))
        elif command_name == 'back':
            (do_next, command_output) = do_back(robot_name, int(arg))
        elif command_name == 'right':
            (do_next, command_output) = do_right_turn(robot_name)
        elif command_name == 'left':
            (do_next, command_output) = do_left_turn(robot_name)
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg))
    return True,' > '+robot_name+' replayed '+str(len(filtered_list))+' commands silently.'


def do_replay_reversed(robot_name,command):
    """
    this funtions replays the forward,back,left,right and sprint 
    commands in the reverse order.
    """
    global history
    filter_list = ['help','off','replay','replay reversed']
    filtered_list = list(filter(lambda cmd: cmd not in filter_list, history))
    filtered_list.reverse()
    replay = [handle_command(robot_name, command) for command in filtered_list]
    return True,' > '+robot_name+' replayed '+str(len(filtered_list))+' commands in reverse.'


def do_Replay_reversed_silent(robot_name,command):
    """
    this funtions replays the forward,back,left,right and sprint commands 
    in the reverse order. Only returns the position.
    """
    global history
    global directions
    list(filter(lambda cmd: cmd in directions, history))
    history.reverse()
    for command in history:
        (command_name, arg) = split_command_input(command)
        if command_name == 'forward':
            (do_next, command_output) = do_forward(robot_name, int(arg))
        elif command_name == 'back':
            (do_next, command_output) = do_back(robot_name, int(arg))
        elif command_name == 'right':
            (do_next, command_output) = do_right_turn(robot_name)
        elif command_name == 'left':
            (do_next, command_output) = do_left_turn(robot_name)
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg))
    return True,' > '+robot_name+' replayed '+str(len(history))+' commands in reverse silently.'


def replay_limit_range(robot_name,command):
    """
    this is the function for replay limit range. 
    """
    global history
    global directions
    list(filter(lambda cmd: cmd in directions, history))
    replay_list = []
    (agr1, agr2) = split_command_input(command)
    list_len = len(history) - int(agr2)
    while list_len < len(history):
        replay_list.append(history[list_len])
        list_len += 1
    for command in replay_list:   
        handle_command(robot_name, command)
    return True,' > '+robot_name+' replayed '+str(len(replay_list))+' commands.'


def do_replay_limit_range_silent(robot_name,command):
    """
    replay limit range silently. Only prints the number of 
    funtions replayed and the updated position.
    """
    global history
    global directions
    list(filter(lambda cmd: cmd in directions, history))
    replay_list = []
    (arg1, arg2) = split_command_input(command)
    (arg3, arg4) = arg2.split(' ')
    list_len = len(history) - int(arg3)
    while list_len < len(history):
        replay_list.append(history[list_len])
        list_len += 1
    for command in replay_list: 
        (command_name, arg) = split_command_input(command)
        if command_name == 'forward':
            (do_next, command_output) = do_forward(robot_name, int(arg))
        elif command_name == 'back':
            (do_next, command_output) = do_back(robot_name, int(arg))
        elif command_name == 'right':
            (do_next, command_output) = do_right_turn(robot_name)
        elif command_name == 'left':
            (do_next, command_output) = do_left_turn(robot_name)
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg))
    return True,' > '+robot_name+' replayed '+str(len(replay_list))+' commands silently.'


def do_replay_limit_reversed(robot_name,command):
    """
    the funtions replays the commands stored in history in reverse.
    """
    global history
    global directions
    list(filter(lambda cmd: cmd in directions, history))
    replay_list = []
    (agr1, agr2) = split_command_input(command)
    (arg3, arg4) = agr2.split(' ')
    list_len = len(history) - int(arg3)
    history.reverse()
    while list_len < len(history):
        replay_list.append(history[list_len])
        list_len += 1
    replay = [handle_command(robot_name, command) for command in replay_list]
    return True,' > '+robot_name+' replayed '+str(len(replay_list))+' commands in reverse.'

    
def replay_limit_parameters(robot_name,command):
    """
    funtion for replay limit parameters.
    """
    (agr1, agr2) = split_command_input(command)
    (agr3, agr4) = agr2.split('-') 
    global history
    global directions
    list(filter(lambda cmd: cmd in directions, history))
    replay_list = []
    start = len(history) - int(agr3)
    end = len(history) - int(agr4)
    while start < end:
        replay_list.append(history[start])
        start += 1
    replay = [handle_command(robot_name, command) for command in replay_list]
    return replay,' > '+robot_name+' replayed '+str(len(replay_list))+' commands.'


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, 
    or else `False` if robot must shutdown
    """
    (command_name, arg) = split_command_input(command)
    if " " in arg:
        (digit, rev) = arg.split(' ')


    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay' and arg == 'silent':
        (do_next, command_output) = replay_silent(robot_name,command)
    elif command_name == 'replay' and arg == 'reversed':
        (do_next, command_output) = do_replay_reversed(robot_name,command)
    elif command_name == 'replay' and arg == 'reversed silent':
        (do_next, command_output) = do_Replay_reversed_silent(robot_name,command)
    elif command_name == 'replay' and is_int(arg):
        (do_next, command_output) = replay_limit_range(robot_name,command)
    elif command_name == 'replay' and '-' in arg:
        (do_next, command_output) = replay_limit_parameters(robot_name,command)
    elif command_name == 'replay' and arg == '':
        (do_next, command_output) = replay_commands(robot_name,command)
    elif command_name == 'replay' and is_int(digit) and rev == 'reversed':
        (do_next, command_output) = do_replay_limit_reversed(robot_name,command)
    elif command_name == 'replay' and is_int(digit) and rev == 'silent':
        (do_next, command_output) = do_replay_limit_range_silent(robot_name,command)
    
    

    print(command_output)
    show_position(robot_name)
    return do_next


def keep_history(command):
    """
    we taking the user commands and storing them into a list named history. 
    The commands will be replayed when needed.
    """
    global history
    if command.split()[0] != 'replay':
        history.append(command)
    return history

    
def robot_start():
    """This is the entry point for starting my robot"""
    
    global history

    global position_x, position_y, current_direction_index
    
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    keep_history(command)                                                                                                                                                                                           
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        keep_history(command)
    output(robot_name, "Shutting down..")

    history = []

if __name__ == "__main__":
    robot_start()
