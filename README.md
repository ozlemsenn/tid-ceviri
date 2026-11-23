# Türk İşaret Dilinden Türkçe Cümleye

Kameradan alınan Türk İşaret Dili işaretlerini kelime düzeyinde tanıyan ve
tanınan kelime dizisini dilbilgisi açısından doğru Türkçe cümlelere çeviren,
sıradan bir bilgisayarda çevrim dışı ve gerçek zamanlı çalışan uçtan uca sistem.

TÜBİTAK 2209-A — Başvuru no: 1919B012615317
Proje yürütücüsü: Özlem Şen · Danışman: Dr. Öğr. Üyesi Muhammed Milani

---

## Kurulum (bir kerelik)

### 1. Python
Python **3.11** veya **3.12** kur. (3.13 ile MediaPipe henüz sorunlu olabilir.)

### 2. Sanal ortam
Proje klasöründe:

```bat
python -m venv .venv
.venv\Scripts\activate
```

Terminalin başında `(.venv)` görmelisin. **Her oturumda bunu aktif et.**

### 3. PyTorch — ÖNCE BU
`pip install torch` yazma. CPU sürümü kurar, ekran kartın kullanılmaz.
CUDA'lı sürüm için:

```bat
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

Doğrula:

```bat
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

`True NVIDIA GeForce RTX 3050 Laptop GPU` yazmalı. `False` yazıyorsa dur, devam etme.

### 4. Geri kalan paketler

```bat
pip install -r requirements.txt
```

### 5. Kurulumu dondur
Her şey çalışınca sürümleri sabitle — altı ay sonra aynı ortamı kurabilmen için:

```bat
pip freeze > requirements-kilit.txt
```

### 6. Git

```bat
git init
git add .
git commit -m "Proje iskeleti"
```

GitHub'da boş bir depo aç, sonra:

```bat
git remote add origin https://github.com/<kullanici>/<depo>.git
git push -u origin main
```

---

## Klasör düzeni

```
tid-ceviri/
├── config.yaml          ← BÜTÜN PARAMETRELER BURADA
├── requirements.txt
├── src/                 ← kod
├── scripts/             ← tek seferlik yardımcı betikler
├── notebooks/           ← deneme/keşif defterleri
├── data/                ← VERİ (git'e girmez)
│   ├── raw/             ← AUTSL buraya
│   ├── interim/         ← çıkarılan eklem noktaları
│   └── processed/       ← 48 kareye sabitlenmiş diziler
└── outputs/             ← model, grafik, rapor (git'e girmez)
```

**Kural:** `data/` ve `outputs/` asla git'e girmez. `.gitignore` bunu zaten engelliyor.
Bu klasörlerin yedeği harici diske alınır.

**Kural:** Kodun içine sabit sayı yazma. Her parametre `config.yaml`'da.

---

## Verinin yerleştirilmesi

AUTSL'i indir, şu yapıda çıkar:

```
data/raw/autsl/
├── ClassId.csv
├── train_labels.csv
├── validation_labels.csv
└── train/ ...
```

Farklı bir yere koyduysan `config.yaml` → `veri.autsl_kok` satırını düzelt.

---

## İP1 adımları

| Adım | Betik | Çıktı |
|---|---|---|
| 1a. Sınıf özetini çıkar | `python -m src.sinif_ozeti` | `outputs/raporlar/sinif_ozeti.csv` |
| 1b. 60 kelimeyi seç | (elle doldur) | aynı dosya, `secildi` sütunu |
| 2. Öznitelik çıkarımı | `src/ozellik_cikarim.py` | `data/interim/*.npy` |
| 3. Ön işleme | `src/on_isleme.py` | `data/processed/*.npy` |
| 4. İşaretçi bazında bölme | `src/bolme.py` | `data/processed/bolme.json` |
| 5. Kalite raporu | `src/kalite.py` | tespit oranı ≥ %90 |

---

## Çalışma düzeni

- **Her gün 5 gloss–Türkçe cümle çifti yaz.** 600 çift ÷ 5 = 120 gün.
  İP3 takvimde 3. ayda başlıyor ama beklemeyin — 60 kelime belli olur olmaz başla.
- **Her akşam commit at.** Küçük commit, açıklayıcı mesaj.
- **Haftada bir harici diske yedekle.** `data/` ve `outputs/` dahil.

---

## Ön çalışma kayıtları (referans)

3 kelimelik alt kümede, 608 video:

| | |
|---|---|
| Normal test doğruluğu | %97,3 |
| Aynalanmış test doğruluğu | %94,7 |
| Fark | 2,7 puan (hedef: < 5) |
| T (kare) | 48 |
| Öznitelik boyutu | 201 |
| Gizli boyut | 128 |
| Güven eşiği | 0,6 |
