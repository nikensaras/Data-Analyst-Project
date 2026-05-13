from datetime import datetime
def sapa_nama(nama= None):
    if nama is None:
        print ("Silahkan masukkan nama")
        return

    print(f"HELLO {nama}")

# printf Sebelum memanggil fungsi

# sapa() 
sapa_nama()

print (datetime.now())


