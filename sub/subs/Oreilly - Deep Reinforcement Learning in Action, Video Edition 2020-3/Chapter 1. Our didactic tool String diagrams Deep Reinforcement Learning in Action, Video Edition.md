# Chương 1. Công cụ giáo khoa của chúng tôi Sơ đồ chuỗi Học tập củng cố sâu trong thực tế, Phiên bản video

---

1.7 Công cụ giáo khoa của chúng tôi - Sơ đồ chuỗi

Các khái niệm cơ bản của RL đã được thiết lập tốt trong nhiều thập kỷ,

nhưng lĩnh vực này đang phát triển rất nhanh, nên bất kỳ kết quả mới cụ thể nào cũng có thể sớm bị lỗi thời.

Đó là lý do tại sao cuốn sách này tập trung vào việc giảng dạy các kỹ năng chứ không phải những chi tiết có thời gian bán hủy ngắn ngủi. Chúng tôi bao gồm

một số tiến bộ gần đây trong lĩnh vực này chắc chắn sẽ được thay thế trong tương lai không xa,

nhưng chúng tôi làm như vậy chỉ để xây dựng các kỹ năng mới chứ không phải vì chủ đề cụ thể mà chúng tôi đang đề cập

nhất thiết phải là một kỹ thuật được thử nghiệm theo thời gian. Chúng tôi tự tin rằng ngay cả khi một số ví dụ của chúng tôi

trở nên lỗi thời, những kỹ năng bạn học sẽ không còn nữa và bạn sẽ sẵn sàng giải quyết các vấn đề về RL

trong một thời gian dài sắp tới. Hơn nữa, RL là một lĩnh vực rộng lớn có rất nhiều điều để học hỏi. Chúng ta không thể hy vọng

để trình bày tất cả những điều đó trong cuốn sách này. Thay vì là một tài liệu tham khảo RL đầy đủ hoặc một khóa học toàn diện,

Mục tiêu của chúng tôi là dạy cho bạn những nền tảng của RL và lấy mẫu một số điều thú vị nhất

những phát triển gần đây trong lĩnh vực này. Chúng tôi hy vọng rằng bạn sẽ có thể tiếp thu những gì bạn đã học ở đây

và dễ dàng bắt kịp tốc độ trong nhiều lĩnh vực khác của RL. Ngoài ra, chúng tôi có một phần trong Chương 11 rằng

cung cấp cho bạn lộ trình về các lĩnh vực mà bạn có thể muốn khám phá sau khi đọc xong cuốn sách này.

Cuốn sách này tập trung vào việc giảng dạy tốt nhưng cũng rất nghiêm ngặt. Học tăng cường và học sâu

việc học về cơ bản đều là toán học. Nếu bạn đọc bất kỳ bài báo nghiên cứu cơ bản nào trong

những trường này, bạn sẽ gặp phải những ký hiệu và phương trình toán học có thể lạ lẫm.

Toán học cho phép chúng ta đưa ra những tuyên bố chính xác về điều gì là đúng và mọi thứ có liên quan như thế nào,

và nó đưa ra những lời giải thích chặt chẽ về cách thức và lý do mọi thứ hoạt động. Chúng tôi có thể dạy RL mà không cần bất kỳ

toán và chỉ sử dụng Python, nhưng cách tiếp cận đó sẽ cản trở bạn trong việc hiểu những tiến bộ trong tương lai.

Vì vậy, chúng tôi nghĩ toán học rất quan trọng, nhưng như biên tập viên của chúng tôi đã lưu ý, có một câu nói phổ biến trong

thế giới xuất bản, "Đối với mỗi phương trình trong cuốn sách, lượng độc giả giảm đi một nửa", điều này có lẽ có một số

sự thật với nó. Có một chi phí nhận thức không thể tránh khỏi trong việc giải mã các phương trình toán học phức tạp,

trừ khi bạn là một nhà toán học chuyên nghiệp đọc và viết toán cả ngày.

Đối mặt với việc muốn trình bày một cách nghiêm ngặt về DRL để mang đến cho độc giả một đánh giá cao nhất

hiểu biết nhưng vẫn muốn tiếp cận càng nhiều người càng tốt, chúng tôi đã nghĩ ra những gì chúng tôi nghĩ

là một đặc điểm rất khác biệt của cuốn sách này. Hóa ra, ngay cả những nhà toán học chuyên nghiệp

đang trở nên mệt mỏi với các ký hiệu toán học truyền thống, với vô số ký hiệu và trong một phạm vi

nhánh cụ thể của toán học nâng cao được gọi là lý thuyết phạm trù, các nhà toán học đã phát triển một

ngôn ngữ đồ họa thuần túy được gọi là "sơ đồ chuỗi". Sơ đồ chuỗi trông rất giống với sơ đồ

và sơ đồ mạch điện, chúng có ý nghĩa khá trực quan nhưng cũng rất chặt chẽ

và chính xác như các ký hiệu toán học truyền thống, phần lớn dựa trên các ký hiệu Hy Lạp và Latinh.

Hình 1.14 cho thấy một ví dụ đơn giản về một loại sơ đồ chuỗi mô tả, ở mức độ cao,

một mạng lưới thần kinh với hai lớp. Học máy, đặc biệt là học sâu, liên quan đến rất nhiều

của các phép toán ma trận và vectơ và sơ đồ chuỗi đặc biệt phù hợp để mô tả các phép toán này

các loại hoạt động đồ họa. Sơ đồ chuỗi cũng rất hữu ích để mô tả các quy trình phức tạp,

bởi vì chúng ta có thể mô tả quá trình ở nhiều mức độ trừu tượng khác nhau.

Bảng trên cùng của Hình 1.14 hiển thị hai hình chữ nhật biểu thị hai lớp của mạng lưới thần kinh,

nhưng sau đó chúng ta có thể phóng to, nhìn vào bên trong hộp, trên Lớp 1 để xem nó làm gì chi tiết hơn,

được thể hiện ở bảng dưới cùng của Hình 1.14.

Hình 1.14, sơ đồ chuỗi cho mạng nơ-ron hai lớp. Đọc từ trái sang phải,

sơ đồ chuỗi trên cùng biểu thị một mạng lưới thần kinh chấp nhận vectơ đầu vào có kích thước n,

nhân nó với một ma trận có kích thước n lần m, trả về một vectơ có kích thước m. Sau đó

hàm kích hoạt sigmoid phi tuyến được áp dụng cho từng phần tử trong vectơ m chiều.

Sau đó, vectơ mới này được cung cấp thông qua trình tự các bước tương tự ở Lớp 2,

tạo ra đầu ra cuối cùng của mạng lưới thần kinh, là một vectơ k chiều.

Chúng ta sẽ thường xuyên sử dụng sơ đồ dây xuyên suốt cuốn sách để truyền đạt mọi thứ từ phức tạp

phương trình toán học cho kiến trúc của mạng lưới thần kinh sâu. Chúng tôi sẽ mô tả điều này

cú pháp đồ họa trong chương tiếp theo và chúng tôi sẽ tiếp tục tinh chỉnh và xây dựng nó trong suốt chương này.

phần còn lại của cuốn sách. Trong một số trường hợp, ký hiệu đồ họa này là quá mức cần thiết đối với những gì chúng tôi đang cố gắng thực hiện

giải thích, vì vậy chúng tôi sẽ sử dụng kết hợp văn xuôi rõ ràng và Python hoặc mã giả. Chúng tôi cũng sẽ

bao gồm ký hiệu toán học truyền thống trong hầu hết các trường hợp, vì vậy bạn sẽ có thể tìm hiểu cơ bản

các khái niệm toán học theo cách này hay cách khác, cho dù là sơ đồ, mã hay ký hiệu toán học thông thường

hầu hết đều kết nối với bạn.