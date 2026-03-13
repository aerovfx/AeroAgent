# 03 - Giải pháp Thực hiện phân tích dữ liệu thăm dò

---

(nhạc có nhịp độ nhanh retro)

- [Người hướng dẫn] Cho đến nay, chúng tôi đã thực hiện bước đầu tìm hiểu

của tập dữ liệu viễn thông của chúng tôi.

Chúng tôi cũng đã xử lý trước tập dữ liệu viễn thông của mình

và lưu tập dữ liệu được xử lý trước

vào một tệp mới có tên là clean_telecom.csv.

Trong thử thách này, chúng ta sẽ tìm cách đạt được cái nhìn sâu sắc

vào dữ liệu bằng cách sử dụng các hình ảnh trực quan như biểu đồ thanh, bản đồ nhiệt,

biểu đồ, biểu đồ phân tán, v.v.

Khi chúng tôi hoàn thành phần phân tích dữ liệu khám phá của mình,

đó là lúc để xây dựng

và đào tạo mô hình học máy của chúng tôi.

Lần tải đầu tiên trong cả tập dữ liệu viễn thông

và tập dữ liệu đã được làm sạch.

Và để làm điều đó, chúng ta sẽ đi tới Tệp

và lấy cả hai tập dữ liệu của chúng tôi và mở.

Và vì vậy bài tập này nằm trong

phần phân tích dữ liệu thăm dò

nơi bạn sẽ tính toán các hợp đồng được phân phối như thế nào.

Bạn sẽ tạo một biểu đồ thanh cho điều đó.

Bạn sẽ tạo một biểu đồ hình tròn

để vẽ biểu đồ loại hợp đồng theo phân phối.

Bạn sẽ tạo một biểu đồ phân tán

để vẽ đồ thị thời gian sử dụng theo tháng so với tổng doanh thu.

Bạn sẽ tạo một bản đồ nhiệt nơi bạn sẽ nhập mã

để hình dung các mối quan hệ trong tương lai,

và bạn sẽ vẽ biểu đồ để vẽ biểu đồ thời gian nắm quyền.

Và có một số kỹ thuật tính năng đơn giản,

nhưng điều này đã được mã hóa cứng cho bạn.

Nó chỉ để bạn tham khảo.

Và cuối cùng, bạn sẽ lưu tệp Clean,

và mã đó cũng được cung cấp.

Vì vậy, điều tiếp theo chúng ta làm là thu gọn tải

trong phần Khám phá dữ liệu và chạy các ô.

Chúng tôi cũng thu gọn phần tiền xử lý dữ liệu

và chạy các ô đó.

Và bây giờ tôi sẽ cuộn xuống,

và ở đây chúng ta đang ở phần Dữ liệu khám phá.

Bây giờ bạn sẽ thấy các biểu đồ bổ sung

và đồ thị để bạn tham khảo,

nhưng đối với các bài tập, chúng khá đơn giản.

Bạn đang tải dữ liệu,

bạn đang nhìn vào năm hàng đầu tiên,

bạn đang xem thông tin trên khung dữ liệu

chỉ để đảm bảo mọi thứ diễn ra như ý muốn.

Đây là biểu đồ thanh,

và chúng tôi đang xem xét việc hình dung

phân bổ loại hợp đồng

Và vì vậy chúng tôi đang làm cho nó có kích thước khoảng 10 X 6

về kích thước hình.

Chúng tôi đang sử dụng phương pháp cốt truyện seaborn.count

đếm số lượng quan sát.

Và chúng tôi đặt cho nó một tiêu đề là plt.title.

Và chúng tôi đang đặt cho trục X một nhãn có tên là Loại hợp đồng,

và nhãn y có tiêu đề được gọi là Đếm.

Và plt.show sẽ hiển thị cốt truyện.

Và đó là những gì chúng tôi có ở đây.

Và chúng ta sẽ làm điều tương tự với biểu đồ thanh.

Vì vậy tôi sẽ lướt qua, đây chỉ là tài liệu tham khảo.

Chúng ta cũng sẽ làm điều tương tự với biểu đồ hình tròn.

Một lần nữa, cùng kích thước hình, 10 X 6.

Chúng tôi đang xem xét Phân phối loại hợp đồng,

và chúng tôi đặt cho nó một tiêu đề,

chúng tôi đang đặt cho nó một nhãn và chúng tôi đang hiển thị cốt truyện.

Đó là biểu đồ hình tròn.

Và sau đó đối với biểu đồ phân tán,

điều tương tự khi sử dụng Matplotlib.

Chúng tôi chỉ có cùng kích thước cơ thể.

Ở đây chúng ta đang xem xét nhiệm kỳ theo tháng so với tổng doanh thu.

Và ở đây với bản đồ nhiệt,

chúng tôi đang thực hiện một phép tương quan_matrix.

Và đây thực sự là hình dung phần này ngay tại đây,

là một phần của bài tập,

nơi bạn đang làm chỉ là vẽ biểu đồ trực quan.

Bạn sẽ nhận thấy rằng kích thước hình đã thay đổi.

Đó là 20X15.

Và đây chỉ là biểu đồ bổ sung để bạn tham khảo.

Và sau đó là biểu đồ, đây là một,

nhưng cái dành cho bài tập thì rất đơn giản.

Chỉ có cái này thôi.

Bạn đang loại bỏ quyền sử dụng tính năng,

và bạn chỉ đang thể hiện sự phân bổ quyền sở hữu

sử dụng biểu đồ phân phối của seaborn.

Đây là tất cả, một lần nữa, để tham khảo.

Và cuối cùng là một số tế bào và kỹ thuật tính năng.

Tôi sẽ mở chúng thật nhanh

bởi vì chúng tôi sẽ tạo ra tính năng này

Giá trị trọn đời của khách hàng.

Hãy nhìn vào đó.

Và chúng tôi sẽ tạo ra tính năng này

được gọi là Tổng số dịch vụ được sử dụng.

Hãy nhìn vào đó.

Nhưng điều bạn thực sự cần làm

trước khi bạn kết thúc bài tập này

là để đảm bảo rằng bạn lưu tập tin

dưới dạng một tệp mới có tên eda_telecom.

Và điều này cho chúng tôi biết rằng tệp này đã được xử lý,

EDA đã được thực hiện,

và bây giờ nó đã sẵn sàng cho mô hình học máy.