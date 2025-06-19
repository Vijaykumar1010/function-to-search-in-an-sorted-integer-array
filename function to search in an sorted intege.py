# function to search in an sorted integer array

# aka binary search

def search(numbers, key)-> bool:

    left_index = 0

    right_index = len(numbers) - 1

    found = False # aumssing we not found

    while (left_index <= right_index):

        middle_index = int(left_index + (right_index - left_index)/2) # type casting

        if (numbers[middle_index] == key):

            found = True

            break
        
        if (numbers[middle_index] > key):

            # you must search on the left side of array 

            right_index = middle_index - 1

        else:

            # you must search on the right side of the array

            left_index = middle_index + 1

    return found

def invoke_search():

    input = [1,2,3,4,5,6]

    key = 6

    result = search(input, key)

    if result:

        print("Number is found")

    else:

        print("Number is not found")
        

invoke_search()