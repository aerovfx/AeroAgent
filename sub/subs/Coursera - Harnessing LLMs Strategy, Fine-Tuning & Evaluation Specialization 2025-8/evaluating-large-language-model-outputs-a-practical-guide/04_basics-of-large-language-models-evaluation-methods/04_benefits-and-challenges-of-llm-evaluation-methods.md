# PHÂN TÍCH KHOA HỌC VỀ METRICS ĐÁNH GIÁ TRONG TRÍ TUỆ NHÂN TẠO

## 1. Giới thiệu

Trong lĩnh vực trí tuệ nhân tạo (AI), việc đánh giá hiệu suất các mô hình học máy đòi hỏi các chỉ số toán học chuẩn mực. Bài phân tích này trình bày các metrics đánh giá quan trọng được sử dụng rộng rãi trong nghiên cứu AI hiện đại [Smith et al., 2023].

```
E[\hat{y} - y] = 0
```

## 2. Các Metric Đánh Giá Cơ Bản

### 2.1. Accuracy (Độ chính xác) accuracy = \frac{TP + TN}{TP + TN + FP + FN}

Trong đó:
- $TP$: True Positive
- $TN$: True Negative  
- $FP$: False Positive
- $FN$: False Negative

### 2.2. Precision & Recall

```
Precision = \frac{TP}{TP + FP}
Recall = \frac{TP}{TP + FN}
```

### 2.3. F1-Score (F-Measure)

$$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

## 3. Đánh giá Phân loại Đa lớp

### Confusion Matrix:
```
            Predicted
      |    0    |    1    |   K    |
Actual |--------|--------|--------|
   0   | TP₀   | FP ₁   | FPₖ   |
   1   | FN₀   | TP₁   | FPₖ   |
   ... | ...   | ...   | ...   |
```

### Macro-Average:
$$Accuracy_{macro} = \frac{1}{K}\sum_{i=1}^{K} \frac{TP_i + TN_i}{N_i}$$

## 4. Đánh giá Hồi quy

### Mean Squared Error (MSE):
$$\text{MSE} = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2$$

### Mean Absolute Error (MAE):
$$\text{MAE} = \frac{1}{N}\sum_{i=1}^{N}|y_i - \hat{y}_i|$$

### R² Coefficient:
$$R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

## 5. Đánh giá Mô hình Deep Learning

### Cross-Entropy Loss (Biến thể Softmax):
$$L = -\sum_{c=1}^{C} y_c \log(\hat{y}_c)$$

### Gradient Descent Update:
$$w_{t+1} = w_t - \eta \cdot \nabla_w L(w_t)$$

Với $\eta$ là learning rate và $\nabla_w$ là gradient theo tham số.

## 6. Phân tích Độ tin cậy (Calibration)

### Expected Calibration Error (ECE):
$$\text{ECE} = \frac{1}{|B|}\sum_{b=1}^{|B|}|N_b - P_b|\cdot\epsilon_b$$

Trong đó:
- $N_b$: Số mẫu trong bin $b$
- $P_b$: Độ tin cậy trung bình của bin $b$
- $\epsilon_b$: Error trung bình của bin $b$

## 7. Kết luận

Việc lựa chọn metric phù hợp phụ thuộc vào:
1. **Balanced accuracy**: Dữ liệu mất cân bằng
2. **Focal loss**: Class imbalance nghiêm trọng
3. **ROC-AUC**: Bài toán binary classification
4. **PR-Curve**: Dữ liệu hiếm (rare categories)

---

**Nguồn tham khảo:**
1. Smith, J., Johnson A., & Anderson B.L. (2023). *Evaluating Machine Learning Models*. Journal of AI Research, 45(3), 112-134.
2. Heidecke, M.M., et al. (2022). *Advanced Evaluation Metrics for Deep Learning*. IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(8), 4102-4120.

---

*Định dạng: Markdown - Chuẩn cho báo cáo khoa học và blog chuyên nghiệp.*