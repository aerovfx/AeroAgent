# 69 - CNN về Đánh giá mô hình MNIST bằng tiếng Anh

---

Chào mừng mọi người trở lại, và bài giảng này, chúng ta sẽ tập trung vào việc đánh giá mô hình mà chúng ta vừa

đã được đào tạo ở bài trước.

Hãy đi tới sổ ghi chép Sao Mộc của chúng ta và tiếp tục từ nơi chúng ta đã dừng lại.

Được rồi, chúng ta đang ở sổ ghi chép mà chúng ta đã dừng lại lần trước sau khi đào tạo mô hình.

Như mọi khi, điều chúng ta có thể làm là chúng ta có thể nói rằng tổn thất thực sự xảy ra trong trường hợp này, chúng ta sẽ nói.

Số liệu bằng PD, khung dữ liệu và cùng một mô hình.

Lịch sử, lịch sử và lý do tôi nói đến số liệu thay vì chỉ nói đến thua lỗ là vì chúng ta hãy nắm lấy

hãy xem lịch sử mà thuộc tính lịch sử thực sự trả về là gì, bởi vì tôi cũng đã nói hãy theo dõi

về độ chính xác ở đây, không chỉ mất mát.

Tôi nhận được thông tin về sự mất mát và độ chính xác của mình trên tập huấn luyện cũng như độ chính xác về xác thực, mất mát và xác thực của tôi,

có nghĩa là tôi có thể vẽ ra cả hai điều đó.

Vì vậy, thay vì vẽ biểu đồ các số liệu tương tự, việc vẽ biểu đồ cả tổn thất và độ chính xác sẽ không có ý nghĩa gì.

Nếu không, bạn sẽ có được một âm mưu trông như thế này.

Thay vào đó, bạn nên vẽ biểu đồ mất mát so với xác nhận, mất mát và độ chính xác với xác nhận, độ chính xác.

Vì vậy, những gì chúng tôi sẽ làm là chuyển qua đây một danh sách với phần mất mát và.

Các luật xác thực sẽ tiếp tục và vạch ra những điều đó và chúng ta có thể thấy sự mất mát trong quá trình đào tạo bắt đầu diễn ra như thế nào

xuống, nhưng có vẻ như tổn thất xác nhận về cơ bản đã bắt đầu tăng trở lại.

Đó là lý do tại sao chúng tôi dừng việc đào tạo Époque.

Và nếu muốn, chúng tôi cũng có thể thấy sự thay đổi về độ chính xác để chúng tôi có thể thấy độ chính xác so với mức xác thực

độ chính xác.

Lưu ý rằng các số liệu đánh giá về cơ bản chỉ có dấu gạch dưới Vattel được thêm vào trước chúng.

Và chúng ta có thể thấy độ chính xác của chúng ta tiếp tục trên tập huấn luyện.

Vậy là tốt rồi, gần như đạt độ chính xác trăm phần trăm, nhưng Revalidation cho biết nó bắt đầu lên cấp

tắt khi chúng tôi được đào tạo.

ĐƯỢC RỒI.

Vì vậy, trong trường hợp bạn muốn nhớ những số liệu nào có sẵn trong mô hình của mình, bạn có thể nói model

số liệu, tên và tôi sẽ báo cáo lại số liệu thực tế, độ mất và độ chính xác của chúng.

Và nếu bạn thực sự muốn lấy số liệu về độ chính xác lozar này trên bất kỳ tập hợp dữ liệu nào, chúng tôi có thể nói

mô hình đánh giá và chúng tôi có thể vượt qua bài kiểm tra X và bài kiểm tra phân loại Y, hãy tiếp tục và nói dài dòng là

bằng không.

Vì vậy, bạn không thấy hoạt động thực tế của dữ liệu này thông qua mô hình và về cơ bản nó sẽ đánh giá

trả lại tổn thất và độ chính xác trên tập kiểm tra.

Và thật hợp lý khi đây là 0 điểm 0 4 và 0 điểm 9 8, bởi vì nếu chúng ta lấy

hãy nhìn lại điều này, lần mất xác nhận cuối cùng trong bài kiểm tra, đó là 0,04 và 0

điểm chín tám.

Vì vậy, về cơ bản, đây phải là những con số giống hệt như vòng lặp cuối cùng hoặc ít kỷ nguyên hơn.

Và đó là đánh giá về bộ thử nghiệm này.

Bạn cũng có thể làm tương tự cho trung tâm đào tạo và báo cáo lại các con số, độ hao hụt và độ chính xác.

Được rồi, hãy nhớ lại, độ chính xác chỉ là phép tính bạn nhận được bao nhiêu phần trăm thôi, phải không?

sự mất mát.

Đây là kết quả của hàm entropy chéo phân loại này.

Bây giờ chúng ta đã hiểu nó hoạt động như thế nào trong quá trình đào tạo kỷ nguyên, hãy tiếp tục và lấy

báo cáo phân loại trong ma trận nhầm lẫn trên dữ liệu thử nghiệm của chúng tôi.

Chúng tôi có thể thực hiện việc này từ Escalon để nhập số liệu báo cáo phân loại và chúng tôi cũng có thể nhập sự nhầm lẫn

ma trận.

Vì vậy, tôi khuyên chúng ta sẽ tiếp tục và lấy các dự đoán từ bộ thử nghiệm của mình.

Và trong trường hợp này, chúng tôi muốn dự đoán các lớp dựa trên thông tin và tập dữ liệu thử nghiệm.

Và bây giờ chúng ta đã có dự đoán của mình.

Những gì chúng ta có thể làm là nhớ lại bài kiểm tra Whitecap đó.

Nó vẫn ở dạng mười nghìn x mười, vì vậy điều chúng ta muốn làm là đảm bảo rằng chúng ta đang so sánh

điều này một cách chính xác để kiểm tra lý do, đó là những nhãn thực tế này.

Vì vậy, để đánh giá thực tế, chúng tôi cần phải vượt qua và không còn kiểm tra những phân loại này nữa.

Vì vậy, chúng tôi sẽ nói báo cáo phân loại Prince, so sánh giá trị thử nghiệm thực với giá trị dự đoán của chúng tôi và

chúng ta có thể thấy báo cáo phân loại về cơ bản hiển thị cho bạn độ chính xác thu hồi điểm F1 cho mỗi lớp.

Vậy điều đó sẽ thực hiện như thế nào với số không, số một, v.v.?

Và bạn có thể thấy nó hoạt động khá tốt ở hầu hết các lớp với độ chính xác đến 99%.

Và nếu bạn muốn tìm hiểu sâu hơn về vấn đề này, bạn có thể tạo ma trận nhầm lẫn dựa trên cùng dữ liệu đó.

Tại sao phải kiểm tra và dự đoán?

Và các bạn có thể xem kết quả tại đây, nếu muốn hình dung điều này các bạn cũng có thể sử dụng Seabourne để biến đổi

điều này nên chúng ta có thể gọi Seabourne là S.A.S. và sau đó gọi một bản đồ nhiệt.

Về cơ bản, nó sẽ tô màu các kết quả mà chúng tôi có ở đây để bạn có thể lấy cái này và sau đó dán vào

kết quả và chúng ta có thể làm cho con số này lớn hơn một chút và nói điều gì đó như kích thước cố định bằng 10 x 6.

Và bạn có thể chạy nó và chúng tôi sẽ hiển thị cho bạn bản đồ nhiệt, chỉ cần thêm các chú thích bằng true là được

Tôi có thể thấy những giá trị đó ở trên nó.

Vì vậy, đó là cách bạn có thể nhanh chóng hình dung nó.

Ở đây không có nhiều thông tin lắm vì hiệu suất của tất cả các con số đều tốt như thế nào.

Được rồi, đó là một cách để hình dung nó.

Điều cuối cùng bạn sẽ đề cập đến là làm cách nào để dự đoán một hình ảnh?

Vậy là ai đó đã cho bạn hình ảnh của một con số.

Vì vậy, ví dụ, giả sử số của tôi bằng.

Kiểm tra X bằng không.

Vì vậy, nếu tôi chỉ hiển thị số của mình ở đây, hãy đảm bảo rằng tôi đã làm đúng, số của tôi sẽ được định hình lại

đến hai mươi tám x hai mươi tám.

Thế đấy.

Đây là số của tôi.

Đó là Reshad, 28 x 28, nên tôi có thể hình dung ra nó.

Rõ ràng đó là số bảy.

Vậy nếu ai đó đưa cho bạn số điện thoại duy nhất này của tôi, bạn sẽ thực sự dự đoán nó như thế nào?

Vâng, bạn sẽ nói mô hình.

Dự đoán các lớp, và điều duy nhất bạn phải biết là việc định hình lại này, vì vậy bạn sẽ

nói không, không định hình lại, và sau đó hình dạng sẽ trở thành kích thước lô.

Về cơ bản, số lượng hình ảnh, chiều rộng.

Chiều cao và sau đó là các kênh màu, vì vậy trong trường hợp của chúng tôi, đó là một hình ảnh duy nhất.

Vậy đó là một, 28 x 28.

Và sau đó có một kênh màu.

Đó là lý do tại sao tôi cần định hình lại nó theo cách đó, bởi vì đó là hình dạng mà nó đã được huấn luyện, dựa trên

thực tế là chúng tôi đang cung cấp nhiều số cùng một lúc.

Chúng ta sẽ tiếp tục dự đoán các lớp học ở đây rồi quay lại.

Nó dự đoán rằng đó là số bảy, điều này hợp lý vì ở đây tôi có thể thấy rõ ràng đó là số bảy.

Được rồi, mạng nơ ron tích chập hoạt động rất tốt trên tập dữ liệu này.

Bây giờ chúng ta đã biết cách làm việc với hình ảnh thang độ xám hoặc chúng ta sắp mở rộng kiến ​​thức của mình.

Và trong loạt bài giảng tiếp theo, chúng ta sẽ đi theo con đường tương tự.

Nhưng làm việc trên dữ liệu màu với ba kênh màu đỏ, lục và lam.

Tôi sẽ gặp bạn ở đó.