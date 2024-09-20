Berikut adalah template README yang informatif dan menarik untuk proyek GitHub Anda, menjelaskan cara menjalankan kode aplikasi cipher yang telah Anda buat:

---

# Aplikasi Cipher GUI

Aplikasi ini adalah sebuah **tool enkripsi dan dekripsi** yang mendukung tiga jenis cipher populer: **Vigenere Cipher**, **Playfair Cipher**, dan **Hill Cipher**. Aplikasi ini dibangun menggunakan **Python** dengan antarmuka GUI berbasis **Tkinter**, memungkinkan pengguna untuk mengenkripsi dan mendekripsi pesan melalui input teks langsung atau file `.txt`.

## Fitur Utama
- **Vigenere Cipher**: Menggunakan kunci berupa kata untuk mengenkripsi dan mendekripsi pesan.
- **Playfair Cipher**: Metode cipher yang bekerja pada pasangan huruf menggunakan matriks 5x5.
- **Hill Cipher**: Cipher berbasis matriks 3x3 dengan dukungan enkripsi dan dekripsi.

## Tangkapan Layar
<img width="796" alt="image" src="https://github.com/user-attachments/assets/be105536-345d-464e-9a56-63accfb6fc3a">


## Cara Instalasi dan Penggunaan

### Prasyarat
Pastikan untuk menginstal **Python 3.x** di sistem. Selain itu, isntall library yang dibutuhkan, yaitu **Tkinter**.

### Langkah-langkah Instalasi

1. Clone repository ini ke komputer:
    ```bash
    git clone https://github.com/username/repository-name.git
    cd repository-name
    ```

2. (Opsional) Aktifkan virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Pastikan Tkinter sudah terinstal. Jika belum, isntall dengan perintah berikut (untuk Linux):
    ```bash
    sudo apt-get install python3-tk
    ```

4. Jalankan aplikasi dengan perintah:
    ```bash
    python main.py
    ```

### Cara Menggunakan Aplikasi

1. Pilih **metode cipher** yang diinginkan dari dropdown menu: `Vigenere`, `Playfair`, atau `Hill`.
2. Masukkan **teks** yang ingin dienkripsi atau didekripsi. Anda bisa mengetik langsung atau memilih file `.txt` melalui opsi input sumber.
3. Masukkan **kunci** untuk proses enkripsi atau dekripsi. 
    - Untuk **Vigenere Cipher**, kunci harus berupa kata.
    - Untuk **Playfair Cipher**, kunci bisa berupa teks tanpa karakter berulang.
    - Untuk **Hill Cipher**, kunci harus berupa teks yang panjangnya 9 huruf.
4. Pilih jenis operasi: **Enkripsi** atau **Dekripsi**.
5. Klik tombol **Proses** untuk melihat hasil enkripsi atau dekripsi.

### Contoh Penggunaan

#### Vigenere Cipher
- **Kunci**: `ITSASECRET`
- **Teks**: `Keberlanjutan hilirisasi untuk menciptakan pusat-pusat pertumbuhan ekonomi baru.`
- **Hasil Enkripsi**: `Sxtejpcennbtf zmnzvbatki ypkyd fwnumrkedig pmwck-iclst tgixnuumhsr vohvhei fciy.`
- **Hasil Dekripsi**: `Cljezhywfblhv pejrnpkhai qlcqr tmnkencwrsu pcoyc-wmzit lcapbeichij ngvfvui xyaq.`

#### Playfair Cipher
- **Kunci**: `ITSASECRET`
- **Teks**: `Keberlanjutan hilirisasi untuk menciptakan pusat-pusat pertumbuhan ekonomi baru.`
- **Hasil Enkripsi**: `MSFSDHIQENSEUVGTGACTAEATZUOIPMZMIUGCOSSLIQXUPEESXUPEESXUTFEOKFOMIQZEHPOPGEXFTDUZ`
- **Hasil Dekripsi**: `MXYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY`

#### Hill Cipher
- **Kunci**: `GYBNQKURP`
- **Teks**: `ACT`
- **Hasil Enkripsi**: `PUFRIEHKQESVRPYCQTCLUYEKJFZYJEOTMWNQEJDNSXOJHJUHOWHJUHQXTIZDWSVNXHWPEIYXBIJTXLHIE`
- **Hasil Dekripsi**: `edonfqjfwnmmpctriayxvaimoqhqzhqhlcrvvrfubqfjnkpsfwakpsblpptrjameermbfvsoibamqznhu`
