from data import Data
from perhitungan import Perhitungan
import numpy as np


def tes_perhitungan():
    x = Perhitungan()
    # Menghitung entropy dan gain untuk setiap fitur
    fitur_fitur = ["BB_U", "TB_U", "BB_TB"]
    target = "Keputusan"
    hasil = []

    # Menampilkan hasil dalam format tabel
    print("Node 1")
    print("BB_U")
    print(x.hitung_entropy("BB_U"))
    print("Gain : ", x.hitung_gain("BB_U"))
    print("")
    print("TB_U")
    print(x.hitung_entropy("TB_U"))
    print("Gain : ", x.hitung_gain("TB_U"))
    print("")
    print("BB_TB")
    print(x.hitung_entropy("BB_TB"))
    print("Gain : ", x.hitung_gain("BB_TB"))
    print("-------------------------------------")

    # Menampilkan hasil dalam format tabel
    for d
    print("NODE 2")
    print("BB_U")
    print(x.hitung_entropy("BB_U"))
    print("Gain : ", x.hitung_gain("BB_U"))
    print("")
    print("TB_U")
    print(x.hitung_entropy("TB_U"))
    print("Gain : ", x.hitung_gain("TB_U"))
    print("")
    print("BB_TB")
    print(x.hitung_entropy("BB_TB"))
    print("Gain : ", x.hitung_gain("BB_TB"))
    print("-------------------------------------")


if __name__ == '__main__':
    tes_perhitungan()
