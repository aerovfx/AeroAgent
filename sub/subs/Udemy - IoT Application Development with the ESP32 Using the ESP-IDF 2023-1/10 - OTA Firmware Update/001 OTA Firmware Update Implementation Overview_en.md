# 001 Tổng quan triển khai cập nhật chương trình cơ sở OTA vi

---

Trong phần này, chúng ta sẽ xem xét quá trình triển khai cập nhật chương trình cơ sở.

Bản cập nhật chương trình cơ sở này sẽ được triển khai qua mạng cục bộ không dây và chúng tôi chỉ cần tải lên

tệp nhị phân tới ISP bằng trang web.

Vì vậy, trước khi đi sâu hơn vào chi tiết, hãy nói về các bản cập nhật OTA nói chung bằng cách sử dụng IDF, vì vậy OTA

cập nhật cho phép thiết bị tự cập nhật dựa trên dữ liệu nhận được.

Ví dụ: qua Wi-Fi, trong khi chương trình cơ sở bình thường đang chạy và việc bật cập nhật chương trình cơ sở yêu cầu

định cấu hình bảng phân vùng có ít nhất hai khe ứng dụng được gọi là OTA zero và Otere một, như

cũng như phân vùng dữ liệu OTA và các chức năng vận hành OTA.

Viết hình ảnh chương trình cơ sở ứng dụng mới vào bất kỳ khe ứng dụng OTA nào hiện chưa được chọn cho

khởi động.

Vì vậy, khi hình ảnh được xác minh, phân vùng dữ liệu OTA sẽ được cập nhật để chỉ định rằng hình ảnh này sẽ

được sử dụng cho lần khởi động tiếp theo.

Và xa hơn nữa là bảng phân vùng, đèn flash của phương Đông có thể chứa nhiều ứng dụng ở nhiều dạng khác nhau

các loại dữ liệu.

Ví dụ: dữ liệu hiệu chuẩn, hệ thống tệp, lưu trữ tham số, v.v.

Và với mục đích này, một bảng phân vùng được flash thành tám nghìn hex trong bộ nhớ flash và mỗi mục nhập

của bảng phân vùng có nhãn, loại con và phần bù trong flash, trong đó phân vùng

được tải.

Ngoài ra, cách đơn giản nhất để sử dụng bảng phân vùng là mở cấu hình dự án hoặc cấu hình SDK

và nhật thực và chọn nhà máy lên tới 0,8 định nghĩa.

Như chúng ta đã thực hiện ở phần cấu hình dự án.

Và đây là bảng phân vùng trông như thế nào.

Ở đây chúng tôi có tên, loại, loại phụ, sự xáo trộn và kích cỡ.

Và trong bảng này, giống với bảng chúng tôi hiện đang sử dụng, chúng tôi có ba ứng dụng.

Chúng tôi có ứng dụng xuất xưởng tại Offset X mười nghìn và hai ứng dụng hoặc ứng dụng tiếp theo có

0 và 0,1 một kiểu con.

Và còn có một khe dữ liệu OTA mới, chứa dữ liệu cho các bản cập nhật OTA.

Bộ nạp khởi động sẽ kiểm tra khe dữ liệu OTA này để biết ứng dụng nào sẽ thực thi.

Vì vậy, nếu nó trống, ứng dụng xuất xưởng sẽ được thực thi.

Ngoài ra, bạn có thể tùy chỉnh bảng phân vùng cho phù hợp với nhu cầu của mình.

Ví dụ: nếu ứng dụng của bạn chiếm nhiều dung lượng hơn, bạn có thể điều chỉnh kích thước và xóa nhà máy

ứng dụng và chỉ sử dụng phân vùng 0 và OTA nếu bạn cần.

OK, bây giờ hãy nói về việc thực hiện của chúng tôi.

Người dùng có thể bắt đầu cập nhật OTA bằng cách tải tệp nhị phân của ứng dụng lên trang web và chương trình cơ sở

sau đó việc cập nhật được thực hiện ở phía máy chủ web và trang web sẽ hiển thị trạng thái, cho dù đó là

đã thành công hay chưa.

Và sau khi cập nhật hoàn tất, trang web sẽ không còn khả dụng nữa và SB 32 sẽ khởi động lại.

Và sau đó chúng tôi có thể kiểm tra bản cập nhật chương trình cơ sở bằng cách chỉ thực hiện một vài thay đổi đơn giản, như thay đổi

bên cạnh Điểm truy cập SB 32S và có thể là nền trang web chỉ để xác minh rằng chương trình cơ sở mới

thực sự là đang chạy.

Vì vậy, bây giờ hãy thảo luận về cách chúng ta có thể thực hiện điều này bằng cách sử dụng ESP IDF.

Tôi khuyên bạn nên duyệt qua tài liệu ấn tượng để hiểu rõ hơn về các chủ đề cập nhật OTA mà bạn

cũng như tài liệu tham khảo API, hãy xem tổng quan về quy trình và các tính năng khác có sẵn sẽ

không được sử dụng trong ví dụ của chúng tôi.

Bạn cũng có thể tìm thêm chi tiết về bảng phân vùng tại đây.

Hãy xem tổng quan, cũng như các chi tiết khác như tạo bảng phân vùng.

Nếu bạn quan tâm.

Vì vậy, các bước phía máy chủ Web sẽ phải thực hiện bắt đầu bằng việc nhận tệp từ web

trang và chúng tôi sẽ gọi các yêu cầu HTTP nhận được cho việc này.

Vì vậy API này sẽ đọc nội dung HTTP.

Dữ liệu từ yêu cầu HTTP vào bộ đệm được cung cấp sau đó sẽ phải thực hiện nhiều cuộc gọi đến chức năng này

mỗi lần tìm nạp độ dài bộ đệm một số byte, trong khi con trỏ tới dữ liệu nội dung được tăng lên

nội bộ bởi cùng một số.

Sau đó, chúng ta sẽ phải xác định nội dung tệp nhị phân thực sự bắt đầu từ đâu bằng cách kiểm tra các ký tự thoát.

Các gợi ý về dấu gạch chéo hiện diện khi nhận tệp từ trang web và sau đó gọi SPRO

để bắt đầu chức năng bắt đầu thể thao điện tử, hãy bắt đầu cập nhật bằng cách ghi vào phân vùng đã chỉ định.

Và sau khi thành công, nó sẽ phân bổ bộ nhớ vẫn được sử dụng cho đến khi hàm kết thúc SPL được gọi.

Vì vậy, tiếp theo, chúng tôi yêu cầu Esposti có quyền viết đoạn dữ liệu đầu tiên mà chúng tôi nhận được từ trang web.

Hàm ghi ghi dữ liệu vào phân vùng đã chỉ định và có thể được gọi nhiều lần dưới dạng dữ liệu

được nhận trong quá trình hoạt động.

Điều này đưa chúng ta đến điểm tiếp theo, chúng ta sẽ tiếp tục nhận phần còn lại của tệp bằng cách gọi Yêu cầu HTTP

Nhận và Esposti viết cho đến khi nhận đủ nội dung.

Sau đó, chúng tôi sẽ hoàn tất cập nhật OTA và xác thực hình ảnh ứng dụng bằng cách gọi Esposti End.

Vì vậy, ở đây đề cập rằng phần xử lý liên quan đến bản cập nhật OTA không còn hợp lệ và

bộ nhớ liên kết với nó sẽ được giải phóng bất kể kết quả như thế nào.

Và tiếp theo, chúng ta sẽ cần định cấu hình dữ liệu từ bảng phân vùng cho phân vùng khởi động mới bằng cách gọi

mỗi vị trí để thiết lập phân vùng khởi động.

Và ở đây có đề cập rằng sau lệnh gọi này, khởi động lại ECP sẽ khởi động ứng dụng mới được cấu hình

phân vùng, đưa chúng ta đến chức năng tiếp theo Khởi động lại ESP.

Chức năng này sẽ khởi động lại cả hai CPU.

Cả CPU Pro và CPU ứng dụng sẽ được khởi động lại và tất nhiên chức năng này sẽ không hoạt động trở lại.

Được rồi, hãy thực hiện kế hoạch này và tôi sẽ gặp bạn trong phần lập trình.