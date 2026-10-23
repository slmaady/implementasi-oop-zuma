class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        self.load_gambar(warna_baru)
        print(f"Katak memuat bola peluru baru berwarna: {warna_baru}")

    def load_gambar(self, warna):
        # Memuat aset gambar
        pass

    def tembak(self, warna_sasaran):
        # Skor tambah +50 jika warna sasaran bola saam dengan warna peluru dan lebih dari 2 bola
        print(f"Katak menembakkan bola warna {self.warna_peluru} ke arah jalur rantai...")
        
        # Mengecek apakah warna peluru sama dengan warna bola sasaran di jalur
        if self.warna_peluru.lower() == warna_sasaran.lower():
            self.skor += 50
            print("BERHASIL!")
        else:
            print("MELESET!")

    def info_status(self):
        print("\n--- STATUS KATAK ZUMA ---")
        print(f"Status Aktif : {self.is_active}")
        print(f"Warna Peluru : {self.warna_peluru}")
        print(f"Skor Saat Ini: {self.skor}")
        print("-------------------------\n")

# --- UJI COBA PROGRAM ---
katak_player = KatakZuma("Kuning")

#Panggil info_status() untuk melihat kondisi awal
katak_player.info_status()

#Uji coba menembak dengan sasaran yang warnanya cocok
katak_player.tembak("Kuning")  # Kuning ketemu Kuning -> Skor nambah

#Ganti warna peluru menjadi Merah
katak_player.ganti_warna("Merah")

#Uji coba menembak dengan sasaran yang tidak cocok (meleset)
katak_player.tembak("Hijau")   # Peluru Merah menembak target Hijau -> Skor tetap

#Panggil kembali info_status() untuk membuktikan perubahan data
katak_player.info_status()