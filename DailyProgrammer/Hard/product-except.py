#Daily Programmer #2 [Hard]

array = [1,2,3,4,5]

def productSumExcept(array):
    output = []

    for i in range(len(array)):
        product_sum = 1

        for j in range(len(array)):
            if i == j:
                continue

            num = array[j]
            product_sum *= num

        output.append(product_sum)

    return output

print(productSumExcept(array))