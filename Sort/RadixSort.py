
def radixSort(array):
    radix = 10
    length = len(array)
    aux = [0] * radix
    maxDigitCount = max(list(map(lambda x: len(str(x)), array)))
    for r in range(maxDigitCount):
        count = [0] * (radix + 1)
        for i in range(length):
            count[digitAt(array[i], r) + 1] += 1
        for i in range(radix):
            count[i + 1] += count[i]
        for i in range(length):
            aux[count[digitAt(array[i], r)]] = array[i]
            count[digitAt(array[i], r)] += 1
        for i in range(length):
            array[i] = aux[i]

def digitAt(value, index):
    return int(value / pow(10, index) % 10)

if __name__ == '__main__':
    array = [14, 5, 3, 12, 1]
    radixSort(array)
    print(array)