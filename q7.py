def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    freq = {}
    for f in fruit_list:
        freq[f] = freq.get(f, 0) + 1
    return freq
