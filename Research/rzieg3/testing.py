ex_string = "this is a string"
ex_int = 14
ex_float = 12.2

ex_string = ex_int
#ex_string = 12
print(ex_string)

arr = ["apples", "bananas", "pears"]
print(arr[1])
arr.append("grapefruit")
print(arr)
arr.remove("apples")

favorite_food = {"alice": "grapefruit", "bob": "carrots"}
print(favorite_food["alice"])

boolean_ex = False

def add(number1, number2):
    return number1 + number2, "hello"

print(add(3, 4))

for i in arr:
    print(i)

for i in range(0, 10): # 0 to 10 not inclusive of 10, inclusive of 0
    print(i)