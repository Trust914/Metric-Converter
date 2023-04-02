from os import system, name
from art import logo


def clear():
    """
    This function clears texts in the terminal
    :return:
    """
    if name == "nt":
        # for windows
        _ = system('cls')
    else:
        # for mac and Linux
        _ = system('clear')


clear()
exit_ = "Good bye"


def inputs_tab():
    """
    Gets the number and unit to be converted from the user and transfer it to the next function
    :return: user requested number to convert and unit to be converted
    """
    repeate = True
    user_num = None
    user_unit = None
    while repeate:
        user_num = float(input("Type in the number to convert:\n"))
        user_unit = int(input(
            "What unit is the number in? Press:\n1 for mm\n2 for cm\n3 for m\n4 for km\n5 to go back\n6 to end\n"))

        if user_unit in range(0, 5):
            repeate = False
        elif user_unit == 5:
            repeate = True
            clear()
            print(logo)
        elif user_unit == 6:
            print(exit_)
            exit()
        elif user_unit not in range(0, 5):
            clear()
            print(logo)
            print("Invalid entry")
            exit()

    return user_num, user_unit


# This next function
def units_tab(num, unit):
    """
     This function takes in the number and unit returned by the first function and performs the necessary calculations
     Then it gets the necessary tab details and returns the conversion tab and results dictionary
    :param num: user requested number to convert
    :param unit: user requested unit to convert from
    :return: type_conversion -> the requested unit to convert to
             unit_dict -> the dictionary for the unit conversion calculation
             num -> the requested number to be converted
    """
    unit -= 1  # to be used in the conversion list, hence for indexing, we reduce the value by 1...
    # dictionary storing all the units and available conversions
    converter_list = [{'mm': [{'mm to cm': (num / 10)}, {'mm to m': (num / 1e3)}, {'mm to km': (num / 1e6)}]},
                      {'cm': [{'cm to mm': (num * 10)}, {'cm to m': (num / 1e2)}, {'cm to km': (num / 1e5)}]},
                      {'m': [{'m to mm': (num * 1e3)}, {'m to cm': (num * 1e2)}, {'m to km': (num / 1e3)}]},
                      {'km': [{'km to mm': (num * 1e6)}, {'km to cm': (num * 1e5)}, {'km to m': (num * 1e3)}]},
                      ]
    clear()  # clear the terminal
    print(logo)
    unit_dict = converter_list[unit]  # the dictionary containing the calculation for the requested conversion

    # Now we want to show the options and available units that the requested unit can be converted to in the terminal
    for keys in unit_dict:
        len_conv_list = len(unit_dict[keys])
        print(f"What unit do you want to convert {num}{keys} to?Press: ")
        for index in range(len_conv_list):
            for the_keys in unit_dict[keys][index]:
                print(f"{index + 1} for {the_keys}")
        print(f"4 Previous menu\n5 Main menu\n6 Exit")
        type_conversion = int(input())  # get the user conversion request,e.g., cm to mm
        return type_conversion, unit_dict, num


def result_tab(convert_to, calc_dict, numbr):
    """
    This function evaluates the requested unit conversion and performs the calculation e.g., if the user selects cm
    to mm, we pick out the corresponding calculation from the unit_dict and evaluate the calculation
    :param convert_to: the requested option tab
    :param calc_dict: unit_dict
    :param numbr: number to be converted
    :return: final result or tab
    """
    convert_to -= 1
    for keys in calc_dict:
        if convert_to in range(len(calc_dict[keys])):  # a valid,available conversion tab is selected,e.g., cm to mm
            for j in calc_dict[keys][convert_to]:
                result_unit_list = list(j)  # to get the resulting,converted unit
                if result_unit_list[-2] == ' ':
                    result_unit = ''.join(result_unit_list[-1])
                else:
                    result_unit = ''.join(result_unit_list[-2:])
                result = f"{numbr}{keys} is equal to {calc_dict[keys][convert_to][j]}{result_unit}"
                return result
        elif convert_to == 5:
            print(exit_)
            exit()
        else:
            return convert_to


def conversion_tabs_handler(tabs, value):
    """
    this next function gets the conversion tab and results dictionary from the previous function, and handles the movement
    from the conversion tab to the unit tab and to the main menu.py
    :param tabs: selected option
    :param value:
    :return:
    """
    # units_tab_output = []
    # val_unit = []
    while tabs in range(3, 5):
        while tabs == 3:
            clear()
            print(logo)
            user_unit = int(input(
                "What unit is the number in?Press:\n1 for mm\n2 for cm\n3 for m\n4 for km\n5 to go back\n6 to end\n"))
            if user_unit == 5:
                tabs = 4
            elif user_unit < 5:
                units_tab_output = []
                units_tab_output += units_tab(value, user_unit)
                tabs = result_tab(units_tab_output[0], units_tab_output[1], units_tab_output[2])
            elif user_unit == 5:
                print(exit_)
                exit()
        while tabs == 4:
            units_tab_output = []
            val_unit = []
            clear()
            print(logo)
            val_unit += inputs_tab()
            units_tab_output += units_tab(val_unit[0], val_unit[1])
            tabs = result_tab(units_tab_output[0], units_tab_output[1], units_tab_output[2])
            if tabs == 3:
                value = units_tab_output[2]
    return tabs


def functions():
    """
    This is the main function that incorporates all the other functions and performs the repetitive task
    :return:
    """
    print(logo)

    # Stage 1: get user inputs(the number and the unit) and store them in the list
    user_num, user_unit = inputs_tab()
    # Stage 2: determine the unit selected,unit to be converted to and perform the necessary calculation.
    type_conversion, unit_dict, num = units_tab(user_num, user_unit) # this is the output of the unit_tab which
    # returns the tab(whether the user wants to go back to the previous menu.py or to main menu.py) and the results
    # dictionary

    # Stage 3: from the returned values of the unit_tab function,get the corresponding result or the tab value res_
    res_ = result_tab(type_conversion, unit_dict, num)
    # Stage 4: depending on the type conversion selected, print the result of the conversion, go to the previous
    # menu.py or go to the main menu.py
    print(conversion_tabs_handler(res_, num))

    # Stage 5: determine if the user wants to perform another conversion or not if yes,repeat from stage one, else,
    # end the application
    go_again = input("Do you want to perform another conversion? Type 'y' to go again,otherwise,type 'n':\n").lower()
    if go_again == "n":
        print(exit_)
        exit()
    elif go_again == "y":
        clear()
        functions()  # recursive function executes if user wants to perform another conversion


functions()
