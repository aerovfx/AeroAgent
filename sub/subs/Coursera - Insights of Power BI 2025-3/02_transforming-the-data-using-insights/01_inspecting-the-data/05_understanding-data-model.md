# 05 hiểu-dữ liệu-mô hình

---

Trong video trước của chúng tôi,

chúng tôi đã khám phá mối quan hệ phức tạp

trong dữ liệu của primebuy, khám phá

cách họ kết nối nhiều bảng.

Trong video này, chúng tôi tiếp tục hành trình tìm kiếm

hiểu dữ liệu bằng cách lặn sâu hơn

vào thế giới của mô hình hóa dữ liệu.

Hiểu mô hình dữ liệu là một điều quan trọng

một phần của hành trình chuyên gia dữ liệu.

Vì hầu hết các bộ dữ liệu đời thực đều phức tạp

bao gồm nhiều tờ,

xử lý nhiều tờ này là

một phần thiết yếu của phân tích dữ liệu.

Hãy bắt đầu [ÂM THANH].

Đầu tiên, hãy chuyển sang chế độ xem mô hình và

hiểu lược đồ của tập dữ liệu của chúng tôi.

Nếu bạn kiểm tra cẩn thận

từng mối quan hệ,

bạn sẽ nhận thấy rằng mọi người khác

trang tính được liên kết với trang tính trung tâm,

đó là Bảng đặt hàng bán hàng,

ngoại trừ Bảng khu vực.

Các khu vực và Bảng đặt hàng bán hàng

được kết nối gián tiếp thông qua

một tờ trung gian

Bảng vị trí được lưu trữ.

Power BI đã tạo được mối quan hệ

giữa các vùng và

Bảng vị trí cửa hàng bằng cách sử dụng

mã trạng thái cột chung.

Hơn nữa, nó kết nối bảng vị trí

với bảng Bán hàng bằng ID cửa hàng

trong Bảng vị trí cửa hàng để

Mã cửa hàng trong Bảng đặt hàng bán hàng.

Điều này giúp tạo ra cầu nối

giữa Bảng vùng và

Phiếu đặt hàng bán hàng.

Bạn có thể quan sát dòng chảy

của các kết nối

bằng cách làm theo hướng nhỏ

mũi tên giữa các kết nối.

The connection from Regions

bảng được chuyển qua

Bảng vị trí cửa hàng và

sau đó cuối cùng đến Bảng đặt hàng bán hàng.

Cùng với đó, chúng tôi đã khám phá lược đồ

của mối quan hệ trong tập dữ liệu,

và bây giờ là thời điểm lý tưởng để giới thiệu

khái niệm về bảng sự kiện và

các bảng chiều.

Bảng sự thật.

Trong Power BI, một bảng dữ kiện là

một bảng trung tâm kết nối với

nhiều tờ trong tập dữ liệu.

Nó thường chứa dữ liệu định lượng

liên quan đến một doanh nghiệp hoặc sự kiện cụ thể.

Giờ bạn nghĩ sao về bảng nào

sẽ phù hợp như một bảng thực tế trong trường hợp của chúng tôi?

Phiếu đặt hàng bán hàng.

Phải.

Phiếu đặt hàng bán hàng bao gồm

một số cột có

một dữ liệu định lượng hiện tại cho

mỗi đơn hàng ở các hàng khác nhau.

Tiếp tục,

hãy hiểu bảng thứ nguyên là gì?

Bảng thứ nguyên là bảng

cung cấp các thuộc tính mô tả cho

dữ liệu được lưu trữ trong bảng sự kiện.

Các bảng này thường

bao gồm dữ liệu văn bản và

số nhận dạng duy nhất là khóa chính

kết nối chúng với bảng sự kiện.

Ví dụ,

Bảng vị trí cửa hàng phục vụ

như một bảng thứ nguyên vì nó

chứa một mã định danh duy nhất

ID cửa hàng kết nối

nó với bảng sự kiện.

Tiếp theo, hãy nói về sự khác biệt

các loại mối quan hệ trong Power BI,

được đại diện bởi

Số lượng trong Power BI.

Chúng tôi đã xem xét ngắn gọn về Cardinality trong

video trước đó trong khi tạo

mối quan hệ giữa sản phẩm và

phiếu đặt hàng bán hàng.

Lần này hãy tìm hiểu sâu hơn

sự hiểu biết về Cardinality.

Tính chủ yếu trong Power BI là tất cả về

cách các trang tính được kết nối với nhau

khác dựa trên tần số của

các giá trị trong các cột kết nối chung.

Có ba loại cardinality.

Một-một, một-nhiều và nhiều-nhiều.

Điều cần thiết là phải thiết lập quyền

cardinality để đảm bảo dữ liệu là

được kết nối chính xác và bộ lọc

làm việc chính xác giữa các bảng.

Một lần nữa, Power BI đủ thông minh để

hiểu loại cardinality, nhưng

chúng ta vẫn nên có một cái gì đó cơ bản

sự hiểu biết về các loại bản số để

hiểu các mối quan hệ tốt hơn.

Hãy bắt đầu mọi thứ với

one-to-one relationship.

Trong mối quan hệ kiểu này, mỗi hàng

của cột chung trong bảng đầu tiên

có chính xác một hàng tương ứng trong

cột kết nối của bảng thứ hai.

Mặc dù kiểu quan hệ này

ít phổ biến hơn trong các mô hình dữ liệu,

nó có thể xảy ra khi bạn có hai

các bảng có thông tin duy nhất

có liên quan một đối một.

Ví dụ: trong mô hình dữ liệu của chúng tôi,

chúng ta có mối quan hệ một-một

giữa Nhân khẩu học của nhóm bán hàng và

Bảng nhóm bán hàng.

Điều này cũng được hiển thị trong chế độ xem mô hình.

Nếu bạn quan sát kỹ ở cả hai

đầu kết nối giữa

Nhân khẩu học của nhóm bán hàng và doanh số bán hàng

Team Sheet, chúng ta có số một.

Khi bạn nhấp vào kết nối

đường giữa các bảng,

bạn sẽ thấy loại cardinality như

một-một trong Ngăn Thuộc tính.

Tiếp theo, hãy nói về điều nhiều nhất

kiểu quan hệ phổ biến,

nghĩa là, nhiều mối quan hệ.

Trong chế độ xem mô hình,

điều này có thể được nhận thấy khá thường xuyên.

Bạn sẽ nhận thấy rằng Đơn đặt hàng bán hàng

Trang tính được kết nối với các trang tính khác

có dấu hoa thị trên Đơn đặt hàng

tờ và một trên các tờ khác.

Dấu hoa thị đại diện cho nhiều trường hợp

các giá trị trong cột trong bảng sự kiện.

Với mối quan hệ kiểu này, mỗi hàng

của cột chung trong bảng đầu tiên

được liên kết với nhiều hàng trong

kết nối các cột của bảng thứ hai.

Trong chế độ xem mô hình, bạn sẽ nhận thấy

kiểu lượng tử nhiều-một đó

hiển thị khi bạn nhấp vào kết nối

dòng giữa Bảng đặt hàng bán hàng và

Bảng vị trí cửa hàng.

Chúng ta hãy nhìn vào một trong

các mối quan hệ nguyên tố theo tập dữ liệu cho

một sự hiểu biết tốt hơn.

Bảng thông tin khách hàng không lặp lại

ID khách hàng được kết nối với việc bán hàng

bảng đặt hàng với mã khách hàng lặp lại.

Mỗi khách hàng có thể có

nhiều giao dịch nhưng

mỗi giao dịch đều có liên quan

chỉ cho một khách hàng.

Vì bạn sẽ gặp phải loại này

về mối quan hệ thường xuyên hơn,

điều quan trọng là phải hiểu đầy đủ nó.

Tại sao bạn không xem qua tất cả

các mối quan hệ còn lại

xác định cách chúng được kết nối và

họ chia sẻ loại hồng y nào?

Hãy đi đến phần cuối cùng

kiểu quan hệ,

đó là mối quan hệ nhiều-nhiều.

Mối quan hệ nhiều-nhiều đề cập đến

thực tế là có nhiều hàng

cột chung trong bảng đầu tiên

được kết nối với nhiều hàng của

cột chung trong bảng thứ hai.

Thật hiếm khi gặp phải

mối quan hệ kiểu này.

Chúng ta hãy cố gắng hiểu mối quan hệ này

sử dụng một ví dụ dữ liệu khác.

Từ menu Bắt đầu,

hãy mở một phiên bản khác của Power BI.

Và hãy nhập một tập dữ liệu nhỏ hơn vào đó

vì chúng tôi không muốn những bảng này được hiển thị cho

minh họa can thiệp

với mô hình dữ liệu hiện có của chúng tôi.

Như bạn có thể thấy,

tập dữ liệu hiện tại của chúng tôi có một khách hàng và

bảng sản phẩm hiển thị trên màn hình.

Hãy chuyển tới chế độ xem Dữ liệu và xem

nhìn vào dữ liệu có trong các bảng này.

Chúng ta có thể thấy ID khách hàng là duy nhất

xác định khách hàng và

chúng tôi cũng có tên khách hàng và

ID sản phẩm của các mặt hàng đã mua.

Tiếp theo chúng ta có bảng sản phẩm.

Là cột đầu tiên,

chúng tôi có ID khách hàng cho

khách hàng đã mua

sản phẩm đã cho trong quá khứ.

Doanh nghiệp duy trì bảng này để giữ

theo dõi khách hàng của ai là ai

một sản phẩm cụ thể

Như chúng ta có thể thấy, một khách hàng có thể mua

nhiều sản phẩm tại cửa hàng.

Ví dụ,

chúng ta có thể thấy từ bảng khách hàng

Ethan đã mua hai cái

sản phẩm có ID 1 và 4.

Tương tự, một sản phẩm có thể

được nhiều khách hàng mua.

Như chúng ta có thể thấy từ bảng sản phẩm,

lò vi sóng được mua bởi

ID khách hàng 1 cũng như 3.

Hãy đến Model, View và kiểm tra

mối quan hệ giữa các bảng này.

Chúng tôi thấy Power BI chưa tự động

đã xác định được mối quan hệ

giữa các bảng này.

Hãy thực hiện kết nối

sử dụng cột CustomerID.

Hộp thoại tạo mối quan hệ sẽ mở ra và

chúng ta có thể thấy chúng ta có rất nhiều

mối quan hệ giữa hai bảng.

Hãy nhấn OK để thiết lập

mối quan hệ [ÂM THANH].

Điều đó đưa chúng ta đến phần cuối của bài học này.

Trong bài học này, chúng tôi đã giúp PrimeBY trong

giải quyết hai báo cáo vấn đề của họ

đang biểu diễn sơ bộ

điều tra trên tập dữ liệu.

Xác định và thiết lập các mối quan hệ

trong dữ liệu có trong các bảng khác nhau.

Trong bài học tiếp theo,

chúng tôi sẽ tiếp tục giúp PrimeBy giải quyết

các phát biểu vấn đề còn lại.

Hẹn gặp bạn ở đó.