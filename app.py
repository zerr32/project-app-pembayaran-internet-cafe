
import random 
from datetime import datetime

ruangan = ["room1", "room2", "room3", "room4", "room5", "room6", "room7", "room8", "room9", "room10"]

makan = {
    "1": ("🍜 Mie Indomie", 5000),
    "2": ("🍚 Nasi Goreng", 10000),
    "3": ("🥚 Nasi Telur", 10000),
    "4": ("🍳 Omurice", 15000),
    "5": ("🍗 Nasi Ayam", 20000),
    "6": ("🔥 Nasi Ayam Geprek", 25000)
}

minum = {
    "1": ("☕ Kopi Panas", 3000),
    "2": ("🧊 Es Kopi", 5000),
    "3": ("🍵 Teh Panas", 3000),
    "4": ("🥤 Es Teh", 5000),
    "5": ("🍊 Jus Jeruk", 8000),
    "6": ("🍋 Es Jeruk", 8000),
    "7": ("🍨 Parfait", 10000)
}

print("===================================================")
print("==============  デジタル注文システム  ==============")
print("===============  DEJITARU CHŪMON  ================")
print("===================================================")
print()

pelanggan = int(input("Masukkan jumlah pelanggan: "))

for i in range(pelanggan):
    print()
    print(f"\n🧾 STRUK PELANGGAN KE-{i+1}")
    nama = input("Masukkan nama pelanggan: ")

    
    print("\n╔══════════════════════════════════╗")
    print("║         💻  MENU BILLING         ║")
    print("╚══════════════════════════════════╝")
    print("1. 💻 Paket Normal               Rp5000/jam")
    print("2. 💎 Paket VIP                 Rp10000/jam")
    print("════════════════════════════════════")

    pilihan = input("Masukkan paket (1/2): ")

    if pilihan == "1":
        paket = "💻 Paket Normal"
        harga = 5000
    elif pilihan == "2":
        paket = "💎 Paket VIP" 
        harga = 10000
    else:
        print("❌ Paket yang anda pilih tidak ada!")
        continue

    if paket == "💎 Paket VIP":
        custom_room = input("Masukkan nama ruangan custom anda, goshujin-sama: ")
        print(f"✨ Yokoso VIP {nama}! Ruangan anda adalah '{custom_room}'.")
    else:
        ruangan_terpilih = random.choice(ruangan)
        print(f"🍀 Sumimasen goshujin-sama, ruangan anda adalah '{ruangan_terpilih}'.")

    jam = int(input("Masukkan durasi billing (jam): "))
    total_billing = harga * jam
    print(f"💰 Total billing {jam} jam = Rp{total_billing}")

    print("\n╔══════════════════════════════════╗")
    print("║          🍜 MENU MAKANAN         ║")
    print("╚══════════════════════════════════╝")

    pesanan_makanan = []
    total_makan = 0
    pesan_makan = input("Apakah ingin memesan makanan? (y/n): ")

    if pesan_makan.lower() == 'y':
        while True:
            for kode, (nama_makanan, harga_makanan) in makan.items():
                print(f"{kode}. {nama_makanan:<25} Rp{harga_makanan}")
            pilih_makanan = input("Pilih makanan (1-6, 0 jika selesai): ")

            if pilih_makanan == '0':
                break
            if pilih_makanan in makan:
                nama_makanan, harga_makanan = makan[pilih_makanan]
                porsi = int(input("Jumlah porsi: "))
                subtotal = harga_makanan * porsi
                pesanan_makanan.append((nama_makanan, porsi, subtotal))
                total_makan += subtotal
            else:
                print("❌ Pesanan tidak valid!")

    print()

    print("\n╔══════════════════════════════════╗")
    print("║          🥤 MENU MINUMAN          ║")
    print("╚══════════════════════════════════╝")

    pesanan_minuman = []
    total_minum = 0
    pesan_minum = input("Apakah ingin memesan minuman? (y/n): ")

    if pesan_minum.lower() == 'y':
        while True:
            for kode, (nama_minuman, harga_minuman) in minum.items():
                print(f"{kode}. {nama_minuman:<25} Rp{harga_minuman}")
            pilih_minuman = input("Pilih minuman (1-7, 0 jika selesai): ")

            if pilih_minuman == '0':
                break
            if pilih_minuman in minum:
                nama_minuman, harga_minuman = minum[pilih_minuman]
                jumlah = int(input("Jumlah gelas: "))
                subtotal = harga_minuman * jumlah
                pesanan_minuman.append((nama_minuman, jumlah, subtotal))
                total_minum += subtotal
            else:
                print("❌ Pesanan tidak valid!")

    total_semua = total_billing + total_makan + total_minum
    print()
    print("================================================================================================")
    print()
    member = input("Apakah pelanggan adalah member? (y/n): ")
    diskon = 0.2 if member.lower() == "y" else 0
    potongan = total_semua * diskon
    total_bayar = total_semua - potongan

    print()
    print("================================================================================================")
    print()
    print("\n💳 PILIH METODE PEMBAYARAN 💳")
    print("1. Tunai")
    print("2. E-Wallet")
    print("3. Kartu Debit/Kredit")

    metode = input("Pilih metode (1/2/3): ")
    metode_bayar = {"1": "Tunai", "2": "E-Wallet", "3": "Kartu Debit/Kredit"}.get(metode, "Lainnya")

    bayar_uang = 0
    kembalian = 0
    if metode in ["1", "2", "3"]:
        while True:
            try:
                bayar_uang = int(input(f"Total pembayaran: Rp{int(total_bayar)}\nMasukkan jumlah uang: "))
                if bayar_uang < total_bayar:
                    print("⚠️ Uang kurang, silakan tambah lagi.")
                else:
                    kembalian = bayar_uang - total_bayar
                    print(f"✅ Kembalian: Rp{int(kembalian)}")
                    break
            except ValueError:
                print("❌ Masukkan angka yang valid.")

    print()
    print("================================================================================================")
    print()
    
    riwayat = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("\n====================================")
    print("           🧾 STRUK PEMBAYARAN          ")
    print("====================================")
    print(f"Nama Pelanggan : {nama}")
    print(f"Paket          : {paket}")
    print(f"Lama Main      : {jam} jam")
    print(f"Harga/Jam      : Rp{harga}")
    if paket == "💎 Paket VIP":
        print(f"Ruangan        : {custom_room}")
    else:
        print(f"Ruangan        : {ruangan_terpilih}")
    print("------------------------------------")

    if pesanan_makanan:
        print("🍱 Makanan:")
        for nama_makanan, jumlah, subtotal in pesanan_makanan:
            print(f"- {nama_makanan} x{jumlah} = Rp{subtotal}")
    else:
        print("🍱 Makanan: -")

    if pesanan_minuman:
        print("🥤 Minuman:")
        for nama_minuman, jumlah, subtotal in pesanan_minuman:
            print(f"- {nama_minuman} x{jumlah} = Rp{subtotal}")
    else:
        print("🥤 Minuman: -")

    print("------------------------------------")
    print(f"Total Billing  : Rp{total_billing}")
    print(f"Total Makanan  : Rp{total_makan}")
    print(f"Total Minuman  : Rp{total_minum}")
    print(f"Subtotal       : Rp{total_semua}")
    if diskon > 0:
        print(f"Diskon Member  : -Rp{int(potongan)}")
    print(f"TOTAL BAYAR    : Rp{int(total_bayar)}")
    print("------------------------------------")
    if metode in ["1", "2", "3"]:
        print(f"Jumlah Uang Pembayaran: Rp{bayar_uang}")
        print(f"Metode Bayar   : {metode_bayar}")
        print(f"Kembalian      : Rp{int(kembalian)}")
    print(f"Tanggal        : {riwayat}")
    print("====================================")
    print("Mata modote kudasai~ ❤️  Arigatou gozaimasu goshujin-sama!")
    print("====================================\n")

