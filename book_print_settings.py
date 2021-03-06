import math


def book_print_settings(nb_pages, nb_blocks=1):
    if nb_pages < 0 or nb_blocks < 0:
        return 'Error'
    if nb_pages == 0 or nb_blocks == 0:
        return []
    res = []
    nb_sheets_remain = math.ceil(nb_pages / 4)  # number of sheets left to process
    nb_pages_remain = nb_pages                  # number of pages  left to process
    if nb_sheets_remain < nb_blocks:
        return 'Error'
    for i in range(0, nb_blocks):
        if i == nb_blocks - 1:
            nb_block_pages = nb_pages_remain  # number of pages in a block
        else:
            nb_block_pages = math.ceil(nb_sheets_remain / (nb_blocks - i)) * 4
        start = nb_pages - nb_pages_remain
        # printing on one side
        if nb_pages_remain == 1:
            res.append((0, start + 1))
            return res
        nb_block_sheets = math.ceil(nb_block_pages / 4)  # number of sheets per block
        for j in range(0, nb_block_sheets):
            nb_block_max_pages = nb_block_sheets * 4     # maximum number of pages in a block
            left = start + nb_block_max_pages - j * 2    # page number to print on the left
            right = start + j * 2 + 1                    # page number to print on the right
            if left > start + nb_block_pages:
                left = 0
            if right > start + nb_block_pages:
                right = 0
            res.append((left, right))
        res.append('@')
        # printing on the other side
        for j in range(0, nb_block_sheets):
            nb_block_max_pages = nb_block_sheets * 4
            left = start + (j + 1) * 2
            right = start + nb_block_max_pages - 1 - j * 2
            if left > start + nb_block_pages:
                left = 0
            if right > start + nb_block_pages:
                right = 0
            res.append((left, right))
        nb_pages_remain -= nb_block_pages
        nb_sheets_remain -= math.ceil(nb_block_pages / 4)
        res.append('#')
    res.pop()
    return res
