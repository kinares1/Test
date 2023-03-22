def get_lengths_list(strings):
    """Возвращает список длин каждой строки из переданного списка."""
    lengths = []
    for string in strings:
        lengths.append(len(string))
    return lengths

print(get_lengths_list(['Tina', 'Raj', 'Tom']))

