# list1 = [56,3,2,78,6,0]
list1 = [56,0,2,2,6,0]
print(list1)
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    # print(min_val)
    min_index=list1.index(min_val,i)
    # print(min_index)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)