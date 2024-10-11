"""

1. Create a list of car brands.
2. Create 2 empty lists call them odd and even.
Edwin Morris
6:56 PM
3. Create a function. The function checks whether the length of the name is odd or even. If odd, places the name in the odd list otherwise in the even.
4. Print both lists.

"""

carbrands = ["Toyota", "Ford", "Honda", "Isuzu", "BMW"]

even = []
odd = []

def sort_by_length (brands):
    for brand in brands:
        if len(brand) % 2 == 0:
            even.append(brand)
        else:
            odd.append(brand)

sort_by_length(carbrands)

print("car with odd length names:", odd)
print("car with even length names:", even)
