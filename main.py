# 11.17.22 - Python version of double_link_list_pystyle(in C)
import csv

# Declare List
my_list = []

print("\n\t~~~ CREATE A LIST ~~~\n")
list_name = input("Name this list: ")

file = open(f"csv/{list_name}.csv", "a")

# Create List (User Input)
while True:
    quit_choice = False
    skip_append = False
    print("\n\t~~~ CREATE A LIST ~~~\n")
    item = input("Enter item:\n")

    #               ___ QUIT? ___
    if item.lower() == "quit" or item.lower() == 'q':
        while True:
            choice = input(f"\n** Do you want to QUIT? (yes/no) **\n")

            # Add as an item?
            if choice.lower() == "no" or choice.lower() == 'n':
                choice2 = input(f"\nDo you want to add {item} as an item to the list? (yes/no)\n")

                if choice2.lower() == "yes" or choice2.lower() == 'y':
                    break
            elif choice.lower() == "yes" or choice.lower() == 'y':
                quit_choice = True
                break
            else:
                print("\n** 'yes' or 'no' only **")


    #               ___ REMOVE? ___ from CSV??!?!??!?!?!?!
    if item.lower() == "remove" or item.lower() == 'r':
        while True:
            choice = input(f"\n** Do you want to REMOVE the last item? (yes/no) **\n")

            # Add as an item?
            if choice.lower() == "no" or choice.lower() == 'n':
                choice2 = input(f"\nDo you want to add {item} as an item to the list? (yes/no)\n")

                if choice2.lower() == "yes" or choice2.lower() == 'y':
                    break
                elif choice2.lower() == "no" or choice2.lower() == 'n':
                    skip_append = True
                    break
            elif choice.lower() == "yes" or choice.lower() == 'y':
                if len(my_list) > 0:
                    skip_append = True
                    popped = my_list.pop()
                    print(f"\nYou just REMOVED:\n{popped}")
                    # Re-write to file
                    file.close()
                    file = open(f"csv/{list_name}.csv", "w")
                    for i in my_list:
                        file.write(f"{i}\n")
                    break
                else:
                    print("\n*** NOTHING TO REMOVE. LIST IS EMPTY ***")
                    skip_append = True
                    break
            else:
                print("\n** 'yes' or 'no' only **")

    # Quit
    if quit_choice == True:
        file.close()
        break



    if skip_append != True:
        my_list.append(item)
        file.write(f"{item}\n")

    # Print
    print("\n")
    print(my_list)

# Goodbye
print("\n\n\t~~ Goodbye! ~~\n\n")
