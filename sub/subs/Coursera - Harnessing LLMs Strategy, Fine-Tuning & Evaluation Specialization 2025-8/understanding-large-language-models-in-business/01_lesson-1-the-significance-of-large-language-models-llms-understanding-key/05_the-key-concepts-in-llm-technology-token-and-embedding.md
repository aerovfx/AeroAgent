# 05-khái niệm-chìa khóa-trong-llm-công nghệ-mã thông báo-và-nhúng

---

Trong video này, chúng tôi

sẽ đi sâu hơn vào

các khối xây dựng kỹ thuật

của các mô hình ngôn ngữ lớn.

Chúng ta sẽ bắt đầu bằng

khám phá khái niệm

của những lời nhắc và

kỹ thuật nhanh chóng,

đóng vai trò quan trọng trong

tối ưu hóa

hiệu suất của LLM.

Sau đó chúng ta sẽ khám phá hai

các yếu tố nền tảng của LLM,

mã thông báo và phần nhúng.

Điều này giúp chúng ta hiểu cách

những mô hình này xử lý

và giải nghĩa ngôn ngữ.

Đến cuối video này,

bạn sẽ học được cách hiểu

của mã thông báo và phần nhúng

trợ giúp về mặt kỹ thuật nhanh chóng để

cải thiện đáng kể

hiệu suất của LLM.

Kỹ thuật nhanh chóng đề cập đến

định dạng chiến lược của

văn bản chúng tôi nhập vào LLM.

Một công trình được xây dựng tốt

lời nhắc cung cấp

bối cảnh phù hợp và hiệu quả

giới hạn phạm vi của

phản ứng của các mô hình.

Vì vậy, nó giúp với

tối ưu hóa

hiệu suất mô hình.

Sự chế tạo cẩn thận này

lời nhắc là

một khía cạnh quan trọng trong việc tận dụng

sức mạnh của LLM một cách hiệu quả.

Bây giờ chúng ta đã biết

lời nhắc là gì,

Hãy cùng khám phá token là gì.

Token là cơ bản

đơn vị thông tin

LLM lấy làm đầu vào

để xử lý.

Chúng có thể là những từ,

dấu chấm câu hoặc số.

Về cơ bản, bất kỳ sự rời rạc nào

phần tử trong một chuỗi văn bản.

Ví dụ, cụm từ,

con mèo ngồi lên,

sẽ được xử lý bởi

một mô hình ngôn ngữ lớn như

bốn mã thông báo riêng biệt: the,

mèo, ngồi, trên.

Chúng tôi cũng có một khái niệm

được gọi là token hóa.

Token hóa là

quá trình phân chia

văn bản vào đây

đơn vị cơ bản hoặc

mã thông báo sử dụng các quy tắc cụ thể để

xử lý các yếu tố ngôn ngữ

như dấu câu

và các cơn co thắt.

Đây là một điều quan trọng

bước chuẩn bị

văn bản tính toán

xử lý bởi LLM.

Bây giờ chúng ta hãy cố gắng hiểu

nhúng trong

bối cảnh của LLM.

Chúng tôi đã thảo luận về các token và

quá trình token hóa,

nơi văn bản được chia thành một

phần nhỏ hơn, dễ quản lý hơn.

Nhúng là bước tiếp theo.

Có cách LLM chuyển đổi

những token này vào

dạng số mà mô hình

có thể hiểu và xử lý.

Về cơ bản, nhúng là

vectơ đa chiều

đại diện cho mỗi mã thông báo.

Ví dụ, con mèo mã thông báo

được chuyển đổi thành một nhúng,

một vectơ có giá trị bằng số.

Vectơ này chứa đựng toàn diện

thông tin về mèo,

bao gồm ý nghĩa của nó và

nó được sử dụng như thế nào trong

bối cảnh khác nhau.

Các vectơ số này

là rất quan trọng bởi vì

họ cho phép các token được

được nhóm lại dựa trên sự giống nhau.

S và LLM tiếp tục

để học hỏi và rèn luyện,

nó cập nhật liên tục

những vectơ này,

để tinh chỉnh độ chính xác

và sự liên quan

về cách mỗi thứ này

token được đại diện.

Tóm lại, chúng tôi đã

đã khám phá các gợi ý và

hai kỹ thuật quan trọng

những khái niệm trao quyền

mô hình ngôn ngữ lớn;

mã thông báo và nhúng.

Token đóng vai trò là

từ rời rạc

giống như các đơn vị tạo thành

cơ sở đầu vào của mô hình,

trong khi nhúng là

sự tinh vi

biểu diễn vector

nắm bắt được

mối quan hệ ngữ nghĩa

giữa các token đó.

Hiểu những điều này

các khái niệm rất quan trọng đối với

đánh giá cao cách LLM diễn giải

và tạo ra ngôn ngữ.

Chúng ta sẽ tìm hiểu hai

khái niệm quan trọng khác

của LLM mà

là máy biến áp và

cơ chế tự chú ý

trong video tiếp theo.

Bây giờ tôi có một câu hỏi cho bạn.