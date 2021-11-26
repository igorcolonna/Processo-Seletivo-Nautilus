def prog(init,last,ratio):
    list_AP=[]
    list_GP=[]
    if ratio % 2 == 0:
        for n in range(init,last,ratio):
            list_AP.append(n)
        print(list_AP)

    else:
        for n in range(init,last+1):
            result = init*(ratio**(n-1))
            list_GP.append(result)
        print(list_GP)

if __name__ == '__main__':
    init = int(input("enter the initial value: "))
    last = int(input("enter the final value: "))
    ratio = int(input("enter a ratio(even = AP, odd = GP): "))
    prog(init,last,ratio)