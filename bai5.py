import random

so_bi_mat = random.randint(1, 100)

while True:
    n = int(input("Nhap so ban doan: "))

    if n < so_bi_mat:
        print("Lon hon")
    elif n > so_bi_mat:
        print("Nho hon")
    else:
        print("Chinh xac")
        break
