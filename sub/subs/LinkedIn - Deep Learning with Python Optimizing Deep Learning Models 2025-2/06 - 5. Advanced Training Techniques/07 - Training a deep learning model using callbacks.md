# 07 - Đào tạo mô hình deep learning sử dụng callbacks

---

- [Người hướng dẫn] Trong video này,

bạn sẽ học cách sử dụng lệnh gọi lại

để áp dụng việc dừng sớm và lập kế hoạch tỷ lệ tuyến tính

đến mô hình học sâu trong Python.

Tôi sẽ chạy mã trong tệp 05_07e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 05_07b.

Biết rằng đây là video thứ ba trong chuỗi ba video

hướng dẫn bạn cách áp dụng chuẩn hóa hàng loạt,

cắt độ dốc, dừng sớm,

và lập kế hoạch tốc độ học tập cho một mô hình học sâu.

Nếu bạn chưa làm như vậy, hãy xem các video khóa học trước

về cách áp dụng chuẩn hóa hàng loạt cho mô hình học sâu

và cách áp dụng cắt chuyển màu

sang mô hình học sâu.

Những video đó cung cấp lời giải thích chi tiết

của mã trước đó.

Trước khi chúng ta bắt đầu,

hãy chạy đoạn mã chúng ta đã tạo trong những video đó

để môi trường của chúng ta tăng tốc.

Vì vậy, như chúng ta đã làm trong quá khứ,

điều đầu tiên chúng tôi muốn làm là chọn kernel của mình.

Bạn có thể nói môi trường Python trong 3.10.

Sau đó tôi sẽ nhấp vào ô mã hiện tại của mình

và tôi sẽ nói chạy các ô mã trước đó.

Tôi cuộn lên một chút để có thể theo dõi tiến trình.

Được rồi, vậy là chúng ta đã xong việc ở đó.

Trong Keras, một cuộc gọi lại là một đối tượng

có thể thực hiện các hành động tùy chỉnh

tại những thời điểm cụ thể trong quá trình đào tạo,

chẳng hạn như ở cuối mỗi kỷ nguyên hoặc đợt.

Một trong những lệnh gọi lại được sử dụng phổ biến nhất là EarlyStopping,

theo dõi một số liệu cụ thể, chẳng hạn như mất xác thực,

và ngừng đào tạo nếu số liệu đó không cải thiện

sau một số kỷ nguyên xác định,

điều đó được gọi là sự kiên nhẫn.

Điều này giúp ngăn chặn việc trang bị quá mức

bằng cách tạm dừng đào tạo khi mô hình

đã đạt được hiệu suất tối ưu trên bộ xác thực.

Vì vậy, để triển khai EarlyStopping,

chúng ta sẽ nhập Early_stopping bằng keras.callbacks.

Vì vậy bây giờ chúng ta sẽ chỉ định

các thông số kỹ thuật dừng sớm.

Chúng ta sẽ gọi hàm Early_stopping.

Chúng tôi sẽ chỉ định số liệu cần theo dõi,

đó là mất xác nhận,

chỉ rõ sự kiên nhẫn mà chúng ta đã học trước đó,

và chúng ta sẽ nói rằng Restore_best_weights bằng true,

điều đó có nghĩa là bất cứ khi nào chúng ta nhận ra

rằng trọng lượng mà chúng ta có trước đây

tốt hơn những gì chúng ta hiện có,

chúng ta nên khôi phục lại những cái đó, được chứ?

Vì vậy hãy tiếp tục và chạy cái này

để xác định các thông số kỹ thuật dừng sớm.

Một cuộc gọi lại thường được sử dụng khác trong Keras

là GiảmLROnPlateau.

Điều này thực hiện lập kế hoạch tốc độ học tập.

Với cuộc gọi lại này,

tốc độ học tập được tự động giảm

khi số liệu được theo dõi đã ngừng cải thiện.

Vì vậy, đây là điều mà chúng ta đã nói đến

trong video trước.

Vì vậy, để thực hiện lập kế hoạch tỷ lệ học tập ở đây

sử dụng GiảmLROnPlateau,

chúng tôi sẽ tiếp tục và nhập GiảmLROnPlateau

từ keras.callbacks.

Sau đó chúng tôi xác định các yêu cầu

hoặc các thông số kỹ thuật cho nó.

Muốn theo dõi việc mất xác thực.

Muốn nói đến yếu tố

mà chúng tôi muốn giảm tỷ lệ học tập xuống 0,1 mỗi lần.

Thời gian kiên nhẫn là hai,

và tốc độ học tối thiểu mà chúng ta muốn có là 0,0001.

Được rồi? Vì vậy, hãy tiếp tục và xác định điều đó ở đây.

Được rồi, sau khi chúng ta đã chỉ định cả hai lệnh gọi lại này,

dừng sớm và lập kế hoạch tốc độ học tập,

sử dụng GiảmLROnPlateau,

bây giờ chúng ta có thể sử dụng các lệnh gọi lại này để huấn luyện mô hình của mình.

Vì vậy, khi xác định lệnh gọi lại của chúng tôi,

chúng ta có thể kết hợp chúng thành một danh sách

và chuyển chúng tới đối số gọi lại trong phương thức fit.

Vì vậy chúng ta sẽ tiếp tục

và tạo danh sách gọi lại, my_callbacks.

Tạo danh sách những người dừng lại sớm

và lập kế hoạch tốc độ học tập.

Bây giờ chúng ta sẽ điều chỉnh mô hình của mình, vì vậy chúng ta chỉ định model.fit,

dữ liệu huấn luyện, nhãn, số kỷ nguyên,

sự phân chia, kích thước lô,

và sau đó trong các cuộc gọi lại, chúng tôi chỉ định danh sách gọi lại

mà chúng tôi vừa thực hiện.

Vì vậy, hãy tiếp tục và sử dụng nó ở đây.

Và vì vậy hãy cho phép mô hình của chúng tôi đào tạo.

Vì vậy, chúng tôi sẽ xác định 20 kỷ nguyên,

vì vậy hãy chú ý điều đó một cách cẩn thận ở đây.

Vậy hãy cho bạn chút thời gian ở đây

để làm việc thông qua quá trình của nó.

Người mẫu vẫn đang được đào tạo,

và chúng tôi nhận thấy rằng quá trình đào tạo đã dừng lại ở 11.

Được chứ? Thật thú vị.

Mặc dù chúng tôi đã chỉ định 20 kỷ nguyên

trong phương pháp phù hợp ở đây,

chỉ có 11 kỷ nguyên được thực thi.

Điều này là do dừng lại sớm.

Đây chính xác là những gì chúng tôi mong đợi sẽ xảy ra ở đây.

Vì vậy đã phát hiện dừng sớm

rằng việc mất xác nhận đã không được cải thiện

cho khoảng thời gian kiên nhẫn được cấu hình là ba.

Vì vậy nó đã tạm dừng quá trình huấn luyện trước khi đạt đến kỷ nguyên 20.

Vì vậy, bây giờ hãy vẽ sơ đồ các chỉ số mất mát trong quá trình đào tạo và xác thực

để hiểu rõ hơn về mô hình của chúng tôi hoạt động như thế nào.

Vì vậy chúng ta thấy rằng những gì đang diễn ra ở đây

là mô hình của chúng tôi đã được cải thiện.

Vì vậy, chúng ta thấy sự mất mát giảm đi,

và sau một thời gian, nó bắt đầu ổn định,

vì vậy đó là lý do tại sao nó cuối cùng đã dừng lại.

Vì vậy, sau khi thêm chuẩn hóa hàng loạt, cắt bớt độ dốc,

dừng sớm và lập kế hoạch tốc độ học tập

đến quá trình đào tạo của chúng tôi,

chúng tôi đã giới thiệu nhiều phương pháp

giúp ổn định và tối ưu hóa

hành vi của mô hình học sâu của chúng ta, phải không?

Và vì vậy mỗi kỹ thuật này

giải quyết những cạm bẫy tiềm ẩn khác nhau trong đào tạo mô hình,

từ chuyển màu bùng nổ đến trang bị quá mức,

và cùng nhau, tất cả đều tạo ra một mô hình

hội tụ đáng tin cậy hơn

và khái quát hóa tốt hơn về dữ liệu chưa nhìn thấy.

Vì vậy, xin chúc mừng.

Nếu bạn đã theo dõi cả ba video,

điều đó có nghĩa là bây giờ bạn đã biết cách áp dụng chuẩn hóa hàng loạt,

cắt độ dốc, dừng sớm,

và lập kế hoạch tốc độ học tập

đến mô hình học sâu bằng Python bằng Keras.