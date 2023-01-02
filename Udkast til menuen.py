import sys

''' Declaring values for non user determined variables'''
age_limit = 10
division_limit = 2
division_prob = 0.6
division_cd = 2

'''Declaring variables we use as default to later adjust from user inputs '''
default_row = 3
current_row = default_row

default_time_limit = 1000
current_time_limit = default_time_limit

default_col = 3
current_col = default_col

default_initial_population = 2
current_initial_population = default_initial_population

def start_menu():
    ''' Prints a menu for the user'''
    print('*******MAIN MENU - CELLULAR AUTOMATA 2.0******')
    print('''Please select one of the following options:  
    [1] Display configuration
    [2] Setup
    [3] Reset settings
    [4] Run simulation
    [5] Exit program''')

def option_one(): 
    ''' Displays the current configurations of the simulation - for all variables'''
    print('Displaying configuration...')
    print ('Row size:\t\t', current_row)
    print('Column size\t\t', current_col) 
    print('Initial population:\t', current_initial_population)
    print ('Age limit:\t\t', age_limit)
    print ('Division limit:\t\t', division_limit)
    print('Division probability:\t', division_prob)
    print ('Division cooldown:\t', division_cd)
    print ('Time limit\t\t', current_time_limit)


def option_reset_to_default():
    ''' Resets the user determined variables to their default value '''
    global current_row
    current_row = default_row
    global current_col
    current_col = default_col
    global current_initial_population
    current_initial_population = default_initial_population
    global current_time_limit
    current_time_limit = default_time_limit

def option_setup_pop_time():
    '''Lets the user determine the initial population and time limit (in ticks)'''
    while True: 
        value_ip = input('Insert the initial population size: ')
        try:
            my_value_pop_size = int(value_ip)
            if my_value_pop_size >= 1 and my_value_pop_size <= current_row * current_col:
                global current_initial_population 
                current_initial_population = my_value_pop_size
                break
            
            else:
                print ('The initial population size must be larger than 0, try again! ')

        except ValueError:
            print ('The initial population size must be an integer larger than 0, try again!')
   
    while True:
        value_tl = input('Insert time limit: ')
        try:
            my_value_tl = int(value_tl)
            if my_value_tl >= 1:
                global current_time_limit
                current_time_limit = my_value_tl
                break
        except ValueError:
            print('The time limit must be an integer larger than 0, try again!')
    

def option_set_grid():
    ''' Takes the user's input for rows and columns in order to make the grid '''
    while True:   
        value_row = input('Insert row size: ')
        try:
            my_value_row = int(value_row)
            if my_value_row >= 3:
                global current_row
                current_row = my_value_row
                break
            else:
                print('Row size must be 3 or greater, try again!')
        except ValueError:
            print('Row size must be an integer greater than 3, try again!')
      

    while True:
        value_col = input('Insert column size: ')
        try:
            my_value_col = int(value_col)
            if my_value_col >= 3:
                global current_col
                current_col = my_value_col
                break
            else: 
                print('Column size must be 3 or greater, try again!')
        except ValueError:
            print('Column must be an greater than 3, try again')


def start_of_program():
    ''' Prints the start menu and takes in the user's input to call the desired function '''
    start_menu()
    while True:
        ans_input = input('Please enter your input: ')
        try:
            ans = int(ans_input)
            if ans == 1:
                option_one()
                start_of_program()
                break
            
            elif ans == 2:
                option_setup_pop_time()
                option_set_grid()
                start_of_program()
                break

            elif ans == 3:
                option_reset_to_default()
                print('Values have been reset to default')
                start_of_program()
                break           
            
            elif ans == 4:
                cel.main() #OBS! samme navn?
                break
            
            elif ans == 5:
                print('Exiting program...')
                print ('Thank you for using Cellular Automata 2.0!')
                sys.exit()
                break
            else:
                print('Please enter a valid option!')
                
        except ValueError:
            print('Please enter a valid option!')
        
start_of_program()