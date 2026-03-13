# 12 cấu hình thế hệ

---

Trong video này, bạn sẽ

kiểm tra một số

các phương pháp và

cấu hình liên quan

thông số mà bạn

có thể sử dụng để tác động đến

cách mà mô hình thực hiện

quyết định cuối cùng về

thế hệ từ tiếp theo.

Nếu bạn đã sử dụng LLM trong

sân chơi như

trên khuôn mặt ôm

trang web hoặc AWS,

bạn có thể đã từng

được trình bày với các điều khiển như

những thứ này để điều chỉnh cách

LLM hành xử.

Mỗi mô hình trưng bày một bộ

cấu hình

các thông số có thể

ảnh hưởng đến mô hình

đầu ra trong quá trình suy luận.

Lưu ý rằng những

khác với

việc đào tạo

các thông số được

đã học trong thời gian đào tạo.

Thay vào đó, những

thông số cấu hình

được gọi tại thời điểm suy luận

và cho bạn quyền kiểm soát

về những thứ như

số lượng tối đa của

mã thông báo khi hoàn thành,

và kết quả đầu ra sáng tạo như thế nào.

Số token mới tối đa là

có lẽ là đơn giản nhất

của các thông số này,

và bạn có thể sử dụng nó để hạn chế

số lượng token đó

mô hình sẽ tạo ra.

Bạn có thể nghĩ về điều này như

đặt giới hạn về số lượng

lần mô hình sẽ đi

thông qua quá trình lựa chọn.

Ở đây bạn có thể xem ví dụ

số lượng mã thông báo mới tối đa đang được đặt

đến 100, 150 hoặc 200.

Nhưng lưu ý chiều dài như thế nào

của việc hoàn thành

trong ví dụ cho

200 thì ngắn hơn.

Điều này là do một cái khác

đã đạt đến điều kiện dừng,

chẳng hạn như mô hình dự đoán

và mã thông báo kết thúc chuỗi.

Hãy nhớ rằng đó là số lượng mã thông báo mới tối đa,

không phải là một con số khó khăn

token mới được tạo ra.

Đầu ra từ

lớp softmax của máy biến áp là

một xác suất

phân phối khắp

toàn bộ từ điển của

những từ mà mô hình sử dụng.

Ở đây bạn có thể thấy một lựa chọn

từ và xác suất của chúng

ghi điểm bên cạnh họ.

Mặc dù chúng ta chỉ

hiển thị bốn từ ở đây,

hãy tưởng tượng rằng đây là một danh sách

tiếp tục với

từ điển hoàn chỉnh.

Ngôn ngữ lớn nhất

mô hình theo mặc định

sẽ hoạt động với

cái gọi là giải mã tham lam.

Đây là hình thức đơn giản nhất

dự đoán từ tiếp theo,

người mẫu ở đâu

sẽ luôn chọn

từ đó với

xác suất cao nhất.

Phương pháp này có thể hoạt động rất tốt

cho thế hệ ngắn nhưng là

dễ bị lặp lại các từ

hoặc những chuỗi từ lặp đi lặp lại.

Nếu bạn muốn tạo

văn bản tự nhiên hơn,

sáng tạo hơn và

tránh lặp lại các từ,

bạn cần sử dụng một số

điều khiển khác.

Lấy mẫu ngẫu nhiên là

cách dễ nhất

để giới thiệu một số biến thể.

Thay vì chọn

từ có thể xảy ra nhất

mỗi lần lấy mẫu ngẫu nhiên,

mô hình chọn một đầu ra

từ ngẫu nhiên bằng cách sử dụng

phân bố xác suất

để cân nhắc việc lựa chọn.

Ví dụ, trong

hình minh họa,

từ chuối có một

điểm xác suất là 0,02.

Với việc lấy mẫu ngẫu nhiên,

điều này tương đương với

2% khả năng là điều này

từ sẽ được chọn.

Bằng cách sử dụng cái này

kỹ thuật lấy mẫu,

chúng tôi giảm khả năng

những từ đó sẽ được lặp lại.

Tuy nhiên, tùy

trên cài đặt,

có khả năng là

kết quả đầu ra có thể quá sáng tạo,

tạo ra những từ gây ra

thế hệ đi lang thang

chuyển sang chủ đề hoặc từ ngữ

điều đó thật vô nghĩa.

Lưu ý rằng trong một số

triển khai,

bạn có thể cần phải vô hiệu hóa

tham lam và kích hoạt ngẫu nhiên

lấy mẫu một cách rõ ràng

Ví dụ như ôm mặt

thực hiện máy biến áp

mà chúng tôi sử dụng trong

phòng thí nghiệm yêu cầu chúng tôi thiết lập

làm mẫu cho bằng đúng.

Cùng khám phá top k và top p nhé

kỹ thuật lấy mẫu để giúp

hạn chế việc lấy mẫu ngẫu nhiên và

tăng cơ hội rằng

đầu ra sẽ hợp lý.

Hai cài đặt, trên cùng p và

top k là kỹ thuật lấy mẫu

mà chúng ta có thể sử dụng để

giúp hạn chế

lấy mẫu ngẫu nhiên và

tăng cơ hội rằng

đầu ra sẽ hợp lý.

Để giới hạn các tùy chọn trong khi vẫn

cho phép một số thay đổi,

bạn có thể chỉ định giá trị k hàng đầu

hướng dẫn mô hình

chỉ chọn từ k token

với xác suất cao nhất.

Trong ví dụ này ở đây,

k được đặt thành ba,

vậy là bạn đang hạn chế

mô hình để lựa chọn

từ ba lựa chọn này.

Sau đó mô hình sẽ chọn

từ các tùy chọn này bằng cách sử dụng

trọng số xác suất

và trong trường hợp này,

nó chọn bánh rán

như từ tiếp theo.

Phương pháp này có thể giúp mô hình

có một số sự ngẫu nhiên trong khi

cản trở việc lựa chọn

rất khó xảy ra

các từ hoàn thiện.

Điều này lần lượt làm cho

thế hệ văn bản của bạn

có nhiều khả năng phát ra âm thanh hơn

hợp lý và có ý nghĩa.

Ngoài ra, bạn

có thể sử dụng p hàng đầu

thiết lập để hạn chế

lấy mẫu ngẫu nhiên

những dự đoán mà

xác suất kết hợp

không vượt quá p. Ví dụ,

nếu bạn đặt p bằng 0,3,

các lựa chọn là bánh ngọt và bánh rán

vì xác suất của chúng

của 0,2 và 0,1 cộng lại thành 0,3.

Sau đó mô hình sẽ sử dụng

xác suất ngẫu nhiên

phương pháp cân

để chọn từ các token này.

Với top k, bạn chỉ định

số lượng token để

chọn ngẫu nhiên từ,

và với đỉnh p,

bạn chỉ định

tổng xác suất

rằng bạn muốn

mô hình để lựa chọn.

Một thông số nữa đó

bạn có thể sử dụng để kiểm soát

sự ngẫu nhiên của

đầu ra mô hình

được gọi là nhiệt độ.

Thông số này

ảnh hưởng đến hình dạng của

xác suất

phân phối đó

mô hình tính toán

cho mã thông báo tiếp theo.

Nói một cách rộng rãi thì

nhiệt độ cao hơn,

tính ngẫu nhiên càng cao,

và nhiệt độ càng thấp,

tính ngẫu nhiên càng thấp.

Giá trị nhiệt độ là

một hệ số tỷ lệ

điều đó được áp dụng trong

lớp softmax cuối cùng

của mô hình đó

tác động đến hình dạng của

phân bố xác suất

của token tiếp theo.

Ngược lại với đỉnh

tham số k và p trên cùng,

thay đổi

nhiệt độ thực sự

làm thay đổi dự đoán

mà mô hình sẽ thực hiện.

Nếu bạn chọn mức thấp

giá trị nhiệt độ,

nói ít hơn một,

xác suất kết quả

phân phối từ

lớp softmax

mạnh mẽ hơn

đạt đỉnh cao với

xác suất là

tập trung ở một

số lượng từ ít hơn.

Bạn có thể thấy điều này ở đây trong

thanh màu xanh bên cạnh bàn,

hiển thị thanh xác suất

biểu đồ quay về phía nó.

Phần lớn xác suất ở đây là

tập trung vào từ bánh.

Mô hình sẽ chọn

từ sự phân phối này

sử dụng phương pháp lấy mẫu ngẫu nhiên và

văn bản kết quả sẽ là

ít ngẫu nhiên hơn và sẽ

theo dõi chặt chẽ hơn

chuỗi từ có khả năng xảy ra nhất

mà người mẫu đã học được

trong quá trình đào tạo.

Nếu thay vào đó bạn đặt

nhiệt độ lên giá trị cao hơn,

nói, lớn hơn một,

sau đó mô hình sẽ tính toán

phẳng hơn

phân phối xác suất

cho mã thông báo tiếp theo.

Chú ý rằng ngược lại

đến các thanh màu xanh,

xác suất đồng đều hơn

trải rộng trên các token.

Điều này dẫn đến mô hình

để tạo văn bản

với trình độ cao hơn

sự ngẫu nhiên

và nhiều biến đổi hơn trong

đầu ra so với một

cài đặt nhiệt độ mát mẻ.

Điều này có thể giúp bạn tạo ra

văn bản nghe có vẻ sáng tạo hơn.

Nếu bạn để lại nhiệt độ

giá trị bằng một,

điều này sẽ để lại

chức năng softmax như

mặc định và không thay đổi

phân phối xác suất

sẽ được sử dụng.

Bạn đã bảo hiểm rất nhiều

mặt đất cho đến nay.

Bạn đã kiểm tra các loại

nhiệm vụ mà LLM đang thực hiện

có khả năng biểu diễn và

tìm hiểu về máy biến áp

kiến trúc mô hình đó

cung cấp năng lượng cho những công cụ tuyệt vời này.

Bạn cũng đã khám phá cách để có được

hiệu suất tốt nhất có thể

trong số các mô hình này bằng cách sử dụng

kỹ thuật nhanh chóng và

bằng cách thử nghiệm với

suy luận khác nhau

các thông số cấu hình.

Trong video tiếp theo,

bạn sẽ bắt đầu xây dựng trên

kiến thức nền tảng này

bằng cách suy nghĩ thấu đáo

các bước cần thiết

để phát triển và

khởi động LLM

-Ứng dụng được hỗ trợ.