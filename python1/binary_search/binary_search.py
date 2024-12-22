def binary_search(array, x, low, high):

    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        
        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [3,4,5,6,7,8,9]
x = 4

result = binary_search(array, x, 0, len(array) -1)

if result != -1:
    print('element is present at index' + str(result))


# import unittest
# from algorithms.binary_search import binary_search

# class TestBinarySearch(unittest.TestCase):
#     def test_binary_search(self)
#     array = [3,4,5,6,7,8,9]
#     find = 4

#     result = binary_search(array, find, 0, len(array) -1)
#     self.assertEqual(result, 1)