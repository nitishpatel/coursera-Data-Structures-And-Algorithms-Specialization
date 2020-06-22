# python3
def max_pairwise_product(numbers):
    sorted_numbers=sorted(numbers)
    return sorted_numbers[-1]*sorted_numbers[len(sorted_numbers)-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
