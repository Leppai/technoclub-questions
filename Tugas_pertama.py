#1 Buat data tabel
arr = [
    {
        'no': 1,
        'nama': 'Haikal',
        'kelas': 'IF21B'
    },
    {
        'no': 2,
        'nama': 'Mr. Santai',
        'kelas': 'IF21B'
    },
    {
        'no': 3,
        'nama': 'Kisah',
        'kelas': 'IF22C'
    },
    {
        'no': 4,
        'nama': 'Ajag',
        'kelas': 'IF23B'
    }
]

for i in arr:
    print(str(i['no']) + ' ' + i['nama'] + ' ' + i['kelas'])

#2 output "Saya Teknik Informatika" sebanyak 100 kali
i = 0
while (True):
    if (i == 100):
        break
        
    print('Saya Teknik Informatika')
    
    i = i + 1

#3 buat 3 contoh operator logika
# and
a = True
b = False

if a and b:
    print("Keduanya benar")
else:
    print("Salah satu atau keduanya salah")
# or
a = True
b = False

if a or b:
    print("Setidaknya satu benar")
else:
    print("Keduanya salah")
# not
a = True

if not a:
    print("a adalah False")
else:
    print("a adalah True")

#4 Buat 3 contoh operator perbandingan
# ==
a = 5
b = 5

if a == b:
    print("a sama dengan b")
else:
    print("a tidak sama dengan b")
# >
a = 7
b = 5

if a > b:
    print("a lebih besar dari b")
else:
    print("a tidak lebih besar dari b")
# <
a = 4
b = 9

if a < b:
    print("a tidak lebih besar dari b")
else:
    print("a lebih besar dari b")

# 1 % 2 hasilnya berapa?
hasil = 1 % 2
print(hasil)

#buatkan 2 fungsi dengan paramater dan fungsi tanpa parameter
#fungsi paramater
def tambah(a, b):
    return a + b

hasil = tambah(4, 3)
print("Hasil penjumlahan:", hasil)

#fungsi tanpa paramater
def sapa():
    print("Halo selamat datang")

sapa()