def merge_sort(arr):
    '''
    Sorts the given array of tuples on the basis of their first element.
    In casse their first element is same, it sorts them on the basis of their second element.

    Uses the merge sort algorithm
    
    Parameter_arr: The list of tuples containing two points (say (x, y)) of an ordered universe
    Precondition: Type of arr is list and it should contain at least on tuple with integer entries.
        '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                arr[k] = left_half[i]
                i += 1
            elif (left_half[i][0] == right_half[j][0]) and (left_half[i][1] < right_half[j][1]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if there are any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if there are any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


data1 = [
    (5, 12),(9, 20),(3, 8),
    (17, 6),(11, 14),(1, 16),
    (7, 18),(13, 10),(19, 4),
    (15, 2),(8,19), (90, 1)]

data2 = [
    (1, 3), (2, 2), (3, 1), (3, 4), (4, 3),
    (2, 5), (5, 2), (6, 4), (7, 1), (7, 3),
    (8, 6), (9, 2), (10, 4), (11, 3), (12, 5),
    (13, 4), (14, 1), (15, 6), (16, 3), (17, 5)
]

data4=[
    (12, 5),  (13, 4),  (14, 1), 
    (15, 5.5),(15, 5.6),(15, 6),
    (15, 5.7),(15, 5.1),(16, 3), 
    (17, 5),  (25, 1),  (25, 1.2),
    (25, 1.3),(25, 4),  (25, 1.5),
    (25, 1.4), (25, 2), (25, 3)
]

data3 = [(2, 3), (4, 5), (1, 7), (3, 2), (1,7),(3,8)]


# Example usage:
if __name__ == "__main__":
    my_list = [
    (1, 3), (2, 2), (3, 1), (3, 4), (4, 3),
    (2, 5), (5, 2), (6, 4), (7, 1), (7, 3),
    (8, 6), (9, 2), (10, 4), (11, 3), (12, 5),
    (13, 4), (14, 1), (15, 5.5),(15, 5.6),(15, 6),(15, 5.7),(15, 5.1), (16, 3), (17, 5), (25, 1),(25, 1.2),(25, 1.3), (25, 4),(25, 1.5),(25, 1.4), (25, 2), (25, 3)
]
    print("Original list:", my_list)

    merge_sort(my_list)

    print("Sorted list:", my_list)