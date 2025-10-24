# Program Menghitung IPK
# Mulia Aldi Sinaga - 24 Oktober 2025

print("=" * 50)
print("PROGRAM MENGHITUNG IPK")
print("=" * 50)

# 1. Input nama mahasiswa
nama = input("\nMasukkan nama mahasiswa: ")

# 2. Input jumlah matakuliah
jumlah_mk = int(input("Masukkan jumlah matakuliah: "))

# 3. Input nama matakuliah dan nilai untuk setiap matakuliah
total_nilai = 0
print("\n" + "=" * 50)

for i in range(1, jumlah_mk + 1):
    print(f"\nMatakuliah ke-{i}")
    nama_mk = input(f"Masukkan nama matakuliah: ")
    nilai = float(input(f"Masukkan nilai matakuliah: "))
    
    # Validasi nilai rentang 0-100
    while nilai < 0 or nilai > 100:
        print("Nilai harus dalam rentang 0-100!")
        nilai = float(input(f"Masukkan nilai matakuliah: "))
    
    total_nilai += nilai

# 4. Menghitung IPK
ipk = total_nilai / jumlah_mk

# 5. Output hasil
print("\n" + "=" * 50)
print("HASIL PERHITUNGAN IPK")
print("=" * 50)
print(f"Nama Mahasiswa: {nama}")
print(f"Total Matakuliah: {jumlah_mk}")
print(f"IPK: {ipk:.2f}")

# 6. Menentukan status kelulusan
if ipk >= 60:
    print(f"Status: LULUS")
else:
    print(f"Status: TIDAK LULUS")

print("=" * 50)