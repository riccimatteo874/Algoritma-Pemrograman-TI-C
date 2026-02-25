def kantin():
    print("Selamat Datang di Kantin")
    nasgor = 15000
    print(f'Harga Nasi Goreng: {nasgor}')

    try:
        jumlah = int(input('beli berapa: '))
        if jumlah <= 0:
            print('minimal beli 1 porsi')
        else:
            harga = jumlah*nasgor
            print(f'bayar {harga}')

    except ValueError:
        print('ketik angka saja (1,2,3,...)')
    
    finally:
        print('Terima kasih')

kantin()