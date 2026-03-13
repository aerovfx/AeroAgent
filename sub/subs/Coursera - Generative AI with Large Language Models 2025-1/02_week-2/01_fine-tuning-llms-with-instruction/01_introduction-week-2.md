# 01 giới thiệu-tuần-2

---

Chào mừng trở lại, tôi ở đây với những người hướng dẫn của tôi

cho tuần này, Mike và Shelby.

Tuần trước bạn đã học về máy biến áp

mạng, đây thực sự là nền tảng quan trọng

cho các mô hình ngôn ngữ lớn, cũng như

Vòng đời dự án Genitive AI.

Và tuần này có

còn nhiều điều nữa để tìm hiểu sâu hơn,

bắt đầu với việc điều chỉnh hướng dẫn

của các mô hình ngôn ngữ lớn.

Và sau đó thực hiện như thế nào

điều chỉnh một cách hiệu quả.

>> Vâng, vậy

chúng ta hãy xem hướng dẫn tinh chỉnh,

vì vậy khi bạn có mô hình cơ sở,

thứ được đào tạo trước ban đầu,

nó được mã hóa rất nhiều thứ thực sự tốt

thông tin, thường là về thế giới.

Vì vậy, nó biết về mọi thứ, nhưng

nó không nhất thiết phải biết làm thế nào để có thể

để trả lời những lời nhắc nhở, những câu hỏi của chúng tôi.

Vì vậy khi chúng tôi hướng dẫn nó

để thực hiện một nhiệm vụ nhất định,

nó không nhất thiết

biết cách trả lời.

Và do đó việc hướng dẫn tinh chỉnh sẽ giúp

nó có thể thay đổi hành vi của nó

để giúp ích nhiều hơn cho chúng tôi.

>> Tôi nghĩ hướng dẫn tinh chỉnh

là một trong những bước đột phá lớn trong

lịch sử thực sự của

mô hình ngôn ngữ lớn

Bởi vì bằng cách học từ văn bản chung

ngoài Internet và các nguồn khác,

bạn học cách dự đoán từ tiếp theo.

Bằng cách dự đoán từ tiếp theo trên

Internet không giống như sau

hướng dẫn.

Tôi nghĩ thật tuyệt vời khi bạn có thể

lấy một mô hình ngôn ngữ lớn,

đào tạo nó trên hàng trăm tỷ

của các từ trên Internet.

Và sau đó tinh chỉnh nó với kích thước nhỏ hơn nhiều

tập dữ liệu theo hướng dẫn sau và

chỉ cần học cách làm điều đó.

>> Đúng vậy và một trong những điều

tất nhiên là bạn phải đề phòng,

là sự lãng quên thảm khốc và

đây là một cái gì đó mà chúng tôi

nói về trong khóa học.

Vì vậy, đó là nơi bạn đào tạo mô hình

một số dữ liệu bổ sung trong hướng dẫn điên rồ này

tinh chỉnh.

Và rồi nó quên đi tất cả

những thứ mà nó đã có trước đó, hoặc

một phần lớn dữ liệu đó

mà nó đã có trước đó.

Và vì vậy có một số kỹ thuật

mà chúng ta sẽ nói về

khóa học để giúp chống lại điều đó.

Chẳng hạn như làm hướng dẫn tinh chỉnh

trên một phạm vi thực sự rộng của

các loại hướng dẫn khác nhau.

Vì vậy đây không chỉ là trường hợp điều chỉnh

đó chỉ là điều bạn muốn nó làm.

Bạn có thể phải có một chút

rộng hơn thế nữa, nhưng

chúng ta nói về nó trong khóa học.

>> Và thế là hóa ra có hai

các loại tinh chỉnh rất có giá trị

đang làm.

Một là hướng dẫn tinh chỉnh

chúng ta vừa nói đến, Mike.

Và sau đó khi một nhà phát triển cụ thể

đang cố gắng tinh chỉnh nó cho

ứng dụng riêng của họ, cho

một ứng dụng chuyên biệt.

Một trong những vấn đề về tinh chỉnh

bạn lấy một mô hình khổng lồ và

bạn tinh chỉnh từng cái một

tham số trong mô hình đó.

Bạn có điều lớn lao này để

lưu trữ xung quanh và triển khai, và

nó thực sự rất tính toán và

bộ nhớ mở rộng.

Thật may mắn,

có những kỹ thuật tốt hơn thế.

>> Đúng rồi, chúng ta đang nói về tham số

tinh chỉnh hiệu quả hoặc viết tắt là PEFT,

như một tập hợp các phương pháp có thể cho phép bạn

giảm bớt một số mối lo ngại đó, phải không?

Vì vậy chúng tôi có rất nhiều khách hàng

muốn có thể điều chỉnh cho

nhiệm vụ rất cụ thể,

những miền rất cụ thể.

Và tinh chỉnh tham số hiệu quả là

một cách tuyệt vời để vẫn đạt được điều tương tự

kết quả thực hiện trên nhiều nhiệm vụ

mà bạn có thể làm được với sự tinh chỉnh đầy đủ.

Nhưng sau đó thực sự lợi dụng

kỹ thuật cho phép bạn đóng băng những

trọng lượng mô hình ban đầu.

Hoặc thêm các lớp thích ứng lên trên đó với

dung lượng bộ nhớ nhỏ hơn nhiều, phải không?

Để bạn có thể đào tạo cho nhiều nhiệm vụ.

>> Trên thực tế, một trong những kỹ thuật

Tôi biết bạn đã sử dụng LoRA rất nhiều.

Tôi nhớ khi tôi đọc bài báo của LoRA,

Tôi nghĩ, điều này thật có ý nghĩa,

điều này sẽ thành công.

>> Đúng vậy, chúng ta thấy rất nhiều

nhu cầu phấn khích xung quanh LoRA

vì hiệu suất

kết quả sử dụng

những ma trận xếp hạng thấp trái ngược

để tinh chỉnh đầy đủ, phải không?

Vì vậy, bạn có thể trở nên thực sự tốt

kết quả hiệu suất với tính toán tối thiểu

và yêu cầu về bộ nhớ.

>> Vậy điều tôi đang thấy trong số

rất nhiều nhà phát triển khác nhau

các nhà phát triển thường sẽ bắt đầu

tắt với sự nhắc nhở, và

đôi khi điều đó mang lại cho bạn đủ tốt

hiệu suất và điều đó thật tuyệt vời.

Và đôi khi nhắc nhở lượt truy cập

mức trần về hiệu suất và

thì kiểu tinh chỉnh này với LoRA hoặc

kỹ thuật PEFT khác

thực sự quan trọng đối với

mở khóa hiệu suất cấp độ bổ sung đó.

Và điều khác tôi đang thấy

trong số rất nhiều nhà phát triển OM

là một cuộc thảo luận tranh luận về

chi phí sử dụng một mô hình khổng lồ,

đó là rất nhiều lợi ích so với của bạn

ứng dụng tinh chỉnh một mô hình nhỏ hơn.

>> Chính xác, tinh chỉnh đầy đủ

có thể rất tốn kém, phải không?

Nói ít nhất là như vậy

khả năng thực sự có thể

sử dụng các kỹ thuật như PEFT để đặt

tinh chỉnh loại mô hình AI tổng quát

trong tay người dùng hàng ngày.

Điều đó có những hạn chế về chi phí và

họ có ý thức về chi phí,

khá nhiều đấy mọi người

trong thế giới thực, phải không?

>> Đúng vậy và tất nhiên,

nếu bạn lo lắng về việc ở đâu

dữ liệu của bạn cũng đang diễn ra.

Vì vậy nếu cần phải như vậy

đang chạy trong tầm kiểm soát của bạn,

sau đó có một mô hình của

một kích thước phù hợp là thực sự quan trọng.

>> Và một lần nữa, rất nhiều

nội dung thú vị để đi sâu vào tuần này.

Chúng ta hãy chuyển sang video tiếp theo nơi Mike

sẽ bắt đầu mọi thứ với sự hướng dẫn

tinh chỉnh.