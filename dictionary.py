user = [{"nama": 'arsene lupin', "nik": 1234, "jenis_kelamin": "male", "tanggal_lahir":"1902-03-23"},
{"nama": "sherlock holmes", "nik": 4321, "jenis_kelamin": "male", "tanggal_lahir":"1876-08-16"},
{"nama": "irene adler", "nik":6789, "jenis_kelamin": "female", "tanggal_lahir":"1884-10-07"},]

print(user)

nama = input("Apa nama anda? ")
nik = int(input("Apa nik anda? "))
jenis_kelamin = input("Apa jenis kelamin anda? ")
tanggal_lahir = input("Apa tanggal lahir anda? ")

user_dict= {"nama": nama, "nik": nik, "jenis_kelamin":jenis_kelamin, "tanggal_lahir":tanggal_lahir}
user.append(user_dict)

print(user)