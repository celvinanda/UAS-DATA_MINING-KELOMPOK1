from data import Data
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class Pelatihan:
    def __init__(self):
        self.data = Data().data_balita  # Diasumsikan kelas Data menyediakan data dalam format yang sama seperti sebelumnya

    def persiapkan_data(self):
        data = self.data
        fitur = []
        label = []

        # Encode fitur-fitur kategorikal
        encoder_bbu = LabelEncoder()
        encoder_tbu = LabelEncoder()
        encoder_bbtb = LabelEncoder()

        for entri in data:
            bbu = entri[1]
            tbu = entri[2]
            bbtb = entri[3]
            keputusan = entri[4]

            # Ubah data kategorikal menjadi label-label numerik
            label_bbu = encoder_bbu.fit_transform([bbu])[0]
            label_tbu = encoder_tbu.fit_transform([tbu])[0]
            label_bbtb = encoder_bbtb.fit_transform([bbtb])[0]

            fitur.append([label_bbu, label_tbu, label_bbtb])
            label.append(keputusan)

        return fitur, label

    # Perhitungan Klasifikasi Penentuan Root Node
    def klasifikasi(self):
        # Persiapkan data dan bagi menjadi fitur-fitur dan label-label
        fitur, label = self.persiapkan_data()

        # Bagi data menjadi data latih (training) dan data uji (testing)
        fitur_latih, fitur_uji, label_latih, label_uji = train_test_split(fitur, label, test_size=0.2, random_state=42)

        # Buat model Decision Tree
        pohon_keputusan = DecisionTreeClassifier()

        # Latih model menggunakan data latih
        pohon_keputusan.fit(fitur_latih, label_latih)

        # Lakukan prediksi menggunakan data uji
        label_prediksi = pohon_keputusan.predict(fitur_uji)

        # Hitung akurasi model
        akurasi = accuracy_score(label_uji, label_prediksi)
        print("Akurasi:", akurasi)
