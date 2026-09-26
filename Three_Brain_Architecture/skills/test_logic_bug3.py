def is_even_count(items):
    count = 0
    for i in items:
        count += 1
    return len(items) % 2 == 0
