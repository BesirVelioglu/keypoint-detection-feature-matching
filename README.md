# Görüntü Eşleştirme ile Özellik Tespiti

Bu proje, OpenCV kütüphanesi kullanarak görüntüler arasında özellik tespiti ve eşleştirme işlemleri gerçekleştirir. ORB, SIFT ve SURF algoritmalarını kullanarak anahtar nokta tespiti ve eşleştirme işlemleri yapılır ve sonuçlar görselleştirilir.

## İçerik

- **ORB**: Oriented FAST and Rotated BRIEF, görüntüdeki anahtar noktaları ve özelliklerini tespit eder.
- **SIFT**: Scale-Invariant Feature Transform, ölçek ve döndürme değişikliklerine dayanıklı anahtar noktaları tespit eder.
- **SURF**: Speeded-Up Robust Features, SIFT'in hızlı bir versiyonudur ve görüntü özelliklerini hızlı bir şekilde tespit eder.

## Gereksinimler

- Python 3.x
- OpenCV (cv2)
- Matplotlib

Bu kodu çalıştırmak için gerekli Python paketlerini yüklemek için:

```bash
pip install opencv-python matplotlib
```
## Kullanım

**Proje Dosyalarını İndirin**: Bu kodu çalıştırmadan önce, proje dosyalarını yerel makinenize klonlayın veya indirin.

   ```bash
   git clone <repo-url>
   ```

## Notlar
- SURF algoritması, OpenCV'nin xfeatures2d modülünde bulunur ve bu nedenle opencv-contrib-python paketinin yüklenmiş olması gerekir.
- opencv-contrib-python paketini yüklemek için:
  
```bash
pip install opencv-contrib-python
```

