# - Get largest number less than 3
# - this is the first digit and remove from list
# - if first digit == 2, find next largest number less than 4
# - otherwise largest number
# - remove and set as second digit
# - next largest number less than 6
# - remove and set as third digit
# - last number is fourth digit
# - format appropriately for output


def get_largest_number_less_than_n(n: int, nums: list[int]) -> int:
    check_list = []
    for num in nums:
        if num < n:
            check_list.append(num)
    if len(check_list) == 0:
        return None
    largest_num = max(check_list)
    nums.remove(largest_num)
    return largest_num


def format_output(ordered_list: list[int]) -> str:
    if len(ordered_list) != 4:
        raise ValueError("input list must be 4 digits")
    return f"{ordered_list[0]}{ordered_list[1]}:{ordered_list[2]}{ordered_list[3]}"


def get_first_two_digits(nums: list[int], twos_allowed=True) -> tuple[str]:
    if twos_allowed:
        first_digit = get_largest_number_less_than_n(3, nums)
    else:
        first_digit = get_largest_number_less_than_n(2, nums)

    if first_digit == 2:
        second_digit = get_largest_number_less_than_n(4, nums)
    else:
        second_digit = get_largest_number_less_than_n(10, nums)

    return (first_digit, second_digit)


if __name__ == "__main__":

    test_list = [9, 2, 2, 5]
    temp_list = [n for n in test_list]
    first_digit, second_digit = get_first_two_digits(temp_list)
    third_digit = get_largest_number_less_than_n(6, temp_list)
    if third_digit is None:
        temp_list = test_list
        first_digit, second_digit = get_first_two_digits(
            temp_list, twos_allowed=False)
        third_digit = get_largest_number_less_than_n(6, temp_list)
    fourth_digit = temp_list[0]
    print(format_output(
        [first_digit, second_digit, third_digit, fourth_digit]))
