def merge_sort(arr):
    
    if len(arr)>1:
        mid=len(arr)//2
        leftArr=arr[:mid]
        rightArr=arr[mid:]
        
        merge_sort(leftArr)
        merge_sort(rightArr)
        
        i=0
        j=0
        k=0
        
        while i<len(leftArr) and j<len(rightArr):
            if(leftArr[i]>rightArr[j]):
                arr[k]=leftArr[i]
                i+=1
            else:
                arr[k]=rightArr[j]
                j+=1
            k+=1
        
        while i<len(leftArr):
            arr[k]=leftArr[i]
            i+=1
            k+=1
            
        while j<len(rightArr):
            arr[k]=rightArr[j]
            j+=1
            k+=1
    return arr


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    str1=""
    str2=""
    if len(input_list)==0:
        return (-1,-1)
    
    sorted_list=merge_sort(input_list)
    
    if len(input_list)<2:
        return input_list
        
    for i in range(len(sorted_list)):
        if i%2==0:
            str1+=str(sorted_list[i])
        else:
            str2+=str(sorted_list[i])
    
    return (int(str1),int(str2))      


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[-1,-1]])
test_function([[1,2],[2,1]])
test_function([[2],[2]])
test_function([[236],[236]])
test_function([[9,9,9,8,8],[998,98]])
