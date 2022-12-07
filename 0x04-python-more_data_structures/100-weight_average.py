#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    array = []
    for i in range(len(my_list)):
        array.append(my_list[i][0] * my_list[i][1])

    totalscore = 0
    for i in array:
        totalscore += i

    totalweight = 0
    for i in range(len(my_list)):
        totalweight += my_list[i][1]

    return totalscore/totalweight
