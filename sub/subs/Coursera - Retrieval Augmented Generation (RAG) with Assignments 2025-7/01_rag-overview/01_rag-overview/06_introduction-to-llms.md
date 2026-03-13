# 06 phần giới thiệu phim

---

Bây giờ bạn đã thấy kiến trúc cấp cao của hệ thống RAG,

chúng ta hãy xem xét kỹ hơn từng thành phần,

bắt đầu với chính mô hình ngôn ngữ lớn.

Hiểu cách họ hoạt động,

điểm mạnh và hạn chế của họ,

sẽ giúp giải thích cách các thành phần khác trong

hệ thống RAG được thiết kế để cải thiện hiệu suất của LLM.

LLM đôi khi được gọi đùa là tự động hoàn thành ưa thích.

Nhưng đó thực sự là một mô tả công bằng.

Tất cả những gì LLM làm là dự đoán

từ tiếp theo sẽ xuất hiện trong một đoạn văn bản.

Ví dụ: nếu tôi cho bạn xem cụm từ chưa hoàn chỉnh,

Thật là một ngày đẹp trời mặt trời chấm, chấm, chấm.

Bạn và tôi có thể đoán được từ nào nên dùng để hoàn thành câu đó,

và LLM cũng vậy.

Tôi cho rằng từ tỏa sáng có ý nghĩa nhất,

nhưng mặt trời đang mọc hoặc mặt trời lặn cũng có thể có tác dụng.

Cụm từ ban đầu được gọi là lời nhắc,

và mỗi cụm từ hoàn chỉnh cuối cùng này được gọi là phần hoàn thành.

Một khả năng có thể hoàn thành cho lời nhắc này là mặt trời đang nổ tung.

Nhưng có lẽ bạn sẽ nói điều đó không chính xác.

Vấn đề không phải là cụm từ đó có sai sót về mặt ngữ pháp,

đó là tiếng Anh hợp lệ, nhưng cụm từ này không thể thực hiện được.

Mặt trời thường không nổ tung,

chắc chắn không phải vào một ngày đẹp trời như thế này.

Bạn có trực giác về cách sử dụng từ ngữ,

và theo một cách nào đó, các mô hình ngôn ngữ cũng vậy.

Bên trong, họ sử dụng mạng lưới thần kinh,

một mô hình toán học khổng lồ và phức tạp của ngôn ngữ.

Mô hình này lưu trữ thông tin về những từ thường được sử dụng với nhau,

chúng thường xuất hiện theo thứ tự nào,

và ở cấp độ cao hơn,

nắm bắt được ý nghĩa của những từ này trong ngữ cảnh.

Sự biểu diễn toán học này của ngôn ngữ

là những gì mô hình cuối cùng sử dụng để tạo văn bản mới.

Khi LLM tạo ra sự hoàn thành,

tất cả những gì nó làm là thêm từ mới vào cuối lời nhắc,

mỗi lần một từ.

Ví dụ: nếu nó đang tạo ra sự hoàn thành cho lời nhắc cuối cùng đó,

nó có thể sẽ thêm từ tỏa sáng,

và sau đó có thể thêm từng từ trên bầu trời vào một lúc,

trước khi báo hiệu hoàn thành và trả lại cho người dùng.

Về mặt kỹ thuật, LLM không tạo ra các từ mà tạo ra các mã thông báo,

đó là một thuật ngữ chung hơn cho các từ.

Một số từ như London và cửa có thể có dấu hiệu riêng,

nhưng những từ ghép phổ biến như lập trình và không hài lòng

thường được chia thành nhiều token.

Dấu câu, như dấu chấm, dấu phẩy và dấu chấm hỏi

cũng có thể nhận được token của riêng mình.

Hầu hết các LLM đều có tổng vốn từ vựng

từ 10 đến hơn 100.000 token.

Có sự linh hoạt để xây dựng các từ ghép

từ những mảnh từ nhỏ hơn,

cho phép mô hình xây dựng bất kỳ từ nào có thể

mà không cần phải gán mã thông báo cho từng cái.

Đây là quá trình LLM trải qua

trước khi thêm từng mã thông báo mới để hoàn thành.

Đầu tiên, nó xử lý trạng thái hoàn thành hiện tại,

tạo ra sự hiểu biết sâu sắc về các mối quan hệ

giữa mỗi từ và ý nghĩa tổng thể của văn bản.

Sau đó LLM xem xét từng mã thông báo trong từ vựng của nó,

thường có hàng chục đến hàng trăm nghìn,

và tính xác suất để nó xuất hiện tiếp theo.

Trong ví dụ bạn đã thấy cho đến nay,

tỏa sáng có thể sẽ có xác suất cao nhất

và sự gia tăng sẽ có xác suất nhỏ hơn,

nhưng ngay cả những từ không thể xảy ra như bùng nổ hay ngáy

vẫn sẽ có một cơ hội rất nhỏ để xuất hiện tiếp theo.

Nói cách khác, LLM tạo ra phân bố xác suất

trên mọi mã thông báo.

Sau đó nó chọn ngẫu nhiên mã thông báo tiếp theo

từ phân bố xác suất đó.

Trong ví dụ này, 80 trong số một trăm,

nó sẽ chọn tỏa sáng,

nhưng vẫn có khả năng nó sẽ chọn tăng

hoặc vâng, thậm chí bùng nổ.

Khi LLM thêm một mã thông báo khác vào quá trình hoàn thành,

nó lặp lại toàn bộ quá trình này.

Lần này, hầu hết các từ ở phần hoàn thành

là từ lời nhắc ban đầu,

nhưng một trong số đó là từ tỏa sáng,

mà nó vừa tạo ra.

Điều này có nghĩa là các lựa chọn mã thông báo mà LLM thực hiện sớm hơn

khi hoàn thành sẽ tác động đến các lựa chọn mà nó thực hiện sau này.

Đây là hành vi mong muốn vì nó có nghĩa là các token mới

sẽ có ý nghĩa trong bối cảnh của các token

LLM đã được chọn.

Điều đó nói lên rằng, điều đó cũng có nghĩa là một khi có bằng LLM

chọn ngẫu nhiên một hướng để hoàn thành,

nó sẽ đi theo con đường mà nó dẫn tới.

Ví dụ, sau khi chọn tỏa sáng,

LLM có thể chọn trong, và bầu trời

vì những từ đó đều có ý nghĩa

trong ngữ cảnh của các từ được chọn trước chúng.

Tuy nhiên, nếu mã thông báo được tạo ban đầu đó đang nóng lên,

LLM sau đó có thể chọn khuôn mặt của chúng tôi

vì điều đó có ý nghĩa hơn

theo hướng mà LLM đã hoàn thành.

Hành vi này được gọi là tự thoái lui,

nghĩa là tự tác động.

Nhờ tính chất ngẫu nhiên và tự hồi quy,

chạy cùng một lời nhắc nhiều lần thông qua cùng một LLM

thường sẽ dẫn đến những sự hoàn thành khác nhau.

LLM có thể hiểu ý nghĩa của lời nhắc

và đưa ra những dự đoán hợp lý về từ ngữ

bởi vì nó đã được huấn luyện trên các tập hợp văn bản lớn.

Mô hình toán học hỗ trợ LLM

có hàng tỷ tham số riêng lẻ hoặc trọng số số.

Trước khi đào tạo, mô hình này sẽ chỉ tạo ra những từ vô nghĩa.

Trong quá trình đào tạo, LLM đã hiển thị những đoạn văn bản chưa hoàn chỉnh

từ dữ liệu huấn luyện

và cố gắng dự đoán từ nào sẽ xuất hiện tiếp theo.

Dựa trên tính chính xác của những dự đoán này,

nó sẽ cập nhật các thông số bên trong của nó.

Bằng cách này, mô hình học cách sản xuất

cả thông tin thực tế

và các phong cách ngôn ngữ trong dữ liệu huấn luyện.

Nhiều mô hình ngôn ngữ lớn hiện nay

được đào tạo về hàng nghìn tỷ mã thông báo văn bản,

phần lớn được lấy từ internet mở.

Các mô hình kết quả có thể tạo ra văn bản

trong nhiều phong cách khác nhau và về nhiều chủ đề khác nhau

bởi vì ví dụ về những phong cách đó

và thông tin về những chủ đề đó đã có trong dữ liệu đào tạo của nó.

Hiểu cách LLM hoạt động và cách chúng được đào tạo

cũng giải thích nhiều hành vi của họ.

Hãy bắt đầu với ảo giác.

Tất cả những gì LLM có thể làm là tạo ra các chuỗi từ có thể xảy ra

dựa trên các mẫu họ đã học được trong dữ liệu huấn luyện của họ.

Nếu bạn hỏi LLM về quyền riêng tư của công ty bạn,

dữ liệu nội bộ hoặc tin tức ngày hôm nay,

người mẫu gần như chắc chắn chưa được đào tạo

về thông tin đó

và do đó không ở vị trí tốt để trả lời.

Trong những trường hợp này, LLM đôi khi sẽ đưa ra phản hồi

điều đó nghe có vẻ đúng nhưng thực tế lại không đúng.

Mặc dù những hành vi này được gọi là ảo giác,

điều quan trọng là phải nhớ LLM

không có giai đoạn tâm lý nào

hoặc thậm chí thực sự gặp trục trặc.

LLM được thiết kế để tạo ra văn bản có thể xảy ra,

văn bản không trung thực.

Sự thật, đối với LLM,

đó chỉ là một chuỗi các từ

có khả năng xảy ra dựa trên dữ liệu huấn luyện của nó.

Với dữ liệu đào tạo chất lượng cao,

sự hiểu biết trực quan của chúng ta về sự thật

và sự hiểu biết toán học của LLM

các chuỗi từ có thể xảy ra có thể được giữ thẳng hàng.

Thách thức sau đó là đảm bảo LLM có quyền truy cập

đến càng nhiều thông tin liên quan càng tốt.

RAG giải quyết vấn đề này bằng cách tận dụng

về việc LLM có thể hiểu ngữ cảnh tốt đến mức nào.

Nếu hệ thống RAG của bạn thêm thông tin liên quan vào lời nhắc,

LLM có thể hiểu được

và kết hợp thông tin đó vào phản hồi của nó,

mặc dù thông tin đó

không phải là một phần của dữ liệu đào tạo của nó.

Thông thường, bạn sẽ nói thông tin này

làm cơ sở cho các phản hồi của LLM.

Mặc dù bạn có thể chỉ muốn thêm

càng nhiều thông tin liên quan đến lời nhắc càng tốt mà bạn có thể tìm thấy,

trong thực tế, có những lý do bạn không thể.

Đầu tiên, những lời nhắc dài hơn sẽ khiến bạn mất nhiều thời gian tính toán hơn để chạy.

Điều này là do trước khi tạo mỗi mã thông báo mới,

mô hình thực hiện quét tính toán phức tạp

của mọi mã thông báo đã hoàn tất,

bao gồm cả lời nhắc ban đầu.

Thứ hai, cuối cùng bạn sẽ đạt đến giới hạn

của cửa sổ ngữ cảnh của LLM,

chuỗi dài nhất nó có thể xử lý cùng một lúc.

Một số mẫu cũ hơn có cửa sổ ngữ cảnh

chỉ với vài nghìn token,

trong khi những cái mới hơn có thể xử lý hàng triệu.

Điều này có nghĩa là khi người truy tìm thêm nhiều thông tin hơn

đến lời nhắc tăng cường,

lúc đầu, bạn sẽ chỉ làm cho lời nhắc của mình tốn kém hơn,

và cuối cùng bạn sẽ sử dụng hết

cửa sổ ngữ cảnh của mô hình.

Có rất nhiều nhà cung cấp LLM,

nhưng trong khóa học này, bạn sẽ sử dụng Together AI,

nơi lưu trữ nhiều mô hình nguồn mở phổ biến.

Sử dụng các mô hình nguồn mở giúp việc này trở nên dễ dàng hơn

để nhìn sâu hơn vào các mô hình ngôn ngữ lớn

và khám phá nhiều khái niệm

bạn sẽ học trong suốt khóa học này.

Còn rất nhiều điều cần tìm hiểu về LLM,

nhưng điều quan trọng nhất ở thời điểm này

là thiết kế của LLM cho phép nó kết hợp thông tin

trong lời nhắc vào phản hồi của nó,

ngay cả khi thông tin đó không được đưa vào

trong dữ liệu huấn luyện.

Vậy hãy chuyển sự chú ý của chúng ta sang chú chó tha mồi

và xem nó hoạt động như thế nào để cung cấp thông tin đó.