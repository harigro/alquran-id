from api import Surah
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




# versi = 21-8-2023.v2.0

def kalimat_pembuka():
    ss = Surah(1).ayat
    return ss[str(1)]['teksArab'], ss[str(1)]['teksLatin'], ss[str(1)]['teksIndonesia']

def daftar_namaLatin() -> List[str]:
    baru = []
    for i in range(1, 115):
        baru.append(Surah(i).data[2])
    return baru

def kata_kunci_namaLatin() -> List[str]:
    baru = {}
    for i in range(1, 115):
        ss = Surah(i).data
        baru[ss[0]] = ss[2]
    return baru

def terminal() -> inquirer.prompt:
    questions = [
        inquirer.List("pilih", message="pilih surah ".title(), choices=daftar_namaLatin(), carousel=True)]

    return inquirer.prompt(questions, theme=BlueComposure())

def data_ayat(nomor_urut, pembuka=True):
    pp = kalimat_pembuka()
    aa = Surah(nomor_urut)
    jumlah_ayat = aa.data[3]
    table = Table(title="Al-Qur'an", show_lines=True, box=box.DOUBLE)
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

# fungsi utama
def main():
    tt = terminal()
    kk = kata_kunci_namaLatin()
    for k, i in kk.items():
        if tt['pilih'] == i:
            if i == "at-taubah".title() or i == "al-fatihah".title():
                data_ayat(k, pembuka=False)
            else:
                data_ayat(k)

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
    
    





