state01 = "Dat do an online"
state02 = "Di mua do an"
state03 = "Nhin doi"
state04 = "An mi tom"

choice1 = input("Chon so 1 hoac 2:\n 1. Con tien\n 2. Het tien\n")
choice2 = input("Chon so 3 hoac 4:\n 3. Lam bieng\n 4. Sieng nang\n")

if choice1 == "1" and choice2 == "3":
    print(state01)
elif choice1 == "1" and choice2 == "4":
    print(state02)
elif choice1 == "2" and choice2 == "3":
    print(state03)
elif choice1 == "2" and choice2 == "4":
    print(state04)
else:
    print("Lua chon khong hop le")
