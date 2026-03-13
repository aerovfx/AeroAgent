# 59 - Keras Project Solutions Tạo và đào tạo Model English

---

Chào mừng mọi người quay trở lại, trong bài giảng này, chúng ta sẽ đi sâu vào việc tạo và đào tạo mô hình cho

dự án của chúng tôi.

Hãy đi đến sổ ghi chép và bắt đầu.

Được rồi, ở đây tôi đang tạo phần mô hình cho sổ ghi chép bài tập của chúng ta.

Chúng tôi sẽ tiếp tục và chạy ô để chạy các lệnh nhập cần thiết, cụ thể là tuần tự và dày đặc và

tùy chọn bạn có thể thêm vào các lớp Drop-Out.

Vì vậy, chúng tôi đã xem lại bài giảng phân loại của phần khóa học.

Vì vậy, ở đây bạn có rất nhiều sự linh hoạt về số lượng lớp và nơ-ron mà bạn muốn.

Chúng ta sẽ làm theo một cách tiếp cận khá đơn giản ở đây nếu chúng ta nhìn vào hình dạng của X Train, nó sẽ

bắt đầu với 78 tính năng.

Vì vậy, những gì tôi sẽ làm là tạo lớp đầu tiên phù hợp mà chúng ta sẽ gọi là mô hình phần thêm đậm đặc.

Và một nguyên tắc chung khá hay là lớp đầu tiên của bạn có thể phải có cùng một số

các tính năng chỉ dành cho mạng nơ ron nhân tạo thông thường và sau đó là hàm kích hoạt.

Chúng ta sẽ chọn đơn vị linnear được chỉnh lưu.

Và sau đó để cố gắng ngăn chặn việc trang bị quá mức, chúng tôi sẽ tiếp tục và thêm một phần bỏ học sau đó và đây là

thứ gì đó bạn có thể thử tùy theo tỷ lệ bỏ học.

Nhưng tôi sẽ tiếp tục và chỉ làm 20 phần trăm ở đây và sau đó tôi sẽ sao chép cái này và thêm vào một vài cái nữa

các lớp ẩn.

Nhưng điều tôi sắp làm là về cơ bản tôi sẽ giảm số lượng tế bào thần kinh, khoảng một nửa cho mỗi tế bào thần kinh.

lớp, vì vậy chúng ta sẽ đi từ 78 đến 39 và sau đó từ 39 đến 19 và chúng ta sẽ có

bỏ học trên mỗi lớp đó.

Và đây là các lớp mà bạn cần đối sánh để thu hồi lớp đầu ra.

Chúng tôi thực sự chỉ đang thực hiện phân loại nhị phân, có nghĩa là chúng tôi phải có một nơron ở ngay đầu

cuối cùng, do đó, một nơ-ron dày đặc nên đơn vị bằng một và nó phải sử dụng hàm kích hoạt sigmoid.

Vì vậy, hãy nhớ lại, hàm kích hoạt sigmoid đẩy các giá trị nằm trong khoảng từ 0 đến một.

Và tiếp theo, chúng ta sẽ biên dịch mô hình và đây cũng là nơi bạn cần so khớp

lên.

Vì vậy, bởi vì chúng tôi đang thực hiện phân loại nhị phân, tổn thất sẽ là entropy chéo gạch dưới nhị phân.

Sau đó, chúng ta sẽ tiếp tục chọn trình tối ưu hóa và tôi sẽ chọn Adam từ Trình tối ưu hóa.

Hãy tiếp tục và chạy ô đó và đảm bảo nó biên dịch.

Và điều tiếp theo là chúng ta cần điều chỉnh mô hình ở đây.

Bạn có rất nhiều lựa chọn.

Và nếu muốn, bạn cũng có thể thêm vào những thứ như dừng sớm.

Nhưng tôi sẽ tiếp tục và chỉ điều chỉnh mô hình cho 25 kỷ nguyên.

Vì vậy, trước tiên chúng ta sẽ xem dữ liệu huấn luyện của mình, chẳng hạn như tàu X và tàu Y.

Và bây giờ chúng ta sẽ nói các kỷ nguyên bằng 25, vì đây là tập dữ liệu lớn hơn nhiều, có lẽ là

một ý tưởng hay là cho ăn món này theo đợt.

Vì vậy, theo đề xuất của nhiệm vụ, chúng ta sẽ nói kích thước lô bằng 256.

Và cuối cùng, chúng tôi cũng muốn chuyển dữ liệu xác thực của mình để có thể vạch ra những tổn thất và xem

nếu chúng ta trang bị quá mức ở bất cứ đâu.

Vì vậy, chúng tôi sẽ vượt qua bài kiểm tra X và chúng tôi kiểm tra trong cuộc gọi phù hợp thực tế.

Vì vậy, nếu chúng ta tiếp tục chạy cái này, hãy để tôi xóa phần chạy cũ và để tôi chạy cái này, đảm bảo rằng chúng ta

không gặp bất kỳ lỗi nào và chúng ta bắt đầu.

Vì vậy, về cơ bản tôi sẽ kết thúc nó ở đây.

Và trong bài giảng tiếp theo chúng ta sẽ làm là sau khi đào tạo xong, chúng ta sẽ chuyển sang

để đánh giá hiệu quả của mô hình.

Và xin nhắc lại, nếu bạn đang sử dụng máy tính chậm hơn hoặc đang chạy ứng dụng này trên Google Cloud, bạn luôn có thể chọn

ít kỷ nguyên hơn, chọn kích thước lô lớn hơn hoặc chỉ loại bỏ kích thước lô.

Tuy nhiên, đây là đủ mẫu mà bạn thực sự nên cho ăn thành từng đợt.

Và điều khác bạn có thể làm là nếu việc đào tạo này mất quá nhiều thời gian như đã đề cập trước đó, bạn có thể

thực ra trước khi bình thường hóa và trước khi thực hiện phân chia treinta, chỉ cần sử dụng D.F. Mẫu để lấy một phần mẫu

của toàn bộ tập dữ liệu.

Vì bạn đang xử lý một tập dữ liệu khá lớn.

OK, vì vậy đây hiện đang là đào tạo.

Tôi sẽ gặp bạn trong bài giảng tiếp theo nơi chúng ta bắt đầu đánh giá hiệu quả hoạt động của mô hình này.