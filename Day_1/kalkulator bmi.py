berat = float (input("Masukkan berat badan : "))
tinggi = float (input ("Masukkan tinggi badan : "))

bmi = berat / ((tinggi/100) ** 2)

print("BMI Anda adalah:", bmi)

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