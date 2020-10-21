# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.w3schools.com/python/gloss_python_dictionary_add_item.asp

dictionary = {}
while True:
    a = input('What is your name?')
    b = input('What is your dream job?')
    dictionary[str(a)] = str(b)
    c = input ("Please pass it on to the next person and enter c to continue and s to stop.")
    if c == 'c':
        print('lets get started')
    elif c == 's':
        break

for key, value in dictionary.items():
    print(key + " wants to be a " + value)