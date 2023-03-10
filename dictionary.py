user = [{"nama": 'arsene lupin', "nik": 1234, "jenis_kelamin": "male", "tanggal_lahir":"1902-03-23"},
{"nama": "sherlock holmes", "nik": 4321, "jenis_kelamin": "male", "tanggal_lahir":"1876-08-16"},
{"nama": "irene adler", "nik":6789, "jenis_kelamin": "female", "tanggal_lahir":"1884-10-07"},]

print(user)
inp=999
while inp!=0:
  print("""
  1. isi Data
  2. Cari berdasar nama
  0. keluar""")
  inp = int(input("Pilih menu: "))
  if inp == 1:
    nama = input("Apa nama anda? ")
    nik = int(input("Apa nik anda? "))
    jenis_kelamin = input("Apa jenis kelamin anda? ")
    tanggal_lahir = input("Apa tanggal lahir anda? ")
    break
  elif inp == 2:
    cari= input("Masukkan nama yang dicari: ")
    for y in user:
      for key, value in y.items():
        if value == cari:
          print("user",cari,"telah ditemukan")
          print(y)
          break
        else:
          print("user",cari,"tidak ada")
          hasil = 0
        if hasil == 0:
          break

user_dict= {"nama": nama, "nik": nik, "jenis_kelamin":jenis_kelamin, "tanggal_lahir":tanggal_lahir}
user.append(user_dict)

print(user)