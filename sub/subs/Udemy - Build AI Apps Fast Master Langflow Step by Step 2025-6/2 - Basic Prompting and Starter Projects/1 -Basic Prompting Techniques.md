# 1 -Các kỹ thuật nhắc nhở cơ bản đã được dịch

---

Khi làm việc với mô hình AA, chúng ta phải hiểu rằng cách chúng ta nhập lời nhắc sẽ phản ánh

một đầu ra tương tự.

Điều này có nghĩa là việc nhắc nhở tốt bao gồm việc tạo ra các hướng dẫn rõ ràng với ngữ cảnh phong phú để giúp

mô hình AA tạo ra những phản hồi mà chúng tôi cần.

Điều này thường dẫn đến việc thử nghiệm và điều chỉnh liên tục các lời nhắc để có kết quả tốt hơn.

Ví dụ: giả sử bạn muốn tạo một trang web, bạn có thể nhập hướng dẫn vào

một số sân chơi, chẳng hạn như tạo một trang web và nhấp vào nút để thực hiện hướng dẫn này.

Sau vài giây, chúng ta thấy kết quả và về cơ bản chúng ta có một trang web, cấu trúc

của một trang web có mã HTML và CSS.

Tuy nhiên, điều này có cấu trúc rất chung vì chúng tôi không chỉ định bất kỳ hướng dẫn chính xác nào,

chúng tôi chỉ yêu cầu nó tạo một trang web để cung cấp cho chúng tôi phản hồi chung về thông tin đầu vào chung.

Bây giờ, nếu bạn muốn điều gì đó cụ thể hơn, bạn có thể sử dụng lời nhắc như lời nhắc bạn thấy trên màn hình,

nơi bạn chỉ ra chính xác khuôn khổ nào bạn cần, chẳng hạn như cho phần thiết kế đồ họa.

Bạn nói rằng bạn cần bao gồm các phương pháp hay nhất chẳng hạn như khả năng truy cập, hiệu suất và SEO.

Bạn thậm chí còn chỉ định cấu trúc tệp sẽ như thế nào trong lời nhắc này,

và những tập tin nào thế hệ này nên bao gồm.

Nó cũng chỉ định các phần khác nhau trên các trang khác nhau.

Mặc dù đây là một lời nhắc mang tính mô tả khá cao nhưng tóm lại nó chi tiết hơn nhiều.

Tôi sẽ sao chép lời nhắc.

Tôi sẽ nhập nó như thể đó là một lời nhắc mới. Đây là như vậy. Tôi sẽ bắt đầu lại cuộc hành quyết.

Sau vài giây, bạn có thể thấy rằng chúng tôi đã có phản hồi ở đây.

Phản hồi là một mã HTML có các phần được chỉ định khác.

Bạn có thể thấy rằng họ cũng đang sử dụng các phần tử từ khung khởi động,

bởi vì chúng tôi đã chỉ định nó theo cách đó.

Mặc dù kết luận là với đầu vào tốt hơn, bạn sẽ có đầu ra tốt hơn.

Tương tự, có thể sử dụng các ví dụ trong gợi ý để giúp hướng dẫn việc tạo ra

phản hồi. Phương pháp đầu tiên chúng tôi sẽ phân tích được gọi là 0 Shot Learning.

Trong kỹ thuật này, bạn bao gồm các hướng dẫn cần tuân theo nhưng loại trừ các ví dụ được gọi là

Hoàn thành Bervatin. Những lời nhắc này rất hữu ích khi bạn muốn có phản hồi chung,

hoặc khi nhiệm vụ không yêu cầu những mục rất cụ thể.

Tôi sẽ xóa ví dụ này mà chúng tôi đã có với tư cách là một phần của thế hệ trước.

Tôi sẽ dán một tin nhắn mới vào đây, trong đó cho biết như một phần của hướng dẫn mục đích của một

yêu cầu của người dùng liên quan đến hệ thống com thông minh. Chúng tôi đang chỉ ra rằng nếu bạn không biết cách trả lời

hoặc câu trả lời là gì, bạn nên nêu rõ từ chưa biết.

Để chỉ định các tùy chọn mà mô hình AJA có thể chọn, chúng tôi đã liệt kê một loạt tùy chọn tại đây.

Về cơ bản, chúng tôi đang mô phỏng hoạt động đầu vào của người dùng, tức là bật đèn trong phòng chiếu sáng,

và về cơ bản, mô hình AJA phải chọn một trong các tùy chọn khác nhau để xuất ra.

Vì vậy, hãy lưu ý rằng không có ví dụ nào được đưa ra về cách nó sẽ phản hồi.

Chúng tôi chỉ đơn giản chỉ ra rằng dựa trên kiến thức của nó, nó phải chọn một phương án dựa trên những gì

một đầu vào của người dùng. Bây giờ, tôi sẽ nhấp vào nút có nội dung chạy để xem phản hồi là gì.

Bạn có thể thấy rằng phản hồi là bật thiết bị, điều này có liên quan chặt chẽ đến hoạt động nhập hoặc

hướng dẫn. Tôi sẽ kiểm tra lệnh thứ hai, nhưng lần này đầu vào của người dùng được đặt bộ hẹn giờ thành

tắt TV sau 30 phút. Nói cách khác, nó đặt hẹn giờ để tắt

truyền hình trong 30 phút. Hãy xem phản hồi của mô hình AJA là gì. Bạn có thể thấy rằng nó

chọn đặt bộ hẹn giờ, đây là tùy chọn mà chúng tôi sẽ quan tâm nếu chúng tôi đang xây dựng một hệ thống cho

một ngôi nhà thông minh. Kỹ thuật thứ hai được gọi là học ít cú đánh. Trong kỹ thuật này,

một số ví dụ về việc hoàn thành bằng lời nói được đưa vào để hỗ trợ việc tạo ra phản hồi.

Thông thường, bao gồm từ 1 đến 5 ví dụ để thể hiện mong muốn

hướng dẫn, phong cách hoặc kiểu phản ứng. Sau đó tôi sẽ xóa những tin nhắn trước đó,

và tôi sẽ dán một tin nhắn mới. Nó rất giống với ví dụ chúng ta đã thấy trước đó.

Ở đây, điểm khác biệt chính là chúng tôi đang hướng dẫn mô hình bằng kiến ​​thức mới.

Chúng tôi đang chỉ ra một cách mà chúng tôi muốn nó phản hồi. Tôi giả sử bạn có một ứng dụng

cần viết lệnh thực thi trước khi thực hiện một trong các lệnh này, ví dụ:

để bắt đầu kích hoạt hoặc bắt đầu một số hành động trong ứng dụng của bạn. Vì vậy, trước đây chúng ta đã thấy rằng một trong những

các tùy chọn sẽ được chọn. Tuy nhiên, trong những ví dụ này, chúng tôi đang chỉ ra rằng người dùng nên

phản hồi hoặc cụ thể hơn, mô hình AJA sẽ phản hồi bằng từ thực thi trước khi đặt một

của các lệnh. Bạn có thể thấy rằng chúng tôi có ba ví dụ ở đây, trong đó có một ví dụ chỉ ra rằng

trường hợp lệnh thực thi không xác định thì phải nhập từ lỗi. Trong đầu vào của người dùng,

chúng ta có thể thấy rằng chúng ta đã có hướng dẫn mà chúng ta sẽ đánh giá. Hãy bấm vào chạy để xem những gì

xảy ra khi phản hồi được trả về. Được rồi, bạn có thể thấy rằng sau đó chúng tôi nhận được phản hồi đặt

từ thực thi trước lệnh để thực thi chính xác. Điều này có thể thực hiện được bởi vì chúng tôi

đã cung cấp một số ví dụ trước đây về cách mô hình AJA sẽ phản hồi. Một điểm quan trọng tôi

Điểm nổi bật nhất là kiểu tiếp cận này mang lại mức tiêu thụ token cao hơn, nhưng nó cũng

rất hữu ích để giảm sự mơ hồ và điều chỉnh kết quả phù hợp với đầu ra đã quyết định.

Một cách khác để cung cấp ví dụ cho mô hình AJA là sử dụng khái niệm được gọi là cá tính.

Đây là một kỹ thuật được sử dụng để hướng dẫn người mẫu áp dụng quan điểm, giọng điệu hoặc kiến thức chuyên môn khi

tạo ra phản hồi. Sử dụng tính cách cho phép bạn tập trung phản hồi tốt hơn cho khán giả

hoặc bối cảnh của nhiệm vụ. Điều này rất hữu ích khi bạn muốn, ví dụ, mô phỏng một nghề nghiệp hoặc

phản ánh một giọng điệu cụ thể. Tôi sẽ loại bỏ các ví dụ trước để chứng minh điều này.

Hãy tưởng tượng bạn muốn giải thích cho một đứa trẻ còn rất nhỏ LLM là gì.

Sau đó, chúng tôi có thể nhập hướng dẫn này, giải thích LLM là gì và xem chúng tôi nhận được phản hồi gì.

Nếu chúng tôi đưa ra phản hồi do mô hình AJA tạo ra cho một đứa trẻ, chúng có thể sẽ không hiểu

tất cả các khái niệm chúng tôi đang trình bày hoặc mô hình AJA đang cung cấp để đáp ứng

bởi vì đây là một câu trả lời khá phức tạp liên quan đến một số khái niệm kỹ thuật thậm chí còn cũ hơn

các cá nhân có thể đấu tranh để nắm bắt đầy đủ. Sau đó tôi sẽ xóa phản hồi và tạo một phản hồi mới

thông báo nêu rõ, tôi cần bạn đóng vai trò là chuyên gia về các khái niệm trí tuệ nhân tạo với các kiến thức bổ sung

chuyên môn về giáo dục và sư phạm trẻ em. Tôi cần bạn giải thích khái niệm LLM một cách đơn giản

và cách hấp dẫn để trẻ có thể hiểu mà không gặp bất kỳ trở ngại nào.

Hãy bắt đầu thực hiện hướng dẫn này.

Bạn có thể thấy rằng câu trả lời này tập trung tốt hơn vào trẻ em vì nó sử dụng sự tương tự dựa trên

trên một thư viện đầy sách. Sau đó nó bắt đầu soạn thảo dưới dạng văn bản dài hơn một chút, nhưng về cơ bản nó

bao gồm khái niệm về những gì LLM đang sử dụng phép loại suy cho trẻ em.

Về cơ bản, đây là cách chúng tôi đã hướng dẫn mô hình AJA áp dụng tính cách và phản hồi dựa trên

về tính cách mà nó đã có được. Bây giờ loại lời nhắc cuối cùng mà chúng ta sẽ khám phá được gọi là

Chuỗi nhắc nhở suy nghĩ. Đó là một kiểu suy luận được sử dụng bởi các mô hình như Deepseek hoặc O3 của OpenAI

mô hình. Với phương pháp này, bạn hướng dẫn người mẫu thực hiện nhiệm vụ theo từng bước trình bày

kết quả đầu ra cho phép bạn xác định bất kỳ vấn đề nào trong quá trình lập luận,

cho phép bạn tập trung tốt hơn vào một trong các bước.

Hãy làm ví dụ này bằng cách xóa các phản hồi trước đó và tôi sẽ nhập yêu cầu hoặc lời nhắc này,

câu hỏi này và nó thường được sử dụng khi đánh giá các mô hình AJA. Có bao nhiêu chữ R trong

từ dâu tây? Nếu chúng tôi thực hiện lời nhắc này, bạn có thể thấy rằng chúng tôi có phản hồi không chính xác

vì nó chỉ ra rằng chỉ có hai chữ cái R trong từ dâu tây, điều này không đúng.

Bây giờ tôi sẽ xóa những phản hồi này, dán một dòng mới và thêm một dòng mới vào lời nhắc chúng tôi đã nhập

trước đó, biểu thị được ngoài câu hỏi hoặc lời nhắc ban đầu như một phần của hướng dẫn, tôi

đang cho bạn. Tôi cần bạn giải thích từng bước lý luận của bạn trước khi cho tôi câu trả lời.

Với điều này, chúng tôi đang khuyến khích mô hình AJA phản hồi nhiều hơn một chút và xem xét cẩn thận câu trả lời

trước khi đưa ra lý do hoặc đưa ra phản hồi của chúng tôi. Chúng tôi bắt đầu thực hiện.

Bạn có thể thấy rằng lần này chúng tôi có câu trả lời đúng, cho biết có ba chữ R trong

từ dâu tây. Tuy nhiên, bạn có thể nhận thấy rằng là một phần của toàn bộ phản hồi do mô hình AJA đưa ra,

chúng tôi có các bước khác nhau được vạch ra. Đầu tiên, nó xác định từng chữ cái tạo nên từ dâu tây.

Tiếp theo, nó đếm số R và cuối cùng nó thực hiện xác minh để thông báo cho chúng tôi về vị trí

ở vị trí của chữ R, đi đến kết luận rằng nó đúng. Bây giờ, một điều quan trọng

điểm mà tôi thực sự thích là bạn có thể thêm lý do của riêng mình trong trường hợp bạn có cách khác

cơ sở để đi tới một kết luận khác. Ví dụ: tôi sẽ xóa những gì chúng tôi có trước đây.

Trong trường hợp cụ thể này, tôi sẽ cung cấp bộ hướng dẫn mà mô hình AJA phải tuân theo để

đi đến một kết luận. Điều này hơi khác so với lý do chúng ta đã thấy trước đó.

Đầu tiên tôi hướng dẫn nó chia từ thành nhiều dòng, đặt số chỉ mục

trước mỗi chữ cái. Bước thứ hai là xóa tất cả các dòng không chứa chữ R.

Cuối cùng, nó phải đếm các dòng còn lại và tổng số dòng là số lượng R trong

từ đó. Hãy xem liệu điều này có hoạt động chính xác không. Được rồi, và bạn có thể thấy rằng lần này chúng tôi có phản hồi

đi đến cùng một kết luận, chỉ ra rằng có ba chữ R trong từ dâu tây.

Tuy nhiên, bạn có thể thấy rằng lý do có phần khác nhau. Nó tách từng chữ cái ra

đặt một chỉ mục trước chúng, sau đó xóa tất cả các chữ cái không phải là R. Điều này dẫn đến

kết luận rằng từ dâu tây chỉ chứa ba chữ R. Đây là một số cách trong đó

bạn có thể nâng cao lời nhắc của mình bằng cách cung cấp hướng dẫn hoặc ví dụ, cho phép mô hình AJA

hiểu rõ hơn cách đáp ứng để đáp ứng nhu cầu của bạn.