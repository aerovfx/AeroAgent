# 05 - Triển khai LoRA trong LLM

---

- [Người hướng dẫn] Bây giờ chúng ta cùng tìm hiểu nhé

cách triển khai bộ điều hợp LoRA trong LLM bằng Python,

TensorFlow và Keras.

Chúng ta sẽ bắt đầu với đoạn trích cho từng phần

và sau đó kết hợp tất cả chúng thành một giải pháp hoạt động đầy đủ.

Tuy nhiên, đừng lo lắng,

chúng tôi sẽ thực hiện điều này trong bản demo sau đó.

Trước khi bắt đầu, chúng ta cần đảm bảo

các thư viện cần thiết đã được cài đặt.

Để làm được điều đó, chúng ta sẽ cài đặt các thư viện

Máy biến áp, TensorFlow và Keras.

Với tất cả những điều đó đã sẵn sàng, hãy bắt đầu.

Điều đầu tiên chúng ta cần làm là tải mô hình

và mã thông báo.

Vì vậy, hãy nhớ rằng chúng tôi sử dụng AutoTokenizer,

from_pretrain trên mô hình đó,

và TFAutoModelForSeq2SeqLM.from_pretraining

trên mô hình đó.

Tất nhiên, nếu bạn muốn sử dụng BERT làm ví dụ,

bạn sẽ sử dụng TFAutoModel để tạo ngôn ngữ ẩn

chứ không phải Seq2Seq,

Seq2Seq là bộ mã hóa, bộ giải mã,

đó là mô hình T5 để đề phòng.

Tiếp theo, chúng ta cần tạo bộ chuyển đổi LoRA.

Điều đó có nghĩa là chúng ta sẽ xác định các ma trận xếp hạng thấp

và tích hợp chúng vào các lớp mô hình.

Vì vậy, trước tiên chúng ta tạo một lớp Keras tùy chỉnh

cho bộ chuyển đổi LoRA.

Và ở đây chẳng hạn,

chúng ta đang tạo ma trận A và B với thứ hạng cho trước

và đặt chúng ở mức có thể huấn luyện được.

Về phương thức gọi, hãy lưu ý rằng những gì chúng ta sẽ làm

đang thực hiện phép nhân ma trận của các đầu vào

với A rồi với B.

Về cơ bản đó sẽ là phép nhân của A và B

mà tôi đã kể cho bạn nghe.

Bây giờ chúng ta có lớp của mình,

chúng tôi sẽ tích hợp bộ chuyển đổi LoRA này

vào lớp hiện có của mô hình.

Được rồi?

Để đơn giản, chúng tôi sẽ thêm LoRA vào lớp dày đặc.

Chỉ để làm cho nó rất đơn giản.

Để làm điều đó, chúng ta cần tạo một lớp lớp mới,

Lớp LoRA dày đặc, sẽ có bộ chuyển đổi, bộ chuyển đổi LoRA.

Và trong phương thức gọi,

và đây là điều quan trọng,

chúng tôi sẽ lấy đầu ra ban đầu,

chúng ta sẽ lấy đầu ra LoRA,

và sau đó chúng ta sẽ cộng chúng lại.

Đây chính xác là một phần LoRA.

Hoạt động đó, đầu ra ban đầu cộng với đầu ra LoRA,

là W + AB mà tôi đã kể với bạn.

Sau khi làm xong việc chúng ta cần làm

là chúng ta cần thay thế các lớp dày đặc của mô hình

với những lớp dày đặc LoRA mới này biết cách thực hiện LoRA.

Và đó là những gì chúng tôi làm ở nơi này.

Trong ví dụ này, chúng tôi thay thế các lớp dày đặc hiện có

với lớp dày đặc LoRA mới của chúng tôi,

do đó tích hợp các bộ điều hợp LoRA.

Điều này cho phép chúng tôi chỉ tinh chỉnh một tập hợp con các tham số.

Cuối cùng, chúng tôi biên dịch và huấn luyện mô hình.

Chúng tôi sẽ sử dụng tập dữ liệu mẫu cho mục đích trình diễn.

Ở đây chúng tôi sẽ tải và xử lý WMT16

Bộ dữ liệu tiếng Anh tiếng Đức.

Chúng tôi sẽ biên dịch mô hình bằng Trình tối ưu hóa Adam

và bắt đầu quá trình đào tạo.

Vì vậy, chúng tôi sẽ tải tập dữ liệu đó từ tiếng Đức sang tiếng Anh.

Chúng tôi sẽ sử dụng công cụ đối chiếu dữ liệu chỉ để đảm bảo

rằng tất cả các phần còn lại của lô

có kích thước đúng.

Và bây giờ chúng ta cần tạo tập dữ liệu của mình.

Để tạo một tập dữ liệu, những gì chúng ta cần làm, như mọi khi,

là để mã hóa dữ liệu.

Vì vậy, chúng ta sẽ ánh xạ tập dữ liệu,

cả tập huấn luyện và tập kiểm tra,

với Lambda sẽ áp dụng mã thông báo

sang bản dịch chính xác để tạo nhãn.

Sau khi chúng tôi thực hiện tất cả những điều đó và có sẵn dữ liệu,

những gì chúng ta phải làm chỉ là biên dịch mô hình

với Adam Optimizer như chúng tôi thường làm,

và chúng tôi phù hợp với mô hình.

Và điều đó sẽ chỉ hoạt động.

Bằng cách này, chúng tôi đã triển khai LoRA một cách hiệu quả

bằng cách thay thế từng lớp dày đặc

của mô hình Flan T5 Large thành các lớp LoRA.