
# 🌐 HTML OS / HTML İşletim Sistemi

## 🇹🇷 HTML OS'a Hoşgeldin! / 🇬🇧 Welcome to HTML OS!

Merhaba! Seni burada görmek harika.  
Bu proje, HTML ile masaüstü deneyimini yeniden tanımlayan bir sistemdir. Aşağıda, projeyi kaynak koddan nasıl çalıştırabileceğini adım adım anlattım.

Hi! It’s great to see you here.  
This project is a desktop-like environment built using HTML. Below are step-by-step instructions on how to run it from the source code.

---

## 🚀 Kurulum / Installation

### 1️⃣ Kaynak kodu indir / Download the source code

- **TR:** Kaynak kodunu indirip 7zip veya WinRAR gibi bir programla ayıkla.  
- **EN:** Download the source code and extract it using 7zip or WinRAR.

---

### 2️⃣ Python yükle / Install Python

- **TR:** Python 3.7 veya üzerini indir. Ardından terminali aç ve şu komutu gir:  
- **EN:** Download Python 3.7 or later. Then open the terminal and type:

```
pip install flask
```

---

### 3️⃣ Klasöre git / Go to the folder

- **TR:** İndirdiğin dizinde `htmlos` klasörüne gir.  
- **EN:** Enter the `htmlos` folder in the extracted directory.

---

### 4️⃣ Terminal aç / Open terminal

- **TR:** Dosya yöneticisinde boş bir yere sağ tıklayıp terminali aç.  
- **EN:** Right-click on empty space in the file manager and open the terminal.

---

### 5️⃣ Sunucuyu başlat / Start the server

```
python server.py
```

---

### 6️⃣ Tarayıcıdan aç / Open in browser

- **TR:** Tarayıcını aç ve şu adresi yaz:  
- **EN:** Open your browser and type:

```
http://localhost:5000
```

---

✅ **TR:** Hepsi bu kadar! HTML OS’a hoşgeldin 🚀  
✅ **EN:** That’s all! Welcome to HTML OS 🚀

---

## 📦 App Loader Nasıl Kullanılır? / How to Use App Loader?

HTML OS, kullanıcıların `.zip` dosyası yükleyerek özel uygulamalar kurmasına izin verir.  
HTML OS allows users to install custom applications using `.zip` files.

---

### 🧩 1. `app.html` oluştur / Create `app.html`

- **TR:** Uygulamanın ana HTML dosyasını `app.html` olarak adlandır.  
- **EN:** Name your main HTML file as `app.html`.

---

### 📝 2. `config.json` oluştur / Create `config.json`

Aynı klasöre `config.json` adında bir dosya ekle ve şunu yaz:

```json
[
  {
    "name": "Benim Uygulamam",
    "icon": "🧠",
    "resizable": true,
    "width": 500,
    "height": 300
  }
]
```

Açıklamalar / Explanations:
- `name`: Görünen uygulama adı / Shown app name   
- `icon`: Emoji veya simge / Emoji or icon  
- `resizable`: Yeniden boyutlandırılabilir mi? / Is it resizable?  
- `width, height`: Sabit boyutlar (isteğe bağlı) — Sadece resizable false olduğu durumlarda geçerlidir./ Fixed dimensions (optional) — Only valid when resizable is set to false.

---

### 🗜️ 3. Zip’le / Zip it

- **TR:** `app.html` ve `config.json` dosyalarını `.zip` arşivine koy.  
- **EN:** Put `app.html` and `config.json` into a `.zip` archive.

---

### 📤 4. AppLoader ile yükle / Load it with AppLoader

- **TR:** HTML OS içindeki AppLoader uygulamasını aç ve `.zip` dosyanı seç.  
- **EN:** Open the AppLoader app in HTML OS and select your `.zip` file.

---

💡 Artık uygulaman otomatik olarak masaüstüne eklenir ve çalıştırılabilir!  
💡 Your app will now be automatically added to the desktop and can be launched instantly!

---

✨ Keyifli kodlamalar! / Happy coding!
