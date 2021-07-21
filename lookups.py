def find_index_or_nearest(iterable, item):
    """ Return the index of an item or indexes of the nearest values if the not found. """
    beg = 0
    end = len(iterable) - 1
    while beg <= end:
        mid = beg + (end - beg) // 2
        if iterable[mid] == item:
            return mid
        elif iterable[mid] < item:
            beg = mid + 1
        else:
            end = mid - 1
    else:
        return [end, beg]


def check_if_exact_result(result, iterable, iterable_key, message):
    """ Check if the result of other function is a single value of exact result index
    or two values of the nearest ones.  """
    choice = ''
    choice_msg = ''
    if type(result) == list:
        if result[0] == -1:
            first = 0
            print(
                f'{message} Therefore, your request will processed with the nearest found result: '
                f'{iterable[first][iterable_key]}.')
            return iterable[first]
        elif result[1] == len(iterable):
            last = len(iterable) - 1
            print(
                f'{message} Therefore, your request will processed with the nearest found result: '
                f'{iterable[last][iterable_key]}.')
            return iterable[last]
        else:
            before = iterable[result[0]]
            after = iterable[result[1]]
            print(f'{message} The nearest found results are: {before[iterable_key]} and {after[iterable_key]}?')
            choice_msg = f'Type 1 to choose {before[iterable_key]} or 2 to choose {after[iterable_key]}. '
            choice = input(choice_msg)
    if choice:
        while choice not in ('1', '2'):
            choice = input(choice_msg)
        if choice == '1':
            return iterable[result[0]]
        else:
            return iterable[result[1]]
    else:
        return iterable[result]
