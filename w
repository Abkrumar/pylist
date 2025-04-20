confirm_user = []

while True:
    try:
        user_input = (input(
        "input yor user name:\n"
        ))
        confirm_user.append(user_input)
        storarge = confirm_user
        print(storarge)
        print(
        f'{user_input} has been confirm'
        )
    except ValueError:
         print("invalid")
    if user_input== "exit":
        print("Bye!!!")
        break