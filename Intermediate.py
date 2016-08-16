def main():
    numbers = []

    for x in range(5):
        user_input = int(input("Number:"))
        numbers.append(user_input)

    print("The first number is {} ".format(numbers[0]))
    print("The last number is {}".format(len(numbers)-1))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of number is {}".format(sum(numbers)/len(numbers)))

main()

