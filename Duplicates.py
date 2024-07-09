def remove_duplicate(li):
    unique_list = []
    duplicate_list = []

    for i in li:
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicate_list.append(i)

    return unique_list


li = [a,p,p,l,e]
print("Original list:", li)
print("List after removing duplicates:", remove_duplicate(li))