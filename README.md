Fathi Qushoyyi Ahimsa (NPM 2206082120) 
PBP C
README.md 
Tautan Deployment Adaptable	: https://pbp-inventory-list.adaptable.app/

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

