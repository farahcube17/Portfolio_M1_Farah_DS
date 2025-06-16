 # Main Menu Function
def main_menu():
    print('''
    ------------------ MENU UTAMA ------------------
    1. Menampilkan Data Karyawan
    2. Menambah Data Karyawan
    3. Mengubah Data Karyawan
    4. Hapus Data Karyawan
    5. Pencarian Data Karyawan
    6. Statistik Data karyawan
    7. Keluar
    ------------------------------------------------
    ''')

# Data Karyawan
tabel_data = {
    'Nomor': [1, 2, 3, 4],
    'Nama': ['Ahamad Jaelani', 'Aida Maudy', 'Desyca Iskandar', 'Fauzi Nazrul'],
    'Employee_id': ['P001', 'P002', 'P003', 'P004'],
    'Gender': ['L', 'P', 'P', 'L'],
    'Umur': [40, 30, 24, 28],
    'Jabatan': ['manajer pemasaran', 'staff administrasi', 'staff produksi', 'manajer produksi'],
    'Salary': [8000000, 5000000, 4700000, 9500000]
}

# Login Program
def login():
    username =input('Masukkan username Anda:')
    password =input('Masukkan password Anda: ')
    if username == 'owner' and password == '123':
        print('\n Login berhasil! Selamat datang Farah!\n')
    else:
        print('\nLogin gagal!Program akan keluar secara otomatis\n')
        exit()

# Menampilkan Data Karyawan
def tampilkan_karyawan():
    while True:
        print('\n1.Tampilkan seluruh data karyawan')
        print('2.Cari karyawan berdasarkan No.ID')
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            data_karyawan()
            input('\nTekan ENTER untuk kembali ke menu utama...') 
            return
        elif pilihan == '2':
            pencarian_dataID()
            input('\nTekan ENTER untuk kembali ke menu utama...')
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def data_karyawan():
    print(f"{'Nomor':<5} | {'Nama':<20} | {'Employee_id':<12} | {'Gender':<6} | {'Umur':<4} | {'Jabatan':<20} | {'Salary':<10}")
    print('-' * 95)
    for i in range(len(tabel_data['Nomor'])):
        print(f"{tabel_data['Nomor'][i]:<5} | {tabel_data['Nama'][i]:<20} | {tabel_data['Employee_id'][i]:<12} | {tabel_data['Gender'][i]:<6} | {tabel_data['Umur'][i]:<4} | {tabel_data['Jabatan'][i]:<20} | {tabel_data['Salary'][i]:<10}")

def pencarian_dataID():
    print('\n--- Menu Pencarian Data Karyawan ---')
    keyword = input("Masukkan ID karyawan: ")
    ditemukan = False
    for i in range(len(tabel_data['Employee_id'])):
        if keyword.lower() == tabel_data['Employee_id'][i].lower():
            print("\nData ditemukan:")
            print('-'*70)
            print(f"ID       : {tabel_data['Employee_id'][i]}")
            print(f"Nama     : {tabel_data['Nama'][i]}")
            print(f"Gender   : {tabel_data['Gender'][i]}")
            print(f"Umur     : {tabel_data['Umur'][i]}")
            print(f"Jabatan  : {tabel_data['Jabatan'][i]}")
            print(f"Gaji     : {tabel_data['Salary'][i]}")
            print('-'*70)
            ditemukan = True
            break

    if not ditemukan:
        print("Ups! Data tidak ditemukan.")

# Menambahkan Data Karyawan
def tambah_data_karyawan():
    print('** Menambah data karyawan **')
    Nama = input('Masukkan Nama Karyawan: ')
    Employee_id = input('Masukkan ID Karyawan: ')
    Gender = input('Jenis kelamin (L/P): ')
    Umur = int(input('Masukkan Umur Karyawan: '))
    Jabatan = input('Masukkan Jabatan Karyawan: ')
    Salary = int(input('Masukan Gaji Karyawan: '))

    tabel_data['Nomor'].append(len(tabel_data['Nomor']) + 1)
    tabel_data['Nama'].append(Nama)
    tabel_data['Employee_id'].append(Employee_id)
    tabel_data['Gender'].append(Gender)
    tabel_data['Umur'].append(Umur)
    tabel_data['Jabatan'].append(Jabatan)
    tabel_data['Salary'].append(Salary)

    print('\nHore! Data karyawan berhasil ditambahkan!')
    data_karyawan()
    input('\nTekan ENTER untuk kembali ke menu utama...')

# Mengubah Data Karyawan
def ubah_data_karyawan():
    print('** Mengubah data karyawan **')
    data_karyawan()
    input_data_ID = input('\nMasukkan ID karyawan yang ingin diubah: ')
    if input_data_ID in tabel_data['Employee_id']:
        i = tabel_data['Employee_id'].index(input_data_ID)
        print(f"\nData karyawan yang dipilih:")
        print(f"{tabel_data['Nomor'][i]:<5} | {tabel_data['Nama'][i]:<20} | {tabel_data['Employee_id'][i]:<12} | {tabel_data['Gender'][i]:<6} | {tabel_data['Umur'][i]:<4} | {tabel_data['Jabatan'][i]:<20} | {tabel_data['Salary'][i]:<10}")

        ubah_data = input('Kolom data apa yang ingin diubah? (Nama/Employee_id/Gender/Umur/Jabatan/Salary): ')
        if ubah_data in tabel_data:
            nilai_baru = input(f'Masukkan nilai baru untuk {ubah_data}: ')
            if ubah_data == 'Umur' or ubah_data == 'Salary':
                nilai_baru = int(nilai_baru)
            konfirmasi_ubah = input("Yakin ingin mengubah data Anda? (y/n): ")
        if konfirmasi_ubah.lower() == 'y': 
            tabel_data[ubah_data][i] = nilai_baru
            print('\nData berhasil diubah!')
            data_karyawan()
        else:
            print('Data tidak berhasil diubah.')
    else:
        print('Data tidak ditemukan.')
    input('\nTekan ENTER untuk kembali ke menu utama...')

# Menghapus Data Karyawan
def hapus_data_karyawan():
    print('** Hapus data karyawan **')
    data_karyawan()
    input_data_ID = input('\nMasukkan ID karyawan yang ingin dihapus: ')
    if input_data_ID in tabel_data['Employee_id']:
        i = tabel_data['Employee_id'].index(input_data_ID)
        konfirmasi_hapus = input("Yakin ingin menghapus data ini? (y/n): ")
        if konfirmasi_hapus.lower() == 'y':
            for key in tabel_data:
                del tabel_data[key][i]
        print('\nData berhasil dihapus!')
        data_karyawan()
    else:
        print('\nID karyawan tidak ditemukan.')
    input('\nTekan ENTER untuk kembali ke menu utama...')

# Melakukan Pencarian Data Manual dengan ID atau Nama Karyawan
def pencarian_data():
    print('\n--- Menu Pencarian Data Karyawan ---')
    while True:
        keyword = input("Masukkan ID / Nama karyawan yang ingin dicari (atau ketik '-' untuk kembali): ")

        if keyword.lower() == '-':
            print("Kembali ke menu utama...\n")
            break

        ditemukan = False
        for i in range(len(tabel_data['Employee_id'])):
            if keyword.lower() == tabel_data['Employee_id'][i].lower() or keyword.lower() == tabel_data['Nama'][i].lower():
                print("\nData ditemukan:")
                print('-'*70)
                print(f"ID       : {tabel_data['Employee_id'][i]}")
                print(f"Nama     : {tabel_data['Nama'][i]}")
                print(f"Gender   : {tabel_data['Gender'][i]}")
                print(f"Umur     : {tabel_data['Umur'][i]}")
                print(f"Jabatan  : {tabel_data['Jabatan'][i]}")
                print(f"Gaji     : {tabel_data['Salary'][i]}")
                print('-'*70)
                ditemukan = True
                break
                
        if not ditemukan:
            print("Ups! Data yang Anda masukkan tidak ditemukan.\n")

 #Statistik Data Karyawan
def statistik_karyawan():
    print("\n--- Statistik  Data Karyawan ---")
    print(f"Total Karyawan : {len(tabel_data['Nama'])}")
    print(f"Rata-rata Umur : {sum(tabel_data['Umur'])/len(tabel_data['Umur']):.1f} tahun")
    print(f"Gaji Tertinggi : Rp{max(tabel_data['Salary'])}")
    print(f"Gaji Terendah  : Rp{min(tabel_data['Salary'])}")
    input('\nTekan ENTER untuk kembali ke menu utama...')

# Melakukan Login Program
login()

# Menjalankan Program Menu
while True:
    main_menu()
    menu_input = input('Masukkan pilihan menu Anda (1-7): ')
    if not menu_input.isdigit():
        print('Pilihan Anda tidak valid, silahkan coba lagi.')
        continue
    menu = int(menu_input)

    if menu == 1:
        tampilkan_karyawan()
    elif menu == 2:
        tambah_data_karyawan()
    elif menu == 3:
        ubah_data_karyawan()
    elif menu == 4:
        hapus_data_karyawan()
    elif menu == 5:
        pencarian_data()
    elif menu == 6:
        statistik_karyawan()
    elif menu == 7:
        print('\n** Terima kasih telah menggunakan program ini! **')
        break
    else:
        print('Pilihan Anda tidak valid, silahkan coba lagi.')
