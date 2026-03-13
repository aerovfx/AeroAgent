# 05 - Sử dụng KerasTuner để điều chỉnh siêu tham số

---

- [Người] Trong video này, bạn sẽ tìm hiểu

cách sử dụng Keras Tuner

để thực hiện tìm kiếm các siêu tham số tối ưu

của mô hình học sâu.

Tôi sẽ viết mã vào tệp "04_05e".

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp "04_05b".

Lưu ý rằng video này là video thứ hai trong chuỗi hai video

nó dạy bạn cách điều chỉnh các siêu tham số

của mô hình học sâu.

Nếu bạn chưa làm như vậy, hãy xem video khóa học trước

về cách xác định mô hình học sâu có thể điều chỉnh

để được giải thích chi tiết về mã trước đó.

Ngoài ra, hãy đảm bảo chạy mã thông thường trước đó

để tăng tốc môi trường của bạn.

Tôi đã làm như vậy rồi.

Vì vậy, sau khi xác định mô hình có thể điều chỉnh siêu tham số của chúng tôi,

bây giờ chúng ta cần thiết lập một bộ chỉnh tần.

Ở đây, chúng tôi chọn Hyperband, một cách tiếp cận tiết kiệm tài nguyên

để điều chỉnh siêu tham số dựa trên tìm kiếm ngẫu nhiên

và kết hợp nó với nguyên tắc dừng sớm.

Mục tiêu chính của nó là giảm

chi phí tính toán của việc điều chỉnh siêu tham số

bằng cách phân bổ động nhiều tài nguyên hơn

đến các cấu hình siêu tham số đầy hứa hẹn

và ít nguồn lực hơn cho những nguồn lực kém hứa hẹn hơn.

Vì vậy, chúng tôi bắt đầu bằng cách nhập Karas Tuner và chúng tôi gọi nó là "kt,"

và chúng ta sẽ gọi hàm Hyperband

từ Keras Tuner.

Vì vậy, ở đây, chúng tôi chỉ định mô hình làm đối số đầu tiên,

và mô hình là chức năng, mô hình có thể điều chỉnh được

mà chúng tôi đã xác định trong video trước,

nên mỗi lần quá trình diễn ra,

nó sẽ gọi hàm đó để xác định một mô hình mới,

vì vậy chúng ta sẽ chỉ định "max_epochs" là năm,

điều đó có nghĩa rằng đây là số kỷ nguyên

nó sẽ thử xem liệu nó có thể cải thiện hiệu suất hay không,

và với mỗi kỷ nguyên, nó sẽ thực hiện một lần lặp,

và sau đó chúng ta sẽ gieo hạt giống

để bạn và tôi có thể nhận được kết quả như nhau nếu chúng ta...

Khi chúng tôi chạy những thứ này...

Quá trình này diễn ra vào những thời điểm khác nhau trên các máy tính khác nhau.

Chúng ta sẽ đặt "ghi đè" thành "Đúng"

điều đó có nghĩa là nó sẽ ghi đè lên nhật ký

của nỗ lực điều chỉnh siêu tham số trước đó,

"mục tiêu" của chúng tôi là tối đa hóa độ chính xác xác thực,

chúng ta sẽ chỉ định trực tiếp cho "tuning_logs,"

mà nó theo dõi quá trình,

và chúng ta sẽ đặt tên cho dự án,

vậy chúng ta hãy tiếp tục và chạy cái này.

Điều đó khởi tạo bộ chỉnh của chúng tôi.

Bây giờ chúng ta có thể bắt đầu quá trình tìm kiếm với...

Sử dụng phương pháp "tuner.search".

Lệnh này sẽ xây dựng và huấn luyện nhiều mô hình

bằng cách sử dụng các kết hợp siêu tham số khác nhau, được chứ?

Và như chúng tôi đã xác định trong mô hình có thể điều chỉnh của mình,

chúng tôi sẽ thử các kích cỡ lớp khác nhau,

tỷ lệ bỏ học khác nhau, tỷ lệ học tập khác nhau,

và chúng tôi cũng sẽ thử các kích cỡ lô khác nhau,

mà chúng tôi chỉ định trong đoạn mã tiếp theo này.

Vì vậy, ở đây chúng tôi chỉ định "tuner.search,"

và trong "tuner.search", chúng tôi chỉ định

dữ liệu huấn luyện, nhãn huấn luyện,

và chúng tôi nói với mỗi quá trình tìm kiếm này,

chúng tôi muốn thực hiện năm kỷ nguyên,

chúng tôi muốn thực hiện phân chia xác thực là 0,1,

và sau đó, chúng tôi muốn chỉ định các kích cỡ lô khác nhau

mà chúng tôi muốn đánh giá,

vì vậy ở đây, chúng tôi chỉ định kích thước lô làm nhãn

đối với loại giá trị tham số này

mà chúng ta sắp xem xét,

nhưng điều chúng tôi đang nói ở đây

là tôi muốn thử kích cỡ lô từ 32 đến 128,

với bước 32, điều này có nghĩa là

mà chúng tôi muốn thử trong mỗi 32,

32, rồi 64, rồi tới 128,

vì vậy đó chính là điều chúng tôi muốn thử ở đây

để xem kích thước lô nào

thực sự mang lại cho chúng tôi hiệu suất tốt nhất,

vì vậy chúng ta sẽ tiếp tục và khởi động bộ điều chỉnh của mình,

và như vậy, quá trình bắt đầu.

Vì vậy chúng ta sẽ để chuyện này trôi qua,

và vì thế, chúng ta thấy rằng nó đang diễn ra

quá trình điều chỉnh siêu tham số,

cố gắng tìm sự kết hợp tốt nhất của siêu tham số

cho vấn đề của chúng ta, vì vậy chúng ta sẽ tiếp tục quan sát điều này

để xem chúng ta đang ở đâu trong quá trình này.

Được rồi, chuyện này sẽ tiếp tục.

(không có âm thanh)

Được rồi.

Vậy là quá trình đã hoàn tất,

và vì thế, chúng tôi đã trải qua 10 thử nghiệm khác nhau,

vì vậy khi tìm kiếm hoàn tất, chúng tôi có thể xuất ra

cấu hình siêu tham số tốt nhất phải không?

Vậy chúng tôi mất khoảng 3 phút 13 giây

để tìm kiếm trong không gian siêu tham số

để tìm ra bộ siêu tham số tối ưu cho vấn đề của chúng ta.

Vậy là bây giờ việc tìm kiếm đã hoàn tất,

chúng ta có thể xuất ra bộ siêu tham số tốt nhất,

nên chúng ta có thể chạy cái này ở đây, và bây giờ đây là những gì chúng ta có được,

“Số lượng đơn vị tối ưu

ở lớp kết nối dày đặc thứ nhất và thứ hai là 416,"

đối với lớp ẩn đầu tiên, "Với tỷ lệ bỏ học là 0,40,"

và 64 cho lớp ẩn thứ hai,

"Với tỷ lệ bỏ học là 0,20" được không?

"Tỷ lệ học tập tối ưu cho trình tối ưu hóa là 0,001,

và quy mô lô đào tạo tối ưu là 96," được chứ?

Vì vậy chúng tôi sử dụng phương pháp Hyperband

để có thể xác định các siêu tham số tối ưu này.

Tiếp theo, bằng cách sử dụng các siêu tham số tối ưu này,

chúng ta sẽ tạo một mô hình được điều chỉnh, vì vậy đây là một mô hình

nó sẽ sử dụng những siêu tham số đó,

chúng ta sẽ xác định mô hình của mình dựa trên những giá trị đó,

vì vậy chúng tôi tiếp tục và tạo ra mô hình của mình,

và cuối cùng, chúng tôi đào tạo mô hình đã điều chỉnh.

(không có âm thanh)

Vậy bây giờ chúng ta sẽ sử dụng...

Cái gì, vậy là 10 kỷ nguyên à?

Vì vậy chúng ta sẽ đợi nó kết thúc,

vì vậy chúng tôi sẽ sử dụng kích thước lô tối ưu

và mô hình, rõ ràng,

được xác định với các giá trị tối ưu

cho các siêu tham số khác.

Được rồi, và bây giờ, chúng ta cũng có thể đánh giá

mô hình được điều chỉnh khái quát hóa dữ liệu mới tốt như thế nào,

vì vậy hãy xem nó hoạt động như thế nào,

và vì vậy, ở đây, chúng ta thấy rằng độ mất kiểm tra là 0,0649,

và độ chính xác của bài kiểm tra là 0,9183, phải không?

Vậy điều này tốt hơn những gì chúng ta đã có trước đây như thế nào?

Vì vậy hãy cuộn lên một chút

để xem mô hình cơ sở là gì...

Nó hoạt động như thế nào, cho đến tận đây,

chúng ta thấy hiệu suất trên...

Của mô hình cơ sở, vì vậy chúng ta có thể thấy

rằng độ chính xác kiểm tra của mô hình cơ sở là 96%,

và mô hình của chúng tôi rõ ràng đã được cải thiện dựa trên điều đó một chút

đến 98% phải không?

Vì vậy, những gì chúng tôi đã làm ở đây là tìm kiếm siêu tham số rất cơ bản.

Chúng ta có thể làm điều gì đó sâu rộng hơn nhiều

hơn những gì chúng tôi đã làm ở đây,

nhưng chỉ một phần nhỏ mà chúng tôi đã làm ở đây

đã có thể cải thiện hiệu suất của mô hình của chúng tôi, vì vậy...

Nếu bạn đã theo dõi giữa video này

và cái trước đó, có nghĩa là bây giờ bạn đã biết

cách điều chỉnh siêu tham số

về mô hình học sâu bằng Python sử dụng Keras Tuner.

Làm tốt lắm.