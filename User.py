while  True:
    input_values = input("""input your name:\n"""
                         "Exit:")

    if input_values == "quit":
        break

    dictionary = {
    "First_name": "Aminu",
    "Sure_name": "Umar",
    "Age": "12"}

    result_check = (
    f'your sure name is {
        dictionary["Sure_name"]
    } and your age is 12')

    result_check_2 = (
    f'your first name is {
        dictionary["First_name"]
    }and your age is 12')

    if input_values == dictionary['First_name']:
        print(result_check)
    elif input_values == dictionary["Sure_name"]:
        print(result_check_2)
    else:
        print("there is no this data in our  saver")
    dictionary["favourite meal"] = 'tuwo'
# del dictionary['Age']
# print(dictionary)
    favourite_meal = input("what is your favourite meal?\n")
    if favourite_meal == dictionary["favourite meal"]:
        print('You have a delecious food preference')
    else:
        print(' you are an inposter')
    