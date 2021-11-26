def Cents(target):
    cents = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0]*target

    for x in cents:
        for i in range(x, target+1):
            ways[i] += ways[i-x]

    print("There are {} possible ways".format(ways[target]))

if __name__ == '__main__':
    target = int(input("Enter a target value: "))
    Cents(target)