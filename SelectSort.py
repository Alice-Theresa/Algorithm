
def selectSort(array):
    for i in range(0, len(array)):
        minIndex = i
        temp = array[i]
        for j in range(i + 1, len(array)):
            if (temp > array[j]):
                minIndex = j
                temp = array[j]
        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]

if __name__ == '__main__':
    array = [5, 4, 6, 3, 2, 1]
    selectSort(array)
    print(array)

