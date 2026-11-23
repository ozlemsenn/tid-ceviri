# Türk İşaret Dilinden Türkçe Cümleye

> Kameradan alınan Türk İşaret Dili işaretlerini kelime düzeyinde tanıyan ve
> tanınan kelime dizisini dilbilgisi açısından doğru Türkçe cümlelere çeviren,
> sıradan bir bilgisayarda çevrim dışı ve gerçek zamanlı çalışan uçtan uca sistem.

- **Proje yürütücüsü:** Özlem Şen
- **Danışman:** Dr. Öğr. Üyesi Muhammed Milani
- **Program:** TÜBİTAK 2209-A — Başvuru no. 1919B012615317
- **Süre:** 8 ay (İP1–İP5)

---

## Durum

- [x] Proje iskeleti
- [x] Ortam kurulumu (Python 3.12.10, CUDA'lı PyTorch, MediaPipe)
- [x] Git / GitHub
- [ ] **İP1-1a** — sınıf özeti (Kaggle)
- [ ] **İP1-1b** — 60 kelimenin seçimi
- [ ] **İP1-2** — öznitelik çıkarımı
- [ ] **İP1-3** — ön işleme
- [ ] **İP1-4** — işaretçi bazında bölme
- [ ] **İP1-5** — kalite kontrolü

---

## Günlük çalışma

Her oturumda, proje klasöründe:

```bat
.venv\Scripts\activate
```

Satır başında `(.venv)` görmelisin. Günün sonunda:

```bat
git add .
git commit -m "ne yaptığını anlatan kısa cümle"
git push
```

---

## Veri nerede duruyor

**AUTSL videoları bilgisayara indirilmez.** Veri seti ~40-60 GB; öznitelik
çıkarımı verinin bulunduğu ortamda (Kaggle) yapılır, buraya yalnızca sonuç iner.

| Ne | Boyut | Nerede |
|---|---|---|
| AUTSL videoları | ~40-60 GB | Kaggle |
| `ClassId.csv`, `train_labels.csv` | ~500 KB | `data/raw/` |
| Çıkarılmış öznitelikler (60 kelime) | ~300-400 MB | `data/interim/` |
| İşlenmiş diziler | ~100 MB | `data/processed/` |

---

## Klasör düzeni

```
tid-ceviri/
├── config.yaml       <- BÜTÜN PARAMETRELER BURADA
├── requirements.txt
├── src/              <- kod
├── scripts/          <- tek seferlik yardımcı betikler
├── notebooks/        <- Kaggle / deneme defterleri
├── data/             <- veri (git'e girmez)
│   ├── raw/          <- etiket dosyaları
│   ├── interim/      <- çıkarılan eklem noktaları
│   └── processed/    <- 48 kareye sabitlenmiş diziler
└── outputs/          <- model, grafik, rapor (git'e girmez)
```

**İki kural:**

1. `data/` ve `outputs/` asla git'e girmez. Yedekleri harici diske alınır.
2. Kodun içine sabit sayı yazılmaz. Her parametre `config.yaml`'da.

---

## İP1 adımları

| Adım | Nerede | Çıktı |
|---|---|---|
| 1a. Sınıf özetini çıkar | Kaggle | `sinif_ozeti.csv` |
| 1b. 60 kelimeyi seç | yerel, elle | aynı dosya, `secildi` sütunu |
| 2. Öznitelik çıkarımı | Kaggle | `data/interim/*.npy` |
| 3. Ön işleme | yerel | `data/processed/*.npy` |
| 4. İşaretçi bazında bölme | yerel | `data/processed/bolme.json` |
| 5. Kalite raporu | yerel | tespit oranı ≥ %90 |

---

## Çalışma düzeni

- **Her gün 5 gloss–Türkçe cümle çifti yaz.** 600 çift ÷ 5 = 120 gün.
  İP3 takvimde 3. ayda ama 60 kelime belli olur olmaz başla — bu iş
  sıkıştırılamaz, erken başlamazsan sona yığılır.
- **Her akşam commit at.** Küçük commit, açıklayıcı mesaj.
- **Haftada bir harici diske yedekle** (`data/` ve `outputs/` dahil).

---

## Sıfırdan kurulum

Yeni bir bilgisayarda kurman gerekirse:

1. **Python 3.12.10** — [python.org](https://www.python.org/downloads/release/python-31210/)
   → *Windows installer (64-bit)*.
   Kurarken **"Add python.exe to PATH"** kutusunu işaretle.
   (3.12.11 ve sonrası yalnızca kaynak kod olarak yayımlanıyor, Windows kurulumu yok.)
2. Proje klasöründe `kurulum.bat` dosyasına çift tıkla.
3. Sonunda `CUDA kullanilabilir: True` görmelisin. `False` ise CPU sürümü
   kurulmuştur, model eğitimi 10-20 kat yavaş olur — düzeltmeden devam etme.
4. Her şey çalışınca sürümleri sabitle: `pip freeze > requirements-kilit.txt`

---

## Ön çalışma kayıtları

3 kelimelik alt kümede, 608 video, işaretçiden bağımsız bölme:

| | |
|---|---|
| Normal test doğruluğu | **%97,3** |
| Aynalanmış test doğruluğu | **%94,7** |
| Fark | 2,7 puan (hedef: < 5 puan) |
| Kare sayısı (T) | 48 |
| Öznitelik boyutu | 201 (67 nokta × 3) |
| Gizli boyut | 128 |
| Güven eşiği | 0,6 |
