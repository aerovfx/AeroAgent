# 06 - Bộ mã hóa tự động Giới thiệu nhẹ nhàng về các mô hình tổng quát

---

- [Giảng viên] Trong phần này,

chúng ta sẽ đi sâu vào việc sử dụng TensorFlow để xây dựng và đào tạo

một bộ mã hóa tự động để phát hiện sự bất thường.

Bộ mã hóa tự động này sẽ được áp dụng

đến cùng một tập dữ liệu nhà ở California

chúng tôi đã và đang làm việc cùng.

Chúng tôi sẽ tập trung vào việc xây dựng lại các tính năng đầu vào

và xác định bất kỳ sự bất thường tiềm ẩn nào trong tập dữ liệu.

Vì vậy, bạn có thể hỏi, bộ mã hóa tự động là gì?

Chà, chúng ta có thể coi nó giống như một loại mạng lưới thần kinh

học cách nén dữ liệu vào một không gian có chiều thấp hơn

và sau đó xây dựng lại nó.

Bằng cách kiểm tra xem dữ liệu được tái tạo tốt như thế nào,

chúng ta có thể xác định các ngoại lệ hoặc sự bất thường

mà bộ mã hóa tự động gặp khó khăn trong việc tạo lại.

Vậy hãy gặp lại nhau trong môi trường không gian mã

và từ khung bên trái, tìm thư mục SRC.

Sau đó hãy tiếp tục và tìm đống trăn 03_06_begin.

Vì vậy, chúng tôi bắt đầu với việc tải và xử lý trước dữ liệu

như chúng ta thường làm.

Tập dữ liệu chúng tôi đang làm việc ở đây

là cùng một tập dữ liệu về nhà ở ở California và được tải

và chia thành các tập huấn luyện, xác nhận và kiểm tra.

Sau khi chúng tôi tải và chuẩn bị tập dữ liệu,

chúng ta chuyển sang bước mở rộng quy mô

và chúng tôi tiếp tục và fit_transform trên X_train.

Sau đó chúng ta chỉ chuyển đổi trên X_validation

và bộ dữ liệu X_test.

Tiếp theo chúng ta tiếp tục và xác định mô hình bộ mã hóa tự động.

Bộ mã hóa ở đây nén dữ liệu đầu vào

thành một biểu diễn có chiều thấp hơn,

nói cách khác, 32 chiều.

Ở đây nó bao gồm ba lớp,

lớp đầu tiên có 128 nơ-ron, lớp thứ hai có 64,

và lớp thứ ba có 32 nơ-ron.

Nó bao gồm ba lớp

giảm dần kích thước của dữ liệu.

Tiếp theo, chúng ta chuyển sang bộ giải mã.

Bộ giải mã tái tạo lại dữ liệu đầu vào

từ biểu diễn nén.

Nó phản chiếu bộ mã hóa, nhưng ngược lại,

mở rộng dữ liệu nén

trở lại kích thước đầu vào ban đầu.

Vì vậy bộ mã hóa tự động là sự kết hợp của bộ mã hóa

và bộ giải mã mà chúng tôi đã xác định ở trên.

Vì vậy, chúng tôi gọi nó từ TensorFlow.keras.Sequential.

Và sau đó chúng tôi đưa vào bộ mã hóa và bộ giải mã

mà chúng tôi đã xác định ở trên,

định nghĩa bộ mã hóa và định nghĩa bộ giải mã.

Vì vậy chúng tôi tạo một bộ mã hóa tự động ở đây,

đó là sự kết hợp giữa bộ mã hóa và bộ giải mã.

Nó được đào tạo để giảm thiểu sự khác biệt

giữa dữ liệu đầu vào và việc tái tạo lại nó.

Sau đó, chúng tôi tiếp tục và biên dịch bộ mã hóa tự động

và chúng tôi sử dụng sai số bình phương trung bình làm hàm mất mát,

và chúng tôi sử dụng Adam làm trình tối ưu hóa.

Sau đó chúng tôi chuẩn bị dữ liệu để trực quan hóa ở đây.

Sau đó chúng ta khởi tạo lịch sử

chúng ta sẽ đi đâu

và huấn luyện bộ mã hóa tự động trong bước tiếp theo.

Vì vậy điều chúng ta sẽ làm tiếp theo là huấn luyện bộ mã hóa tự động

để xây dựng lại dữ liệu đầu vào.

Nó sử dụng cả dữ liệu huấn luyện và dữ liệu xác nhận

cho nhiệm vụ này.

Số lượng kỷ nguyên sẽ được đặt thành 20.

Vì vậy, đây là tệp Python khởi đầu của chúng tôi

nơi chúng tôi tải các thư viện cần thiết,

đã chuẩn bị tập dữ liệu, thực hiện phân chia, chia tỷ lệ.

Sau đó, chúng tôi xác định mô hình bộ mã hóa tự động

với bộ mã hóa và bộ giải mã.

Sau đó, chúng tôi xác định bộ mã hóa tự động.

Sau đó, chúng tôi biên dịch bộ mã hóa tự động của mình.

Chúng tôi đã chuẩn bị dữ liệu để trực quan hóa,

và bây giờ chúng tôi đang tiếp tục đào tạo bộ mã hóa tự động.

Vì vậy, hãy tiếp tục và bắt đầu từ phần giữ chỗ ở đây.

Vì vậy, chúng ta sẽ đào tạo bộ mã hóa tự động,

và sau đó chúng ta sẽ tiếp tục đào tạo

của bộ mã hóa tự động ở đây.

Vì vậy chúng ta sẽ tiếp tục và gọi nó là lịch sử

và lịch sử = autoencoding.fit.

Và sau đó chúng ta sẽ nói X_train và sau đó là X_train.

Vì vậy lần xuất hiện đầu tiên của X_train là đầu vào

đến bộ mã hóa tự động.

Nó đại diện cho dữ liệu gốc

rằng chúng tôi muốn bộ mã hóa tự động

để học cách mã hóa và sau đó giải mã.

Sau đó, chúng tôi sử dụng X_train thứ hai ở đây,

đó là đầu ra mục tiêu cho bộ mã hóa tự động.

Vì mục tiêu của bộ mã hóa tự động ở đây là tái tạo lại

dữ liệu đầu vào, đầu ra dự kiến trong quá trình đào tạo

giống như đầu vào.

Tiếp theo chúng ta tiếp tục và đi tiếp

và chúng tôi đưa ra số lần lặp.

Hãy tiếp tục và sử dụng lại, 20 ở đây là kỷ nguyên.

Sau đó, chúng tôi sử dụng dữ liệu xác nhận.

Hãy tạo khoảng trống ở đây bằng cách thu nhỏ khung bên trái.

Vì vậy, validation_data sẽ bằng X_valid,

và sau đó chúng ta sẽ sử dụng cùng một x_valid.

Được rồi, điều chúng tôi đã làm là tiếp tục

và huấn luyện bộ mã hóa tự động để tái tạo lại dữ liệu đầu vào.

Nó sử dụng cả dữ liệu huấn luyện và dữ liệu xác nhận

cho nhiệm vụ này và nó sử dụng 20 kỷ nguyên.

Vậy thì chúng ta đã chuẩn bị sẵn ở trên rồi

trực quan hóa dữ liệu cho biểu đồ mất xác thực của kỷ nguyên

ở trên để chúng ta không phải tiếp tục và xác định lại điều này.

Vì vậy, điều chúng ta sẽ làm tiếp theo là gọi hàm này

mà chúng tôi đã chuẩn bị sẵn ở tập tin bắt đầu cho chúng tôi,

và chúng ta sẽ tiếp tục và gọi nó là

trong phần tiếp theo của mã.

Vì vậy, hãy làm điều đó ở đây.

Vì vậy chúng ta sẽ gọi nó là âm mưu huấn luyện mất mát

và lưu nó.

Vì vậy chúng ta sẽ gọi hàm mà chúng ta xác định ở trên

và sau đó chúng tôi sẽ đưa lịch sử vào đó.

Tiếp theo, chúng ta sẽ tiếp tục và hình dung bản gốc

so với dữ liệu được xây dựng lại bằng cách sử dụng các biểu đồ đường.

Để hình dung được điều đó, chúng ta sẽ tiếp tục

và tạo ra một chức năng.

Hãy đặt tiêu đề cho việc chúng ta đang làm trước tiên.

Vì vậy, hãy trực quan hóa dữ liệu gốc và dữ liệu được xây dựng lại

sử dụng các đường vẽ.

Vì vậy, đối với điều này, chúng ta sẽ tiếp tục và nói,

định nghĩa cốt truyện_reconstruction.

Hãy cuộn lên một chút và đây sẽ là mô hình

và nó sẽ mất n = 10.

Vậy N là n mẫu đầu tiên trong tập kiểm tra.

Hãy sửa lỗi đánh máy ở đây

và nó sẽ tiếp tục vẽ cả bản gốc

và xây dựng lại các giá trị cho mỗi tương lai.

Vậy điều này sẽ cho phép chúng ta làm gì?

Nó sẽ cho phép chúng tôi đánh giá trực quan độ chính xác

của việc tái thiết bằng cách sử dụng chức năng này.

Vì vậy hãy tiếp tục và nói samples = X_test

và sẽ mất n,

và tiếp theo chúng ta sẽ nói,

mẫu được xây dựng lại = model.predict(mẫu).

Hãy chuẩn bị hình ở đây.

Vì vậy, hãy tính, axs = plt.subplots(n, 1, figsize=(10, 20)).

Vì vậy chúng ta sẽ tiếp tục lặp tìm i trong phạm vi (n)

axs[i].plot và sẽ lấy mẫu của i

và chúng tôi sẽ dán nhãn vì đây sẽ là bản gốc.

Tiếp theo, chúng ta sẽ tiếp tục thực hiện axs[i].plot

(được xây dựng lại_samples).

Vì vậy, đây sẽ là mẫu được xây dựng lại của chúng tôi về i,

và sau đó chúng tôi sẽ gắn nhãn cái này là được xây dựng lại,

và sau đó chúng ta sẽ có một kiểu đường nét như thế này

để chúng ta có thể phân biệt giữa hai điều này.

Vì vậy hãy tiếp tục và đọc lại mã của chúng ta một lần nữa,

hãy chắc chắn rằng nó không có lỗi đánh máy.

Chúng tôi đã tạo ra một hàm gọi là tái thiết cốt truyện với mô hình

và 10 mẫu.

Sau đó chúng ta tiếp tục và tạo các mẫu.

Chúng tôi nói các mẫu được xây dựng lại = model.predict(samples).

Sau đó, chúng tôi chuẩn bị hình của chúng tôi.

Chúng tôi tạo một vòng lặp trong phạm vi n,

và sau đó chúng tôi tạo ra bản gốc.

Tiếp theo chúng ta tạo ra bản dựng lại.

Tiếp theo chúng ta sẽ tiếp tục và thêm chú thích vào nó.

Vậy axs[i].legend(),

sau đó chúng ta sẽ tiếp tục và lưu nó.

Vì vậy, fig.savefig("output/03_06_reconstruction_plot.png")

như mọi khi.

Vì vậy, chúng ta sẽ lưu hình của chúng ta vào thư mục đầu ra.

Tiếp theo, tất cả những gì chúng ta phải làm là gọi hàm này.

Vì vậy, hãy gọi hàm tiếp theo,

âm mưu tái thiết, không mất mát, tái thiết,

và sau đó chúng tôi sẽ cung cấp bộ mã hóa tự động ở đây.

Vì vậy, đây là bộ mã hóa tự động mà chúng tôi đã tạo ở trên.

Vì vậy, đó là những gì chúng tôi đang đưa vào hàm này

làm mô hình và sau đó chúng tôi có n mẫu.

Thế là xong.

Vậy chức năng này sẽ làm là chức năng này sẽ so sánh

dữ liệu gốc sang dữ liệu được xây dựng lại

cho n mẫu đầu tiên trong tập kiểm tra.

Nó vẽ cả giá trị ban đầu và giá trị được xây dựng lại

cho từng tính năng và nó sẽ cho phép chúng tôi

để đánh giá trực quan độ chính xác của việc xây dựng.

Vì vậy, hãy tiếp tục và phóng to khung bên trái.

Mã này sau đó sẽ tương tự

vào tệp python 03_06_end.

Vì vậy, hãy tiếp tục và chạy tập tin kết thúc

và sau đó để nó thực hiện điều kỳ diệu với bộ mã hóa tự động.

Sau đó chúng ta sẽ tiếp tục và mở rộng thư mục đầu ra,

và sau đó chúng tôi sẽ bình luận về phân tích

mà mã mang lại.

Vì vậy hãy để nó chạy trong vài phút.

Vì vậy chúng ta sẽ trải qua 20 kỷ nguyên ở đây.

Vì vậy, sau khi hoàn thành, hãy tiếp tục và cuộn lên

và xem thư mục đầu ra.

Lưu ý rằng chúng tôi đã tạo 03_06_loss_plot.

Sau đó, chúng tôi cũng đã tạo 03_06_reconstruction_plot.png.

Vì vậy, chúng tôi đã tạo ra hai hình.

Hãy bắt đầu từ cái đầu tiên.

Lưu ý, tôi đang thu nhỏ thiết bị đầu cuối bằng cách kéo nó xuống,

kéo dòng này xuống để tạo thêm không gian

vào khu vực chúng tôi đang xem xét để phân tích hình ảnh.

Vì vậy, chúng ta hãy nhìn vào biểu đồ mất đào tạo

giống như chúng tôi đã mở ngay bây giờ.

Đường màu cam thể hiện sự mất xác thực,

và đường màu xanh biểu thị sự mất mát ở đây,

đó là sự mất mát đào tạo.

Vì vậy, chúng tôi cũng có nhãn X, các kỷ nguyên, các lần lặp,

mà chúng tôi đã cho 20 trên nhãn X

và nhãn Y là tổn thất.

Vì vậy, tổn thất đào tạo, tức là đường màu xanh, rất thấp,

và nó vẫn khá nhất quán.

Vì vậy, điều này chỉ ra rằng mô hình đang học

để tái tạo lại dữ liệu huấn luyện một cách tốt nhất.

Khi chúng tôi nhìn vào sự mất mát xác thực,

đó là đường màu cam,

sự mất mát xác nhận rất khác nhau

và cao hơn nhiều so với tổn thất đào tạo.

Điều này cho thấy mô hình đang gặp khó khăn

để khái quát hóa dữ liệu chưa nhìn thấy,

cho thấy khả năng cho ăn quá mức

hoặc thiếu khả năng khái quát hóa.

Tiếp theo, chúng ta đang chuyển sang cốt truyện tái thiết.

Vì vậy, chúng tôi có nhiều lô ở đây.

Chuỗi biểu đồ đường so sánh dữ liệu gốc,

đó là những đường liền nét màu xanh dẫn đến dữ liệu được xây dựng lại

cho nhiều mẫu.

Vì vậy, dữ liệu được xây dựng lại là đường nét đứt màu cam,

và dữ liệu gốc là đường nét liền màu xanh.

Dữ liệu được xây dựng lại bám sát dữ liệu gốc

trong hầu hết các trường hợp, nhưng có những khác biệt nhỏ.

Vì vậy, điều này cho thấy bộ mã hóa tự động nhìn chung có hiệu quả

khi xây dựng lại dữ liệu đầu vào,

nhưng nó có thể có một số hạn chế,

đặc biệt là trong việc nắm bắt tất cả các chi tiết.

Vậy chúng ta có thể nói gì để kết luận về bước mã hóa tự động?

Vậy là mô hình autoencoding này đã thành công.

Nó được đào tạo thành công để xây dựng lại dữ liệu đầu vào

và kết quả cho thấy khả năng xây dựng hợp lý,

đặc biệt là đối với dữ liệu huấn luyện.

Sự khác biệt về mất xác nhận cho thấy rằng mô hình

có thể không khái quát hóa tốt, đặc biệt là đối với dữ liệu không nhìn thấy được.

Nó gợi ý rằng chúng ta có thể muốn xem xét

một số điều chỉnh thêm,

hoặc chúng ta có thể xem xét một mô hình phức tạp hơn

để cải thiện hiệu suất.

Khi chúng tôi nhìn vào các sơ đồ tái thiết,

họ xác nhận trực quan

rằng trong khi mô hình nắm bắt được xu hướng chung của dữ liệu,

vẫn còn những lỗi nhỏ trong quá trình tái thiết

và chúng đặc biệt đáng chú ý trong bộ xác thực.

Vì vậy, để kết luận, chúng ta có thể nói rằng bộ mã hóa tự động là

một loại mạng lưới thần kinh

được thiết kế để học cách biểu diễn dữ liệu một cách hiệu quả,

thường nhằm mục đích giảm kích thước.

Chìa khóa đằng sau việc này là nó cố gắng học cách mã hóa,

nói cách khác, một biểu diễn nén

của dữ liệu đầu vào và sau đó xây dựng lại dữ liệu đầu vào

từ mã hóa của nó.

Vậy là đã kết thúc phiên mã hóa của chúng ta.