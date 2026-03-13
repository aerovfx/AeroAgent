# Tự Động Đo Hiệu Suất Mô Hình Ngôn Ngữ Lớn: Phương Pháp Luận và Ứng Dụng Thực Tiễn

**Bản ghi khoa học · 2026 PixelBox**  
*Mọi quyền được bảo lưu © 2026 Pixiboss | hello@pixibox.ai*

---

## Tóm Tắt

Bài viết này thảo luận về hệ thống các chỉ số tự động trong việc đánh giá Mô Hình Ngôn Ngữ Lớn (LLM) trên nền tảng Vertex AI. Chúng ta xem xét phương pháp luận chuẩn hóa cho quá trình thu thập, tính toán, và so sánh điểm hiệu suất của mô hình thông qua các nhiệm vụ phân loại, tóm tắt, trả lời câu hỏi, và tạo văn bản tự động.

---

## 1. Giới Thiệu Các Chỉ Số Tự Động

### 1.1 Mục Đích Của Đánh Giá Tự Động

Trong nghiên cứu học thuật và phát triển công nghệ AI, việc đánh giá hiệu suất mô hình LLM đòi hỏi các chỉ số định lượng khách quan để:

- Tối ưu hóa chiến lược điều chỉnh tham số
- Xác định điểm yếu của mô hình trên các task cụ thể
- Đảm bảo kết quả có thể so sánh giữa các nghiên cứu khác nhau

```
[Input (Prompt) + Output (Generated)] → [Metrics] → [Analysis/Improvement]
```

### 1.2 Khung Đánh Giá Vertex AI

Vertex AI hiện hỗ trợ các mô hình **PaLM** và **Gemini**, phù hợp với các tác vụ:
- Phân loại (**Classification**)
- Tóm tắt văn bản (**Summarization**)  
- Hỏi đáp (**QA**)
- Tạo nội dung (**Text Generation**)

> *Quy trình chuẩn:* Dữ liệu → Upload GCP → Chạy Pipeline → Tính điểm số.

---

## 2. Các Chỉ Số Đánh Giá Chính

### 2.1 Phân Loại (Classification Metrics)

```math
F_1 = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
```

| Chỉ số | Định nghĩa | Ứng dụng |
|--------|------------|----------|
| **Micro-F1** | Tổng hợp toàn bộ tập dữ liệu (global) | Đa lớp (multi-class), ưu tiên các class ít mẫu |
| **Macro-F1** | Trung bình cộng qua từng class | Công bằng qua số loại, quan tâm đến mọi class |

Mỗi lớp `k` trong mô hình đa lớp có công thức:

```math
F_{1}^{(k)} = \frac{2TP_k}{2TP_k + FP_k + FN_k}
\quad (\text{Macro-F1} = \frac{1}{N} \sum_{k=1}^N F_1^{(k)})
```

### 2.2 Tóm Tắt Văn Bản (Summarization Metrics)

**ROUGE-L**: Dùng độ dài chuỗi chung dài nhất (LCS – Longest Common Subsequence).

```math
\text{ROUGE-L}(A, B) = \frac{\text{LCS}(A, B)}{\max(|A|, |B|)}
```

Trong đó: `A` là câu tóm tắt, `B` là ground truth.

### 2.3 Câu Hỏi Trả Lời (QA Accuracy)

```math
\text{Exact Match} = \begin{cases}
1 & \text{nếu } \hat{y} = y \\
0 & \text{nếu } \hat{y} \neq y
\end{cases}
```

Tham số `β` để điều chỉnh độ chính xác:

```math
F_β = (1+β^2)f_1 f_2 / (f_1 + β^2 f_2)
```

### 2.4 Tạo Văn Bản (Generation Metrics - BLEU)

Đo lường chất lượng từ ngữ và cú pháp của văn bản:

```math
\text{BLE}U = \exp\left(\sum_{i=1}^{n}\frac{C}{R_i} \log p_i\right)
$$  $$
= \frac{\exp\left(\sum_{n=4}^{N} g_n \log \phi_n\right)}{w_0}
```

Trong đó:
`Rₙ` – Số lần xuất hiện của từ `n-gram`
`C` – Sự giống nhau giữa văn bản gốc và tham chiếu.

---

## 3. Quy Trình Thực Thi Đánh Giá

### 3.1 Bước Chuẩn Bị Dữ Liệu

```mermaid
graph LR; 
A[ Prompt + Ground Truth ] --> B[Tập dữ liệu đánh giá]; 
B --> C[Tối thiểu 10 mẫu ví dụ]; 
C --> D[Tiêu chuẩn hóa JSON]
```

- Mỗi dòng gồm: {prompt, expected_output}
- Tập dữ liệu tối thiểu **≥10 cặp mẫu** để đại diện cho task.

### 3.2 Quy Trình Uploading và Chạy Mô Hình

```python
from vertexai.evaluations import EvaluationPipeline

# Chuẩn bị tập dữ liệu
data = {
    "inputs": ["X1", "X2", ...],
    "targets": ["Y1_gt", "Y2_gt", ...]
}

# Đưa vào bộ nhớ GCP
storage_path = gs://bucket-evaluations/"dataset-name"

# Chạy đánh giá với Vertex AI
task_type = "classification"
model_uri = gcs://vertex-ai-models/palm2
pipeline.run(
  evaluation_dataset_path,
  task_type=task_type,
  model=model_uri
)
```

---

## 4. Ưu Điểm Của Đánh Giá Tự Động

1. **Tiết kiệm thời gian**: Giảm thao tác thủ công trong kiểm tra kết quả.
2. **Khách quan**: Không phụ thuộc vào đánh giá chủ quan của con người.
3. **Chuẩn hóa**: Kết quả có thể so sánh trên nền tảng và bài báo.
4. **Nhanh chóng phản hồi**: Xác định khu vực cần tối ưu trong vòng vài phút.

| Ưu điểm | Thời gian giảm | Độ tin cậy tăng | Công cụ hỗ trợ |
|---------|---------------|-----------------|------------------|
| Tự động tính số liệu | ~90% | +40%BLEU-F1 | Python API Vertex AI |

---

## 5. Kết Luận

Các chỉ số tự动 đóng vai trò quan trọng trong tối ưu hóa hiệu suất LLM:

- `Micro-F1`, `Macro-F1`: Tối ưu phân loại đa lớp
- `ROUGE-L`: Đo độ gần đúng của tóm tắt
- `Exact Match`: Đánh giá câu trả lời chính xác
- `BLEU`: Định lượng sinh văn bản chất lượng

Vertex AI cung cấp framework hoàn chỉnh cho các nghiên cứu đánh giá mô hình, phù hợp với quy chuẩn học thuật.

---

## 6. Tài Liệu Tham Khảo

1. **Tosh (2025).** _Automatic Metrics in Vertex AI LLM Evaluation_ [Video]
2. **Lin, C. Y. (2004).** ROUGE: A Package for Automatic Evaluation of Summarization. *EMNLP*, 89–94.
3. **Papineni, K., et al. (2002).** BLEU: a Method for Automatic Evaluation of Machine Translation. *ACL*, 311–318.
4. **Kuhnert, D. (2026).** Micro-F1, Macro-F1: Benchmarking Multi-Class Classification Tasks. *ICML Workshop*.
5. **Google Cloud AI Lab.** Vertex AI Evaluation Pipelines Documentation, 2026. [https://cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai)

---

**© 2026 Pixiboss. Mọi quyền được bảo lưu.**  
Liên hệ: hello@pixibox.ai