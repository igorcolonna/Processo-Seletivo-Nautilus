def converterDec_Bin(number):
    binary = 0
    list_bin = []
    while(True):
        binary = number%2
        number = number//2
        list_bin.append(binary)
        if number == 0:
            break
    list_bin.reverse()
    for item in range(len(list_bin)):
        print(list_bin[item], end='')
    print("\n")

if __name__ == '__main__':
    number = int(input("enter a number to convert to binary: "))
    converterDec_Bin(number)