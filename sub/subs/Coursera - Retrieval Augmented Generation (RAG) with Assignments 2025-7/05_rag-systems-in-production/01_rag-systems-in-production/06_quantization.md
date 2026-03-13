# 06 lượng tử hóa

---

Khi bạn có thể đánh giá hệ thống RAG của mình và thử nghiệm các cấu hình khác nhau,

bạn sẽ sẵn sàng chấp nhận một số sự đánh đổi quen thuộc trong nhiều dự án phần mềm. Chi phí, tốc độ và

chất lượng.

Bạn sẽ khám phá những sự đánh đổi này trong một số video tiếp theo, nhưng trước tiên hãy giới thiệu một khái niệm quan trọng,

lượng tử hóa. Nói tóm lại, lượng tử hóa là quá trình nén cho cả LLM và vectơ được tạo bằng các mô hình nhúng.

Lượng tử hóa thay thế các trọng số mô hình bên trong LLM hoặc các giá trị của vectơ nhúng bằng một vectơ nén,

loại dữ liệu có độ chính xác thấp hơn.

Điều này làm cho các mô hình hoặc vectơ tương ứng nhỏ hơn, rẻ hơn và chạy nhanh hơn mà thường không phải hy sinh nhiều về mặt

sự liên quan truy xuất hoặc chất lượng phản hồi. Chúng ta hãy xem nó hoạt động như thế nào. Một sự tương tự tốt cho

lượng tử hóa là nén hình ảnh.

Hình ảnh chất lượng cao này sử dụng 24 bit dữ liệu để thể hiện màu sắc ở mỗi pixel. Màu sắc trông tuyệt vời,

nhưng nó sử dụng khá nhiều dữ liệu để lưu trữ tất cả thông tin đó.

Bạn có thể nén hình ảnh bằng cách sử dụng 12 hoặc thậm chí 6 bit cho mỗi pixel.

Hình ảnh nén có kích thước bằng 1/2 và 1/4 kích thước của ảnh gốc, giúp tiết kiệm bộ nhớ đáng kể.

Điều đó có nghĩa là hình ảnh 12 bit trông không đẹp bằng và trong hình ảnh 6 bit, có nhiều hiện tượng màu sắc có thể nhìn thấy được.

Tuy nhiên, tùy thuộc vào nơi bạn đang sử dụng hình ảnh, việc giảm chất lượng này có thể đáng để tiết kiệm bộ nhớ đáng kể.

Lượng tử hóa có cách tiếp cận tương tự với LLM và vectơ nhúng,

thu nhỏ kích thước của chúng với một số tổn thất về chất lượng như một sự đánh đổi.

Hãy bắt đầu bằng cách xem nó hoạt động như thế nào đối với LLM.

Các tham số trong mô hình ngôn ngữ điển hình sử dụng mỗi tham số 16 bit bộ nhớ.

Với các mô hình hiện đại có thông số từ khoảng một tỷ đến một nghìn tỷ, những mô hình này rất lớn,

cần nhiều bộ nhớ để lưu trữ chúng và GPU mạnh để chạy chúng.

Các mô hình lượng tử hóa nén các tham số 16 bit đó xuống còn 8 hoặc thậm chí 4 bit tương đương.

Điều này làm giảm đáng kể bộ nhớ GPU cần thiết để chạy mô hình với cái giá là hiệu năng và chất lượng của mô hình bị giảm đi một chút.

Các vectơ nhúng lượng tử hóa hoạt động tương tự.

Một vectơ 768 chiều khá điển hình sẽ sử dụng 768 số dấu phẩy động 32 bit.

Đó là 3 kilobyte dữ liệu cho mỗi vectơ trong cơ sở kiến ​​thức của bạn.

Các mô hình có chiều cao hơn có thể dễ dàng yêu cầu gấp nhiều lần như vậy.

Khi bạn đang lưu trữ hàng triệu hoặc thậm chí hàng tỷ vectơ này, bạn sẽ có một lượng lớn dữ liệu vectơ để xử lý.

Các vectơ này cần được lưu trữ ở đâu đó để sử dụng chúng và đặc biệt nếu bạn muốn sử dụng chúng trong tìm kiếm vectơ nhanh,

chúng cần được nạp vào RAM đắt tiền.

Lượng tử hóa số nguyên là một phương pháp thường được sử dụng để thu nhỏ các vectơ này.

Nó thay thế các số dấu phẩy động 32 bit bằng một số nguyên nhỏ hơn nhiều, ví dụ: số nguyên 8 bit.

Điều này có nghĩa là vectơ của bạn bây giờ ngay lập tức có kích thước bằng một phần tư kích thước ban đầu, tiết kiệm không gian đáng kể.

Những giá trị số nguyên này cũng rất dễ tính toán.

Đây là cách quá trình hoạt động.

Bạn tìm thấy các giá trị tối thiểu và tối đa xuất hiện trong mỗi thứ nguyên cho dữ liệu vectơ của mình.

Điều này sẽ xác định phạm vi mà các giá trị trong thứ nguyên đó sẽ nằm trong đó.

Sau đó, bạn chia phạm vi đó thành 256 phần có kích thước bằng nhau.

Số lượng giá trị duy nhất bạn có thể tạo với 8 bit.

Các phần đó sau đó được đánh số 0, 1, 2, 3, v.v. cho đến 255.

Sau đó, mỗi số dấu phẩy động từ vectơ ban đầu của bạn chỉ được gán một giá trị nguyên bằng bất kỳ phần nào mà nó nằm trong đó.

Nếu bạn cũng lưu trữ giá trị tối thiểu và độ rộng của từng phần, bạn sẽ có tất cả thông tin cần thiết để tính toán xấp xỉ số float 32 bit ban đầu nhưng chỉ sử dụng 8 bit dữ liệu.

Mặc dù chỉ sử dụng một phần tư dữ liệu và thuật toán nén có vẻ đơn giản, lượng tử hóa số nguyên 8 bit hoạt động rất tốt.

Đối với các điểm chuẩn như Thu hồi ở K, bạn có thể chỉ thấy giảm một vài điểm phần trăm với lượng tử hóa 8 bit.

Trong khi đó, các vectơ nhúng được lượng tử hóa này cho phép lưu trữ ít dữ liệu hơn trong cơ sở dữ liệu vectơ của bạn đồng thời hỗ trợ tìm kiếm nhanh hơn vì các phép tính cần thiết đã được đơn giản hóa.

LLM được lượng tử hóa cũng thường chỉ giảm hiệu suất một chút khi được đo bằng các điểm chuẩn được tham chiếu phổ biến.

Trong khi đó, chúng sử dụng ít bộ nhớ GPU hơn và có thể tạo văn bản nhanh hơn.

Nói cách khác, đây là mức tăng bộ nhớ và hiệu suất rất lớn nhưng chất lượng lại giảm một chút.

Trong khi các vectơ lượng tử hóa số nguyên 8 bit được sử dụng phổ biến thì các vectơ lượng tử hóa 1 bit hoặc nhị phân cũng đang trở nên phổ biến.

Cách tiếp cận này nén kích thước của vectơ theo hệ số 32, từ 32 bit trên mỗi chiều xuống chỉ còn 1 bit, đây là một mức tiết kiệm lớn.

Ở mức nén này, mỗi giá trị trong vectơ của bạn là 1 hoặc 0 và chỉ cho bạn biết giá trị đó ở thứ nguyên đó là số dương hay số âm.

Như bạn có thể tưởng tượng, ở những mức nén cực độ này, hiệu suất có thể giảm đáng kể khi nhúng truy xuất dựa trên mô hình.

Điều đó cho thấy, lượng tử hóa 1 bit mang lại kết quả truy xuất dựa trên vectơ nhỏ hơn và nhanh hơn đáng kể.

Nó cũng có thể được ghép nối với các kỹ thuật khác, chẳng hạn như thực hiện truy xuất nhanh dựa trên mô hình nhúng lượng tử hóa 1 bit, sau đó ghi lại bằng cách sử dụng vectơ 32 bit gốc đầy đủ.

Một cách khác để thu nhỏ kích thước vectơ của bạn là sử dụng mô hình nhúng Matryoshka, dựa trên từ tiếng Nga có nghĩa là búp bê làm tổ.

Các vectơ này được thiết kế sao cho bạn có thể chọn chỉ sử dụng một tập hợp con kích thước của vectơ khi thực hiện những việc như so sánh độ tương tự.

Ví dụ: nếu vectơ đầy đủ có 1000 thứ nguyên, bạn có thể chọn chỉ sử dụng 500 thứ nguyên đầu tiên hoặc 100 thứ nguyên đầu tiên.

Để kích hoạt hành vi này, các mô hình nhúng Matryoshka có một thuộc tính đặc biệt.

Kích thước của chúng được sắp xếp theo mức độ dày đặc thông tin của chúng.

Ở đây, thông tin có nghĩa là mức độ khác biệt thống kê mà bạn mong đợi thấy trong thứ nguyên đó khi nhúng số lượng lớn văn bản.

Trong một mô hình nhúng điển hình, mọi thứ nguyên sẽ có lượng phương sai hoặc thông tin gần như giống nhau.

Trong mô hình Matryoshka, nhờ sử dụng quy trình huấn luyện, các chiều trước đó sẽ có nhiều phương sai hơn, đồng nghĩa với việc có nhiều nội dung thông tin hơn.

Các kích thước sau này có ít phương sai hơn, nghĩa là chúng cung cấp ít thông tin hơn và do đó bạn phải trả ít tiền phạt hơn khi loại trừ chúng.

Có một số cách để sử dụng vectơ Matryoshka.

Bạn có thể chọn chỉ sử dụng 100 chiều đầu tiên, tiết kiệm không gian và dẫn đến tính toán nhanh hơn, đồng thời bảo toàn lượng thông tin tối đa có thể.

Hoặc bạn luôn có thể thực hiện truy xuất ban đầu bằng cách sử dụng 100 thứ nguyên đầu tiên, sau đó kéo 900 thứ nguyên còn lại, hiện đang sử dụng toàn bộ 1000 thứ nguyên, với bộ nhớ chậm hơn, rẻ hơn để giúp ghi lại bộ tài liệu ban đầu mà bạn đã truy xuất.

Các đặc tính linh hoạt của mô hình Matryoshka làm cho nó phù hợp nhất với môi trường động, nơi bạn có thể muốn nhanh chóng chuyển từ biểu diễn vectơ có độ chính xác thấp sang cao.

Mặc dù các kỹ thuật nâng cao này cho thấy những gì có thể xảy ra ở mức độ tiên tiến của lượng tử hóa, nhưng điểm mấu chốt là bạn có thể nên thử nghiệm bằng cách sử dụng LLM lượng tử hóa số nguyên và các mô hình nhúng.

Hầu hết các nhà cung cấp mô hình nhúng và LLM sẽ cung cấp các mô hình lượng tử hóa 8 hoặc 4 bit cùng với các mô hình cơ sở của họ.

Tiết kiệm không gian và chi phí mà chúng mang lại có thể là đáng kể và mức giảm chất lượng là khá nhỏ.