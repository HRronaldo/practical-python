# bounce.py
#
# Exercise 1.5

height = 100    # Meters
bounce = 1

# while height > 0.0001:
#     height = height * (3 / 5)
#     height = round(height, 4)
#     print(bounce, height)
#     bounce += 1
while bounce <= 10:
    height = height * (3/5)
    print(bounce, round(height, 4))
    bounce += 1
