# Đánh Giá Con Người trong Mô Hình AI Tạo Ra Nội Dung: Hình Ảnh, Âm Thanh và Video

**© 2026 Pixiboss**. Mọi quyền được bảo lưu.  
*Liên hệ: hello@pixibox.ai*

---

## Trích yếu

Việc đánh giá mô hình AI thế hệ mới cho nội dung đa phương tiện là quá trình phức hợp, kết hợp giữa phương pháp **đánh giá chủ quan** (dựa trên nhận định của con người) và **đánh giá khách quan** (sử dụng các số liệu kỹ thuật). Bài viết này tổng hợp các phương pháp tiên tiến hiện nay để đánh giá chất lượng hình ảnh, âm thanh và video do AI tạo ra.

---

## 1. Tổng Quan về Đánh Giá AI

| Phương Diện | Định Nghĩa | Công Cụ/Thước Đo Điển Hình |
|-------------|------------|---------------------------|
| Chủ quan    | Phán xét dựa trên cảm xúc & trải nghiệm con người | Khảo sát, thang điểm Likert |
| Khách quan  | Đo lường bằng số liệu kỹ thuật tự động | PSNR, SSIM, SNR, Spectral Flatness |

---

## 2. Đánh Giá Hình Ảnh AI

Đánh giá hình ảnh bao gồm cả các yếu tố chủ quan (vẻ đẹp, tính hiện thực) và khách quan (số liệu pixel).

### 2.1 Thước đo khách quan

#### Tỷ lệ Tín hiệu trên Nhiễu (PSNR)

$$
\text{PSNR} = 10 \log_{10}\left(\frac{\text{MAX}_I^2}{MSE}\right)\text{dB}
$$

trong đó:
- $\text{MAX}_I$ là giá trị tuyệt đối lớn nhất của cường độ pixel (ví dụ: 255 cho ảnh 8-bit)
- $MSE$ là sai số trung bình căn phương giữa hình ảnh gốc và hình ảnh tái tạo:

$$
\text{MSE} = \frac{1}{N \times M}\sum_{i=0}^{N-1} \sum_{j=0}^{M-1} (I(i,j) - \hat{I}(i,j))^2
$$

#### Chỉ số Tương đồng Cấu trúc (SSIM)

$$
\text{SSIM}(x,y) = \frac{(2\mu_x\mu_y + C_1)(2\sigma_{xy} + C_2)}{(\mu_x^2 + \mu_y^2 + C_1)(\sigma_x^2 + \sigma_y^2 + C_2)}
$$

với:
- $\mu_x, \mu_y$: trung bình intensity hình ảnh gốc và tái tạo
- $\sigma_x^2, \sigma_y^2, \sigma_{xy}$: phương sai và hiệp phương sai
- $C_1 = (k_1 L)^2$, $C_2 = (k_2 L)^2$ là hằng số ổn định

---

### 2.2 Thước đo chủ quan

Các yếu tố được đánh giá qua khảo sát con người:

| Yếu Tố | Mô Tả |
|--------|-------|
| Tính Hiện Thực | Mức độ giống với cảnh thực tế |
| Vẻ Đẹp Thị giác | Đánh giá cảm xúc nghệ thuật |
| Cảm Xúc | Tác động tâm lý khi xem |

---

## 3. Đánh Giá Âm Thanh AI

#### Thước đo khách quan âm thanh:

$$
\text{SNR} = L_{\text{signal}} - L_{\text{noise}} \, (\text{dB})
$$

$$
\text{Spectral Flatness} = \exp\left(\frac{-\sum_{b=0}^{N-1} \ln|P(f_b)|}{N}\right)
$$

với $P(f_b)$ là power spectrum tại tần số $f_b$.

#### Yếu tố cảm xúc âm thanh:

- **Nhịp điệu**: Tính đồng đều của beat theo thời gian.
- **Giọng nói**: Độ rõ ràng, tự nhiên.
- **Tần số**: Sự đa dạng trong dải tần (bass, mid, treble).

---

## 4. Đánh Giá Video AI

Video yêu cầu thêm hai yếu tố: **chất lượng hình ảnh giữa khung hình** và **sự mạch lạc về thời gian**.

### 4.1 Thước đo chất lượng hình ảnh

- PSNR đã đề cập ở mục 2.1
- SSIM để so sánh cấu trúc giữa video tham chiếu và video AI.

### 4.2 Sự Mạch Lược Về Thời Gian (Temporal Coherence)

Xét chuyển tiếp từ khung hình này sang khung khác:

$$
\text{Coherence} = \frac{1}{K}\sum_{k=1}^{K-1} \|V_k - V_{k+1}\|_\infty
$$

trong đó $V_k$ là vectơ đặc trưng của khung hình thứ $k$.

### 4.3 Sự Phù Hợp Theo Ngữ Cảnh

Ví dụ: Video thợ lặn phải có sóng biển, chuyển động tự nhiên, và bầu không khí nhất quán với kịch bản.

---

## 5. Tổng Kết Chiến Lược Đánh Giá

| Phương Tiện | Thước Đo Chính | Mục Đích |
|-------------|---------------|----------------|
| Hình Ảnh    | PSNR, SSIM, Khảo sát Likert | Độ sắc nét, cảm xúc, hiện thực |
| Âm Thanh    | SNR, Spectral Flatness | Chất lượng âm thanh và cảm xúc |
| Video       | PSNR, SSIM, Temporal Coherence | Cả chất lượng hình ảnh lẫn sự mạch lạc theo thời gian |

---

## Kết Luận

Việc kết hợp **đánh giá số liệu** với **phản hồi chủ quan** là bắt buộc để phát triển AI có ứng dụng thực tế. Chỉ số kỹ thuật đo lường đúng chuẩn, nhưng con người mới đánh giá được trải nghiệm cảm xúc — điều tối thượng của nội dung sáng tạo.

---

## Tài Liệu Tham Khảo

1. Wang, Z., et al. (2004). *Image Quality Assessment: From Error Visibility to Structural Similarity*. IEEE TIP.
2. ITU-R BS.500 (2009). *Subjective assessment of subjective quality using a two-alternative forced choice method*.
3. Plumbley, M.D., et al. (1998). *Analysis of the human perception of audio and visual media*. IEEE Signal Processing Magazine.
4. Pixiboss AI Research Lab. (2025). *Evaluating Generative AI Content Quality Standards*.

---