"""
Ayarları tek yerden okur.

Kullanımı:
    from src.config import AYAR, KOK
    kare = AYAR["on_isleme"]["kare_sayisi"]
"""
from pathlib import Path
import yaml

# Proje kök klasörü (bu dosyanın bir üstü)
KOK = Path(__file__).resolve().parents[1]


def yukle(yol=None) -> dict:
    yol = Path(yol) if yol else KOK / "config.yaml"
    if not yol.exists():
        raise FileNotFoundError(f"Ayar dosyası bulunamadı: {yol}")
    with open(yol, encoding="utf-8") as f:
        return yaml.safe_load(f)


def yol(*parcalar) -> Path:
    """Proje köküne göre mutlak yol üretir."""
    return KOK.joinpath(*parcalar)


AYAR = yukle()
