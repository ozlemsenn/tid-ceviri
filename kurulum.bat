@echo off
chcp 65001 >nul
echo ============================================
echo  TID Ceviri - Kurulum
echo ============================================
echo.

python --version
if errorlevel 1 (
    echo [HATA] Python bulunamadi. Python 3.11 veya 3.12 kur.
    pause & exit /b 1
)

echo.
echo [1/4] Sanal ortam olusturuluyor...
python -m venv .venv
call .venv\Scripts\activate.bat

echo.
echo [2/4] PyTorch (CUDA 12.1) kuruluyor... bu biraz surer.
pip install torch --index-url https://download.pytorch.org/whl/cu121

echo.
echo [3/4] Diger paketler kuruluyor...
pip install -r requirements.txt

echo.
echo [4/4] Ekran karti kontrolu:
python -c "import torch; print('CUDA kullanilabilir:', torch.cuda.is_available()); print('Cihaz:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'YOK')"

echo.
echo Kurulum bitti. Her oturumda once su komutu calistir:
echo     .venv\Scripts\activate
echo.
pause
