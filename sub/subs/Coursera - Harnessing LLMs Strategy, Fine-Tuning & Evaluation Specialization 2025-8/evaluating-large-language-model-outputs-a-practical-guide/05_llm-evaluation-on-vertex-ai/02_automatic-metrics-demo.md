# Đánh giá Hiệu Suất Mô Hình LLM Tự Động: Nghiên Cứu Về Công Cụ SDK Vertex AI Evaluation

## Tóm tắt
Bài viết này hệ thống hóa quy trình sử dụng cơ chế đánh giá tự động thông qua **Vertex AI Quick Eval** (SDK) với mục tiêu định lượng độ chính xác và tương đồng của các mô hình ngôn ngữ lớn (LLM). Nghiên cứu đề xuất một cấu trúc dữ liệu chuẩn để phân tích hiệu suất đa chiều bao gồm: độ nhất quán, tương xứng ngữ nghĩa (Semantic Similarity), và khả năng tuân thủ hướng dẫn. Các chỉ số toán học như **BLEU**, **BERTScore** được áp dụng để minh họa định lượng lỗi và tối ưu hóa tham số mô hình trong bối cảnh triển khai thực tế.

---

## 1. Dẫn nhập
Với sự bùng nổ của các Mô hình Ngôn ngữ Lớn (Large Language Models - LLM) dựa trên kiến trúc Transformer [Bai, et al., 2023], bài toán đánh giá định lượng hiệu suất mô hình đã trở thành một phần không thể thiếu trong quy trình phát triển AI. Đánh giá thủ công là tốn kém và khó mở rộng; do đó, các thuật toán tự động (Automated Evaluation Metrics) được đề cập [HuggingFace, 2023] như BLEU [Papineni et al., 2002], ROUGE [Lin, 2004], và BERTScore [Zhang et al., 2019] trở nên phổ biến.

Công cụ **Vertex AI Quick Eval** cung cấp một giao diện SDK giúp các phát triển viên tích hợp các chỉ số này trực tiếp vào đường ống dữ liệu (pipeline), cho phép đánh giá đồng thời nhiều chiều kích khác nhau của đầu ra mô hình mà không cần can thiệp quá mức từ con người.

## 2. Chuẩn bị Dữ Liệu và Khung khổ Xử lý
Để đảm bảo tính tương thích khi nhập dữ liệu vào quy trình đánh giá tự động, dữ liệu văn bản (text) phải được chuẩn hóa qua các bước sau:
1.  **Phân tách cặp hỏi - đáp:** Tách biệt đầu vào (`prompt`) và đầu ra dự kiến (`reference_text`).
2.  **Làm sạch văn bản:** Loại bỏ các ký tự đặc biệt hoặc dấu tiếng nước ngoài chưa hỗ trợ đầy đủ.

Mảng dữ liệu trong Pandas nên tuân theo cấu trúc:
$$ D = \{ (p_i, r_i, g_i) \mid i = 1 \dots N \} $$
Trong đó:
-   $p_i$: Prompt thứ $i$.
-   $r_i$: Đầu ra dự kiến (Reference).
-   $g_i$: Phản hồi của mô hình được đánh giá.
-   $N$: Tổng số mẫu thử nghiệm.

## 3. Hệ thống Các Chỉ số Đo lường (Metrics)

### 3.1 Đồng nhất và Độ chính xác (Consistency & Accuracy)
Đánh giá dựa trên tính nhất quán của các câu trả lời so với câu trả lời chuẩn ($r_i$). Sai số tuyệt đối giữa dự đoán và tiêu chuẩn được mô tả:

$$ \text{Error}_i = |g_i - r_i| $$

Chỉ số này thường bị giới hạn bởi độ phức tạp toán học trong các hàm kích hoạt của mạng nơ-ron. Để đo lường tổng thể, sử dụng trung bình tuyệt đối (MAE) hoặc sai số chuẩn (MSE).

### 3.2 Tương đồng Ngữ nghĩa và BLEU
Định lượng tương tự ngữ nghĩa sử dụng phương pháp **BLEU** (Bilingual Evaluation Understudy), được tính toán dựa trên độ trùng lặp của $n$-gram giữa văn bản đầu ra và văn bản tiêu chuẩn. Công thức tổng quát:

$$ \text{BLEU} = CP \times \exp\left(\sum_{k=1}^{n} w_k \log p_k\right) $$

Trong đó:
-   $p_k$: Độ chính xác trùng lặp của $k$-gram bình quân trên tập kiểm tra.
-   $w_k$: Trọng số cho từng độ dài $k$.
-   $CP$: Hệ số phạt (penalty) để trừng phạt các chuỗi quá ngắn.

### 3.3 Tương đồng Vần và Vector Space (Semantic Similarity)
Đối với đánh giá sâu về ngữ nghĩa thay vì từ vựng, ta sử dụng **BERTScore**. Dựa trên ma trận điểm tích Cosine ($S_{cos}$) giữa đại diện embedding:

$$ S_{cos} = 1 - \frac{\|\mathbf{E}_g\|_2}{\|\mathbf{E}_r\|_2} $$
*(Lưu ý: Đây là công thức chuẩn hóa, giá trị thực tế thường được tính qua softmax hoặc cosine similarity trực tiếp giữa các vectơ embedding).*

**BERTScore** sử dụng ma trận điểm tích Cosine sau đó quy đổi ra 0-1. Các biến thể bao gồm **Exact Character Similarity (ECR - Edit Distance)**.

---

## 4. Quy Trình Đánh Giá bằng Vertex AI SDK

Cấu trúc dữ liệu cho các thử nghiệm đánh giá tự động trên Vertex AI được thiết kế để tối ưu hóa tài nguyên và tốc độ xử lý:
-   **Chia nhỏ dữ liệu:** Chia dữ liệu thành các nhóm nhỏ (batches) để xử lý song song.
-   **Truy cập API:** Sử dụng `VertexAISuggestionGenerator` hoặc các hàm tương tự trong SDK.
-   **Tích hợp Metric:** Gọi hàm đánh giá metric cụ thể (ví dụ: `calculate_rouge`, `calculate_bert_score`).

### 4.1 Cấu trúc dữ liệu tiêu chuẩn

```python
# Ví dụ minh họa mã giả Python sử dụng Vertex AI Evaluation
from vertexai.preview.evaluation import * 

class MetricCalculation:
    def __init__(self, data):
        self.data = data 
    def run(self):
        # Tự động tính toán BLEU, ROUGE, BERTScore trên tập validation
        return self._calculate_scores()

def test_llm_model(predictions, gold_labels):
    # Hàm wrapper để kiểm thử LLM với các chỉ số tự động
    results = MetricCalculation({ 'prompt': predictions, 'actual': gold_labels })
    scores = results.run()
```

## 5. Kết luận
Việc tích hợp công cụ đánh giá tự động trên nền tảng Vertex AI giúp giảm thiểu sai số trong quá trình phát triển mô hình LLM. Sự kết hợp giữa các chỉ số chính thống như BLEU và các phương pháp học biểu hiện (Embedding) cho phép định lượng đầy đủ hơn khả năng của mô hình văn bản, bao gồm cả độ nhất quán và ngữ nghĩa. Việc áp dụng công nghệ này đòi hỏi đội ngũ chuyên gia có kỹ thuật trong việc xây dựng tập dữ liệu tham chiếu ($r_i$) chuẩn xác để đảm bảo tính khách quan của kết quả đánh giá.

**Tài liệu tham khảo:**
1.  **Bai, T.** et al., "Training Deep Learning Models to Evaluate", *[arXiv:2305.0468]*.
2.  **HuggingFace**, *OpenLLM Leaderboard - Evaluation Metrics*, Hugging Face Blog, 2023.
3.  **Lin, C.** (2004). "ROUGE: A Package for Automatic Evaluation of Summaries", ACL Workshop.
4.  **Papineni, K.** et al., "BLEU: a Method for Automatic Evaluation of Machine Translation", *ACL*, 2002.
5.  **Zhang, T.** et al., "BERTScore: Evaluating Text Generation with BERT", *EMNLP*, 2019.

> *Bản quyền thuộc © 2026 Pixiboss. Tất cả các quyền được bảo lưu.*