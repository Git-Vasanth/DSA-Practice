
Q_array = []

def split(given_array):

    if len(given_array) <=1:
        return given_array

    mid_point = len(given_array) // 2

    left_part = given_array[:mid_point]
    right_part = given_array[mid_point:]

    left_split = split(left_part)
    right_split = split(right_part)

    return merge_sort(left_split , right_split)

def merge_sort(left , right):
    

    result = []

    counter_at_left , counter_at_right = 0,0

    while counter_at_left < len(left) and counter_at_right < len(right):

        if left[counter_at_left] < right[counter_at_right]:

            result.append(left[counter_at_left])

            counter_at_left += 1

        else:

            result.append(right[counter_at_right])

            counter_at_right +=1

    result.extend(left[counter_at_left:])
    result.extend(right[counter_at_right:])    

    return result

def main(given_array):

    result = split(given_array=given_array)

    print(result)

if __name__ == "__main__":

    main(given_array=Q_array)

