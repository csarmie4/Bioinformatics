#################################         Variables and Some Arithmetic         #################################################
# import unittest
# import time

# def square(nums):
#     """Calculate the sum of squares of numbers in a list."""
#     return sum(int(i) ** 2 for i in nums)


# with open("C:/Users/sarmi/Downloads/rosalind_ini2 (2).txt", "r") as file:
#     for num in file:
#         start_time = time.time()
#         print(square(num.split()))
#         end_time = time.time()
#         print(f"Time spent: {end_time - start_time} seconds")

# class TestSquareFunction(unittest.TestCase):
#     """Test cases for the square function."""

#     def test_square(self):
#         """Test the square function with different input values."""

#         # Test case 1: Test with a list of integers
#         nums_1 = [1, 2, 3, 4, 5]
#         self.assertEqual(square(nums_1), 55)

#         # Test case 2: Test with an empty list
#         nums_2 = []
#         self.assertEqual(square(nums_2), 0)

#         # Test case 3: Test with a list containing negative integers
#         nums_3 = [-1, -2, -3, -4, -5]
#         self.assertEqual(square(nums_3), 55)


# if __name__ == "__main__":
#     unittest.main()


#################################         Strings and Lists         #################################################



# with open("C:/Users/sarmi/Downloads/rosalind_ini3 (4).txt", "r") as file:
#         split_text = file.readline()
#         a, b, c, d = map(int, file.readline().split())

# print(f'{split_text[a:b+1]}, {split_text[c:d+1]}')

#################################         Conditions and Loops         #################################################
# def odd_sum(a, b):
#     return sum(i for i in range(a, b+1) if i%2==1)

# with open("C:/Users/sarmi/Downloads/rosalind_ini4 (1).txt", "r") as file:
#     a, b = map(int, file.readline().split())
#     print(odd_sum(a, b))


#################################         Working with Files         #################################################
def even_lines(lines):
    return [lines[i] for i in range(len(lines)) if i%2==1]

with open("C:/Users/sarmi/Downloads/rosalind_ini5 (2).txt", "r") as file:
    lines = file.readlines()
even_lines = even_lines(lines)
print("".join(even_lines))

