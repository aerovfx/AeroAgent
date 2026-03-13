# Chương 7. Xem lại xác suất và số liệu thống kê Học tăng cường sâu trong thực tế, Phiên bản video đã dịch

---

Phần 7.2, Xem lại Xác suất và Thống kê.

Trong khi cơ sở toán học đằng sau lý thuyết xác suất là nhất quán và không gây tranh cãi, thì

giải thích ý nghĩa của việc nói điều gì đó tầm thường như xác suất của một hội chợ

đồng xu lật mặt là 0,5, thực sự có phần gây tranh cãi.

Hai phe chính được gọi là Người thường xuyên và Bations.

Một người thường xuyên nói rằng xác suất để một đồng xu ngửa là bất kỳ tỷ lệ nào

mặt ngửa được quan sát thấy nếu người ta có thể tung đồng xu vô số lần.

Một chuỗi tung đồng xu ngắn có thể mang lại tỷ lệ mặt ngửa cao tới 0,8, nhưng cũng như

bạn tiếp tục lật, nó sẽ có xu hướng tiến tới chính xác 0,5 trong giới hạn vô hạn.

Do đó, xác suất chỉ là tần số của các sự kiện.

Trong trường hợp này, có hai kết quả có thể xảy ra, mặt ngửa hoặc mặt ngửa, và xác suất của mỗi kết quả

là tần số của nó sau vô số lần thử, tung đồng xu.

Tất nhiên đây là lý do tại sao xác suất là các giá trị nằm trong khoảng từ 0, không thể và 1, chắc chắn và

xác suất của tất cả các kết quả có thể xảy ra phải có tổng bằng 1.

Đây là một cách tiếp cận đơn giản và dễ hiểu đối với xác suất, nhưng nó có những hạn chế đáng kể.

Trong bối cảnh Người theo chủ nghĩa thường xuyên, rất khó hoặc có lẽ không thể hiểu được một câu hỏi

như, xác suất để Jane Doe được bầu vào Hội đồng Thành phố là bao nhiêu?

Vì trên thực tế và lý thuyết, một cuộc bầu cử như vậy không thể diễn ra vô hạn.

nhiều lần, xác suất thường xuyên không có nhiều ý nghĩa đối với những loại

sự kiện một lần.

Chúng ta cần một khuôn khổ mạnh mẽ hơn để xử lý những tình huống này và đó là điều Bayesian

xác suất mang lại cho chúng ta.

Trong khuôn khổ Bayes, xác suất thể hiện mức độ tin tưởng về nhiều khả năng khác nhau có thể xảy ra.

kết quả.

Bạn chắc chắn có thể có niềm tin về điều gì đó chỉ có thể xảy ra một lần, như một cuộc bầu cử,

và niềm tin của bạn về những gì có thể xảy ra có thể khác nhau tùy thuộc vào lượng thông tin

bạn có thông tin về một tình huống cụ thể và thông tin mới sẽ khiến bạn phải cập nhật

niềm tin.

Bảng C 7.1

Khung toán học cơ bản cho xác suất bao gồm một không gian mẫu, Omega, là không gian

tập hợp tất cả các kết quả có thể xảy ra cho một câu hỏi cụ thể.

Ví dụ, trong trường hợp một cuộc bầu cử, không gian mẫu là tập hợp tất cả các ứng cử viên

đủ điều kiện để được bầu.

Có một hàm phân phối xác suất hoặc hàm đo lường.

P là hàm từ tập Omega đến khoảng 0, 1, trong đó P là hàm từ

không gian mẫu đến các số thực trong khoảng từ 0 đến 1.

Bạn có thể thay P, ứng cử viên A, và nó sẽ đưa ra một số từ 0 đến 1 biểu thị

xác suất ứng cử viên A thắng cử.

Ghi chú.

Lý thuyết xác suất phức tạp hơn những gì chúng tôi trình bày ở đây và liên quan đến

một nhánh của toán học gọi là lý thuyết độ đo.

Vì mục đích của mình, chúng ta không cần phải nghiên cứu sâu hơn về lý thuyết xác suất.

có.

Chúng ta sẽ tiếp tục phần giới thiệu không chính thức và không chặt chẽ về mặt toán học đối với xác suất

những khái niệm chúng ta cần.

Độ hỗ trợ của phân bố xác suất là một thuật ngữ khác mà chúng ta sẽ sử dụng.

Hỗ trợ chỉ là tập hợp con của các kết quả được ấn định xác suất khác 0.

Ví dụ: nhiệt độ không thể nhỏ hơn 0 Kelvin, do đó nhiệt độ âm sẽ

được gán xác suất 0.

Độ hỗ trợ của phân bố xác suất theo nhiệt độ sẽ từ 0 đến dương

vô cùng.

Vì chúng tôi thường không quan tâm đến những kết quả không thể xảy ra nên bạn sẽ thường thấy sự hỗ trợ

và không gian mẫu được sử dụng thay thế cho nhau, mặc dù chúng có thể không giống nhau.

Mục 7.2.1, trước và sau.

Nếu chúng tôi hỏi bạn, xác suất mỗi ứng cử viên sẽ giành chiến thắng trong cuộc đua bốn bên là bao nhiêu?

mà không chỉ rõ ứng cử viên là ai hoặc cuộc bầu cử diễn ra như thế nào, bạn có thể

từ chối trả lời với lý do không đủ thông tin.

Nếu chúng tôi thực sự ép bạn, bạn có thể nói như vậy vì bạn không biết gì khác nên mỗi ứng viên đều

có 1/4 cơ hội chiến thắng.

Với câu trả lời đó, bạn đã thiết lập được phân bố xác suất trước đó đồng nhất.

Mỗi kết quả có thể xảy ra đều có xác suất như nhau đối với các ứng cử viên.

Trong khuôn khổ Bayes, xác suất đại diện cho niềm tin và niềm tin luôn mang tính thăm dò

trong những tình huống khi thông tin mới có thể có sẵn.

Vì vậy, phân phối xác suất trước chỉ là phân phối bạn bắt đầu trước khi nhận

một số thông tin mới.

Sau khi bạn nhận được thông tin mới, chẳng hạn như một số thông tin tiểu sử về ứng viên,

bạn có thể cập nhật bản phân phối trước đó của mình dựa trên thông tin mới đó.

Phân phối cập nhật này bây giờ được gọi là phân phối xác suất sau của bạn.

Sự khác biệt giữa phân phối trước và phân phối sau là theo ngữ cảnh, vì phân phối sau của bạn

phân phối sẽ trở thành phân phối trước mới ngay trước khi bạn nhận được một bộ phân phối mới khác

thông tin.

Niềm tin của bạn được cập nhật liên tục dưới dạng sự nối tiếp của các lần phân phối trước tới các lần phân phối sau,

Hình 7.5, và quá trình này được gọi chung là suy luận Bayes.

Hình 7.5 Suy luận Bayes là quá trình bắt đầu với phân phối trước, nhận

một số thông tin mới và sử dụng thông tin đó để cập nhật thông tin trước đó thành một bản phân phối mới, đầy đủ thông tin hơn

gọi là phân phối sau.

Phần 7.2.2 Kỳ vọng và Phương sai

Có một số câu hỏi chúng ta có thể hỏi về phân bố xác suất.

Chúng ta có thể hỏi kết quả có khả năng xảy ra nhất là gì mà chúng ta thường coi là kết quả trung bình

hoặc trung bình của phân phối.

Có thể bạn đã quen với cách tính giá trị trung bình bằng cách lấy tổng của tất cả các giá trị

kết quả và chia cho số kết quả.

Ví dụ: giá trị trung bình của dự báo nhiệt độ trong 5 ngày là 18211721 độ C là 18

cộng 21 cộng 17 cộng 21 chia 5 bằng 94 chia 5 bằng 18,8 độ C.

Đây là nhiệt độ dự đoán trung bình trong một mẫu 5 ngày ở Chicago, Illinois,

Hoa Kỳ.

Thay vào đó, hãy xem xét nếu chúng ta yêu cầu 5 người đưa ra dự đoán về nhiệt độ ngày mai

ở Chicago, và họ tình cờ cho chúng ta những con số giống nhau, 18, 21, 17, 17, 21 độ

độ C.

Nếu chúng ta muốn nhiệt độ trung bình cho ngày mai, chúng ta sẽ làm theo quy trình tương tự, thêm

các số tăng lên và chia cho số lượng mẫu, 5, để có được giá trị trung bình dự đoán

nhiệt độ cho ngày mai.

Nhưng điều gì sẽ xảy ra nếu người 1 là một nhà khí tượng học và chúng ta tin tưởng hơn rất nhiều vào dự đoán của họ

so với 4 người còn lại mà chúng tôi ngẫu nhiên kéo được trên đường?

Có lẽ chúng ta sẽ muốn chờ dự đoán của nhà khí tượng học cao hơn những người khác.

Giả sử chúng ta nghĩ rằng dự đoán của họ có 60% khả năng là đúng và 4 dự đoán còn lại là

chỉ có 10% có khả năng là sự thật.

Chú ý 0,6 cộng 4 nhân 0,10 bằng 1,0.

Đây là mức trung bình có trọng số.

Nó được tính bằng cách nhân từng mẫu với trọng lượng của nó.

Trong trường hợp này, điều đó diễn ra như sau.

0,6 nhân 18 cộng 0,1 nhân 21 cộng 17 cộng 17 cộng 21 bằng 18,4 độ C.

Mỗi nhiệt độ là một kết quả có thể xảy ra vào ngày mai, nhưng không phải tất cả các kết quả đều như nhau

có thể xảy ra trong trường hợp này, vì vậy chúng tôi nhân từng kết quả có thể xảy ra với xác suất, trọng số và

sau đó một số.

Nếu tất cả các trọng số bằng nhau và có tổng bằng 1, chúng ta sẽ có được phép tính trung bình thông thường, nhưng nhiều

nhiều lúc thì không.

Khi các trọng số không giống nhau, chúng ta nhận được giá trị trung bình có trọng số gọi là kỳ vọng

giá trị của một phân phối.

Giá trị kỳ vọng của phân bố xác suất là khối tâm của nó, giá trị

rất có thể là trung bình.

Cho một phân bố xác suất, p của x, trong đó x là không gian mẫu, giá trị kỳ vọng

đối với phân bố rời rạc được tính như sau.

Bảng 7.2 Tính giá trị kỳ vọng từ phân bố xác suất, xem bảng số liệu.

Toán tử giá trị mong đợi, trong đó toán tử là một thuật ngữ khác của hàm, được biểu thị

e, và đó là hàm nhận phân phối xác suất và trả về giá trị mong đợi của nó.

Nó hoạt động bằng cách lấy một giá trị x, nhân với xác suất liên quan của nó, p của x, và

tính tổng tất cả các giá trị có thể có của x.

Trong Python, nếu p của x được biểu diễn dưới dạng một mảng xác suất, xác suất và một mảng khác

mảng kết quả phức tạp, không gian mẫu, giá trị mong đợi là.

Xem mã này.

Ngoài ra, giá trị mong đợi có thể được tính dưới dạng tích số chấm bên trong giữa các thăm dò

mảng và mảng kết quả, vì sản phẩm bên trong thực hiện điều tương tự.

Nó nhân từng phần tử tương ứng trong hai mảng và tính tổng tất cả.

Xem mã này.

Phân bố xác suất rời rạc có nghĩa là không gian mẫu của nó là một tập hữu hạn, hoặc trong

nói cách khác, chỉ có một số hữu hạn các kết quả có thể xảy ra.

Ví dụ, việc tung đồng xu chỉ có thể có một trong hai kết quả.

Tuy nhiên, nhiệt độ ngày mai có thể là bất kỳ số thực nào hoặc nếu đo bằng Kelvin,

nó có thể là bất kỳ số thực nào từ 0 đến vô cùng.

Và các số thực, hay bất kỳ tập con nào của số thực, đều là vô hạn, vì chúng ta có thể liên tục

chia chúng.

1,5 là một số thực và 1,500001 cũng vậy, v.v.

Khi không gian mẫu là vô hạn thì đây là phân bố xác suất liên tục.

Trong phân bố xác suất liên tục, phân bố không cho bạn biết xác suất

về một kết quả cụ thể, bởi vì với vô số kết quả có thể xảy ra, mỗi cá nhân

kết quả phải có xác suất vô cùng nhỏ để tổng bằng một.

Do đó, phân bố xác suất liên tục cho bạn biết mật độ xác suất xung quanh một điểm cụ thể

kết quả có thể xảy ra.

Mật độ xác suất là tổng các xác suất xung quanh một khoảng nhỏ của một giá trị nào đó.

Đó là xác suất mà kết quả sẽ rơi vào một khoảng thời gian nhỏ nào đó.

Sự khác biệt giữa phân phối rời rạc và liên tục được mô tả trong hình 7.6.

Đó là tất cả những gì chúng ta sẽ nói về phân phối liên tục bây giờ, bởi vì trong cuốn sách này chúng ta sẽ thực sự

chỉ xử lý phân bố xác suất rời rạc.

Hình 7.6.

Bên trái.

Một phân phối rời rạc giống như một mảng xác suất phức tạp được liên kết với một mảng xác suất phức tạp khác.

mảng các giá trị kết quả.

Có một tập hợp hữu hạn các xác suất và kết quả.

Phải.

Phân phối liên tục biểu thị vô số kết quả có thể xảy ra và trục y

là mật độ xác suất, là xác suất mà kết quả nhận một giá trị trong phạm vi

một khoảng nhỏ.

Một câu hỏi khác mà chúng ta có thể đặt ra về phân bố xác suất là độ chênh lệch hoặc phương sai của nó.

Niềm tin của chúng ta về điều gì đó có thể chắc chắn ít nhiều, vì vậy phân bố xác suất

có thể hẹp hoặc rộng tương ứng.

Việc tính toán phương sai sử dụng toán tử kỳ vọng và được định nghĩa như sau, nhưng không

lo lắng về việc ghi nhớ phương trình này.

Chúng tôi sẽ sử dụng các hàm numpy tích hợp để tính toán phương sai.

phương sai được ký hiệu là var của x hoặc sigma bình phương, trong đó căn bậc hai của sigma bình phương

bằng sigma là độ lệch chuẩn, do đó phương sai là bình phương độ lệch chuẩn.

Mu trong phương trình này là ký hiệu chuẩn cho giá trị trung bình, cũng là nơi mu bằng

tới giá trị kỳ vọng của x, trong đó x là biến ngẫu nhiên cần quan tâm.

Biến ngẫu nhiên chỉ là một cách khác để sử dụng phân phối xác suất.

Biến ngẫu nhiên gắn liền với phân bố xác suất và phân bố xác suất

có thể mang lại các biến ngẫu nhiên.

Chúng ta có thể tạo một biến ngẫu nhiên t cho nhiệt độ ngày mai.

Nó là một biến ngẫu nhiên vì nó là một giá trị không xác định, nhưng nó chỉ có thể nhận các giá trị cụ thể

hợp lệ đối với phân bố xác suất cơ bản của nó.

Chúng ta có thể sử dụng các biến ngẫu nhiên ở bất kỳ nơi nào có thể sử dụng biến xác định thông thường, nhưng

nếu chúng ta thêm một biến ngẫu nhiên với một biến xác định, chúng ta sẽ nhận được một biến ngẫu nhiên mới.

Ví dụ: nếu chúng ta nghĩ nhiệt độ ngày mai sẽ bằng nhiệt độ hôm nay cộng thêm

một số nhiễu ngẫu nhiên, chúng ta có thể mô hình hóa nó thành t bằng t0 cộng e, trong đó e là biến ngẫu nhiên

của tiếng ồn.

Nhiễu có thể có phân bố chuẩn, Gaussian, tập trung quanh 0 với phương sai là

1.

Do đó, t sẽ là phân phối chuẩn mới với giá trị trung bình t0, nhiệt độ ngày hôm nay, nhưng nó sẽ

vẫn có phương sai là 1.

Phân phối chuẩn là đường cong hình chuông quen thuộc.

Bảng 7.3 cho thấy một số phân bố phổ biến.

Phân phối chuẩn trở nên rộng hơn hoặc hẹp hơn tùy thuộc vào tham số phương sai, nhưng mặt khác

nó trông giống nhau đối với bất kỳ tập hợp tham số nào.

Ngược lại, bản phân phối beta và gamma có thể trông khá khác nhau tùy thuộc vào

các thông số.

Hai phiên bản khác nhau của mỗi phiên bản này được hiển thị.

Bảng 7.3, phân bố xác suất chung, xem bảng hình.

Các biến ngẫu nhiên thường được ký hiệu bằng chữ in hoa như x.

Trong Python, chúng ta có thể thiết lập một biến ngẫu nhiên bằng mô-đun ngẫu nhiên của numpy.

Xem mã này.

Ở đây chúng tôi đã tạo một hàm ẩn danh không chấp nhận đối số và chỉ thêm một số ngẫu nhiên nhỏ

số thành 18,4 mỗi lần nó được gọi.

Phương sai của t là 1, có nghĩa là hầu hết các giá trị mà t trả về sẽ nằm trong

một độ 18,4.

Nếu phương sai là 10 thì sự chênh lệch nhiệt độ có thể sẽ lớn hơn.

Nói chung, chúng tôi bắt đầu với phân phối trước có phương sai cao và khi chúng tôi nhận được nhiều hơn

thông tin, sự khác biệt giảm đi.

Tuy nhiên, thông tin mới có thể làm tăng sự khác biệt của phần sau

nếu thông tin chúng tôi nhận được rất bất ngờ và khiến chúng tôi kém chắc chắn hơn.