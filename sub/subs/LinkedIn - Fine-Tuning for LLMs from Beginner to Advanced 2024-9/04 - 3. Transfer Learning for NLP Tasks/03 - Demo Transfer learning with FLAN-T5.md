# 03 - Demo Học chuyển giao với FLAN-T5

---

- Trong bản demo này,

chúng tôi sẽ dịch từ tiếng Anh

sang tiếng Tây Ban Nha bằng Flan-T5

và chúng ta sẽ thực hiện điều đó bằng cách học chuyển tiếp

trên tập dữ liệu opus-100.

Đây là một nhiệm vụ rất rất quan trọng

và đây cũng là một bản demo rất quan trọng về tổng thể

bởi vì đó là một trong những điều

mà chúng ta sẽ làm thường xuyên nhất.

Vì vậy, nói rằng, hãy kết nối với GPU.

Hoàn hảo, giờ chúng ta đã có GPU,

như bạn biết điều đầu tiên chúng ta cần làm

là thực hiện cài đặt pip.

Hoàn hảo, bây giờ quá trình cài đặt pip đã hoàn tất,

bạn có thể tưởng tượng bước thứ hai

là tải xuống mô hình mã thông báo.

Lưu ý rằng đối với bản demo cụ thể này,

chúng tôi sẽ sử dụng đế 5 Flan-T5,

thay vì lớn và lý do duy nhất là mất ít thời gian hơn

trong quá trình đào tạo, một cách trung thực.

Bạn có thể sử dụng lớn và nó sẽ hoạt động tốt,

bạn có thể sử dụng loại nhỏ nếu bạn không có GPU,

mọi chuyện sẽ ổn thôi, được chứ?

Sự khác biệt về kích thước sẽ là công suất

thực hiện nhiệm vụ ngày càng tốt hơn, phải không?

Thế là xong, mô hình của chúng ta đã được tải xuống,

vì vậy bây giờ chúng ta phải tải tập dữ liệu và bật,

bật lại tập dữ liệu thấp từ gói tập dữ liệu.

Chúng ta chỉ cần đặt tên của tập dữ liệu

trong trường hợp này là Helsinki-NLP

từ Đại học Helsinki opus-100,

và chúng ta sẽ chọn biến thể EN gạch nối ES,

điều đó có nghĩa là tiếng Anh sang tiếng Tây Ban Nha và hãy in một ví dụ.

Bạn có nhận thấy một mô hình?

Vâng, điều này giống như chúng ta đã làm ở chương hai.

Bạn có thể thấy nó lặp lại mã như thế nào, chúng ta đây,

và bạn có thể thấy rằng một ví dụ về cơ bản là một bản dịch

và sau đó nó có phần tiếng Anh và phần tiếng Tây Ban Nha.

Vì vậy bây giờ chúng ta sẽ tiến hành xử lý trước dữ liệu.

Đây là một điều mới mẻ đối với bạn,

nhưng hãy tin tôi đi, nó sẽ lặp đi lặp lại nhiều lần.

Vậy nên hãy làm từng chút một nhé, đừng lo lắng.

The first thing we need to do

là tạo ra những lời nhắc thực tế

vì chúng tôi có bản dịch sang tiếng Tây Ban Nha,

đó là mục tiêu thực tế, điều đó tốt,

nhưng bằng tiếng Anh chúng tôi chỉ có văn bản bằng tiếng Anh.

Hãy nhớ T5 cần biết bạn cần làm gì,

đó là lý do tại sao chúng tôi sẽ thêm bản dịch vào phần đầu vào

từ tiếng Anh sang tiếng Tây Ban Nha cho đến mọi ví dụ.

Khi chúng tôi có đầu vào và mục tiêu,

chúng tôi sẽ chuyển thông qua mã thông báo đầu vào

và thông qua tokenizer mục tiêu.

Điều đó về cơ bản sẽ tạo ra mô hình đầu vào

những gì chúng ta sẽ chuyển qua mô hình

và nó sẽ tạo ra các nhãn.

Điều đó có nghĩa là những gì chúng ta sẽ so sánh với

để thực hiện việc đào tạo.

Cũng lưu ý một cái gì đó rất quan trọng.

Vì đây là mô hình trình tự nối tiếp trình tự,

thì bộ giải mã cũng cần đầu vào,

nhưng theo một nghĩa nào đó đó sẽ chỉ là những nhãn hiệu

bởi vì hãy nhớ rằng những gì người mẫu cần biết

là cho mỗi từ nó cần so sánh

nếu từ tiếp theo được dự đoán đúng,

chính xác là từ đó nhé.

Hãy nhớ rằng khi chúng ta thực hiện bất kỳ loại trình tự nào theo trình tự,

đây là mẫu truyền thống nên đầu vào bộ giải mã

cũng sẽ là tokenizer của mục tiêu,

và chúng tôi đặt nó vào đầu vào mô hình dưới dạng ID đầu vào của bộ giải mã.

Trong bất kỳ mô hình trình tự nào,

chúng ta sẽ cần ba thứ này trong đầu vào của mô hình

ID đầu vào nhãn và ID đầu vào bộ giải mã.

Đây là một hàm sẽ lấy một loạt ví dụ

và nó sẽ áp dụng quá trình tiền xử lý

Vậy thứ chúng ta sẽ lấy là đoàn tàu

và bộ kiểm tra.

Trong tập hợp xe lửa, chúng ta sẽ lọc nó

một lần nữa, chỉ có 30.000 ví dụ,

để làm cho việc đào tạo diễn ra nhanh hơn

Trên thực tế, bạn sẽ không làm điều đó,

và chúng tôi sử dụng chức năng bản đồ để ánh xạ chức năng này

đến từng lô của tập huấn luyện và bộ kiểm tra.

Điều đó sẽ tạo ra một đối tượng tập dữ liệu huấn luyện và kiểm tra

sẽ có tất cả ý tưởng chúng ta cần ở định dạng hàng loạt.

Nào, bạn có thể thấy nó khá nhanh

và kết quả cuối cùng trong tập dữ liệu xe lửa, ví dụ:

có bản dịch,

nhưng hãy chú ý xem chúng ta có ID đầu vào là gì,

và bên phải

chúng ta sẽ có một thứ gọi là mặt nạ chú ý

Nếu bạn biết máy biến áp và LLM,

bạn biết rằng điều này rất quan trọng để biết

những gì cần chú ý ở đầu vào và chúng tôi có nhãn

và thậm chí nhiều hơn ở bên phải,

chúng ta sẽ có ID đầu vào của bộ giải mã.

Vì vậy, chúng tôi có tất cả các yếu tố cần thiết trên tàu

và kiểm tra các bộ dữ liệu để tạo các bộ dữ liệu luồng tensor của chúng tôi,

đó là tập dữ liệu đầu vào cho mô hình

phù hợp với việc giao tiếp với người chăm sóc, hãy nhớ.

Vì vậy bây giờ chúng ta sẽ chuyển đổi các đối tượng tập dữ liệu này

vào bộ dữ liệu TensorFlow,

và chúng ta sẽ lặp lại mô hình này trong suốt

toàn bộ khóa học.

Ý tưởng luôn giống nhau.

Đối tượng, trong trường hợp này là tập dữ liệu được đào tạo,

hai tập dữ liệu TF, đây là phương pháp.

Chúng ta sẽ đặt vào các cột

những gì chúng tôi muốn chuyển dưới dạng X.

Đây sẽ là ID đầu vào, ID đầu vào của bộ giải mã,

và mặt nạ chú ý

Trong các cuộc gọi nhãn,

bạn sẽ đặt nhãn thực tế là gì

những gì bạn đang so sánh với.

Nếu chúng ta muốn xáo trộn hay không, kích thước lô, một lần nữa,

đây là 64 để chạy nhanh vì mình có RAM GPU,

nhưng nếu bạn không có nhiều RAM GPU,

ghi số 8 hoặc 16 thì được,

và sau đó chúng tôi đặt nó vào hàm đối chiếu.

Đối chiếu có nghĩa là tôi phải làm gì nếu có lô cuối cùng,

ví dụ có thể có 50 phần tử đúng không,

bởi vì chúng tôi không có đủ, vậy tôi phải làm gì?

Trong trường hợp này, chúng tôi nói không làm gì nhưng đôi khi,

chúng ta bỏ qua nó hoặc đôi khi chúng ta điền nó bằng số không,

và chúng tôi làm tương tự với tập dữ liệu thử nghiệm.

Chúng tôi chạy cái này và cái này sẽ tự động,

bởi vì điều này chạy ở chế độ lười biếng.

Đừng lo lắng về cảnh báo này.

Đây là khoảng thời gian TensorFlow 3 ra mắt,

sẽ có một chút thay đổi đối với bộ dữ liệu TensorFlow này

và trong trường hợp đó nó sẽ như vậy, ở đây nó cho bạn biết chính xác

phải làm gì, nó rất rất đơn giản

Thay vì nhãn dưới mã, nó sẽ được gọi là nhãn,

và bây giờ chúng ta sẽ thực hiện việc học chuyển giao.

Vì vậy, nếu chúng ta thực hiện tóm tắt mô hình ngay bây giờ,

chúng ta có thể thấy rằng mô hình của chúng tôi có

247 triệu thông số phải không?

Và chúng được phân phối theo cách này,

chúng ta có một bộ nhúng, một bộ mã hóa, một bộ giải mã,

và cái đầu cuối cùng để thực hiện việc dự đoán.

Điều chúng ta sắp làm là chúng ta sẽ đóng băng

bộ mã hóa và giải mã nhúng,

vì vậy chúng ta sẽ chỉ đào tạo lớp đầu cuối cùng.

Cách thực hiện điều đó luôn giống nhau, model.getlayer,

tên của lớp chúng tôi muốn .trainable

và chúng tôi đặt nó thành sai.

Nếu chúng ta thực hiện điều này thì thông báo rằng bây giờ phần tóm tắt mô hình

trong các tham số không thể huấn luyện được

chúng ta sẽ có khoảng 222 triệu thông số,

và chúng ta sẽ chỉ đào tạo 24 triệu người, ít hơn rất nhiều.

Bây giờ chúng ta đã hoàn thành việc này, chúng ta đã sẵn sàng cho việc lắp đặt.

Đây là việc học chuyển giao.

Chúng tôi có một mô hình, chúng tôi chuyển giao kiến thức từ T5,

và chúng tôi đã đóng băng phần đầu tiên.

Chúng ta sẽ chỉ đào tạo phần cuối cùng.

Bây giờ chúng ta hãy đi đến các khái niệm quan trọng.

để đào tạo một mô hình từ giai đoạn hack,

Tôi đã nói với bạn trong slide,

chúng ta luôn cần có entropy chéo phân loại thưa thớt,

và chúng ta cần đặt logic bằng true.

Đây là hai điều kiện rất quan trọng

cho bất kỳ mô hình giai đoạn cao cấp.

Thực ra, phía trên bạn có một tin nhắn đề phòng trường hợp bạn quên

vì vậy bạn có nó với bạn.

Đối với trình tối ưu hóa, chúng tôi sẽ sử dụng Adam,

và trong trường hợp này, hãy để tôi đặt Adam,

vì vậy bạn đã quen với việc chạy trình tối ưu hóa và nó chỉ hoạt động.

Bạn có thể sử dụng lớp hoặc chuỗi,

Thành thật mà nói thì đối với chúng tôi cũng vậy.

Và sau đó chúng tôi làm mô hình phù hợp,

chúng tôi chỉ phân tích tập dữ liệu tàu và dữ liệu xác thực,

tập dữ liệu thử nghiệm và chúng tôi đặt tám kỷ nguyên thành miễn phí.

Vì vậy, hãy chạy cái này và xem nó có hoạt động không.

Thế đấy, những cảnh báo này sẽ thực sự vang lên

trong TensorFlow 3 vì hiện tại,

họ đang đề cập đến điều gì đó nội bộ

với Caras mà chúng ta không thể làm gì được

Và hãy đợi cho đến khi chúng ta bắt đầu nhìn thấy thanh tiến trình.

Nó đây rồi.

Bây giờ bạn có thể thấy rằng chúng tôi có thanh tiến trình

và mỗi kỷ nguyên sẽ mất khoảng hai phút

và 40 giây hai phút 50 giây.

Vì vậy, bây giờ điều này sẽ đào tạo trong khoảng bảy

phút rưỡi, vậy nên chúng ta sẽ gặp lại nhau khi hết giờ.

Vậy là kỷ nguyên đầu tiên đã xong và nó sẽ còn có thêm hai kỷ nguyên nữa.

Và thế là xong,

và bạn có thể thấy ở phía dưới nó được thực hiện trên máy tính này

tại thời điểm này để phân phối 11 phút.

Bây giờ những dấu hiệu rất quan trọng cần đề cập

Trước hết, bạn có thể thấy rằng đây là một khóa đào tạo tốt

vì sự mất mát giảm dần trên mỗi kỷ nguyên.

Điều này có nghĩa là nó thực sự đã được đào tạo,

lúc đầu là 25, sau đó là 1,5 và bây giờ là 0,77.

Có lẽ nếu chúng ta đào tạo nhiều kỷ nguyên hơn,

nó thực sự sẽ tiếp tục giảm.

Thứ hai, chúng ta có thể thấy rằng việc mất xác nhận

not only went down, but also, it never spiked,

đó là một điều rất quan trọng

như bạn biết vì chúng tôi đang tránh việc điều chỉnh quá mức

Vì vậy đây là một mô hình tốt

rằng bây giờ chúng tôi có thể thực hiện bản dịch của mình.

Và chúng ta làm điều đó như thế nào?

Vâng, tất nhiên là nhắc nhở.

Điều đó có nghĩa là chúng ta sẽ nhận được ID của mình

đối với một bản vá trạng thái nhất định,

sau đó chúng ta sẽ chạy tạo mô hình

và sau đó chúng ta sẽ sử dụng mã thông báo giống như trước.

Và sau đó chúng tôi in bản giải mã đầu vào,

chỉ để cho bạn thấy, một bản giải mã đầu ra,

chỉ để cho bạn xem bản dịch tham khảo, và cuối cùng,

văn bản được dịch theo mô hình.

Vì vậy, hãy chạy cái này, việc này có thể mất một chút thời gian.

Bây giờ chúng ta đã chạy xong, bạn có thể thấy nó mất khoảng ba phút

rưỡi và chúng tôi đã có bản dịch, vì vậy chúng ta hãy xem một số.

Ví dụ như cái đầu tiên,

bạn có thể thấy nó nói, "Chim,

bạn không cần phải lúc nào cũng phải siêu dũng cảm."

"Chim" (nói bằng tiếng Tây Ban Nha)

"Tôi cảm thấy cá tuyết ở đây" (nói bằng tiếng Tây Ban Nha)

Đó không hẳn là bản dịch hoàn hảo,

nhưng nó thực sự rất tốt.

Và điều cuối cùng, bạn có thể tự kiểm tra.

Vì vậy, về tổng thể, chúng ta có thể dịch từ tiếng Anh

sang tiếng Tây Ban Nha với việc học chuyển tiếp trên tập dữ liệu opus-100 này

Xin chúc mừng.