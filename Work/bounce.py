# bounce.py
#
# Exercise 1.5
height = 100

decrement = 0.6

total_bounces = 10

bounce = 1

while (bounce <= total_bounces):

    height = height*decrement
    print(bounce, round(height, 4))
    bounce = bounce + 1

