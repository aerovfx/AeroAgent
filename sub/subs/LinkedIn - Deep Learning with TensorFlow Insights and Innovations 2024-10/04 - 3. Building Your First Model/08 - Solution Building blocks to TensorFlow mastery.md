# 08 - Giải pháp Xây dựng các khối để làm chủ TensorFlow

---

(âm nhạc vui tươi)

- [Người hướng dẫn] Chào mừng các bạn đến với video giải pháp.

Bây giờ chúng ta sẽ bắt đầu từ mã thử thách,

đó là 03_07_challenge.py,

và chúng ta sẽ tìm đến tệp Python giải pháp,

đó là 03_08_solution.py.

Vì vậy, hãy tiếp tục và đóng cửa sổ bên trái

bằng cách nhấp vào Explorer ở đây và sau đó chúng ta sẽ tiếp tục

và tiếp tục với mã thử thách của chúng tôi

để thực hiện theo cách của chúng tôi đối với mã giải pháp.

Vì vậy, hãy tiếp tục và xem lại những gì chúng ta có cho đến nay.

Chúng tôi có những thư viện quan trọng và cần thiết

chẳng hạn như tensorflow, sklearn, matplotlib.

Sau đó, chúng tôi tiếp tục tải và chuẩn bị tập dữ liệu.

Chúng tôi lại sử dụng nhà ở California.

Sau đó, chúng tôi chia dữ liệu để có chuỗi X, xác thực X,

y huấn luyện, y xác nhận.

Tiếp theo chúng ta sẽ chuyển sang mã giải pháp,

bắt đầu bằng việc chuẩn hóa dữ liệu.

Vì vậy đây là nhiệm vụ số một mà chúng tôi sắp thực hiện

từ video thử thách.

Vì vậy, hãy tiếp tục và chuẩn hóa dữ liệu tiếp theo.

Vì vậy, để chuẩn hóa dữ liệu, chúng ta sẽ bắt đầu

bằng thước đo tiêu chuẩn.

Vì vậy chúng ta sẽ gọi StandardScaler ở đây,

và sau đó gán tỷ lệ cho bằng nhau

để mở và đóng dấu ngoặc đơn StandardScaler.

Tiếp theo chúng ta sẽ chuyển đổi dữ liệu tàu X

bằng cách gọi Scaler.fit_transform,

và sau đó chúng ta sẽ gọi X_train.

Tiếp theo, chúng ta sẽ chuyển đổi xác thực X.

Lưu ý rằng chúng tôi không sử dụng biến đổi phù hợp

đúng hơn là chúng tôi chỉ sử dụng phép biến đổi để xác thực X.

Vậy đó là Scaler.transform,

và sau đó nó sẽ lấy X_valid.

Tiếp theo chúng ta sẽ sử dụng X_test,

và nó sẽ có Scaler.transform

và nó sẽ có X_test.

Vậy là điều này sẽ kết thúc nhiệm vụ đầu tiên của chúng ta,

đó là việc chuẩn hóa dữ liệu.

Tiếp theo chúng ta bắt đầu nhiệm vụ thứ hai.

Tiếp theo chúng ta sẽ tiếp tục

với việc xây dựng mô hình với hai lớp ẩn

và một lớp đầu ra như được yêu cầu trong video thử thách.

Vì vậy chúng ta sẽ tiếp tục và bắt đầu xây dựng mô hình

sử dụng TensorFlow Keras và sau đó là Sequential.

Vì vậy, hãy tiếp tục và làm điều đó.

Và sau đó chúng ta sẽ mở dấu ngoặc đơn.

Vậy việc tiếp theo chúng ta sẽ làm là

chúng ta sẽ gọi tf.keras.layers.Dense,

và chúng ta sẽ sử dụng 30 nơ-ron

với chức năng kích hoạt của relu.

Và sau đó chúng ta sẽ tiếp tục

và gán input_shape

trở thành X_train.shape của chúng tôi,

rồi mở dấu ngoặc đơn, 1,

rồi đóng dấu ngoặc đơn, dấu phẩy.

Vì vậy, đây là lớp đầu vào đầu tiên của chúng tôi với 30 nơ-ron

với chức năng kích hoạt của relu,

và sau đó chúng tôi xác định hình dạng đầu vào.

Tiếp theo, chúng ta sẽ tạo lớp thứ hai

như được hỏi từ video thử thách.

Vì vậy, hãy tiếp tục và làm lớp thứ hai.

Vì vậy chúng ta sẽ tạo lại, 30 nơ-ron

với chức năng kích hoạt của relu.

Vì vậy, đây sẽ là lớp thứ hai của chúng ta,

và sau đó chúng ta sẽ có lớp cuối cùng,

đó là lớp đầu ra chỉ có một nơ-ron.

Vì vậy, hãy tiếp tục và làm điều đó.

Và hãy loại bỏ những khoảng trống không cần thiết ở đây

để làm cho mã của chúng tôi trở nên Pythonic và rõ ràng hơn.

Và chúng tôi có nó.

Chúng tôi đã tạo hai lớp ẩn với 30 nơ-ron

với chức năng kích hoạt của relu và sau đó là một lớp đầu ra.

Tiếp theo chúng ta sẽ chuyển sang thử thách tiếp theo,

đang biên dịch mô hình.

Sau khi xác định kiến trúc,

bây giờ chúng ta sẽ biên dịch mô hình

sử dụng sai số bình phương trung bình làm hàm mất

và giảm độ dốc ngẫu nhiên làm trình tối ưu hóa.

Vì vậy, hãy tiếp tục và làm điều đó.

Vì vậy, chúng ta có thể làm điều đó trong một dòng, model.compile,

và sau đó chúng ta sẽ cung cấp cho nó hàm mất mát

của Mean_squared_error.

Và sau đó là SGD, giảm độ dốc ngẫu nhiên, làm công cụ tối ưu hóa.

Một lần nữa, MSE là hàm mất mát được sử dụng phổ biến

cho các nhiệm vụ hồi quy, đó là những gì chúng tôi đang làm ở đây,

nơi mục tiêu là giảm thiểu sự khác biệt

giữa giá trị dự đoán và giá trị thực tế.

SGD là một công cụ tối ưu hóa đơn giản và hiệu quả

để huấn luyện mạng lưới thần kinh,

đặc biệt thích hợp cho các mô hình nhỏ hơn.

Tiếp theo, chúng ta sẽ chuyển sang đào tạo mô hình.

Vì vậy, khi mô hình của chúng tôi được biên dịch,

chúng ta sẽ tiếp tục với bước đào tạo.

Vì vậy mô hình sẽ học bằng cách tối thiểu hóa hàm mất mát

trong giai đoạn đào tạo.

Vì vậy, hãy tiếp tục và mã hóa nó.

Vì thế chúng ta sẽ gọi nó là lịch sử,

và sau đó chúng ta sẽ gọi model.fit để huấn luyện mô hình,

và sau đó sẽ cần X_train, y_train,

kỷ nguyên bằng 20,

và sau đó chúng tôi sẽ cung cấp dữ liệu xác nhận

là xác thực X và xác thực Y, X_valid, y_valid.

Vì vậy, trong bước này, chúng tôi đang đào tạo mô hình cho 20 kỷ nguyên

và giám sát cả việc mất dữ liệu đào tạo và xác nhận

để đảm bảo rằng mô hình đang học tập hiệu quả

và không khớp quá mức với dữ liệu huấn luyện.

Mất xác nhận cung cấp cái nhìn sâu sắc

về mức độ khái quát của mô hình đối với dữ liệu không nhìn thấy được.

Vì vậy, sau khi đào tạo, chúng ta có thể tiếp tục

để đánh giá mô hình trên tập kiểm tra.

Vậy chúng ta sẽ làm điều đó như thế nào?

Chúng tôi sẽ sử dụng sai số bình phương trung bình cho điều đó.

Vì vậy hãy tiếp tục và bắt đầu viết mã, mse_test bằng,

và sau đó tất cả những gì chúng ta làm ở đây là gọi model.evaluate,

sau đó chúng ta sẽ sử dụng X_test và y_test.

Vì vậy, sai số bình phương trung bình trên tập kiểm tra

cung cấp thước đo định lượng về hiệu suất của mô hình của chúng tôi

đặc biệt là trên dữ liệu chưa nhìn thấy.

Vì vậy, nó cung cấp một chỉ số quan trọng

mô hình đã học được từ dữ liệu huấn luyện tốt như thế nào.

Vậy sau đó chúng ta sẽ tiếp tục

và chúng ta sẽ giải quyết bước hình dung.

Vì vậy, để làm được điều đó, chúng tôi sẽ vẽ sơ đồ tổn thất đào tạo và xác nhận.

Sơ đồ này sẽ giúp chúng ta xác định

liệu mô hình của chúng ta có được trang bị quá mức, không được trang bị đầy đủ hay không,

hoặc đang khái quát hóa tốt.

Vì vậy hãy tiếp tục và bắt đầu với plt.plot.

Và sau đó hãy cuộn lên

để chúng ta có thể xem thêm mã, plt.plot,

và nó sẽ lấy history.history.

Và rồi nó sẽ mất mát, nhãn mác,

và chúng tôi sẽ gắn nhãn nó là Mất mát.

Tiếp theo, chúng ta sẽ nói plt.plot.

Lần này chúng tôi đã sẵn sàng cho việc mất xác nhận.

Vì vậy, history.history,

val_loss, nhãn bằng,

lần này chúng ta sẽ gọi nó là Mất xác thực.

Tuyệt vời.

Tiếp theo chúng ta sẽ tiếp tục

và dán nhãn trục X và trục Y.

Vì vậy, hãy bắt đầu với trục X, plt.xlabel.

Đó sẽ là Kỷ nguyên.

Và khi đó nhãn Y sẽ chẳng là gì ngoài Mất mát.

Được rồi, sau đó chúng ta sẽ nói plt.legend.

Được rồi, tiếp theo, việc chúng ta sẽ làm là tiếp tục

và lưu hình này vào thư mục đầu ra,

để chúng ta có thể sử dụng nó trong tương lai.

Hãy tiếp tục và đưa ra đường dẫn, đầu ra/,

và lưu ý rằng chúng tôi đang làm điều này để tìm giải pháp.

Vậy giải pháp sẽ là 03_08_loss_plot.png.

Vì vậy đây là con đường chúng tôi đang cung cấp

cho con số âm mưu mất mát của chúng tôi.

Vậy là điều này kết thúc thử thách của chúng ta với cốt truyện,

giúp chúng tôi xác định liệu mô hình của chúng tôi có bị trang bị quá mức hay không,

không được trang bị đầy đủ hoặc khái quát hóa tốt.

Đây là bước rất cần thiết,

và nhìn thấy nó một cách trực quan sẽ đưa ra rất nhiều lời giải thích

để phân tích về mô hình của chúng tôi.

Vì vậy, trong thử thách này, chúng tôi đã giải quyết vấn đề xây dựng, đào tạo,

và đánh giá mạng lưới thần kinh đơn giản bằng cách sử dụng TensorFlow.

Chúng ta sẽ tiếp tục và so sánh mã này ngay bây giờ

với mã thử thách,

và nếu chúng ta có bất kỳ khác biệt nào, hãy tiếp tục và giải quyết chúng

bằng cách mở thư mục src từ khung bên trái,

và tìm 03_08_solution.py.

Vì vậy, khi bạn đã hoàn tất, hãy chạy thử,

và sau đó chúng ta sẽ xem xét kết quả.

Sẽ mất vài phút

để trải qua tất cả các thời đại và việc tạo ra các cốt truyện,

và sau đó chúng ta sẽ cùng nhau phân tích ý nghĩa của cốt truyện

và chúng ta có thể rút ra kết luận gì từ thử thách này.

Kỷ nguyên 1, 2, 3. Nó diễn ra khá nhanh.

Vì vậy, nó sẽ kết thúc khá nhanh chóng. Và nó đã kết thúc.

Vì vậy, những gì chúng ta thấy ở đây được in trong thiết bị đầu cuối

là sai số bình phương trung bình trên tập kiểm tra là 0,31.

Vậy chúng ta hãy tiếp tục

và bây giờ hãy tìm cốt truyện của chúng tôi từ khung bên trái

bằng cách mở rộng thư mục đầu ra

và tìm 03_08_loss_plot.png.

Vì vậy, sau khi kịch bản của chúng tôi hoàn thành,

chúng ta có thể thấy sai số bình phương trung bình trên tập kiểm tra là 0,31.

Vậy nên chúng tôi đã đi trước

và mở hình từ thư mục đầu ra,

có tiêu đề là 03_08_loss_plot.png.

Vì vậy hãy tiếp tục và đánh giá con số này

và hiểu hình ảnh này đang nói với chúng ta điều gì.

Vì vậy, biểu đồ này thể hiện sự mất mát trong quá trình đào tạo,

đó là đường màu xanh,

và mất xác nhận, đó là đường màu cam,

hơn 20 lần lặp, 20 kỷ nguyên

trong quá trình huấn luyện mạng nơ-ron.

Những quan sát chính mà chúng ta có thể rút ra là gì

từ âm mưu này?

Mất xác nhận bắt đầu tương đối cao

và tăng đáng kể trong vài kỷ nguyên đầu tiên

đạt đỉnh trên 5.

Vâng, nó chỉ ra điều gì?

Điều này chỉ ra rằng mô hình ban đầu gặp khó khăn

để khái quát hóa tốt dữ liệu xác nhận.

Mất xác nhận dao động khá nhiều

trong thời kỳ đầu với mức tăng giảm mạnh.

Vì vậy điều này có thể gợi ý

rằng mô hình ban đầu không ổn định, có thể do

đến tốc độ học tập hoặc khởi tạo ngẫu nhiên các trọng số.

Tiếp theo vào khoảng kỷ thứ 5, chúng ta có thể thấy

rằng việc mất xác nhận đã giảm đáng kể

và sau đó tiếp tục giảm,

ổn định ở mức thấp hơn nhiều.

Vâng, nó gợi ý gì?

Điều này gợi ý rằng mô hình cuối cùng sẽ học được

để khái quát hóa tốt hơn dữ liệu xác nhận.

Việc mất huấn luyện giảm dần

và duy trì ở mức thấp trong suốt quá trình đào tạo, cho thấy

rằng mô hình đang học dữ liệu huấn luyện một cách nhất quán

không gặp nhiều khó khăn.

Vì vậy, khi kết thúc khóa đào tạo, đó là

sau khoảng kỷ thứ 7, cả quá trình đào tạo

và tổn thất xác nhận là khá thấp

và có thể nói là tương đối ổn định.

Điều này chỉ ra rằng mô hình đã học được các mẫu

trong dữ liệu và không quá phù hợp.

Vậy chúng ta có thể học được gì từ điều này?

Vâng, sự bất ổn ban đầu.

Những biến động đáng kể về mất xác nhận

trong vài kỷ nguyên đầu tiên gợi ý

rằng mô hình ban đầu gặp khó khăn

tìm giải pháp ổn định.

Vâng, điều này có thể là do nhiều yếu tố khác nhau

chẳng hạn như tốc độ học tập, khởi tạo trọng số,

hoặc thậm chí là độ phức tạp của dữ liệu của chúng tôi.

Sự mất mát đào tạo luôn thấp hơn

so với việc mất xác nhận, điều này khá điển hình,

nhưng cần được theo dõi.

Tuy nhiên, do mất xác nhận ổn định

ở giá trị thấp,

không có dấu hiệu mạnh mẽ nào về việc trang bị quá mức ở đây.

Cho rằng các giá trị tổn thất ổn định sau một vài kỷ nguyên,

chúng ta có thể xem xét thực hiện tiêu chí dừng sớm

trong tương lai.

Điều này sẽ giúp chúng ta tránh được việc đào tạo không cần thiết

ngoài điểm này,

và nó sẽ tiết kiệm tài nguyên tính toán.

Bất chấp sự bất ổn ban đầu,

mô hình cuối cùng đã khái quát hóa khá tốt

được chứng minh bằng sự ổn định

và mất xác nhận thấp vào cuối khóa đào tạo.

Vì vậy, cuối cùng, chúng ta có thể nói biểu đồ này cho thấy

rằng mô hình đã phải đối mặt với những thách thức

trong giai đoạn đầu của quá trình đào tạo,

đặc biệt với việc khái quát hóa dữ liệu xác nhận,

nhưng cuối cùng nó đã tìm ra giải pháp ổn định bằng cả đào tạo

và tổn thất xác nhận hội tụ về giá trị thấp.

Nó gợi ý điều gì?

Vâng, điều này cho thấy rằng mô hình đã học được một cách hiệu quả,

mặc dù chúng tôi quan sát thấy một số bất ổn ban đầu.

Vì vậy, điều này kết thúc giải pháp của chúng tôi.

Hãy quay lại mã giải pháp

và xem lại những gì chúng tôi đã làm.

Chúng tôi đã nhập các thư viện.

Chúng tôi đã tải và chuẩn bị tập dữ liệu.

Chúng tôi đã phân tách và tạo X huấn luyện, xác thực X,

tập dữ liệu xác thực y và y.

Chúng tôi đã chuẩn hóa dữ liệu bằng StandardScaler.

Chúng tôi bắt đầu với fit_transform trên tàu X,

và chúng tôi chỉ sử dụng biến đổi để xác thực X và kiểm tra X.

Vậy nên chúng tôi đã đi trước

và xây dựng mô hình với hai lớp ẩn.

Trước hết, chúng tôi bắt đầu với 30 nơ-ron.

Chúng tôi đã đưa ra chức năng kích hoạt của relu,

và sau đó chúng ta có một lớp khác, cũng có 13 nơ-ron

với chức năng kích hoạt của relu.

Sau đó chúng ta có một lớp đầu ra. Tiếp theo, chúng tôi biên soạn mô hình.

Chúng tôi đã sử dụng sai số bình phương trung bình

và chúng tôi đã sử dụng phương pháp giảm độ dốc ngẫu nhiên làm trình tối ưu hóa.

Sau đó, chúng tôi tiếp tục và đào tạo mô hình.

Chúng tôi đã đánh giá mô hình trên tập thử nghiệm.

Chúng tôi đã in ra sai số bình phương trung bình trên tập kiểm tra.

Cuối cùng, chúng tôi đã đi trước

và vẽ biểu đồ tổn thất đào tạo và xác nhận,

và chúng tôi đã lấy đi một số quan sát từ cốt truyện đó.

Vì vậy, công việc tuyệt vời là giải quyết thách thức này và giải pháp.

Hãy tôn vinh những gì bạn đã học được,

và tôi sẽ gặp bạn trong buổi học tiếp theo.