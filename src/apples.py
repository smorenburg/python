def eat_apples(num_of_apples, on_diet=False):
    """
    """
    apples_remaining = num_of_apples

    while apples_remaining > 0 and not on_diet:
        apples_remaining -= 1
        print('Thank you!')

    print('Done')

    return
