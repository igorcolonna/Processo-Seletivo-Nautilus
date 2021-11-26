def ExpSeries(series):
    list_series = []
    list_series_temp = []
    for exp in range(series + 1):
        result = exp**exp
        list_series.append(result)

    list_series_temp = list_series[-10:]
    for item in range(len(list_series_temp)):
        print("|{:.2e}|".format(list_series_temp[item]))

if __name__ == '__main__':
    series = int(input("enter a series size: "))
    ExpSeries(series)