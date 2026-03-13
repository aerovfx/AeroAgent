# 04 - Demo kỹ thuật nhanh chóng với FLAN-T5

---

- [Giảng viên] Được rồi, chào mừng mọi người

đến bản demo đầu tiên của khóa học này.

Tất cả các bản demo trong khóa học này

sẽ sử dụng Google Colaboratory.

Nói ngắn gọn, Google Colab là một nền tảng

nơi chúng ta có thể đặt các tập tin sổ ghi chép của mình,

và nó sẽ kết nối chúng ta miễn phí

đến một phiên bản trong nền tảng Google Cloud

nơi chúng tôi cũng có thể kết nối GPU.

Tất nhiên điều này rất hữu ích,

đặc biệt là đối với các ý tưởng tạo mẫu.

URL của Colab là colab.research.google.com.

Vì vậy, một khi bạn đến đó,

bạn sẽ đến một trang như thế này,

và tôi sẽ cho bạn thấy

chúng ta sẽ tải sổ ghi chép lên như thế nào cho lần này,

từ các tập tin Bài tập.

Vì vậy, chúng tôi chuyển đến tập tin, tải sổ ghi chép lên,

và ở đây chúng ta sẽ duyệt qua.

Và chúng ta sẽ đi đây,

có các tập tin bài tập của tôi trên Máy tính để bàn, Chương 2,

và sau đó chúng ta có Chương 2 Demo1.

Vì vậy chúng ta sẽ mở nó ra,

và thông báo rằng nó sẽ tải lên.

Và thế là xong. Chúng tôi có sổ ghi chép của chúng tôi.

Đây là sổ ghi chép Jupyter truyền thống,

nhưng mọi thứ đã được cấu hình sẵn cho bạn.

Lưu ý rằng nếu chúng ta nhấp vào kết nối,

nó sẽ kết nối bạn với GPU tốt nhất hiện có.

Vì vậy, bây giờ nó đang kết nối,

bạn có thể thấy đó là một cuốn sổ tay bình thường.

Bạn sẽ có văn bản và bạn sẽ có mã.

Ở đó chúng ta có thể thấy rằng bây giờ chúng ta đã được kết nối,

và thực tế nếu bạn nhấp vào đây,

bạn có thể thấy trong trường hợp này chúng ta có 83 gigabyte RAM,

và GPU có 40 gigabyte.

Tôi không thể đảm bảo với bạn loại GPU nào bạn sẽ nhận được

bởi vì nó phụ thuộc vào tình trạng sẵn có, đó là múi giờ của bạn,

khi nào bạn kết nối,

và liệu gần đây bạn có sử dụng nhiều GPU hay không.

Được rồi, đó là một chuyện.

Nó phụ thuộc vào tình trạng sẵn có vì nó miễn phí.

Vậy điều đầu tiên chúng ta phải làm

hãy nhớ cài đặt Transformers và TensorFlow.

Nó đây rồi. Chúng ta có thể thấy rằng nó đã kết thúc.

Và bây giờ chúng tôi đã làm được điều đó,

sau đó chúng ta có thể tải mã thông báo và mô hình của mình.

Hãy nhớ rằng chúng ta cần sử dụng TFAutoModel.

TF cho Tensorflow.

Mô hình tự động vì thay vì chỉ tải xuống LLM,

nó sẽ bổ sung thêm các đầu mục cho nhiệm vụ của chúng ta.

Và chúng ta sẽ làm nhiệm vụ gì?

Vâng, trong nhiệm vụ của chúng tôi sẽ là một chuỗi nối tiếp nhau,

do đó nó sẽ là Seq2SeqLM.

AutoTokenizer luôn giống nhau

và mô hình là google/flan-t5-large,

đó là một mô hình rất tốt

Vì vậy, chúng ta sẽ nhấp vào đây và việc này sẽ mất một chút thời gian

bởi vì nó cần tải xuống tất cả LLM.

Được rồi, nó đây rồi. Chúng tôi đã thấy rằng nó đã tải xuống LLM.

Hãy để tôi đề cập một chút về những cảnh báo này.

Vì vậy, loại cảnh báo đầu tiên chỉ là

bởi vì tôi đã không xác thực

với người dùng của tôi là ôm mặt,

nhưng nó siêu ổn và nó bình thường.

Và chúng ta đi xuống, nó sẽ cho bạn biết cảnh báo thứ hai.

Một lần nữa, không sao cả, nhưng bạn cần biết về điều này.

Nó sẽ cho bạn biết mô hình này

thực sự đã được đào tạo thành người mẫu PyTorch

và sau đó họ săn trộm nó,

chúng có nghĩa là ôm mặt, theo TensorFlow.

Được rồi?

Bạn sẽ có tỷ lệ chẵn lẻ bằng 99,9%,

nhưng họ chỉ nói với bạn trong trường hợp

mà bạn biết nó thực sự được đào tạo trên nền tảng nào.

Và bây giờ chúng tôi đã sẵn sàng.

Đầu tiên chúng ta sẽ thực hiện tóm tắt,

nhưng hãy nhớ rằng việc nhắc LLM luôn phải thực hiện bốn bước,

xác định lời nhắc, chuyển qua mã thông báo,

sử dụng mô hình tạo ra,

và sau đó giải mã bằng mã thông báo.

Vì vậy, lời nhắc đầu tiên của chúng ta sẽ là lời nhắc tóm tắt.

Trong T5, nó rất quan trọng

để đặt nhiệm vụ thực tế trên một cột

ở đầu lời nhắc.

Trong trường hợp này, cột tóm tắt,

và sau đó là phần còn lại của văn bản.

Trong trường hợp này, văn bản sẽ

nghiên cứu cho thấy ăn cà rốt giúp cải thiện thị lực

và họ bắt đầu nói về cà rốt

và chúng chứa vitamin A như thế nào.

Hoàn hảo. Bước tiếp theo sẽ là về tokenizer.

Chúng tôi vượt qua lời nhắc và ghi nhớ,

đầu tiên chúng ta cần đặt các tenxơ trả về thành tf.

Điều đó có nghĩa là các tensor mà chúng ta thu được cho mô hình

sẽ là các tensor TensorFlow.

Tiếp theo, chúng ta cần đặt độ dài tối đa

với giá trị thực tế từ mô hình.

Từ các slide trên clip trước của chúng tôi,

chúng tôi biết đó là 512.

Vì một số lời nhắc có thể dài hơn hoặc ngắn hơn 512 từ,

chúng ta cần đặt phần cắt ngắn thành true nếu nó dài hơn

và đệm thành đúng nếu nó ngắn hơn.

Sau đó chúng tôi có đầu vào của chúng tôi.

Tiếp theo là mô hình tạo ra.

Điều đó sẽ lấy đầu vào trên ID đầu vào một cách cụ thể

và chúng tôi sẽ chỉ định độ dài tối đa.

Điều đó có nghĩa là số lượng từ tối đa là bao nhiêu

chúng tôi muốn mô hình tạo ra.

Số_đậu và điểm dừng sớm,

hãy nhớ cấu hình của chúng tôi,

để kiểm soát cách văn bản được tạo ra.

Và bây giờ nó không quan trọng.

Bạn thậm chí có thể xóa chúng nếu bạn muốn

và nó sẽ vẫn ổn thôi.

Đầu ra sẽ là ID, một tensor ID.

Mỗi ID đại diện cho một từ.

Vì vậy bước cuối cùng cần phải thông qua tokenizer

giải mã để lấy lại

những ID đó thành từ.

Nếu chúng ta chạy cái này, sẽ mất một chút thời gian

và chúng tôi sẽ nhận được phản hồi từ mô hình của chúng tôi.

Và chúng ta đây, phản hồi từ người mẫu.

Có thể nói đó là một bản tóm tắt khá ngắn. Ăn cà rốt.

Được rồi, không phải là nó sai.

Có lẽ nó có thể tốt hơn một chút.

Chúng ta sẽ xem qua khóa học và chương,

làm cách nào chúng tôi có thể cải thiện một chút lời nhắc của mình

để làm cho những bản tóm tắt này ngày càng tốt hơn,

nhưng bạn có thể thấy rằng toàn bộ quy trình làm việc đã hoạt động.

Và việc dịch thuật cũng vậy.

Ví dụ: dịch tiếng Anh sang tiếng Tây Ban Nha,

phô mai rất ngon.

Và một lần nữa, tokenizer có cùng lý lẽ như trước,

mô hình tạo ra với các đối số giống như trước.

Tôi đặt độ dài tối đa lên 40 để tăng tốc

và sau đó chúng tôi mã thông báo để giải mã.

Nếu chúng ta chạy cái này,

(người hướng dẫn nói tiếng Tây Ban Nha)

và đó là một bản dịch chính xác.

Và nếu bạn không nói được tiếng Tây Ban Nha, hãy tin tôi.

Tôi đến từ Argentina nên tôi nói được tiếng Tây Ban Nha.

Và sau đó là bản demo nhỏ này, chúng ta hãy hỏi và đáp.

Hãy nhớ Q và A có nghĩa là

mà chúng ta sẽ đưa ra một khoảng thời gian bối cảnh,

thì chúng ta sẽ giao nhiệm vụ,

đó sẽ là một câu hỏi,

và sau đó dựa trên bối cảnh đó

và những gì nó đã biết về LLM, nó sẽ trả lời.

Vì vậy, câu hỏi ngữ cảnh của chúng tôi sẽ là

Vạn Lý Trường Thành của Trung Quốc dài hơn 13.000 dặm.

Đó là thông tin của chúng tôi.

Tôi cố ý làm nó ngắn lại.

Tất nhiên, bạn có thể làm nó bao lâu tùy thích.

Dấu hai chấm câu hỏi, rất quan trọng ở T5, hãy nhớ nhé.

Vạn Lý Trường Thành của Trung Quốc dài bao nhiêu?

Chúng ta thực hiện các bước tương tự

và chúng tôi nhận lại câu trả lời của mình.

Nó dài hơn 13.000 dặm.

Điều đó có nghĩa là không chỉ cơ chế của chúng tôi

để nhắc LLM thành công, chỉ cần bốn bước,

nhưng LLM của chúng tôi cũng hoạt động.

Cái này, chỉ cái này khi bạn có nó,

bạn có thể đặt nó vào bất kỳ chatbot nào

và bạn đã có thể tăng cường nó bằng LLM.

Vậy là bạn đã có rất nhiều quyền lực trong tay rồi

mà không cần phải làm nhiều thứ.