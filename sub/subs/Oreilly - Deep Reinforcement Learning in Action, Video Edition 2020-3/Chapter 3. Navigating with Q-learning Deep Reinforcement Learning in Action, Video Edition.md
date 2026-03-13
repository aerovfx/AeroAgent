# Chương 3. Điều hướng bằng Học tập tăng cường sâu Q-learning trong thực tế, Phiên bản video được dịch

---

Phần 3.2 Điều hướng với Q Learning

Vào năm 2013, DeepMind đã xuất bản một bài báo có tựa đề Chơi Atari với phương pháp học tập tăng cường sâu,

đã vạch ra cách tiếp cận mới của họ đối với thuật toán cũ, mang lại cho họ đủ hiệu suất

chơi 6 trên 7 Atari, 2600 trận ở mức kỷ lục.

Điều quan trọng là thuật toán họ sử dụng chỉ dựa vào việc phân tích dữ liệu pixel thô từ trò chơi,

giống như một con người sẽ làm.

Bài viết này thực sự đặt ra lĩnh vực học tăng cường sâu.

Thuật toán cũ mà họ sửa đổi được gọi là Q Learning và nó đã tồn tại trong nhiều thập kỷ.

Tại sao phải mất quá nhiều thời gian để đạt được tiến bộ đáng kể như vậy?

Một phần lớn là do sự thúc đẩy chung của mạng lưới thần kinh nhân tạo, Deep Learning,

đã có vài năm trước với việc sử dụng GPU cho phép đào tạo các mạng lớn hơn nhiều.

Nhưng phần lớn là do các tính năng mới cụ thể mà DeepMind triển khai để giải quyết

một số vấn đề khác mà thuật toán học tăng cường gặp khó khăn.

Chúng tôi sẽ đề cập đến tất cả trong chương này.

Phần 3.2.1 Q Learning là gì?

Bạn hỏi Q Learning là gì?

Nếu bạn đoán nó có liên quan gì đó đến Hàm giá trị hành động Q Pi của SA, thì đó

chúng tôi đã mô tả trước đây, bạn nói đúng, nhưng đó chỉ là một phần nhỏ của câu chuyện.

Q Learning là một phương pháp cụ thể để học các giá trị hành động tối ưu, nhưng có những phương pháp khác

phương pháp.

Nghĩa là, hàm giá trị và hàm giá trị hành động là những khái niệm chung trong RL

xuất hiện ở nhiều nơi.

Q Learning là một thuật toán cụ thể sử dụng các khái niệm đó.

Dù bạn có tin hay không, chúng tôi đã triển khai thuật toán Q Learning ở chương trước

khi chúng tôi xây dựng mạng lưới thần kinh để tối ưu hóa vấn đề về vị trí đặt quảng cáo.

Ý tưởng chính của Q Learning là thuật toán của bạn dự đoán giá trị của cặp hành động trạng thái,

và sau đó bạn so sánh dự đoán này với phần thưởng tích lũy quan sát được sau đó

thời gian và cập nhật các tham số của thuật toán để lần sau thuật toán đưa ra dự đoán tốt hơn.

Đó thực chất là những gì chúng ta đã làm trong chương trước khi mạng lưới thần kinh của chúng ta dự đoán

phần thưởng mong đợi, giá trị của mỗi hành động trong một trạng thái, phần thưởng thực tế được quan sát,

và cập nhật mạng cho phù hợp.

Đó là cách triển khai cụ thể và đơn giản của một lớp thuật toán Q Learning rộng hơn

được mô tả bởi quy tắc cập nhật sau đây.

Bảng 3.1 Bảng xem quy tắc cập nhật học tập Q Hình

Phần 3.2.2 Xử lý thế giới lưới

Bây giờ bạn đã thấy công thức cho Q Learning.

Hãy lùi lại một bước và áp dụng công thức này cho bài toán thế giới lưới của chúng ta.

Mục tiêu của chúng ta trong chương này là huấn luyện mạng lưới thần kinh để chơi một trò chơi thế giới lưới đơn giản

từ đầu.

Tất cả các đặc vụ sẽ có quyền truy cập vào bảng trông như thế nào, giống như một người chơi

sẽ.

Thuật toán không có lợi thế về thông tin.

Hơn nữa, chúng ta đang bắt đầu với một thuật toán chưa qua huấn luyện, nên nó thực sự không biết gì cả

về thế giới.

Nó không có thông tin trước về cách trò chơi hoạt động.

Điều duy nhất sẽ cung cấp là phần thưởng cho việc đạt được mục tiêu.

Thực tế là chúng ta sẽ có thể dạy thuật toán học cách chơi, bắt đầu từ con số không,

thực sự là khá ấn tượng.

Chúng ta sẽ thảo luận về con người sống trong một dòng thời gian dường như liên tục.

Thuật toán tồn tại trong một thế giới rời rạc, do đó cần phải có điều gì đó xảy ra ở mỗi thế giới riêng biệt.

bước thời gian.

Tại thời điểm bước 1, thuật toán sẽ nhìn vào bảng trò chơi và đưa ra quyết định về những gì

hành động cần thực hiện.

Sau đó bảng trò chơi sẽ được cập nhật, v.v.

Bây giờ chúng ta hãy phác thảo chi tiết của quá trình này.

Đây là chuỗi sự kiện của trò chơi thế giới lưới.

1.

Chúng ta bắt đầu trò chơi ở một trạng thái nào đó mà chúng ta gọi là ST.

Trạng thái bao gồm tất cả thông tin về trò chơi mà chúng tôi có.

Đối với ví dụ về thế giới lưới của chúng tôi, trạng thái trò chơi được biểu diễn dưới dạng tensor 4x4x4.

Chúng ta sẽ đi vào chi tiết hơn về các chi tiết cụ thể của bảng khi chúng ta triển khai thuật toán.

2.

Chúng tôi cung cấp dữ liệu ST và hành động ứng cử viên vào mạng lưới thần kinh sâu hoặc một số thứ ưa thích khác

thuật toán học máy.

Và nó đưa ra dự đoán về giá trị của việc thực hiện hành động đó trong trạng thái đó, xem hình

3.2.

Hãy nhớ rằng thuật toán không dự đoán phần thưởng chúng ta sẽ nhận được sau khi lấy một số tiền cụ thể.

hành động.

Nó dự đoán giá trị kỳ vọng, phần thưởng kỳ vọng, là phần thưởng trung bình dài hạn

chúng ta sẽ nhận được từ việc thực hiện một hành động trong một trạng thái và sau đó tiếp tục hành xử theo

chiếc bánh chính sách của chúng tôi.

Chúng tôi làm điều này cho một số, có lẽ là tất cả, những hành động khả thi mà chúng tôi có thể thực hiện trong trạng thái này.

3.

Chúng ta thực hiện một hành động, có lẽ vì mạng lưới thần kinh của chúng ta dự đoán đó là giá trị cao nhất

hành động, hoặc có lẽ chúng ta thực hiện một hành động ngẫu nhiên.

Chúng tôi sẽ gắn nhãn hành động AT.

Bây giờ chúng ta đang ở một trạng thái mới của trò chơi, chúng ta sẽ gọi là ST cộng 1 và chúng ta nhận hoặc quan sát

một phần thưởng có nhãn RT cộng 1.

Chúng tôi muốn cập nhật thuật toán học tập của mình để phản ánh phần thưởng thực tế mà chúng tôi nhận được sau

thực hiện hành động mà nó dự đoán là tốt nhất.

Có lẽ chúng tôi đã nhận được phần thưởng tiêu cực hoặc phần thưởng thực sự lớn và chúng tôi muốn cải thiện độ chính xác

dự đoán của thuật toán, xem hình 3.3.

4.

Bây giờ chúng tôi chạy thuật toán sử dụng ST cộng 1 làm đầu vào và tìm ra hành động mà thuật toán của chúng tôi thực hiện

dự đoán có giá trị cao nhất.

Chúng ta sẽ gọi giá trị này là Q của ST cộng 1A.

Nói rõ hơn, đây là một giá trị duy nhất phản ánh giá trị Q được dự đoán cao nhất, cho trước

trạng thái mới của chúng tôi và tất cả các hành động có thể.

5.

Bây giờ chúng ta đã có tất cả những phần cần thiết để cập nhật các tham số của thuật toán.

Chúng ta sẽ thực hiện một lần huấn luyện bằng cách sử dụng một số hàm mất mát, chẳng hạn như bình phương trung bình

lỗi, để giảm thiểu sự khác biệt giữa giá trị dự đoán từ thuật toán của chúng tôi và

dự đoán mục tiêu này.

Hình 3.3, sơ đồ Q học với thế giới lưới, hàm Q nhận trạng thái và

một hành động và trả về phần thưởng, giá trị dự đoán của cặp hành động trạng thái đó.

Sau khi thực hiện hành động, chúng tôi quan sát phần thưởng và sử dụng công thức cập nhật, chúng tôi sử dụng công thức này

quan sát để cập nhật hàm Q để đưa ra dự đoán tốt hơn.

Hình 3.2, hàm Q có thể là bất kỳ hàm nào chấp nhận trạng thái và hành động rồi trả về

giá trị, phần thưởng mong đợi của việc thực hiện hành động đó trong trạng thái đó.

Phần 3.2.3, siêu tham số.

Các tham số gamma và alpha được gọi là siêu tham số vì chúng là các tham số ảnh hưởng đến

thuật toán học như thế nào nhưng chúng không liên quan đến việc học thực sự.

Tham số alpha là tốc độ học tập và nó là siêu tham số tương tự được sử dụng để huấn luyện

nhiều thuật toán học máy.

Nó kiểm soát tốc độ chúng ta muốn thuật toán học hỏi từ mỗi lần di chuyển.

Giá trị nhỏ có nghĩa là nó sẽ chỉ thực hiện các cập nhật nhỏ ở mỗi bước, trong khi giá trị lớn

có nghĩa là thuật toán sẽ có khả năng thực hiện các cập nhật lớn.

Mục 3.2.4, hệ số chiết khấu.

Tham số gamma, hệ số chiết khấu, là một biến từ 0 đến 1 kiểm soát

đại lý của chúng tôi giảm giá bao nhiêu phần thưởng trong tương lai khi đưa ra quyết định.

Hãy lấy một ví dụ đơn giản.

Đại lý của chúng tôi có quyết định giữa việc chọn một hành động dẫn đến 0 phần thưởng, sau đó cộng thêm

Phần thưởng 1 hoặc hành động dẫn đến phần thưởng cộng 1 rồi đến phần thưởng 0, xem Hình 3.4.

Hình 3.4 minh họa quỹ đạo hành động dẫn đến tổng phần thưởng như nhau, nhưng

có thể được đánh giá khác nhau vì những phần thưởng gần đây thường có giá trị cao hơn những phần thưởng xa hơn

phần thưởng.

Trước đây chúng ta đã xác định giá trị của quỹ đạo là phần thưởng mong đợi.

Tuy nhiên, cả hai quỹ đạo trong Hình 3.4 đều cung cấp cộng thêm 1 phần thưởng tổng thể, vậy trình tự nào

thuật toán nên ưu tiên hành động nào?

Làm thế nào chúng ta có thể phá vỡ sự ràng buộc?

Chà, nếu gamma hệ số chiết khấu nhỏ hơn 1, chúng tôi sẽ chiết khấu nhiều hơn cho các phần thưởng trong tương lai

hơn là những phần thưởng ngay lập tức.

Trong trường hợp đơn giản này, mặc dù cả hai con đường đều dẫn đến tổng cộng 1 phần thưởng, nhưng hành động

b nhận được phần thưởng cộng 1 muộn hơn hành động a và vì chúng tôi đang giảm giá cho hành động

hơn nữa trong tương lai, chúng tôi thích hành động a.

Chúng tôi nhân phần thưởng cộng 1 trong hành động b với hệ số chờ nhỏ hơn 1, vì vậy chúng tôi hạ thấp

phần thưởng từ cộng 1 thành 0,8, như vậy việc lựa chọn hành động đã rõ ràng.

Yếu tố chiết khấu xuất hiện trong đời thực cũng như RL.

Giả sử ai đó đề nghị cho bạn 100 USD bây giờ hoặc 110 USD sau một tháng nữa.

Hầu hết mọi người muốn nhận tiền ngay bây giờ vì chúng tôi chiết khấu tương lai cho một số người.

mức độ, điều này có ý nghĩa vì tương lai là không chắc chắn.

Điều gì sẽ xảy ra nếu người đưa tiền cho bạn chết sau hai tuần nữa?

Hệ số chiết khấu của bạn trong cuộc sống thực sẽ phụ thuộc vào số tiền mà ai đó sẽ phải trả

đề nghị bạn trong một tháng để bạn thờ ơ với việc lựa chọn điều đó so với việc nhận đúng 100 đô la

bây giờ.

Nếu bạn chỉ chấp nhận 200 đô la trong một tháng so với 100 đô la ngay bây giờ, hệ số chiết khấu của bạn sẽ

được 100 USD chia cho 200 USD bằng 0,5 USD mỗi tháng.

Điều này có nghĩa là ai đó sẽ phải đề nghị cho bạn 400 USD trong hai tháng để bạn lựa chọn.

tùy chọn đó thay vì nhận 100 đô la ngay bây giờ, vì chúng tôi giảm giá 0,5 đô la trong một tháng và 0,5 đô la một lần nữa

cho tháng tiếp theo, tức là 0,5 USD nhân 0,5 USD bằng 0,25 USD và 100 USD bằng 0,25 USD, vì vậy x bằng

400 đô la.

Có lẽ bạn có thể thấy mô hình giảm giá theo cấp số nhân theo thời gian.

Giá trị của một vật tại thời điểm t với hệ số chiết khấu gamma nằm trong khoảng từ 0 đến 1 là gamma

với sức mạnh của t.

Hệ số chiết khấu cần phải nằm trong khoảng từ 0 đến 1 và chúng ta không nên đặt hệ số này bằng chính xác

lên 1, vì nếu không giảm giá chút nào, chúng ta sẽ phải xem xét phần thưởng trong tương lai

vô cùng xa trong tương lai, điều này là không thể trong thực tế.

Ngay cả khi chúng tôi giảm giá ở mức 0,99999, cuối cùng sẽ đến một thời điểm mà chúng tôi không thể

hãy xem xét bất kỳ dữ liệu nào lâu hơn vì nó sẽ được chiết khấu về 0.

Trong QLearning, chúng tôi phải đối mặt với quyết định tương tự.

Chúng ta cân nhắc bao nhiêu phần thưởng quan sát được trong tương lai khi học cách dự đoán giá trị Q?

Thật không may, không có câu trả lời dứt khoát cho vấn đề này hoặc để thiết lập hầu hết các

các siêu tham số mà chúng tôi có quyền kiểm soát.

Chúng ta chỉ cần thử nghiệm những nút này và xem cái nào hoạt động tốt nhất theo kinh nghiệm.

Cần chỉ ra rằng hầu hết các trò chơi đều có tính chất từng tập, nghĩa là có nhiều

cơ hội để hành động trước khi trận đấu kết thúc, và nhiều trò chơi như cờ vua thì không tự nhiên

chỉ định điểm cho bất cứ điều gì khác ngoài việc thắng hoặc thua trò chơi.

Do đó, tín hiệu thưởng trong các trò chơi này rất thưa thớt, gây khó khăn cho việc thử và dựa trên lỗi.

học cách học bất cứ điều gì một cách đáng tin cậy, vì nó đòi hỏi phải nhìn thấy phần thưởng khá thường xuyên.

Trong GridWorld, chúng tôi đã thiết kế trò chơi sao cho bất kỳ nước đi nào không thắng trò chơi sẽ nhận được

phần thưởng trừ 1.

Nước đi thắng được thưởng cộng 10 và nước đi thua được thưởng trừ 10.

Đây thực sự chỉ là nước đi cuối cùng của trò chơi mà thuật toán có thể nói, aha, giờ tôi hiểu rồi

nó.

Vì mỗi tập của trò chơi GridWorld có thể giành chiến thắng chỉ với một số nước đi khá nhỏ, nên

vấn đề phần thưởng thưa thớt không phải là quá tệ, nhưng trong các trò chơi khác thì đó lại là một vấn đề nghiêm trọng

rằng ngay cả những thuật toán học tăng cường tiên tiến nhất vẫn chưa đến được với con người

hiệu suất cấp độ.

Một phương pháp được đề xuất để giải quyết vấn đề này là ngừng dựa vào mục tiêu tối đa hóa

phần thưởng mong đợi và thay vào đó hướng dẫn thuật toán tìm kiếm tính mới, qua đó nó sẽ

tìm hiểu về môi trường của nó, đó là điều chúng ta sẽ đề cập đến trong chương 8.

Mục 3.2.5.

Xây dựng mạng lưới.

Hãy cùng tìm hiểu cách chúng tôi xây dựng thuật toán deep learning cho trò chơi này.

Hãy nhớ lại rằng mạng nơ-ron có một loại kiến ​​trúc hoặc cấu trúc liên kết mạng cụ thể.

Khi bạn xây dựng một mạng lưới thần kinh, bạn phải quyết định xem nó nên có bao nhiêu lớp, như thế nào

nhiều tham số mà mỗi lớp có, độ rộng của lớp và cách các lớp được kết nối.

GridWorld đủ đơn giản để chúng ta không cần phải xây dựng bất cứ thứ gì cầu kỳ.

Chúng ta có thể tạo ra một mạng nơ-ron chuyển tiếp nguồn cấp dữ liệu khá đơn giản chỉ với một vài

các lớp, sử dụng đơn vị kích hoạt tuyến tính được chỉnh lưu điển hình RayLoo.

Phần duy nhất cần suy nghĩ cẩn thận hơn là cách chúng ta trình bày thông tin đầu vào của mình.

dữ liệu và cách chúng tôi sẽ thể hiện lớp đầu ra.

Chúng ta sẽ bao phủ lớp đầu ra trước tiên.

Trong cuộc thảo luận về việc học Q, chúng ta đã nói rằng hàm Q là một hàm có

một số trạng thái và một số hành động, rồi tính giá trị của cặp hành động trạng thái đó, Q của

SA.

Đây là cách xác định hàm Q ban đầu, hình 3.5.

Như chúng ta đã lưu ý ở chương trước, cũng có một hàm giá trị trạng thái, thường được ký hiệu là

v pi của S, tính toán giá trị của một trạng thái nào đó, với điều kiện là bạn đang theo dõi một trạng thái cụ thể

chính sách pi.

Hình 3.5.

Hàm Q ban đầu chấp nhận một cặp hành động trạng thái và trả về giá trị của hành động trạng thái đó

cặp, một số duy nhất.

Hãy nhớ rằng đã sử dụng hàm Q có giá trị vectơ đã sửa đổi để chấp nhận trạng thái và trả về

một vectơ chứa các giá trị hành động trạng thái, một giá trị cho mỗi hành động có thể có với trạng thái đầu vào.

Hàm Q có giá trị vectơ hiệu quả hơn vì bạn chỉ cần tính hàm một lần

cho mọi hành động.

Nói chung, chúng ta muốn sử dụng hàm Q vì nó có thể cho chúng ta biết giá trị của việc lấy một

hành động ở một trạng thái nào đó, vì vậy chúng ta có thể thực hiện hành động có giá trị dự đoán cao nhất.

Nhưng sẽ khá lãng phí nếu tính toán riêng các giá trị Q cho từng hành động có thể xảy ra.

với trạng thái nhất định, mặc dù hàm Q ban đầu được xác định theo cách đó.

Một quy trình hiệu quả hơn nhiều và là quy trình mà tâm trí sâu sắc đã sử dụng để thực hiện nó

của học sâu Q, thay vào đó là viết lại hàm Q dưới dạng hàm có giá trị vectơ, nghĩa là

rằng thay vì tính toán trả về một giá trị Q duy nhất cho một cặp hành động trạng thái, nó

sẽ tính toán các giá trị Q cho tất cả các hành động cho trước một số trạng thái và trả về vectơ của tất cả

những giá trị Q đó.

Vì vậy, chúng ta có thể biểu thị phiên bản mới này của hàm Q là QA của S, trong đó chỉ số dưới

A biểu thị tập hợp tất cả các hành động có thể xảy ra, hình 3.5.

Giờ đây thật dễ dàng để sử dụng mạng thần kinh làm phiên bản QA của S của hàm Q.

Lớp cuối cùng sẽ đơn giản tạo ra một vectơ đầu ra có các giá trị Q, một cho mỗi giá trị có thể

hoạt động.

Trong trường hợp của GridWorld, chỉ có bốn hành động có thể thực hiện được là lên, xuống, trái, phải,

vì vậy lớp đầu ra sẽ tạo ra các vectơ bốn chiều.

Sau đó, chúng ta có thể trực tiếp sử dụng đầu ra của mạng lưới thần kinh để quyết định hành động cần thực hiện

sử dụng một số quy trình lựa chọn hành động, chẳng hạn như cách tiếp cận tham lam Epsilon đơn giản hoặc

chính sách lựa chọn softmax

Trong chương này, chúng ta sẽ sử dụng cách tiếp cận tham lam của Epsilon, hình 3.6, như tâm trí sâu sắc đã làm,

và thay vì sử dụng giá trị Epsilon tĩnh như chúng ta đã làm ở chương trước, chúng ta sẽ

khởi tạo nó thành một giá trị lớn, tức là 1, vì vậy chúng ta sẽ bắt đầu với một lựa chọn hoàn toàn ngẫu nhiên

của các hành động.

Và chúng ta sẽ giảm dần nó để sau một số lần lặp nhất định, Epsilon

giá trị sẽ nằm ở một giá trị nhỏ nào đó.

Bằng cách này, chúng tôi sẽ cho phép thuật toán khám phá và học hỏi nhiều điều ngay từ đầu,

nhưng sau đó nó sẽ quyết định tối đa hóa phần thưởng bằng cách khai thác những gì nó đã học được.

Hy vọng rằng chúng ta sẽ thiết lập quy trình giảm dần để nó không bị khám phá quá mức hoặc khám phá quá mức,

nhưng điều đó sẽ phải được kiểm tra bằng thực nghiệm.

Hình 3.6, trong phương pháp lựa chọn hành động tham lam của Epsilon, chúng ta đặt tham số Epsilon thành một số

giá trị, ví dụ 0,1 và với xác suất đó, chúng tôi sẽ chọn ngẫu nhiên một hành động, hoàn toàn

bỏ qua các giá trị Q dự đoán hoặc với xác suất 1 trừ Epsilon bằng 0,9, chúng ta sẽ

chọn hành động liên quan đến giá trị Q được dự đoán cao nhất.

Một kỹ thuật hữu ích bổ sung là bắt đầu với giá trị Epsilon cao, chẳng hạn như 1, sau đó

giảm dần nó qua các lần lặp đào tạo.

Chúng ta đã tìm ra lớp đầu ra, bây giờ chúng ta sẽ giải quyết phần còn lại.

Trong chương này, chúng ta sẽ xây dựng một mạng chỉ có 3 lớp với độ rộng 164 đầu vào

lớp, 150, lớp ẩn, 4, lớp đầu ra mà bạn đã thấy.

Bạn được hoan nghênh và khuyến khích thêm nhiều lớp ẩn hơn hoặc thử nghiệm với kích thước của

lớp ẩn.

Bạn có thể sẽ đạt được kết quả tốt hơn với mạng lưới sâu hơn.

Chúng tôi đã chọn triển khai một mạng khá nông ở đây để bạn có thể huấn luyện mô hình với

CPU của riêng bạn, cần có MacBook Air 1,7 GHz Intel Core Y7 với 8GB RAM chỉ một vài

phút để tập luyện.

Chúng ta đã thảo luận tại sao lớp đầu ra có chiều rộng 4, nhưng chúng ta chưa nói về

lớp đầu vào chưa.

Tuy nhiên, trước khi làm điều đó, chúng tôi cần giới thiệu GridWorld Game Engine mà chúng tôi sẽ sử dụng.

Chúng tôi đã phát triển Trò chơi GridWorld cho cuốn sách này và nó được đưa vào kho GitHub

cho chương này.

Phần 3, 2.6, giới thiệu GridWorld Game Engine.

Trong kho GitHub của chương này, bạn sẽ tìm thấy một tệp có tên là Gridworld.py.

Sao chép và dán tập tin này vào bất kỳ thư mục nào bạn sẽ làm việc.

Bạn có thể đưa nó vào phiên Python của mình bằng cách chạy từ ngôi sao nhập GridWorld.

Mô-đun GridWorld chứa một số lớp và hàm trợ giúp để chạy Trò chơi GridWorld

ví dụ.

Để tạo một phiên bản Trò chơi GridWorld, hãy chạy mã trong danh sách sau.

Tạo 3.1, tạo Trò chơi GridWorld.

Bảng GridWorld luôn có hình vuông nên kích thước đề cập đến kích thước của một bên.

Trong trường hợp này, Lưới 4x4 sẽ được tạo.

Có ba cách để khởi tạo bảng.

Đầu tiên là khởi tạo nó một cách tĩnh, như đăng ký 3.1, sao cho các đối tượng trên

board được khởi tạo tại cùng một vị trí được xác định trước.

Thứ hai, bạn có thể đặt chế độ bằng trình phát để chỉ trình phát được khởi tạo ngẫu nhiên

vị trí trên bảng.

Cuối cùng, bạn có thể khởi tạo nó để tất cả các đối tượng được đặt ngẫu nhiên, điều này khó hơn

để thuật toán học, sử dụng chế độ bằng ngẫu nhiên.

Cuối cùng chúng tôi sẽ sử dụng cả ba tùy chọn.

Bây giờ chúng ta đã tạo xong trò chơi, hãy chơi nó.

Gọi phương thức hiển thị để hiển thị bảng và phương thức thực hiện di chuyển để thực hiện một nước đi.

Sử dụng mã hóa của chúng tôi với một chữ cái duy nhất, bạn ở trên, L ở bên trái, v.v.

Sau mỗi lần di chuyển, bạn nên hiển thị bảng để xem hiệu quả.

Ngoài ra, sau mỗi nước đi, bạn sẽ muốn quan sát kết quả thưởng của nước đi đó.

bằng cách gọi phương thức khen thưởng.

Trong GridWorld, mỗi nước đi không thắng sẽ nhận được phần thưởng trừ một.

Nước đi thắng, về đích được thưởng cộng mười, có trừ mười

phần thưởng cho nước đi thua, rơi xuống hố.

Xem mã này.

Bây giờ chúng ta hãy xem trạng thái trò chơi thực sự được thể hiện như thế nào, vì chúng ta sẽ cần cung cấp thông tin này

vào mạng lưới thần kinh của chúng ta.

Chạy lệnh sau.

Xem mã này.

Trạng thái được biểu diễn dưới dạng tensor 4x4x4, trong đó chỉ số chiều thứ nhất là tập hợp bốn

ma trận có kích thước 4x4.

Bạn có thể hiểu điều này là có kích thước khung theo chiều cao và chiều rộng.

Mỗi ma trận là một lưới 4x4 gồm các số 0 và một số 0, trong đó một số 1 biểu thị vị trí

của một đối tượng cụ thể.

Mỗi ma trận mã hóa vị trí của một trong bốn đối tượng, người chơi, mục tiêu,

hố và tường.

Nếu bạn so sánh kết quả hiển thị với trạng thái trò chơi, bạn có thể thấy rằng điều đầu tiên

ma trận mã hóa vị trí của người chơi.

Ma trận thứ hai mã hóa vị trí mục tiêu, ma trận thứ ba mã hóa vị trí

của hố và ma trận cuối cùng mã hóa vị trí của bức tường.

Nói cách khác, chiều thứ nhất của ba tensor này được chia thành bốn lưới riêng biệt

mặt phẳng, trong đó mỗi mặt phẳng thể hiện vị trí của từng phần tử.

Hình 3.7 minh họa ví dụ người chơi ở vị trí lưới 2, 2, mục tiêu là 0,

hố là 0, 1, tường là 1, 1, trong đó các mặt phẳng là hàng, cột.

Tất cả các yếu tố khác là số không.

Hình 3.7.

Đây là cách bảng lưới thế giới được biểu diễn dưới dạng mảng num pi.

Nó là một tenxơ 4x4 bao gồm bốn lát lưới 4x4.

Mỗi lát lưới đại diện cho vị trí của một đối tượng riêng lẻ trên bảng và chứa

một phần tử duy nhất, với tất cả các phần tử khác là số không.

Vị trí của một biểu thị vị trí của đối tượng của lát cắt đó.

Về nguyên tắc, mặc dù chúng ta có thể xây dựng một mạng lưới thần kinh có thể hoạt động trên một tensor 4x4x4,

sẽ dễ dàng hơn nếu chỉ làm phẳng nó thành một tenxơ 1, một vectơ.

Một tenxơ 4x4x4 có 4 lập phương bằng tổng cộng 64 phần tử, vì vậy lớp đầu vào của mạng thần kinh của chúng ta

mạng phải được định hình phù hợp.

Mạng lưới thần kinh sẽ phải tìm hiểu ý nghĩa của dữ liệu này và nó liên quan như thế nào đến việc tối đa hóa

phần thưởng.

Hãy nhớ rằng, thuật toán sẽ hoàn toàn không biết gì để bắt đầu.

Mục 3.2.7.

Mạng nơ-ron là hàm Q.

Hãy xây dựng mạng lưới thần kinh sẽ đóng vai trò là hàm Q của chúng ta.

Như bạn đã biết, trong cuốn sách này, chúng tôi đang sử dụng pi torch cho tất cả các mô hình deep learning của mình, nhưng nếu

bạn thấy thoải mái hơn với một khung khác như tensor flow hoặc MX net, thì nó phải như vậy

khá đơn giản để chuyển các mô hình.

Hình 3.8 thể hiện kiến ​​trúc chung của mô hình chúng ta sẽ xây dựng.

Hình 3.9 thể hiện nó ở dạng sơ đồ chuỗi với các chuỗi được gõ.

Hình 3.8.

Mô hình mạng nơron mà chúng ta sẽ sử dụng để chơi GridWorld.

Mô hình có lớp đầu vào có thể chấp nhận vectơ trạng thái trò chơi có độ dài 64.

Một số lớp ẩn, chúng tôi sử dụng một nhưng hai lớp được mô tả cho tính tổng quát.

Lớp đầu ra tạo ra vectơ có độ dài 4 giá trị Q cho mỗi hành động với trạng thái nhất định.

Hình 3.9.

Sơ đồ chuỗi cho DQN của chúng tôi.

Đầu vào là vectơ Boolean có độ dài 64 và đầu ra là vectơ thực có độ dài 4 có giá trị Q.

Để thực hiện điều này với pi torch, chúng ta sẽ sử dụng mô-đun NN, đây là giao diện cấp cao hơn

đối với đèn pin pi, tương tự như Keras đối với dòng tensor.

Chuỗi 3.2, hàm Q mạng nơ-ron.

Cho đến nay, tất cả những gì chúng ta đã làm là thiết lập mô hình mạng nơ-ron, xác định hàm mất mát và học

tốc độ, thiết lập trình tối ưu hóa và xác định một vài tham số.

Nếu đây là một mạng lưới thần kinh phân loại đơn giản thì chúng ta gần như đã hoàn thành.

Chúng ta chỉ cần thiết lập một vòng lặp for để chạy lặp lại trình tối ưu hóa nhằm giảm thiểu lỗi mô hình

đối với dữ liệu.

Việc học tăng cường sẽ phức tạp hơn, đó có thể là lý do tại sao bạn đang đọc

cuốn sách này.

Chúng ta đã trình bày rõ các bước chính trước đó nhưng hãy phóng to một chút.

Liệt kê 3.3 thực hiện vòng lặp chính của thuật toán.

Nói một cách rộng rãi, đây là những gì nó làm.

1.

Chúng tôi thiết lập một vòng lặp for cho số kỷ nguyên.

2.

Trong vòng lặp, chúng ta thiết lập vòng lặp while khi trò chơi đang diễn ra.

3.

Chúng tôi chạy mạng Q về phía trước.

4.

Chúng tôi đang sử dụng triển khai tham lam Epsilon.

Vì vậy tại thời điểm t với xác suất Epsilon, chúng ta sẽ chọn một hành động ngẫu nhiên.

Với xác suất 1 trừ Epsilon, chúng ta sẽ chọn hành động có kết quả cao nhất

Giá trị Q từ mạng lưới thần kinh của chúng tôi.

5.

Thực hiện hành động a như đã xác định ở bước trước và quan sát nguyên tố và trạng thái mới

phần thưởng rt cộng 1.

6.

Chạy mạng chuyển tiếp bằng cách sử dụng s prime.

Lưu trữ giá trị Q cao nhất mà chúng tôi gọi là Q tối đa.

7.

Giá trị mục tiêu của chúng tôi cho việc huấn luyện mạng là thế này, trong đó gamma là tham số từ 0 đến

1.

Nếu sau khi thực hiện hành động, trò chơi kết thúc thì không có điểm cộng 1 hợp lệ.

Vì vậy, điều này không hợp lệ và chúng ta có thể đặt nó thành 0.

Mục tiêu chỉ trở thành rt cộng 1.

8.

Thậm chí chúng tôi có 4 đầu ra và chúng tôi chỉ muốn cập nhật, đó là tàu, đầu ra liên quan

với hành động chúng ta vừa thực hiện.

Vectơ đầu ra mục tiêu của chúng ta giống với vectơ đầu ra của lần chạy đầu tiên, ngoại trừ

chúng tôi thay đổi một đầu ra liên quan đến hành động của chúng tôi thành kết quả mà chúng tôi đã tính toán bằng cách sử dụng

Công thức học Q.

9.

Huấn luyện mô hình trên mẫu này, sau đó lặp lại các bước 2.9.

Nói rõ hơn, khi chúng ta chạy mạng nơ-ron lần đầu tiên và nhận được kết quả là các giá trị hành động

như thế này, xem mã này.

Vectơ mục tiêu của chúng ta cho một lần lặp có thể trông như thế này.

Xem mã này.

Ở đây chúng tôi chỉ thay đổi một mục nhập thành giá trị mà chúng tôi muốn cập nhật.

Có một chi tiết khác mà chúng ta cần đưa vào mã trước khi tiếp tục.

Phương thức di chuyển của công cụ trò chơi thế giới lưới mong muốn nhân vật như bạn thực hiện một bước di chuyển,

nhưng thuật toán học Q của chúng tôi chỉ biết cách tạo ra các con số.

Vì vậy chúng ta cần một bản đồ đơn giản từ phím số đến ký tự hành động.

Xem mã này.

Được rồi, hãy bắt đầu viết mã cho vòng lặp đào tạo chính.

Liệt kê 3.3, Q learning, vòng huấn luyện chính.

Lưu ý, tại sao chúng tôi lại thêm tiếng ồn vào trạng thái trò chơi?

Nó giúp ngăn chặn các tế bào thần kinh chết, có thể xảy ra khi sử dụng các đơn vị tuyến tính được chỉnh lưu

Ray-Loo là chức năng kích hoạt của chúng tôi.

Về cơ bản, vì hầu hết các phần tử trong mảng trạng thái trò chơi của chúng ta đều là 0 nên chúng sẽ không chơi

tốt với Ray-Loo, về mặt kỹ thuật không thể phân biệt được ở mức 0.

Do đó, chúng tôi thêm một chút nhiễu để không có giá trị nào trong mảng trạng thái chính xác

0.

Điều này cũng có thể giúp khắc phục tình trạng trang bị quá mức, đó là khi người mẫu học bằng cách ghi nhớ các thông tin giả.

chi tiết trong dữ liệu mà không tìm hiểu các tính năng trừu tượng của dữ liệu, cuối cùng ngăn chặn

nó từ khái quát hóa đến dữ liệu mới.

Có một vài điều cần chỉ ra rằng bạn có thể chưa từng thấy trước đây.

Điều mới đầu tiên là việc sử dụng bối cảnh torched.no gạch dưới grad khi tính toán

giá trị Q trạng thái tiếp theo.

Bất cứ khi nào chúng ta chạy mô hình ngọn đuốc tròn với một số đầu vào, nó sẽ ngầm tạo ra một mô hình tính toán

đồ thị.

Mỗi tensor ngọn đuốc hình tròn không chỉ là nơi lưu trữ dữ liệu tensor mà còn theo dõi dữ liệu nào

tính toán đã được thực hiện để tạo ra nó.

Bằng cách sử dụng bối cảnh cấp độ gạch dưới của torched.no, chúng tôi yêu cầu pie torch không tạo ra một thuật toán tính toán

biểu đồ cho mã trong ngữ cảnh.

Điều này sẽ tiết kiệm bộ nhớ khi chúng ta không cần đến đồ thị tính toán.

Khi tính toán các giá trị Q cho trạng thái 2, chúng tôi chỉ sử dụng chúng làm mục tiêu đào tạo.

Chúng tôi sẽ không truyền bá ngược lại thông qua biểu đồ tính toán mà lẽ ra đã có

được tạo nếu chúng tôi không sử dụng torched.no gạch dưới grad.

Chúng tôi chỉ muốn truyền ngược thông qua biểu đồ tính toán được tạo khi chúng tôi gọi

mô hình trạng thái 1 vì chúng tôi muốn huấn luyện các tham số liên quan đến trạng thái 1 chứ không phải

trạng thái 2.

Đây là một ví dụ đơn giản với mô hình tuyến tính.

Xem mã này.

Chúng ta tạo hai tham số có thể huấn luyện được, M và B, bằng cách đặt mức độ gạch dưới yêu cầu của chúng.

thuộc tính thành true, có nghĩa là pie torch sẽ coi các tham số này là các nút trong

đồ thị tính toán và sẽ lưu trữ lịch sử tính toán của họ.

Bất kỳ tensor mới nào được tạo bằng M và B chẳng hạn như Y trong trường hợp này cũng sẽ có

yêu cầu cấp độ gạch dưới được đặt thành true và do đó cũng sẽ lưu giữ bộ nhớ tính toán của chúng

lịch sử.

Bạn có thể thấy rằng lần đầu tiên chúng ta gọi mô hình tuyến tính và in Y, nó cho chúng ta một tensor

với kết quả bằng số và cũng hiển thị một thuộc tính.

Dấu gạch dưới cấp độ fn bằng với việc thêm số 0 ngược.

Chúng ta cũng có thể thấy trực tiếp thuộc tính này bằng cách in dấu gạch dưới cấp độ Y chấm fn.

Điều này chứng tỏ tensor này được tạo ra bởi phép cộng.

Nó được gọi là cộng ngược vì nó thực sự lưu trữ đạo hàm của hàm cộng.

Nếu bạn gọi hàm này với một đầu vào, nó sẽ trả về hai đầu ra, ngược lại với

phép cộng, nhận hai đầu vào và trả về một đầu ra.

Vì hàm cộng của chúng ta là hàm hai biến nên có đạo hàm riêng

đối với đầu vào thứ nhất và đạo hàm riêng đối với đầu vào thứ hai.

Đạo hàm riêng của Y bằng A cộng B đối với M bằng delta Y chia cho

delta A bằng một, và delta Y chia cho delta B bằng một.

Hoặc nếu Y bằng A nhân B, thì delta Y chia cho delta A bằng B và delta Y chia

bởi delta B bằng A. Đây chỉ là những quy tắc cơ bản của việc lấy đạo hàm.

Khi chúng ta truyền ngược từ một nút nhất định, chúng ta cần nó trả về tất cả các đạo hàm riêng,

vì vậy đó là lý do tại sao hàm gradient 0 lùi lại trả về hai kết quả đầu ra.

Chúng tôi có thể xác minh rằng PyTorch thực sự đang tính toán độ dốc như mong đợi bằng cách gọi hàm ngược

phương pháp trên Y. Xem mã này.

Đây chính xác là những gì chúng ta sẽ nhận được từ việc tính toán các đạo hàm riêng đơn giản này trong đầu,

hoặc trên giấy. Để truyền ngược hiệu quả, PyTorch theo dõi tất cả các tính toán chuyển tiếp

và lưu trữ đạo hàm của chúng, để cuối cùng khi chúng ta gọi phương thức lùi trên đầu ra

nút của biểu đồ tính toán của chúng tôi, nó sẽ lan truyền trở lại thông qua các hàm gradient này

từng nút một cho đến nút đầu vào. Đó là cách chúng tôi có được độ dốc cho tất cả các tham số

trong mô hình. Lưu ý rằng chúng ta cũng gọi phương thức tách trên tensor Y. Đây là

thực sự không cần thiết, vì chúng tôi đã sử dụng Torch.no gạch dưới grad, khi chúng tôi tính toán hàng đợi mới,

nhưng chúng tôi đã đưa nó vào vì việc tách các nút khỏi biểu đồ tính toán sẽ trở nên phổ biến

trong suốt phần còn lại của cuốn sách và việc tách các nút không đúng cách là nguyên nhân phổ biến

các lỗi khi huấn luyện mô hình. Nếu chúng ta gọi phương thức lùi trên biến mất mát, chuyển

X và Y làm đối số và Y được liên kết với biểu đồ tính toán của chính nó với khả năng huấn luyện

các tham số, chúng tôi sẽ truyền ngược vào Y và X, và quy trình huấn luyện sẽ học

để giảm thiểu tổn thất bằng cách cập nhật các tham số có thể huấn luyện trong biểu đồ X và biểu đồ Y,

trong khi chúng tôi chỉ muốn cập nhật biểu đồ X. Chúng tôi tách nút Y khỏi biểu đồ để

nó chỉ được sử dụng làm dữ liệu chứ không phải là nút biểu đồ tính toán. Bạn không cần phải suy nghĩ quá nhiều

về các chi tiết, nhưng bạn cần phải chú ý đến phần nào của biểu đồ mà bạn đang

thực sự truyền ngược vào và đảm bảo rằng bạn không truyền ngược vào sai

nút. Bạn có thể tiếp tục và chạy vòng đào tạo. 1.000

kỷ nguyên sẽ là quá đủ. Sau khi hoàn tất, bạn có thể vẽ biểu đồ tổn thất để xem liệu

đào tạo thành công và mô hình hội tụ. Sự mất mát ít nhiều sẽ giảm và ổn định

trong suốt thời gian đào tạo. Đồ thị của chúng tôi được thể hiện trong Hình 3.10.

Hình 3.10, biểu đồ mất mát cho thuật toán Q-learning đầu tiên của chúng tôi, rõ ràng đang có xu hướng giảm dần

các thời đại đào tạo. Cốt truyện mất mát khá ồn ào nhưng cảm động

trung bình của đồ thị đang có xu hướng tiến tới 0 một cách đáng kể. Điều này mang lại cho chúng tôi sự tự tin

quá trình đào tạo đã có hiệu quả nhưng chúng ta sẽ không bao giờ biết được cho đến khi kiểm tra nó. Chúng tôi đã viết một cách đơn giản

trong danh sách 3.4 cho phép chúng tôi thử nghiệm mô hình trên một trò chơi.

Liệt kê 3.4, kiểm tra mạng Q. Chức năng kiểm tra về cơ bản giống như chức năng

mã trong vòng đào tạo của chúng tôi, ngoại trừ việc chúng tôi không thực hiện bất kỳ phép tính tổn thất hoặc truyền ngược nào.

Chúng tôi chỉ chạy mạng về phía trước để nhận được dự đoán. Hãy xem liệu nó có học được như thế nào không

để chơi GridWorld. Xem mã này. Chúng ta có thể nhận được một tràng pháo tay không

cho người chơi GridWorld của chúng ta ở đây? Rõ ràng là nó biết nó đang làm gì. Nó đi thẳng tới

mục tiêu. Nhưng chúng ta đừng quá phấn khích. Đó là phiên bản tĩnh của trò chơi,

thực sự rất dễ dàng. Nếu bạn sử dụng chức năng kiểm tra của chúng tôi với chế độ bằng ngẫu nhiên, bạn sẽ tìm thấy một số

sự thất vọng. Xem mã này. Điều này thực sự thú vị. Nhìn kỹ

tại các bước di chuyển mà mạng đang thực hiện. Người chơi bắt đầu trò chơi chỉ với hai ô

bên phải khung thành. Nếu nó thực sự biết cách chơi trò chơi thì sẽ mất thời gian ngắn nhất

đường đi tới mục tiêu. Thay vào đó, nó bắt đầu di chuyển xuống bên trái, giống như trong

chế độ trò chơi tĩnh. Có vẻ như người mẫu vừa ghi nhớ bảng cụ thể đó

được đào tạo và không khái quát chút nào. Có lẽ chúng ta chỉ cần huấn luyện nó bằng trò chơi

chế độ được đặt thành ngẫu nhiên và sau đó nó sẽ thực sự học. Hãy thử nó. Đào tạo lại nó với chế độ ngẫu nhiên.

Có thể bạn sẽ may mắn hơn chúng tôi, nhưng hình 3.11 thể hiện biểu đồ thua của chúng tôi ở chế độ ngẫu nhiên

và 1000 kỷ nguyên. Điều đó trông không đẹp chút nào. Không có dấu hiệu nào cho thấy việc học tập quan trọng

đang xảy ra với chế độ ngẫu nhiên. Chúng tôi sẽ không hiển thị những kết quả này, nhưng mô hình dường như

tìm hiểu cách chơi với chế độ người chơi, trong đó chỉ người chơi được đặt ngẫu nhiên trên lưới.

Hình 3.11, đồ thị mất mát cho quá trình học Q ở chế độ ngẫu nhiên, không có dấu hiệu nào

của sự hội tụ. Đây là một vấn đề lớn. Học tăng cường sẽ không có giá trị gì nếu tất cả chỉ là vậy

có thể làm là học cách ghi nhớ hoặc học hàng tuần. Nhưng đây là một vấn đề mà sâu

đội tâm trí đã đối mặt và giành chiến thắng, họ đã giải quyết được.