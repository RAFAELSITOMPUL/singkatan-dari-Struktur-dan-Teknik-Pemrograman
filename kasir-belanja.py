# Program Kasir Minimarket
# Mulia ALdi Sinaga - 24 Oktober 2025

print("=" * 50)
print("PROGRAM KASIR MINIMARKET")
print("=" * 50)

# 1. Input jumlah barang
jumlah_barang = int(input("\nMasukkan jumlah barang yang dibeli: "))

# List untuk menyimpan data barang
daftar_barang = []
total_harga = 0

# 2. Input data untuk setiap barang
print("\n" + "=" * 50)
for i in range(1, jumlah_barang + 1):
    print(f"\nBarang ke-{i}")
    nama = input("Nama barang: ")
    harga = float(input("Harga barang: Rp "))
    jumlah = int(input("Jumlah: "))
    
    # 3. Hitung subtotal per barang
    subtotal = harga * jumlah
    total_harga += subtotal
    
    # Simpan data barang
    daftar_barang.append({
        'nama': nama,
        'harga': harga,
        'jumlah': jumlah,
        'subtotal': subtotal
    })

# Tampilkan struk belanja
print("\n" + "=" * 50)
print("STRUK BELANJA")
print("=" * 50)

for i, barang in enumerate(daftar_barang, 1):
    print(f"\nBarang ke-{i}:")
    print(f"  Nama Barang: {barang['nama']}")
    print(f"  Harga: Rp {barang['harga']:,.0f}")
    print(f"  Jumlah: {barang['jumlah']}")
    print(f"  Subtotal: Rp {barang['subtotal']:,.0f}")

print("\n" + "=" * 50)
print(f"Total Harga: Rp {total_harga:,.0f}")

# 4. Cek diskon 10% jika total lebih dari Rp 500.000
if total_harga > 500000:
    diskon = total_harga * 0.10
    total_bayar = total_harga - diskon
    print(f"Diskon 10%: Rp {diskon:,.0f}")
    print(f"Total Bayar: Rp {total_bayar:,.0f}")
else:
    total_bayar = total_harga
    print(f"Total Bayar: Rp {total_bayar:,.0f}")

# 5. Input pembayaran dan hitung kembalian
print("\n" + "=" * 50)
uang_bayar = float(input("Uang yang dibayarkan: Rp "))

while uang_bayar < total_bayar:
    print(f"Uang tidak cukup! Kurang Rp {total_bayar - uang_bayar:,.0f}")
    uang_bayar = float(input("Uang yang dibayarkan: Rp "))

kembalian = uang_bayar - total_bayar

print("\n" + "=" * 50)
print("PEMBAYARAN")
print("=" * 50)
print(f"Total Bayar: Rp {total_bayar:,.0f}")
print(f"Uang Dibayar: Rp {uang_bayar:,.0f}")
print(f"Kembalian: Rp {kembalian:,.0f}")
print("=" * 50)
print("Terima kasih sudah berbelanja!")
print("=" * 50)