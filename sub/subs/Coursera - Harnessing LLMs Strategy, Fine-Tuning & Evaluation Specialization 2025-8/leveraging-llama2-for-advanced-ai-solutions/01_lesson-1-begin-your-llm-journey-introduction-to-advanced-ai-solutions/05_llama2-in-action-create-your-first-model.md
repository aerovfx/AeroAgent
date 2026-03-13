# 05 llama2-in-action-tạo-mô hình đầu tiên của bạn

---

Bạn đã tò mò chưa

về cách xây dựng

một cố vấn AI sẽ hướng dẫn bạn

thậm chí thông qua

chủ đề phức tạp nhất?

Vâng, trong video này,

bạn sẽ học cách

để tùy chỉnh Llama 2

để trở thành của bạn

chuyên gia AI cá nhân.

Đến cuối video,

bạn sẽ có thể

trò chuyện với một người mẫu

hoạt động giống như một AI

nhà nghiên cứu tại Meta,

và bạn sẽ có thể

định cấu hình tệp mô hình Ollama và

đánh giá tác dụng của

điều chỉnh mô hình và

kỹ thuật nhanh chóng.

Bây giờ chúng ta hãy đi sâu vào và

xem chúng ta có thể xoay chuyển thế nào

Llama 2 thành một

cố vấn AI am hiểu.

Siêu tham số của mô hình.

Nổi bật nhất

cơ hội để tùy chỉnh

mô hình Llama 2 là

điều chỉnh các mô hình

siêu tham số.

Âm thanh khá cao cấp,

đúng, trên thực tế, nó đơn giản.

Bạn có thể tưởng tượng các siêu tham số

như các nút bấm và

công tắc điều khiển như thế nào

ngôn ngữ lớn của bạn

mô hình học từ dữ liệu.

Chúng ảnh hưởng đến kiến trúc,

sự tối ưu hóa và

chính quy hóa mô hình.

Siêu tham số không

được học từ chính mô hình đó,

mà đúng hơn là bởi e. có

một vài thông số,

và phù hợp nhất cho

mục tiêu của chúng tôi là nhiệt độ.

Hãy nghĩ về nhiệt độ như

thước đo sáng tạo,

nó càng cao,

càng nhiều entropy

họ sẽ có phản ứng.

Nó có thể tiếp tục tìm kiếm mọi thứ

nghe có vẻ như

họ đi cùng nhau.

Nó thực sự có thể phát điên nếu

Tuy nhiên, bạn đã đi quá thấp,

mô hình trở nên xác định.

Nó sẽ luôn tạo ra

câu trả lời chính xác như nhau.

Bạn có thể viết mã theo nếu

bạn đã cài đặt

sự phụ thuộc như

được hiển thị trong video cuối cùng.

Hoặc chỉ xem và kiểm tra

nhánh file mẫu 01 sau

vào để xem xét chi tiết.

Để điều chỉnh siêu tham số và đặt

cài đặt thiết yếu

cho mô hình Llama của chúng tôi.

Ollama sử dụng như vậy

được gọi là tập tin mô hình.

Chúng ta có thể chỉ cần tạo một cái bằng cách

tạo một tập tin mới và

chúng tôi gọi nó là tập tin mô hình,

đi kèm mà không có bất kỳ loại tập tin.

Tiếp theo, chúng ta đi sâu vào thực tế

điều chỉnh mô hình Llama.

Đầu tiên, chúng tôi xác định mô hình

chúng tôi muốn làm việc cùng.

Chúng tôi bắt đầu với việc xác định

mô hình cơ sở.

Chúng tôi vừa tải xuống trước đó,

sử dụng chữ viết hoa

từ lệnh.

Dòng này nói với Ollama

chúng ta là người mẫu nào

được xây dựng từ.

Tiếp theo chúng ta sẽ điều chỉnh phím

nhiệt độ siêu tham số.

Theo mặc định,

nhiệt độ được đặt thành 0,8,

nhưng vì mục đích của chúng tôi,

chúng tôi muốn mô hình phát ra âm thanh

năng động và sáng tạo hơn.

Chúng tôi sẽ gửi nó tới một người,

điều này mang lại sự linh hoạt hơn

và sự sáng tạo trong những phản ứng của nó,

làm cho nó cảm thấy nhiều hơn

trò chuyện và ít robot hơn.

Giá trị nhiệt độ cao cho phép

mô hình để khám phá một

phạm vi đầu ra rộng,

thật biết ơn khi chúng ta

muốn có một con người hơn

thích cuộc trò chuyện.

Bây giờ hãy xác định

tin nhắn hệ thống,

mang lại cho mô hình

một vai trò trong bối cảnh.

Trong trường hợp này, chúng tôi đang nói

mô hình đó là

một nhà nghiên cứu AI đã gọi

Jake làm việc tại Meta.

Mục tiêu ở đây là đảm bảo

mà mô hình có thể giải thích

chủ đề AI phức tạp trong đơn giản

thuật ngữ dành cho người mới bắt đầu.

Thông báo hệ thống đơn giản này

thiết lập giai điệu cho cách

mô hình sẽ trả lời.

Đó là một cách mạnh mẽ để

hướng dẫn hành vi của AI

và tập trung nó vào một

tính cách hoặc vai trò cụ thể.

Cuối cùng, để áp dụng những thay đổi này,

chúng ta phải tạo ra

một phiên bản mới của

mô hình và để có được điều đó,

chúng tôi thực sự điều hành Ollama

tạo để xây dựng

mô hình tùy chỉnh của chúng tôi và

sau đó theo dõi bằng cách

Ollama Chạy để bắt đầu

tương tác với nó.

Thế thôi. Chỉ trong vài bước,

chúng tôi đã tạo ra một AI

nhà nghiên cứu có thể

giúp giải thích nhỏ gọn

linh hoạt các chủ đề AI cho chúng tôi.

Bây giờ là lúc để thực sự kiểm tra.

Đầu tiên, chúng tôi hỏi người mẫu, này,

bạn là ai và

xem nó chặt chẽ đến mức nào

phù hợp với vai trò chúng tôi đặt ra

trong tin nhắn hệ thống.

Bước tiếp theo là đánh giá

chúng ta gần nhau hơn bao nhiêu

đã phải xây dựng

một AI có thể giải thích về Llama

để nghiên cứu bài viết một cách chi tiết.

Bây giờ chúng tôi yêu cầu nó

về mục lục

của chính tờ giấy đó.

Có vẻ như mô hình thực sự

đã thực sự cho chúng tôi

câu trả lời tự tin,

nhưng bây giờ hãy kiểm tra thực tế nếu

phản ứng đó là

thực sự đúng.

Như bạn thấy, nó quay

ra trong khi câu trả lời

nghe có vẻ hợp lý, đó là

thực tế là không chính xác.

Mẫu vừa làm xong

mục lục đó.

Điều chúng ta vừa chứng kiến

là một trong những chính

thách thức của

làm việc với ngôn ngữ lớn

mô hình, ảo giác.

Nhưng tại sao điều này lại xảy ra?

Vâng, hãy nhớ lớn

mô hình ngôn ngữ tạo ra

thống kê nhất

khả năng phản ứng

dựa trên đầu vào của bạn và

bối cảnh trước đó.

Đối với người mẫu, có vẻ như

giống như một cách hoàn hảo

câu trả lời hợp lý.

Có vẻ như chúng tôi

vẫn còn rất nhiều

công việc để đạt được mục tiêu của chúng ta.

Trong các video tiếp theo,

bạn sẽ khám phá cách giải quyết

những hạn chế này và xây dựng

một giải pháp AI đáng tin cậy hơn.

Trước khi kết thúc, tôi muốn

bạn hãy tự hỏi mình.

Cách tốt nhất để hỏi là gì

câu hỏi về mô hình AI mới của bạn

để khám phá khả năng của nó và

tìm hiểu xem nó có

ảo giác hay không?

Trong video này, bạn

bắt đầu hiểu và

tùy chỉnh Llama bằng cách sử dụng

Tệp mô hình Ollama.

Bạn cũng đánh giá tác động lên

mô hình Llama đơn giản và

đánh giá

kỹ thuật tối ưu hóa

của kỹ thuật nhanh chóng.

Thật không may, không

vấn đề nhắc nhở,

mô hình vẫn còn

ảo giác khi nó

đến với câu hỏi

về tờ giấy thực tế.

Hãy luôn tò mò và

tiếp tục thử nghiệm.

Bây giờ tôi có thêm một cái nữa

câu hỏi dành cho bạn.