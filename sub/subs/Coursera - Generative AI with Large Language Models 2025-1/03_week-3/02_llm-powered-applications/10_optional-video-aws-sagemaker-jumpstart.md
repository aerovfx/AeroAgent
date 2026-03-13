# 10 tùy chọn-video-aws-sagemaker-khởi động

---

Bây giờ bạn đã khám phá

những điều cơ bản của

ứng dụng xây dựng

sử dụng LLM,

Tôi muốn cho bạn xem

một dịch vụ AWS

được gọi là Amazon

Khởi động Sagemaker,

điều đó có thể giúp bạn

đi vào sản xuất

nhanh chóng và hoạt động ở quy mô lớn.

Đây là ứng dụng

ngăn xếp mà bạn

đã khám phá ở video trước.

Như bạn đã thấy, việc xây dựng

một ứng dụng hỗ trợ LLM

đòi hỏi nhiều thành phần.

Sagemaker JumpStart

là một trung tâm kiểu mẫu,

và nó cho phép bạn

triển khai nhanh chóng

các mô hình nền tảng được

có sẵn trong dịch vụ,

và tích hợp chúng vào

các ứng dụng của riêng bạn.

Dịch vụ JumpStart

cũng cung cấp

một cách dễ dàng để tinh chỉnh

và triển khai các mô hình.

JumpStart bao gồm nhiều phần của

sơ đồ này, bao gồm

cơ sở hạ tầng,

bản thân LLM,

các công cụ và khuôn khổ,

và thậm chí cả API để

gọi mô hình.

Ngược lại với các mô hình

rằng bạn đã làm việc

trong phòng thí nghiệm,

Các mô hình JumpStart yêu cầu GPU

để tinh chỉnh và triển khai.

Và hãy nhớ rằng, những GPU này

tùy thuộc vào yêu cầu

giá cả và bạn

nên tham khảo

Trang định giá Sagemaker

trước khi chọn

tính toán bạn muốn sử dụng.

Ngoài ra, hãy nhớ xóa

mô hình Sagemaker

điểm cuối khi không ở trong

sử dụng và theo dõi giám sát chi phí

thực tiễn tốt nhất để tối ưu hóa chi phí.

Hãy để tôi chỉ cho bạn một chuyến tham quan nhanh

JumpStart và cách truy cập

nó từ tài khoản AWS của riêng bạn.

Sagemaker JumpStart là

có thể truy cập từ bảng điều khiển AWS,

hoặc thông qua studio Sagemaker.

Đối với chuyến tham quan ngắn này,

Tôi sẽ bắt đầu trong studio rồi chọn

JumpStart từ màn hình chính.

Tôi có thể tùy ý chọn

Khởi động từ

menu bên trái,

và chọn mẫu, sổ ghi chép,

và cả các giải pháp.

Sau khi tôi nhấp vào "JumpStart",

bạn sẽ thấy khác

các danh mục bao gồm

giải pháp đầu cuối trên toàn

trường hợp sử dụng khác nhau,

cũng như một số

mô hình nền tảng cho

phương thức khác nhau

mà bạn có thể dễ dàng triển khai,

cũng như tinh chỉnh,

trong đó có được chỉ định dưới

tùy chọn tinh chỉnh.

Chúng ta hãy nhìn vào một

ví dụ bạn là tất cả

làm quen sau khi làm việc

thông qua khóa học,

đó là mẫu Flan-T5.

Bạn đã đặc biệt

sử dụng biến thể cơ sở trong

khóa học để giảm thiểu

các nguồn lực cần thiết bởi

các môi trường phòng thí nghiệm.

Tuy nhiên, như bạn có thể thấy ở đây,

bạn cũng có thể sử dụng

các biến thể khác của

Flan-T5 thông qua JumpStart

tùy thuộc vào nhu cầu của bạn.

Bạn cũng sẽ nhận thấy

Logo ôm mặt ở đây,

điều đó có nghĩa là họ

thực sự đang đến

trực tiếp từ Ôm Mặt.

Và AWS đã làm việc với

Ôm mặt vào vấn đề

nơi bạn có thể dễ dàng,

chỉ với vài cú nhấp chuột, triển khai,

hoặc tinh chỉnh mô hình.

Nếu tôi chọn Flan-T5 Base,

bạn sẽ thấy tôi có một vài lựa chọn.

Đầu tiên mình có thể chọn triển khai

mô hình bằng cách xác định

một số thông số chính như

loại và kích thước cá thể.

Và đây là

loại và kích thước phiên bản

cái đó nên dùng

để lưu trữ mô hình.

Và như một lời nhắc nhở,

cái này triển khai theo thời gian thực

điểm cuối liên tục,

và giá cả phụ thuộc vào

ví dụ lưu trữ

mà bạn chọn ở đây.

Và một số trong số này

có thể khá lớn,

vì vậy hãy luôn nhớ xóa

bất kỳ điểm cuối nào

không được sử dụng

để tránh phát sinh

mọi chi phí không cần thiết.

Bạn cũng sẽ nhận thấy

bạn có thể chỉ định

một số cài đặt bảo mật

cho phép bạn thực hiện

các điều khiển đó là

mua lại cho riêng bạn

yêu cầu bảo mật.

Sau đó bạn có thể chọn

để nhấn "Triển khai",

và điều này sẽ

tự động triển khai

mẫu Flan-T5 Base đó để

điểm cuối bằng cách sử dụng

cơ sở hạ tầng mà bạn chỉ định.

Trong tab thứ hai,

bạn sẽ nhận thấy

lựa chọn để đào tạo.

Bởi vì mô hình này

hỗ trợ tinh chỉnh,

bạn cũng có thể thiết lập

tinh chỉnh công việc bằng cách chỉ định

địa điểm đào tạo của bạn

và bộ dữ liệu xác thực,

sau đó chọn kích thước của

tính toán mà bạn muốn

để sử dụng cho việc đào tạo.

Và đó chỉ là một sự điều chỉnh dễ dàng

theo kích thước tính toán

thông qua trình đơn thả xuống này,

bạn có thể dễ dàng

chọn loại gì

tính toán bạn muốn sử dụng

cho công việc đào tạo của bạn.

Và hãy ghi nhớ một lần nữa,

bạn bị tính phí cho

tính toán cơ bản

trong khoảng thời gian cần thiết

để huấn luyện mô hình.

Vì vậy chúng tôi khuyên bạn nên chọn

trường hợp nhỏ nhất đó là

cần thiết cho nhiệm vụ cụ thể của bạn.

Một tính năng khác là khả năng

để nhanh chóng xác định và sửa đổi

các siêu tham số có thể điều chỉnh cho

mô hình cụ thể này

thông qua các danh sách thả xuống này.

Nếu chúng ta tiếp tục và cuộn

xuống phía dưới,

bạn sẽ thấy một tham số

loại được gọi là PEFT,

tham số hiệu quả

tinh chỉnh mà bạn

đã học ở bài 6.

Ở đây bạn có thể chọn Laura,

mà bạn đã học trong

Bài 4 chỉ qua

một danh sách thả xuống đơn giản,

làm cho nó dễ dàng hơn để thực hiện

những kỹ thuật khác nhau này

mà bạn đã học.

Sau đó bạn có thể tiếp tục

và nhấn "Tàu".

Và điều đó sẽ bắt đầu

một công việc đào tạo để

tinh chỉnh việc đào tạo trước này

Model Flan-T5 sử dụng đầu vào

được cung cấp cho nhiệm vụ cụ thể của bạn.

Cuối cùng, đây là một cái khác

tùy chọn đó là

có JumpStart tự động

tạo một cuốn sổ tay cho bạn.

Hãy nói rằng bạn không thích

bằng cách sử dụng trình đơn thả xuống,

và ưu tiên lập trình

làm việc với những mô hình này.

Cuốn sổ này về cơ bản

cung cấp cho bạn tất cả mã

đằng sau những gì đang xảy ra

các lựa chọn mà chúng tôi

được che phủ trước đó.

Đây là một lựa chọn nếu

bạn thích làm việc với

Khởi động ở mức thấp nhất

cấp độ theo chương trình.

Đó chỉ là một chuyến tham quan nhanh

của JumpStart để minh họa

triển khai một trung tâm kiểu mẫu

mà bạn đã học

về trong khóa học.

Ngoài vai trò là

một trung tâm mô hình bao gồm

mô hình nền tảng,

JumpStart cũng cung cấp rất nhiều

tài nguyên về mặt blog,

video và ví dụ

sổ tay cũng vậy.

Tôi chắc chắn khuyến khích

bạn kiểm tra xem nó ra

nhiều hơn nữa bằng cách khám phá

mô hình nền tảng khác nhau,

và các biến thể của chúng

có sẵn

để giúp bạn bắt đầu nhanh chóng.