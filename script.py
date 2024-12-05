# Description: This script is a simple program that simulates a coffee bot at a cafe. 
def coffee_bot():
  print("Welcome to the Cafe!")
  size = get_size()
  print(size)
  drink_type = get_drink_type()
  print(drink_type)

# Get the size of the drink
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

# Get the type of drink
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return 'Latte'
  else:
    print_message()
    return get_drink_type() 
  
# Print a message for the user
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Call coffee_bot()!
coffee_bot()