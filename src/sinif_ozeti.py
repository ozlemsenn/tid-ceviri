"""
İP1 - Adım 1a: AUTSL sınıf listesini ve her sınıfın örnek sayısını çıkarır.

Ne yapar:
  - ClassId.csv (226 kelime) ile train_labels.csv'yi birleştirir
  - Her kelimenin eğitim kümesinde kaç örneği olduğunu sayar
  - outputs/raporlar/sinif_ozeti.csv dosyasını üretir

Çalıştırma (proje kökünden):
    python -m src.sinif_ozeti
"""
import sys
import pandas as pd

from src.config import AYAR, yol


def _etiket_oku(dosya):
    """train_labels.csv başlıklı da başlıksız da gelebilir; ikisini de kaldırır."""
    ilk = pd.read_csv(dosya, nrows=1, header=None)
    ikinci_hucre = str(ilk.iloc[0, 1])
    basliksiz = ikinci_hucre.strip().lstrip("-").isdigit()

    if basliksiz:
        return pd.read_csv(dosya, header=None, names=["video", "sinif"])
    df = pd.read_csv(dosya)
    df.columns = ["video", "sinif"][: df.shape[1]]
    return df


def main():
    kok = yol(AYAR["veri"]["autsl_kok"])
    sinif_dosyasi = kok / AYAR["veri"]["sinif_dosyasi"]
    etiket_dosyasi = kok / AYAR["veri"]["egitim_etiket"]

    for d in (sinif_dosyasi, etiket_dosyasi):
        if not d.exists():
            print(f"[HATA] Dosya yok: {d}")
            print("       config.yaml icindeki 'veri.autsl_kok' yolunu kontrol et.")
            sys.exit(1)

    siniflar = pd.read_csv(sinif_dosyasi)
    etiketler = _etiket_oku(etiket_dosyasi)

    print(f"ClassId.csv sutunlari : {list(siniflar.columns)}")
    print(f"Sinif sayisi          : {len(siniflar)}")
    print(f"Egitim ornegi sayisi  : {len(etiketler)}\n")

    id_sutunu = siniflar.columns[0]
    sayim = etiketler["sinif"].value_counts()
    siniflar["ornek_sayisi"] = siniflar[id_sutunu].map(sayim).fillna(0).astype(int)
    siniflar["rol"] = ""          # elle doldurulacak: ozne / nesne / fiil / yer / zaman / soru / sifat
    siniflar["aynalanabilir"] = ""  # elle doldurulacak: evet / hayir / supheli
    siniflar["secildi"] = ""        # elle doldurulacak: x

    hedef = yol("outputs", "raporlar", "sinif_ozeti.csv")
    hedef.parent.mkdir(parents=True, exist_ok=True)
    siniflar.to_csv(hedef, index=False, encoding="utf-8-sig")

    ort = siniflar["ornek_sayisi"].mean()
    az = siniflar[siniflar["ornek_sayisi"] < ort * 0.7]

    print(siniflar.sort_values("ornek_sayisi", ascending=False).head(15).to_string(index=False))
    print(f"\nOrtalama ornek sayisi : {ort:.1f}")
    print(f"Ortalamanin %70'inin altinda kalan sinif sayisi: {len(az)}")
    print(f"\n[OK] Yazildi -> {hedef}")


if __name__ == "__main__":
    main()
