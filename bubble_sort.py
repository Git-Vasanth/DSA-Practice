unordered_list = []

def bubble_sort(unordered_list):

    for i in range(0 , len(unordered_list)):

        for j in range(0 , len(unordered_list) - 1):

            if unordered_list[j] > unordered_list[j + 1]:

                unordered_list[j] , unordered_list[j+1] = unordered_list[j + 1] , unordered_list [j]

    return unordered_list


x = bubble_sort(unordered_list=unordered_list)

print(x)