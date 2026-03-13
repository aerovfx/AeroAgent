# 03 - Giám sát đào tạo và xác nhận

---

- [Giảng viên] Bây giờ chúng ta đã thành công rồi.

dữ liệu của chúng tôi được xử lý trước

và sau đó xây dựng mô hình học máy của chúng tôi,

đã đến lúc chuyển sang phần thú vị,

đào tạo mô hình tensorflow của chúng tôi và sau đó tiếp tục

và nhìn vào hiệu suất của nó một cách trực quan.

Điều này sẽ cho chúng ta một sự hiểu biết rõ ràng

về việc mô hình của chúng tôi học tập tốt như thế nào

và nơi nó có thể phải đối mặt với những thách thức.

Vì vậy, chúng ta hãy tiếp tục và gặp nhau tại trang chính của Codespaces.

Và từ đây, chúng ta sẽ tìm thư mục src

rồi nhấp vào tệp Python 03_03_begin,

chỉ ra rằng đây là tệp Python bắt đầu

mà chúng ta sẽ bắt đầu.

Và sau đó, chúng ta sẽ kết thúc bằng tệp 03_03_ và Python.

Vì vậy, chúng ta sẽ tiếp tục và nhập thư viện của mình như bình thường,

thư viện tensorflow, matplotlib và sklearn,

tiếp theo là tải dữ liệu từ

lấy lại tập dữ liệu get_california_housing.

Chúng tôi sẽ tiếp tục thực hiện các phần thử nghiệm trên tàu

để tạo các phần tách thử nghiệm tàu của chúng tôi,

cũng như dữ liệu xác nhận.

Tiếp theo, chúng ta sẽ tiếp tục và chia tỷ lệ dữ liệu ở đây.

Một lần nữa, chúng ta sẽ có một bộ chia tỷ lệ.

Chúng ta sẽ fit_transform trên chuyến tàu X,

tiếp theo là chỉ chuyển đổi khi xác thực X và kiểm tra X,

tiếp theo là xác định mô hình.

Ở đây, chúng tôi đã xác định một mô hình trước đây,

vì vậy hãy tiếp tục và xem xét nó bao gồm những gì.

Trước hết, chúng ta bắt đầu với tf.keras.layers.Dense

với 30 tế bào thần kinh,

và sau đó chúng tôi cung cấp năng lượng kích hoạt của relu

và sau đó chúng ta sẽ cung cấp cho nó một hình dạng đầu vào.

Vì vậy, lớp ẩn ở đây là lớp đầu tiên,

mà chúng tôi cung cấp cho 30 tế bào thần kinh.

Nó đưa tính phi tuyến tính vào mô hình.

Nó cho phép nó học các mẫu phức tạp ở đây.

Vì chúng ta đang dự đoán một giá trị liên tục,

chúng tôi cung cấp một nơ-ron duy nhất cho lớp đầu ra, điều này là ổn.

Sau đó, chúng tôi sử dụng Mean_squared_error cho phần mất mát,

và đối với trình tối ưu hóa,

chúng tôi lại sử dụng phương pháp giảm độ dốc ngẫu nhiên.

Vì vậy, hãy tiếp tục và bắt đầu từ đây

và một lần nữa, đào tạo mô hình

tiếp theo là trực quan hóa hiệu suất của mô hình.

Vì vậy, hãy tiếp tục và nói Đào tạo mô hình ở đây.

Và sau đó chúng ta sẽ tiếp tục

và tạo một biến gọi là history.

Và sau đó chúng ta sẽ nói model.fit,

và những gì chúng tôi cung cấp ở đây bây giờ là X_train, y_train

và sau đó là số lần lặp lại,

nói cách khác, kỷ nguyên, sẽ là 20,

theo sau là validation_data,

mà chúng ta đã chuẩn bị ở trên rồi phải không?

Vì vậy, đối với dữ liệu xác thực, chúng ta sẽ cung cấp những gì?

Chúng tôi sẽ đưa ra xác nhận X_

và sau đó y_ xác nhận.

Thế thôi.

Vì vậy, đây là những gì chúng tôi làm để đào tạo mô hình một dòng.

Tiếp theo là điểm chính của phiên

là làm thế nào để chúng ta hình dung được mô hình đào tạo?

Điều này rất cần thiết để có thể nhìn vào mô hình đào tạo

và xem chúng ta có thể cải thiện nó như thế nào, chúng ta có thể phân tích nó như thế nào.

Trước hết, chúng ta sẽ gọi âm mưu,

và rồi chúng ta sẽ có lịch sử,

và sau đó chúng ta sẽ có lại lịch sử,

và chúng ta sẽ gọi sự mất mát ở đây

và chúng tôi sẽ gắn nhãn nó là Mất tập luyện.

Tiếp theo chúng ta sẽ tiếp tục

và tạo ra sự mất xác nhận trong cốt truyện.

Vì vậy, một lần nữa, plt.plot mở ngoặc đơn history.history

và sau đó chúng tôi sẽ đưa ra thông tin mất xác thực ở đây,

tiếp theo là hãy đặt nhãn cho nó để dễ đọc

và chúng tôi sẽ đánh giá cao những nhãn này

khi chúng ta nhìn vào nó trong một giây.

Mất xác thực.

Thực hiện theo bằng cách đặt tiêu đề cho cốt truyện của chúng tôi

để chúng tôi biết chúng tôi đang làm việc với cái gì,

vì vậy hãy làm cho tiêu đề rõ ràng.

Hãy gọi nó là Mất đào tạo và xác thực.

Vì vậy, điều đó sẽ khá giải thích.

Tuy nhiên, có lẽ cũng vậy, hãy tiếp tục và thêm Epoch

để chúng ta biết đó chính là điều chúng ta đang làm việc, phải không?

Vì vậy, đây là tiêu đề và chúng tôi có nhãn x.

Vì vậy, hãy gọi chúng là xlabels.

Đó là thời đại mà chúng tôi làm việc cùng.

Và sau đó là plt.ylabels.

Đó là sự mất mát mà chúng tôi đang giải quyết.

Chúng ta sẽ gọi plt.legend.

Và sau đó chúng ta hãy tiếp tục và lưu hình này như bình thường.

Hãy nhớ rằng khi chúng ta làm việc với không gian mã,

cốt truyện.show không hoạt động tại thời điểm quay video này.

Nó có thể thay đổi trong tương lai,

nhưng plt.show không hoạt động trên Codespaces.

Vì vậy, có những cách giải quyết,

nhưng không cần những sự phức tạp đó.

Chúng tôi sẽ tiếp tục và lưu nó vào thư mục đầu ra của chúng tôi.

Và lợi ích khác của việc lưu nó là gì

trong thư mục đầu ra chúng ta có thể mở nó bất cứ lúc nào phải không?

Chúng ta có thể quay lại thăm nó và tiếp tục phân tích nó

trong tương lai.

Vì vậy, chúng tôi có một kỷ lục.

Hãy tiếp tục và nhanh chóng xem những gì chúng ta đã làm.

Vì vậy, chúng tôi đã tạo ra một biểu đồ cho phép chúng tôi hình dung

người mẫu đang học tốt như thế nào

và nơi nó có thể quá phù hợp.

Vì vậy, chúng tôi đã tiếp tục và tạo ra sự mất mát lịch sử cốt truyện PLT,

và sau đó là Mất đào tạo và sau đó là Mất xác thực.

Đó là sự mất xác thực mà chúng tôi đang giải quyết.

Chúng tôi đặt tên cho nó.

Sau đó chúng tôi đưa ra nhãn X và nhãn Y

và chúng tôi đã lưu hình này.

Đó là một số bước chúng tôi đã trải qua.

Tiếp theo, hãy tiếp tục và đánh giá mô hình trên tập kiểm tra.

Để làm được điều đó, chúng ta sẽ gọi mse_test, kiểm tra lỗi bình phương trung bình,

mô hình.đánh giá,

và chúng tôi cho nó X_test, y_test, phải không?

Vì vậy, điều đó sẽ mang lại cho chúng tôi mse_test và chúng tôi sẽ tiếp tục

và in kết quả của mse_test này.

Vậy là Lỗi bình phương trung bình trên tập kiểm tra, phải không?

Và chúng ta sẽ tiếp tục nói mse_test. Vì vậy, đó là nó.

Vì vậy, nó sẽ giúp chúng tôi in nó cuối cùng.

Vì vậy, đây là nó.

Vì vậy, chúng tôi đã tạo ra chương trình đào tạo

và quá trình giám sát xác nhận ở đây.

Tại sao điều đó lại quan trọng?

Điều quan trọng là cách mô hình của chúng tôi hoạt động như thế nào

qua các lần lặp lại, qua các kỷ nguyên.

Vì vậy, đây gần như giống hệt mã Python

với, một lần nữa, nhìn vào khung bên trái

trong thư mục src, 03_03_ và tệp Python.

Vì vậy, hãy tìm nó và mở nó ra và so sánh nó

với mã bạn đã viết.

Hãy chắc chắn rằng nó phù hợp.

Nếu không, có lẽ hãy dành thêm một chút thời gian

và cố gắng hiểu những gì chúng tôi đang làm ở đây

khi chúng ta hình dung cụ thể quá trình đào tạo,

và sau đó đánh giá mô hình trên tập kiểm tra.

Tôi sẽ tiếp tục và chạy nó

với hình tam giác nhỏ này ở hướng thẳng đứng.

Nó sẽ trải qua hơn 20 lần lặp, 20 kỷ nguyên.

Sẽ mất vài phút, không quá lâu,

và nó sẽ lưu một tệp đầu ra cho chúng tôi,

ở dạng PNG.

Chúng ta sẽ tiếp tục và mở nó

và sau đó chúng tôi sẽ thực hiện một số phân tích về nó.

Vì vậy, Sai số bình phương trung bình của chúng tôi trên Tập kiểm tra là khoảng 0,35

nếu chúng ta làm tròn nó.

Vì vậy, đây là MSE của chúng tôi trên tập thử nghiệm.

Bây giờ chúng ta hãy tiếp tục và xem hình dung.

Vì vậy, tôi sẽ tìm thư mục đầu ra,

và sau đó tôi sẽ bấm vào khung bên trái, thư mục đầu ra,

và sau đó nó sẽ hiển thị ở đây

03_03_training_validation_loss.png.

Vì vậy, đây là Mất mát về đào tạo và xác thực của chúng tôi qua các Kỷ nguyên.

Vì vậy, hãy tiếp tục và dành chút thời gian để phân tích nó.

Một lần nữa, như một lời nhắc nhở,

mặc dù chúng tôi đặt trạng thái ngẫu nhiên,

vẫn còn một số sự ngẫu nhiên xảy ra trong dữ liệu,

nó được phân chia như thế nào và nó hoạt động như thế nào,

và biểu đồ của bạn có thể hơi khác so với biểu đồ của tôi.

Và nếu bạn chạy tập lệnh nhiều lần,

bạn thậm chí có thể thấy kết quả hơi khác một chút,

và điều đó không sao cả, và điều đó được mong đợi.

Vì vậy, nhìn vào biểu đồ này,

chúng ta có đường màu xanh là mất huấn luyện

và đường màu cam là mất xác nhận qua các kỷ nguyên,

mà chúng ta có 20 kỷ nguyên, nói cách khác là các lần lặp.

Và trên trục Y, chúng ta có phần lỗ.

Vì vậy, khi chúng ta nhìn vào đường màu xanh,

đó là sự mất mát trong quá trình đào tạo,

mất mát đào tạo giảm nhanh chóng trong vài kỷ nguyên đầu tiên

và sau đó ổn định gần bằng không.

Điều này chỉ ra rằng mô hình đã nhanh chóng học được

để phù hợp với dữ liệu đào tạo rất tốt,

đạt được tỷ lệ lỗi thấp trên tập huấn luyện.

Tiếp theo là mất xác nhận.

Vì vậy, điều này được thể hiện bằng đường màu cam.

Mất xác nhận cũng tăng nhanh,

nhưng nó bắt đầu ở một giá trị cao hơn nhiều

so với sự mất mát đào tạo.

Tương tự như việc mất huấn luyện,

mất xác nhận giảm đáng kể

trong vài kỷ nguyên đầu tiên và ổn định ở một giá trị

gần đến mức mất đào tạo.

Thực tế là việc mất xác nhận theo sát

sự mất mát đào tạo sau vài kỷ nguyên đầu tiên

cho thấy mô hình đang khái quát hóa tốt

và không quá phù hợp với dữ liệu huấn luyện.

Vì vậy, cả tổn thất đào tạo và xác nhận đều giảm mạnh

giữa vài kỷ nguyên đầu tiên,

chỉ ra rằng mô hình đã nhanh chóng học được từ dữ liệu

và điều chỉnh các thông số của nó một cách hiệu quả.

Sự mất mát xác nhận theo sát sự mất mát đào tạo

sau thời gian điều chỉnh ban đầu,

ngụ ý rằng mô hình khái quát hóa tốt

tới những dữ liệu chưa được nhìn thấy.

Sự ổn định của cả hai tổn thất sau một vài kỷ nguyên

chỉ ra rằng mô hình đã hội tụ,

có nghĩa là việc đào tạo thêm khó có thể xảy ra

để dẫn đến bất kỳ cải tiến đáng kể nào về hiệu suất.

Vì vậy, quá trình đào tạo này gợi ý rằng

mô hình đã có thể học một cách hiệu quả

từ dữ liệu huấn luyện

và khái quát hóa dữ liệu xác nhận,

dẫn đến giá trị tổn thất thấp cho cả hai.

Vì vậy, không có sự khác biệt giữa đào tạo

và tổn thất xác nhận là một dấu hiệu tích cực

chỉ ra rằng mô hình không quá phù hợp.

Sự hội tụ nhanh chóng cũng cho thấy

rằng kiến trúc mô hình đã chọn và bước huấn luyện

rất phù hợp với vấn đề hiện tại.

Vì vậy, tóm lại, trong phần này,

chúng ta đã thấy cách giám sát quá trình đào tạo, mất xác thực

sau khi tạo mô hình

và làm thế nào để đưa ra kết luận từ nó.

Hãy tiếp tục.