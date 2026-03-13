Dưới đây là phần tiếp theo của bài viết khoa học, được biên soạn lại từ nội dung bạn cung cấp, bổ sung mô hình toán học, phân tích thuật toán và hệ thống phân loại (taxonomy). Nội dung được viết theo chuẩn học thuật Markdown để nối tiếp các phần trước.

⸻

22. Nguồn gốc của thuật ngữ Speculative Decoding

Tên gọi Speculative Decoding xuất phát từ khái niệm Speculative Execution trong khoa học máy tính.

Speculative Execution là một kỹ thuật tối ưu hóa trong kiến trúc CPU, trong đó hệ thống thực hiện trước một số tác vụ dự đoán trước khi biết chắc rằng chúng có cần thiết hay không.

Ý tưởng chính:

\text{Execute Early} \rightarrow \text{Avoid Future Latency}

Ví dụ trong CPU pipeline:

Predict branch → execute instruction → verify branch

Nếu dự đoán đúng:
	•	tiết kiệm thời gian chờ

Nếu sai:
	•	rollback kết quả

Speculative decoding áp dụng cùng nguyên lý cho sinh văn bản của mô hình ngôn ngữ:

Draft tokens → Verify tokens → Accept or reject

Do đó tên gọi speculative decoding đã được cộng đồng nghiên cứu chấp nhận rộng rãi.

⸻

23. Greedy Decoding và Sampling

Trong suy luận LLM, hai phương pháp giải mã phổ biến là:

Phương pháp	Đặc điểm
Greedy decoding	luôn chọn token có xác suất cao nhất
Sampling	chọn token ngẫu nhiên theo phân bố xác suất


⸻

23.1 Greedy Decoding

Greedy decoding chọn:

y_t = \arg\max_{y} P(y|y_{<t},x)

Ưu điểm:
	•	ổn định
	•	kết quả xác định

Nhược điểm:
	•	thiếu đa dạng
	•	dễ lặp nội dung

Ví dụ:

Input: Hello
Output: Hello, how are you today?

Mỗi lần chạy sẽ cho kết quả giống nhau.

⸻

23.2 Sampling

Sampling lấy mẫu từ phân bố xác suất:

y_t \sim P(y|y_{<t},x)

Ưu điểm:
	•	đa dạng
	•	sáng tạo hơn

Do đó các hệ thống như:
	•	chatbot
	•	creative writing
	•	storytelling

thường sử dụng sampling.

⸻

23.3 Các kỹ thuật sampling phổ biến

Top-K Sampling

Chỉ chọn từ K token có xác suất cao nhất.

y_t \sim P(y | y \in TopK)

⸻

Top-P Sampling (Nucleus Sampling)

Chọn tập token sao cho:

\sum_{y \in S} P(y) \ge P

với P thường khoảng:

P = 0.9

⸻

Temperature

Điều chỉnh phân bố xác suất:

P_T(y) = \frac{P(y)^{1/T}}{\sum P(y)^{1/T}}

Temperature	Hiệu ứng
T < 1	ít đa dạng
T = 1	bình thường
T > 1	sáng tạo hơn


⸻

24. Speculative Sampling

Speculative decoding ban đầu được thiết kế cho greedy decoding.

Tuy nhiên trong thực tế, các hệ thống chatbot cần sampling.

Do đó các nhà nghiên cứu đề xuất Speculative Sampling.

Mục tiêu:

P_{speculative}(y) = P_{original}(y)

tức là giữ nguyên phân bố xác suất của mô hình gốc.

⸻

24.1 Quy trình Speculative Sampling

Giả sử:
	•	draft model: Q
	•	target model: P

Bước 1: draft model sinh token x

x \sim Q(x)

Bước 2: tính xác suất

q_x = Q(x)

p_x = P(x)

⸻

Trường hợp 1

Nếu:

p_x \ge q_x

Token được chấp nhận trực tiếp.

⸻

Trường hợp 2

Nếu:

p_x < q_x

Token được chấp nhận với xác suất:

\alpha = \frac{p_x}{q_x}

⸻

Nếu bị từ chối

Token mới được lấy mẫu từ phân bố điều chỉnh:

P'(y) = \frac{P(y) - Q(y)}{1 - \sum_{z} Q(z)}

Kỹ thuật này đảm bảo:

Distribution_{speculative} = Distribution_{target}

⸻

25. Benchmark Speculative Decoding

Hiện nay đã có nhiều benchmark đánh giá các phương pháp speculative decoding.

Một benchmark phổ biến là SpecBench.

Kết quả cho thấy:

Method	Speedup
EAGLE / ECO	1.8x – 2.4x
Medusa	~2x
SpecInfer	~2x

Tuy nhiên:
	•	mỗi phương pháp tối ưu cho task khác nhau

Ví dụ:

Task	Best Method
Summarization	specialized methods
Chat	Medusa
Reasoning	ECO


⸻

26. Taxonomy của Speculative Decoding

Speculative decoding có thể chia thành hai thành phần chính:

Speculative Decoding
       │
 ┌─────┴─────┐
 Drafting   Verification


⸻

26.1 Drafting

Drafting tạo các token dự đoán.

Hai yếu tố quan trọng:

1. Speculation Accuracy

Số token được chấp nhận:

Accuracy = \frac{\text{Accepted Tokens}}{\text{Draft Tokens}}

⸻

2. Draft Latency

Thời gian tạo draft:

T_{draft}

Mục tiêu tối ưu:

\text{Maximize Accuracy}

\text{Minimize Latency}

⸻

Trade-off

High accuracy
      ▲
      │
      │
      │
      └────────► Low latency

Phương pháp tốt nằm trong vùng tối ưu (green area).

⸻

27. Independent Drafting

Một phương pháp phổ biến là Independent Drafting.

Ý tưởng:

Sử dụng một mô hình khác làm draft model.

Draft Model → Draft tokens
Target Model → Verification

Hai câu hỏi quan trọng:

1️⃣ Chọn draft model nào?
2️⃣ Có nên fine-tune draft model?

⸻

28. Non-Autoregressive Drafting

Một hướng nghiên cứu là dùng Non-Autoregressive Models (NAR).

⸻

28.1 Auto-Regressive Model

Sinh token từng bước:

Build → a → large → language → model

Thời gian:

T \propto n

⸻

28.2 Non-Autoregressive Model

Sinh toàn bộ chuỗi song song.

Ví dụ:

Input:

Build [MASK] [MASK] [MASK] [MASK]

Output:

Build a large language model

Một bước duy nhất:

T \approx constant

⸻

28.3 Ưu điểm
	•	rất nhanh
	•	sinh nhiều token cùng lúc

⸻

28.4 Nhược điểm

Chất lượng thấp hơn:

Quality_{NAR} < Quality_{AR}

Tuy nhiên trong speculative decoding:

Low quality draft → Verified by large model

Do đó NAR vẫn phù hợp làm draft model.

⸻

29. Small Language Models làm Draft Model

Một giải pháp thực tế hơn là sử dụng mô hình nhỏ hơn.

Ví dụ:

Target Model	Draft Model
LLaMA-70B	LLaMA-7B
T5-XXL	T5-Small

Do:

Latency_{small} << Latency_{large}

⸻

30. Trade-off giữa kích thước draft model và tốc độ

Nếu draft model quá nhỏ:

Accuracy \downarrow

Nếu quá lớn:

Latency \uparrow

Do đó tồn tại điểm tối ưu.

Ví dụ thực nghiệm:

Draft Model	Acceptance	Speedup
T5-Small	thấp	cao
T5-Base	trung bình	trung bình
T5-Large	cao	thấp

Thường:

draft model nhỏ nhất cho tốc độ tốt nhất.

⸻

31. Knowledge Distillation cho Draft Model

Để tăng chất lượng draft, ta có thể huấn luyện draft model bắt chước target model.

Kỹ thuật này gọi là:

\text{Knowledge Distillation}

⸻

31.1 Quy trình

1️⃣ Target model sinh dữ liệu:

Prompt → Response

2️⃣ Dùng dữ liệu này huấn luyện draft model.

Loss function:

L = KL(P_{target} || P_{draft})

⸻

31.2 Lợi ích
	•	tăng acceptance rate
	•	cải thiện tốc độ speculative decoding

⸻

32. Kết luận phần Taxonomy

Hiệu quả của speculative decoding phụ thuộc vào:

Speedup = f(Accuracy, Latency)

Trong đó:
	•	accuracy → nhiều token được chấp nhận
	•	latency → draft model đủ nhanh

Do đó thiết kế draft model là bài toán quan trọng nhất trong speculative decoding.

Dưới đây là phần tiếp theo của bài viết khoa học, được biên soạn lại từ nội dung bạn cung cấp, bổ sung mô hình toán học, giải thích thuật toán và cấu trúc hệ thống, tiếp nối logic các phần trước.

⸻

33. Hạn chế của các phương pháp Draft Model độc lập

Các phương pháp Independent Drafting dựa trên mô hình (model-based drafting) thường gặp một số hạn chế quan trọng.

Một trong những hạn chế lớn nhất là yêu cầu tokenizer phải giống nhau giữa draft model và target model.

Giả sử:
	•	Target model: M_T
	•	Draft model: M_D

Hai mô hình cần sử dụng cùng tokenizer:

Tokenizer(M_T) = Tokenizer(M_D)

Nếu không:

Tokens(M_D) \neq Tokens(M_T)

Điều này làm cho việc xác minh token trở nên không khả thi.

⸻

Ví dụ thực tế

Một số hệ sinh thái mô hình phổ biến:

Model	Tokenizer
LLaMA	SentencePiece
Qwen	BPE tùy chỉnh
GPT	Byte Pair Encoding

Do đó:
	•	Qwen nhỏ có thể làm draft cho Qwen lớn
	•	nhưng không thể làm draft cho LLaMA

Điều này tạo ra rào cản khi triển khai speculative decoding.

⸻

Chi phí huấn luyện

Một hạn chế khác:

Nếu muốn sử dụng draft model hiệu quả, ta cần huấn luyện:
	•	một mô hình lớn
	•	một mô hình nhỏ tương thích

Chi phí:

Cost_{total} = Cost_{target} + Cost_{draft}

Trong nhiều trường hợp:

Cost_{draft} \approx O(10^{23}) \text{ FLOPs}

Điều này không khả thi với nhiều tổ chức.

⸻

34. Independent Drafting không dựa trên mô hình

Để giải quyết vấn đề trên, các nhà nghiên cứu đề xuất các phương pháp drafting không cần mô hình.

Các phương pháp này sử dụng:
	•	corpus
	•	input context
	•	heuristic

⸻

35. Context Retrieval Drafting

Một phương pháp đơn giản là Context Retrieval.

Ý tưởng:

Sử dụng prefix hiện tại để tìm các chuỗi tương tự trong corpus.

⸻

35.1 Quy trình

Giả sử prefix:

for (int i = 0;

Ta tìm trong corpus các đoạn tiếp theo:

for (int i = 0; i < n; i++)
for (int i = 0; i < size; i++)
for (int i = 0; i < len; i++)

Sau đó xây dựng một cây trie.

⸻

35.2 Xây dựng Trie Tree

Giả sử có các continuation:

in range(
in range(len(
in range(n)

Ta xây dựng cấu trúc:

root
 └── in
      └── range
            ├── (
            │    └── len
            └── (
                 └── n

Tần suất mỗi node được thống kê:

freq(token_i)

Chỉ giữ các nhánh phổ biến.

⸻

35.3 Chọn Draft Chain

Từ cây trie, ta chọn chuỗi có xác suất cao nhất:

Draft = \arg\max_{path} \prod freq(token_i)

Ví dụ:

in range(

Chuỗi này được dùng làm draft tokens.

⸻

35.4 Ưu điểm
	•	không cần mô hình
	•	chi phí thấp
	•	dễ triển khai

⸻

35.5 Nhược điểm

Phụ thuộc mạnh vào corpus:

Performance \propto Corpus\ Coverage

⸻

36. Copy Mechanism Drafting

Một phương pháp khác là Copy-based Drafting.

Ý tưởng:

Trong nhiều nhiệm vụ NLP, output có sự trùng lặp lớn với input.

⸻

Ví dụ

Task: Question Answering

Input:

Document:
Pancreas is an organ in pigs...

Question:

Where does insulin come from?

Output:

Insulin comes from the pancreas of pigs.

Nhiều token được copy từ document.

⸻

36.1 Quy trình

Giả sử mô hình đã sinh:

comes from

Nếu chuỗi này xuất hiện trong input:

comes from the pancreas of pigs

Ta có thể copy phần còn lại:

the pancreas of pigs

Chuỗi này trở thành draft tokens.

⸻

36.2 Xác minh

Target model xác minh:

Prefix + Draft

Nếu đúng → chấp nhận.

Như vậy có thể sinh nhiều token trong một bước.

⸻

36.3 Ưu điểm

Đặc biệt hiệu quả trong các task:

Task	Hiệu quả
Text editing	cao
Grammar correction	cao
Document QA	cao


⸻

37. Self-Drafting

Một hướng tiếp cận khác là Self-Drafting.

Thay vì sử dụng mô hình khác, ta dùng chính mô hình target làm draft model.

Target Model
      │
 ┌────┴────┐
Drafting  Verification


⸻

Ưu điểm
	•	không cần mô hình thứ hai
	•	không cần tokenizer giống nhau

⸻

38. Các phương pháp Self-Drafting

Ba kỹ thuật phổ biến:

1️⃣ Extra Heads
2️⃣ Layer Skipping
3️⃣ Mask Predict

⸻

39. Extra Heads

Phương pháp này được đề xuất trong Blockwise Decoding (2018).

Ý tưởng:

Thêm nhiều prediction heads trên transformer.

⸻

Cấu trúc

Transformer decoder output:

Hidden State
      │
 ┌────┼─────┐
Head1 Head2 Head3

Mỗi head dự đoán:

Head	Token
Head1	t+1
Head2	t+2
Head3	t+3


⸻

Ví dụ

Input:
Build a

Output heads:
Head1 → large
Head2 → language
Head3 → model


⸻

40. Medusa Architecture

Một hệ thống hiện đại sử dụng extra heads là Medusa.

Medusa thêm nhiều head vào transformer:

Transformer Layer
        │
   Medusa Heads
   ├── head_1
   ├── head_2
   ├── head_3

Các head này sinh token song song.

⸻

Tốc độ

Medusa đạt:

Speedup \approx 2\times

trong nhiều benchmark.

⸻

41. Layer Skipping

Một phương pháp self-drafting khác là Layer Skipping.

⸻

Ý tưởng

Trong quá trình drafting, ta bỏ qua một số layer của transformer.

Giả sử transformer có L layer:

L = 32

Trong drafting:

Layers_{draft} = \{1,3,5,7,...\}

⸻

Thời gian suy luận

Thời gian giảm:

T_{draft} \propto |Layers_{draft}|

⸻

42. Lựa chọn layer tối ưu

Chọn layer nào để skip là bài toán khó.

Các tác giả đề xuất:
	•	sử dụng black-box evaluation
	•	tối ưu bằng Bayesian Optimization

⸻

Biểu diễn vector

Layer selection được biểu diễn:

v = (v_1, v_2, ..., v_L)

với:

v_i =
\begin{cases}
1 & \text{use layer} \\
0 & \text{skip layer}
\end{cases}

⸻

Hàm mục tiêu

Tối ưu:

\max f(v)

với:

f(v) = \alpha \cdot AcceptanceRate - \beta \cdot Latency

⸻

43. Kết quả

Layer skipping cho phép:
	•	giảm chi phí tính toán
	•	vẫn giữ tỉ lệ acceptance cao

⸻

44. Tổng kết phần Drafting

Các phương pháp drafting hiện nay có thể phân loại như sau:

Drafting Methods
       │
 ┌─────┴─────────┐
Independent   Self-Drafting
       │
 ┌─────┼─────┐
Model  Retrieval Copy


⸻

45. Hướng nghiên cứu tiếp theo

Các nghiên cứu mới tập trung vào:
	•	tree-based verification
	•	multi-branch drafting
	•	dynamic speculation

Những phương pháp này sẽ được trình bày trong các phần tiếp theo.

⸻

Tài liệu tham khảo
	1.	Leviathan, Y. et al. (2023)
Fast Inference from Transformers via Speculative Decoding
	2.	Stern, M. et al. (2018)
Blockwise Parallel Decoding
	3.	Cai, T. et al. (2024)
Medusa: Accelerating LLM Generation
	4.	Kim, Y., Rush, A. (2016)
Sequence-Level Knowledge Distillation
	5.	Chen, L. et al. (2024)
A Survey on Speculative Decoding

	1.	Leviathan, Y. et al. (2023)
Fast Inference from Transformers via Speculative Decoding
	2.	Stern, M. et al. (2018)
Blockwise Parallel Decoding
	3.	Cai, T. et al. (2024)
Medusa: Accelerating LLM Generation
	4.	Kim, Y. & Rush, A. (2016)
Sequence-Level Knowledge Distillation
	5.	DeepSeek AI (2024)
DeepSeek-V3 Technical Report

⸻

© 2026 Pixiboss. Mọi quyền được bảo lưu.
Liên hệ: hello@pixibox.ai

