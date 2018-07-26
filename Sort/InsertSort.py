
def insertSort(array):
    for i in range(1, len(array)):
        j = i
        temp = array[i]
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp

if __name__ == '__main__':
    array = [4, 5, 3, 2, 1]
    insertSort(array)
    print(array)

