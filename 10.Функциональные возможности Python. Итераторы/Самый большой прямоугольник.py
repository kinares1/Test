def largest_histogram(histogram):
    """Используем стек чтобы хранить индексы столбцов гистограммы в порядке возрастания высоты."""
    stack = []
    max_area = 0
    i = 0
    while i < len(histogram):
        if not stack or histogram[i] >= histogram[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = histogram[top] * (i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        area = histogram[top] * (i - stack[-1] - 1 if stack else i)
        max_area = max(max_area, area)
    return max_area

print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))