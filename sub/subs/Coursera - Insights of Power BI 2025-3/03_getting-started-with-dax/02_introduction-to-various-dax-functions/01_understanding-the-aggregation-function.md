# 01 hiểu-hàm-tổng hợp

---

Xin chào và chào mừng trở lại.

Ở bài học trước,

chúng ta đã học được những nguyên tắc cơ bản của

cột được tính toán

và các biện pháp và

cũng phát hiện ra

sự khác biệt giữa

hai bằng cách giải Prime

Do vấn đề kinh doanh.

Trong video này hãy cùng giải quyết

một doanh nghiệp khác

vấn đề đối với Prime By.

Prime By muốn thực hiện

quyết định trong tương lai về tài nguyên

phân bổ và thiết lập

chỉ tiêu doanh số từng cửa hàng

dựa trên khả năng sinh lời của họ

trong suốt cả năm.

Prime By muốn tính toán

tỷ suất lợi nhuận ròng cho

mỗi cửa hàng để đánh giá

hiệu suất của họ.

Tỷ suất lợi nhuận ròng là

thước đo tài chính đo lường

khả năng sinh lời của một doanh nghiệp

so với tổng doanh thu của nó.

Công thức tính toán

biên lợi nhuận ròng là

tỷ suất lợi nhuận ròng

bằng lợi nhuận ròng

chia cho tổng doanh thu

nhân với 100.

Lợi nhuận ròng ở đâu

tổng lợi nhuận kiếm được

của doanh nghiệp sau

trừ đi mọi chi phí.

Tức là tổng chi phí

từ tổng doanh thu.

Để giải quyết vấn đề này,

chúng ta hãy hướng tới

Máy tính để bàn Power BI

và điều hướng đến

phiếu đặt hàng bán hàng.

Tuy nhiên, chúng tôi nhận thấy rằng có

không có cột hiện có tên

tỷ suất lợi nhuận ròng.

Bây giờ để tính toán

tỷ suất lợi nhuận ròng,

chúng ta sẽ cần phải

tính toán lợi nhuận ròng.

Đối với điều này, chúng tôi sẽ

cần hai thành phần;

doanh thu và chi phí,

và sau đó sử dụng chúng để tìm

tỷ suất lợi nhuận ròng

cho mỗi cửa hàng.

10 điều này sẽ được tổng hợp

khắp các cửa hàng bằng cách sử dụng

các hàm tổng hợp.

Chúng tôi đã sử dụng tổng hợp

hoạt động sớm hơn.

Hãy nhớ rằng, khi bạn tạo

số lượng đơn đặt hàng được đo lường,

bạn sử dụng chức năng đếm hàng.

Đếm hàng là một trong những

các hàm tổng hợp.

Một hàm tổng hợp

là một cách để thực hiện

phép tính trên một tập hợp các giá trị

để trả về một giá trị duy nhất

tóm tắt hoặc đại diện

những giá trị đó.

Một số tổng hợp thông dụng

các hàm là tổng,

đếm, trung bình, tối thiểu, tối đa, v.v.

Với kiến thức này,

hãy tiếp tục với

nhiệm vụ của Prime By

tính toán mạng

tỷ suất lợi nhuận cho

mỗi cửa hàng và

hiểu các biến và

chức năng tổng hợp tốt hơn như

chúng tôi giải quyết vấn đề kinh doanh.

Đầu tiên, hãy tạo

cột tổng chi phí

sử dụng các cột tính toán.

Để đạt được điều này, hãy điều hướng

vào phiếu đặt hàng bán hàng,

và nhấp chuột phải vào nó.

Từ trình đơn thả xuống,

chọn cột mới.

Bây giờ, trong thanh công thức,

chuyển qua cột

đặt tên là tổng chi phí và

tính toán tổng chi phí

cho mỗi đơn hàng bằng

nhân các giá trị trong

cột đơn giá và

các giá trị trong

cột số lượng đặt hàng

và sau đó nhấn "Enter." Với điều đó,

chúng tôi đã thêm một cái mới

cột tính toán

tổng chi phí trong

phiếu đặt hàng bán hàng.

Bây giờ hãy bắt đầu quá trình

về việc tạo ra thước đo mục tiêu của chúng tôi,

đó là tỷ suất lợi nhuận ròng.

Để làm điều đó, nhấp chuột phải vào

phiếu đặt hàng bán hàng và

chọn biện pháp mới từ

trình đơn thả xuống.

Tiếp theo, chuyển tên của

thước đo là lợi nhuận ròng

lề có dấu bằng.

Đây sẽ là một

tính toán phức tạp

cái nào sẽ sử dụng cái khác

các biến và thước đo,

vậy hãy tạo hai

biện pháp bên trong

phép tính mà

sẽ được giao cho

biến, doanh thu và chi phí.

Những biến này sẽ giúp chúng ta

giá trị tạm thời khi chúng ta đi

thông qua tính toán

từng bước một.

Đầu tiên chúng ta tính tổng của

cột số tiền bán hàng từ

phiếu đặt hàng bán hàng và

lưu trữ nó trong

biến doanh thu.

Để làm được điều đó chúng ta cần sử dụng

một hàm tổng hợp là

tổng hợp và chuyển tiếp

tên của cột.

Điều này mang lại cho chúng tôi tổng số

doanh thu từ tất cả các lần bán hàng.

Tóm lại, hãy sử dụng var

từ khóa trước khi bạn

tạo một biến.

Tiếp theo, chúng ta tính tổng

cột tổng chi phí bằng

sử dụng hàm tổng hợp và

lưu trữ nó trong biến chi phí.

Điều này thể hiện tổng chi phí

phát sinh trong việc thực hiện các giao dịch bán hàng đó.

Bây giờ hãy tạo

một biến khác.

Bây giờ chúng ta có doanh thu

và chi phí được lưu trữ trong các biến,

chúng ta có thể chuyển sang

tính toán lợi nhuận ròng.

Hãy tạo một cái khác

biến cho lợi nhuận ròng.

Chúng ta sẽ sử dụng hàm chia

để thực hiện phép tính này.

Chức năng chia

có hai đối số.

Tử số và

mẫu số,

điều đó cũng được thể hiện bởi

intellisense từ Power BI,

trong đó hiển thị cú pháp và

các đối số cần thiết.

Trong trường hợp của chúng tôi, tử số

là lợi nhuận ròng,

đó là doanh thu

trừ chi phí,

và mẫu số

là doanh thu.

Hãy vượt qua những lập luận này.

Chúng tôi sẽ sử dụng lại các biến

mà chúng tôi đã thực hiện.

Nhưng chờ đã, còn một cái nữa

điều chúng ta cần xem xét,

điều gì sẽ xảy ra nếu doanh thu của một

cửa hàng cụ thể bằng không?

Chúng ta không muốn chia cho số 0,

bởi vì đó là

về mặt toán học không xác định,

để chia một số cho 0,

và Power BI do đó sẽ

trả về vô cùng trong trường hợp đó.

Vì vậy, để xử lý tình huống,

chúng tôi đặt ra một đối số thứ ba cho

hàm chia bằng 0.

Điều này có nghĩa là nếu

mẫu số,

trong trường hợp của chúng tôi doanh thu bằng 0,

chức năng sẽ trở lại

một kết quả thay thế của

số không thay vì vô cùng.

Xin lưu ý rằng

chức năng chia

không phải là hàm tổng hợp,

vì nó chủ yếu được sử dụng cho

tính toán số học,

và không tập trung vào việc tóm tắt

hoặc tổng hợp dữ liệu.

Cuối cùng, sau khi tính toán

lợi nhuận ròng sử dụng

hàm chia,

hãy đóng dấu ngoặc đơn lại

và chúng tôi sử dụng

báo cáo trả lại tại

sự kết thúc để trở lại

biến cuối cùng là

đầu ra của biện pháp này.

Cuối cùng, nhấp vào "Enter."

Với những bước này,

chúng tôi đã tạo ra một thước đo

tính toán đó

tỷ suất lợi nhuận ròng

cho đơn đặt hàng của chúng tôi.

Để giúp chúng tôi dễ dàng

dùng mọi biện pháp

mà chúng tôi đang tạo ra,

chúng tôi sẽ thêm tất cả các biện pháp vào

một bảng duy nhất được gọi là

Bảng đo.

Việc thực hành này sẽ

giúp theo dõi

các biện pháp trong khi làm việc

trong một dự án lớn hơn.

Hãy tạo bảng Biện pháp.

Điều hướng đến tab Trang chủ

và chọn bảng mới,

hiện diện dưới

phần tính toán.

Trên thanh công thức, chúng ta sẽ

chuyển tên bảng như

Bảng đo bằng cách sử dụng

dấu bằng và nhấn "Enter."

Bạn có thể thấy một bảng mới bằng cách

cùng một tên giữ

không có dữ liệu nào được tạo ra.

Bây giờ hãy di chuyển mạng

thước đo tỷ suất lợi nhuận

từ Đơn bán hàng

Tờ, vào bảng này.

Để thực hiện việc này, hãy quay lại

phiếu đặt hàng bán hàng

và chọn mạng

thước đo tỷ suất lợi nhuận,

và truy cập

Tab Công cụ đo lường.

Dưới tab này, bạn

sẽ tìm thấy các tùy chọn,

tên và bảng nhà.

Bấm vào menu thả xuống

trong tùy chọn Bảng Nhà,

và lựa chọn biện pháp

bảng từ danh sách.

Bằng cách làm này, mạng

thước đo tỷ suất lợi nhuận

bây giờ sẽ xuất hiện trong

bảng Biện pháp.

Tương tự, chúng ta có thể lặp lại

quá trình di chuyển

số lượng đơn đặt hàng

từ việc bán hàng

Đơn đặt hàng

mà chúng tôi đã tạo trong

bài học cuối cùng,

và thêm nó vào

Bảng đo.

Bây giờ chúng ta hãy nhớ lại

báo cáo vấn đề ở đây.

PrimBuy muốn tính toán

tỷ suất lợi nhuận ròng

cho mỗi cửa hàng,

để đánh giá hiệu suất của họ và

xác định điều tốt nhất và

cửa hàng hoạt động kém nhất

Để hình dung điều này,

hãy điều hướng đến

chế độ xem báo cáo

phần trong một trang mới,

và chọn hình ảnh ma trận.

Khi được chọn tại

cột mã cửa hàng từ

Phiếu đặt hàng bán hàng tới

trường hàng của

ma trận trực quan.

Tiếp theo điều hướng đến

bảng đo,

và kéo lợi nhuận ròng

đo từ nó,

và thả nó vào các giá trị

trường của ma trận trực quan.

Bạn có thể thấy

tỷ suất lợi nhuận ròng

sắp ra ở dạng số thập phân.

Để khắc phục điều này, chúng ta cần nhấp vào

về thước đo từ

ngăn dữ liệu,

và dưới định dạng,

chúng ta chỉ cần nhấp vào

trên biểu tượng phần trăm.

Bây giờ lợi nhuận ròng

đến dưới dạng phần trăm.

Với những bước này, bạn

có thể thấy một bảng ma trận

tạo ra sự cho đi

thông tin về

lợi nhuận ròng

khắp các cửa hàng.

Với hình ảnh này, PrimBuy đã

có thể phát hiện ra rằng cửa hàng

đó là lợi nhuận cao nhất bởi

bấm vào cột

tiêu đề của lợi nhuận ròng,

và sắp xếp nó để có được

lợi nhuận ròng cao nhất.

Họ nhận thấy rằng

mã cửa hàng 122,

là lợi nhuận cao nhất

trong số những người khác.

Mặt khác, cửa hàng

ở cuối danh sách là

cửa hàng có mã 46.

Phân tích này sẽ giúp

PrimBuy tiếp tục

thực hiện theo các thông lệ tốt trong

cửa hàng nơi

khả năng sinh lời cao,

và thực hiện chẩn đoán

phân tích tại

cửa hàng nơi có lợi nhuận

tỷ lệ phần trăm thấp hơn.

Với điều đó, chúng ta đi đến

cuối bài học.

Chúng tôi đã thành công

đã giúp PrimBuy khám phá cách

các cửa hàng đang hoạt động dựa trên

trên tương ứng của họ

tỷ suất lợi nhuận ròng.

Chúng tôi cũng đã hiểu

sử dụng các hàm tổng hợp

Trong video sắp tới,

chúng tôi sẽ giúp PrimBuy đánh giá

bán thiết bị điện tử tại

liên quan đến tổng

doanh thu và doanh thu bình quân.