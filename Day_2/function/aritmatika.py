def add(a=None, b=None):
    if a == None or b == None:
        print ("parameter tidak lengkap")
        return
    
    total = a + b
    return total

#print(add(10,5))
#umlah = add(10, 5)

#print(f"jumlah dari 10 dan 5 = {jumlah}")

def substract(a=None, b=None):
    if a == None or b == None:
        print("parameter tidak lengkap")
        return
    
    total = a - b
    return total

def bmi (berat=None, tinggi=None):
    if berat == None or tinggi == None:
        print("parameter tidak lengkap")
        return

    total = berat / ((tinggi/100) ** 2)
    return total

def bmi_check (bmi=None):
    if bmi == None:
        print("parameter tidak lengkap")
        return
    
    
    if bmi <18.5:
        print ("Kategori: Berat badan kurang")
    elif 18.5 <= bmi <= 22.9:
         print ("Kategori: Berat badan normal")
    elif 23 <= bmi <= 24.9:
        print ("Kategori: Berat badan berlebih")
    elif 24.9 <= bmi <= 30:
        print ("Kategori: Obesitas")
    else:
         print ("ERROR")