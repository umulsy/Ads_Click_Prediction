# Ads_Click_Prediction
# Laporan Proyek Machine Learning: Ads Click Prediction
## 1. Domain Proyek
### Latar Belakang
Dalam dunia periklanan digital, memahami perilaku pengguna saat mereka mengklik atau mengabaikan iklan adalah informasi penting bagi pengiklan untuk meningkatkan efektivitas kampanye. Prediksi klik iklan sangat penting untuk mengoptimalkan alokasi anggaran pemasaran dan meningkatkan konversi.

### Tujuan
Prediksi klik iklan memungkinkan perusahaan untuk:
- Meningkatkan ROI iklan melalui penargetan yang lebih tepat.
- Mengurangi pemborosan anggaran dengan mengurangi jumlah iklan yang ditayangkan pada audiens yang kurang berpotensi.

### Riset Terkait
Studi menunjukkan bahwa penggunaan model machine learning seperti Random Forest dan XGBoost telah meningkatkan akurasi prediksi dalam analisis perilaku klik iklan karena kedua model ini mampu menangani data kompleks dengan baik (Sumber1, Sumber2).

## 2. Business Understanding
### Masalah
Problem Statement: Apakah dapat diprediksi apakah pengguna akan mengklik iklan berdasarkan atribut mereka seperti usia, jenis kelamin, riwayat penelusuran, jenis perangkat, dan waktu akses?

### Tujuan:
Mengembangkan model prediksi yang akurat untuk meminimalkan iklan yang tidak tepat sasaran.

### Solution Statement
Algoritma KNN: Menggunakan KNN untuk memprediksi kecenderungan klik berdasarkan kesamaan profil pengguna.
Algoritma Random Forest: Model ini digunakan karena kemampuannya dalam menangani data dengan variabel kategori dan menangani overfitting dengan baik.
XGBoost: Model ini diharapkan meningkatkan akurasi lebih lanjut karena algoritma boosting yang optimal untuk mengurangi kesalahan prediksi.

## 3. Data Understanding
### Tentang dataset
Tentang
diunduh dari : [LINK DATASET](https://www.kaggle.com/datasets/marius2303/ad-click-prediction-dataset)
Kumpulan data ini memberikan wawasan tentang perilaku pengguna dan iklan daring, khususnya berfokus pada prediksi apakah pengguna akan mengeklik iklan daring. Kumpulan data ini berisi informasi demografi pengguna, kebiasaan menjelajah, dan detail terkait tampilan iklan.
Kumpulan data ini ideal untuk membangun model klasifikasi biner guna memprediksi interaksi pengguna dengan iklan daring.

### Fitur

id: Pengidentifikasi unik untuk setiap pengguna.
full_name: Nama pengguna diformat sebagai "UserX" untuk anonimitas.
age: Usia pengguna (berkisar antara 18 hingga 64 tahun).
gender: Jenis kelamin pengguna (dikategorikan sebagai Pria, Wanita, atau Non-Biner).
device_type: Jenis perangkat yang digunakan pengguna saat melihat iklan (Seluler, Desktop, Tablet).
ad_position: Posisi iklan di halaman web (Atas, Samping, Bawah).
browsing_history: Aktivitas penjelajahan pengguna sebelum melihat iklan (Belanja, Berita, Hiburan, Pendidikan, Media Sosial).
time_of_day: Waktu saat pengguna melihat iklan (Pagi, Siang, Sore, Malam).
click: Label target yang menunjukkan apakah pengguna mengklik iklan (1 untuk klik, 0 untuk tidak mengklik).

## 4. Data Preparation
### Teknik Data Preparation
Penanganan Missing Values: Mengisi nilai kosong dengan mean (untuk variabel numerik) atau mode (untuk variabel kategori).
Encoding Variabel Kategori: Menggunakan teknik one-hot encoding untuk variabel seperti device type dan gender.
Menghapus kolom id
Membuat kolom user type dengan label recurrent user dan first time user
Normalisasi Data: Normalisasi kolom numerik untuk meningkatkan kinerja KNN.
Pembagian Data: Membagi dataset menjadi 80% data latih dan 20% data uji.
### Alasan Data Preparation
Encoding dilakukan untuk memastikan bahwa semua data dalam format numerik.
Normalisasi bertujuan untuk mengurangi efek skala pada model KNN yang sensitif terhadap jarak antar data.
Untuk mengkategorikan tipe user
## 5. Modeling
### Algoritma yang Digunakan
KNN (K-Nearest Neighbors): Model ini menggunakan parameter k yang disetel melalui cross-validation.
Random Forest: Parameter n_estimators dan max_depth disetel melalui grid search.
XGBoost: Kami menggunakan learning_rate, n_estimators, dan max_depth sebagai parameter utama untuk proses tuning.
Kelebihan dan Kekurangan
KNN: Sederhana namun kurang optimal untuk dataset besar.
Random Forest: Kuat terhadap overfitting tetapi membutuhkan lebih banyak sumber daya.
XGBoost: Sangat akurat dan efisien dalam meminimalkan kesalahan, namun membutuhkan waktu yang lebih lama untuk pelatihan.
### Model Terbaik
Hasil menunjukkan bahwa Random forest memberikan hasil terbaik dengan akurasi 96%, diikuti oleh XGBoost dengan akurasi 92%. Random Forest dipilih sebagai model akhir karena akurasinya yang lebih tinggi.

## 6. Evaluation
### Metrik Evaluasi
Akurasi: Persentase prediksi benar dari seluruh prediksi.
Precision dan Recall: Digunakan untuk mengukur relevansi prediksi, terutama untuk kelas positif (klik).
F1-Score: Menggabungkan precision dan recall dalam satu metrik.
### Hasil Proyek
Model Random forest mencapai akurasi sebesar 96% dan F1-Score sebesar 0,96, menunjukkan bahwa model ini cukup efektif dalam memprediksi klik iklan.

## Source
1. Understanding Ads Click-Through Rate Prediction with Machine Learning from Medium [LINK](https://medium.com/@varun.tyagi83/understanding-ads-click-through-rate-prediction-with-machine-learning-9ee1e637203c)
2. Research Gate : Difference of KNN, Random Forest, XGB [LINK](https://www.researchgate.net/post/What_is_the_difference_between_the_three_Machine_Learning_models)
