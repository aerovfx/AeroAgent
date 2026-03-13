# 01 cài đặt-Django

---

Xin chào, chào mừng trở lại. Trong chương ngắn này, chúng ta sẽ tìm hiểu cách cài đặt Django bằng cách sử dụng

Mã Visual Studio. Vậy là chúng ta có terminal bên trong Visual Studio Code, phải không? Vì vậy, bạn

thực sự không cần phải ra khỏi thiết bị đầu cuối nếu bạn muốn sử dụng bất kỳ dấu nhắc lệnh nào

hoặc bất kỳ trình thông dịch dòng lệnh nào. Tuy nhiên, nếu bạn muốn sử dụng dấu nhắc dòng lệnh,

dấu nhắc lệnh đi kèm với Windows chứ không phải PowerShell thì rõ ràng bạn sẽ

phải bước ra khỏi Visual Studio Code và khởi chạy dấu nhắc lệnh riêng. Tuy nhiên,

nếu bạn không muốn thoát khỏi môi trường đó của Visual Studio Code, bạn có thể ở lại

ở đó và bạn có thể cài đặt Django, bạn có thể làm rất nhiều việc mà không cần rời khỏi

môi trường Visual Studio. Vậy trước tiên hãy hiểu Django là gì phải không? Vì vậy, nếu bạn là người mới

đối với Django, thì Django là một framework mới, đó là một framework cấp cao được xây dựng bằng Python

được thiết kế để phát triển web an toàn và có thể mở rộng. Nó được thiết kế để đảm bảo an toàn và

phát triển web có thể mở rộng và có sự hỗ trợ phong phú cho các mẫu trang cũng như làm việc với dữ liệu và

một loạt những thứ khác. Vì vậy, trước tiên hãy xem cách cài đặt Django và sau đó

chúng ta sẽ tạo một ứng dụng rất đơn giản và thử nghiệm nó. Trên thực tế, chúng tôi sẽ sử dụng cùng một mã

chúng ta đã tìm ra hướng dẫn về một số trong chương trước. Chúng tôi sẽ sử dụng chính xác

cùng một mã và trong trang web hoặc máy chủ mà chúng tôi tạo bằng Django, chúng tôi sẽ có

trang in ra giai thừa của bất kỳ số nào bạn nhập vào hàm đó. Vì vậy, hãy

quay lại Visual Studio Code ngay bây giờ. Được rồi, vậy là chúng ta đã quay lại Visual Studio Code. Bây giờ,

trước khi thực sự cài đặt Django, chúng tôi sẽ sử dụng thứ gọi là môi trường ảo

và chúng ta sẽ tạo một môi trường ảo rồi cài đặt Django bên trong môi trường ảo đó

môi trường. Vì vậy, sử dụng môi trường ảo sẽ tránh cài đặt Django vào Python toàn cầu

môi trường trong hệ thống của bạn và nó cho phép bạn kiểm soát chính xác các thư viện mà bạn

có thể sử dụng trong ứng dụng của bạn. Nó cũng giúp dễ dàng tổ chức các dự án khác nhau dựa trên

trên các môi trường ảo khác nhau. Vì vậy, trước tiên hãy xem nó được thực hiện như thế nào. So, what I'm going

việc cần làm ở đây là tôi sẽ sử dụng con đường cụ thể này. Mặc dù tôi đã nói rằng chúng ta có thể làm được

mọi thứ bên trong môi trường Visual Studio Code của chúng ta, vấn đề là bạn có thể sử dụng PowerShell nếu bạn

muốn. Bạn có thể làm mọi thứ bên trong thiết bị đầu cuối này nếu muốn. Tuy nhiên, vấn đề là nếu bạn

đang tạo môi trường ảo thì sẽ luôn có tên của môi trường ảo

mà bạn đang làm việc sẽ nằm cạnh đường dẫn trong ngoặc đơn. Nhưng trong PowerShell,

bạn không thể thấy điều đó. Vì vậy, nó không quan trọng. Tuy nhiên, môi trường được tạo ra.

Điều đó hoạt động hoàn hảo, nhưng bạn sẽ không biết mình đang làm việc trong môi trường nào nếu bạn

đang xem xét nó trong dấu nhắc lệnh. Vì vậy, đó là lý do duy nhất khiến chúng ta bước

hiện đã hết PowerShell và chúng tôi sẽ mở dấu nhắc lệnh cho việc đó. Vì vậy, chỉ để cài đặt

Django và chỉ để cài đặt môi trường ảo, chúng tôi sẽ thử nó. Vì vậy, hãy

quay lại đây và sao chép đường dẫn này. Dù bạn chọn đường dẫn nào, chỉ cần sao chép đường dẫn đó và

hãy mở dấu nhắc lệnh. Được rồi, hãy tối đa hóa nó và chúng ta sẽ chỉ nói CD và dán

nó ở đây. Bây giờ, nó sẽ không hoạt động. Vì vậy, nếu tôi nói D lái xe và bạn sẽ đi. Vì vậy, đó

sẽ đưa chúng ta trở lại bên trong đó và bây giờ hãy tạo một thư mục mới và chúng ta sẽ gọi nó là

Thử nghiệm Django hoặc các dự án Django. Tại sao không tạo thư mục cho các dự án Django và sau đó chúng ta sẽ chỉ

nói dir và bạn có các dự án Django. Vì vậy, hãy vào thư mục cụ thể đó

dự án Django. Vì vậy, bây giờ chúng ta đang ở trong dự án này và bây giờ những gì chúng ta có thể làm là chúng ta sẽ

cài đặt môi trường ảo. Vì vậy, chúng ta sẽ nói Python dash M và chúng ta sẽ nói môi trường ảo.

Vì vậy, VENV và trước khi chúng ta làm điều đó, tôi đã xóa toàn bộ màn hình. Chúng ta phải cài đặt ảo

môi trường bao bọc là tốt. Chúng ta có thể không có nó. Vì vậy, hãy làm điều đó đầu tiên. Chúng tôi sẽ sử dụng

trình quản lý gói PIP và chúng tôi sẽ nói PIP và lệnh cài đặt và gói đó là gì

chúng tôi cần là chúng tôi cần trình bao bọc ENV ảo và chúng tôi cần nó cho Windows. Vì vậy, khi bạn nhấn enter,

tôi tin rằng sẽ mất một chút thời gian và vì vậy rõ ràng là chúng tôi đã không có nó. Vì vậy, bây giờ là

cài đặt trình bao bọc môi trường ảo và bây giờ chúng ta có trình bao bọc môi trường ảo.

Bây giờ, điều này sẽ chưa tạo ra môi trường ảo cho bạn vì chúng tôi chỉ đơn giản là

tải xuống và cài đặt gói. Vì vậy, bây giờ chúng ta phải sử dụng gói này và chúng ta

phải tạo một môi trường và sau đó trong môi trường đó, chúng ta sẽ cài đặt Django vì

chúng tôi không muốn có một môi trường Django Python toàn cầu. Chúng tôi chỉ muốn giới hạn môi trường Django

đến một không gian nhỏ mà chúng ta tạo ra cho chính mình. Vì vậy, hãy làm điều đó. Vì vậy, bây giờ chúng ta hãy tạo một ảo

môi trường. Vì vậy, chúng tôi sẽ nói MK tạo ra môi trường ảo ENV chứ không phải ENG và tạo môi trường ảo

môi trường. Vì vậy, hãy nghĩ ra một cái tên và gọi đây là Django VNV. Bây giờ, nếu bạn đánh

nhập, sẽ mất một chút thời gian và nó sẽ tạo ra một môi trường ảo

dành cho bạn. Đây chính là điều tôi đang nói đến. Vì vậy, nếu bạn thấy bạn có đường dẫn và sau đó

bạn đã tạo môi trường ảo và tên của môi trường ảo là Django

UNV. Bây giờ, nếu bạn sử dụng PowerShell, bạn sẽ không bao giờ thấy điều này. Thay vào đó, bạn sẽ thấy

PS thông thường và chữ viết tắt PS bên cạnh đường dẫn. Vì vậy, điều này không hữu ích lắm vì

bạn sẽ vẫn không biết mình đang ở trong môi trường ảo nào. Bây giờ, nếu bạn có thể bước ra ngoài

của môi trường ảo này và nếu bạn muốn quay lại thì còn có một lệnh khác

mà có lẽ chúng ta sẽ xem xét nó sau. Nhưng hiện tại, chúng tôi có thiết lập này. Chúng tôi có

thiết lập môi trường ảo và tôi đã xóa màn hình. Vì vậy, bây giờ chúng ta hãy mở Visual

Studio Code ngay từ đây và chúng tôi đang trên đường đi. Chúng ta cũng đang ở trong một thế giới ảo hoàn hảo

môi trường. Vì vậy, chúng ta có thể vào code và dash dot code space dot. Vì vậy, điều đó sẽ mở Visual

Mã Studio cho môi trường cụ thể này hoặc dự án cụ thể này. Nó không quan trọng

Visual Studio là gì, tôi tin rằng mã không thực sự hiểu được môi trường. Tùy vào thôi

Python để hiểu nó. Vì vậy, khi tôi nhấn enter, nó sẽ mở Visual Studio Code và

họ có thể thấy trong trình khám phá giải pháp, bạn có thể thấy các dự án Django, dự án mà chúng tôi vừa

được tạo ra. So, we are now inside that file. Bây giờ chúng ta đang ở trong thư mục đó. Vì vậy, bây giờ là

đã đến lúc chúng ta tạo các tệp mới và bây giờ chúng ta có thể bắt đầu cài đặt Django. Vì vậy, bây giờ chúng ta có

để mở bảng lệnh và chúng ta phải cho họ biết rằng chúng ta phải để Visual

Studio biết rằng chúng tôi sẽ làm việc bằng Python. Vì vậy, chúng ta sẽ nói điều khiển dịch chuyển P sang

mở bảng lệnh và hãy tìm kiếm trình thông dịch chọn Python. Và một khi chúng tôi đã

đã làm điều đó, nó sẽ làm điều này và nó sẽ chọn trình thông dịch mới nhất và

chúng tôi muốn bit 3.8.164. Bây giờ, nếu bạn nhìn vào đây, bạn biết đấy, mặc dù chúng tôi đã chọn

cái cuối cùng, Python 3.8.164 bit, thực ra, chúng tôi muốn đi sâu vào phần ảo cụ thể này

môi trường vì đó là môi trường mà chúng ta đã tạo ra, phải không? Vì vậy, có ba trong số họ.

Có một cái là 3.7.5 64 bit. Rõ ràng, danh sách này có thể khác nhau tùy thuộc vào số lượng

các phiên bản Python khác nhau mà bạn có thể đã cài đặt. Nhưng nếu bạn chỉ có 3.8.1 thì

có lẽ bạn chỉ nên thấy hai trong số này trong danh sách. Bạn sẽ thấy 3.8.1 64 bit và

bất kể tên của môi trường ảo mà bạn được cung cấp khi chúng tôi tạo

môi trường ảo đó trong dấu nhắc lệnh và môi trường không có bất kỳ môi trường ảo nào

môi trường. Vì vậy, thay vì chọn cái cuối cùng, chúng ta nên chọn cái thứ hai

một và làm điều đó ngay bây giờ. Vì vậy mình sẽ chọn Django ENV, đó là môi trường ảo

và tên của môi trường ảo là VENV. Nếu bạn muốn quay lại và kiểm tra

nó trông như thế này. Thế đấy. Vì vậy, mọi thứ đều ổn và chúng tôi đang ở trong

môi trường ảo. Chúng tôi cũng ở trong thư mục. Ngoài ra, nếu bạn muốn thay đổi

terminal từ PowerShell đến dấu nhắc lệnh, hãy thử điều đó. Và nếu là bạn, chúng ta có thể tạo ra

một thiết bị đầu cuối tích hợp mới. Vì vậy, bạn có thể nói dấu ngã điều khiển và nó đây. Và bây giờ

họ đi. Vì vậy, bây giờ nó đang hiển thị cho chúng ta môi trường ảo. Vì vậy, tôi sẽ chỉ nói CLS. Thông thường,

nó không thực sự hiển thị bên trong PowerShell. Nhưng bây giờ sau khi cập nhật, tôi tin là bây giờ

hiển thị môi trường ảo. Được rồi, được rồi. Vì vậy, bây giờ là lúc cài đặt Django.

Cuối cùng, chúng ta sẽ nói Python bên trong đây, dấu gạch ngang M của Python ở cuối và chúng ta sẽ mang

lên PIP và sau đó chúng tôi sẽ nói cài đặt Django. Nhấn enter và sẽ mất một lúc tùy thuộc vào

trên kết nối internet. Nó sẽ cài đặt Django bên trong môi trường ảo này.

Bây giờ tôi nhận được một số cảnh báo và nó báo là không thể thiết lập được. Nó bảo không tìm thấy

một phiên bản đáp ứng yêu cầu Django. Nhưng điều này xảy ra vì tôi đã mất mạng

kết nối. Vì vậy, hãy thử lại lần nữa và giả sử Python dash M PIP cài đặt Django. bây giờ

hãy chờ một lát. Thế đấy. Và bây giờ nó đang được thu thập và tôi có thể thấy thanh tiến trình. Vì vậy,

bây giờ nó đang hoạt động. Khỏe. Vì vậy, nó là khoảng 7,5 meg. Không có gì và không nên mất quá một nửa

một phút. Và bây giờ nó đã được tải xuống. Bây giờ nó đang cài đặt Django. Vì vậy, tùy thuộc vào tốc độ

thiết bị của bạn là gì hoặc kết nối internet của bạn nhanh như thế nào. Bây giờ, đây chỉ là Django. Nó cũng phải mang lại

trong các gói khác cùng với Django. Vì vậy, nó đang làm tất cả những điều đó. Vì vậy, tôi sẽ tạm dừng

video và sau khi cài đặt xong.