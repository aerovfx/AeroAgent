# 70 - CNN trên CIFAR10 Dữ liệu tiếng Anh

---

Chào mừng mọi người trở lại, trong loạt bài giảng này, bây giờ chúng ta sẽ học cách xử lý màu sắc

dữ liệu và chúng tôi sẽ thực hiện điều này, tập dữ liệu Safah 10.

Vì vậy, phần một sẽ tập trung vào chính dữ liệu thực tế cũng như việc tạo mô hình của chúng tôi.

Và bộ dữ liệu SSAFA 10 là những hình ảnh lớn hơn một chút so với những gì chúng ta vừa xử lý ở đó, 32 x 32 hình ảnh

của mười đối tượng khác nhau.

Vì vậy, các loại đồ vật khác nhau có sẵn là máy bay, thẻ, chim, mèo, thiers, chó, v.v.

Và điều cần lưu ý chính là đây là những hình ảnh màu.

Hãy nhớ rằng, 32 x 30 vẫn còn khá nhỏ nhưng bạn sẽ có thể thấy một số mức độ chi tiết

con người có thể nhận ra những gì thực sự có trong hình ảnh.

Vì vậy, trong loạt bài giảng này, chúng tôi thực sự sẽ sử dụng lại rất nhiều thuật toán tích chập trước đó

mã mạng nơ-ron.

Vì vậy, thực sự điều chúng tôi sẽ tập trung vào là những bổ sung cần thiết nhờ sự ra đời của ba

các kênh màu.

Đó là các kênh màu đỏ, lục và lam.

Vì vậy, hãy mở một cuốn sổ tay và bắt đầu, chúng ta sẽ sao chép và dán khá nhiều đoạn mã

bởi vì khoảng 90 phần trăm mã giống hệt với loạt bài trước.

Đây chỉ là một vài bổ sung để xử lý ba kênh màu.

Hãy đi tới một cuốn sổ tay để bắt đầu.

Được rồi, ở đây, nhắm vào một cuốn sổ.

Tôi đã nhập những điều cơ bản.

Hãy tải lên tập dữ liệu của chúng tôi.

Cái này cũng được chế tạo thành ô tô cho mục đích học tập.

Chúng ta sẽ nói từ luồng tensor mang tập dữ liệu đó được nhập.

Cho đến nay, 10.

Và sau đó chúng ta sẽ tải nó thực sự giống như cách chúng ta đã làm lần trước.

Nó thực sự đã được chia cho chúng tôi khi chúng tôi sử dụng ít dữ liệu.

Chúng tôi tải lên các cặp đào tạo.

Và các cặp thử nghiệm.

Và sau đó chúng tôi đặt giá trị đó bằng SSAFA 10.

Dữ liệu thấp.

Hãy tiếp tục chạy nó và tải dữ liệu lên cho bạn và bây giờ chúng ta hãy xem hình dạng dữ liệu của chúng ta.

Vì vậy, bây giờ hãy chú ý rằng hình dạng này có thêm một chiều vì có ba kênh màu, vậy nên có

50000 hình ảnh, có 32 x 32 và có ba kênh màu, màu đỏ, xanh lục và xanh lam

kênh.

Vì vậy, chúng ta hãy nhìn vào chỉ một hình ảnh duy nhất.

Extranet số không.

Và chính là khu vực này đây.

Chúng ta hãy tiếp tục và kiểm tra hình dạng của nó.

Giả sử nó có kích thước 32 x 32 x 3, IMNSHO và cho bạn thấy hình ảnh gợi dục trông như thế nào.

Và hy vọng bạn có thể làm mờ tầm nhìn của mình một chút và thấy rằng đây là hình ảnh của một con ếch.

Và bạn có thể chuyển các số ngẫu nhiên vào đây trong phạm vi năm mươi nghìn điểm để xem các hình ảnh khác nhau.

Như vậy ở đây chúng ta có thể thấy đây là hình ảnh của một con ngựa.

Đây là những hình ảnh rất nhỏ.

Họ chỉ mới 32 x 32 thôi.

Nhưng ở đây có đủ thông tin để con người phát hiện ra thứ nó đang nhìn.

Hãy nhớ rằng một số trong số này kém rõ ràng hơn một chút.

Vì vậy, tôi chỉ chọn ngẫu nhiên ở đây, cái này, có lẽ đối với tôi ít rõ ràng hơn một chút.

Nó trông giống như một con nai và chúng ta có thể kiểm tra điều đó dựa trên nhãn.

Tôi tin rằng đây là một con nai, nhưng bạn có thể thấy rằng vì hình ảnh quá nhỏ nên một số trong số này là

chắc chắn sẽ bị phân loại sai.

Vì vậy, nó sẽ không đạt được hiệu suất tốt như chúng tôi đã làm trên tập dữ liệu.

Được rồi, ngay trước khi chúng ta cần thực hiện quá trình tiền xử lý ngay bây giờ, nếu chúng ta xem xét một trong những hình ảnh này

và yêu cầu giá trị tối đa.

Chúng đi từ 0 đến 255 cho mỗi kênh màu, vì vậy chúng ta sẽ làm điều tương tự như

trước đây.

Chúng ta sẽ nói đơn giản đoàn tàu X bằng đoàn tàu X chia cho 255.

Và hãy nhớ rằng bạn chỉ nên chạy các lệnh này một lần, nếu không bạn sẽ chia

hai năm mươi lăm lần.

Vì vậy, hãy ghi nhớ điều đó thì chúng ta sẽ nói số dư chia cho hai năm mươi lăm.

Hãy tiếp tục và chạy nó.

Và nếu chúng ta nhìn vào kích thước hoặc hình dạng dư thừa, có mười nghìn hình ảnh trong bộ thử nghiệm,

Được rồi.

Ngoài ra, giống như trước đây, nếu chúng ta xem dữ liệu huấn luyện Y của mình, bạn sẽ thấy rằng chính các nhãn

giống như chúng ta đã làm lần trước.

Chúng được gắn nhãn bởi một số nguyên.

Vì vậy, điều chúng ta thực sự cần không phải là đọc những giá trị này dưới dạng giá trị liên tục mà là giá trị phân loại.

Và cũng giống như trước đây, chúng ta có thể chuyển đổi điều này bằng cách nói luồng Tenzer mang các tiện ích nhập vào phân loại

và sau đó chúng ta sẽ chuyển đổi chúng thành phân loại.

Vì vậy, chúng ta sẽ nói rằng phân loại y cho tập huấn luyện của tôi bằng hai phân loại.

Về lý do đào tạo và chúng tôi có thể chỉ định rằng có mười lớp ở đây và chúng tôi sẽ làm điều tương tự.

Đối với bộ thử nghiệm của chúng tôi nhằm phân loại lý do tại sao thử nghiệm mười, cho đến nay, về việc định hình lại mọi thứ, không có gì

đã thay đổi so với những gì chúng tôi đã làm với hình ảnh đen trắng.

Việc chia tỷ lệ vẫn hoạt động giống hệt nhau, vì nếu không, may mắn thay, việc chia tỷ lệ cho hai năm mươi lăm xảy ra

trên cả ba chiều trên các kênh màu.

Vì vậy, nó được mở rộng trên tất cả những điều đó.

Vì vậy chúng ta không cần phải lo lắng về điều đó.

Và bản thân các nhãn, cũng giống như lần trước.

Chúng tôi chuyển đổi chúng thành các danh mục.

Và xin lưu ý nhanh, một câu hỏi phổ biến là, những con số này thực sự đại diện cho điều gì?

Bởi vì nếu chúng ta nhìn vào chẳng hạn.

Tại sao các bài kiểm tra số 0 lại gợi nhớ đến số ba đó, nếu chúng ta nhìn vào thực tế thì hãy nhìn vào tàu hỏa.

Vậy tại sao lại có con số 0?

Nó ghi nhãn là sáu.

Chà, giả sử Patti IMNSHO trên chuyến tàu X số 0 và chúng ta thấy kết quả là một con ếch.

Vậy làm thế nào để chúng ta biết rằng sáu thực sự kết nối con ếch?

Nếu bạn chỉ tìm kiếm trên Google cho đến nay, 10 tên nhãn sẽ hiển thị cho bạn.

Đó là danh sách.

Máy bay, số không là ô tô.

Vì vậy, tôi có thể thấy ở đây, con ếch sáu tuổi hoặc bạn có thể truy cập trang web chính thức bộ dữ liệu Safah Ten và nó có chúng

được tổ chức theo thứ tự đó.

Vì vậy, máy bay không phải là ô tô, v.v.

Vì vậy, đây là trang web chính thức.

Nếu bạn chỉ cần vào bộ dữ liệu Safah Ten rồi tra cứu trang web chính thức trên Google, bạn sẽ thấy

rằng cũng có một nhãn lớn hơn.

Vậy là có một trăm SSAFA.

Nhưng đó là một tập dữ liệu quá lớn để chúng tôi có thể chạy.

Và đó là những ý tưởng tương tự cho đến nay.

Được rồi, chúng ta sẽ quay lại với sổ ghi chép của mình.

Chúng tôi hiểu cách làm việc với dữ liệu.

Chúng tôi hiểu các nhãn.

Hãy tiếp tục và xây dựng mô hình của chúng tôi.

Và điều chúng ta sắp làm là tôi sẽ sao chép và dán một số mã này từ sổ ghi chép của mình vì

nó khá giống với những gì chúng ta đã làm lần trước.

Điều duy nhất chúng ta cần chỉnh sửa là hình dạng đầu vào.

Vì vậy, chúng ta hãy tiếp tục và xây dựng.

Mô hình tuần tự của chúng ta, giống như chúng ta đã làm trước đây, và hãy thêm vào một lớp chập, cũng như một

kéo lớp, tôi sẽ sao chép và dán mã này.

Từ sổ ghi chép của chúng ta rồi chỉ cần lưu ý những thay đổi, nên thay đổi chính ở đây vẫn sẽ sử dụng cùng một số

của các bộ lọc, cùng kích thước hạt nhân.

Tuy nhiên, hãy nhớ lại rằng hình dạng đầu vào được xác định bởi dữ liệu của chúng tôi.

Vậy ở đây sẽ là ba mươi hai nhân ba mươi hai nhân ba, đó là mức ổn ở đây.

Khi chúng tôi kiểm tra hình dạng thực tế của một hình ảnh, thử nghiệm tiếp theo là 32 x 32

bằng ba.

Được rồi, bây giờ khi bạn đang xử lý các hình ảnh phức tạp hơn, hãy nhớ lại rằng một hình ảnh duy nhất, nếu chúng ta chỉ

hãy xem hoặc nếu chúng ta nghĩ về số lượng pixel hoặc điểm dữ liệu thực sự bên trong một bức ảnh đen trắng

hình ảnh, tổng số giá trị là hai mươi tám lần hai mươi tám, là bảy trăm tám mươi.

Đối với tổng số giá trị trong một ảnh màu ở đây sẽ là ba mươi hai nhân ba, hai

nhân ba.

Như bạn có thể thấy, có nhiều thông tin hơn trong hình ảnh màu này so với hình ảnh trước đó.

và tập dữ liệu vì điều đó.

Có lẽ một ý tưởng hay là khi hình ảnh của chúng ta ngày càng phức tạp hơn, lớn hơn và cũng phức tạp hơn, chúng ta

thực hiện màu mà chúng ta thêm vào, nhiều lớp xoắn và kéo hơn.

Vì vậy, chúng ta sẽ tiếp tục sao chép và dán cái này và thêm vào một lớp chập khác cũng như một lớp khác

lớp.

Và thường thì các nhà nghiên cứu cũng muốn có số lượng bộ lọc khác nhau và số lượng lớp khác nhau

vì vậy bạn có thể mở rộng số lượng bộ lọc khi các lớp chập đi sâu hơn.

Đối với trường hợp sử dụng của chúng tôi, những hình ảnh này khá đơn giản, vì vậy chúng tôi sẽ giữ mọi thứ như cũ.

Được rồi, sau đó chúng ta sẽ tiếp tục và chỉ giữ nó ở hai lớp chập, tiếp theo là hai lớp kéo

và chúng ta sẽ làm phẳng các hình ảnh giống như chúng ta đã làm trước đây.

Vì vậy, chúng tôi làm phẳng hình ảnh.

Và do số điểm ở đây ngày càng phức tạp hơn khi chúng ta thêm vào lớp dày đặc của mình.

Chúng ta sẽ tiếp tục và thêm nhiều nơ-ron hơn vào nó, chúng ta sẽ nói là có hai trăm năm mươi sáu nơ-ron khi kích hoạt

hoạt động tương đương với Iraq để chiến đấu với đơn vị tuyến tính và cuối cùng mọi thứ khác sẽ diễn ra khá nhiều

người mẫu cũng sẽ nói như vậy.

Hãy tiếp tục và thêm sự tử tế.

Hàm kích hoạt phải bằng Softmax vì đây là hàm đa lớp và sau đó chúng ta

biên dịch mô hình Model S., biên dịch mất mát, có nên phân loại không?

Entropy chéo.

Bạn có thể chọn bất kỳ trình tối ưu hóa nào bạn muốn, chúng tôi sẽ tiếp tục và chọn trình tối ưu hóa mục phù hợp

ổn thôi.

Và nếu bạn muốn theo dõi các số liệu khác nhau, nhưng ngoài việc mất mát, chúng tôi có thể nói số liệu là

bằng và tôi có thể vượt qua.

Cuộc gọi chính xác đó, được chứ?

Chạy nó, đảm bảo bạn không có lỗi chính tả, có vẻ như việc đó đã diễn ra tốt đẹp.

Bạn có thể đặt hàng một bản tóm tắt về mô hình của bạn theo cùng một mô hình.

Tóm tắt đó ở đây, bạn có thể thấy các lớp khác nhau.

Và hãy tiếp tục và thêm tính năng dừng sớm để chúng ta sẽ nói từ luồng cảm biến.

Cuộc gọi lại của Doc Kerrisdale.

Dừng nhập sớm, giống như chúng tôi đã làm trước đây.

Chúng tôi sẽ tạo một cuộc gọi dừng sớm, chúng tôi sẽ nói dừng sớm.

Chúng tôi sẽ theo dõi sự mất mát.

Bạn cũng có thể theo dõi độ chính xác về mặt kỹ thuật nếu đó là số liệu quan trọng nhất của bạn và sau đó hãy

cho nó một bệnh nhân gồm hai người.

Và hãy để phù hợp với điều này sẽ nói, một mô hình phù hợp với dữ liệu huấn luyện.

Hãy đảm bảo rằng bạn khớp chính xác với các phiên bản phân loại của nhãn, chẳng hạn như kỷ nguyên, hãy sử dụng

một số lượng lớn hơn

Có thể sẽ không thay đổi hoặc huấn luyện cho tổng cộng 15 người, nhưng chúng tôi dừng lại sớm để đảm bảo

bạn chỉ định dữ liệu xác thực của mình tương đương với thử nghiệm X và thử nghiệm phân loại Y.

Và cuối cùng thêm vào các cuộc gọi lại.

Đối với việc dừng lại sớm.

Phù hợp với điều đó, hãy đảm bảo bạn thấy đầu ra đầu tiên đó để đảm bảo rằng bạn đang thực hiện việc này một cách chính xác và đó là

khá nhiều đấy.

Vì vậy, bạn nhận thấy ở kỷ nguyên đầu tiên này, độ chính xác không được tốt lắm.

Nhưng khi chúng ta tiếp tục huấn luyện, chúng ta sẽ thấy độ chính xác của dê tăng lên.

Và đó là điều thú vị khi thêm độ chính xác khi gọi số liệu ở đây, bởi vì nó khá

khó có thể giải thích luật ngoài việc nó sẽ đi xuống.

Điều tuyệt vời là tôi thực sự có thể diễn giải độ chính xác một cách rất trực quan và có thể thấy nó tăng dần theo thời gian

được đào tạo ngày càng xa hơn.

Được rồi, một điều nữa cần lưu ý là độ chính xác mặc định bằng cách đoán ngẫu nhiên thực tế phải là 10

phần trăm.

Vì vậy thực tế là chúng ta đang đạt trên 10 phần trăm là thực sự tốt và chúng ta sẽ còn vượt xa hơn thế, bởi vì

nếu bạn đoán ngẫu nhiên lớp và hình ảnh nào thuộc về bạn, bạn sẽ có 10% cơ hội

làm cho nó đúng.

Nhưng ở đây, dựa trên Kỷ nguyên thứ bảy, chúng tôi đã thực hiện độ chính xác 0,75 phần trăm đó.

Vì vậy, chúng tôi đang làm khá tốt trên tập dữ liệu này.

Được rồi.

Tôi sẽ kết thúc bài giảng này ở đây.

Và phần tiếp theo, chúng ta sẽ nói về việc đánh giá mô hình và chúng ta cũng sẽ nói về việc thực hiện các dự đoán

trên dữ liệu mới.

Tôi sẽ gặp bạn ở đó.