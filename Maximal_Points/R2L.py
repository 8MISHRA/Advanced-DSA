import mergeSort
from mergeSort import data1, data2, data3, data4

count = 0
def R2L(points):
    '''
    Retruns the list of maximal points in an array, also tells the count of iteraions
    
    It uses the right to left sweeping algorithm and does not requirs any candidate list.
    
    Parameter_points: List of all the points to be processed
    Precondition: Type of point should be a list containing the the tuple.
    '''
    global count

    mergeSort.merge_sort(points)
    result = [points[-1]]
    for i in range(len(points)):
        point = points[len(points)-i-1]
        count += 1
        if result[-1][1] < point[1]:
            count += 1
            result.append(point)
            
    print("ORIGINAL_DATA: ", points)
    print("No of iterations: ", count)

    return "Maximal Points: ", result[::-1]


print(R2L(data2))