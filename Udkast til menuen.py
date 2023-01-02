                  
import sys
import time
from collections import namedtuple
from msilib.schema import SelfReg

def start_menu():
    ''' Prints a menu for the user'''
    print('*******MAIN MENU - CELLULAR AUTOMATA 2.0******')
    print('''Please select one of the following options:  
    [1] Display configuration
    [2] Setup
    [3] Reset settings
    [4] Run simulation
    [5] Exit program''')

def option_one():  #skal der eventuelt indsættes mere her med de nye ændringer i programmet
    ''' Displays the current configurations of the simulation - with the values the user can choose'''
    print('Displaying configuration...')
    print ('Row size:\t\t', current_row)
    print('Column size\t\t', current_col) 
    print('Initial population:\t', current_initial_population)
    print ('Age limit:\t\t', current_age_limit)
    print ('Division limit:\t\t', current_division_limit)
    print('Division probability:\t', current_division_prob)
    print ('Division cooldown:\t', current_division_cd)
    print ('Time limit\t\t', current_time_limit)
#Fjernet punktet, hvor man kunne se om visualiseringen er slået til eller fra 

def option_reset_to_default():
    ''' Resets the current variables to the default variables - limited to the values the user can determine in phase 2 '''
    global current_initial_population
    current_initial_population = default_initial_population
    global current_time_limit
    current_time_limit = default_time_limit
    

def user_setup():
    '''Lets the user determine the initial population and time limit (in ticks)'''
    while True: 
        value_ip = input('Insert the initial population size: ')
        global current_row
        global current_col
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
                print('Initiating  setup, please stand by...')
                user_setup()
                print('Returning to the main menu...')
                start_of_program()
                break

            elif ans == 3:
                print('Resetting setup to default...')
                option_reset_to_default()
                start_of_program()
                break           
            
            elif ans == 4:
                cel.main() #Får måske et nyt navn? 
                break
            
            elif ans == 5:
                print('Exiting program...')
                print ('Thank you for using Cellular Automata 2.0!')
                sys.exit()
                break
            
            else:
                print('Please enter a valid option')
                
        except ValueError:
            print('Please enter a valid option')
        
start_of_program()
