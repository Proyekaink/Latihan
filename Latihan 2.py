print('Selamat datang di percobaan kedua')
print('-' * 10)
kamus_ind_eng = {'Abang': 'Big bro', 'istri': 'wive', 'babeh': 'father', 'emak': 'mother', 'Aink': 'Middle son', 'Adek':
    'Pussy_cat'}

print(kamus_ind_eng)
print(kamus_ind_eng['babeh'])
print(kamus_ind_eng['emak'])
print(kamus_ind_eng['Abang'])
print(kamus_ind_eng['Aink'])
print(kamus_ind_eng['Adek'])
print('-' * 10)
print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
