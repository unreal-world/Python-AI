# BT tuan 01, buoi 01 mon AI
# Nguyen Van Hoai - 20110107

decision01 = "Dat do an online"
decision02 = "Di mua do an"
decision03 = "Nhin doi"
decision04 = "An mi tom"

choice1 = input("Nhap so 1 hoac 2:\n 1. Con tien\n 2. Het tien\n")
choice2 = input("Nhap so 3 hoac 4:\n 3. Lam bieng\n 4. Sieng nang\n")

def make_decision():
    if choice1 == "1" and choice2 == "3":
        print("Quyet dinh: ", decision01)
    elif choice1 == "1" and choice2 == "4":
        print("Quyet dinh: ", decision02)
    elif choice1 == "2" and choice2 == "3":
        print("Quyet dinh: ", decision03)
    elif choice1 == "2" and choice2 == "4":
        print("Quyet dinh: ", decision04)
    else:
        print("Lua chon khong hop le!!!")

make_decision()
