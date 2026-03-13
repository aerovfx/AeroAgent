# 010 Xây dựng thủ công & Vòng lặp vô hạn tự nhiên

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong video này, chúng ta sẽ nói về Vòng lặp vô hạn.

Một vòng lặp vô hạn là một vòng lặp.

Điều đó thực thi khối câu lệnh của nó nhiều lần cho đến khi người dùng buộc chương trình phải thoát.

Khi luồng chương trình đi vào thân vòng lặp, nó không thể thoát ra được.

Thật không may, những lập trình viên mới bắt đầu có thể vô tình tạo ra các vòng lặp vô hạn.

Và những vòng lặp vô hạn này thể hiện các lỗi logic trong chương trình của họ.

Chúng ta có thể tạo ra một vòng lặp vô hạn có chủ ý.

Thông thường, sử dụng mã đơn giản này, mặc dù đúng, nhưng sẽ làm được điều gì đó mãi mãi.

Không thay đổi điều kiện này.

Câu lệnh while.

Vì vậy, trong ví dụ nhỏ này, tuy đúng nhưng hãy làm điều gì đó mãi mãi.

Sự thật luôn luôn là sự thật.

Vì vậy, điều kiện vòng lặp không thể sai.

Cách duy nhất để thoát khỏi vòng lặp là bằng câu lệnh break, câu lệnh return hoặc lệnh gọi thoát hệ thống.

được nhúng ở đâu đó trong phần thân của vòng lặp while.

Chúng ta hãy xem vòng lặp vô hạn này như thế nào.

Cái gì?

Vì vậy, ở đây tôi có một đoạn mã nhỏ.

Tôi bằng một.

Trong khi đúng.

In I.

Nó sẽ.

Tiếp tục in.

Giá trị a mãi mãi.

Hãy để chúng tôi.

Nhìn thấy.

Tôi sẽ tiếp tục in giá trị I.

Vì vậy, ở đây bạn có thể thấy trong cửa sổ giao diện điều khiển, nó vẫn tiếp tục chạy giá trị.

Vì tôi chưa sử dụng bất kỳ câu lệnh break hoặc câu lệnh return nào.

Cách duy nhất để thoát khỏi vòng lặp là.

Làm gián đoạn vòng lặp.

Thực hiện bằng lệnh Ctrl C.

Ctrl c.

Vì vậy, đây không gì khác ngoài việc ngắt bàn phím hoặc ngắt thủ công.

Vì vậy, khi chúng ta sử dụng vòng lặp vô hạn mà không có bất kỳ câu lệnh break, return hay bất kỳ câu lệnh nào khác.

Để chấm dứt vòng lặp.

Tùy chọn duy nhất là sử dụng ngắt thủ công.

Loại vòng lặp vô hạn có chủ ý này rất dễ viết chính xác.

Nhưng các vòng lặp vô hạn ngẫu nhiên khá phổ biến.

Và những vòng lặp vô hạn ngẫu nhiên này có thể gây bối rối cho người mới bắt đầu.

Để chẩn đoán và sửa chữa.

Đây là một ví dụ như vậy.

Điều đó được lập trình để tìm ra các thừa số của số đó.

Chúng ta hãy chọn số lần lặp tối đa là 20 và khởi tạo giá trị n là một.

Trong khi N nhỏ hơn hoặc bằng hệ số đặt tối đa bằng một.

In giá trị của N.

Trong khi hệ số nhỏ hơn hoặc bằng n.

Kiểm tra xem hệ số có phải là hệ số của n hay không bằng cách sử dụng điều kiện if này.

Nếu n.

Hệ số mô đun bằng 0.

In vectơ.

Nếu vậy, hãy in và hiển thị hệ số và mức tăng.

Hệ số nhân tố bằng hệ số cộng một.

Và cuối cùng.

Giá trị n tăng thêm n bằng N cộng một.

Vì vậy, đây là một số lỗi logic.

Điều này làm cho chương trình chạy vô tận.

Hãy để chúng tôi chạy mã này và xem logic là gì.

Nhìn vào đây.

Chương trình chỉ hiển thị.

Ba dòng mã có nghĩa là.

Ba lần.

Và sau đó chương trình đang chạy nhưng không có màn hình.

Ở đây chương trình đang cố gắng tìm kiếm.

Các hệ số từ 1 đến 20 nhưng nó hiển thị 1 thành 1 rồi treo hoặc treo.

Ở đây nó đã bị treo cổ.

Loại hành vi này là một triệu chứng thường xuyên.

Của một vòng lặp vô tình, vô tận.

Vì thế không có ý định.

Nhưng vô tình, nó đã trở thành vòng lặp vô tận.

Ở đây chương trình hiển thị đúng thừa số đầu tiên của 3 rồi treo.

Vì chương trình ngắn.

Chương trình có thể dễ dàng xác định vị trí, vì vậy chúng ta có thể dễ dàng xác định được vấn đề ở đâu.

Trong một số chương trình lớn.

Lỗi có thể khó tìm.

Vì vậy, để tránh các vòng lặp vô hạn.

Có nghĩa là loại vòng lặp vô hạn không chủ ý này.

Chúng ta phải đảm bảo rằng vòng lặp thể hiện một số thuộc tính nhất định.

Thuộc tính đầu tiên là điều kiện vòng lặp không được lặp lại như thế này.

Một biểu thức boolean không bao giờ có thể sai.

Vì vậy, đây là biểu thức boolean phức hợp không bao giờ sai.

Vì vậy, đây không là gì ngoài một tautology.

Và thuộc tính thứ hai là điều kiện của một thời điểm.

Vòng lặp ban đầu phải đúng để có quyền truy cập vào phần thân của nó.

Nếu chúng ta tuân theo mã này.

Điều kiện vòng lặp bên ngoài liên quan đến các biến.

Ian và Max, chúng tôi thấy rằng chúng tôi chỉ định tối đa 22.

Trước vòng lặp và không bao giờ thay đổi nó sau đó.

Vì vậy, để tránh vòng lặp vô hạn, điều cần thiết là n phải được sửa đổi trong vòng lặp.

May mắn thay, câu lệnh cuối cùng trong phần thân của vòng lặp bên ngoài tăng n tức là n bằng n

cộng một.

Trong cái đầu tiên của anh ấy.

Và Max là 20.

Vì vậy, trừ khi có trường hợp phát sinh khiến vòng lặp bên trong trở nên vô hạn.

Đó là vòng lặp while.

Vòng lặp bên trong.

Vòng lặp bên ngoài cuối cùng sẽ chấm dứt điều kiện vòng lặp bên trong liên quan đến các biến n và hệ số.

Không có câu lệnh nào trong vòng lặp bên trong sửa đổi.

N.

Vì vậy, điều bắt buộc là yếu tố đó phải được sửa đổi trong vòng lặp.

Giải pháp cho vấn đề ở đây là hệ số được tăng lên trong phần thân của vòng lặp bên trong.

Không nằm trong vòng lặp.

Sự vội vàng.

Trong câu lệnh if.

Vòng lặp bên trong chứa một câu lệnh không có gì khác ngoài câu lệnh if.

Câu lệnh lần lượt có hai câu lệnh trong phần nội dung của nó.

Nghĩa là, số in và hệ số bằng hệ số cộng một.

Nếu điều kiện của vòng lặp là sai thì hệ số biến đổi sẽ không thay đổi.

Trong tình huống này, nếu yếu tố biểu hiện.

Anh ta nhỏ hơn hoặc bằng n.

Đã đúng.

Và nó sẽ vẫn đúng.

Điều này tạo ra một vòng lặp vô hạn một cách hiệu quả.

Vì vậy điều kiện này ở giá trị thứ hai, câu lệnh sửa đổi hệ số phải được chuyển ra ngoài

cái.

Mỗi tuyên bố.

Và.

Nên ở trong vòng lặp while.

Nhìn vào đây.

Vấn đề nằm ở yếu tố này.

Đó là.

Thực ra.

Được sử dụng trong vòng lặp while thứ hai nằm bên trong câu lệnh if.

Nó phải nằm trong vòng lặp while.

Được rồi.

Chúng ta hãy quay lại.

Hệ số này bằng hệ số cộng một.

Bên trong vòng lặp while.

Vì vậy, bây giờ yếu tố này nằm trong vòng lặp while thứ hai.

Chương trình sẽ hiển thị chính xác các yếu tố.

Từ 1 đến 20.

Vì vậy, đây là một trong những sửa chữa.

Mình đã hướng dẫn bạn cách sửa rồi.

Được rồi.

Vì vậy, chúng ta hãy chạy mã này hoặc mã này, tùy theo cái nào có thể.

Và nhìn vào đây.

Chúng tôi đã có.

Các vectơ từ 1 đến 20 đúng cách.

Chúng ta cũng có thể sử dụng các vòng lặp for thay vì các vòng lặp while lồng nhau để tìm các thừa số.

Và khi chúng ta sử dụng vòng lặp for thay vì vòng lặp while lồng nhau.

Nó trở nên ngắn hơn một chút, nhưng nó tránh được khả năng tăng sai số của hệ số

biến.

Điều này là do.

Câu lệnh mặc định tự động xử lý việc cập nhật biến vòng lặp.

Vì vậy, ở đây chúng ta có thể thấy Max bằng 20 cho N trong phạm vi, một đến max cộng một bằng 1 đến 20.

Ở giữa phạm vi, 1 đến 20 bản in.

Đâu là số nguyên.

Chúng ta đang kiểm tra à?

Hoặc những số nguyên nào chúng ta đang kiểm tra để tìm thừa số trong phạm vi từ một đến n cộng một.

Có nghĩa là bắt đầu từ một.

Và tám lên tới N cộng một.

Nếu n có nghĩa là nếu n hệ số mô đun bằng 0.

Yếu tố in ấn

Và cuối cùng chọn câu lệnh in.

Để hiển thị kết quả độc đáo.

Hãy để chúng tôi chạy mã này và xem kết quả.

Vì vậy, ở đây chúng tôi lại nhận được kết quả tương tự.

Khi chúng tôi đến đây.

Đây.

Không có câu hỏi về việc tăng hệ số.

Bởi vì Guadalupe.

Chúng tôi biết điều đó.

Chúng ta có thể sử dụng đối tượng lặp.

Vì vậy, chúng tôi đang sử dụng các hàm phạm vi.

Cách này hoạt động tương tự như tăng hệ số từ hệ số cộng một.

Và N bằng n cộng một cho thừa số chúng ta đang sử dụng.

Vòng lặp lồng nhau.

Và với n chúng ta đang sử dụng vòng lặp for.

TRONG.

Với vòng lặp for.

Và tính hệ số với vòng lặp for lồng nhau.

Vì vậy, chúng tôi chỉ đang loại bỏ điều này.

Hai câu lệnh chương trình này.

Chúng chẳng là gì ngoài hệ số bằng hệ số cộng một.

Và sau câu lệnh in, n bằng n cộng một với sự trợ giúp của vòng lặp for.

Trong phạm vi.

Muốn tối đa cộng một.

Đối với điều kiện này và đối với điều kiện này hệ số nhỏ hơn hoặc bằng một.

Chúng tôi đang sử dụng hệ số vòng lặp for lồng nhau trong phạm vi từ một đến n cộng một.

Vì chúng ta đang sử dụng nhỏ hơn hoặc bằng n.

Do đó ở đây chúng ta đang sử dụng n cộng một thay vì n.

Max cũng n nhỏ hơn hoặc bằng Max.

Do đó Max cộng một và các mệnh đề khác vẫn giữ nguyên, nghĩa là.

Tuyên bố in và tuyên bố in này.

Hệ số này đã bị loại bỏ và hệ số này bằng n cộng đã được loại bỏ với sự trợ giúp của vòng lặp for.

Bởi vì khi chúng ta sử dụng vòng lặp for, nó sẽ tự động lặp qua giá trị cuối.

Ở đây max và N là giá trị cuối của lần lặp.

Max là.

Giá trị cuối của vòng lặp for đầu tiên và n là giá trị cuối của vòng lặp for.

Thứ hai.

Hoặc vòng lặp for lồng nhau.

Vì vậy, đây là cách chúng ta có thể tạo và tránh các vòng lặp vô hạn một cách thủ công.

Tạo các vòng lặp vô hạn với sự trợ giúp của một số thuộc tính nhất định.

Có nghĩa.

Chúng ta nên làm vậy.

Kiểm tra tautology và tình trạng của một thời gian.

Ban đầu phải đúng để có quyền truy cập vào cơ thể của nó.

Đây là hai thuộc tính chúng ta cần.

Jake trước khi sáng tạo.

Các vòng lặp sử dụng vòng lặp while.

Vì vậy cảm ơn vì đã xem bài học này.

Hẹn gặp lại các bạn trong bài học tiếp theo.