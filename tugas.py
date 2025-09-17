class Main:
    def __init__(self):
        pass

    def main(self): pass
    def uiLogin(self): pass
    def uiMenu(self): pass
    def uiHitungPembayaran(self): pass
    def uiCetakStruk(self): pass


class LoginKasir:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def validasiLogin(self): pass
    def logout(self): pass


class KoneksiDatabase:
    def __init__(self, host="", database="", userName="", password=""):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password

    def membukaKoneksi(self): pass
    def eksekusiQuerySelect(self): pass
    def eksekusiQueryInsert(self): pass
    def eksekusiQueryUpdate(self): pass
    def eksekusiQueryDelete(self): pass
    def tutupKoneksi(self): pass


class HitungPembayaran:
    def __init__(self, idMenu="", namaMenu="", harga=0.0, jumlah=0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = 0.0

    def insertPembayaran(self): pass
    def updatePembayaran(self): pass
    def deleteDataPembayaran(self): pass
    def cariDataPembayaranByIdMenu(self): pass


class PembayaranTunai:
    def __init__(self):
        pass

    def hitungTotalHarga(self): pass


class PembayaranByCard:
    def __init__(self):
        pass

    def hitungTotalHarga(self): pass


class CetakStruk:
    def __init__(self, noStruk="", totalHarga=0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga

    def cetakStruk(self): pass


class TabelHitungPembayaran:
    def __init__(self, idMenu="", namaMenu="", harga=0.0, jumlah=0, totalHarga=0.0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = totalHarga

    def setIdMenu(self): pass
    def getIdMenu(self): pass
    def setNamaMenu(self): pass
    def getNamaMenu(self): pass
    def setHarga(self): pass
    def getHarga(self): pass
    def setJumlah(self): pass
    def getJumlah(self): pass
    def setTotalHarga(self): pass
    def getTotalHarga(self): pass


class TabelPembayaranByCard:
    def __init__(self, idCard="", jenisCard="", namaBank="", totalHarga=0.0):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga

    def setIdCard(self): pass
    def getIdCard(self): pass
    def setJenisCard(self): pass
    def getJenisCard(self): pass
    def setNamaBank(self): pass
    def getNamaBank(self): pass
    def setTotalHarga(self): pass
    def getTotalHarga(self): pass
