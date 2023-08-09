import pandas as pd
import math
import numpy as np


class Perhitungan:
    dt = None

    def __init__(self,data):
        self.dt = data

    # Membuat dataframe dari data
    kolom = ["No", "BB_U", "TB_U", "BB_TB", "Keputusan"]
    df = pd.DataFrame(dt, columns=kolom)

    def hitung_entropy(self, label):
        labels = set(self.df[label])

        # hitung entropy bbu
        jumlah_bbu = []
        gizi_buruk_bbu = []
        gizi_baik_bbu = []

        for i in labels:
            subset = self.df[self.df[label] == i]
            jumlah_bbu.append(subset[label].count())
            gizi_buruk_bbu.append(subset[subset["Keputusan"] == "Gizi Buruk"]["Keputusan"].count())
            gizi_baik_bbu.append(subset[subset["Keputusan"] == "Gizi Baik"]["Keputusan"].count())

        array_bbu = np.array(jumlah_bbu)
        array_buruk_bbu = np.array(gizi_buruk_bbu)
        array_baik_bbu = np.array(gizi_baik_bbu)

        entropy_bbu1 = (-(array_buruk_bbu / array_bbu) * np.log2(array_buruk_bbu / array_bbu))
        entropy_bbu2 = ((array_baik_bbu / array_bbu) * np.log2(array_baik_bbu / array_bbu))
        entropy_bbu = entropy_bbu1 - entropy_bbu2

        return labels, jumlah_bbu, entropy_bbu

    def entropy_total(self, label):
        labels = set(self.df[label])
        jumlah = []
        gigi_buruk = []
        gizi_baik = []

        for i in labels:
            subset = self.df[self.df[label] == i]
            jumlah.append(subset[label].count())
            gigi_buruk.append(subset[subset["Keputusan"] == "Gizi Buruk"]["Keputusan"].count())
            gizi_baik.append(subset[subset["Keputusan"] == "Gizi Baik"]["Keputusan"].count())

        result = (-(sum(gigi_buruk) / sum(jumlah)) * np.log2(sum(gigi_buruk) / sum(jumlah))) - (
                (sum(gizi_baik) / sum(jumlah)) * np.log2(sum(gizi_baik) / sum(jumlah)))

        return result, jumlah

    def hitung_gain(self, label):
        result = 0
        total_entropy, jumlah_semua_entropy = self.entropy_total(label)
        label_entropy, jumlah, entropy = self.hitung_entropy(label)

        for i in range(len(label_entropy)):
            x_enropy = 0
            x_jumlah_item = jumlah[i]
            if (entropy[i] > 0):
                x_enropy = entropy[i]
            # print("cek ", x_enropy, " | ", x_jumlah_item)
            result = result + (x_jumlah_item / sum(jumlah_semua_entropy) * x_enropy)

        return total_entropy - result
