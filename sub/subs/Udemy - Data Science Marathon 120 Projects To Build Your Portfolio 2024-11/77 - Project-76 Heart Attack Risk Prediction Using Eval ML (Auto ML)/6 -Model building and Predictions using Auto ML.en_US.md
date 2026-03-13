# 6 -Xây dựng mô hình và dự đoán bằng Auto ML.en US

---

WEBVTT

Xin chào.

Trong phần này, chúng ta sẽ thảo luận về các kỹ thuật học máy tự động khác nhau mà chúng ta

có thể sử dụng thay cho các kỹ thuật học máy mà chúng ta đã sử dụng trong các phần trước.

Chúng tôi sẽ sử dụng ML cho dự án này, ngay cả khi đó là thư viện Auto Machine Learning mã nguồn mở

được viết bằng Python tự động hóa phần lớn quá trình học máy và chúng ta có thể dễ dàng đánh giá

quy trình máy học nào hoạt động tốt hơn với một tập hợp dữ liệu nhất định.

Bạn chỉ cần cung cấp một loại dữ liệu nhất định và thậm chí email sẽ cung cấp cho bạn dự đoán dự đoán

đầu ra bằng cách so sánh tất cả các tham số khác nhau cũng như các tham số và mô hình siêu điều chỉnh.

Ngoài ra bạn phải cài đặt.

Bạn có thể thực hiện bằng dấu nhắc lệnh hoặc bạn có thể cài đặt trực tiếp nó trong môi trường phòng thí nghiệm của mình bằng cách chết,

bằng cách viết, chấm than, cài giấy.

Tôi đã làm nó rồi.

Sẽ mất khoảng 5 phút để cài đặt.

Nó sẽ tải xuống tất cả các thư viện, sau đó chúng tôi sẽ đọc tập dữ liệu đã hoàn thành trước đó hoặc được cung cấp

phần được sao chép.

Sau đó chúng ta sẽ thấy tập dữ liệu của chúng tôi.

Nó cũng giống như trước đây.

Chúng tôi sẽ không làm gì cả.

Chúng tôi chỉ chia dữ liệu thành một biến phụ thuộc và biến độc lập.

Như chúng ta thấy, đây là biến phụ thuộc, biến mục tiêu và đây là các biến độc lập của chúng ta.

Bây giờ chúng ta sẽ nhập thư viện phần tử.

Tôi đã làm nó rồi.

Sẽ mất từ ​​2 đến 3 phút để nhập.

Bây giờ chúng ta sẽ chia nhỏ dữ liệu của mình.

Những gì chúng tôi làm là sử dụng chức năng nhập dữ liệu phân tách trước khi xử lý.

Điều này sẽ làm gì, điều này sẽ xử lý dữ liệu, giống như thực hiện tất cả những việc như tiêu chuẩn.

Vì vậy, chúng tôi đang thực hiện tiêu chuẩn hóa, chúng tôi không mã hóa và mọi thứ và nó phân chia dữ liệu dưới dạng

hương vị tàu hỏa.

Tỷ lệ nó sử dụng là 28%, 80% dùng cho dữ liệu huấn luyện và 20% cho dữ liệu thử nghiệm.

Bây giờ chúng là các loại tham số khác nhau trong loại bài toán chẵn là nhị phân.

Có nhiều loại vấn đề khác nhau.

Đó là thời gian hồi quy đa lớp nhị phân.

Đó là thời gian hồi quy.

Đó là thời gian nhị phân, nó là đa lớp.

Ở đây đầu vào của chúng tôi là nhị phân và bằng 0 hoặc một hai sẽ sử dụng nhị phân.

Nếu nhiều hơn hai thì chúng ta sẽ sử dụng multiclass.

Và nếu đó là một con số, chúng ta sẽ sử dụng hồi quy.

Bây giờ để tìm kiếm mô hình tốt nhất tốt nhất, chúng tôi sẽ sử dụng từ đầu vào ML hoặc HTML hoặc tìm kiếm HTML độc ác.

Tìm kiếm AutoML giống như một tham số mà chúng tôi sẽ cung cấp, chúng tôi sẽ cung cấp các dữ liệu khác nhau và chúng tôi sẽ thực hiện

loại vấn đề dưới dạng nhị phân và chúng tôi sẽ thực hiện tìm kiếm dấu chấm AutoML.

Nó sẽ tự động tìm kiếm giữa tất cả các mô hình khác nhau và điều chỉnh nó để cung cấp cho chúng tôi những gì tốt nhất,

đầu ra tốt nhất cho mô hình của chúng tôi.

Bây giờ, như bạn có thể thấy, nó đang sử dụng nhiều loại dữ liệu khác nhau.

Và sau đó anh ấy hoàn thành việc tìm kiếm và kết thúc ngắn gọn sau 0,1 5 giây.

Tốt nhất lúc đó là phân loại ngẫu nhiên bằng máy tính và nhật ký quy trình tốt nhất.

Cái này là 0,04.

Bây giờ chúng ta sẽ xem.

Ngoài ra, chúng ta cũng có thể xem thứ hạng, như bạn có thể thấy, có các mô hình và kiểu dáng khác nhau

nó cho chúng tôi những điểm số khác nhau, điểm CV, điểm xác nhận.

Và một điều nữa, như bạn có thể thấy rằng chúng ta có a.

Chúng tôi có điểm xác nhận và tốt hơn 80% so với 97%.

Và vì xác thực chéo là 0,03, khá thấp và có nghĩa là điểm CV là 42.

Cái nào ít nhất và cái này là cao nhất.

Như vậy có thể thấy mô hình phân loại rừng ngẫu nhiên bằng máy tính là mô hình tốt nhất hiện nay.

Chúng ta sẽ xem đâu là đường ống tốt nhất.

Đường ống có nghĩa là nó sẽ cung cấp cho chúng tôi tất cả các chi tiết được sử dụng như máy tính, máy tính nào được sử dụng

đã sử dụng, trình phân loại nào đã được sử dụng, tham số nào chúng tôi đã sử dụng và sẽ lưu trữ nó trong một quy trình dựa trên mô hình.

Bây giờ, nếu muốn mô tả chi tiết về mô hình này, chúng ta có thể sử dụng lệnh hoặc để mô tả

đường ống.

Chúng tôi sẽ sử dụng xếp hạng tự động và chúng tôi sẽ chọn nhóm đầu tiên là khu rừng ngẫu nhiên theo lệnh, bằng cách

theo lệnh, theo lệnh.

Dấu chấm ghi bằng không.

Nó Mô tả cho chúng tôi mọi thứ chúng tôi có thể.

Mô tả một máy tính Ba Lan ngẫu nhiên với thông tin chi tiết về những thứ chúng tôi sử dụng sẽ bị mất nhật ký,

điểm nhị phân, điểm AUC, điểm Ganey và ứng dụng tiền mùa giải và như bạn có thể thấy, các loại điểm khác nhau

đã cho.

Bây giờ nếu chúng ta muốn xem chúng ta đạt được bao nhiêu điểm về các mục tiêu như AOC và Precision, nó sẽ

tùy thuộc vào chủ nhân của bạn hoặc nút miền.

Người khác đang có điểm kiến thức miền mà anh ta phải thi sẽ đạt điểm khác

và chuyển đổi nó thành cơ sở dữ liệu.

Như bạn có thể thấy, điểm AOC có độ chính xác xấp xỉ là 91%, F là 86%.

Chúng tôi có độ chính xác là 87,5% và 84,4%.

Như bạn có thể thấy, điều này tốt hơn và chính xác hơn nhiều so với các mẫu chúng tôi sử dụng trong máy

học tập.

Bây giờ, nếu chúng ta giả sử nếu một nhà tuyển dụng nói rằng chúng ta phải sử dụng một mục tiêu nhất định, chẳng hạn như

Hãy xem, bây giờ chúng ta phải sử dụng điểm để có thể huấn luyện mô hình của mình bằng điểm đó, chúng ta sẽ làm gì, chúng ta sẽ sử dụng

cùng một tìm kiếm AutoML, chúng tôi sẽ cung cấp dữ liệu và chúng tôi sẽ chọn mục tiêu của mình là AUC.

Sau đó, chúng ta sẽ thấy các mục tiêu bổ sung đã chọn nếu có độ chính xác.

Điều này sẽ đào tạo mô hình của chúng tôi dựa trên đó, dựa trên thứ hạng và mô hình đang có

điểm cao nhất sẽ được cung cấp.

Sẽ mất một chút thời gian vì nó tìm kiếm tất cả các mô hình khác nhau và sau đó sẽ được cung cấp mô hình đó,

như bạn có thể thấy.

Nó vẫn đang tìm kiếm.

Và bây giờ chúng ta có được bản trích xuất mô hình được phân loại bằng máy tính.

Và điều này đã mang lại cho chúng tôi trường AUC cao nhất.

Chúng ta sẽ xem thứ hạng như chúng ta có thể thấy, ba phân loại bổ sung được đưa ra sau khu rừng ngẫu nhiên.

Phân loại rừng ngẫu nhiên

Bây giờ chúng ta có thể chọn cái này.

Chúng tôi có thể mô tả mô hình hoạt động tốt nhất của mình với sự trợ giúp của AutoML để mô tả Đường ống.

Và sau đó nó sẽ mô tả tất cả những thứ khác nhau được lấy điểm EF một cách chính xác và

những thứ khác nhau sẽ lưu trữ điều này trong một đường dẫn tốt nhất.

Bây giờ chúng ta có thể làm gì.

Chúng ta sẽ có điểm.

Chúng ta sẽ có số điểm là

Những gì bạn thấy là những gì chúng tôi có bây giờ.

Như bạn có thể thấy, chúng tôi đạt được khoảng 91,55%, tốt hơn nhiều so với các mô hình trước đó.

Bây giờ, chúng tôi đã xây dựng một mô hình dựa trên sự trợ giúp của một kỹ thuật trong đó độ chính xác của

khoảng 91%.

Bây giờ điều chúng ta phải làm là xem liệu mô hình trong tệp dưa chua có thể làm được những gì bạn có thể làm, nhưng bạn có thể làm điều này

bằng đường ống tốt nhất.

Đường ống tốt nhất là thứ mà chúng tôi lưu trữ và yêu cầu Đường ống, không nói mô hình, không nhặt.

Và để tải mô hình của chúng ta, chúng ta có thể thực hiện việc này bằng mô hình cuối cùng hoặc nhập mô hình tải dot Pickle và chúng ta

có thể dự đoán kết quả với sự trợ giúp của điều này bây giờ sẽ dự đoán kết quả.

Như bạn có thể thấy, chúng tôi đang nhận được các xác suất kết quả khác nhau đối với dữ liệu thử nghiệm đầu tiên,

xác suất của một trong đó là.

Rằng nó không có nhiều.

Không phải xác suất xảy ra là khoảng 65%.

Một đầu ra có xác suất lớn nhất.

Chúng ta có thể xem xét điều đó cho dữ liệu thứ hai.

Một là có xác suất 97%.

Và theo danh sách, đây là chủ đề của chúng ta về cách chúng ta có thể dự đoán công cụ dự đoán dữ liệu hoặc tạo mô hình

thậm chí với sự trợ giúp của kỹ thuật này, bạn đã học được cách áp dụng các phương pháp học máy khác nhau

thư viện và sau đó so sánh nó với các kỹ thuật tự động, tất cả mã và liên kết và mã hóa

bản trình bày và các tập tin sẽ được cung cấp cho bạn.

Bạn có thể tham khảo mã này và tự thực hành để đạt được hiệu quả tối đa.