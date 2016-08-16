import random

def main():
    user_input = int(input("How many quick picks?"))

    info = ""

    for x in range(user_input):
        numbers = [0, 0, 0, 0, 0, 0]

        for y in range(6):
            random_number = random.randint(1, 45)

            while random_number in numbers:
                random_number = random.randint(1, 45)

            numbers[y] = random_number

        numbers.sort()
        info += "{} {} {} {} {} {}\n".format(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5])

    print(info)

main()

