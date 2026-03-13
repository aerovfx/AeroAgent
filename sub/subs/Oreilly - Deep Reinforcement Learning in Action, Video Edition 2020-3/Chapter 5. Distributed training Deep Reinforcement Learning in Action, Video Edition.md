# Chương 5. Đào tạo phân tán Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Phần 5.2, Đào tạo phân tán.

Như chúng tôi đã đề cập trong phần giới thiệu, mục tiêu của chúng tôi trong chương này là triển khai một mô hình

được gọi là Nhà phê bình diễn viên lợi thế phân tán, DA2C và chúng ta đã thảo luận về Diễn viên lợi thế

Phần phê phán của tên ở cấp độ khái niệm.

Bây giờ chúng ta hãy làm tương tự cho phần Distributed.

Đối với hầu hết tất cả các mô hình deep learning, chúng tôi thực hiện đào tạo hàng loạt, trong đó một tập hợp con ngẫu nhiên của

dữ liệu đào tạo của chúng tôi được gộp lại với nhau và chúng tôi tính toán tổn thất cho toàn bộ lô này

trước khi chúng tôi truyền bá trở lại và thực hiện giảm độ dốc.

Điều này là cần thiết vì độ dốc, nếu chúng ta huấn luyện với các phần dữ liệu đơn lẻ tại một

thời gian, sẽ có quá nhiều phương sai và các tham số sẽ không bao giờ hội tụ về mức tối ưu của chúng.

các giá trị.

Chúng ta cần tính trung bình nhiễu trong một loạt dữ liệu để có được tín hiệu thực trước khi cập nhật

các tham số mô hình.

Ví dụ: nếu bạn đang huấn luyện một bộ phân loại hình ảnh để nhận dạng các chữ số vẽ tay và bạn

huấn luyện nó với một hình ảnh tại một thời điểm, thuật toán sẽ nghĩ rằng các pixel nền chỉ là

quan trọng như các chữ số ở phía trước.

Nó chỉ có thể nhìn thấy tín hiệu khi được tính trung bình cùng với các hình ảnh khác.

Khái niệm tương tự được áp dụng trong học tăng cường, đó là lý do tại sao chúng tôi phải sử dụng một

trải nghiệm bộ đệm phát lại với DQN.

Việc đào tạo bộ đệm phát lại đủ lớn đòi hỏi nhiều bộ nhớ và trong một số trường hợp,

bộ đệm phát lại là không thực tế.

Có thể sử dụng bộ đệm phát lại khi môi trường học tập tăng cường và thuật toán tác nhân của bạn tuân theo

các tiêu chí nghiêm ngặt của quá trình ra quyết định Markov và đặc biệt là thuộc tính Markov.

Nhớ lại thuộc tính Markov nói rằng hành động tối ưu cho trạng thái ST có thể được tính toán mà không cần

tham chiếu đến ST trừ 1 của bất kỳ trạng thái trước đó.

Không cần phải lưu giữ lịch sử của các trạng thái đã truy cập trước đó.

Đối với các trò chơi đơn giản thì điều này là đúng, nhưng đối với các môi trường phức tạp hơn, điều này có thể cần thiết.

nhớ lại quá khứ để lựa chọn phương án tốt nhất hiện tại.

Thực tế, trong nhiều trò chơi phức tạp, người ta thường sử dụng các mạng thần kinh hồi quy, RNN, như

bộ nhớ ngắn hạn dài, LSTM, mạng hoặc đơn vị tái phát có kiểm soát, GRU.

Các RNN này có thể giữ trạng thái bên trong có thể lưu trữ dấu vết của quá khứ, hình 5.7.

Chúng đặc biệt hữu ích cho việc xử lý ngôn ngữ tự nhiên, NLP.

Các nhiệm vụ trong đó việc theo dõi các từ hoặc ký tự trước đó là rất quan trọng để có thể

mã hóa hoặc giải mã một câu.

Tính năng phát lại trải nghiệm không hoạt động với RNN trừ khi bộ đệm phát lại lưu trữ toàn bộ quỹ đạo

hoặc các tập đầy đủ vì RNN được thiết kế để xử lý dữ liệu tuần tự.

Hình 5.7 Mạng nơ ron tái phát chung, RNN,

Lớp xử lý một chuỗi dữ liệu bằng cách kết hợp đầu ra trước đó với đầu vào mới.

Đầu vào bên trái, cùng với đầu ra trước đó được đưa vào mô-đun RN, sau đó

tạo ra một đầu ra.

Đầu ra được đưa trở lại RNN ở bước thời gian tiếp theo và một bản sao có thể được đưa vào

một lớp khác.

RNN sẽ không hoạt động bình thường với các trải nghiệm đơn lẻ trong bộ đệm phát lại trải nghiệm vì

nó cần phải hoạt động dựa trên những chuỗi trải nghiệm.

Một cách để sử dụng RNN mà không cần phát lại trải nghiệm là chạy nhiều bản sao của tác nhân

song song, mỗi cái có sự thể hiện riêng biệt của môi trường.

Bằng cách phân phối nhiều tác nhân độc lập trên các tiến trình CPU khác nhau, hình 5.8,

chúng ta có thể thu thập một tập hợp trải nghiệm đa dạng và do đó có được một mẫu độ dốc

chúng ta có thể tính trung bình cùng nhau để có được độ dốc trung bình phương sai thấp hơn.

Điều này giúp loại bỏ nhu cầu phát lại trải nghiệm và cho phép chúng tôi huấn luyện thuật toán theo cách hoàn toàn

thời trang trực tuyến, chỉ ghé thăm mỗi tiểu bang một lần khi nó xuất hiện trong môi trường.

Hình 5.8 Hình thức đào tạo deep learning phổ biến nhất

mô hình là đưa một loạt dữ liệu vào mô hình để trả về một loạt dự đoán.

Khi chúng tôi tính toán tổn thất cho mỗi dự đoán và tính trung bình hoặc tính tổng tất cả các tổn thất trước đó

lan truyền ngược và cập nhật các tham số mô hình, điều này tính trung bình sự biến thiên hiện diện trên

tất cả những trải nghiệm.

Ngoài ra, chúng ta có thể chạy nhiều mô hình với mỗi mô hình lấy một trải nghiệm duy nhất và thực hiện

một dự đoán duy nhất, truyền ngược qua từng mô hình để có được độ dốc và sau đó một số

được tính trung bình các gradient trước khi thực hiện bất kỳ cập nhật tham số nào.

Đa xử lý và đa luồng Máy tính để bàn và máy tính xách tay hiện đại có

đơn vị xử lý trung tâm, CPU, có nhiều lõi, là các đơn vị xử lý độc lập

có khả năng thực hiện các tính toán đồng thời.

Do đó, nếu bạn có thể chia một phép tính thành các phần có thể được tính riêng

và kết hợp sau đó, bạn có thể tăng tốc độ đáng kể.

Phần mềm hệ điều hành trừu tượng hóa bộ xử lý CPU vật lý thành các tiến trình ảo

và chủ đề.

Một tiến trình chứa không gian bộ nhớ riêng của nó và các luồng chạy trong một tiến trình duy nhất.

Có hai dạng tính toán song song, đa luồng và đa xử lý, và chỉ

ở dạng sau là các phép tính được thực hiện thực sự đồng thời.

Trong đa xử lý, các tính toán được thực hiện đồng thời trên nhiều vật lý khác nhau

các đơn vị xử lý, chẳng hạn như lõi CPU hoặc GPU.

Xem hình này.

Các tiến trình là sự trừu tượng hóa của phần cứng CPU cơ bản do hệ điều hành tạo ra.

Nếu bạn có hai CPU, bạn có thể chạy hai tiến trình đồng thời.

Tuy nhiên, hệ điều hành sẽ cho phép bạn tạo ra nhiều hơn hai tiến trình ảo và nó

sẽ tìm ra cách thực hiện đa nhiệm giữa chúng.

Mỗi tiến trình có không gian địa chỉ bộ nhớ riêng và có thể có nhiều luồng, tác vụ.

Trong khi một luồng đang chờ một tiến trình bên ngoài kết thúc, chẳng hạn như đầu vào, đầu ra

hoạt động, hệ điều hành có thể cho phép một luồng khác chạy.

Điều này tối đa hóa việc sử dụng bất kỳ CPU nào bạn có.

Đa luồng cũng giống như khi mọi người thực hiện đa nhiệm.

Họ chỉ có thể làm một việc tại một thời điểm, nhưng họ chuyển đổi giữa các nhiệm vụ khác nhau trong khi

một nhiệm vụ khác đang nhàn rỗi.

Do đó, các tác vụ không thực sự được thực hiện đồng thời với đa luồng.

Đây là một cơ chế cấp phần mềm để nâng cao hiệu quả khi chạy nhiều phép tính.

Đa luồng thực sự hiệu quả khi tác vụ của bạn yêu cầu nhiều đầu vào gạch chéo đầu ra

các hoạt động như đọc và ghi dữ liệu vào đĩa cứng.

Khi dữ liệu đang được đọc vào RAM từ đĩa cứng, việc tính toán trên CPU sẽ không hoạt động, vì

nó chờ dữ liệu cần thiết và hệ điều hành có thể sử dụng thời gian CPU nhàn rỗi đó để hoạt động

đang thực hiện một tác vụ khác, sau đó chuyển trở lại khi thao tác IO hoàn tất.

Các mô hình học máy thường không yêu cầu thao tác IO.

Học máy bị giới hạn bởi tốc độ tính toán, do đó nó được hưởng lợi từ tính đồng thời thực sự

tính toán đa xử lý.

Tất cả các mô hình học máy lớn đều yêu cầu bộ xử lý đồ họa, GPU để thực hiện

hiệu quả, nhưng các mô hình phân tán trên nhiều CPU có thể mang tính cạnh tranh trong một số trường hợp.

Python cung cấp một thư viện gọi là đa xử lý giúp việc đa xử lý trở nên rất dễ dàng.

Ngoài ra, PyTorch bao bọc thư viện này và có phương pháp cho phép các tham số mô hình

được chia sẻ trên nhiều tiến trình.

Hãy xem một ví dụ đơn giản về đa xử lý.

Như một ví dụ đơn giản, giả sử chúng ta có một mảng với các số 0, 1, 2, 3,

đến 64, và chúng ta muốn bình phương mỗi số.

Vì bình phương một số không phụ thuộc vào bất kỳ số nào khác trong mảng nên chúng ta có thể dễ dàng

song song điều này trên nhiều bộ xử lý.

Liệt kê 5.1, Giới thiệu về Đa xử lý.

Ở đây chúng ta định nghĩa một hàm, bình phương, nhận vào một mảng và bình phương nó.

Đây là chức năng sẽ được phân phối trên nhiều quy trình.

Chúng tôi tạo một số dữ liệu mẫu đơn giản là danh sách các số từ 0 đến 63 và đúng hơn là

hơn là bình phương chúng một cách tuần tự trong một quá trình duy nhất.

Chúng ta chia mảng thành 8 phần và tính bình phương cho mỗi phần một cách độc lập trên

một bộ xử lý khác, Hình 5.9.

Hình 5.9, một ví dụ đa xử lý đơn giản.

Chúng tôi muốn bình phương tất cả các số trong một mảng một cách hiệu quả hơn.

Thay vì bình phương mỗi phần tử 1 x 1, chúng ta có thể chia mảng thành 2 phần và gửi

mỗi mảnh tới một bộ xử lý khác nhau sẽ bình phương chúng đồng thời.

Sau đó chúng ta có thể kết hợp lại các phần thành một mảng duy nhất.

Bạn có thể xem máy tính của mình có bao nhiêu bộ xử lý phần cứng bằng cách sử dụng dấu gạch dưới mp.cpu

chức năng đếm.

Bạn có thể thấy trong danh sách 5.1 chúng ta có 8.

Nhiều máy tính hiện đại có thể có 4 bộ xử lý phần cứng độc lập, nhưng chúng sẽ có hai

nhiều bộ xử lý ảo thông qua cái gọi là siêu phân luồng.

Siêu phân luồng là một thủ thuật hiệu suất mà một số bộ xử lý sử dụng có thể cho phép 2 tiến trình chạy

về cơ bản đồng thời trên một bộ xử lý vật lý.

Điều quan trọng là không tạo ra nhiều tiến trình hơn số lượng CPU có trên máy của bạn, vì

các tiến trình bổ sung về cơ bản sẽ hoạt động như các luồng và CPU sẽ phải nhanh chóng

chuyển đổi giữa các tiến trình.

Trong danh sách 5.1, chúng tôi thiết lập một nhóm bộ xử lý gồm 8 quy trình với mp.pool8, sau đó chúng tôi

đã sử dụng pool.map để phân phối hàm bình phương trên 8 phần dữ liệu.

Bạn có thể thấy chúng tôi nhận được danh sách 8 mảng với tất cả các phần tử của chúng bình phương, đúng như chúng tôi muốn.

Các quy trình sẽ quay trở lại ngay sau khi chúng hoàn tất, vì vậy thứ tự của các phần tử trong

danh sách trả về có thể không phải lúc nào cũng theo thứ tự chúng được ánh xạ.

Chúng tôi sẽ cần kiểm soát nhiều hơn một chút đối với các quy trình của mình so với mức mà nhóm bộ xử lý cho phép,

vì vậy chúng tôi sẽ tạo và bắt đầu một loạt quy trình theo cách thủ công.

Liệt kê 5.2, khởi động thủ công các tiến trình riêng lẻ.

Đây là nhiều mã hơn, nhưng về mặt chức năng, nó giống như những gì chúng tôi đã làm trước đây với nhóm.

Tuy nhiên, giờ đây thật dễ dàng chia sẻ dữ liệu giữa các quy trình bằng cách sử dụng các cấu trúc dữ liệu có thể chia sẻ đặc biệt

trong thư viện đa xử lý và chúng tôi có nhiều quyền kiểm soát hơn đối với các quy trình.

Chúng tôi đã sửa đổi hàm bình phương một chút để chấp nhận một số nguyên biểu thị quá trình

ID, mảng thành hình vuông và cấu trúc dữ liệu chung dùng chung được gọi là hàng đợi mà chúng ta có thể

đưa dữ liệu vào và trích xuất dữ liệu bằng phương thức .get.

Để chạy qua mã, trước tiên chúng tôi thiết lập một danh sách để chứa các phiên bản của quy trình của chúng tôi.

Chúng tôi đã tạo đối tượng hàng đợi được chia sẻ và chúng tôi đã tạo dữ liệu mẫu như trước đây.

Sau đó, chúng tôi xác định một vòng lặp để tạo, trong trường hợp của chúng tôi, tám quy trình và bắt đầu chúng bằng cách sử dụng

phương pháp bắt đầu.

Chúng tôi thêm chúng vào danh sách quy trình của mình để có thể truy cập chúng sau này.

Tiếp theo, chúng tôi chạy qua danh sách quy trình và gọi từng quy trình, phương thức tham gia.

Điều này cho phép chúng tôi chờ đợi để trả lại bất cứ thứ gì cho đến khi tất cả các quá trình kết thúc.

Khi chúng tôi gọi mỗi phương thức chấm dứt quy trình để đảm bảo nó bị hủy.

Cuối cùng, chúng tôi thu thập tất cả các thành phần của hàng đợi vào một danh sách và in ra.

Các kết quả trông giống như với nhóm quy trình, ngoại trừ chúng được sắp xếp theo thứ tự ngẫu nhiên.

Đó thực sự là tất cả những gì cần làm để phân phối một chức năng trên nhiều bộ xử lý CPU.