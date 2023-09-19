Fathi Qushoyyi Ahimsa (NPM 2206082120) 
PBP C
README.md (Tugas 2 dan Tugas 3)
Tautan Deployment Adaptable	: https://pbp-inventory-list.adaptable.app/

# TUGAS 2
•	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.	Pertama-tama saya membuat sebuah folder bernama tugas2 pada direktori lokal di dalam laptop. Lalu dengan mengaktifkan virtual environment, saya melakukan instalasi Django dengan menambahkan berkas requirements.txt ke dalam direktori tugas2.
2.	Setelah itu, saya melakukan konfigurasi proyek dengan menambahkan nilai “*” pada variable ALLOWED_HOST agar semua orang dapat mengakses aplikasi
3.	Menjalankan perintah “django-admin startproject data_leaked_store” dan terbantuk folder tugas_inventory sebagai app dari proyek tugas2.
4.	Membuat aplikasi baru dengan perintah “python manage.py startapp main” dan mendaftarkan main ke dalam daftar aplikasi yang ada di dalam proyek
5.	Selanjutnya, saya merubah berkas model dengan menambahkan beberapa variable seperti name, amount, price, dan description. Lalu saya melakukan migrasi model
6.	Setelah itu, saya membuat fungsi untuk mengatur tampilan di dalam aplikasi main. Tampilan ini akan digunakan untukk membuat tampilan html 
7.	Membuat folder templates dalam direktori utama dan menambahkna file main.html yang akan berfungsi sebagai template tampilan website. File yang dibuat langsung memuat kode Django yang akan digunakan untuk menampilkan data, seperti name, class, dan npm
8.	Saya menambahkan file urls.py dalam direktori main yang berfungsi untuk me-return aplikasi main ke dalam peramban web ketika diakses 
9.	Selanjutnya, saya menambahkan rute url di dalam direktori proyek agar url aplikasi main dapat diakses di tingkat proyek
10. Mengubah konfigurasi pada unit test
11.	Membuat berkas gitignore dan inisiasi repository di dalam github 
12.	Melakukan push ke repository melalui command prompt
13. Melakukan deploy ke adaptable

•	Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](gambarMVT.png)

•	Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Dengan menggunakan virtual environment, kita ddapat menginstall package-package yang dibutuhkan dalam sebuah proyek tanpa mengganggu keseluruhan device yang sedang dipakai. Hal ini memudahkan apabila kita membuat berbagai proyek dengan versi package yang berbeda-beda
Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Akan tetapi, besar kemungkinan terjadi error karena setiap proyek diinstal dengan package yang berbeda-beda. Hal ini akan membuat versi package akan terus diperbarui sedangkan proyek yang telah dibuat menggunakan versi lama. Perbedaan ini membuat inkompatibilitas package ssehingga proyek tidak bisa dijalankan.

•	Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1.	MVC merupakan singkatan dari Model, View, Controller. Model merupakan komponen yang menerima data dari database dan menyalurkannya ke controller. Controller merupakan komponen penghubung view dan model, berfungsi untuk mendapatkan respons pengguna dan melakukan perubahan model sesuai dengan request. View merupakan tampilan visualiasi yang terlihat pada user. 
2.	MVT merupakan singkatan dari Model, View, dan Template. Sama dengan MVC, model dalam MVT berguna untuk berkomunikasi dengan database. Template berguna untuk mengelola tampilan aplikasi. View berguna untuk menyimpan action yang dilakukan oleh user dan memberikan/menyajikan tampilan aplikasi
3.	MVVM merupakan singkatan dari Model, View, dan ViewModel. ViewModel berguna untuk mengakomodasi pemrosesan yang dilakukan dari model ke view. View sendiri merupakan tampilan aplikasi dan berguna sebagai penyimpan input/action dari user. 
4.	Perbedaan dari Ketiganya terletak pada pengikatan data. MVC mempunyai mekanisme akses data yang saling terikat satu sama lain. Sedangkan model lain menggunakan komponen lain dalam saluran komunikasi dantara model dan view. MVT dan MVVM mempunyai referensi terhadap templates dan ViewModel. Sedangkan MVC tidak punya referensi/control terhadap controller. Pada MVT, view berperan untuk membuat template yang sesuai dengan permintaan. Sedangkan template pada MVT mempunyai fungsi yang mirip dengan view di dalam MVC. Selain itu, perbedaan ketiga bentuk desain system ini terletak pada kemudahan implementasi perubahan pada kode. MVT dan MVVM lebih mudah dalam melakukan perubahan dan mudah apabila kita ingin menaikkan skalabilitas. Selain itu, kerumitan juga  menjadi perbedaan, MVC mempunyai flow yang paling mudah dipahami. 


# TUGAS 3
•	Apa perbedaan antara form post dan form get pada Django?
Perbedaan antara kedua form tersebut terletak pada beberapa hal, antara lain metode HTTP yang digunakan, keamanan, pembaruan data, dan juga kapasitas data. Ketika kita menggunakan form POST, data di dalam form dikirimkan dalam bentuk HTTP yang tidak terlihat dalam url. Hal ini berguna Ketika kita mengirim data sensitive. Akan tetapi, ketika kita menggunakan form GET, data form disertakan dalam parameter query string. Hal tersebut menyebabkan keamanan form POST jauh lebih aman dibandingkan dengan form GET karena visibilitas dari bentuk HTTP yang tidak terlihat dalam url tadi. Selain itu, kapasitas pengiriman data untuk form POST juga jauh lebih besar daripada form GET yang dikirim melalui url. Dengan menggunakan form POST, kita juga bisa memperbarui atau menyimpan informasi di server, sedangkan form GET hanya bisa melakukan request pembacaan data tanpa bisa memodifikasi data yang ada.
•	Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
1.	XML (eXtensible Markup Language): biasa digunakan untuk menggambarkan struktur data dengan nama variable/tag yang sudah diatur sebelumnya. XML dapat digunakan untuk pertukaran data dan pemodelan data. Akan tetapi, kompleksitas XML sendiri jauh lebih kompleks dibandingkan dengan JSON dan HTML.
2.	JSON (Javascript Object Notation): JSON mempunyai format yang mudah dibaca oleh manusia dan sering digunakan dalam pertukaran data, khususnya pada website. JSON yang mempunyai format sederhana ini mendukung tipe data primitive dan sederhana, seperti string, Boolean, integer, dll. 
3.	HTML (HyperText Markup Language): HTML biasa digunakan sebagai template tampilan dan struktur halaman website. Dalam HTML, biasa digunakan tag markup yang dipakai untuk mendefinisikan elemen-elemen visual, seperti head, body, dan paragraph. HTML tidak digunakan untuk pertukaran data karena fungsi HTML lebih spesifik dengan tampilan dan interaksi dengan pengguna

•	Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Terdapat beberapa alasan JSON sering digunakan untuk pertukaran data antar web app. Pertama, JSON mempunyai visibilitas yang mudah dibaca oleh manusia sehingga mudah untuk mengatur, memahami, dan membuat struktur data yang terstruktur dengan baik untuk dikirimkan antar aplikasi. Kedua, JSON mempynyai kompatibilitas dengan Javascript yang memudahkan penggabungan implementasi kode aplikasi web yang dibangun dengan Javasccript. Ketiga, JSON dapat diproses oleh berbagai Bahasa pemrograman yang membuat berbagai programmer dapat mengakses dan menggunakan JSON secara luas. 

•	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
1.	Pertama-tama, kita perlu melakukan routing dari main ke/ agar sesuai dengan konvensi routing yang ada
2.	Selanjutnya kita perlu mengimplementasikan skeletaon dengan membuat berkas base.html pada root folder templates (perlu membuat folder baru). Base.html berfungsi untuk kerangka umum website. Selanjutnya, kita perlu menyesuaikan kode setting.py agar dapat membaca berkas base.html dengan menambahkan base pada kode TEMPLATES. Selain itu, kita perlu mengubah berkas main.html pada direktori main agar sesuai dengan template dari base yang telah kita buat tadi.
3.	Selanjutnya, kita perlu membuat form input. Form input dapat dibuat dengan membuat berkas forms.py pada direktori main. Kita perlu membuat function Bernama create_item untuk menghasilkan form yang dapat menambahkan data produk secara otomatis Ketika user menekan tombol submit (tombol submit kita representasikan dengan nama Add Item). Selain itu, kita perlu mengubah berkas views.py agar dapat membaca form item yang telah dibuat. Kita juga perlu melakukan routing ke dalam urlpatterns agar dapat mengakses function yang ada pada forms.py. 
4.	Setelah forms dan routing diatur, kita perlu menambahkan template dengan nama create_item.html untuk menampilkan fields form. Kita juga pelru untuk menambahkan kode {% block content %} pada berkas main.html
5.	Kita perlu membuat pengembalian data dalam bentuk XML dan JSON. Hal ini dapat dilakukan dengan membuat function dalam berkas views.py pada folder main agar variable di dalam function tersebut dapat menyimpan query data item dan dapat mereturn hasil query yang sudah ditransformasi menajdi JSON  dan XML. Selanjutnya kita dapat melakukan routing path url ke dalam urlpatterns untuk mengakses kedua fungsi XML dan JSON tersebut. 
6.	Selanjutnya, kita perlu membuat pengembalian data ID dalam XML dan JSON. Kita dapat membuat fungsi pada views.py di folder main dengan nama show_xml_by_id dan show_json_by_id. Buatlah sedikit mirip dengan proses yang telah kita lakukan pada nomor sebelumnya. Tambahkan juga part hurl ke urlpatterns dengan format sebagai berikut
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
7.	Website yang telah dibuat sudah dapat dijalankan dan dapat dicek dengan menggunakan Postman sebagai data viewer

Screenshot Gambar Postman
HTML
![alt text](IMG_Tugas3/get_html.png)

JSON
![alt text](IMG_Tugas3/get_json.png)

XML
![alt text](IMG_Tugas3/get_xml.png)

JSON by ID
![alt text](IMG_Tugas3/get_json_by_id.png)

XML by ID
![alt text](IMG_Tugas3/get_xml_by_id.png)
