print('Selamat Malam Dunia Tipu tipu')
#Data skalar
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Haram')
print(anak)

print('\nsapa anak Haram')
print(f'Hai anak {anak[4]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')