height = 10

for n in range(height):
    print(" " * n+"*" * (height - n))

for n in range(height+1):
    print(" " * (height - n), "*" * (n * 2 - 1))

for n in range(height):
    if n < 8:
        print(" " * (height - n-2)+" *" * (n + 2))



