
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        print(elements)
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    print(elements)
    print(elements)
    # return end


if __name__ == '__main__':
    # elements = [11,9,29,7,2,15,28]
    # # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    # quick_sort(elements, 0, len(elements)-1)
    # print(elements)
    ls = [11,9,29,7,2,15,28]
    print(partition(ls,0,len(ls)-1))

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    # for elements in tests:
    #     quick_sort(elements, 0, len(elements)-1)
    #     print(f'sorted array: {elements}')