# <span style="color: green">Django Login Uygulaması</span>

Bu uygulama, Django web çatısı kullanarak bir login sayfası oluşturmanızı sağlar. Kullanıcıların giriş yapmasına, kaydolmasına ve profil bilgilerini düzenlemesine izin verir.

## Kurulum

1. Bu projeyi klonlayın: `git clone https://github.com/kullaniciadi/projeadi.git`
2. Virtual environment oluşturun: `python -m venv env`
3. Virtual environment'i aktifleştirin:
   - Windows: `.\env\Scripts\activate`
   - Linux/MacOS: `source env/bin/activate`
4. Gerekli kütüphaneleri yükleyin: `pip install -r requirements.txt`
5. Veritabanını oluşturun: `python manage.py migrate`
6. Sunucuyu başlatın: `python manage.py runserver`

## Kullanım

1. Tarayıcınızda `http://localhost:8000/login` adresine gidin.
2. Kullanıcı adı ve şifrenizle giriş yapın veya kaydolun.
3. Kullanıcı profilinizi düzenlemek için `http://localhost:8000/profile` adresine gidin.

## Ekran Görüntüleri

### Login Sayfası
![Login Sayfası](https://github.com/hakanmolla/Django-Login/blob/main/Screenshot.jpg)


## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylı bilgi için `LICENSE` dosyasına bakın.

Bu örnek, projeniz için başlangıç noktası olarak kullanabilirsiniz. Lütfen, README dosyanızın ihtiyacınıza göre düzenlemeyi unutmayın ve gerekli görüntüleri ve bağlantıları ekleyin. Başarılar!