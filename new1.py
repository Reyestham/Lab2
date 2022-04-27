
import statistics

def main():
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    print(avg)
    max = find_min_max(num_list)
    print(max)
    sort = sort_temperature(num_list)
    print(sort)
    med = calc_median_temperature(num_list)
    print(med)

def display_main_menu():
    print("display main menu")
    print("69,13,313")

def get_user_input():
    print("get_user_input")
    x1 = float(input("Please enter temp 1: "))
    x2 = float(input("Please enter temp 2: "))
    x3 = float(input("Please enter temp 3: "))
    x4 = float(input("Please enter temp 4: "))
    tot = [x1,x2,x3,x4]
    return tot


def calc_average(x):
    print("calculate average")
    avg = (x[0]+x[1]+x[2]+x[3])/4
    return avg


def find_min_max(x):
    print("find_min_max")
    max = x[0]
    for i in range(0,4):
        if x[i]>max:
            max = x[i]
    return max


def sort_temperature(x):
    print("sort_temperature")
    x.sort()
    return x

def calc_median_temperature(x):
    print("calc_median_temperature")
    med = statistics.median(x)
    return med

if __name__ == '__main__':
    main()





