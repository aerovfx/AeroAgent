# 14 -Đánh giá sự thiên vị và công bằng dịch

---

Các video trong phần này cho đến nay đã tập trung vào ngôn ngữ và những gì chúng ta có thể gọi là

năng lực nhận thức của các mô hình.

Nhưng những mô hình này không tồn tại trong bong bóng.

Họ tương tác với thế giới thực.

Và nếu các mô hình được sử dụng ngày càng nhiều để đưa ra các quyết định có tác động đến con người thực trong cuộc sống thực

thế giới, chúng tôi muốn những mô hình này công bằng và không thiên vị.

Chúng tôi chắc chắn không muốn những mô hình này mang tính phân biệt giới tính hoặc phân biệt chủng tộc hoặc có bất kỳ nội dung nào khác được cài sẵn.

thành kiến chống lại các giới tính hoặc nhóm người hoặc quốc tịch cụ thể.

Việc đánh giá sự thiên vị và công bằng thực sự khá phức tạp và đôi khi tốt nhất là nên thực hiện một cách định tính.

bằng cách yêu cầu mọi người đọc kết quả đầu ra của một mô hình tổng quát và đưa ra phản hồi chi tiết về nó

thành kiến.

Nhưng có một số đánh giá định lượng có thể cung cấp một số hiểu biết sâu sắc về những thành kiến trong

các mô hình ngôn ngữ và tôi sẽ mô tả một vài mô hình đó trong video này.

Nhưng trước hết tôi chỉ muốn nhấn mạnh rằng về bản chất các mô hình không thiên vị bất kỳ ai.

các nhóm xã hội hoặc chính trị cụ thể.

Bất kỳ thành kiến hoặc sự không công bằng mang tính hệ thống nào trong mô hình ngôn ngữ đều xuất phát từ dữ liệu huấn luyện của nó, có nghĩa là

nó đến từ tổng số văn bản do con người viết trên web, trong sách, v.v.

Có rất nhiều bài viết về đo lường sự thiên vị và công bằng trong các mô hình ngôn ngữ.

Trên thực tế, vấn đề này và loại nghiên cứu này đã có trước kiến ​​trúc máy biến áp.

Nó quay trở lại vài thập kỷ trước khi các mô hình ngôn ngữ thực sự chỉ là các mô hình nhúng cố định.

Vì vậy, có cả một tài liệu về chủ đề này và ở đây tôi chỉ nêu bật hai điều cụ thể

xem lại các bài viết đề phòng trường hợp bạn muốn đọc thêm về tài liệu này.

Tôi sẽ không xem qua bất kỳ bản demo Python nào vì các đánh giá về cơ bản là giống nhau

như những gì bạn đã thấy trong phần này ngoại trừ chủ đề, từ và câu

được tinh chỉnh để đánh giá sự công bằng và thiên vị.

Vì vậy, thay vào đó điều tôi sắp làm là cho bạn biết về bốn cách tiếp cận chung được sử dụng trong

phương pháp eVAL khác nhau. Một cách tiếp cận là xem xét các thành kiến được tích hợp trong quá trình nhúng

vectơ. Vì vậy, ví dụ: bạn có thể tính độ tương tự cosin giữa bốn từ này ở đây.

Và ý tưởng là nếu đàn ông và bác sĩ có quan hệ gần gũi với nhau thì phụ nữ và y tá có quan hệ chặt chẽ với nhau

có liên quan với nhau, trong khi đàn ông, y tá, phụ nữ và bác sĩ có những điểm tương đồng cosin yếu hoặc thậm chí âm,

thì điều đó sẽ cung cấp bằng chứng cho thấy ma trận nhúng trong mô hình này sẽ có một số sai lệch về giới tính

đúng, bạn biết đấy, được tích hợp ngay ở cấp độ nhúng mã thông báo. Ngay cả trước những phần nhúng đó

đi vào một mô hình ngôn ngữ để xử lý và chuyển đổi. Một cách tiếp cận khác sẽ là

dự đoán mã thông báo mặt nạ chính xác như những gì tôi đã cho bạn xem trong một số video trước đây. Vì vậy, ví dụ,

bạn có thể đưa ra cho người mẫu một câu như cô ấy giỏi hoặc anh ấy giỏi và sau đó là một biểu tượng mặt nạ.

Và sau đó bạn có thể xem các giá trị logic hoặc có thể là giá trị softmax của nhật ký cho các mã thông báo khác nhau

và xem liệu, chẳng hạn, tính logic trong toán học có cao hơn không nếu câu bắt đầu bằng he so với she.

Và sau đó chúng ta có ví dụ này ở đây, nó xuất phát từ ý tưởng của heliswag,

nơi bạn nhìn vào tổng xác suất của một câu cho rằng hai câu giống nhau

ngoại trừ giới tính trong trường hợp này. Hoặc bạn biết đấy, nó cũng có thể là một chủng tộc hoặc một quốc gia xuất xứ hoặc

liên kết chính trị hoặc một cái gì đó như thế. Vì vậy, ý tưởng là nếu câu liên quan đến một

khuôn mẫu thiên vị được mô hình cho là có nhiều khả năng xảy ra hơn, thì đó là bằng chứng cho thấy mô hình có

thiên vị tích hợp. Vâng, sau đó chúng tôi có ví dụ này. Đây thực ra cũng chỉ là một biến thể của chiếc mặt nạ

ví dụ về mã thông báo ở đây. Vì vậy, trong câu ví dụ này, chúng ta có thể che giấu từ dành cho đại từ.

Và nếu bạn trình bày mô hình bằng một từ hoặc mô tả, điều đó có thể được liên kết với một

giới tính hoặc nhóm, sau đó bạn có thể xem đại từ nào mà mô hình có cao nhất

logic cho. Tôi nghĩ bạn thấy từ những ví dụ này việc đánh giá một cách định lượng các khái niệm xã hội như

thiên vị và công bằng thực ra không quá khó khăn. Nó chỉ đòi hỏi một số cách thông minh và khéo léo để

sử dụng các phương pháp đánh giá mà bạn đã quen thuộc. Một khi những thành kiến này được xác định,

họ có thể được huấn luyện ngoài mô hình, ít nhất ở một mức độ nào đó. Điều đó có thể xảy ra bằng cách học tăng cường,

ví dụ: khen thưởng mô hình tạo ra phản hồi công bằng và không thiên vị cũng như đưa ra phản hồi tiêu cực

phản hồi cho mô hình khi nó tạo ra văn bản có sẵn thành kiến rõ ràng. Cũng có thể

để sửa đổi tập huấn luyện. Ví dụ: giả sử bạn có một tập dữ liệu có nhiều câu lệnh

về việc các kỹ sư và bác sĩ gắn liền với nam giới. Bạn có thể chỉ cần chỉnh sửa những câu đó để

họ có đại từ she thay vì he hoặc woman thay vì man, và sau đó đặt những từ đã thay đổi

câu trở lại tập huấn luyện. Sao cho tập huấn luyện có 50% mô tả về

nam là kỹ sư và bác sĩ, và 50% nữ là kỹ sư và bác sĩ.

Tôi đoán điểm cuối cùng tôi muốn nói ở đây là một mặt, nhiều người có lý khi

quan tâm đến việc sử dụng các mô hình để đưa ra những quyết định quan trọng có tác động đến con người và xã hội,

liệu những mô hình này có tạo nên thành kiến ủng hộ hoặc chống lại các nhóm cụ thể hay không. Nhưng mặt khác,

Tôi nghĩ ở mức độ mà những thành kiến này được xem xét một cách nghiêm túc và điều tra và cố gắng giải quyết

đã sửa, thực sự có một cơ hội tốt ở đây vì những thành kiến mà các mô hình học được

tiết lộ những thành kiến ​​có trong văn bản văn hóa của chúng ta. Và vì vậy tôi nghĩ rằng việc cố gắng khắc phục

những thành kiến trong các mô hình cũng có tác động tích cực trong việc giúp làm cho sự tương tác của con người trở nên hiệu quả hơn.

công bằng và ít thiên vị hơn.