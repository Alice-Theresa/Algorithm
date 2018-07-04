
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

if __name__ == '__main__':
    array = [5, 4, 3, 2, 1]
    bubbleSort(array)
    print(array)