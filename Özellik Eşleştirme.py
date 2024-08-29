import cv2
import matplotlib.pyplot as plt

# Görüntüleri içe aktar
chos = cv2.imread("animals.jpg", 0)
cho = cv2.imread("panda.jpg", 0)

plt.figure(), plt.imshow(chos, cmap="gray"), plt.axis("off"), plt.title("Ana Görüntü")
plt.figure(), plt.imshow(cho, cmap="gray"), plt.axis("off"), plt.title("Aranacak Görüntü")

# ORB tanımlayıcı
orb = cv2.ORB_create(nfeatures=1000)  # Daha fazla özellik noktası tespiti için nfeatures parametresini artırdım

# Anahtar nokta tespiti ORB ile
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# BF matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Mesafeye göre sırala
matches = sorted(matches, key=lambda x: x.distance)

# En iyi eşleşmeleri seç (ilk 50 eşleşme)
good_matches = matches[:50]

# Eşleşen resimleri görselleştir
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, good_matches, None, flags=2)
plt.imshow(img_match), plt.axis("off"), plt.title("ORB ile Eşleşme")

# SIFT tanımlayıcı
sift = cv2.SIFT_create()

# Anahtar nokta tespiti SIFT ile
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

# BF matcher
bf = cv2.BFMatcher()

# Noktaları eşleştir
matches = bf.knnMatch(des1, des2, k=2)

# Güzel eşleşmeleri belirle
good_matches = []

for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

# Eşleşen resimleri görselleştir
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, good_matches, None, flags=2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("SIFT ile Eşleşme")

# SURF tanımlayıcı (SURF, SIFT'e göre daha hızlı ve genellikle daha iyi sonuçlar verebilir)
surf = cv2.xfeatures2d.SURF_create()

# Anahtar nokta tespiti SURF ile
kp1, des1 = surf.detectAndCompute(cho, None)
kp2, des2 = surf.detectAndCompute(chos, None)

# BF matcher
bf = cv2.BFMatcher()

# Noktaları eşleştir
matches = bf.knnMatch(des1, des2, k=2)

# Güzel eşleşmeleri belirle
good_matches = []

for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

# Eşleşen resimleri görselleştir
plt.figure()
surf_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, good_matches, None, flags=2)
plt.imshow(surf_matches), plt.axis("off"), plt.title("SURF ile Eşleşme")

plt.show()
