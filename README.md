# siberGuvenlik

### arka planda sessiz calisarak fare tiklamalarinda cekilen ekran resimlerini servera yollar.

##### server.py dosyasi icerisinde soket ile dinleme baslatilip gelen dosyanin kaydi gerceklestirilir.
##### client.py dosyasi icerisinde sokete baglanti yapilir ve getStateKey fonksiyonu icerisinde tanimlanan tusa basildiginda ekran resmi alarak servera yollar. server IP adresi duruma gore degistirilmelidir.
##### her iki dosyada da ayni port adresinin verildiginden emin olunmalidir. ayrica 1024 ten kucuk port adresi verilmemelidir. 1024 ile 65000 arasinda herhangi bir port numarasi secilebilir.
