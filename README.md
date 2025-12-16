# classturunan
class turunan
# Proyek PBO – Simulasi Struktur Rumah dengan OOP Python

## Deskripsi Proyek
Proyek ini merupakan contoh penerapan **Pemrograman Berorientasi Objek (PBO)** menggunakan bahasa pemrograman **Python**.  
Program ini mensimulasikan sebuah rumah besar yang memiliki dua lantai, di mana setiap lantai terdiri dari beberapa ruangan.

Tujuan dari proyek ini adalah untuk memahami konsep dasar PBO seperti **class**, **inheritance (pewarisan)**, dan **method**.

---

## Konsep PBO yang Digunakan

1. **Class**
   - `Tempat` sebagai class induk
   - `Lantai1` dan `Lantai2` sebagai class turunan

2. **Inheritance (Pewarisan)**
   - Class `Lantai1` dan `Lantai2` mewarisi method dari class `Tempat`

3. **Method**
   - Setiap ruangan direpresentasikan sebagai method
   - Method digunakan untuk menampilkan informasi ruangan

---

## Struktur Class

### 1. Class Tempat
Class ini berfungsi sebagai **class induk** yang berisi informasi umum tentang rumah.

Method:
- `Rumah1()` → Menampilkan informasi lantai 1
- `Rumah2()` → Menampilkan informasi lantai 2

---

### 2. Class Lantai1
Class ini merupakan turunan dari `Tempat` dan berisi ruangan-ruangan di lantai 1.

Ruangan:
- Ruang Tamu
- Ruang Keluarga
- Ruang Makan dan Dapur
- Kamar Utama
- Kamar Pembantu

---

### 3. Class Lantai2
Class ini juga merupakan turunan dari `Tempat` dan berisi ruangan-ruangan di lantai 2.

Ruangan:
- Teras
- Kamar Tamu
- Kamar Anak Perempuan
- Kamar Anak Laki-laki
- Kamar Pembantu

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Simpan kode program dalam satu file, misalnya `rumah.py`
3. Jalankan perintah berikut di terminal atau command prompt:

```bash
python rumah.py
