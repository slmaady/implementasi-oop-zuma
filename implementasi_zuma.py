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
        pass

    def tembak(self, warna_sasaran, jumlah_bola_berdekatan):
        print(f"Katak menembakkan bola warna {self.warna_peluru}")
        
        # Warna harus cocok dan jumlah bola yang sama di jalur minimal 2 (sehingga total jadi 3 atau lebih)
        if self.warna_peluru.lower() == warna_sasaran.lower() and jumlah_bola_berdekatan >= 2:
            self.skor += 50
            print(f"BERHASIL! Skor bertambah 50!")
        else:
            print("GAGAL!")

    def info_status(self):
        print("\n--- STATUS KATAK ZUMA ---")
        print(f"Status Aktif : {self.is_active}")
        print(f"Warna Peluru : {self.warna_peluru}")
        print(f"Skor Saat Ini: {self.skor}")
        print("-------------------------\n")

# --- UJI COBA PROGRAM ---
katak_player = KatakZuma("Hijau")
katak_player.info_status()

# Uji coba: Warna cocok dan jumlah bola di jalur ada 2 (total 3 bola berdekatan) -> Skor nambah
katak_player.tembak("Hijau", jumlah_bola_berdekatan=2)  

# Ganti warna ke Merah
katak_player.ganti_warna("Merah")

# Uji coba: Warna cocok tapi bola di jalur cuma 1 (kurang dari syarat minimal) -> Skor tidak nambah
katak_player.tembak("Merah", jumlah_bola_berdekatan=1)   

katak_player.info_status()