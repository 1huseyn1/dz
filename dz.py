result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a must be greater than or equal to b")
        if b == 0:
            raise ZeroDivisionError("b cannot be zero")
        if b > 100:
            raise IndexError("b must be less than or equal to 100")
        return a / b
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
for key in data:
    if isinstance(key, tuple) or not isinstance(key, int):
        print(f"Skipping key {key}, it's not a valid integer.")
        continue
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)












