class ProductList:
    def __init__(self, array):
        self.input_list = self.validate_list(array)
        self.output_list = self.get_product_list(array)
    
    @staticmethod
    def validate_list(array):
        if not isinstance(array, list):
            raise Exception("Input is not a list")
        if len(array) == 0:
            raise Exception("Input is a empty list")
        return array
    
    @staticmethod
    def aux_get_zeros_and_product(array):
        whole_product = 1
        count_zeros = 0
        # we use 'for loop' for more explicit iteration
        # this is O(n)
        for element in array:
            if not isinstance(element, int) and not isinstance(element, float):
                raise Exception("List contains other than numbers")
            if element == 0:
                count_zeros += 1
                continue
            whole_product = whole_product * element
        return whole_product, count_zeros

    @classmethod
    def get_product_list(cls, array):
        output_list = []
        product, zeros = cls.aux_get_zeros_and_product(array)
        # if has more than 1 zero
        # means that the product will be 0 on every iteration
        if zeros > 1:
            output_list = [0] * len(array)
            return output_list
        # this 'for loop' is also O(n)
        for element in array:
            if element == 0:
                output_list.append(product)
            elif zeros == 1:
                output_list.append(0)
            else:
                output_list.append(product/element)
        return output_list

product_test1 = ProductList([1, 2, 3, 4])
product_test2 = ProductList([1, 2, 3, 34, 54, 0, 1])
product_test3 = ProductList([12, 11.1, 10, 9, 3.4, 1.3])
product_test4 = ProductList([1, 0, 2, 0, 3, 4])
product_test5 = ProductList([1, 1, 1, 1, 1])

print(product_test1.output_list)
print(product_test2.output_list)
print(product_test3.output_list)
print(product_test4.output_list)
print(product_test5.output_list)

# product_error1 = ProductList("")
# product_error2 = ProductList([])
# product_error3 = ProductList(())
# product_error4 = ProductList(None)
