
import random
print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')

print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
# the user picks a number between 1 to 3 and it stores in the variable user_input
user_input = input('Pick a number: ')
# a random number generates between 1 and 3 and its stores in the variable cpu_input
cpu_input = random.randint(1,5)
# a control statement to determine who one and which options where pick
if user_input == '1':
    print('You chose: ✊')
    if cpu_input == '1':
        print('CPU chose: ✊')
        print('Its a tie!')
    elif cpu_input == '2':
        print('CPU chose: ✋')
        print('The CPU won!')
    elif cpu_input == '3':
        print('CPU chose: ✌️')
        print('The player won!')
    elif cpu_input == '4':
        print('CPU chose: 🦎')
        print('The player won!')
    else: 
        print('CPU chose: 🖖')
        print('The CPU won!')
elif user_input == '2':
    print('You chose: ✋')
    if cpu_input == '1':
        print('CPU chose: ✊')
        print('The player won!')
    elif cpu_input == '2':
        print('CPU chose: ✋')
        print('Its a tie!')
    elif cpu_input == '3':
         print('CPU chose: ✌️')
         print('The CPU won!')
    elif cpu_input == '4':
        print('CPU chose: 🦎')
        print('The CPU won!')
    else: 
        print('CPU chose: 🖖')
        print('The player won!')
elif user_input == '3':
    print('You chose: ✌️')
    if cpu_input == '1':
        print('CPU chose: ✊')
        print('The CPU won!')
    elif cpu_input == '2':
        print('CPU chose: ✋')
        print('The player won!')
    elif cpu_input == '3': 
        print('CPU chose: ✌️')
        print('Its a tie!')
    elif cpu_input == '4':
        print('CPU chose: 🦎')
        print('The player won!')
    else: 
        print('CPU chose: 🖖')
        print('The CPU won!')
elif user_input == '4':
    print('You chose: 🦎')
    if cpu_input == '1':
        print('CPU chose: ✊')
        print('The cpu won!')
    elif cpu_input == '2':
        print('CPU chose: ✋')
        print('The player won!')
    elif cpu_input == '3': 
        print('CPU chose: ✌️')
        print('The cpu won!')
    elif cpu_input == '4':
        print('CPU chose: 🦎')
        print('Its a tie!')
    else: 
        print('CPU chose: 🖖')
        print('The player won!')
else:
    print('You chose: 🖖')
    if cpu_input == '1':
        print('CPU chose: ✊')
        print('The player won!')
        
    elif cpu_input == '2':
        print('CPU chose: ✋')
        print('The cpu won!')
        
    elif cpu_input == '3': 
        print('CPU chose: ✌️')
        print('The player won!')
        
    elif cpu_input == '4':
        print('CPU chose: 🦎')
        print('The cpu won!')
        
    else: 
        print('CPU chose: 🖖')
        print('Its a tie!')
        