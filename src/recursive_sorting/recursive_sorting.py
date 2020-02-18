# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # set length
    elements = len( arrA ) + len( arrB )
    # create list with length of elements
    merged_arr = [0] * elements
    # TO-DO
    merged_arr = arrA + arrB
    # print(merged_arr)
    
    merged_arr.sort()
    # print(merged_arr)
    return merged_arr

merge([1,3,5,7,9], [0,2,4,6,8])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
