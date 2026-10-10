n = int(input())

if n > 2:
    print("NO")
else:
    for i in range(2, n):
        if m % i == 0:
            print("NO")
            break
    else:
        print("YES")
