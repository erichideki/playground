from math import inf

def find_max(number_list):
    max_number = -inf
    for number in number_list:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    print(find_max([1]))
    print(find_max([1, 100]))