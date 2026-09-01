# break - exits the current loop and continues with the next statement after the loop.

for i in range(10):
    if i==7:
        break
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6


# continue - skips the current iteration and continues with the next iteration of the loop.

for i in range(10):
    if i==6:
        continue
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9