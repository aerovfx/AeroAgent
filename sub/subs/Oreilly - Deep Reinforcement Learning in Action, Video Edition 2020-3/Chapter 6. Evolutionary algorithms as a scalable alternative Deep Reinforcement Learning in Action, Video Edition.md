# Chương 6. Các thuật toán tiến hóa như một giải pháp thay thế có thể mở rộng Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Phần 6.5, các thuật toán tiến hóa như một giải pháp thay thế có thể mở rộng.

Nếu có sẵn thiết bị mô phỏng, thời gian và chi phí tài chính để thu thập mẫu với tiến hóa

thuật toán ít gặp vấn đề hơn.

Trên thực tế, việc tạo ra một tác nhân khả thi bằng thuật toán tiến hóa đôi khi có thể nhanh hơn so với dựa trên độ dốc.

tiếp cận bởi vì chúng ta không phải tính toán độ dốc thông qua lan truyền ngược.

Tùy thuộc vào độ phức tạp của mạng, điều này sẽ giảm thời gian tính toán khoảng

hai đến ba lần.

Nhưng có một ưu điểm khác của thuật toán tiến hóa có thể cho phép chúng đào tạo nhanh hơn

hơn so với các bản sao gradient của chúng.

Các thuật toán tiến hóa có thể mở rộng quy mô cực kỳ tốt khi bị tê liệt.

Chúng ta sẽ thảo luận điều này một cách chi tiết trong phần này.

Phần 6.5.1, mở rộng các thuật toán tiến hóa.

Trong AI đã phát hành một bài báo có tên là chiến lược tiến hóa như một giải pháp thay thế có thể mở rộng cho việc củng cố

learning của Tim Salamons, 2017, trong đó họ mô tả các tác nhân đào tạo một cách đáng kinh ngạc

nhanh chóng và hiệu quả bằng cách bổ sung thêm nhiều máy móc.

Trên một máy duy nhất có 18 lõi CPU, họ có thể tạo ra một hình người 3D học cách đi bộ

trong 11 giờ nữa.

Nhưng với 80 máy, 1.440 lõi CPU, họ có thể tạo ra một tác nhân trong vòng chưa đầy 10 phút.

Bạn có thể nghĩ đó là điều hiển nhiên.

Họ chỉ ném thêm máy móc và tiền bạc vào vấn đề.

Nhưng điều này thực sự phức tạp hơn vẻ bề ngoài và các phương pháp tiếp cận dựa trên độ dốc khác đang gặp khó khăn.

để mở rộng quy mô cho nhiều máy đó.

Trước tiên chúng ta hãy xem thuật toán của họ khác với những gì chúng ta đã làm trước đó như thế nào.

thuật toán tiến hóa là một thuật ngữ chung cho nhiều loại thuật toán lấy cảm hứng

từ quá trình tiến hóa sinh học và dựa vào việc lựa chọn lặp đi lặp lại các giải pháp tốt hơn một chút từ một lượng lớn

dân số để tối ưu hóa một giải pháp.

Cách tiếp cận mà chúng tôi triển khai để chơi bài cực được gọi cụ thể hơn là thuật toán di truyền,

bởi vì nó gần giống với cách các gen sinh học được cập nhật từ thế hệ này sang thế hệ khác

tạo ra thông qua tái tổ hợp và đột biến.

Đây là một loại thuật toán tiến hóa khác được gọi một cách khó hiểu là chiến lược tiến hóa,

ES, sử dụng một hình thức tiến hóa kém chính xác về mặt sinh học, như được minh họa trong hình

6.10.

Hình 6.10.

Trong chiến lược tiến hóa, chúng ta tạo ra một quần thể gồm các cá thể bằng cách liên tục thêm vào một số lượng nhỏ

lượng nhiễu ngẫu nhiên đến cá thể bố mẹ để tạo ra nhiều biến thể của bố mẹ.

Sau đó, chúng tôi chỉ định điểm thể lực cho từng biến thể bằng cách kiểm tra chúng trong môi trường và sau đó

chúng ta có được cha mẹ mới bằng cách lấy tổng có trọng số của tất cả các biến thể.

Nếu chúng ta đang huấn luyện mạng nơ-ron bằng thuật toán ES, chúng ta sẽ bắt đầu với một tham số duy nhất

vectơ theta t, lấy mẫu một loạt các vectơ nhiễu có kích thước bằng nhau, thường là từ phân bố Gaussian,

chẳng hạn như e, sub, i, tuân theo phân phối chuẩn với giá trị trung bình mu và sigma độ lệch chuẩn, trong đó

n là phân bố Gaussian với vectơ trung bình mu và sigma độ lệch chuẩn.

Sau đó, chúng tôi tạo ra một tập hợp các vectơ tham số là phiên bản đột biến của theta t bằng cách

lấy theta i, số nguyên tố bằng theta cộng e, i.

Chúng tôi kiểm tra từng vectơ tham số đột biến này trong môi trường và gán cho chúng mức độ phù hợp

điểm dựa trên hiệu suất của họ trong môi trường.

Cuối cùng, chúng ta nhận được một vectơ tham số được cập nhật bằng cách lấy tổng có trọng số của từng biến đổi

vectơ, trong đó trọng số tỷ lệ thuận với điểm thích hợp của chúng, hình 6.11.

Hình 6.11.

Trong chiến lược tiến hóa, tại mỗi bước thời gian, chúng ta nhận được một vectơ tham số cập nhật bằng cách lấy

vectơ tham số cũ và thêm nó vào tổng có trọng số của các vectơ nhiễu, trong đó

trọng lượng tỷ lệ thuận với điểm thể lực.

Thuật toán chiến lược tiến hóa này đơn giản hơn đáng kể so với thuật toán di truyền mà chúng tôi đã triển khai

sớm hơn vì không có bước giao phối.

Chúng ta chỉ thực hiện đột biến và bước tái tổ hợp không liên quan đến việc hoán đổi các phần từ

cha mẹ khác nhau, nhưng chỉ là một phép tính tổng có trọng số đơn giản, rất dễ thực hiện

và tính toán nhanh.

Như chúng ta sẽ thấy, cách tiếp cận này cũng dễ thực hiện song song hơn.

Mục 6.5.2 xử lý song song và nối tiếp.

Khi chúng tôi sử dụng thuật toán di truyền để đào tạo các tác nhân chơi trò thăm dò giỏ hàng, chúng tôi phải tuần tự

lặp lại từng tác nhân và để mỗi tác nhân chơi cuộc thăm dò giỏ hàng cho đến khi thua để xác định

tác nhân mạnh nhất ở mỗi thế hệ trước khi chúng tôi bắt đầu đợt tiếp theo.

Nếu tác nhân mất 30 giây để chạy qua môi trường và chúng tôi đang xác định mức độ phù hợp

đối với 10 đại lý, quá trình này sẽ mất 5 phút.

Điều này được gọi là chạy một chương trình nối tiếp, hình 6.12.

Hình 6.12.

Chạy hoạt động thể chất của một đại lý thường là bước chậm nhất trong vòng đào tạo và đòi hỏi

rằng chúng tôi chạy tác nhân qua môi trường, có thể nhiều lần.

Nếu chúng tôi thực hiện việc này trên một máy tính, chúng tôi sẽ thực hiện việc này theo chuỗi.

Chúng ta phải đợi một người chạy xong môi trường trước khi có thể bắt đầu xác định

sự phù hợp của tác nhân thứ hai.

Thời gian cần thiết để chạy thuật toán này là một hàm của số lượng tác nhân và thời gian

nó cần phải chạy qua môi trường cho một tác nhân duy nhất.

Việc điều hành khả năng hoạt động của mỗi tác nhân nói chung sẽ là nhiệm vụ kéo dài nhất trong quá trình tiến hóa.

thuật toán, nhưng mỗi tác nhân có thể đánh giá mức độ phù hợp của chính nó một cách độc lập với nhau.

Nhưng chẳng có lý do gì mà chúng ta phải đợi Agent 1 chơi xong môi trường cả

trước khi chúng ta bắt đầu đánh giá tác nhân 2.

Thay vào đó, chúng ta có thể chạy từng tác nhân trong thế hệ trên nhiều máy tính cùng một lúc.

Mỗi người trong số 10 đặc vụ sẽ sử dụng 10 máy và chúng tôi có thể xác định mức độ phù hợp của họ cùng một lúc.

Điều này có nghĩa là việc hoàn thành một thế hệ sẽ mất khoảng 30 giây trên 10 máy

trái ngược với 5 phút trên một máy, tốc độ tăng gấp 10 lần.

Điều này được gọi là chạy quá trình song song, hình 6.13.

Hình 6.13.

Nếu chúng tôi có nhiều máy theo ý muốn, chúng tôi có thể xác định mức độ phù hợp của từng tác nhân

trên máy của nó song song với nhau.

Chúng ta không phải đợi một tác nhân chạy xong môi trường trước khi bắt đầu

cái tiếp theo.

Điều này sẽ giúp tăng tốc độ rất nhiều nếu chúng ta đào tạo các đặc vụ có thời lượng tập phim dài.

Bây giờ bạn có thể thấy rằng thuật toán này chỉ là một hàm của thời gian cần thiết để đánh giá

mức độ phù hợp của một tác nhân chứ không phải số lượng tác nhân mà chúng tôi đang đánh giá.

Mục 6.5.3.

Hiệu quả mở rộng quy mô

Bây giờ chúng ta có thể sử dụng nhiều máy móc và tiền bạc hơn để giải quyết vấn đề và chúng ta sẽ không phải chờ đợi nữa.

miễn là.

Trong ví dụ giả định trước đó, chúng tôi đã thêm 10 máy và tăng tốc độ gấp 10 lần

hiệu suất chia tỷ lệ là 1,0.

Hiệu quả mở rộng quy mô là một thuật ngữ được sử dụng để mô tả cách một phương pháp cụ thể được cải thiện như thế nào

tài nguyên được ném vào nó và có thể được tính như sau.

Xem công thức này.

Trong thế giới thực, các quy trình không bao giờ có hiệu suất mở rộng bằng một.

Luôn có một số chi phí bổ sung khi bổ sung thêm máy móc làm giảm hiệu quả.

Thực tế hơn, việc thêm 10 máy nữa sẽ chỉ giúp chúng ta tăng tốc độ lên 9 lần.

Sử dụng phương trình hiệu suất mở rộng quy mô trước đó, chúng ta có thể tính hiệu suất mở rộng quy mô như sau

0.9, khá tốt trong thế giới thực.

Cuối cùng, chúng ta cần kết hợp các kết quả từ việc đánh giá mức độ phù hợp của từng tác nhân trong

song song để chúng ta có thể kết hợp lại và biến đổi chúng.

Vì vậy, chúng ta cần sử dụng xử lý song song thực sự, sau đó là một giai đoạn xử lý tuần tự.

Điều này thường được gọi là tính toán phân tán, hình 6.14, vì chúng ta bắt đầu với

một bộ xử lý duy nhất, thường được gọi là nút chính và phân phối các tác vụ cho nhiều bộ xử lý

để chạy song song và sau đó thu thập kết quả trở lại nút chính.

Hình 6.14, sơ đồ chung về cách thức hoạt động của điện toán phân tán.

Nút chính phân công nhiệm vụ cho các nút công nhân.

Các nút công nhân thực hiện các nhiệm vụ đó và sau đó gửi kết quả của chúng trở lại nút chính,

không được hiển thị.

Mỗi bước cần một chút thời gian mạng để liên lạc giữa các máy, điều này

điều mà chúng ta sẽ không gặp phải nếu chạy mọi thứ trên một máy.

Ngoài ra, nếu chỉ một máy chạy chậm hơn các máy khác thì những công nhân khác sẽ cần

để chờ đợi.

Để đạt được hiệu quả mở rộng tối đa, chúng tôi muốn giảm lượng giao tiếp giữa

các nút càng nhiều càng tốt, cả về số lần các nút cần gửi dữ liệu,

cũng như lượng dữ liệu mà họ gửi.

Trong 6.5.4, giao tiếp giữa các nút.

Các nhà nghiên cứu tại OpenAI đã phát triển một chiến lược gọn gàng cho điện toán phân tán, trong đó mỗi nút

chỉ gửi một số, không phải toàn bộ vectơ, tới nút khác, loại bỏ sự cần thiết

một nút chủ riêng biệt.

Ý tưởng là mỗi công nhân lần đầu tiên được khởi tạo với cùng một vectơ tham số gốc.

Sau đó, mỗi công nhân thêm một vectơ nhiễu vào cha mẹ của nó để tạo ra một con hơi khác một chút

vectơ, hình 6.15.

Sau đó, mỗi công nhân sẽ chạy vectơ con trong môi trường để lấy điểm thể lực.

Điểm thể lực của mỗi công nhân được gửi đến tất cả các công nhân khác, việc này chỉ bao gồm việc gửi

một số duy nhất.

Vì mỗi công nhân có cùng một bộ hạt giống ngẫu nhiên nên mỗi công nhân có thể tạo lại các vectơ nhiễu

được tất cả các công nhân khác sử dụng.

Cuối cùng, mỗi công nhân tạo ra cùng một vectơ cha mẹ mới và quá trình lặp lại.

Sau phiên bản 6.15, kiến ​​trúc bắt nguồn từ bài báo ES phân tán của OpenAI.

Mỗi công nhân tạo một vectơ tham số con từ cha mẹ bằng cách thêm nhiễu vào cha mẹ.

Sau đó, nó đánh giá tình trạng thể lực của trẻ và gửi điểm thể lực cho tất cả các tác nhân khác.

Bằng cách sử dụng các hạt giống ngẫu nhiên được chia sẻ, mỗi tác nhân có thể tái tạo lại các vectơ nhiễu được sử dụng để tạo

các vectơ khác từ các công nhân khác mà không cần phải gửi toàn bộ vectơ.

Cuối cùng, các vectơ cha mẹ mới được tạo bằng cách thực hiện tổng trọng số của các vectơ con,

cân nặng theo điểm số thể lực của họ.

Việc đặt hạt giống ngẫu nhiên cho phép chúng tôi luôn tạo ra các số ngẫu nhiên giống nhau một cách nhất quán,

thậm chí trên các máy khác nhau.

Nếu bạn chạy mã trong danh sách 6.14, bạn sẽ nhận được kết quả được hiển thị, mặc dù những con số này

nên được tạo ngẫu nhiên.

Cài đặt 6.14, cài đặt hạt giống ngẫu nhiên.

Việc gieo hạt là quan trọng.

Nó cho phép các nhà nghiên cứu khác tái tạo các thí nghiệm liên quan đến số ngẫu nhiên.

Nếu bạn không cung cấp hạt giống rõ ràng, thời gian hệ thống hoặc một số loại số biến khác

được sử dụng.

Nếu chúng tôi nghĩ ra một thuật toán RL mới, chúng tôi muốn người khác có thể xác minh

làm việc trên máy của chính họ.

Chúng tôi muốn tác nhân mà phòng thí nghiệm khác tạo ra giống hệt nhau để loại bỏ mọi nguồn

có lỗi, và do đó nghi ngờ.

Đó là lý do tại sao điều quan trọng là chúng tôi phải cung cấp càng nhiều chi tiết về thuật toán của mình càng tốt.

Kiến trúc, siêu tham số được sử dụng và đôi khi là hạt giống ngẫu nhiên mà chúng tôi đã sử dụng.

Tuy nhiên, chúng tôi hy vọng chúng tôi đã phát triển được một thuật toán mạnh mẽ và tập hợp cụ thể

số ngẫu nhiên được tạo không quan trọng đối với hiệu suất của thuật toán.

Mục 6.5.5, chia tỷ lệ tuyến tính.

Khi các nhà nghiên cứu AI mở giảm khối lượng dữ liệu được gửi giữa các nút, việc thêm các nút

không ảnh hưởng đáng kể đến mạng.

Họ có thể mở rộng quy mô tới hơn một nghìn công nhân một cách tuyến tính.

Chia tỷ lệ tuyến tính có nghĩa là với mỗi máy được thêm vào, chúng tôi nhận được hiệu suất gần như nhau

boost như chúng tôi đã làm bằng cách thêm máy trước đó.

Điều này được biểu thị bằng một đường thẳng trên biểu đồ hiệu suất so với tài nguyên, như được thấy trong

hình 6.16.

Hình 6.16, hình được tái tạo từ các chiến lược tiến hóa AI mở như một giải pháp thay thế có thể mở rộng

vào bài học củng cố.

Hình này chứng minh rằng khi có nhiều tài nguyên máy tính được thêm vào thì thời gian được cải thiện

vẫn không đổi.

Phần 6.5.6, chia tỷ lệ các phương pháp tiếp cận dựa trên độ dốc.

Các phương pháp tiếp cận dựa trên gradient cũng có thể được đào tạo trên nhiều máy.

Tuy nhiên, chúng không có quy mô gần như ES.

Hiện nay, hầu hết việc đào tạo phân tán các phương pháp tiếp cận dựa trên độ dốc đều liên quan đến việc đào tạo tác nhân

trên mỗi công nhân và sau đó chuyển gradient trở lại máy trung tâm để tổng hợp.

Tất cả các gradient phải được thông qua cho mỗi chu kỳ sử thi hoặc cập nhật, đòi hỏi rất nhiều

băng thông mạng và sự căng thẳng trên máy trung tâm.

Cuối cùng, mạng lưới sẽ bão hòa và việc bổ sung thêm công nhân cũng không cải thiện được việc đào tạo

tốc độ là tốt.

Hình 6.17.

Hiệu suất của các phương pháp tiếp cận dựa trên độ dốc hiện tại trông như thế này.

Ban đầu, có một xu hướng dường như tuyến tính vì mạng chưa bão hòa.

Nhưng cuối cùng, khi nhiều tài nguyên được thêm vào, chúng ta ngày càng nhận được ít sự tăng cường hiệu suất hơn.

Mặt khác, các phương pháp tiến hóa không yêu cầu lan truyền ngược, vì vậy chúng thực hiện

không cần gửi bản cập nhật gradient đến máy chủ trung tâm.

Và với các kỹ thuật thông minh như kỹ thuật mở AI đã phát triển, họ có thể chỉ cần

gửi một số duy nhất.