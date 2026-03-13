# 05 đào tạo trước khi thích ứng với tên miền

---

Cho đến nay, tôi đã nhấn mạnh rằng bạn sẽ

thường làm việc với LLM hiện có khi bạn

phát triển ứng dụng của bạn.

Điều này giúp bạn tiết kiệm rất nhiều thời gian và có thể nhận được

bạn có một nguyên mẫu hoạt động nhanh hơn nhiều.

Tuy nhiên, có một tình huống mà bạn

có thể thấy cần phải tự đào tạo trước

mô hình từ đầu.

Nếu miền mục tiêu của bạn sử dụng từ vựng và

cấu trúc ngôn ngữ không

thường được sử dụng trong ngôn ngữ hàng ngày.

Bạn có thể cần thực hiện điều chỉnh tên miền

để đạt được hiệu suất mô hình tốt.

Ví dụ: hãy tưởng tượng bạn là nhà phát triển

xây dựng một ứng dụng để giúp các luật sư và

trợ lý pháp lý tóm tắt các bản tóm tắt pháp lý.

Văn bản pháp luật sử dụng rất

các thuật ngữ cụ thể như mens rea trong

ví dụ đầu tiên và

res judicata trong phần thứ hai.

Những từ này hiếm khi được sử dụng bên ngoài

thế giới pháp luật, có nghĩa là họ

khó có thể xuất hiện rộng rãi

trong văn bản đào tạo của LLM hiện có.

Kết quả là, các mô hình có thể có

khó hiểu các điều khoản này hoặc

sử dụng chúng một cách chính xác.

Một vấn đề khác là ngôn ngữ pháp lý

đôi khi sử dụng những từ hàng ngày

trong một bối cảnh khác,

giống như sự xem xét trong ví dụ thứ ba.

Điều đó chẳng liên quan gì tới việc trở nên tử tế,

nhưng thay vào đó đề cập đến yếu tố chính của

một hợp đồng làm cho

thỏa thuận có hiệu lực thi hành.

Vì những lý do tương tự,

bạn có thể phải đối mặt với những thách thức nếu bạn cố gắng sử dụng

LLM hiện có trong ứng dụng y tế.

Ngôn ngữ y học chứa đựng nhiều điều bất thường

những từ để mô tả tình trạng bệnh lý và

thủ tục.

Và những điều này có thể không xuất hiện thường xuyên

trong tập dữ liệu huấn luyện bao gồm

mẩu tin lưu niệm trên web và văn bản sách.

Một số miền còn sử dụng ngôn ngữ

một cách rất đặc trưng.

Ví dụ cuối cùng về ngôn ngữ y tế

có thể trông giống như một chuỗi ngẫu nhiên

ký tự, nhưng nó thực sự là một tốc ký

bác sĩ dùng để viết đơn thuốc.

Văn bản này có ý nghĩa rất rõ ràng

ý nghĩa đối với một dược sĩ,

uống một viên bốn lần một ngày,

sau bữa ăn và trước khi đi ngủ.

Bởi vì người mẫu học từ vựng và

hiểu ngôn ngữ thông qua

nhiệm vụ đào tạo trước ban đầu.

Đào tạo trước mô hình của bạn từ đầu

sẽ tạo ra những mô hình tốt hơn cho

lĩnh vực chuyên môn cao như luật,

y học, tài chính hoặc khoa học.

Bây giờ hãy quay trở lại BloombergGPT,

được công bố lần đầu tiên vào năm 2023 tại

bài viết của Shijie Wu, Steven Lu,

và các đồng nghiệp tại Bloomberg.

BloombergGPT là một ví dụ về một

mô hình ngôn ngữ đã được huấn luyện trước

cho một miền cụ thể,

trong trường hợp này là tài chính.

Các nhà nghiên cứu của Bloomberg đã chọn

để kết hợp cả dữ liệu tài chính và

dữ liệu thuế cho mục đích chung để huấn luyện trước

mô hình đạt giải Bestinclass

kết quả dựa trên các tiêu chuẩn tài chính.

Đồng thời duy trì tính cạnh tranh

hiệu suất trên mục đích chung LLM

điểm chuẩn.

Vì vậy, tác giả đã lựa chọn dữ liệu

bao gồm 51% dữ liệu tài chính và

49% dữ liệu công khai

Trong bài báo của họ,

các nhà nghiên cứu của Bloomberg mô tả

kiến trúc mô hình chi tiết hơn.

Họ cũng thảo luận về cách họ bắt đầu với

luật chia tỷ lệ chinchilla để được hướng dẫn và

nơi họ phải đánh đổi.

Hai biểu đồ này so sánh một số LLM,

bao gồm BloombergGPT,

để mở rộng quy luật đã được

được các nhà nghiên cứu thảo luận.

Ở bên trái, các đường chéo theo dõi

kích thước mô hình tối ưu tính bằng tỷ

của các thông số cho

một loạt các ngân sách tính toán.

Ở bên phải, các đường theo dõi quá trình tính toán

kích thước tập dữ liệu đào tạo tối ưu

được đo bằng số lượng token.

Đường nét đứt màu hồng trên mỗi biểu đồ

cho biết ngân sách điện toán

nhóm Bloomberg đã sẵn sàng cho

đào tạo mô hình mới của họ.

Các vùng tô màu hồng tương ứng với

tính toán tổn thất tỷ lệ tối ưu được xác định trong

giấy Chinchilla.

Về kích thước mô hình, bạn có thể thấy

BloombergGPT đại khái tuân theo

cách tiếp cận Chinchilla cho vấn đề đã cho

ngân sách tính toán 1,3 triệu giờ GPU,

hoặc khoảng 230.000.000 petaflop.

Mô hình chỉ có một chút

phía trên vùng bóng mờ màu hồng,

gợi ý số lượng tham số

là khá gần mức tối ưu.

Tuy nhiên, số lượng token thực tế được sử dụng

để đào tạo trước BloombergGPT 569.000.000.000

thấp hơn mức Chinchilla được đề xuất

giá trị cho ngân sách điện toán có sẵn.

Dữ liệu đào tạo nhỏ hơn tối ưu

thiết lập là do sự sẵn có hạn chế của

dữ liệu miền tài chính.

Cho thấy những hạn chế trong thế giới thực

có thể buộc bạn phải đánh đổi khi

đào tạo trước các mô hình của riêng bạn.

Chúc mừng bạn đã làm

đến hết tuần thứ nhất,

bạn đã bao quát rất nhiều lĩnh vực, vì vậy hãy

hãy dành một phút để tóm tắt lại những gì bạn đã thấy.

Mike đã hướng dẫn bạn một số

các trường hợp sử dụng phổ biến cho LLM,

chẳng hạn như viết luận văn,

tóm tắt và dịch đoạn hội thoại.

Sau đó ông đã trình bày chi tiết về

kiến trúc máy biến áp cung cấp năng lượng

những mô hình này.

Và thảo luận về một số thông số bạn

có thể sử dụng tại thời điểm suy luận để tác động

đầu ra của mô hình.

Anh ấy kết thúc bằng việc giới thiệu bạn với

một vòng đời dự án AI tổng quát mà bạn

có thể sử dụng để lập kế hoạch và

hướng dẫn công việc phát triển ứng dụng của bạn.

Tiếp theo, bạn đã thấy cách đào tạo người mẫu

trên số lượng lớn dữ liệu văn bản

trong quá trình đào tạo ban đầu

giai đoạn được gọi là đào tạo trước.

Đây là nơi phát triển các mô hình

sự hiểu biết của họ về ngôn ngữ.

Bạn đã khám phá một số tính toán

thách thức của việc đào tạo những mô hình này,

đó là những điều đáng kể.

Trong thực tế vì

hạn chế bộ nhớ GPU,

bạn hầu như sẽ luôn sử dụng một số hình thức

lượng tử hóa khi đào tạo mô hình của bạn.

Bạn kết thúc tuần bằng cuộc thảo luận về

định luật tỷ lệ đã được phát hiện cho

LLM và cách chúng có thể được sử dụng để

thiết kế tính toán mô hình tối ưu.

Nếu bạn muốn đọc thêm chi tiết,

hãy chắc chắn kiểm tra cái này

bài tập đọc hàng tuần.