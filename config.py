import sys
import cell_sim as cel
import numpy as np

''' Declaring values for non user determined variables'''
age_limit = 10
division_limit = 7
division_prob = 0.6
division_cd = 1

'''Declaring variables we use as default to later adjust from user inputs '''
default_time_limit = 1000
current_time_limit = default_time_limit

default_chosen_grid = "grid_1.txt"
current_chosen_grid = default_chosen_grid

default_initial_population = 2
current_initial_population = default_initial_population



def start_menu():
    ''' Prints a menu for the user'''
    print("")
    print('*******MAIN MENU - CELLULAR AUTOMATA 2.0******')
    print('''Please select one of the following options:  
    [1] Display configuration
    [2] Setup
    [3] Reset settings
    [4] Run simulation
    [5] Exit program''')

def option_one(): 
    ''' Displays the current configurations of the simulation - for all variables'''
    print("")
    print('Displaying configuration...')
    print("")
    print ('Chosen grid option:\t', current_chosen_grid)  
    print('Initial population:\t', current_initial_population)
    print ('Age limit:\t\t', age_limit)
    print ('Division limit:\t\t', division_limit)
    print('Division probability:\t', division_prob)
    print ('Division cooldown:\t', division_cd)
    print ('Time limit\t\t', current_time_limit)
    print("")


def option_reset_to_default():
    ''' Resets the user determined variables to their default value '''
    global current_initial_population
    current_initial_population = default_initial_population
    global current_chosen_grid
    current_chosen_grid = default_chosen_grid
    global current_time_limit
    current_time_limit = default_time_limit

def option_setup_pop_time():
    '''Lets the user determine the initial population and time limit (in ticks)'''
    while True: 
        value_ip = input('Insert the initial population size from 1 to 5: ')
        try:
            my_value_pop_size = int(value_ip)
            if my_value_pop_size >= 1 and my_value_pop_size <= 5:
                global current_initial_population 
                current_initial_population = my_value_pop_size
                break
            
            else:
                print ('The initial population size must an integer from 1 to 5, try again! ')

        except ValueError:
            print ('The initial population size must an integer from 1 to 5, try again! ')
   
    while True:
        value_tl = input('Insert time limit from 10 to 1000: ')
        try:
            my_value_tl = int(value_tl)
            if my_value_tl >= 10 and my_value_tl <= 1000:
                global current_time_limit
                current_time_limit = my_value_tl
                break
            else:
                print('The time limit must be an integer from 10 to 1000, try again!')
                
        except ValueError:
            print('The time limit must be an integer from 10 to 1000, try again!')
    

def option_choose_grid():
    global current_chosen_grid
    while True:
        print("Please choose a grid option:")
        print("[1] grid_1.txt")
        print("[2] grid_2.txt")
        print("[3] grid_3.txt")
        # Add more options here if necessary
        selection = input('Enter your selection: ')
        try:
            ans = int(selection)
            if ans == 1:
                current_chosen_grid = "grid_1.txt"
            elif ans == 2:
                current_chosen_grid = "grid_2.txt"
            elif ans == 3:
                current_chosen_grid = "grid_3.txt"
            # Add more options here if necessary
            grid = np.genfromtxt(current_chosen_grid, dtype='str')
            row = len(grid)
            col = len(grid[0])
            if row < 3 or col < 3:
                with open("grid_err.txt", "r") as f:
                    grid_err_msg = f.read()
                print(grid_err_msg)
            else:
                break
        except ValueError:
            print('Invalid input, please enter a valid option.')


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
                option_choose_grid()
                start_of_program()
                break

            elif ans == 3:
                option_reset_to_default()
                print('Values have been reset to default')
                start_of_program()
                break           
            
            elif ans == 4:
                cel.main()
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
