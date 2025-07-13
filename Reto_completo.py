import time

#Here, we get the user information
name = input("Please, type your name: ")
try:
    age = int(input("Please, type your age: "))
except ValueError:
    print("We're really sorry, only type numbers in your age. Please, try again.")
    exit()

#Here, we use the conditionals and bucles
if age < 12:
    print("We're really sorry, only can enter people older to 12 years.")
elif 12 <= age <= 17:
    passs = input(f"Welcome: {name}. Do you have a pass? (Yes/No)").strip().lower()
    if passs in ["si", "yes", "sí"]:
        for num1 in range(1, 6):
            print(f"You can enter to young zone {num1}")
            time.sleep(1.0)
    else:
        print(f"We're really sorry, you can't enter because you need a pass to enter.")
    # python Reto_completo.py
elif age >= 18:
    table = input(f"{name}, Do you wish see the multiplicate table? (Yes/No)").strip().lower()
    if table in ["si", "yes", "sí"]:
        try:
            user_num = int(input("Please, type a random number: "))
        except ValueError:
            print("Please, only type numbers. try again.")
            exit()
        for user_num2 in range(1, 11):
            print(f"\nThe results of: {user_num} X {user_num2} = {user_num * user_num2}")
            time.sleep(0.8)
    else:
        print(f"Thanks a lot for your visit {name}.")