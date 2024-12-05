# Define your functions
def coffee_bot():
  print("Welcome to the Cafe!")

# Ask user to input preferred cup size
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
    return get_size() # if the user enters an invalid response, run the function again
  
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Call coffee_bot()!
coffee_bot()
get_size()