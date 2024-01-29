import mergeSort
import copy
from mergeSort import data1, data2, data3, data4

count = 0
def L2R(points):
    '''
    Retruns the list of maximal points in an array, also tells the count of iteraions
    
    It uses the left to right sweeping algorithm and requirs a candidate list in adition.

    Parameter_points: List of all the points to be processed
    Precondition: Type of point should be a list containing the the tuple.
    '''
    global count
    
    mergeSort.merge_sort(points)
    candidate_list = [points[0]]

    for point in points:
        candidate_copy = copy.deepcopy(candidate_list)
        for cd in candidate_copy:
            count += 1
            if cd[1] <= point[1]:  
                candidate_list.remove(cd)
        candidate_list.append(point)
    
    print("ORIGINAL_DATA: ", points)
    print("No of iterations: ", count)

    return "Maximal Points: ", candidate_list



result = L2R(data2)
print(result)