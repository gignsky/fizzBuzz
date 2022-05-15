# gig 5.15 fizzbuzz 1-NUMBER_OF_ITERATIONS Value

# config
def config():
    NUMBER_OF_ITERATIONS = 1000000000
    return NUMBER_OF_ITERATIONS


def main():
    t = config() + 1
    i = 1
    while i != t:
        mod = check(i)
        print(i, ": ", mod)
        i = i + 1


def check(i):
    fizz = checkFizz(i)
    buzz = checkBuzz(i)

    if fizz == bool(1):
        if buzz == bool(1):
            return "FizzBuzz"
        else:
            return "Fizz"
    elif buzz == bool(i):
        return "Buzz"
    else:
        return i


def checkFizz(i):
    check = i % 3
    var = checker(check)
    return var


def checkBuzz(i):
    check = i % 5
    var = checker(check)
    return var


def checker(check):
    if check == 0:
        return bool(1)
    else:
        return bool(0)


main()
