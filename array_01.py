
def snail(array):
    result = []
    while array:

        for i in range(len(array[0])):
            result.append(array[0][i])
        array.pop(0)

        for i in range(len(array)):
            result.append(array[i][-1])
            array[i].pop()

        if array:
            result += array[-1][::-1]
            array.pop(-1)

        for i in range(len(array) - 1, -1, -1):
            result.append(array[i][0])
            array[i].pop(0)

    return result

if __name__ == '__main__':
    array = [[1, 2, 3, 4],
             [12,13,14,5],
             [11,16,15,6],
             [10,9 ,8 ,7]]
    
    print(snail(array))
