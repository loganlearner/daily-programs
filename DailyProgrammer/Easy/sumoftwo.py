array = [10,15,3,7]

def sumOfParts(array, target):
    previous_nums = set()

    for ele in array:
        something = (target - ele)

        if something in previous_nums:
            return something, ele

        previous_nums.add(ele)


print(sumOfParts(array, 17))
