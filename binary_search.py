import time


def func_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        answer = func(*args, **kwargs)
        stop = time.time()
        print(
            f"Time for {func.__name__}:{(stop - start)*10000}ms {func.__name__} result:{answer}"
        )

    return wrapper


def repetition_checker(index, num_to_find, num_list):
    """
    Checks for repeated values in a list and returns a list of the indicies of the repeated values.
    returns index of required value if no repeated values exist
    """
    mid_number = num_list[index]
    indicies = [index]

    if mid_number == num_to_find:
        # Checks for repeated-items on the left-side of list
        if (index - 1) >= 0 and num_list[index - 1] == num_to_find:
            indicies.append(index - 1)

        # Checks for repeated-items on the right-side of list
        if (index + 1) < len(num_list) and num_list[index + 1] == num_to_find:
            indicies.append(index + 1)

        # If there are no repeated values it will return the index
        else:
            return index

    return sorted(indicies)


@func_timer
def linear_search(num_list, num_to_find):
    position = None
    for index, number in enumerate(num_list):
        if number == num_to_find:
            position = index
    return position


def binary_search(num_list: list, num_to_find: int):
    num_list = sorted(
        num_list
    )  # method works with only sorted lists. This case we are using an ascending list
    left_index = 0  # basically the index of the first item
    right_index = len(num_list) - 1  # index of last item
    mid_index = 0

    while left_index <= right_index:  # Main loop that locates the required number.
        # This done because in this case since we have an ascending list then the last item has the highest index.
        # If it was a descending one it would be the other way round
        mid_index = (
            left_index + right_index
        ) // 2  # Basically used to find the index of the middle item
        mid_number = num_list[mid_index]

        if mid_number == num_to_find:
            result = repetition_checker(mid_index, num_to_find, num_list)
            return result

        # This just gives us a new left index that will let us work with a shorter range keeping the right_index same(constant)
        if mid_number < num_to_find:
            left_index = mid_index + 1

        # This is litterally almost the same thing as above just that we are changing the right_index and keeping the left_index constant
        else:
            right_index = mid_index - 1

    # This is returned if the required number isn't in the list
    return -1


numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]

# linear_search(numbers_list, 45)
print(binary_search(numbers_list, 21))
