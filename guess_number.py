numbers = [1, 2, 3, 4, 5, 9, 8, 7, 6]
n = 0
while True:
    print("if you want to quit, type \"q\"!")
    number = input("Guess the secret number:")
    if number == "q":
        break
    elif int(number) == numbers[n]:
        print("Your answer is True")
    else:
        print("your answer is wrong, try again!")
    n = (n+1) % 10