index = [0, 1, 2, 3, 4, 5, 6]
nama = ["Alice", "Bob", "Charlie", "Edi", "Farah", "Gita", "Hasti"]
nilai = [80, 100, 90, 70, 86, 65]

nama_slice_3_tengah = nama[2:5]

print(nama_slice_3_tengah)

nama_slice_3_tengah[2] = "Clara"
print("\n")
print(nama_slice_3_tengah)


# INSERT
nama_slice_3_tengah.insert(1, "Zara")
print("\n INSERT")
print(nama_slice_3_tengah)

# APPEND
nama_slice_3_tengah.append("Zara")
print("\n")
print(nama_slice_3_tengah)

# SORT
nama_slice_3_tengah.sort()
print("\n")
print(nama_slice_3_tengah)

# POP
nama_slice_3_tengah.pop()
print("\n")
print(nama_slice_3_tengah)

# REVERSE
nama_slice_3_tengah.reverse()
print("\n")
print(nama_slice_3_tengah)


print(nama)


print("Print dengan index")
print(f"panjang data dari nama = {len(nama)}")

print("\n")
print(nama[1])
print(f"Nama {nama[1]} mendapatkan nilai {nilai[1]}")

for z in range(len(nama)):
    print(z)
    print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")