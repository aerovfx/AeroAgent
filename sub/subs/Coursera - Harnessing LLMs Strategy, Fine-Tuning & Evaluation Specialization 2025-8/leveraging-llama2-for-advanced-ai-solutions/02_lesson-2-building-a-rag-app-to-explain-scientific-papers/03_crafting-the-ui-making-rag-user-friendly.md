# 03 craft-the-ui-làm-giẻ-thân thiện với người dùng

---

Bạn đã cảm thấy chưa

sự cần thiết phải làm

ứng dụng chuyên gia AI cá nhân của bạn

dễ tiếp cận hơn hoặc tương tác hơn?

Vâng, trong video này,

bạn sẽ học nhanh

và cách đơn giản để

thêm giao diện người dùng vào giải pháp RAG của bạn

để người dùng có thể nhiều hơn

dễ dàng tương tác với

chuyên gia AI cá nhân của bạn.

Đến cuối video,

bạn sẽ có thể tương tác

với cái lớn

mô hình ngôn ngữ hơn

giao diện thuận tiện

và bạn sẽ biết cách

xây dựng giao diện người dùng như vậy

sử dụng thư viện Streamlit.

Bây giờ, hãy đi sâu vào cách chúng ta có thể

nâng cao mô hình AI của chúng tôi với

giao diện thân thiện với người dùng.

Ngành kiến ​​​​trúc. Kiến trúc này

của hệ thống hỏi đáp của chúng tôi là

được thiết kế để tích hợp liền mạch

một mô hình Llama 2 được điều chỉnh với

một giao diện thân thiện với người dùng.

Phần back-end bao gồm

mô hình ngôn ngữ lớn

khung LangChain,

xử lý đầu vào

và dữ liệu đầu ra,

điều chỉnh từ Llama 2.

Tay cầm mô hình

nhiệm vụ phức tạp của

tạo ra phản hồi

dựa trên truy vấn của người dùng.

Giao diện người dùng được xây dựng bằng cách sử dụng

khung web Streamlit,

cung cấp giao diện người dùng hệ thống Hỏi đáp,

nơi người dùng có thể

nhập truy vấn của họ.

Đầu vào từ UI là

sau đó gửi đến LangChain,

xử lý nó và

trả về phản hồi

được tạo ra bởi Llama đã điều chỉnh

2 trở lại giao diện người dùng.

Vòng lặp tương tác này

đảm bảo rằng người dùng nhận được

mạch lạc và phù hợp

câu trả lời trong thời gian thực,

làm cho cả hệ thống

mạnh mẽ và dễ tiếp cận.

Bây giờ chúng ta đã hiểu

kiến trúc

của hệ thống hỏi đáp của chúng tôi,

đã đến lúc phải tiếp tục

đến việc thực hiện.

Đầu tiên, tôi tạo một

tập tin Python mới.

Tôi gọi RAG_withUI của tôi là,

và đây là nơi chúng ta sẽ

triển khai logic và giao diện người dùng của chúng tôi.

Tiếp theo, sao chép các phần phụ thuộc

chúng tôi đã sử dụng trong

video trước đó.

Những điều này sẽ cho phép chúng ta

xử lý việc vẫn nuốt phải,

tách, nhúng và

truy xuất logic bằng LangChain.

Tiếp theo, chúng tôi đã

đã cài đặt Streamlit

và đây là lý do tại sao chúng ta có thể

nhập khẩu nó ngay lập tức.

Bây giờ hãy xác định tiêu đề

và dòng tiêu đề phụ cho giao diện người dùng của chúng tôi.

Điều này cực kỳ đơn giản và có thể

thực hiện chỉ với hai

dòng mã.

Điều này sẽ cung cấp cho ứng dụng của chúng tôi

một cái nhìn chuyên nghiệp

với một tiêu đề và

một lời giải thích cho cái gì

ứng dụng này sẽ được sử dụng cho.

Tiếp theo, chúng tôi lưu trữ dữ liệu

logic nhập vào giống nhau,

nhưng bao bọc phần còn lại của logic của chúng tôi

thành hàm phản hồi.

Chức năng này sẽ

được gọi một lần

người dùng gửi một

câu hỏi thông qua giao diện người dùng.

generate_response

tay cầm chức năng

việc truy xuất mô hình

logic và kéo

câu trả lời có liên quan từ

tài liệu sử dụng

ngôn ngữ La Mã

mô hình và LangChain.

Đầu vào của người dùng được phân tích cú pháp dưới dạng

một tham số và mô hình sử dụng

chúng đến kho tài liệu để

tìm thấy nhiều nhất

thông tin liên quan.

Cuối cùng, chúng tôi hiển thị

câu trả lời bằng cách sử dụng

st.info trong ứng dụng Streamlit.

Bây giờ chúng ta sẽ thiết lập

một hình thức cho phép

người dùng gõ vào

hỏi và nộp nó.

Đây là cách chúng ta có thể định nghĩa điều đó.

Chúng tôi xác định biểu mẫu bằng cách sử dụng st.form,

chứa vùng văn bản cho

đầu vào của người dùng và

một nút gửi.

Văn bản giữ chỗ

đưa ra gợi ý cho

người dùng về cái gì

những câu hỏi họ có thể hỏi.

Sau khi người dùng gửi

câu hỏi của họ,

tạo ra

chức năng phản ứng là

được kêu gọi để cung cấp một

câu trả lời dựa trên đầu vào.

Cuối cùng nhưng không kém phần quan trọng,

chúng ta cần phải lấy

tham số đầu vào, văn bản đầu vào của chúng tôi,

mà chúng tôi phân tích cú pháp

hàm tạo_response

và sử dụng nó để thay thế

đầu vào được mã hóa cứng mà chúng tôi phân tích

chức năng gọi chuỗi RAG.

Vâng, đó là nó bây giờ.

Một khi chúng tôi đã viết

logic và thiết lập giao diện người dùng,

ứng dụng của chúng tôi đã sẵn sàng để chạy.

Khi bạn kiểm tra nó,

ứng dụng sẽ cho phép bạn

đặt câu hỏi về

Llama 2 và người mẫu

sẽ lấy và hiển thị

câu trả lời có liên quan dựa trên

tài liệu chúng tôi đã nhập.

Để xem việc triển khai hoàn chỉnh

hoặc nếu bạn gặp phải bất kỳ vấn đề nào,

vui lòng kiểm tra

Giao diện người dùng chi nhánh 04 đã hoàn tất.

Với thiết lập này, bạn đã xây dựng

đầy đủ chức năng

Hệ thống hỏi đáp với

giao diện thân thiện với người dùng

sử dụng Streamlit và LangChain.

Tóm lại, tạo

giao diện thân thiện với người dùng cho

mô hình ngôn ngữ lớn là

cần thiết để thực hiện những điều này

các công cụ mạnh mẽ có thể truy cập được.

Đến cuối khóa học này,

bạn sẽ có thể

hiểu những điều cơ bản của

xây dựng tương tác

giao diện với

Streamlit và bạn

sẽ sẵn sàng

thực hiện chúng trong

dự án AI của bạn.

Từ việc thiết lập giao diện trò chuyện

để tinh chỉnh các phản hồi,

bạn sẽ có kỹ năng để

tạo ra các giải pháp AI có tác động mạnh mẽ.

Hãy thử hỏi các chuyên gia AI của bạn

các câu hỏi khác nhau và

suy ngẫm về cách giao diện này

nâng cao khả năng sử dụng.

Ngoài ra, hãy xem xét cách tùy chỉnh

mô hình ngôn ngữ lớn

có thể biến đổi một sản phẩm hoặc

dịch vụ bạn sử dụng thường xuyên.

Sự phản ánh này sẽ chuẩn bị

bạn cho những bài học sắp tới.

Hãy luôn tò mò và

tiếp tục thử nghiệm.

Bây giờ tôi còn một cái nữa

câu hỏi dành cho bạn.