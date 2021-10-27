def favourite_book(read):
    """display a simple greetings """
    print(f"My favourite book is {read.title()}")

favourite_book('the millioniare mind')


def describe_pet(animal_type , pet_name ):
    """ Display info. about your pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet('hamster','vrk')
describe_pet('dog','tyson')

def describe_pet(animal_type , pet_name ):
    """ Display info. about your pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(animal_type='hamster',pet_name='vrk')
describe_pet(pet_name='vrk',animal_type='hamster')

def get_formatted_name(first_name, last_name):
   """Return a full name, neatly formatted."""
   full_name = f"{first_name} {last_name}"
   return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name(first_name,middle_name,last_name):
   """Return a full name, neatly formatted."""
   full_name = f"{first_name} {middle_name} {last_name}"
   return full_name.title()
musician = get_formatted_name('jimi','lee', 'hendrix')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
   """Return a full name, neatly formatted."""
   if middle_name:
     full_name = f"{first_name} {middle_name} {last_name}"
   else:
       full_name = f"{first_name} {last_name}"
   return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name, age=None):
    """ Return a dictionary of information about a person """
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] =age
    return person
musician = build_person('vrk','kautlya',age=21)
print(musician)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'quit' anytime to quit )")

    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    if l_name == "quit":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def greet_user(names):
    """ print a simple msg to all the user in the list """
    for name in names:
        msg = (f"Hello,{name.title()} !")
        print(msg)

usernames = ['vikram','guddu','surendra jha','gunjana jha']
greet_user(usernames)


unprinted_designs = ['phonecase','cover','robot pendant','charger pot']
completed_models =[]

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"printing model : {current_design}")
    completed_models.append(current_design)

print("\nThe folowing model have been printed ! ")
for completed_model in completed_models :
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
# """Build a dictionary containing everything we know about a user."""
 user_info['first_name'] = first
 user_info['last_name'] = last
 return user_info
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)


















