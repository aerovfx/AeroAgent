# 01 cuộc trò chuyện giữa-chanin-nantasenamat-và-andrew-ng

---

Chào mừng bạn đến với khóa học này, nơi bạn học cách tạo nguyên mẫu nhanh chóng cho các ứng dụng AI tổng hợp,

sử dụng Streamlit. Khóa học này được tạo ra với sự hợp tác giữa Deep Learning.ai

và Snowflake, công ty quản lý Streamlit. Ngày nay, những người biết cách xây dựng bằng GenAI đều

di chuyển nhanh hơn bao giờ hết có thể trước đây. Và khả năng AI viết mã cho bạn,

giải quyết vấn đề, lập kế hoạch cho các ứng dụng phần mềm phức tạp, đang tăng tốc đáng kể

tốc độ mà tất cả chúng ta có thể xây dựng phần mềm. Bây giờ điều đó là có thể, và trên thực tế thường là thích hợp hơn,

để khám phá các ý tưởng bằng cách sử dụng các nguyên mẫu phần mềm hoạt động thực tế, thay vì chỉ sử dụng một phần

giấy hoặc tài liệu cung cấp một số thông số kỹ thuật hoặc một số khung dây được vẽ bằng tay.

Khi bạn xây dựng thứ gì đó một cách nhanh chóng, bạn có thể lấy nguyên mẫu phần mềm đó và nhận phản hồi,

và thông tin phản hồi phong phú này cho phép bạn quyết định phải làm gì cho lần lặp tiếp theo và bạn có thể thực hiện

tiến bộ và nhận được phản hồi thực tế để thúc đẩy tiến độ đó nhanh hơn nhiều so với trước đây.

Vì vậy, trong khóa học này, bạn học được nền tảng tinh thần để suy nghĩ về cách xây dựng nguyên mẫu nhanh chóng,

và cách lặp lại nhanh chóng. Tôi rất vui được ở đây cùng với người hướng dẫn của bạn, Tiến sĩ Chanin Nantasenamat,

người cũng đã tạo ra kênh YouTube, The Data Professor, kênh này giúp hàng nghìn nhà phát triển

biến ý tưởng AI của họ thành hiện thực. Chào mừng, Chanin. Vâng, cảm ơn Andrew vì lời giới thiệu tử tế.

Tôi biết bạn đã nói rất nhiều về việc GenAI đã biến đổi hoàn toàn chính bạn như thế nào

quá trình phát triển. Thay đổi lớn nhất đối với cá nhân bạn là gì? Làm việc trong lĩnh vực AI và phần mềm,

Tôi có cảm giác như đây đã là một lĩnh vực thú vị trong một thời gian, nhưng tôi lại cảm thấy như mình đang đi tàu lượn siêu tốc,

chỉ di chuyển chậm rãi và tôi không thấy chán. Đó là một tàu lượn siêu tốc, một tàu lượn siêu tốc hạnh phúc. Nhưng

những thay đổi gần đây trong mã hóa tác nhân, có cảm giác như, chàng trai, tàu lượn siêu tốc này đang di chuyển nhanh hơn nhiều,

và tốc độ và vận tốc đó, tôi thấy rất thú vị. Vì vậy, dạo gần đây, tôi thực sự ngừng viết mã

hầu như mỗi cuối tuần. Tôi có nhiều thời gian vào thứ bảy và chủ nhật hơn các ngày trong tuần để viết mã.

Nhưng tôi thấy rằng nếu một ý tưởng có thể đến quán cà phê vào chiều thứ Bảy, hãy ngồi xuống và bắt đầu

một cái gì đó sẽ hoàn thành và chạy trong vòng một đến bốn giờ, và hóa ra rất nhiều ý tưởng của tôi lại là những ý tưởng tồi.

Thực hiện nó, nhìn vào nó và đi, ôi, điều đó không hiệu quả. Và sau đó nó sẽ không bao giờ nhìn thấy

ánh sáng ban ngày, và điều đó không sao cả, vì tôi chỉ lãng phí một khoảng thời gian nhỏ. Đôi khi tôi xây dựng

gì đó rồi đi, bạn biết không, tôi thực sự thích điều này và tôi sẽ mang nó đến nhóm của mình để xem liệu

có sự quan tâm đến việc đưa nó lên quy mô lớn. Nhưng tốc độ đó và sự giảm đáng kể chi phí cố gắng

điều gì đó xảy ra có nghĩa là tôi và tôi thấy nhiều nhóm thông minh trên khắp thế giới hiện sẵn sàng thực hiện

nhiều cú đánh nữa. Hãy thử nó. Nếu nó không hoạt động, không sao cả. Ý tôi là, chỉ cần chụp nhiều ảnh hơn để

khám phá những thứ thực sự hiệu quả và đáng để mở rộng quy mô. Tôi thấy các nhà phát triển đang chuyển từ,

hãy để tôi lên kế hoạch từng chi tiết, để tôi thử nghiệm ý tưởng này. Khi quá trình tạo mẫu diễn ra nhanh chóng,

nút thắt thực sự là chờ đợi phản hồi. Nếu bạn có thể nhận được phản hồi vào ngày thứ ba thay vì

tuần thứ ba, bạn có nhiều thời gian hơn để thực hiện những cải tiến có ý nghĩa. Nhưng Andrew, khi sự phát triển chuyển động

nhanh như vậy, làm thế nào để bạn chắc chắn rằng mình đang học được điều gì đó hữu ích cho mỗi lần lặp lại? Một thực hành

Tôi thường sử dụng khi ngồi xuống nguyên mẫu, đôi khi tôi sẽ lái xe đến quán cà phê,

Tôi chỉ có hai giờ. Và điều tôi thường làm là tiếp tục cắt giảm phạm vi cho đến khi dự án tôi muốn

việc triển khai có thể thực hiện được trong hai giờ. Đôi khi bạn có thể cắt phạm vi đủ nhỏ để xây dựng một phạm vi

thành phần của một ứng dụng hình dung lớn hơn nhiều, sau đó lấy thành phần đó và hiển thị cho người dùng và

xem họ có thích nó không. Vì vậy, ví dụ: nếu bạn có, tôi không biết, hãy nói Hình dung để biết cách trợ giúp người dùng

xử lý email tốt hơn, có thể bạn có thể cắt bớt phạm vi để xây dựng MVP chỉ bằng một số ít email,

có thể sao chép, dán nó từ email của bạn và sau đó có nội dung nào đó để hiển thị kết quả. Và bạn có thể

mang nó đi kiểm tra người dùng hoặc thậm chí tự kiểm tra nó. Và nếu ruột của bạn đôi khi không như vậy,

bạn biết đấy, có một số nguy hiểm khi tự mình thử nghiệm. Nhưng đôi khi nếu bạn trau dồi ruột của mình

để dự đoán những gì người dùng sẽ muốn, tôi thấy điều đó đủ tốt để đưa ra quyết định thực sự nhanh chóng

để tốc độ ra quyết định về sản phẩm có thể phù hợp với tốc độ thực hiện hiện tại

có thể. Với Snowflake của riêng bạn và cũng đang điều hành một kênh YouTube, bạn đã thấy gì về

tư duy của nhà phát triển đang chuyển sang phương pháp tạo mẫu nhanh này? Vâng, thật tuyệt vời khi

xem mọi người có khoảnh khắc bừng sáng khi họ nhận ra rằng họ có thể triển khai và nhận phản hồi về một ý tưởng

tính bằng ngày thay vì tháng. Những nhà phát triển nắm bắt vấn đề này nhanh thường là những người đã

trước đây đã phạm sai lầm này. Họ dành hàng tháng trời để xây dựng một thứ gì đó, cho ra mắt nó và chỉ sau đó

khám phá ra người dùng muốn thứ gì đó hoàn toàn khác. Khi tôi nói chuyện với đồng nghiệp của mình tại Snowflake, một trong những

mối lo ngại trước mắt là liệu việc tạo mẫu nhanh có ảnh hưởng đến chất lượng của ứng dụng hay không

được phát triển? Vậy suy nghĩ của bạn về điều đó là gì? Bạn biết đấy, tôi nghĩ thật thú vị khi thường xuyên

chính sự lặp lại nhanh chóng sẽ giúp bạn đạt được chất lượng. Bởi vì nếu chúng ta bắt đầu không thực sự

biết chính xác điều người dùng muốn, đó là quá trình xây dựng thứ gì đó, nhận phản hồi, xây dựng thứ gì đó,

nhận được phản hồi, điều đó cho phép chúng tôi hiểu rõ hơn về người dùng để từ đó đạt được điều gì đó thực sự

thực sự tốt cho người dùng và đáp ứng nhu cầu của họ sâu sắc hơn nhiều. Nói xong điều này, có

một dấu hoa thị cho điều này, đó là khi bạn mở rộng quy mô một sản phẩm, tôi nghĩ kỹ thuật phần mềm tốt

nguyên tắc cơ bản không quan trọng. Nếu bạn đang xây dựng một ứng dụng quy mô, cấp độ sản xuất, an toàn,

hiểu rằng các nguyên tắc cơ bản về phần mềm về cơ sở dữ liệu bạn sử dụng, cách bảo mật phần mềm, cách thức

để triển khai một đám mây đắt tiền, bộ kiến thức sâu sắc đó vẫn thực sự có giá trị. Vì vậy không phải tất cả mọi thứ

trong cuộc sống chỉ là, bạn biết đấy, rung cảm với việc viết mã và chúng ta hãy làm mọi thứ nhanh chóng và ném mọi thứ ra khỏi đó.

Nhưng trong giai đoạn đầu của dự án, nơi cần xây dựng những tính năng nào, điều này có đáng để xây dựng không khi

tất cả những điều đó đều chưa rõ ràng, việc tạo nguyên mẫu nhanh để sau đó quyết định điều gì cần đầu tư kỹ thuật sâu hơn

để mở rộng quy mô một cách mạnh mẽ, đáng tin cậy và an toàn, đó dường như là một điều thực sự quan trọng

mảnh ghép. Bạn biết đấy, bạn đã làm điều này rất nhiều. Chúng tôi muốn chia sẻ những gì

các khuôn khổ mà bạn thấy hữu ích nhất để thúc đẩy loại tiến bộ nhanh chóng này.

Tôi nhận thấy rằng công cụ tốt nhất để lặp lại nhanh chóng là những công cụ loại bỏ sự tích hợp hệ thống

hoàn toàn. Bạn có thể viết code nhanh với GenAI nhưng kết nối tất cả front-end và back-end

là nơi bạn mất tốc độ. Đó là lý do tại sao chúng tôi xây dựng khóa học này bằng Snowflake và Streamlit. Họ giải quyết

điều này một cách hoàn hảo. Snowflake quản lý dữ liệu của bạn, Streamlit tạo giao diện người dùng tức thì. Vì vậy, bạn có thể lặp lại

vào ý tưởng cốt lõi của bạn thay vì dành nhiều thời gian để gỡ lỗi. Là một người có hậu phương mạnh mẽ hơn

hơn là nền tảng front-end, bạn biết đấy, tôi chỉ không giỏi về front-end thôi. Tôi thấy rằng có thể

để sử dụng Gen AI để viết mã Streamlit hoặc viết mã JavaScript, chỉ cần quan tâm đến giao diện người dùng

cho tôi. Cuối cùng, dạo này tôi viết nhiều mã front-end hơn thay vì để AI viết nhiều

tôi có nhiều mã giao diện người dùng hơn trước đây. Thế là tuyệt vời rồi. Tại sao bạn không dẫn chúng tôi đi qua

những gì mọi người sẽ thấy trong khóa học này. Chắc chắn, bạn sẽ xây dựng bảng điều khiển phân tích cảm tính

cho một công ty thiết bị thể thao hư cấu tên là Avalanche. Nó dựa trên một thực tế khá phổ biến

kịch bản thế giới. Dữ liệu của bạn lộn xộn, dự án tiếp tục phát triển và mọi người đều cần những hiểu biết sâu sắc

họ có thể hiểu và sử dụng. Khi xây dựng, bạn sẽ sử dụng các công cụ Gen AI để giúp viết, khắc phục sự cố,

và lặp lại mã của bạn như một nhà phát triển mã thực sự. Sau đó, bạn sẽ kết nối trang tổng quan của mình

ứng dụng cho dữ liệu đánh giá của khách hàng được lưu trữ trong Snowflake và thiết lập các cơ chế cần thiết để truy vấn dữ liệu đó

một cách hiệu quả. Bạn sẽ cải thiện trang tổng quan của mình bằng cách thêm chatbot và sử dụng kỹ thuật nhanh chóng

và tạo tăng cường truy xuất hoặc RAG để đưa ra câu trả lời dựa trên dữ liệu thực tế. Cuối cùng,

bạn sẽ triển khai ứng dụng của mình và thực hành thu thập phản hồi vì quá trình phát triển không kết thúc ở

phóng. Nó bắt đầu ở đó. Cuối cùng, bạn sẽ tạo được một ứng dụng chức năng minh họa cách

để biến dữ liệu thành thông tin chuyên sâu mà bạn có thể chia sẻ với nhóm của mình và bạn sẽ nắm vững cách làm việc hiệu quả

quy trình làm việc để biến ý tưởng của bạn thành nguyên mẫu hoạt động. Và đó thực sự là mục tiêu của

tất nhiên, để giúp bạn trau dồi kỹ năng lặp lại nhanh chóng, chu đáo để họ có thể có được những trải nghiệm thú vị

các ý tưởng và biến chúng thành hiện thực bằng các công cụ, đồng thời giúp người dùng tiềm năng có thể tiếp cận ý tưởng này

để nhận phản hồi và tiếp tục phát triển. Vì vậy, nếu bạn có một số ý tưởng, và nếu không thì cũng không sao,

có một số ý tưởng bạn đang nghĩ có lẽ bạn nên xây dựng nó vào một ngày nào đó, nhưng nếu không thì

chắc chắn nên bắt đầu từ đâu, tôi hy vọng rằng cách tiếp cận từng bước của khóa học này sẽ

giúp chỉ cho bạn một số hướng để bắt đầu từ một khái niệm mơ hồ hoặc mang tính thăm dò để đạt được

một nguyên mẫu đang hoạt động Hy vọng bạn thấy những kỹ năng học được trong khóa học này hữu ích cho công việc của bạn,

cũng như cho các dự án cá nhân thú vị của bạn. Và với điều đó, tôi hy vọng bạn tiếp tục xem video tiếp theo

nơi Chanin sẽ chia sẻ về cách GenAI đã thay đổi nguyên mẫu một cách cơ bản và điều này có ý nghĩa gì

về cách bạn tiếp cận việc xây dựng các ứng dụng. Vậy chúng ta hãy chuyển sang video tiếp theo.