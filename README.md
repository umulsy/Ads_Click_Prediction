# Laporan Proyek Machine Learning: Ads Click Prediction
## 1. Domain Proyek
### Latar Belakang
Dalam dunia periklanan digital, memahami perilaku pengguna saat mereka mengklik atau mengabaikan iklan adalah informasi penting bagi pengiklan untuk meningkatkan efektivitas kampanye. Prediksi klik iklan sangat penting untuk mengoptimalkan alokasi anggaran pemasaran dan meningkatkan konversi (Saraswati et al., 2019).
### Tujuan
Prediksi klik iklan memungkinkan perusahaan untuk:
Meningkatkan ROI iklan melalui penargetan yang lebih tepat.
Mengurangi pemborosan anggaran dengan mengurangi jumlah iklan yang ditayangkan pada audiens yang kurang berpotensi.
## 2. Business Understanding
Proyek ini dibuat berdasarkan karakteristik perusahaan iklan
#### 1. Perusahaan Periklanan Digital yang Berorientasi pada Analisis Data
Perusahaan ini sangat menekankan penggunaan analisis data untuk meningkatkan efektivitas kampanye iklan mereka. Dengan mengakui pentingnya analisis prediktif dan machine learning, mereka memiliki komitmen untuk mengoptimalkan setiap keputusan pemasaran digital. Prediksi klik iklan yang akurat memungkinkan perusahaan untuk menargetkan pelanggan potensial secara lebih efektif, meningkatkan konversi, serta mengelola anggaran iklan secara lebih efisien.
#### 2. Perusahaan dengan Basis Data Pelanggan yang Kaya
Perusahaan ini memiliki akses ke basis data pelanggan yang luas dan kaya, mencakup variabel seperti usia, jenis perangkat, riwayat penelusuran, serta preferensi waktu pengguna saat mengakses platform. Data ini adalah aset berharga yang dapat digunakan untuk mengembangkan model prediktif guna mengidentifikasi pelanggan yang kemungkinan besar akan mengklik iklan tertentu.
#### 3. Perusahaan yang Berfokus pada Keunggulan Kompetitif
Dengan kompetisi yang ketat di pasar periklanan digital, perusahaan ini berfokus untuk membangun keunggulan kompetitif dengan memanfaatkan teknik prediktif yang canggih. Analisis prediktif dan machine learning membantu perusahaan mengoptimalkan kampanye iklan mereka, menawarkan iklan yang lebih relevan kepada calon pelanggan, serta memaksimalkan efisiensi anggaran pemasaran.
Dengan memahami karakteristik bisnis perusahaan periklanan digital ini, proyek prediksi klik iklan dapat dirancang untuk memenuhi kebutuhan dan tujuan bisnis yang spesifik, serta memberikan manfaat berikut:
a. Penargetan Iklan yang Lebih Akurat
Dengan menggunakan model prediktif, perusahaan dapat menargetkan pelanggan yang lebih mungkin untuk mengklik iklan, berdasarkan faktor-faktor yang relevan seperti waktu akses, jenis perangkat, dan riwayat penelusuran. Model ini memungkinkan perusahaan untuk menentukan kampanye yang lebih tepat sasaran, meningkatkan ROI iklan, dan menghindari pemborosan pada iklan yang kurang efektif.
b. Peningkatan Efisiensi dan Produktivitas
Penggunaan teknologi analisis prediktif memungkinkan perusahaan untuk memproses data pengguna secara otomatis, memprediksi klik iklan dengan lebih cepat, dan mengurangi waktu serta upaya yang dibutuhkan dalam analisis manual. Dengan model prediktif, proses penentuan target kampanye dapat diotomatisasi sehingga tim pemasaran dapat fokus pada strategi lain untuk meningkatkan jangkauan dan kualitas iklan.
c. Pengambilan Keputusan yang Lebih Informasional
Model prediktif memberikan wawasan lebih mendalam tentang faktor-faktor yang memengaruhi klik iklan, membantu perusahaan memahami pola perilaku pengguna dan mengidentifikasi tren yang signifikan. Informasi ini memungkinkan perusahaan untuk mengembangkan kampanye yang lebih informatif, serta memberikan penawaran yang lebih relevan bagi pengguna yang berbeda karakteristiknya.
d. Keunggulan Kompetitif di Pasar Periklanan Digital
Dengan memanfaatkan model prediktif yang canggih, perusahaan dapat membangun keunggulan kompetitif melalui kampanye yang lebih terukur dan relevan bagi calon pelanggan. Dengan meningkatkan akurasi penargetan dan menyediakan iklan yang lebih menarik, perusahaan ini dapat menarik lebih banyak calon pelanggan dan mempertahankan pelanggan saat ini, memperluas pangsa pasar serta membedakan diri dari pesaing.
Dengan demikian, proyek prediksi klik iklan ini dapat membantu perusahaan membuat keputusan bisnis yang lebih baik, meningkatkan efisiensi operasional, dan mencapai keunggulan kompetitif di pasar periklanan digital(Chieh-jen et al.2016),.
## 3. Problem Statement
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
Kurangnya akurasi dalam memprediksi klik iklan:
Masalah: Sulitnya memahami faktor-faktor yang berkontribusi terhadap minat pengguna dalam mengklik iklan, seperti jenis perangkat, waktu akses, dan riwayat penelusuran. Contoh: Seorang pengguna yang sering mengakses media sosial pada malam hari mungkin memiliki pola perilaku yang berbeda dari pengguna di pagi hari, sehingga model prediktif harus mampu menangkap perbedaan ini untuk meningkatkan akurasi prediksi klik.
Kurangnya relevansi iklan bagi calon pelanggan:
Masalah: Banyak calon pelanggan merasa bahwa iklan yang ditampilkan tidak sesuai dengan minat atau kebutuhan mereka. Contoh: Pengguna yang lebih sering mencari produk teknologi akan merasa iklan gadget atau aksesoris teknologi lebih relevan daripada iklan produk yang tidak mereka minati. Faktor seperti riwayat penelusuran dan kategori produk favorit dapat dimanfaatkan untuk meningkatkan relevansi iklan.
Risiko pemborosan anggaran iklan:
Masalah: Menargetkan iklan kepada audiens yang kurang tertarik meningkatkan biaya periklanan tanpa adanya konversi yang berarti. Contoh: Jika perusahaan terus menampilkan iklan kepada pengguna yang jarang atau tidak pernah mengklik, biaya iklan akan meningkat tanpa hasil yang diharapkan, menyebabkan kerugian finansial. Dalam proyek "Click Prediction for Ads", faktor-faktor ini akan dianalisis secara komprehensif dan dimasukkan ke dalam model prediktif.

Dengan memanfaatkan teknik machine learning, model ini akan menghasilkan perkiraan klik iklan yang lebih akurat berdasarkan faktor-faktor relevan yang mempengaruhi perilaku pengguna. Selain itu, dengan mengidentifikasi variabel yang paling signifikan dalam prediksi klik, perusahaan dapat menyusun strategi periklanan yang lebih efektif, relevan, dan transparan, menciptakan pengalaman pengguna yang lebih personal serta mengurangi pemborosan anggaran.

## 4. Tujuan Proyek
Tujuan proyek prediksi klik iklan ini adalah sebagai berikut:
1) Mengembangkan model analisis prediktif untuk prediksi klik iklan: 
Tujuan utama proyek ini adalah mengembangkan model analisis prediktif yang dapat memperkirakan kemungkinan klik iklan dengan tingkat akurasi tinggi. Dengan melakukan analisis data yang komprehensif dan memanfaatkan teknik machine learning, model ini bertujuan untuk memberikan prediksi klik yang lebih tepat, memungkinkan perusahaan untuk meningkatkan efektivitas dan ROI dari kampanye iklan mereka.
2) Meningkatkan relevansi dan personalisasi iklan:
Proyek ini bertujuan untuk meningkatkan relevansi dan personalisasi iklan bagi audiens. Dengan mengidentifikasi faktor-faktor yang paling signifikan dalam mempengaruhi minat pengguna terhadap iklan, model ini dapat membantu perusahaan menyajikan iklan yang lebih sesuai dengan preferensi individu, meningkatkan engagement pengguna, dan menciptakan pengalaman yang lebih positif.
3) Mengoptimalkan penggunaan anggaran iklan: Salah satu tujuan proyek ini adalah membantu perusahaan mengelola anggaran iklan secara lebih efektif dengan mengurangi pemborosan pada target yang tidak potensial. Dengan prediksi klik yang lebih akurat, perusahaan dapat menargetkan iklan kepada audiens yang lebih tepat, memaksimalkan konversi, dan menjaga efisiensi anggaran iklan.

Metrik evaluasi yang akan digunakan untuk mengukur keberhasilan proyek ini dalam mencapai setiap tujuan meliputi:
- Akurasi prediksi klik: Metrik ini digunakan untuk mengukur sejauh mana model dapat memprediksi klik iklan dengan tepat. Akurasi prediksi yang tinggi menunjukkan bahwa model memberikan perkiraan yang andal, sehingga mendukung tujuan pertama.
- Tingkat relevansi iklan: Metrik ini dapat diukur melalui tingkat keterlibatan pengguna (seperti click-through rate) untuk melihat sejauh mana pengguna merasa iklan yang ditampilkan relevan dengan minat mereka. Semakin tinggi tingkat keterlibatan, semakin tinggi relevansi dan personalisasi yang berhasil dicapai.
- Efisiensi anggaran iklan: Metrik ini dapat diukur dengan membandingkan pengeluaran iklan dan hasil konversi sebelum dan sesudah penerapan model prediktif. Jika model membantu mengurangi pemborosan anggaran, maka tujuan ketiga tercapai.
  
## 5. Solution Statement
Solusi yang diberikan untuk proyek prediksi klik iklan ini melibatkan beberapa tahapan dan algoritma yang digunakan. 
Berikut adalah penjelasan yang lebih rinci mengenai solusi yang direncanakan:
Eksplorasi Data (Exploratory Data Analysis - EDA) Sebelum melatih model, proses EDA akan dilakukan untuk memahami karakteristik data iklan dan pengguna. EDA ini bertujuan untuk mengidentifikasi pola, menemukan korelasi antar variabel (seperti usia pengguna, waktu tayang iklan, atau jenis iklan), serta memperoleh wawasan yang berguna dalam memprediksi kemungkinan klik iklan.

Tiga algoritma utama dipilih untuk proyek ini:
- K-Nearest Neighbors (KNN): Algoritma ini akan digunakan untuk memprediksi kemungkinan klik iklan berdasarkan kemiripan karakteristik pengguna yang ada di data. KNN dapat membantu dalam menangkap pola dengan pendekatan jarak antar data yang mirip.
- Random Forest: Algoritma ensemble ini memanfaatkan beberapa pohon keputusan untuk menghasilkan prediksi yang lebih stabil dan akurat. Random Forest sangat berguna dalam menangani data yang kompleks serta membantu mengidentifikasi variabel paling berpengaruh dalam prediksi klik iklan.
- XGBoost (Extreme Gradient Boosting): XGBoost adalah algoritma boosting yang dapat menghasilkan model prediksi yang kuat dan efisien. Algoritma ini akan digunakan untuk memaksimalkan akurasi prediksi dengan memanfaatkan teknik boosting untuk memperbaiki kesalahan pada prediksi sebelumnya.

Evaluasi dengan Metrik Akurasi, Precision, Recall, dan MSE (Mean Squared Error) Beberapa metrik evaluasi utama yang akan digunakan adalah:
- Akurasi: Digunakan untuk mengukur persentase prediksi yang benar oleh model, memastikan bahwa model dapat mengidentifikasi klik iklan dengan tepat.
- Precision dan Recall: Untuk mengukur sejauh mana model mampu memprediksi klik iklan secara benar tanpa terlalu banyak kesalahan atau melewatkan kemungkinan klik yang sebenarnya.
- Mean Squared Error (MSE): MSE akan digunakan untuk menghitung kesalahan rata-rata kuadrat antara nilai prediksi dan nilai sebenarnya, khususnya untuk memastikan bahwa model tidak terlalu jauh meleset dalam prediksinya.
Esperimen dan Optimasi Model Setiap model akan diuji menggunakan metrik evaluasi tersebut, dan optimasi hyperparameter akan dilakukan secara manual atau dengan teknik seperti Grid Search atau Random Search. Melalui pendekatan eksperimen ini, performa setiap algoritma akan dibandingkan untuk menentukan model terbaik dalam memprediksi klik iklan.

## 6. Data Understanding
Tentang dataset
dataset diunduh dari : [LINK](https://www.kaggle.com/datasets/marius2303/ad-click-prediction-dataset)
Kumpulan data ini memberikan wawasan tentang perilaku pengguna dan iklan daring, khususnya berfokus pada prediksi apakah pengguna akan mengeklik iklan daring. Kumpulan data ini berisi informasi demografi pengguna, kebiasaan menjelajah, dan detail terkait tampilan iklan. Kumpulan data ini ideal untuk membangun model klasifikasi biner guna memprediksi interaksi pengguna dengan iklan daring.
a. Informasi Dataset
- Jumlah total baris (data): 8,337
- Jumlah total kolom (fitur): 9
- Kolom target: click (menunjukkan apakah iklan di-klik atau tidak, dengan nilai integer 1 atau 0)
- Deskripsi Setiap Kolom id (int64):
  ID unik untuk setiap entri atau pengguna. Kolom ini mungkin tidak relevan untuk analisis karena hanya digunakan sebagai pengidentifikasi. 
  full_name (object): Nama lengkap pengguna. Kolom ini mungkin hanya berfungsi sebagai informasi tambahan dan dapat dihapus untuk analisis prediksi, karena nama pengguna   
  biasanya tidak memiliki korelasi dengan kemungkinan klik iklan. 
  age (float64): Usia pengguna. Hanya ada 4,458 non-null dari total 8,337 data, menunjukkan bahwa sekitar 47% data tidak memiliki informasi usia.
  gender (object): Jenis kelamin pengguna, dengan hanya 3,644 non-null data, sehingga sekitar 56% data tidak memiliki informasi gender. 
  device_type (object): Jenis perangkat yang digunakan pengguna untuk browsing (misalnya, mobile, desktop). Terdapat 6,674 non-null data, dengan sekitar 20% data yang 
  kosong di kolom ini. 
  ad_position (object): Posisi iklan pada halaman (misalnya, header, sidebar, footer). Terdapat 6,683 non-null data, sehingga sekitar 20% data lainnya kosong. 
  browsing_history (object): Riwayat browsing pengguna, yang dapat menunjukkan minat atau kebiasaan pengguna dalam mengunjungi situs tertentu. Hanya ada 4,329 non-null 
  data, dengan sekitar 48% data yang kosong, sehingga mungkin perlu dipertimbangkan untuk imputasi atau penanganan lain. 
  time_of_day (object): Waktu dalam hari saat iklan ditampilkan (misalnya pagi, siang, malam). Hanya ada 6,672 non-null data, dengan sekitar 20% data yang kosong.
  click (int64): Kolom target yang menunjukkan apakah iklan di-klik atau tidak (dengan nilai 1 untuk klik dan 0 untuk tidak klik). Kolom ini lengkap dengan 8,337 non-null 
  data.
  

Analisis Missing Values Dataset ini memiliki sejumlah nilai kosong di beberapa kolom, terutama di age, gender, dan browsing_history, yang dapat berdampak pada hasil prediksi. Perlu dilakukan strategi untuk menangani missing values, misalnya dengan mengimputasi nilai median untuk kolom numerik (age) atau kategori terbanyak untuk kolom kategorikal (device_type, ad_position, dll.).
#### Fitur
- id: Pengidentifikasi unik untuk setiap pengguna.
- full_name: Nama pengguna diformat sebagai "UserX" untuk anonimitas.
- age: Usia pengguna (berkisar antara 18 hingga 64 tahun).
- gender: Jenis kelamin pengguna (dikategorikan sebagai Pria, Wanita, atau Non-Biner).
- device_type: Jenis perangkat yang digunakan pengguna saat melihat iklan (Seluler, Desktop, Tablet).
- ad_position: Posisi iklan di halaman web (Atas, Samping, Bawah).
- browsing_history: Aktivitas penjelajahan pengguna sebelum melihat iklan (Belanja, Berita, Hiburan, Pendidikan, Media Sosial).
- time_of_day: Waktu saat pengguna melihat iklan (Pagi, Siang, Sore, Malam).
- click: Label target yang menunjukkan apakah pengguna mengklik iklan (1 untuk klik, 0 untuk tidak mengklik).


Visualisasi Proses EDA
plot nilai missing value
![Screenshot 2024-11-15 084742](https://github.com/user-attachments/assets/ea6ecd89-2b98-4dda-a9e1-88f6e406dba4)

Jumlah click masing-masing user. Terlihat bahwa pengguna baru lebih banyak mengklik

![Screenshot 2024-11-15 084409](https://github.com/user-attachments/assets/0f88c0c2-4b47-4f21-8a20-f5c8329da01a)

Rentang usia yang mengklik iklan dan tertarik pada iklan

![Screenshot 2024-11-15 085223](https://github.com/user-attachments/assets/34997b66-00a3-4403-bd56-42e7ff83d2a2)

Persentase posisi iklan yang banyak diklik. Posisi iklan paling banyak diklik ada pada posisi bawah

![Screenshot 2024-11-15 085457](https://github.com/user-attachments/assets/7cbe600f-4e1e-43b5-a81e-c237270c2823)

Prediksi iklan berdasarkan device type dan posisi iklan. Masing-masing device type memiliki posisi iklan yang paling banyak diklik masing-masing
![Screenshot 2024-11-15 091556](https://github.com/user-attachments/assets/dc2394bf-e970-43f7-8d7e-95efc9f4db4a)

## 7. Data Preparation
Dalam proses persiapan data untuk proyek prediksi klik iklan, berikut adalah teknik yang digunakan:

### Handling Missing value
Terdapat beberapa missing value dalam data, dalam project ini saya mengatasinya dengan cara mengisi kolom null dengan ‘Unknown’ untuk menghindari imbalance data. Pengisian kolom null dengan mean, median, mode tidak dilakukan untuk mencegah analisis berlebihan terhadap data asli sekaligus mempertahankan informasi yang dibawa oleh nilai yang hilang.Selain itu, pendekatan ini membantu mengurangi bias model dan mengurangi risiko overfitting.

### Handling duplicate data
Duplikasi data yang terjadi disebabkan oleh pengguna berulang, sehingga tidak dihapus agar dapat membuat kolom baru dengan mengidentifikasi melalui kolom tersebut.

### Feature Engineering 
Pada project ini, dibuat kolom baru untuk mengidentifikasi aktivitas klik iklan pengguna baru dan pengguna lama. Kolom dinamai sebagai user_type. Selain itu dibuat juga age_group untuk mengkategorikan rentang usia pengguna.

### One Hot Encoding pada Fitur Kategorikal
Pada dataset prediksi iklan, terdapat beberapa fitur kategorikal, seperti gender, device_type, ad_position, dan time_of_day, yang tidak dapat langsung digunakan dalam algoritma machine learning karena sebagian besar algoritma hanya bekerja dengan data numerik. Oleh karena itu, teknik One Hot Encoding digunakan untuk mengonversi variabel kategorikal ini ke dalam representasi numerik.
Library Pandas menyediakan fungsi pd.get_dummies(), yang memudahkan proses One Hot Encoding. Fungsi ini menghasilkan kolom-kolom baru yang mewakili setiap nilai unik dari fitur kategorikal. Misalnya, jika fitur device_type memiliki nilai unik seperti "Mobile", "Desktop", dan "Tablet," setelah One Hot Encoding, akan terbentuk kolom baru, yaitu device_type_Mobile, device_type_Desktop, dan device_type_Tablet. Jika suatu baris menunjukkan nilai "Mobile" pada fitur device_type, maka kolom device_type_Mobile akan bernilai 1, sementara kolom lainnya akan bernilai 0.

### Pembagian Dataset menjadi Data Training dan Data Testing
Pembagian dataset menjadi data training dan data testing sangat penting dalam pengembangan model prediksi iklan. Pembagian ini dilakukan untuk mengukur seberapa baik model dapat melakukan prediksi pada data yang belum pernah dilihat sebelumnya, serta menghindari masalah overfitting.
Data training (80% dari data) digunakan untuk melatih model sehingga model dapat mempelajari pola dari fitur yang diberikan.
Data testing (20% dari data) digunakan untuk mengevaluasi performa model setelah pelatihan, untuk mengukur seberapa baik model dapat memprediksi klik pada iklan di data baru.
Rasio 80:20 adalah aturan praktis yang umum dalam machine learning, memberikan keseimbangan yang baik antara data yang cukup untuk melatih model dan data yang cukup untuk menguji akurasi model. Rasio ini juga dapat disesuaikan tergantung pada ukuran dataset dan kebutuhan spesifik proyek.

## 8. Model Development
Dalam proyek prediksi klik iklan, model yang digunakan adalah K-Nearest Neighbors (KNN), Random Forest, dan XGBoost. Berikut adalah penjelasan konsep dan langkah-langkah yang diterapkan pada setiap algoritma dalam proses modeling (Martin et al., 2022):
### 1. K-Nearest Neighbors (KNN):
####Cara Kerja: KNN mengukur jarak antara titik data baru dan titik data training untuk menemukan "K" tetangga terdekat, lalu menentukan nilai kelas berdasarkan mayoritas kelas tetangga tersebut.
#### Kelebihan:
Mudah dipahami dan diterapkan, Tidak ada periode pelatihan; prediksi dibuat saat runtime, Berfungsi dengan baik untuk kumpulan data berukuran kecil hingga sedang.
#### Kekurangan:
Bisa memakan banyak komputasi untuk kumpulan data besar, Sensitif terhadap pilihan k dan metrik jarak, Tidak berfungsi dengan baik dengan data berdimensi tinggi.
#### Parameter model : KNeighborsClassifier(n_neighbors=10). Parameter ini menentukan jumlah tetangga terdekat yang digunakan dalam prediksi.

### 2. Random Forest:
#### Cara Kerja: 
Model ini melatih banyak pohon keputusan pada subset acak dari data, lalu menggabungkan prediksi dari setiap pohon untuk menghasilkan hasil akhir. Hal ini memberikan stabilitas dan akurasi yang lebih tinggi
#### Kelebihan:
-Memberikan akurasi dan generalisasi yang lebih baik dibandingkan dengan pohon keputusan individual, Menangani data berdimensi tinggi dengan baik, Mengurangi overfitting.
#### Kekurangan:
-Bisa lebih lambat untuk dilatih dibandingkan dengan pohon keputusan tunggal, Kurang dapat diinterpretasikan daripada pohon keputusan tunggal.
#### Parameter model : 
n_estimators=50, max_depth=16, random_state=50, n_jobs=-1
n_estimators=50: Jumlah random forest, di sini ada 50.
max_depth=16: Kedalaman maksimum tiap pohon dibatasi hingga 16 tingkat.
random_state=50: Menetapkan seed agar hasil model konsisten pada setiap run.
n_jobs=-1: Menggunakan semua CPU yang tersedia untuk mempercepat pemrosesan.

### 3. XGBoost (Peningkatan Gradien Ekstrim):
#### Cara kerja : 
Algoritma ini melatih model-model pohon keputusan secara bertahap, dengan model baru yang fokus pada kesalahan dari model sebelumnya, menghasilkan prediksi yang lebih akurat.
#### Kelebihan:
- Kinerja prediktif yang sangat baik; sering digunakan dalam kompetisi pembelajaran mesin.
- Penanganan kumpulan data besar secara efisien.
- teknik regularisasi untuk mencegah overfitting.
##### Kekurangan:
Memerlukan penyetelan hiperparameter.
Dapat menghabiskan banyak biaya komputasi untuk kumpulan data yang sangat besar.
Kurang dapat diinterpretasikan dibandingkan dengan model linier
#### Parameter model :
n_estimators=50, max_depth=16, random_state=55, n_jobs=-1. Untuk deskripsi hampir mirip random forest.


## 9. Evaluasi
Metrik Evaluasi Model: Akurasi Akurasi adalah salah satu metrik evaluasi yang umum digunakan untuk mengukur seberapa baik model dalam mengklasifikasikan data, khususnya dalam kasus klasifikasi biner seperti prediksi klik iklan (ya atau tidak). Akurasi dihitung sebagai persentase prediksi yang benar dari total prediksi yang dilakukan oleh model.

### Langkah-langkah untuk Menghitung Akurasi:
Persiapkan Data: Pisahkan dataset menjadi data latih (training) dan data uji (testing). Melatih Model: Gunakan data latih untuk melatih model menggunakan algoritma yang dipilih (KNN, Random Forest, XGBoost). Prediksi pada Data Uji: Gunakan model yang dilatih untuk memprediksi nilai pada data uji. Hitung Akurasi: Bandingkan prediksi dengan nilai aktual pada data uji, lalu hitung persentase prediksi yang benar. Hasil Evaluasi Model Setelah melatih dan menguji model dengan data latih dan uji, berikut adalah hasil evaluasi akurasi masing-masing model:
##### Model scores akurasi : 
{'KNN': 0.8866906474820144,
 'Random Forest': 0.9592326139088729,
 'XGBoost': 0.9382494004796164}

#### Penjelasan Hasil Evaluasi: 
- Akurasi KNN:Model KNN menunjukkan akurasi 83% pada data uji, yang berarti model ini dapat memprediksi klik iklan dengan cukup baik meskipun ada ruang untuk perbaikan lebih lanjut. KNN lebih sensitif terhadap data yang tidak terstandarisasi, sehingga normalisasi data dapat membantu meningkatkan kinerjanya.
- Akurasi Random Forest: Random Forest memberikan akurasi tertinggi, yaitu 96% pada data uji. Ini menunjukkan bahwa model ini sangat baik dalam memprediksi klik iklan dan mengklasifikasikan data dengan sangat akurat. Random Forest bekerja dengan baik karena mampu menangani fitur yang kompleks dan tidak linear.
- Akurasi XGBoost: XGBoost juga memberikan hasil yang sangat baik dengan akurasi 94% pada data uji. Model ini dikenal dengan kemampuannya untuk menangani data yang besar dan beragam serta memberikan prediksi yang lebih akurat dibandingkan banyak algoritma lainnya. Berikut perbandingan ketiga model 

![image](https://github.com/user-attachments/assets/b952ba67-7762-4010-a498-8cde92ccab02)


## 10. Kesimpulan Project
Proyek ini berhasil mengembangkan model prediksi iklan menggunakan model Random Forest yang memberikan tingkat akurasi tinggi dalam memperkirakan kemungkinan klik iklan, yaitu sebesar 96%, melebihi model KNN (83%) dan XGBoost (94%). Hasil evaluasi menunjukkan bahwa model Random Forest memberikan prediksi yang paling akurat pada data pelatihan dan uji dibandingkan dengan model lain.
### Manfaat bagi Platform Iklan:
#### Peningkatan Efisiensi Iklan:
Model prediksi berbasis Random Forest dapat membantu platform iklan menampilkan iklan yang lebih relevan kepada pengguna, meningkatkan kemungkinan klik dan konversi, serta memaksimalkan pendapatan dari setiap iklan.
#### Pengurangan Biaya Iklan: 
Dengan menargetkan iklan secara lebih presisi, pengiklan dapat mengurangi biaya yang dikeluarkan untuk iklan yang tidak relevan, sehingga meningkatkan efisiensi anggaran pemasaran mereka.
#### Transparansi dalam Proses Penayangan Iklan: 
Dengan memahami faktor-faktor signifikan yang memengaruhi prediksi klik iklan, platform dapat memberikan penjelasan yang lebih baik kepada pengiklan mengenai alasan di balik performa kampanye iklan, meningkatkan transparansi dan kepercayaan.

### Manfaat bagi Pengiklan:
#### ROI Lebih Tinggi: 
Dengan prediksi yang akurat tentang iklan mana yang lebih mungkin diklik, pengiklan dapat mengalokasikan anggaran mereka pada iklan yang paling efektif, sehingga meningkatkan return on investment (ROI).
#### Pemahaman yang Lebih Baik atas Preferensi Pengguna: 
Data prediktif dari model Random Forest membantu pengiklan lebih memahami karakteristik pengguna yang lebih cenderung tertarik pada iklan mereka, memungkinkan personalisasi lebih lanjut dalam strategi pemasaran.

### Langkah Tindak Lanjut:
- Implementasi Model: Model Random Forest yang telah dikembangkan dapat diimplementasikan oleh platform iklan untuk memperkuat mekanisme prediksi klik iklan secara real-time.
Peningkatan Data dan Pemeliharaan Model: Platform iklan dapat terus memperkaya data input untuk model dan melakukan pemeliharaan secara berkala untuk memastikan prediksi tetap akurat seiring perubahan tren pengguna.
- Evaluasi dan Peningkatan Berkelanjutan: Evaluasi rutin terhadap kinerja model dapat membantu dalam mengidentifikasi area perbaikan, seperti eksplorasi model lain yang mungkin memberikan akurasi lebih tinggi atau fitur tambahan yang dapat memperkuat prediksi.

Dengan langkah-langkah ini, platform iklan dapat memanfaatkan model prediksi ini untuk meningkatkan efektivitas kampanye iklan, mengoptimalkan pengeluaran iklan, dan memberikan pengalaman beriklan yang lebih baik bagi pengiklan serta relevansi lebih tinggi bagi pengguna.

## Source
Chieh-Jen Wang and Hsin-Hsi Chen , "Learning User Behaviors for Advertisements Click Prediction," National Taiwan University, Taiwan. 2016

D. Martin and S. S. Chai, "A Study on Performance Comparisons between KNN, Random Forest and XGBoost in Prediction of Landslide Susceptibility in Kota Kinabalu, Malaysia," 2022 IEEE 13th Control and System Graduate Research Colloquium (ICSGRC), Shah Alam, Malaysia, 2022.

S. Saraswathi et al, "Machine Learning Based Ad-click Prediction System " ISSN: 2249-8958 (Online), Volume-8 Issue-6, August 2019.



