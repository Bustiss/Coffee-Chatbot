# Description: This script is a simple program that simulates a coffee bot at a cafe. 
def coffee_bot():
  print("Welcome to the Cafe!")
  size = get_size()
  temp = hot_or_iced()
  drink_type = get_drink_type()
  cup = choose_cup()
  print(f"Alright, that's a {size} {temp} {drink_type} in a {cup}")
  name = input('Can I get your name please? ')
  print(f"Thanks, {name}! Your drink will be ready shortly.")

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
    return order_latte()
  else:
    print_message()
    return get_drink_type()

# If the user selects a latte, ask for the type of milk
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')

  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte() 

# Ask the user if they want a plastic cup or a reuseable cup
def choose_cup():
  res = input('Would you like plastic cup or your own reuseablecup? \n[a] Plastic cup \n[b] reuseable cup \n>')

  if res == 'a':
    return 'plastic cup'
  elif res == 'b':
    return 'reuseable cup'
  else:
    print_message()
    return choose_cup()

# Ask the user if they want their drink hot or iced
def hot_or_iced():
  res = input('Would you like your drink hot or iced? \n[a] Hot \n[b] Iced \n>')

  if res == 'a':
    return 'hot'
  elif res == 'b':
    return 'iced'
  else:
    print_message()
    return hot_or_iced()

# Print a message if the user enters an invalid response
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Call coffee_bot()
coffee_bot()