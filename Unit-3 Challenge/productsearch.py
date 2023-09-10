def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices


product_list = []
try:
    x=int(input("Enter no: of items"))
except Exception:
    print("Enter proper values only: ")
else: 
    for i in range(x):
        y=input("Enter products: ")
        product_list.append(y)

    target = input("Enter element to be found: ")
    result = linear_search_product(product_list, target)
    if result:
        print("The product,",target," was found at indices:", result)
    else:
        print([])
