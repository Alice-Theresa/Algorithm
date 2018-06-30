

def selectSort(array):
    for i in range(0, len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if (array[i] > array[j]):
                minIndex = j
        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]

if __name__ == '__main__':
    array = [5, 4, 3, 2, 1]
    selectSort(array)
    print(array)

