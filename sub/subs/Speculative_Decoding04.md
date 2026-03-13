# Speculative Decoding và Tối ưu hóa Drafting – Phương pháp Tăng tốc Suy luận cho Mô hình Ngôn ngữ Lớn

**© 2026 Pixiboss. Mọi quyền được bảo lưu.**  
Liên hệ: hello@pixibox.ai  

---

# Tóm tắt

Các mô hình ngôn ngữ lớn (Large Language Models – LLMs) hiện nay đạt hiệu năng rất cao trong nhiều tác vụ như sinh văn bản, lập trình, dịch máy và hỏi đáp. Tuy nhiên, quá trình suy luận (inference) của các mô hình này vẫn gặp hạn chế lớn về **độ trễ** do cơ chế sinh token tuần tự (autoregressive decoding).

Một hướng tiếp cận hiệu quả nhằm giảm độ trễ này là **Speculative Decoding**, trong đó một mô hình nhanh hơn (draft model) sinh ra các token dự đoán và mô hình lớn (target model) xác minh chúng song song. Bài viết này trình bày một phân tích toàn diện về speculative decoding, bao gồm:

- các phương pháp drafting
- các kỹ thuật verification
- chiến lược tối ưu hóa efficiency
- phương pháp context-based drafting
- dynamic tree verification

Ngoài ra, bài viết cũng phân tích các phương pháp tiên tiến như **Medusa**, **EAGLE**, **retrieval-based drafting**, và **dynamic draft tree**, đồng thời cung cấp các công thức toán học minh họa cho các cơ chế tăng tốc suy luận.

---

# 1. Giới thiệu

Quá trình sinh văn bản của LLM dựa trên mô hình xác suất chuỗi:

\[
P(x_1, x_2, ..., x_n) = \prod_{t=1}^{n} P(x_t | x_1,...,x_{t-1})
\]

Trong đó:

- \(x_t\) là token tại bước \(t\)
- mỗi token phụ thuộc vào toàn bộ lịch sử trước đó.

Điều này dẫn đến chi phí suy luận tuyến tính theo độ dài chuỗi:

\[
T_{inference} \approx O(n)
\]

Với các mô hình có hàng chục tỷ tham số, mỗi bước suy luận có thể tốn nhiều mili-giây hoặc thậm chí hàng trăm mili-giây.

**Speculative decoding** được đề xuất nhằm giảm số lần gọi mô hình lớn bằng cách sinh nhiều token trong một bước.

---

# 2. Paradigm của Speculative Decoding

Speculative decoding hoạt động theo mô hình **draft-then-verify**.

Quy trình cơ bản:

1. Draft model sinh \(k\) token dự đoán:

\[
\hat{x}_{t+1}, \hat{x}_{t+2}, ..., \hat{x}_{t+k}
\]

2. Target model kiểm tra song song các token này.
3. Các token hợp lệ được chấp nhận.

Nếu token thứ \(i\) không hợp lệ:

\[
\hat{x}_{t+i} \neq \arg\max_x P(x|x_{1:t+i-1})
\]

thì toàn bộ token phía sau bị loại bỏ.

---

# 3. Trade-off giữa Speculation Accuracy và Latency

Hiệu quả của speculative decoding phụ thuộc vào hai yếu tố:

- **Speculation accuracy**: tỉ lệ token được chấp nhận
- **Draft latency**: thời gian sinh token dự đoán

Giả sử:

- \(k\) token được draft
- \(p\) là xác suất token được chấp nhận

Số token trung bình sinh được mỗi bước:

\[
E[tokens] = 1 + p(k-1)
\]

Tốc độ tăng tốc xấp xỉ:

\[
Speedup \approx \frac{E[tokens]}{1 + C_d}
\]

Trong đó \(C_d\) là chi phí tính toán của draft model.

Do đó mục tiêu tối ưu:

\[
\max \left(\frac{E[tokens]}{Latency_{draft}}\right)
\]

---

# 4. Các phương pháp Drafting hiện đại

## 4.1 Medusa: Multi-Head Drafting

Medusa là phương pháp thêm nhiều **language modeling heads** vào mô hình gốc.

Kiến trúc:

Transformer
↓
Last Hidden State
/   |   
Head1 Head2 Head3

Mỗi head dự đoán một token tương lai:

\[
\hat{x}_{t+i} = \arg\max_x P_i(x|h_t)
\]

Trong đó:

- \(h_t\) là hidden state của transformer.

Ưu điểm:

- tái sử dụng representation đã tính toán
- latency thấp

Nhược điểm:

- các token dự đoán **không phụ thuộc lẫn nhau**

\[
P(x_{t+2}) \neq P(x_{t+2}|x_{t+1})
\]

---

## 4.2 EAGLE: Autoregressive Drafting

EAGLE cải thiện Medusa bằng cách thêm **dependency giữa các token dự đoán**.

Quá trình sinh token:

\[
x_{t+1} \sim P(x|h_t)
\]

\[
x_{t+2} \sim P(x|h_t, x_{t+1})
\]

\[
x_{t+3} \sim P(x|h_t, x_{t+1}, x_{t+2})
\]

Nhờ modeling dependency:

\[
P(x_{t+i}|x_{t+1:t+i-1})
\]

EAGLE đạt speculation accuracy cao hơn.

---

# 5. Context-Based Drafting

Một số phương pháp không sử dụng mô hình draft.

Thay vào đó chúng **tận dụng context có sẵn**.

---

## 5.1 Copy-Based Drafting

Nếu output có độ tương đồng cao với input:

\[
Sim(Input, Output) > \theta
\]

ta có thể copy trực tiếp từ input.

Ví dụ:

Input:

The pancreas of pigs produces insulin

Prefix:

The pancreas of

Draft:

pigs produces insulin

Ưu điểm:

- không cần mô hình
- latency gần như bằng 0

---

## 5.2 Retrieval-Based Drafting (RICE)

Phương pháp **RICE** mở rộng copy-based drafting bằng cách sử dụng một **corpus lớn**.

Quy trình:

1. xây dựng corpus \(C\)
2. tìm prefix tương tự

\[
prefix \in C
\]

3. sử dụng phần tiếp theo làm draft.

Draft latency lúc này:

\[
Latency_{draft} = Latency_{retrieval}
\]

---

## 5.3 Suffix Automaton Retrieval

Một phương pháp mới hơn sử dụng **Suffix Automaton** để tìm prefix hiệu quả.

Thời gian truy vấn:

\[
O(|query|)
\]

Điều này giúp retrieval cực nhanh.

---

# 6. Kết hợp nhiều phương pháp Drafting

Một phát hiện quan trọng là:

> Không có một phương pháp drafting nào tối ưu trong mọi trường hợp.

Ví dụ:

| Method | Accuracy | Latency |
|------|------|------|
| EAGLE | cao | trung bình |
| Copy | thấp | rất thấp |

Do đó có thể **kết hợp nhiều phương pháp**.

Ví dụ:

if similarity(input, output) > threshold:
use copy drafting
else:
use eagle drafting

Kết quả thực nghiệm cho thấy:

\[
Speedup_{combined} = 2.58
\]

so với

\[
Speedup_{EAGLE} = 2.38
\]

Tăng khoảng **10% tốc độ suy luận**.

---

# 7. Verification trong Speculative Decoding

Verification là bước kiểm tra các token dự đoán.

Giả sử độ dài verification tối đa là \(L\):

\[
L \leq 64
\]

Nếu \(L\) quá lớn:

\[
Latency_{verify} \uparrow
\]

Do đó cần chọn **draft token chất lượng cao**.

---

# 8. Draft Tree Verification

Thay vì kiểm tra một chuỗi token, ta có thể kiểm tra **nhiều chuỗi song song**.

Ví dụ:

I am very
I like you

Tree:

  I
 / \

am  like
|     |
very  you

Attention mask được thiết kế để mỗi nhánh chỉ nhìn thấy prefix của nó.

---

# 9. Static Draft Tree

Trong Medusa, cấu trúc tree là **cố định**.

Ví dụ:

- top-1 token được mở rộng nhiều
- top-10 token chỉ kiểm tra một bước.

Giả định:

\[
Acceptance(token) = f(position)
\]

---

# 10. Context Dependency

Thực tế cho thấy acceptance rate phụ thuộc **context**.

Ví dụ:

Context 1:

10 + 2

Token tiếp theo có thể:

=
+

Context 2:

10 + 2 =

Token tiếp theo gần như chắc chắn:

12

Do đó:

\[
P(token|context_1) \neq P(token|context_2)
\]

---

# 11. Dynamic Draft Tree (EAGLE-2)

EAGLE-2 đề xuất **dynamic tree**.

Thay vì tree cố định:

\[
Tree = f(context)
\]

Tức là:

- phân bổ tài nguyên cho token có xác suất cao
- loại bỏ token có xác suất thấp.

Ví dụ:

10 + 2 =

Tree tối ưu:

  1
  |
  2

thay vì

  1
 / \
2   3

Kết quả:

- tăng acceptance rate
- tăng số token được chấp nhận.

---

# 12. Phân tích hiệu quả

Giả sử verification capacity là \(K\).

Static tree:

\[
Accepted \approx pK
\]

Dynamic tree:

\[
Accepted \approx p'K
\]

với

\[
p' > p
\]

Do đó:

\[
Speedup_{dynamic} > Speedup_{static}
\]

---

# 13. Kết luận

Speculative decoding là một kỹ thuật quan trọng giúp tăng tốc suy luận của các mô hình ngôn ngữ lớn mà không làm thay đổi phân phối đầu ra của mô hình.

Các hướng phát triển chính gồm:

- multi-head drafting (Medusa)
- autoregressive drafting (EAGLE)
- retrieval-based drafting
- dynamic draft tree verification

Trong tương lai, việc **kết hợp nhiều phương pháp drafting** và **tối ưu verification theo context** sẽ tiếp tục đóng vai trò quan trọng trong việc cải thiện hiệu năng suy luận của các hệ thống AI quy mô lớn.

# Speculative Decoding: Tăng tốc suy luận cho mô hình ngôn ngữ lớn và các hệ sinh tự hồi quy

**© 2026 Pixiboss. Mọi quyền được bảo lưu.**  
Liên hệ: hello@pixibox.ai  

---

# Tóm tắt

Sự phát triển của **Large Language Models (LLMs)** đã mở ra nhiều khả năng mới trong xử lý ngôn ngữ tự nhiên, sinh mã nguồn, và hệ thống hỏi đáp. Tuy nhiên, quá trình **suy luận tự hồi quy (autoregressive inference)** vẫn là nút thắt hiệu năng do phải sinh từng token tuần tự.

**Speculative Decoding** là một kỹ thuật tăng tốc suy luận mà vẫn giữ được chất lượng đầu ra gần như không thay đổi. Phương pháp này dựa trên ý tưởng sử dụng một **draft model** để dự đoán trước nhiều token và sau đó dùng **target model** để xác minh song song.

Bài viết này tổng hợp và phân tích các hướng nghiên cứu quan trọng trong speculative decoding, bao gồm:

- mô hình dự đoán draft
- phương pháp ước lượng xác suất chấp nhận
- dynamic verification tree
- judge decoding (xác minh theo đánh giá của con người)
- các ứng dụng trong hệ thống gợi ý và sinh ảnh

Ngoài ra, bài viết trình bày các mô hình tiêu biểu như **Medusa**, **EAGLE**, **EAGLE-2**, và các hướng mở rộng speculative decoding sang các lĩnh vực khác của trí tuệ nhân tạo.

---

# 1. Giới thiệu

Các mô hình ngôn ngữ hiện đại sinh văn bản theo phân phối xác suất chuỗi:

\[
P(x_{1:n}) = \prod_{t=1}^{n} P(x_t | x_1, x_2, ..., x_{t-1})
\]

Trong đó:

- \(x_t\) là token tại bước \(t\)
- mỗi token phụ thuộc vào toàn bộ lịch sử trước đó.

Điều này dẫn đến chi phí suy luận tuyến tính:

\[
T(n) = O(n)
\]

Đối với các mô hình lớn như:

- LLaMA
- GPT
- Qwen

chi phí tính toán mỗi bước có thể rất lớn.

Speculative decoding giúp giảm số lần gọi mô hình lớn bằng cách sinh nhiều token trong một lần xác minh.

---

# 2. Paradigm Draft–Verify

Quy trình speculative decoding gồm hai giai đoạn:

### 1. Draft

Draft model dự đoán \(k\) token:

\[
\hat{x}_{t+1}, \hat{x}_{t+2}, ..., \hat{x}_{t+k}
\]

### 2. Verify

Target model kiểm tra các token song song.

Nếu token đầu tiên không khớp:

\[
\hat{x}_{t+1} \neq \arg\max_x P(x|x_{1:t})
\]

thì toàn bộ chuỗi bị loại.

Nếu khớp liên tiếp:

\[
\hat{x}_{t+i} = x_{t+i}
\]

thì ta chấp nhận nhiều token cùng lúc.

---

# 3. Mô hình xác suất chấp nhận

Giả sử:

- \(k\) token được draft
- \(p_i\) là xác suất token thứ \(i\) được chấp nhận

Kỳ vọng số token chấp nhận:

\[
E[T] = \sum_{i=1}^{k} P(\text{token } i \text{ accepted})
\]

Nếu giả sử xác suất giống nhau:

\[
E[T] \approx k \cdot p
\]

Speedup gần đúng:

\[
Speedup \approx \frac{E[T]}{Latency_{draft} + Latency_{verify}}
\]

---

# 4. Ước lượng xác suất chấp nhận

Một câu hỏi quan trọng:

**Làm sao biết trước token nào có khả năng được chấp nhận?**

Nghiên cứu **GLIDE (ACL 2024)** chỉ ra rằng:

> Confidence của draft model có tương quan cao với acceptance rate.

Nếu:

\[
P_{draft}(x) > 0.9
\]

thì:

\[
P_{accept}(x) \approx 0.9
\]

Do đó có thể dùng **xác suất dự đoán** làm thước đo giá trị token.

---

# 5. EAGLE-2: Value-based Draft Tree

EAGLE-2 đề xuất đánh giá giá trị của token theo đường đi trong cây dự đoán.

Giá trị token:

\[
V(node) = \prod_{i=1}^{d} p_i
\]

Trong đó:

- \(p_i\) là confidence tại mỗi bước
- \(d\) là độ sâu node trong cây.

Các token có giá trị thấp sẽ bị loại bỏ.

Thuật toán:

	1.	xây dựng draft tree
	2.	tính value cho từng node
	3.	sort theo value
	4.	giữ top-k nodes

Nhờ đó:

- giảm token chất lượng thấp
- tăng số token được chấp nhận.

Thực nghiệm cho thấy:

\[
Speedup_{EAGLE2} \approx 20\%-40\% \text{ so với EAGLE}
\]

---

# 6. Giới hạn lý thuyết của Speculative Decoding

Nhiều nghiên cứu chỉ ra rằng speculative decoding có **giới hạn trên (upper bound)**.

Giả sử:

- draft model có độ chính xác rất cao
- verification hoàn toàn chính xác

thì số token chấp nhận trung bình:

\[
E[T] \approx 4 \sim 5
\]

Điều này dẫn tới speedup tối đa:

\[
Speedup_{max} \approx 4 - 5\times
\]

Nguyên nhân chính:

**ràng buộc verification quá nghiêm ngặt**

token phải **giống hoàn toàn** với output của target model.

---

# 7. Judge Decoding: Relaxed Verification

Nghiên cứu mới **Judge Decoding (ICLR 2025)** đề xuất thay đổi tiêu chí verification.

Thay vì yêu cầu:

\[
x_{draft} = x_{target}
\]

ta yêu cầu:

\[
Quality(x_{draft}) \geq \theta
\]

Trong đó quality được đánh giá theo **human judgment**.

---

# 8. Human Judgment Model

Judge decoding huấn luyện một **judgment head**.

Cho hidden state \(h_i\):

\[
score_i = \sigma(W h_i + b)
\]

Trong đó:

- \(score_i \in [0,1]\)
- biểu thị mức độ phù hợp với đánh giá con người.

Token được chấp nhận nếu:

\[
score_i > \tau
\]

---

# 9. Kết quả thực nghiệm

Với strict verification:

\[
MeanAcceptedTokens \approx 4.5
\]

Với judge decoding:

\[
MeanAcceptedTokens \approx 20
\]

Điều này mở ra khả năng speedup lớn hơn nhiều.

---

# 10. Ứng dụng trong Generative Recommendation

Hệ thống gợi ý truyền thống là bài toán **matching**:

\[
score(u,i)
\]

Trong đó:

- \(u\) là user
- \(i\) là item.

Generative recommendation biến nó thành bài toán sinh chuỗi:

\[
P(item | history)
\]

Input:

user behavior sequence

Output:

recommended items

Tuy nhiên hệ thống gợi ý cần **top-K results**.

Do đó verification chuyển từ:

\[
N \rightarrow 1
\]

sang:

\[
N \rightarrow K
\]

Điều này làm giảm acceptance rate.

Giải pháp:

- KL-divergence distillation
- relaxed verification.

---

# 11. Ứng dụng trong Autoregressive Image Generation

Ảnh có thể biểu diễn bằng chuỗi **visual tokens**:

\[
I \rightarrow (v_1, v_2, ..., v_n)
\]

thông qua mô hình **VQ-VAE**.

Sinh ảnh trở thành bài toán:

\[
P(v_t | v_{<t}, text)
\]

---

# 12. Vấn đề Token Ambiguity

Trong sinh ảnh:

\[
P(top1) \ll P(top1)_{text}
\]

tức là xác suất token cao nhất thấp hơn nhiều so với text.

Nguyên nhân:

- nhiều visual token gần nhau trong latent space.

Giải pháp:

cho phép thay thế token bằng **neighbors**.

Acceptance condition mới:

\[
v \in B_k(\hat{v})
\]

Trong đó:

- \(B_k\) là tập neighbor tokens.

Kết quả:

- tăng acceptance rate
- giảm lỗi hình ảnh.

---

# 13. Xu hướng nghiên cứu tương lai

### 1. Từ multi-model → single-model

Self-drafting:

- layer skipping
- multi-token prediction.

---

### 2. Từ training → pretraining

LLM tương lai có thể học trực tiếp:

multi-token prediction

trong pretraining.

---

### 3. Từ strict verification → relaxed verification

Thay vì:

match target model

sẽ chuyển sang:

match human judgment

---

# 14. Kết luận

Speculative decoding là một trong những kỹ thuật quan trọng nhất để tăng tốc suy luận của các mô hình sinh tự hồi quy.

Các hướng phát triển chính gồm:

- efficient drafting (Medusa, EAGLE)
- dynamic verification (EAGLE-2)
- relaxed verification (Judge Decoding)
- cross-domain applications

Trong tương lai, speculative decoding có thể trở thành **chuẩn tăng tốc suy luận** cho nhiều hệ thống AI lớn.

---

# Tài liệu tham khảo

1. Leviathan et al., *Fast Inference from Transformers via Speculative Decoding*, ICML 2023  
2. Cai et al., *Medusa: Efficient LLM Inference with Multi-head Decoding*, 2023  
3. Li et al., *EAGLE: Efficient Autoregressive Generation*, 2024  
4. Li et al., *EAGLE-2: Dynamic Draft Tree for Speculative Decoding*, 2024  
5. Chen et al., *Judge Decoding: Human-aligned Speculative Decoding*, ICLR 2025 (under review)  
6. Xia et al., *Draft & Verify: Lossless Acceleration of LLMs*, 2023  
7. Stern et al., *Blockwise Parallel Decoding*, NeurIPS 2018  
8. Gu et al., *Non-Autoregressive Machine Translation*, ICLR 2018  


1. Leviathan et al., *Fast Inference from Transformers via Speculative Decoding*, ICML 2023.  
2. Cai et al., *Medusa: Simple LLM Inference Acceleration Framework*, 2023.  
3. Li et al., *EAGLE: Efficient Autoregressive Generation*, 2024.  
4. Xia et al., *Draft & Verify: Lossless Acceleration of LLMs*, 2023.  
5. Stern et al., *Blockwise Parallel Decoding*, NeurIPS 2018.  
6. Gu et al., *Non-Autoregressive Neural Machine Translation*, ICLR 2018.

---

**© 2026 Pixiboss. Mọi quyền được bảo lưu.**  
Liên hệ: hello@pixibox.ai