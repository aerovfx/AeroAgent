# 04 mô hình chia tỷ lệ luật và tính toán tối ưu

---

Trong video cuối cùng,

bạn đã khám phá một số

những thách thức tính toán của

đào tạo các mô hình ngôn ngữ lớn.

Ở đây bạn sẽ tìm hiểu về

nghiên cứu có

đã tìm hiểu mối quan hệ

giữa kích thước mô hình, đào tạo,

cấu hình và hiệu suất trong

một nỗ lực để xác định chỉ

mô hình cần phải lớn đến mức nào.

Hãy nhớ rằng, mục tiêu trong

đào tạo trước là để

tối đa hóa hiệu suất của mô hình

về mục tiêu học tập của nó,

đó là giảm thiểu tổn thất

khi dự đoán mã thông báo.

Hai lựa chọn bạn phải đạt được

hiệu suất tốt hơn là

tăng kích thước của

tập dữ liệu bạn

đào tạo mô hình của bạn trên

và tăng số lượng

các tham số trong mô hình của bạn.

Về lý thuyết, bạn có thể

quy mô một trong hai

cả hai đại lượng này

để cải thiện hiệu suất.

Tuy nhiên, một cái khác

vấn đề cần quan tâm

sự cân nhắc là của bạn

tính toán ngân sách mà

bao gồm các yếu tố như

số lượng GPU bạn có

truy cập vào và

thời gian bạn có sẵn

cho các mô hình đào tạo.

Để giúp bạn hiểu một số

của cuộc thảo luận phía trước,

trước tiên hãy xác định một đơn vị của

tính toán định lượng

các nguồn lực cần thiết.

Một petaFLOP mỗi ngày thứ hai

là một phép đo

về số lượng

dấu phẩy động

các thao tác thực hiện tại

tỷ lệ một

petaFLOP mỗi giây,

chạy suốt cả ngày.

Lưu ý, một petaFLOP

tương ứng với

một triệu triệu trôi nổi

hoạt động điểm mỗi giây.

Khi suy nghĩ cụ thể

về đào tạo máy biến áp,

một petaFLOP mỗi giây

ngày là khoảng

tương đương với tám

GPU NVIDIA V100,

hoạt động hết công suất

trong một ngày trọn vẹn.

Nếu bạn có thêm

bộ vi xử lý mạnh mẽ mà

có thể thực hiện nhiều hơn

hoạt động cùng một lúc,

sau đó là petaFLOP mỗi giây

ngày cần ít chip hơn.

Ví dụ, hai

GPU NVIDIA A100

đưa ra phép tính tương đương

đến tám chip V100.

Để cung cấp cho bạn một ý tưởng

quy mô của những điều này

tính toán ngân sách,

biểu đồ này cho thấy sự so sánh

giảm petaFLOP mỗi giây ngày

bắt buộc phải đào tạo trước

phương sai khác nhau

của Bert và Roberta,

cả hai đều là

mô hình chỉ có bộ mã hóa.

T5 và bộ mã hóa-giải mã

mô hình và GPT-3,

đó là mô hình chỉ có bộ giải mã.

Sự khác biệt

giữa các mô hình trong

mỗi gia đình là một con số

của các thông số đã được huấn luyện,

dao động từ vài trăm

triệu cho căn cứ Bert để

175 tỷ đồng cho

biến thể GPT-3 lớn nhất.

Lưu ý rằng trục y

là logarit.

Mỗi lần tăng theo chiều dọc

là lũy thừa của 10.

Ở đây chúng ta thấy T5 XL với

ba tỷ

thông số cần thiết

gần 100 petaFLOP

mỗi giây ngày.

Trong khi GPT-3 175 lớn hơn

mô hình tham số tỷ

cần khoảng 3.700

petaFLOP mỗi giây ngày.

Biểu đồ này làm cho nó rõ ràng

rằng một lượng lớn

máy tính cần thiết để

đào tạo các mô hình lớn nhất.

Bạn có thể thấy những mô hình lớn hơn

tốn nhiều tài nguyên máy tính hơn để

đào tạo và nói chung cũng yêu cầu

nhiều dữ liệu hơn để đạt được

hiệu suất tốt.

Hoá ra là họ

thực sự được xác định rõ

mối quan hệ giữa

ba lựa chọn mở rộng quy mô này.

Các nhà nghiên cứu có

khám phá sự đánh đổi

giữa kích thước tập dữ liệu huấn luyện,

kích thước mô hình và ngân sách tính toán.

Đây là một con số từ một bài báo của

các nhà nghiên cứu tại OpenAI rằng

khám phá tác động của tính toán

ngân sách về hiệu suất của mô hình.

Trục y là tổn thất kiểm tra,

mà bạn có thể xem xét

như một người đại diện cho

hiệu suất mô hình ở đâu

giá trị nhỏ hơn là tốt hơn.

Trục x là ngân sách tính toán

tính bằng đơn vị petaFLOP

mỗi giây ngày.

Như bạn vừa thấy, số lớn hơn

có thể đạt được bằng một trong hai

sử dụng nhiều sức mạnh tính toán hơn hoặc

đào tạo lâu hơn hoặc cả hai.

Mỗi đường màu xanh mỏng ở đây thể hiện

sự mất mát mô hình trong một

đợt tập luyện duy nhất.

Nhìn vào đâu

sự mất mát bắt đầu

giảm chậm hơn

cho mỗi lần chạy,

tiết lộ rõ ràng

mối quan hệ giữa

ngân sách tính toán và

hiệu suất của mô hình.

Điều này có thể được xấp xỉ bởi

một mối quan hệ luật lũy thừa,

được thể hiện bằng đường màu hồng này.

Định luật lũy thừa là một

mối quan hệ toán học

giữa hai biến,

trong đó một tỷ lệ thuận với

người khác được nâng lên một quyền lực nào đó.

Khi vẽ trên đồ thị ở đó

cả hai trục đều là logarit,

mối quan hệ luật lũy thừa

hiện dưới dạng đường thẳng.

Mối quan hệ ở đây được giữ

miễn là kích thước mô hình và

kích thước tập dữ liệu đào tạo không

cản trở quá trình đào tạo.

Tính theo mệnh giá,

điều này sẽ gợi ý rằng

bạn chỉ có thể tăng

ngân sách điện toán của bạn để đạt được

hiệu suất mô hình tốt hơn.

Tuy nhiên trong thực tế,

tài nguyên máy tính mà bạn

có sẵn để đào tạo sẽ

nói chung là khó khăn

ràng buộc được thiết lập bởi

Các yếu tố như phần cứng

bạn có quyền truy cập vào,

thời gian có sẵn để đào tạo

và tài chính

ngân sách của dự án.

Nếu bạn giữ

tính toán ngân sách cố định,

hai đòn bẩy bạn phải

cải thiện mô hình của bạn

hiệu suất là

kích thước của tập dữ liệu huấn luyện

và số lượng

các tham số trong mô hình của bạn.

Các nhà nghiên cứu OpenAI đã tìm thấy

rằng hai người này

số lượng cũng hiển thị

mối quan hệ lũy thừa với

mất kiểm tra trong trường hợp

hai biến còn lại

được giữ cố định.

Đây là một hình khác

từ bài báo khám phá

tác động của tập dữ liệu huấn luyện

kích thước trên hiệu suất mô hình.

Ở đây, ngân sách tính toán

và kích thước mô hình được giữ

cố định và kích thước của

tập dữ liệu huấn luyện là khác nhau.

Biểu đồ cho thấy rằng như

khối lượng đào tạo

dữ liệu tăng lên,

hiệu suất của

mô hình tiếp tục được cải thiện.

Trong biểu đồ thứ hai,

ngân sách tính toán và

kích thước tập dữ liệu đào tạo

được giữ không đổi.

Mô hình số khác nhau

của các tham số được huấn luyện.

Khi mô hình tăng kích thước,

tổn thất kiểm tra giảm

cho thấy hiệu suất tốt hơn.

Tại thời điểm này bạn

có thể đang hỏi,

sự cân bằng lý tưởng là gì

giữa ba đại lượng này?

Chà, hóa ra là rất nhiều

mọi người quan tâm

trong câu hỏi này.

Cả việc nghiên cứu và

cộng đồng ngành

đã xuất bản rất nhiều

dữ liệu thực nghiệm cho đào tạo trước

tính toán mô hình tối ưu.

Trong một bài báo xuất bản năm 2022,

một nhóm các nhà nghiên cứu

được lãnh đạo bởi Jordan Hoffmann,

Sebastian Borgeaud

và Arthur Mensch

đã thực hiện một nghiên cứu chi tiết về

hiệu suất của

mô hình ngôn ngữ của

kích cỡ và số lượng khác nhau

của dữ liệu huấn luyện.

Mục đích là để tìm ra

số lượng tham số tối ưu

và khối lượng dữ liệu huấn luyện

cho một ngân sách tính toán nhất định.

Tên tác giả, kết quả

tính toán tối ưu

người mẫu, Chinchilla.

Bài viết này thường được nhắc đến

như tờ giấy Chinchilla.

Chúng ta hãy nhìn vào

một số phát hiện của họ

Bài báo Chinchilla gợi ý rằng

nhiều trong số 100 tỷ

mô hình ngôn ngữ lớn tham số

như GPT-3 thực sự có thể

được tham số hóa quá mức,

nghĩa là họ có

nhiều thông số hơn

họ cần đạt được một

hiểu biết tốt về

ngôn ngữ và được đào tạo

để họ được hưởng lợi từ

xem thêm dữ liệu đào tạo.

Các tác giả đưa ra giả thuyết rằng

mô hình nhỏ hơn có thể

có thể đạt được

hiệu suất tương tự

những cái lớn hơn nhiều

nếu họ được đào tạo

trên các tập dữ liệu lớn hơn.

Trong bảng này, bạn có thể thấy

một lựa chọn các mô hình cùng

với kích thước và thông tin của họ

về tập dữ liệu

họ đã được đào tạo.

Một bài học quan trọng từ

tờ báo Chinchilla là vậy

đào tạo tối ưu

kích thước tập dữ liệu

đối với một mô hình nhất định là về

lớn hơn 20 lần

số lượng tham số

trong mô hình.

Chinchilla đã xác định

để tính toán tối ưu.

Với giá 70 tỷ

mô hình tham số,

đào tạo lý tưởng

tập dữ liệu chứa 1,4

nghìn tỷ token hoặc 20 lần

số lượng tham số.

Ba mô hình cuối cùng trong

cái bàn đã được đào tạo về

tập dữ liệu nhỏ hơn

hơn Chinchilla

kích thước tối ưu.

Những mô hình này thực sự có thể

được đào tạo.

Ngược lại, LLaMA

đã được đào tạo về

kích thước tập dữ liệu của

1,4 nghìn tỷ token,

gần với

Số lượng khuyến nghị của Chinchilla.

Một kết quả quan trọng khác

từ tờ giấy là

tính toán Chinchilla tối ưu

mô hình vượt trội

không tính toán tối ưu

các mô hình như

GPT-3 trên phạm vi rộng lớn

nhiệm vụ đánh giá tiếp theo.

Với kết quả của

giấy Chinchilla

trong tay các đội có

gần đây đã bắt đầu phát triển

mô hình nhỏ hơn mà

đạt được tương tự,

nếu không kết quả tốt hơn

các mô hình lớn hơn đã được

được đào tạo một cách không tối ưu.

Tiến về phía trước, bạn có thể có thể

mong đợi để thấy một sự sai lệch

từ lớn hơn là

xu hướng luôn tốt hơn của

vài năm gần đây như

nhiều nhóm hoặc nhà phát triển hơn thích

bạn bắt đầu tối ưu hóa

thiết kế mô hình của họ.

Mẫu cuối cùng được hiển thị

trên slide này,

Bloomberg GPT, là một

mô hình thực sự thú vị.

Nó đã được đào tạo về tính toán

cách tối ưu sau

trận thua Chinchilla

và do đó đạt được

hiệu suất tốt với kích thước

của 50 tỷ thông số.

Đó cũng là một điều thú vị

ví dụ về một tình huống trong đó

đào tạo trước người mẫu

từ đầu là

cần thiết để đạt được

thực hiện nhiệm vụ tốt.

Hãy chuyển sang

video cuối cùng của

tuần này để thảo luận lý do tại sao.