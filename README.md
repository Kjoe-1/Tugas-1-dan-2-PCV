# Tugas Pengolahan Citra Digital (OpenCV)

Dokumen ini berisi dua program utama:

1. **Tugas 1:** Smoothing & Blurring (Average, Gaussian, Sharpen)  
2. **Tugas 2:** Deteksi Objek Biru (HSV + Morphology + Contour Detection)

Keduanya berjalan secara real-time menggunakan webcam.

---

## Requirements

```bash
pip install opencv-python numpy
```

---

## Cara Menjalankan

### **Tugas 1 — Smoothing dan Blurring**

```bash
python tugas1_smoothing_blurring.py
```

#### **Kontrol Keyboard**
| Tombol | Fungsi |
|--------|--------|
| `0` | Mode Normal |
| `1` | Average Blur (5×5) |
| `2` | Gaussian Blur (Custom Kernel) |
| `3` | Sharpening |
| `q` | Quit |

---

### **Tugas 2 — Deteksi Objek Biru**

```bash
python tugas2_deteksi_biru.py
```

---

# Penjelasan Tugas

---

## 🔹 Tugas 1 — Real-Time Image Filtering

Program ini menerapkan berbagai filter real-time menggunakan webcam.

### **Filter yang Tersedia**
- Normal Mode  
- Average Blur (5×5)  
- Gaussian Blur (Custom Kernel 5×5)  
- Sharpening Filter  

### **Cuplikan Kode Kernel**

#### Gaussian Kernel
```python
gauss_1d = cv2.getGaussianKernel(5, sigma=1)
gaussian_kernel = gauss_1d @ gauss_1d.T
```

#### Sharpen Kernel
```python
sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])
```

---

## 🔹 Tugas 2 — Deteksi Objek Biru (HSV + Morphology)

Program ini mendeteksi objek berwarna biru menggunakan segmentasi HSV, kemudian membersihkan hasil threshold menggunakan operasi morfologi.

### **Rentang Warna Biru (HSV)**
```python
lower_blue = np.array([100, 120, 50])
upper_blue = np.array([140, 255, 255])
```

### **Tahapan Deteksi**
1. Konversi BGR → HSV  
2. Threshold berdasarkan warna biru  
3. Morphology Opening (hilangkan noise)  
4. Morphology Closing (menutup lubang)  
5. Deteksi kontur  
6. Tampilkan bounding box jika objek valid  

---

## Catatan
- Pastikan webcam berfungsi dengan baik  
- Cahaya ruangan mempengaruhi hasil deteksi  
- Rentang HSV bisa disesuaikan sesuai kebutuhan  
