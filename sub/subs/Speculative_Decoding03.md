
Speculative Decoding: Tăng tốc suy luận cho Mô hình Ngôn ngữ Lớn

© 2026 Pixiboss. Mọi quyền được bảo lưu.
Liên hệ: hello@pixibox.ai

⸻

Tóm tắt

Sự phát triển của mô hình ngôn ngữ lớn (Large Language Models - LLMs) đã tạo ra những bước tiến đáng kể trong nhiều lĩnh vực như xử lý ngôn ngữ tự nhiên, lập trình tự động và trợ lý AI. Tuy nhiên, quá trình suy luận (inference) của các mô hình này thường có độ trễ cao do cơ chế tự hồi quy (autoregressive decoding), trong đó các token được sinh tuần tự từng bước.

Một hướng tiếp cận nổi bật nhằm giải quyết vấn đề này là Speculative Decoding, một phương pháp cho phép dự đoán nhiều token trước bằng một mô hình nhanh hơn và sau đó xác thực song song bằng mô hình mục tiêu. Bài viết này trình bày tổng quan về kiến trúc speculative decoding, phân loại các phương pháp drafting và verification, đồng thời phân tích các phương pháp tối ưu hoá nhằm đạt được tốc độ suy luận cao mà vẫn giữ nguyên phân phối đầu ra của mô hình.

⸻

1. Giới thiệu

Trong các mô hình ngôn ngữ lớn, quá trình sinh văn bản thường dựa trên xác suất điều kiện:

P(x_1, x_2, ..., x_n) = \prod_{t=1}^{n} P(x_t | x_1, x_2, ..., x_{t-1})

Trong đó:
	•	x_t là token tại bước t
	•	mỗi token phụ thuộc vào toàn bộ các token trước đó.

Cơ chế này dẫn đến độ trễ suy luận tuyến tính theo độ dài chuỗi:

T_{inference} \propto n

Với các mô hình có hàng chục hoặc hàng trăm tỷ tham số, thời gian tính toán cho mỗi bước suy luận trở nên rất lớn.

Để giảm độ trễ này, Speculative Decoding được đề xuất nhằm:
	•	dự đoán trước nhiều token
	•	xác minh chúng song song
	•	giảm số lần gọi mô hình lớn.

⸻

2. Khái niệm Speculative Decoding

Speculative decoding là một paradigm “draft-then-verify”.

Quy trình cơ bản gồm hai thành phần:
	1.	Draft Model
	2.	Target Model (Verifier)

Quy trình hoạt động:
	1.	Draft model sinh ra k token dự đoán:

\hat{x}_{t+1}, \hat{x}_{t+2}, ..., \hat{x}_{t+k}
	2.	Target model kiểm tra song song các token này.
	3.	Các token hợp lệ được chấp nhận.

Nếu một token không hợp lệ:
	•	token đó và tất cả token phía sau bị loại bỏ
	•	target model tiếp tục sinh token đúng.

⸻

3. Phương pháp Drafting

Các phương pháp drafting được chia thành hai nhóm chính.

⸻

3.1 Independent Drafting

Independent drafting sử dụng một mô hình hoặc hệ thống riêng để tạo token dự đoán.

3.1.1 Small Language Model

Một mô hình nhỏ M_d được sử dụng để dự đoán token.

\hat{x}_{t+i} \sim P_d(x | x_{1:t+i-1})

Trong đó:
	•	P_d là phân phối xác suất của draft model.

Yêu cầu quan trọng:
	•	draft model và target model phải dùng cùng tokenizer.

Nếu tokenizer khác nhau:

token_{draft} \neq token_{target}

quá trình xác minh sẽ không khả thi.

⸻

3.1.2 Context Retrieval

Phương pháp này không cần mô hình.

Ý tưởng:
	1.	Tìm các đoạn văn trong corpus có prefix giống với input.
	2.	Thu thập các phần tiếp theo.
	3.	Xây dựng trie tree.

Ví dụ:

prefix: f_lambda_num

Corpus trả về:

in range
in range(len
in list

Trie:

      in
     / \
  range list

Xác suất token có thể được ước lượng:

P(token) = \frac{freq(token)}{\sum freq(tokens)}

⸻

3.1.3 Copy from Input

Trong nhiều tác vụ như:
	•	question answering
	•	editing
	•	summarization

Output có độ trùng lặp cao với input.

Giả sử input:

... comes from the pancreas of pigs

Khi prefix khớp:

comes from the

các token tiếp theo có thể được copy trực tiếp.

⸻

3.2 Self-Drafting

Self-drafting sử dụng chính mô hình mục tiêu để tạo token dự đoán.

⸻

3.2.1 Extra Heads

Thêm nhiều head dự đoán token trong transformer.

Ví dụ:

Head	Prediction
1	x_{t+1}
2	x_{t+2}
3	x_{t+3}

Tất cả được dự đoán cùng lúc:

\hat{x}_{t+i} = Head_i(h_t)

trong đó h_t là hidden state của transformer.

Các nghiên cứu tiêu biểu:
	•	Blockwise Parallel Decoding (2018)
	•	Medusa (2023)

⸻

3.2.2 Layer Skipping

Trong giai đoạn drafting, một số layer transformer được bỏ qua.

Giả sử mô hình có L layer.

Vector lựa chọn layer:

s = (s_1, s_2, ..., s_L)

với:

s_i =
\begin{cases}
1 & sử dụng layer \\
0 & bỏ qua layer
\end{cases}

Mục tiêu tối ưu:

\max_s \frac{AcceptanceRate(s)}{Latency(s)}

⸻

3.2.3 Mask Predict

Một phương pháp khác là parallel decoding bằng mask prediction.

Thay vì sinh token tuần tự:

prefix + [MASK][MASK][MASK]

Model dự đoán đồng thời:

x_{t+1}, x_{t+2}, x_{t+3}

Sau mỗi iteration:

x^{(k+1)} = f(x^{(k)})

Quá trình lặp đến khi hội tụ.

⸻

4. Verification

Sau khi drafting, target model thực hiện verification song song.

⸻

4.1 Lossless Verification

Token được chấp nhận nếu nó khớp top-1 prediction.

\hat{x}_t = \arg\max_x P(x|prefix)

Nếu draft token khác:

x_{draft} \neq \hat{x}_t

token bị loại bỏ.

Ưu điểm:
	•	đảm bảo output giống hệt mô hình gốc.

⸻

4.2 Approximate Verification

Thay vì top-1, cho phép token nằm trong top-k.

x_{draft} \in TopK(P(x|prefix))

Phương pháp này:
	•	tăng tốc độ
	•	nhưng thay đổi phân phối đầu ra.

⸻

5. Speculative Sampling

Trong trường hợp sampling, mục tiêu là bảo toàn phân phối:

P_{target}(x)

Nếu token bị từ chối, mô hình thực hiện resampling.

⸻

6. Token Tree Verification

Thay vì một chuỗi token, ta có thể tạo nhiều chuỗi candidate.

Ví dụ:

I am very
I like you

Cây token:

      I
     / \
   am  like
   |     |
  very  you

Target model có thể xác minh cả cây trong một forward pass.

⸻

7. Phân tích tốc độ

Giả sử:
	•	k token được draft
	•	p là tỉ lệ chấp nhận.

Số token trung bình mỗi bước:

E[tokens] = 1 + p(k-1)

Speedup xấp xỉ:

Speedup = \frac{k}{1 + (1-p)k}

Khi:

p > 0.5

speculative decoding thường mang lại tăng tốc đáng kể.

⸻

8. Ứng dụng thực tế

Speculative decoding được áp dụng trong:
	•	hệ thống chatbot
	•	AI coding assistants
	•	inference server (vLLM, TensorRT-LLM)
	•	dịch máy
	•	tìm kiếm ngữ nghĩa

Các hệ thống production thường đạt:

2x – 5x inference speedup


⸻

9. Kết luận

Speculative decoding là một kỹ thuật quan trọng giúp tăng tốc suy luận của các mô hình ngôn ngữ lớn mà không làm thay đổi phân phối đầu ra của mô hình. Bằng cách kết hợp giữa drafting và verification, phương pháp này cho phép sinh nhiều token trong một bước, giảm đáng kể độ trễ của quá trình sinh văn bản.

Trong tương lai, các hướng nghiên cứu tiềm năng bao gồm:
	•	thiết kế draft model tối ưu
	•	adaptive speculation
	•	tích hợp sâu với GPU kernel
	•	speculative decoding cho multimodal models.



10. Tối ưu hóa Speculative Decoding: Efficient Drafting

Mục tiêu cốt lõi của speculative decoding là tăng tốc suy luận (inference acceleration) của mô hình ngôn ngữ lớn. Tuy nhiên, hiệu quả của phương pháp này phụ thuộc vào sự cân bằng giữa hai yếu tố chính:
	1.	Speculation Accuracy – tỉ lệ token dự đoán được chấp nhận.
	2.	Drafting Latency – thời gian cần thiết để sinh các token dự đoán.

Một chiến lược speculative decoding hiệu quả cần tối ưu hóa cả hai yếu tố này.

⸻

10.1 Trade-off giữa Accuracy và Latency

Giả sử trong mỗi bước suy luận:
	•	mô hình draft sinh k token
	•	m token được target model chấp nhận

Khi đó:

m \leq k

Tốc độ suy luận trung bình có thể được ước lượng:

Speedup \approx \frac{k}{1 + C_d}

Trong đó:
	•	C_d là chi phí tính toán của draft model so với target model.

Nếu C_d quá lớn, lợi ích từ speculative decoding sẽ giảm.

Ví dụ:

Tokens drafted	Tokens accepted	Speedup
10	10	~10×
10	5	~5×
10	1	~1×

Do đó mục tiêu tối ưu là:

\max \left( \frac{E[m]}{Latency_{draft}} \right)

⸻

11. Efficient Drafting Strategies

Các nghiên cứu gần đây đề xuất một hướng tiếp cận gọi là Efficient Drafting.

Khác với các phương pháp trước đó:
	•	không thay đổi kiến trúc mô hình lớn
	•	không tăng kích thước draft model

Thay vào đó, chúng tận dụng:
	•	context
	•	representation đã được tính toán
	•	thông tin nội bộ của transformer.

⸻

12. Medusa: Multi-Head Speculative Decoding

Một trong những phương pháp tiêu biểu là Medusa.

Thay vì sử dụng một draft model riêng, Medusa thêm nhiều language modeling heads vào mô hình.

Kiến trúc cơ bản:

Embedding
    ↓
Transformer Layers
    ↓
Last Hidden State
   / | \
Head1 Head2 Head3

Mỗi head dự đoán một token khác nhau.

Ví dụ:

Head	Token Prediction
Head 1	x_{t+1}
Head 2	x_{t+2}
Head 3	x_{t+3}

Công thức dự đoán:

\hat{x}_{t+i} = \arg\max_x P_i(x|h_t)

Trong đó:
	•	h_t là hidden representation của token cuối.

⸻

12.1 Ưu điểm của Medusa

Medusa có hai lợi thế chính:

1. Tái sử dụng biểu diễn

Thay vì tính lại transformer layers, Medusa tận dụng hidden state:

h_t = Transformer(x_{1:t})

Do đó chi phí tính toán gần như chỉ nằm ở các feed-forward heads.

⸻

2. Latency thấp

Các head chỉ là các mạng nhỏ:

y = W h_t + b

nên chi phí tính toán rất thấp.

⸻

12.2 Hạn chế của Medusa

Một nhược điểm của Medusa là thiếu phụ thuộc giữa các token dự đoán.

Cụ thể:

x_{t+2} \not\sim P(x_{t+2} | x_{t+1})

Điều này xảy ra vì các token được sinh song song theo cách non-autoregressive.

Hệ quả:
	•	speculation accuracy bị giới hạn.

⸻

13. EAGLE: Autoregressive Drafting

Một phương pháp mới hơn là EAGLE, được xem là state-of-the-art trong speculative decoding.

EAGLE giải quyết vấn đề phụ thuộc token bằng cách sử dụng draft model autoregressive.

⸻

13.1 Kiến trúc EAGLE

Sau khi lấy hidden representation từ mô hình gốc:

h_t

EAGLE sử dụng một mô hình nhỏ:

Embedding
   ↓
AR Decoder
   ↓
LM Head

để sinh token theo cách autoregressive:

x_{t+1} \sim P(x|h_t)

x_{t+2} \sim P(x|h_t, x_{t+1})

x_{t+3} \sim P(x|h_t, x_{t+1}, x_{t+2})

⸻

13.2 Ưu điểm

Nhờ modeling dependency giữa token:

P(x_{t+i}|x_{t+1:t+i-1})

EAGLE đạt speculation accuracy cao hơn Medusa.

⸻

14. So sánh Medusa và EAGLE

Method	Draft Type	Token Dependency	Latency
Medusa	Non-AR	Không	Thấp
EAGLE	AR	Có	Trung bình

EAGLE thường đạt:

1.5× – 2× speculation accuracy improvement

so với Medusa.

⸻

15. Context-based Drafting

Trong một số tác vụ, đầu vào và đầu ra có độ tương đồng cao.

Ví dụ:
	•	summarization
	•	question answering
	•	document editing.

Trong trường hợp này:

Output \approx Input

Do đó ta có thể copy trực tiếp từ input.

⸻

15.1 Copy Mechanism

Giả sử:

Input:

The pancreas of pigs produces insulin

Prefix:

The pancreas of

Token tiếp theo có thể được copy:

pigs produces insulin

Điều này giúp:
	•	không cần draft model
	•	không tăng latency

⸻

16. Phân tích Benchmark

Một benchmark phổ biến là SpecBench.

Kết quả thực nghiệm cho thấy:

Task	Best Method
Chat	EAGLE
Coding	EAGLE
QA	EAGLE
Summarization	Copy-based

Lý do:

Trong summarization, input và output có độ tương đồng cao:

Sim(Input, Output) > 0.6

Do đó phương pháp copy đạt hiệu quả cao.

⸻

17. Phân tích hiệu quả

Giả sử:
	•	k token được draft
	•	p là tỉ lệ chấp nhận.

Số token trung bình mỗi bước:

E[tokens] = 1 + p(k-1)

Tốc độ suy luận:

Speedup = \frac{E[tokens]}{1 + Latency_{draft}}

Điều này cho thấy:
	•	tăng p là yếu tố quan trọng nhất.

⸻

18. Hướng nghiên cứu tương lai

Các hướng phát triển tiềm năng gồm:

Adaptive Drafting

điều chỉnh số token draft động theo context.

Hardware-aware Speculation

tối ưu speculative decoding cho GPU.

Multimodal Speculative Decoding

áp dụng cho mô hình:
	•	vision-language
	•	speech-language.

⸻

Tài liệu tham khảo
	1.	Leviathan et al., Fast Inference from Transformers via Speculative Decoding, ICML 2023.
	2.	Chen et al., Accelerating Large Language Model Decoding with Speculative Sampling, 2023.
	3.	Stern et al., Blockwise Parallel Decoding for Deep Autoregressive Models, NeurIPS 2018.
	4.	Cai et al., Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads, 2023.
	5.	Li et al., EAGLE: Efficient Autoregressive Generation via Layered Execution, 2024.
	6.	Xia et al., Draft & Verify: Lossless Acceleration of LLMs, 2023.

	1.	Chen et al., Accelerating Large Language Model Decoding with Speculative Sampling, 2023.
	2.	Stern et al., Blockwise Parallel Decoding for Deep Autoregressive Models, NeurIPS 2018.
	3.	Cai et al., Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads, 2023.
	4.	Leviathan et al., Fast Inference from Transformers via Speculative Decoding, ICML 2023.
	5.	Gu et al., Non-Autoregressive Neural Machine Translation, ICLR 2018.
	6.	Xia et al., Draft & Verify: Lossless Acceleration of LLMs, 2023.


© 2026 Pixiboss. Mọi quyền được bảo lưu.
Liên hệ: hello@pixibox.ai

