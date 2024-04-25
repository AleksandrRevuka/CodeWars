def triangle(row: str) -> str:
    key = {"GG": "G", "RR": "R", "BB": "B",
           "BG": "R", "GB": "R",
           "RB": "G", "BR": "G",
           "RG": "B", "GR": "B"
           }
    row = list(row)
    for i in range(len(row) - 1, 0, -1):
        for k in range(i):
            row.append(key[row[k] + row[k + 1]])
        del row[:i+1]

    return row[0]


if __name__ == '__main__':
    print(triangle('RGBG'))