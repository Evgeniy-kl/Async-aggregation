def get_label(row: int):
    with open('labels.txt', 'r') as file:
        for i, line in enumerate(file):
            if i == row:
                return line
