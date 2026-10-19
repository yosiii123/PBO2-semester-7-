from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_untuk_flash_message'

# 1. Class: Minimal 1 class domain
class Buku:
    def __init__(self, id_buku, judul, penulis, tahun):
        # 2. Attribute: Minimal 4 attribute
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    # 3. Method: Minimal 2 method
    def get_info(self):
        return f"Buku {self.judul} ditulis oleh {self.penulis}"

    def identitas_singkat(self):
        return f"{self.id_buku} - {self.judul}"

# Database sementara menggunakan list
data_buku_list = []

@app.route('/')
def index():
    # Menampilkan GUI form dan tabel
    return render_template('index.html', data_buku=data_buku_list)

@app.route('/tambah', methods=['POST'])
def tambah():
    # Menangkap input dari pengguna
    id_buku = request.form.get('id_buku')
    judul = request.form.get('judul')
    penulis = request.form.get('penulis')
    tahun = request.form.get('tahun')

    # 4. Validasi: Minimal 2 validasi input
    # Validasi 1: Mencegah input kosong
    if not id_buku or not judul or not penulis or not tahun:
        flash("Error: Semua kolom data harus diisi!")
        return redirect(url_for('index'))

    # Validasi 2: Mencegah duplikasi ID
    for buku in data_buku_list:
        if buku.id_buku == id_buku:
            flash(f"Error: ID Buku {id_buku} sudah terdaftar!")
            return redirect(url_for('index'))

    # 5. Object: Object dibuat dari input pengguna
    buku_baru = Buku(id_buku, judul, penulis, tahun)
    
    # 6. Aksi: Tambah data
    data_buku_list.append(buku_baru)
    flash("Sukses: Data buku berhasil ditambahkan!")
    
    return redirect(url_for('index'))

@app.route('/hapus/')
def hapus(id_buku):
    global data_buku_list
    # 6. Aksi: Hapus data
    data_buku_list = [buku for buku in data_buku_list if buku.id_buku != id_buku]
    flash(f"Sukses: Data dengan ID {id_buku} berhasil dihapus!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)