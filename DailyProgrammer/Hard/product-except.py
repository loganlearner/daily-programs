array = [1,2,3,4,5]

def productExcept(array):
    output = []

    for i in range(len(array)):
        product_sum = 1

        for j in range(len(array)):
            num = array[j]
            if i == j:
                continue

            product_sum *= num

        output.append(product_sum)

    return output

print(productExcept(array))