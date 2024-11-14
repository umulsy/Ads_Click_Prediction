# Ads_Click_Prediction
# Laporan Proyek Machine Learning: Ads Click Prediction
## 1. Domain Proyek
### Latar Belakang
Dalam dunia periklanan digital, memahami perilaku pengguna saat mereka mengklik atau mengabaikan iklan adalah informasi penting bagi pengiklan untuk meningkatkan efektivitas kampanye. Prediksi klik iklan sangat penting untuk mengoptimalkan alokasi anggaran pemasaran dan meningkatkan konversi.

### Tujuan
Prediksi klik iklan memungkinkan perusahaan untuk:
- Meningkatkan ROI iklan melalui penargetan yang lebih tepat.
- Mengurangi pemborosan anggaran dengan mengurangi jumlah iklan yang ditayangkan pada audiens yang kurang berpotensi.

## 2. Business Understanding
Proyek ini dibuat berdasarkan karakteristik perusahaan iklan
### 1. Perusahaan Periklanan Digital yang Berorientasi pada Analisis Data
Perusahaan ini sangat menekankan penggunaan analisis data untuk meningkatkan efektivitas kampanye iklan mereka. Dengan mengakui pentingnya analisis prediktif dan machine learning, mereka memiliki komitmen untuk mengoptimalkan setiap keputusan pemasaran digital. Prediksi klik iklan yang akurat memungkinkan perusahaan untuk menargetkan pelanggan potensial secara lebih efektif, meningkatkan konversi, serta mengelola anggaran iklan secara lebih efisien.

### 2. Perusahaan dengan Basis Data Pelanggan yang Kaya
Perusahaan ini memiliki akses ke basis data pelanggan yang luas dan kaya, mencakup variabel seperti usia, jenis perangkat, riwayat penelusuran, serta preferensi waktu pengguna saat mengakses platform. Data ini adalah aset berharga yang dapat digunakan untuk mengembangkan model prediktif guna mengidentifikasi pelanggan yang kemungkinan besar akan mengklik iklan tertentu.

### 3. Perusahaan yang Berfokus pada Keunggulan Kompetitif
Dengan kompetisi yang ketat di pasar periklanan digital, perusahaan ini berfokus untuk membangun keunggulan kompetitif dengan memanfaatkan teknik prediktif yang canggih. Analisis prediktif dan machine learning membantu perusahaan mengoptimalkan kampanye iklan mereka, menawarkan iklan yang lebih relevan kepada calon pelanggan, serta memaksimalkan efisiensi anggaran pemasaran.

Dengan memahami karakteristik bisnis perusahaan periklanan digital ini, proyek prediksi klik iklan dapat dirancang untuk memenuhi kebutuhan dan tujuan bisnis yang spesifik, serta memberikan manfaat berikut:

#### a. Penargetan Iklan yang Lebih Akurat
Dengan menggunakan model prediktif, perusahaan dapat menargetkan pelanggan yang lebih mungkin untuk mengklik iklan, berdasarkan faktor-faktor yang relevan seperti waktu akses, jenis perangkat, dan riwayat penelusuran. Model ini memungkinkan perusahaan untuk menentukan kampanye yang lebih tepat sasaran, meningkatkan ROI iklan, dan menghindari pemborosan pada iklan yang kurang efektif.

#### b. Peningkatan Efisiensi dan Produktivitas
Penggunaan teknologi analisis prediktif memungkinkan perusahaan untuk memproses data pengguna secara otomatis, memprediksi klik iklan dengan lebih cepat, dan mengurangi waktu serta upaya yang dibutuhkan dalam analisis manual. Dengan model prediktif, proses penentuan target kampanye dapat diotomatisasi sehingga tim pemasaran dapat fokus pada strategi lain untuk meningkatkan jangkauan dan kualitas iklan.

#### c. Pengambilan Keputusan yang Lebih Informasional
Model prediktif memberikan wawasan lebih mendalam tentang faktor-faktor yang memengaruhi klik iklan, membantu perusahaan memahami pola perilaku pengguna dan mengidentifikasi tren yang signifikan. Informasi ini memungkinkan perusahaan untuk mengembangkan kampanye yang lebih informatif, serta memberikan penawaran yang lebih relevan bagi pengguna yang berbeda karakteristiknya.

#### d. Keunggulan Kompetitif di Pasar Periklanan Digital
Dengan memanfaatkan model prediktif yang canggih, perusahaan dapat membangun keunggulan kompetitif melalui kampanye yang lebih terukur dan relevan bagi calon pelanggan. Dengan meningkatkan akurasi penargetan dan menyediakan iklan yang lebih menarik, perusahaan ini dapat menarik lebih banyak calon pelanggan dan mempertahankan pelanggan saat ini, memperluas pangsa pasar serta membedakan diri dari pesaing.

Dengan demikian, proyek prediksi klik iklan ini dapat membantu perusahaan membuat keputusan bisnis yang lebih baik, meningkatkan efisiensi operasional, dan mencapai keunggulan kompetitif di pasar periklanan digital.

### Problem Statement
#### a. Bagaimana langkah yang dapat diambil untuk meningkatkan akurasi dalam memprediksi klik iklan?
Perusahaan periklanan menghadapi tantangan dalam memastikan iklan yang mereka tampilkan efektif dan menjangkau audiens yang tepat. Hal ini disebabkan oleh keterbatasan dalam memahami faktor-faktor yang memengaruhi kemungkinan seseorang untuk mengklik iklan.

Dalam proyek ini, kami akan mengatasi masalah ini dengan mengembangkan model analisis prediktif yang dapat memperkirakan peluang klik iklan dengan akurasi lebih tinggi, sehingga memungkinkan perusahaan untuk meningkatkan efektivitas iklan dan memaksimalkan ROI dari kampanye iklan mereka.

#### b. Bagaimana caranya untuk meningkatkan relevansi dan personalisasi iklan bagi calon pelanggan?
Banyak pengguna merasa bahwa iklan yang mereka lihat kurang relevan atau tidak sesuai dengan minat mereka, yang mengurangi kemungkinan klik dan interaksi.

Dalam proyek ini, kami akan meningkatkan relevansi dan personalisasi iklan dengan mengidentifikasi faktor-faktor yang paling berpengaruh dalam menentukan minat pengguna terhadap suatu iklan. Hal ini akan membantu perusahaan untuk menyajikan iklan yang lebih sesuai dengan preferensi individu, meningkatkan engagement, dan menciptakan pengalaman pengguna yang lebih positif.

#### c. Bagaimana risiko pemborosan anggaran iklan dapat dikurangi?
Anggaran iklan yang tidak dikelola dengan baik dapat menyebabkan pemborosan. Jika iklan ditampilkan kepada audiens yang tidak tertarik, ini dapat meningkatkan biaya tanpa menghasilkan klik atau konversi yang diinginkan.

Dalam proyek ini, kami akan membantu mengurangi risiko pemborosan anggaran dengan menggunakan model prediktif yang lebih akurat, sehingga perusahaan dapat menargetkan iklan kepada audiens yang paling berpotensi untuk berinteraksi, menghasilkan konversi, dan memaksimalkan efektivitas anggaran pemasaran.

Dalam konteks prediksi klik iklan, berikut adalah contoh konkret dari faktor-faktor spesifik yang sering menyebabkan masalah-masalah yang disebutkan sebelumnya:

1. Kurangnya akurasi dalam memprediksi klik iklan:

Masalah: Sulitnya memahami faktor-faktor yang berkontribusi terhadap minat pengguna dalam mengklik iklan, seperti jenis perangkat, waktu akses, dan riwayat penelusuran.
Contoh: Seorang pengguna yang sering mengakses media sosial pada malam hari mungkin memiliki pola perilaku yang berbeda dari pengguna di pagi hari, sehingga model prediktif harus mampu menangkap perbedaan ini untuk meningkatkan akurasi prediksi klik.

2. Kurangnya relevansi iklan bagi calon pelanggan:

Masalah: Banyak calon pelanggan merasa bahwa iklan yang ditampilkan tidak sesuai dengan minat atau kebutuhan mereka.
Contoh: Pengguna yang lebih sering mencari produk teknologi akan merasa iklan gadget atau aksesoris teknologi lebih relevan daripada iklan produk yang tidak mereka minati. Faktor seperti riwayat penelusuran dan kategori produk favorit dapat dimanfaatkan untuk meningkatkan relevansi iklan.

3. Risiko pemborosan anggaran iklan:

Masalah: Menargetkan iklan kepada audiens yang kurang tertarik meningkatkan biaya periklanan tanpa adanya konversi yang berarti.
Contoh: Jika perusahaan terus menampilkan iklan kepada pengguna yang jarang atau tidak pernah mengklik, biaya iklan akan meningkat tanpa hasil yang diharapkan, menyebabkan kerugian finansial.
Dalam proyek "Click Prediction for Ads", faktor-faktor ini akan dianalisis secara komprehensif dan dimasukkan ke dalam model prediktif.

Dengan memanfaatkan teknik machine learning, model ini akan menghasilkan perkiraan klik iklan yang lebih akurat berdasarkan faktor-faktor relevan yang mempengaruhi perilaku pengguna. Selain itu, dengan mengidentifikasi variabel yang paling signifikan dalam prediksi klik, perusahaan dapat menyusun strategi periklanan yang lebih efektif, relevan, dan transparan, menciptakan pengalaman pengguna yang lebih personal serta mengurangi pemborosan anggaran.

### Tujuan Proyek
Tujuan proyek prediksi klik iklan ini adalah sebagai berikut:

Mengembangkan model analisis prediktif untuk prediksi klik iklan:
Tujuan utama proyek ini adalah mengembangkan model analisis prediktif yang dapat memperkirakan kemungkinan klik iklan dengan tingkat akurasi tinggi. Dengan melakukan analisis data yang komprehensif dan memanfaatkan teknik machine learning, model ini bertujuan untuk memberikan prediksi klik yang lebih tepat, memungkinkan perusahaan untuk meningkatkan efektivitas dan ROI dari kampanye iklan mereka.

Meningkatkan relevansi dan personalisasi iklan:
Proyek ini bertujuan untuk meningkatkan relevansi dan personalisasi iklan bagi audiens. Dengan mengidentifikasi faktor-faktor yang paling signifikan dalam mempengaruhi minat pengguna terhadap iklan, model ini dapat membantu perusahaan menyajikan iklan yang lebih sesuai dengan preferensi individu, meningkatkan engagement pengguna, dan menciptakan pengalaman yang lebih positif.

Mengoptimalkan penggunaan anggaran iklan:
Salah satu tujuan proyek ini adalah membantu perusahaan mengelola anggaran iklan secara lebih efektif dengan mengurangi pemborosan pada target yang tidak potensial. Dengan prediksi klik yang lebih akurat, perusahaan dapat menargetkan iklan kepada audiens yang lebih tepat, memaksimalkan konversi, dan menjaga efisiensi anggaran iklan.

Metrik evaluasi yang akan digunakan untuk mengukur keberhasilan proyek ini dalam mencapai setiap tujuan meliputi:

Akurasi prediksi klik:
Metrik ini digunakan untuk mengukur sejauh mana model dapat memprediksi klik iklan dengan tepat. Akurasi prediksi yang tinggi menunjukkan bahwa model memberikan perkiraan yang andal, sehingga mendukung tujuan pertama.

Tingkat relevansi iklan:
Metrik ini dapat diukur melalui tingkat keterlibatan pengguna (seperti click-through rate) untuk melihat sejauh mana pengguna merasa iklan yang ditampilkan relevan dengan minat mereka. Semakin tinggi tingkat keterlibatan, semakin tinggi relevansi dan personalisasi yang berhasil dicapai.

Efisiensi anggaran iklan:
Metrik ini dapat diukur dengan membandingkan pengeluaran iklan dan hasil konversi sebelum dan sesudah penerapan model prediktif. Jika model membantu mengurangi pemborosan anggaran, maka tujuan ketiga tercapai.

### Solution Statement

Solusi yang diberikan untuk proyek prediksi klik iklan ini melibatkan beberapa tahapan dan algoritma yang digunakan. Berikut adalah penjelasan yang lebih rinci mengenai solusi yang direncanakan:

1. Eksplorasi Data (Exploratory Data Analysis - EDA)
Sebelum melatih model, proses EDA akan dilakukan untuk memahami karakteristik data iklan dan pengguna. EDA ini bertujuan untuk mengidentifikasi pola, menemukan korelasi antar variabel (seperti usia pengguna, waktu tayang iklan, atau jenis iklan), serta memperoleh wawasan yang berguna dalam memprediksi kemungkinan klik iklan.

2. Algoritma KNN (K-Nearest Neighbors), Random Forest, dan XGBoost
Tiga algoritma utama dipilih untuk proyek ini:

K-Nearest Neighbors (KNN): Algoritma ini akan digunakan untuk memprediksi kemungkinan klik iklan berdasarkan kemiripan karakteristik pengguna yang ada di data. KNN dapat membantu dalam menangkap pola dengan pendekatan jarak antar data yang mirip.

Random Forest: Algoritma ensemble ini memanfaatkan beberapa pohon keputusan untuk menghasilkan prediksi yang lebih stabil dan akurat. Random Forest sangat berguna dalam menangani data yang kompleks serta membantu mengidentifikasi variabel paling berpengaruh dalam prediksi klik iklan.

XGBoost (Extreme Gradient Boosting): XGBoost adalah algoritma boosting yang dapat menghasilkan model prediksi yang kuat dan efisien. Algoritma ini akan digunakan untuk memaksimalkan akurasi prediksi dengan memanfaatkan teknik boosting untuk memperbaiki kesalahan pada prediksi sebelumnya.

3. Evaluasi dengan Metrik Akurasi, Precision, Recall, dan MSE (Mean Squared Error)
Beberapa metrik evaluasi utama yang akan digunakan adalah:

Akurasi: Digunakan untuk mengukur persentase prediksi yang benar oleh model, memastikan bahwa model dapat mengidentifikasi klik iklan dengan tepat.

Precision dan Recall: Untuk mengukur sejauh mana model mampu memprediksi klik iklan secara benar tanpa terlalu banyak kesalahan atau melewatkan kemungkinan klik yang sebenarnya.

Mean Squared Error (MSE): MSE akan digunakan untuk menghitung kesalahan rata-rata kuadrat antara nilai prediksi dan nilai sebenarnya, khususnya untuk memastikan bahwa model tidak terlalu jauh meleset dalam prediksinya.

4. Eksperimen dan Optimasi Model
Setiap model akan diuji menggunakan metrik evaluasi tersebut, dan optimasi hyperparameter akan dilakukan secara manual atau dengan teknik seperti Grid Search atau Random Search. Melalui pendekatan eksperimen ini, performa setiap algoritma akan dibandingkan untuk menentukan model terbaik dalam memprediksi klik iklan.

Dengan pendekatan ini, solusi diharapkan dapat memenuhi tujuan proyek untuk mengembangkan model prediksi klik iklan yang akurat, membantu perusahaan mengoptimalkan strategi iklan, dan meningkatkan efektivitas kampanye marketing mereka.

## 3. Data Understanding
### Tentang dataset
dataset diunduh dari : [LINK DATASET](https://www.kaggle.com/datasets/marius2303/ad-click-prediction-dataset)
Kumpulan data ini memberikan wawasan tentang perilaku pengguna dan iklan daring, khususnya berfokus pada prediksi apakah pengguna akan mengeklik iklan daring. Kumpulan data ini berisi informasi demografi pengguna, kebiasaan menjelajah, dan detail terkait tampilan iklan.
Kumpulan data ini ideal untuk membangun model klasifikasi biner guna memprediksi interaksi pengguna dengan iklan daring.

#### a. Informasi Dataset
- Jumlah total baris (data): 8,337
- Jumlah total kolom (fitur): 9
- Kolom target: click (menunjukkan apakah iklan di-klik atau tidak, dengan nilai integer 1 atau 0)

Deskripsi Setiap Kolom
id (int64):

ID unik untuk setiap entri atau pengguna. Kolom ini mungkin tidak relevan untuk analisis karena hanya digunakan sebagai pengidentifikasi.
full_name (object):

Nama lengkap pengguna. Kolom ini mungkin hanya berfungsi sebagai informasi tambahan dan dapat dihapus untuk analisis prediksi, karena nama pengguna biasanya tidak memiliki korelasi dengan kemungkinan klik iklan.
age (float64):

Usia pengguna. Hanya ada 4,458 non-null dari total 8,337 data, menunjukkan bahwa sekitar 47% data tidak memiliki informasi usia.
gender (object):

Jenis kelamin pengguna, dengan hanya 3,644 non-null data, sehingga sekitar 56% data tidak memiliki informasi gender.
device_type (object):

Jenis perangkat yang digunakan pengguna untuk browsing (misalnya, mobile, desktop). Terdapat 6,674 non-null data, dengan sekitar 20% data yang kosong di kolom ini.
ad_position (object):

Posisi iklan pada halaman (misalnya, header, sidebar, footer). Terdapat 6,683 non-null data, sehingga sekitar 20% data lainnya kosong.
browsing_history (object):

Riwayat browsing pengguna, yang dapat menunjukkan minat atau kebiasaan pengguna dalam mengunjungi situs tertentu. Hanya ada 4,329 non-null data, dengan sekitar 48% data yang kosong, sehingga mungkin perlu dipertimbangkan untuk imputasi atau penanganan lain.
time_of_day (object):

Waktu dalam hari saat iklan ditampilkan (misalnya pagi, siang, malam). Hanya ada 6,672 non-null data, dengan sekitar 20% data yang kosong.
click (int64):

Kolom target yang menunjukkan apakah iklan di-klik atau tidak (dengan nilai 1 untuk klik dan 0 untuk tidak klik). Kolom ini lengkap dengan 8,337 non-null data.

Analisis Missing Values
Dataset ini memiliki sejumlah nilai kosong di beberapa kolom, terutama di age, gender, dan browsing_history, yang dapat berdampak pada hasil prediksi. Perlu dilakukan strategi untuk menangani missing values, misalnya dengan mengimputasi nilai median untuk kolom numerik (age) atau kategori terbanyak untuk kolom kategorikal (device_type, ad_position, dll.).

### Fitur

- id: Pengidentifikasi unik untuk setiap pengguna.
- full_name: Nama pengguna diformat sebagai "UserX" untuk anonimitas.
- age: Usia pengguna (berkisar antara 18 hingga 64 tahun).
- gender: Jenis kelamin pengguna (dikategorikan sebagai Pria, Wanita, atau Non-Biner).
- device_type: Jenis perangkat yang digunakan pengguna saat melihat iklan (Seluler, Desktop, Tablet).
- ad_position: Posisi iklan di halaman web (Atas, Samping, Bawah).
- browsing_history: Aktivitas penjelajahan pengguna sebelum melihat iklan (Belanja, Berita, Hiburan, Pendidikan, Media Sosial).
- time_of_day: Waktu saat pengguna melihat iklan (Pagi, Siang, Sore, Malam).
- click: Label target yang menunjukkan apakah pengguna mengklik iklan (1 untuk klik, 0 untuk tidak mengklik).

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

## 7. Source
1. Understanding Ads Click-Through Rate Prediction with Machine Learning from Medium [LINK](https://medium.com/@varun.tyagi83/understanding-ads-click-through-rate-prediction-with-machine-learning-9ee1e637203c)
2. Research Gate : Difference of KNN, Random Forest, XGB [LINK](https://www.researchgate.net/post/What_is_the_difference_between_the_three_Machine_Learning_models)

## 8. Struktur Laporan
Laporan ini mengikuti format yang disarankan, dengan penjelasan yang diuraikan sesuai template, menyertakan kode snippet jika diperlukan untuk memudahkan pemahaman pembaca.

