# 04 - Thước đo thành công

---

- [Giảng viên] Trong phần này,

chúng tôi sẽ mở rộng mô hình TensorFlow trước đây của mình

bằng cách thêm nhiều số liệu hơn vào nó.

Vì vậy, điều này sẽ cho chúng ta những hiểu biết sâu sắc hơn

vào hiệu suất của mô hình.

Chúng tôi sẽ tiếp tục làm việc với bộ dữ liệu Nhà ở California

và mở rộng phân tích của chúng tôi bằng cách kết hợp trực quan hóa

và các chỉ số đánh giá bổ sung

như lỗi tuyệt đối trung bình, MAE

và sai số bình phương trung bình gốc, RMSE.

Vì vậy, để bắt đầu, hãy mở các không gian mã

rồi tìm thư mục src từ khung bên trái.

Và sau đó chúng ta sẽ nhấp vào tệp python 03_04_begin.

Vì vậy, trước khi bắt đầu, chúng ta hãy tiếp tục và xem xét

và nhập từng thư viện một.

NumPy cho các phép toán số,

gấu trúc để thao tác và phân tích dữ liệu,

matplotlib.pyplot để tạo trực quan hóa,

TensorFlow cho xây dựng

và huấn luyện mô hình mạng lưới thần kinh,

sklearn.dataset để tìm nạp bộ dữ liệu Nhà ở California,

sklearn.model_selection

để chia dữ liệu thành huấn luyện,

xác nhận và bộ kiểm tra,

sklearn.preprocessing để chia tỷ lệ dữ liệu.

Vì vậy, sau khi chúng tôi nhập thư viện của mình,

chúng tôi tiếp tục và lấy tập dữ liệu.

Để làm được điều đó, chúng tôi sử dụng Fetch_california_housing

và chúng tôi gán nó cho biến nhà ở.

Bây giờ, bộ dữ liệu Nhà ở California đã được tải

và chuyển đổi thành DataFrame của gấu trúc

để thao tác dễ dàng hơn.

Thông báo trong dòng này, housing_df["MedHouseVal"],

biến mục tiêu, MedHouseVal,

đại diện cho giá trị ngôi nhà trung bình,

được thêm vào DataFrame.

Tiếp theo, chúng tôi tiếp tục và chia tập dữ liệu.

Hãy tiếp tục và thu nhỏ cửa sổ bên trái.

Vì vậy, tập dữ liệu được chia thành đào tạo,

xác nhận và bộ kiểm tra,

sau đó chúng tôi theo dõi nó bằng cách chia nhỏ hơn nữa tập huấn luyện

vào tập huấn luyện và xác nhận.

Ở đây, trong phạm vi phần dữ liệu,

các tính năng được chia tỷ lệ bằng StandardScaler

để chuẩn hóa chúng, giúp cải thiện hiệu suất của mô hình

bằng cách đảm bảo tất cả các tính năng đóng góp như nhau.

Tiếp theo, chúng ta tiếp tục và xem xét việc khám phá dữ liệu ban đầu

và trực quan hóa.

Vì vậy, phần này chúng ta tiếp tục

và thực hiện một bản tóm tắt thống kê cơ bản về tập dữ liệu,

được tạo bằng hàm mô tả.

Vì vậy, chúng ta tiếp tục và nói housing_df.describe().transpose()

và chúng tôi tiếp tục chuẩn bị đồ thị cho biểu đồ.

Vì vậy, biểu đồ được vẽ ở đây

để hình dung sự phân bố của từng tính năng

trong tập dữ liệu.

Sau đó, chúng ta tiếp tục và lưu hình này dưới dạng tệp PNG

trong thư mục đầu ra.

Vì vậy, đây là nơi chúng ta sẽ bắt đầu viết mã của chương này,

và hãy mở lại khung bên trái

bằng cách nhấp vào biểu tượng này ở đây, biểu tượng thám hiểm.

Vì vậy chúng ta sẽ bắt đầu từ file python 03_04_begin.

Chúng tôi thêm mã mới của chúng tôi ở đây,

và chúng ta sẽ kết thúc trong tệp python 03_04_end.

Vì vậy hãy tiếp tục và chạy tập tin bắt đầu này,

và chúng ta sẽ có thể

để tạo ra sự phân bổ dữ liệu nhà ở ở đây,

và sau đó chúng ta sẽ chuyển sang các số liệu bổ sung tiếp theo.

Vì vậy, hãy nhấp vào thư mục đầu ra,

và chúng ta sẽ có thể thấy cốt truyện mới

mà chúng tôi vừa tạo,

đó là 03_04_housing_data_distribution.

Ở đây, chúng ta có thể thấy sự phân bổ dữ liệu nhà ở,

và hãy tiếp tục và phóng to từng tính năng một chút.

Vì vậy, biểu đồ chúng ta đang xem xét

cung cấp một hình ảnh trực quan về sự phân bố

các tính năng khác nhau từ bộ dữ liệu Nhà ở California.

Vì vậy, đây là một số quan sát.

Cái đầu tiên chúng ta đang xem xét

ở phía trên bên trái là thu nhập trung bình.

Vì vậy, viết tắt là MedInc.

Sự phân bố bị lệch phải

với hầu hết các hộ gia đình có thu nhập trung bình

từ hai đến năm.

Một số ít hộ gia đình

có thu nhập cao hơn đáng kể, nhưng họ là những người ngoại lệ.

Và ở hình giữa phía trên, chúng ta đang xem HouseAge.

Sự phân bố cho thấy mức chênh lệch tương đối đồng đều

từ 10 đến 50 năm,

nhưng có nhiều mức tăng đột biến ở một số độ tuổi nhất định,

có khả năng chỉ ra thời kỳ

phát triển nhà ở đáng kể.

Vì vậy, tiếp theo, chúng ta hãy nhìn vào hình AveRooms phía trên bên phải

và sau đó là hình ở giữa bên trái trên AveBedrms.

Vì thế khi chúng ta cùng nhau ngắm nhìn chúng,

chúng ta sẽ thấy rằng cả hai đặc điểm ở đây đều có độ lệch phải rất cao,

chỉ ra rằng hầu hết các ngôi nhà

có một số ít phòng và phòng ngủ.

Có một vài ngôi nhà

với số lượng phòng hoặc phòng ngủ cao bất thường,

nhưng như bạn có thể thấy, những điều này rất hiếm.

Tiếp theo, chúng ta đang xem xét dân số.

Sự phân bố dân số cũng bị lệch phải

với hầu hết các khu vực có dân số dưới 10.000 người.

Một số khu vực có dân số đông hơn đáng kể,

một lần nữa, đó là những ngoại lệ.

Tiếp theo, chúng ta đang xem xét công suất phòng trung bình.

Tính năng này bị lệch nhiều về bên phải

với hầu hết các giá trị được nhóm gần một,

chỉ ra rằng hầu hết các ngôi nhà

có số người trong mỗi hộ thấp.

Tiếp theo, chúng ta đang xem xét vĩ độ và kinh độ cùng nhau.

Những tính năng này cung cấp cái nhìn sâu sắc

vào sự phân bố địa lý của các ngôi nhà

với các cụm rõ ràng tương ứng

đến các khu vực cụ thể ở California.

Tiếp theo, chúng ta đang xem xét giá trị ngôi nhà trung bình.

Biến mục tiêu hơi lệch phải

với sự tập trung giá trị ngôi nhà xung quanh mức trung bình

và một số lượng đáng kể các ngôi nhà đạt đến giới hạn trên

trong phạm vi giá của tập dữ liệu.

Nhìn chung, biểu đồ cho thấy

nhiều đặc điểm trong tập dữ liệu này bị lệch phải,

có nghĩa là hầu hết các điểm dữ liệu đều tập trung

ở các giá trị thấp hơn với đuôi dài có giá trị cao hơn.

Chà, cái nhìn sâu sắc này có thể hữu ích

khi chúng tôi áp dụng các mô hình học máy

vì một số mô hình có thể yêu cầu chuyển đổi dữ liệu

để xử lý các phân phối sai lệch này một cách hiệu quả.

Vì trọng tâm chính của chúng tôi là các mô hình TensorFlow,

hãy mở lại tập tin python 03_04_begin một lần nữa

và hãy tiếp tục mã của chúng tôi

với việc tiếp tục tạo ra một mô hình.

Vì vậy, chúng tôi đã dừng việc lưu sơ đồ phân phối,

vì vậy chúng ta sẽ tiếp tục xác định mô hình ở đây.

Vì vậy, hãy tạo một mô hình mạng thần kinh đơn giản

bằng cách gán model = tf.keras.Sequential.

Và rồi từ đó trở đi,

chúng ta sẽ tiếp tục và tạo các lớp ở đây.

Đây sẽ là một mô hình mạng lưới thần kinh đơn giản

và nó sẽ có một lớp ẩn

với 30 nơ-ron sử dụng chức năng kích hoạt ReLU

và một lớp đầu ra với một nơ-ron duy nhất

bởi vì đây là một nhiệm vụ hồi quy.

Vì vậy, hãy tiếp tục và viết mã những gì chúng ta vừa nói.

Chúng ta sẽ mã hóa lớp đầu tiên là Dense

và sau đó chúng ta sẽ lấy 30, dấu phẩy.

Chức năng kích hoạt sẽ là ReLU,

vì vậy kích hoạt = "relu".

Sau đó chúng ta sẽ đi tiếp

và đặt input_shape là X_train.shape.

Sau đó chúng tôi sẽ đưa ra một

rồi đóng dấu ngoặc đơn, dấu phẩy.

Tiếp theo, chúng ta sẽ mã hóa lớp đầu ra của mình,

trong đó có một nơ-ron duy nhất,

vì vậy chúng ta sẽ nói tf.keras.layers.Dense

và sau đó chúng ta hãy tiếp tục và đưa ra một cái,

cho biết chúng ta có một lớp đầu ra với một nơ-ron duy nhất.

Tuyệt vời.

Vì vậy, sau khi chúng ta hoàn thành mô hình,

hãy tiếp tục và kiểm tra kích hoạt tf.keras.layer.Dense

và sau đó là input_shape.

Tất cả chúng ta đều xác định rõ mô hình.

Tiếp theo, chúng ta sẽ biên dịch mô hình,

vì vậy hãy tiếp tục và thực hiện điều đó, biên dịch mô hình

và sau đó chúng ta sẽ bắt đầu biên dịch bằng model.compile

và sau đó chúng ta sẽ nói mất mát =

"mean_squared_error",

trình tối ưu hóa = "sgd",

và sau đó chúng ta sẽ tiếp tục

và xác định các số liệu mới mà chúng tôi đang giới thiệu.

Vì vậy, số liệu sẽ là, hãy mở dấu ngoặc đơn

và bắt đầu viết ra danh sách số liệu.

Vì vậy nó sẽ có tf.keras.metrics.MeanAbsoluteError.

Vì vậy, hãy tiếp tục và bắt đầu với điều đó.

số liệu.MeanAbsoluteError(name ='mae'),

tf.keras.metrics.RootMeanSquaredError

và sau đó chúng ta sẽ gọi rmse.

Và cuối cùng, chúng ta sẽ có sai số bình phương trung bình,

vì vậy tf.keras.metrics.MeanSquaredError.

Hãy đi xuống. Nói tên ='mse'.

Được rồi.

Sau đó chúng ta sẽ đóng dấu ngoặc đơn,

dấu ngoặc vuông và sau đó là dấu ngoặc màu vàng.

Hãy lùi lại một bước và tóm tắt những gì chúng ta vừa làm.

Trước hết, chúng tôi biên soạn mô hình

với hàm mất có nghĩa là bình phương sai số.

Vì vậy, hàm mất mát đo lường

dự đoán của mô hình phù hợp như thế nào

các giá trị mục tiêu thực tế.

Về cơ bản nó hướng dẫn quá trình đào tạo

bằng cách cung cấp phản hồi về tính chính xác của chính mô hình.

Và chúng tôi đang sử dụng MSE làm trình tối ưu hóa ở đây

và sai số bình phương trung bình là một hàm mất mát được sử dụng phổ biến

trong các nhiệm vụ hồi quy.

Nó tính toán mức trung bình của sự khác biệt bình phương

giữa giá trị dự đoán và giá trị thực tế.

Chúng ta hãy tiếp tục và xem công thức cho nó.

Vì vậy, sai số bình phương trung bình là một hàm mất mát được sử dụng phổ biến

trong các nhiệm vụ hồi quy.

Nó tính toán mức trung bình của sự khác biệt bình phương

giữa giá trị dự đoán và giá trị thực tế.

Bạn có thể hỏi tại sao lại bình phương lỗi?

Trong khi bình phương các sai số đảm bảo rằng cả hai giá trị lớn

và các lỗi nhỏ được xem xét,

nhưng nó mang lại nhiều trọng lượng hơn cho những lỗi lớn hơn

bởi vì thuật ngữ lỗi là bình phương.

Điều này đồng nghĩa với việc người mẫu sẽ bị phạt nhiều hơn

đối với những lỗi lớn hơn,

khuyến khích nó đưa ra những dự đoán chính xác hơn.

Và ở đây, chúng ta đang xem xét công thức

trong đó y-sub-i là giá trị thực tế

và y-hat-sub-i là giá trị dự đoán

và n là số lượng điểm dữ liệu.

Và ở đây, chúng ta thấy công thức

trong đó y-sub-i là giá trị thực tế

và y-sub-i-hat là giá trị dự đoán

và n là số lượng điểm dữ liệu.

Tiếp theo, chuyển sang thước đo thành công khác.

Sai số tuyệt đối trung bình đo lường sự khác biệt tuyệt đối trung bình

giữa giá trị dự đoán và giá trị thực tế.

Thật đơn giản để giải thích

bởi vì nó đại diện cho sai số trung bình

trong cùng đơn vị với biến mục tiêu.

Tiếp theo là gốc nghĩa là lỗi bình phương, viết tắt là RMSE.

Vì vậy, điều này tương tự như MSE, sai số bình phương trung bình,

nhưng căn bậc hai được áp dụng để đưa đơn vị trở lại

có cùng tỷ lệ với biến mục tiêu.

RMSE nhạy cảm hơn với các lỗi lớn hơn MAE,

đó là lỗi tuyệt đối, làm cho nó hữu ích

khi lỗi lớn đặc biệt không mong muốn.

Và ở đây, chúng ta có thể thấy công thức của RMSE.

Và quay trở lại mã của chúng tôi,

hãy xem lại trình tối ưu hóa mà chúng tôi đã chọn.

Chúng tôi đang sử dụng SGD, phương pháp giảm độ dốc ngẫu nhiên.

Đây là một kiểu giảm độ dốc

nơi trọng số của mô hình được cập nhật

lặp đi lặp lại bằng cách sử dụng các tập hợp con dữ liệu ngẫu nhiên nhỏ.

Chúng ta có thể gọi chúng là những đợt nhỏ

thay vì toàn bộ tập dữ liệu cùng một lúc.

Vậy SGD hoạt động như thế nào, đối với mỗi lô nhỏ, độ dốc,

nói cách khác, đạo hàm riêng của hàm mất mát

đối với mỗi trọng lượng, được tính toán.

Các trọng số sau đó được cập nhật

theo hướng ngược lại với gradient để giảm tổn hao.

Quá trình lặp lại cho mỗi lô nhỏ

và qua nhiều kỷ nguyên, nhiều lần lặp lại,

đầy đủ đi qua tập dữ liệu.

Và bạn có thể hỏi, điều đó tốt, nhưng tại sao chúng ta lại sử dụng nó?

Nó hiệu quả về mặt tính toán

bởi vì nó không cần xử lý

toàn bộ tập dữ liệu cùng một lúc,

làm cho nó nhanh hơn và phù hợp với các tập dữ liệu lớn.

Nó cũng giới thiệu một số tính ngẫu nhiên,

có thể giúp thoát khỏi mức tối thiểu cục bộ trong quá trình tối ưu hóa.

Vì vậy, sau lần xem xét này,

hãy tiếp tục và tiếp tục với mã của chúng ta.

Tiếp theo, chúng ta sẽ tiếp tục và đào tạo mô hình,

vậy chúng ta hãy tiếp tục và huấn luyện mô hình.

Vì vậy, điều này sẽ liên quan đến việc điều chỉnh trọng số của nó

để giảm thiểu hàm mất mát mà chúng ta vừa nói đến.

Vì vậy chúng ta sẽ tiếp tục

và tạo lịch sử = model.fit,

và sau đó chúng tôi sẽ cung cấp X_train, y_train.

Một lần nữa, chúng ta sẽ cung cấp các kỷ nguyên là 20.

Đây là sự lặp lại.

Và sau đó chúng tôi sẽ cung cấp validation_data=(X_valid, y_valid)

Vì vậy, việc đó sẽ đảm nhiệm việc đào tạo mô hình cho chúng ta.

Vì vậy, khi chúng tôi đưa ra 20 kỷ nguyên,

điều này có nghĩa là toàn bộ dữ liệu huấn luyện được sử dụng 20 lần

để cập nhật trọng số.

Và dữ liệu xác nhận được sử dụng

để theo dõi hiệu suất của mô hình

trên dữ liệu chưa nhìn thấy trong quá trình đào tạo.

Điều này giúp phát hiện việc trang bị quá mức.

Vì vậy, khi mô hình hoạt động tốt trên dữ liệu huấn luyện,

nhưng kém về dữ liệu mới.

Và lịch sử ở đây thì sao?

Đây là đối tượng

lưu trữ thông tin chi tiết về quá trình đào tạo.

Ví dụ: giá trị tổn thất và số liệu ở mỗi thời điểm,

tại mỗi lần lặp cho cả quá trình huấn luyện và xác nhận.

Và như chúng ta đã xem xét nó trước đây,

chúng ta có thể vẽ đồ thị đường cong học tập này

và đánh giá hiệu quả của mô hình.

Để tóm tắt những gì chúng ta đã nói cho đến nay,

chức năng mất được giảm thiểu trong quá trình đào tạo,

hướng dẫn mô hình đưa ra dự đoán chính xác.

Và trình tối ưu hóa SGD

lặp đi lặp lại cập nhật trọng số của mô hình

để đạt được mức tối thiểu này.

Và các số liệu ở đây cung cấp cái nhìn sâu sắc

vào cách mô hình hoạt động cả trong quá trình đào tạo

và khi đánh giá mô hình cuối cùng.

Quá trình đào tạo lặp đi lặp lại cải thiện mô hình

sử dụng dữ liệu huấn luyện và đánh giá hiệu suất của nó

trên dữ liệu xác nhận để đảm bảo tính khái quát.

Vậy sau đó chúng ta có thể tiếp tục

và đánh giá mô hình trên tập kiểm tra.

Vì vậy, chúng ta hãy tiếp tục và làm điều đó.

Hãy chắc chắn rằng chúng tôi đặt tiêu đề phù hợp trong phần bình luận.

Đánh giá mô hình trên tập kiểm tra.

Vì vậy, chúng ta hãy tiếp tục và viết nó xuống đây.

Đây là cách đánh giá mô hình sau khi đào tạo.

Vì vậy chúng ta sẽ gọi nó là test_results.

Vì vậy, đây là đánh giá trên tập kiểm tra

để xem nó khái quát hóa dữ liệu mới tốt như thế nào.

Vì vậy chúng ta sẽ gọi nó là test_results,

và chúng ta sẽ gọi model.evaluate,

sau đó chúng tôi sẽ đưa ra X_test, y_test,

và sau đó return_dict là đúng.

Được rồi, chúng ta hãy tiếp tục và sửa lỗi chính tả.

Vì vậy return_dict = Đúng.

Tiếp theo, chúng ta hãy tiếp tục và in những kết quả này.

f"Kết quả kiểm tra:

và chúng tôi sẽ nói {test_results}"

Được rồi, vậy là việc đánh giá mô hình sẽ được thực hiện

và sau đó in kết quả cho chúng tôi.

Hãy chắc chắn rằng chúng ta có chữ T viết hoa ở đây

và hoàn hảo.

Chuyển sang vẽ biểu đồ các số liệu qua các kỷ nguyên,

nói cách khác, sự lặp lại.

Vì vậy, hãy tiếp tục và bắt đầu làm điều đó.

Vẽ biểu đồ các số liệu qua các kỷ nguyên.

Vì vậy, chúng ta sẽ tiếp tục

và khởi tạo hình plt.figure

và cho nó kích thước, vậy figsize có thể là 14,7.

Và sau đó, hãy tiếp tục và tạo một cốt truyện phụ.

Và khi đó subplot sẽ có 1,2,1.

Tiếp theo, chúng tôi sẽ đưa ra lịch sử ở đây, vì vậy plt.plot

history.history

và sau đó chúng tôi sẽ gọi MAE,

label = "Đào tạo MAE"

Tiếp theo, hãy tiếp tục và thêm MAE xác thực, tức là plt.plot.

Chúng ta sẽ thêm history.history,

thì chúng ta sẽ gọi Xác thực MAE ở đây, val_mae.

Và sau đó chúng ta sẽ gắn nhãn nó là MAE xác thực, được chứ?

Tiếp theo, chúng ta sẽ tiếp tục đặt tên cho plt.title này.

Và sau đó, chúng ta sẽ nói Lỗi tuyệt đối trung bình, MAE.

Tiếp theo, chúng ta sẽ cung cấp xlabel và ylabel

tới plt.xlabel("Epochs") này

và sau đó plt.ylabel("MAE")

Cuối cùng, chúng ta sẽ truy cập plt.legend.

Vì vậy, chuyển sang phần phụ thứ hai tiếp theo

và lần này chúng ta sẽ tập trung vào RMSE

thay vì MAE mà chúng tôi đã làm ở phần đầu tiên.

Vì thế hãy tiếp tục và có lẽ chúng ta có thể tiếp tục

và sao chép ô phụ ở trên và thực hiện các thay đổi cho nó

như vậy sẽ nhanh hơn rất nhiều.

Vì vậy, vị trí sẽ là 1,2,2.

Lần này, thay vì MAE, chúng ta sẽ lấy RMSE ở đây,

đó là lỗi bình phương trung bình gốc

và sau đó chúng ta sẽ đổi tiêu đề thành Training RMSE.

Và sau đó chúng ta sẽ tiếp tục và nhận RMSE xác thực tiếp theo,

vì vậy chúng ta sẽ thay đổi nó ngay tại đây,

tương ứng trên nhãn là tốt.

Tiếp theo, chúng tôi sẽ đánh vần nó trong tiêu đề

dưới dạng lỗi bình phương gốc.

Và sau đó, phiên bản ngắn gọn là RMSE.

Sau đó chúng ta sẽ có lại các kỷ nguyên, ylabel sẽ là RMSE,

và chúng ta sẽ có huyền thoại.

Thế thôi. Vì vậy, chúng tôi có hai ô phụ ở đây.

Phần đầu tiên hiển thị MAE đào tạo.

Nói cách khác,

mô hình hoạt động tốt như thế nào trên dữ liệu đào tạo.

Và MAE xác thực cho thấy mô hình tốt như thế nào

đang khái quát hóa dữ liệu chưa nhìn thấy trong dữ liệu đầu tiên.

Và trong cái thứ hai,

RMSE phản ánh hiệu suất trên dữ liệu huấn luyện

trong khi RMSE xác thực biểu thị sự khái quát hóa

đến dữ liệu xác thực.

Và hãy nhớ, RMSE là căn bậc hai của giá trị trung bình

chênh lệch bình phương giữa giá trị dự đoán và giá trị thực tế.

Vì vậy, điều này nhạy cảm hơn

sai số lớn hơn sai số trước là sai số tuyệt đối.

Một cái gì đó cần ghi nhớ.

Vậy tại sao chúng ta lại có những mảnh đất riêng biệt?

Bởi vì chúng ta đang xem xét hai số liệu khác nhau

cung cấp những hiểu biết độc đáo về hiệu suất của mô hình.

Cái đầu tiên, MAE,

cung cấp phép đo lỗi đơn giản

trong khi cái thứ hai, RMSE,

mang lại nhiều trọng lượng hơn cho các lỗi lớn hơn.

Bằng cách vẽ chúng một cách riêng biệt,

chúng ta có thể so sánh cách mô hình hoạt động theo

đến các số liệu lỗi khác nhau.

Vì vậy, hãy tiếp tục và hoàn tất việc này.

Vậy chúng ta sẽ làm gì tiếp theo, plt.tight_layout.

Và sau đó chúng ta hãy tiếp tục

và lưu nó ở cùng vị trí mà chúng ta đã lưu,

trong thư mục đầu ra, vì vậy out/03_04

và chúng tôi sẽ gọi đây là số liệu_visualization.png.

Chúng ta sẽ tiếp tục và lưu nó

trong đầu ra/03_04_metrics_visualization.png.

Thế thôi.

Vì vậy, nếu bạn viết mã ở đây thì thật tuyệt.

Nếu không, hãy tiếp tục và tìm khung bên trái

và nhấp vào tệp python 03_04_end.

Vì vậy, điều này mang lại chính xác những gì chúng tôi đã làm cho đến nay.

Vì vậy, hãy tiếp tục và chạy nó để tạo ra những đồ thị này,

và sau đó chúng ta sẽ tiếp tục và xem xét từng cái một.

Vì vậy, chỉ mất vài phút, khá nhanh,

vượt qua tất cả 20 kỷ nguyên,

và sau đó nó sẽ tạo các ô của chúng tôi trong thư mục đầu ra.

Vì vậy, hãy đảm bảo rằng bạn đã mở rộng thư mục đầu ra.

Bằng cách đó, chúng ta có thể nhanh chóng tiếp tục và xem các ô.

Khi nó kết thúc,

chúng tôi có thể xem kết quả kiểm tra từ trên xuống trong thiết bị đầu cuối,

và chúng ta có thể thấy sự mất mát, đó là MSE trong trường hợp này,

trên tập kiểm tra là khoảng 0,36.

Điều này cho biết sai số bình phương trung bình của mô hình

khi dự đoán giá nhà.

Và chúng ta có MAE xấp xỉ 0,426

và điều này cho thấy sai số tuyệt đối trung bình

trong dự đoán của mô hình.

Tiếp theo, chúng ta đang xem xét RMSE và nó vào khoảng 0,601,

cao hơn một chút so với MAE.

Và điều này cho thấy có một số lỗi lớn hơn

nhưng không đáng kể lắm.

Tiếp theo chúng ta sẽ tiếp tục

và tìm biểu đồ mà chúng tôi đã tạo ở đây,

vì vậy hãy tiếp tục và mở rộng thư mục đầu ra.

Và trong thư mục đầu ra,

bạn sẽ thấy 03_04_metrics_visualization.png.

Vì vậy, ở bên trái, chúng ta đang thấy sai số tuyệt đối trung bình,

và ở bên phải, chúng ta đang thấy lỗi bình phương trung bình gốc.

Khi chúng ta nhìn vào biểu đồ bên trái trước tiên, đó là MAE,

đồ thị cho thấy MAE giảm đều đặn

cho cả dữ liệu huấn luyện và xác nhận

khi số lượng kỷ nguyên, số lần lặp tăng lên.

Nó gợi ý điều gì?

Vâng, điều này cho thấy mô hình đang học tập hiệu quả

và cải thiện dự đoán của mình bằng cách đào tạo nhiều hơn

vì đường màu xanh, Đào tạo MAE,

và đường màu cam, Xác thực MAE, đều giảm.

Cốt truyện tiếp theo, chúng tôi đang xem RMSE.

Một lần nữa, đường màu xanh lam là Training RMSE,

dòng màu cam là RMSE xác thực.

Biểu đồ này cho thấy xu hướng tương tự như biểu đồ MAE.

Ban đầu, RMSE cho cả đào tạo

và xác nhận cao hơn,

nhưng nó giảm mạnh trong vài lần lặp đầu tiên

rồi ổn định lại.

Sự sụt giảm mạnh trong vài kỷ nguyên đầu tiên cho thấy

rằng mô hình nhanh chóng học được những tính năng quan trọng nhất

hoặc các mẫu trong dữ liệu,

điều này dẫn đến việc giảm nhanh chóng các lỗi lớn.

Giống như biểu đồ MAE, RMSE đào tạo và xác nhận hội tụ

và sau đó chúng vẫn khá ổn định.

Đây là một dấu hiệu tích cực tuyệt vời

về khả năng khái quát hóa của mô hình.

Vì vậy, mô hình dường như đã được đào tạo hiệu quả

không có dấu hiệu trang bị quá mức

khi chúng ta xem xét các chỉ số đào tạo và xác nhận ở đây,

MAE và RMSE.

Sự giảm mạnh ở cả hai đồ thị

trong những lần lặp lại đầu tiên, những kỷ nguyên,

gợi ý rằng mô hình đã nhanh chóng học được

các mẫu cơ bản trong dữ liệu,

tiếp theo là tinh chỉnh trong các kỷ nguyên sau này.

Và kết quả kiểm tra cuối cùng phù hợp tốt

với các xu hướng quan sát được trong cốt truyện,

gợi ý mô hình khái quát tốt cho dữ liệu chưa nhìn thấy.

Vì vậy, để kết luận, chúng ta có thể nói mô hình này có vẻ

để hoạt động khá tốt trên bộ dữ liệu Nhà ở California

với hiệu suất nhất quán trong quá trình đào tạo, xác nhận,

và tập dữ liệu thử nghiệm.

Hãy tiếp tục.