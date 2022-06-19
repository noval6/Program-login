G = 3
while G>=3:
    username=input("masukkan username anda : ")
    password=input("masukkan password : ")

    if username == "alpro" and password == "daspro123":
        print("selamat, anda berhasil login")

        break

    else:
        G-=1
        print("login gagal, sisa percobaan login sebanyak ",G)