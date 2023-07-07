def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')

    with open('working_with_files/acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def find_acronym():
    look_up = input('What software acronym would you like to look up?\n')

    found = False
    try:
        with open('working_with_files/acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print('-----------')
                    print("Acronym found:")
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return

    if not found:
        print('The acronym does not exist.')

def main():
    choice = input('Do you want to find(f) or add(a) an acronym?\n')
    if choice == 'f':
        find_acronym()
    elif choice == 'a':
        add_acronym()
    else:
        print("Choice is invalid")

main()