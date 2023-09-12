from api import Surah, Juz
import inquirer
from inquirer.themes import BlueComposure
from pyfiglet import Figlet
from rich import box
from rich.console import Console
from rich.table import Table
from os import system, name
from functools import cached_property
from shutil import get_terminal_size
from typing import List, Dict




# versi = 12-09-2023.v3.1

# klasifikasi Surah
def kalimat_pembuka():
    ss = Surah(1).ayat
    return ss[str(1)]['teksArab'], ss[str(1)]['teksLatin'], ss[str(1)]['teksIndonesia']

def daftar_namaLatin() -> List[str]:
    baru = []
    for i in range(1, 115):
        baru.append(Surah(i).data[2])
    return baru

def kata_kunci_namaLatin() -> Dict[str, str]:
    baru = {}
    for i in range(1, 115):
        ss = Surah(i).data
        baru[ss[0]] = ss[2]
    return baru

def terminalSurah() -> inquirer.prompt:
    qs = [
        inquirer.List("pilih", message="pilih surah ".title(), choices=daftar_namaLatin(), carousel=True)]

    return inquirer.prompt(qs, theme=BlueComposure())

def data_ayat(nomor_urut: int, nama: str, pembuka=True):
    pp = kalimat_pembuka()
    aa = Surah(nomor_urut)
    jumlah_ayat = aa.data[3]
    table = Table(title="{}".format(nama), show_lines=True, box=box.DOUBLE)
    table.add_column("Nomor", justify="center", style="white", no_wrap=True)
    table.add_column("Ayat", justify="center", style="deep_sky_blue1")
    table.add_column("Teks Latin", justify="center", style="orange_red1")
    table.add_column("Terjemahan", justify="center", style="gold1")
    if pembuka:
        table.add_row("", "{}".format(pp[0]), "{}".format(pp[1]), "{}".format(pp[2]))
        for i in range(jumlah_ayat):
            table.add_row(
                "{}".format(i+1), "{}".format(aa.ayat[str(i+1)]['teksArab']), "{}".format(aa.ayat[str(i+1)]['teksLatin']), 
                "{}".format(aa.ayat[str(i+1)]['teksIndonesia']))
    else:
        for i in range(jumlah_ayat):
            table.add_row(
                "{}".format(i+1), "{}".format(aa.ayat[str(i+1)]['teksArab']), "{}".format(aa.ayat[str(i+1)]['teksLatin']), 
                "{}".format(aa.ayat[str(i+1)]['teksIndonesia']))

    console = Console()
    console.print(table)

# klasifikasi Juz
def daftar_namaJuz() -> List[str]:
    baru = []
    for i in range(1, 31):
        baru.append(f"Juz {i}")
    return baru

def kata_kunci_namaJuz() -> Dict[str, str]:
    baru = {}
    for i in range(1, 31):
        baru[i] = f"Juz {i}"
    return baru

def terminalJuz() -> inquirer.prompt:
    qns = [
        inquirer.List("pilih", message="pilih juz ".title(), choices=daftar_namaJuz(), carousel=True)]

    return inquirer.prompt(qns, theme=BlueComposure())

def data_juz(nomor_urut: int, nama: str) -> Console:
    kjuz = Juz(nomor_urut).data
    table = Table(title="Juz {}".format(nama), show_lines=True, box=box.DOUBLE)
    table.add_column("Nomor", justify="center", style="white", no_wrap=True)
    table.add_column("Ayat", justify="center", style="deep_sky_blue1")
    table.add_column("Teks Latin", justify="center", style="orange_red1")
    table.add_column("Terjemahan", justify="center", style="gold1")
    for v in kjuz.values():
        table.add_row(
            "{}".format(v[0]), "{}".format(v[1]), "{}".format(v[2]), "{}".format(v[3]))

    console = Console()
    console.print(table)

# fungsi utama
def main():
    print("(1). Juz")
    print("(2). Surah")
    ll = input("Masukkan Pilihan : ")
    if ll == str(2):
        tt = terminalSurah()
        kk = kata_kunci_namaLatin()
        for k, i in kk.items():
            if tt['pilih'] == i:
                nn, mm = "at-taubah".title(), "al-fatihah".title()
                if i ==  nn:
                    data_ayat(k, nn, pembuka=False)
                elif i == mm:
                    data_ayat(k, mm, pembuka=False)
                else:
                    data_ayat(k, i)
    elif ll == str(1):
        mli = terminalJuz()
        lit = kata_kunci_namaJuz()
        for k, v in lit.items():
            if mli['pilih'] == v:
                dtm = v.split(' ')[1]
                data_juz(dtm, dtm)

def bersihkan_layar():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def judul(kalimat: str, tengah=True):
    f = Figlet(font='slant', justify='center')
    if tengah:
        print(*[x.center(get_terminal_size().columns) for  x in f.renderText(kalimat).split('\n')], sep='\n')
    else:
        print(f.renderText(kalimat))

class Main(object):
    def __init__(self, acuan=True):
        self.acuan = acuan

    @cached_property
    def menu(self):
        while self.acuan:
            bersihkan_layar()
            judul("Al-Qur'an")
            print('\n'*2)
            main()
            print()
            cari_surah_lagi = input("Cari surah lainnya (Y/n) ")
            if cari_surah_lagi == 'y' or cari_surah_lagi == 'Y':
                pass
            else:
                self.acuan = False


if __name__ == '__main__':
    mm = Main()
    mm.menu
    
    





