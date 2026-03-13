# Đánh Giá Mô Hình Ngôn ngữ Dựa trên Văn Bản: METEOR, Perplexity và Độ Công Bằng

## © 2026 Pixiboss. Mọi quyền được bảo lưu.  
**Liên hệ:** hello@pixibox.ai

---

```markdown
# Mô hình Đánh giá dựa trên Văn bản cho LLMs

## 1. Giới thiệu

Các mô hình ngôn ngữ lớn (LLM) ngày nay đóng vai trò quan trọng trong nhiều ứng dụng thực tế, từ dịch thuật đến phê duyệt khoản vay và tuyển dụng. Để đảm bảo chất lượng và công bằng của các hệ thống này, việc sử dụng **thước đo đánh giá hiệu quả** là cần thiết. Bài viết này trình bày ba khía cạnh chính:
1. **METEOR**: Số liệu đánh giá chất lượng dịch
2. **Perplexity (Sự bối rối)**: Đánh giá dự đoán văn bản
3. **Độ công bằng**: Định lượng thành kiến nhóm nhân khẩu học

---

## 2. METEOR: Đánh giá Dịch với Thứ tự Cải thiện

**METEORE** (Mean Explanatory Error for Translation) là số liệu cải tiến so với BLEU, xem xét cả ngữ nghĩa và từ đồng nghĩa.

### Công thức METEOR:
$$F_{\text{meteor}} = \frac{(P \cdot R)}{\alpha P + \beta R}$$  

Trong đó:
- $P$: Độ chính xác (Precision)
- $R$: Độ truy xuất (Recall)
- $\alpha, \beta$: Trọng số ($\alpha = 1, \beta = 0.5$ mặc định)

**METEOR** tính cả:
- Match chuỗi nguyên vẹn
- Từ đồng nghĩa (synonyms)
- Từ paraphrase
- Stem matching

**Ví dụ:**
```
Văn bản tham khảo: "con mèo nhanh nhảy qua con chó"
Dịch A: "gato rápido salta por el perro"
Dịch B: "el gato saltará por el perra"

METEOR cho Dịch A điểm cao hơn do bảo toàn cấu trúc và ngữ nghĩa.
```

---

## 3. Perplexity (Sự Bối Rối): Đánh giá Dự đoán Văn bản

**Perplexity** đo lường sự không chắc chắn của mô hình trong việc dự đoán chuỗi văn bản.

### Công thức Perplexity:
$$P = \frac{1}{L} \sum_{i=1}^{L} \log p(x_i | x_{<i})$$  
$$\text{Perplexity} = e^{-NPL} = \exp\left(\sum_{i=1}^L -\log p(x_i|x_{<i})\right)$$

Trong đó:
- $L$: Chiều dài chuỗi từ
- $p(x_i | x_{<i})$: Xác suất dự đoán từ tiếp theo
- **NPL**: Normalized Perplexity

**Ví dụ:**  
Mô hình dự đoán "cửa sổ, ô tô, mặt trăng" cho câu "con mèo ngồi trên":
- Nếu xác suất chính: $p(\text{thảm}|x_{<i}) = 0.5$
- Perplexity = $1/0.5^1 = 2$ (giai đoạn thấp → mô hình tự tin cao)

---

## 4. Đánh giá Công bằng cho Mô hình AI

Để xác định thành kiến trong dự đoán, ta phân tích sự khác biệt giữa các nhóm:

### Công thức Khác biệt Tỷ lệ Sai số:
$$\Delta = |P_A - P_B|$$  
Trong đó:
- $P_A, P_B$: Tỷ lệ lỗi dương tính giả cho nhóm A và B
- Giá trị $\Delta > 0.1$ → cảnh báo thiên vị tiềm tàng

### Ví dụ thực tế - Phê duyệt khoản vay:
- Nhóm A (nam): 40% được dự đoán tín dụng xứng đáng
- Nhóm B (nữ): 20% → **Thiên vị phát hiện**

| Hạng mục | Nhóm A | Nhóm B | $\Delta$ |
|----------|-------|--------|---------|
| Dự đoán tích cực | 40%   | 20%    | 20.0%   |
| Đánh dấu sai dương tính | 10%    | 30%    | 20.0%   |

---

## 5. Kết luận

- **METEOR**: Đảm bảo chất lượng dịch qua nhiều tiêu chí ngữ nghĩa.
- **Perplexity**: Đo lường độ tự tin của mô hình trong dự đoán câu.
- **Độ công bằng**: Phát hiện thiên vị, đảm bảo xử lý công bằng các nhóm nhân khẩu học khác nhau.

**Ứng dụng thực tiễn:**  
Khi triển khai AI trong quyết định tuyển dụng, vay vốn, cần kiểm soát cả ba số liệu để đảm bảo tính pháp lý và đạo đức.

---

## Tài liệu Tham khảo

1. Banarjee et al. (2016). METEOR: An Effective Metric for Machine Translation.
2. Oord et al. (2016). Perplexity as a Predictor for Language Model Quality.
3. Kleinberg & Mullainathan (2023). Evaluating Bias in AI Decision Systems.

```