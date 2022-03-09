import math


def book_print_settings(nb_pages):
    if nb_pages < 0:
        return 'Error'
    if nb_pages == 0:
        return []
    if nb_pages == 1:
        return [(0,  1)]
    res = []
    nb_sheets = math.ceil(nb_pages / 4)
    # printing on one side
    for i in range(0, nb_sheets):
        left = nb_sheets * 4 - i * 2
        right = i * 2 + 1
        if left > nb_pages:
            left = 0
        if right > nb_pages:
            right = 0
        res.append((left, right))
    res.append('@')
    # printing on the other side
    for i in range(0, nb_sheets):
        left = (i + 1) * 2
        right = nb_sheets * 4 - 1 - i * 2
        if left > nb_pages:
            left = 0
        if right > nb_pages:
            right = 0
        res.append((left, right))
    return res


if __name__ == '__main__':
    print(book_print_settings(1))

