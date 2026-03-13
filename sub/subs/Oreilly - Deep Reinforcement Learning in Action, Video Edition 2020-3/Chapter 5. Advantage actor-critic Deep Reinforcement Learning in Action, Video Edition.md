# Chương 5. Học tập tăng cường sâu trong hành động của diễn viên-nhà phê bình có lợi thế, Phiên bản video được dịch

---

Mục 5.3, Nhà phê bình diễn viên có lợi thế

Bây giờ chúng ta đã biết cách phân phối tính toán giữa các quy trình, chúng ta có thể quay lại quá trình học tăng cường thực sự.

Trong phần này, chúng ta sẽ tập hợp các phần của mô hình Advantage Actor Critic được phân phối đầy đủ lại với nhau.

Để cho phép đào tạo nhanh và so sánh kết quả với chương trước, chúng tôi sẽ lại sử dụng trò chơi Cart Pull làm môi trường thử nghiệm.

Tuy nhiên, nếu chọn, bạn có thể dễ dàng điều chỉnh thuật toán cho phù hợp với một trò chơi khó hơn như Pong và OpenAI Gym.

Bạn có thể tìm thấy cách triển khai như vậy trên trang GitHub của chương này tại liên kết này.

Cho đến nay, chúng tôi đã trình bày Diễn viên và Nhà phê bình dưới dạng hai hàm riêng biệt, nhưng chúng tôi có thể kết hợp chúng thành một mạng nơ-ron duy nhất có hai đầu ra.

Đó là những gì chúng ta sẽ làm trong đoạn mã sau.

Thay vì mạng nơ-ron thông thường trả về một vectơ duy nhất, nó có thể trả về hai vectơ khác nhau, một cho chính sách và một cho giá trị.

Điều này cho phép chia sẻ một số tham số giữa chính sách và giá trị, điều này có thể giúp mọi việc hiệu quả hơn vì một số thông tin cần thiết để tính toán các giá trị cũng hữu ích trong việc dự đoán hành động tốt nhất cho chính sách.

Nhưng nếu hiện tại, mạng nơ-ron hai đầu có vẻ quá xa lạ, bạn có thể tiếp tục và viết hai mạng nơ-ron riêng biệt.

Nó sẽ hoạt động tốt.

Hãy xem một số mã giả cho thuật toán, sau đó chúng ta sẽ dịch nó sang Python.

Liệt kê 5.3, mã giả dành cho nhà phê bình tác nhân có lợi trực tuyến.

Đây là mã giả rất đơn giản nhưng nó thể hiện được ý chính.

Phần quan trọng cần chỉ ra là tính toán lợi thế.

Hãy xem xét trường hợp chúng ta thực hiện một hành động. Chúng tôi nhận được phần thưởng cộng 10. Dự đoán giá trị là cộng 5 và dự đoán giá trị cho trạng thái tiếp theo là cộng 7.

Vì các dự đoán trong tương lai luôn ít giá trị hơn phần thưởng được quan sát hiện tại nên chúng tôi chiết khấu giá trị của trạng thái tiếp theo theo hệ số chiết khấu gamma.

Lợi thế của chúng ta bằng 10 cộng 0,9 lần 7 trừ 5 bằng 10 cộng 6,3 trừ 5 bằng 10 cộng 1,3 bằng cộng 11,3.

Vì chênh lệch giữa giá trị trạng thái tiếp theo và giá trị trạng thái hiện tại là dương nên nó làm tăng giá trị tổng thể của hành động mà chúng ta vừa thực hiện, vì vậy chúng ta sẽ củng cố nó nhiều hơn.

Lưu ý rằng hàm lợi thế bootstraps vì nó tính toán giá trị cho trạng thái hiện tại và hành động dựa trên các dự đoán cho trạng thái trong tương lai.

Trong chương này, chúng ta sẽ sử dụng lại mô hình DA2C trong thăm dò giỏ hàng, mô hình này được thực hiện theo từng giai đoạn.

Vì vậy, nếu chúng tôi thực hiện cập nhật Monte Carlo đầy đủ, tức là chúng tôi cập nhật sau khi toàn bộ tập phim hoàn tất, giá trị gạch dưới tiếp theo sẽ luôn là 0 cho bước cuối cùng vì không có trạng thái tiếp theo khi tập phim kết thúc.

Trong trường hợp này, số hạng lợi thế thực sự rút gọn thành lợi thế bằng giá trị phần thưởng trừ đi, là giá trị cơ sở mà chúng ta đã thảo luận ở đầu chương.

Biểu thức lợi thế đầy đủ, A bằng R sub T cộng 1 cộng gamma nhân V của S sub T cộng 1 trừ V của S sub T, được sử dụng khi chúng ta học trực tuyến hoặc N bước học.

Xem hình này.

Học bước N là sự kết hợp giữa học trực tuyến hoàn toàn và chờ đợi một tập đầy đủ trước khi cập nhật, tức là Monte Carlo.

Như tên cho thấy, chúng tôi tích lũy phần thưởng qua N bước, sau đó tính toán tổn thất và lan truyền ngược.

Số bước có thể thay đổi từ một, điều này làm giảm việc học hoàn toàn trực tuyến, đến số bước tối đa trong tập, đó là Monte Carlo.

Thông thường chúng ta chọn cái gì đó ở giữa để có được lợi thế của cả hai.

Trước tiên, chúng tôi sẽ hiển thị thuật toán phê bình diễn viên theo từng tập và sau đó chúng tôi sẽ điều chỉnh nó theo N bước với N được đặt thành 10.

Hình 5.10 cho thấy tổng quan chung về thuật toán phê bình tác nhân.

Một mô hình phê bình tác nhân cần tạo ra cả giá trị trạng thái và xác suất hành động.

Chúng tôi sử dụng xác suất hành động để chọn một hành động và nhận phần thưởng, chúng tôi so sánh phần thưởng này với giá trị trạng thái để tính toán lợi thế.

Ưu điểm cuối cùng là những gì chúng tôi sử dụng để củng cố hành động và huấn luyện mô hình.

Hình 5.10, một mô hình phê bình tác nhân tạo ra giá trị trạng thái và xác suất hành động, được sử dụng để tính toán giá trị lợi thế và đây là đại lượng được sử dụng để huấn luyện mô hình thay vì phần thưởng thô như chỉ với việc học Q.

Với ý nghĩ đó, chúng ta hãy bắt đầu mã hóa mô hình phê bình diễn viên để đóng vai Cartpole. Đây là trình tự các bước.

1. Thiết lập mô hình nhà phê bình diễn viên của chúng tôi, mô hình hai đầu hoặc bạn có thể thiết lập hai mạng lưới nhà phê bình và diễn viên độc lập.

Mô hình chấp nhận trạng thái Cartpole làm đầu vào, là một vectơ gồm bốn số thực.

Đầu tác nhân cũng giống như mạng chính sách, tác nhân, ở chương trước, do đó, nó tạo ra một vectơ hai chiều biểu thị phân bố xác suất rời rạc trên hai hành động có thể xảy ra.

Nhà phê bình đưa ra một số duy nhất đại diện cho giá trị trạng thái.

Nhà phê bình được ký hiệu là V của S và tác nhân được ký hiệu là pi của S. Hãy nhớ rằng pi của S trả về log xác suất cho mỗi hành động có thể xảy ra, trong trường hợp của chúng ta là hai hành động.

2. Khi chúng ta đang xem tập hiện tại, a. Xác định siêu tham số, gamma, hệ số chiết khấu, b. Bắt đầu một tập mới ở trạng thái ban đầu, st. Nhìn thấy.

Tính giá trị v của st và lưu nó vào danh sách.

D. Tính số pi của st, lưu vào danh sách, lấy mẫu và thực hiện hành động a.t. Nhận trạng thái mới st cộng 1 và phần thưởng r.t cộng 1. Lưu phần thưởng vào danh sách.

3. Tàu hỏa. A. Khởi tạo r bằng 0. Lặp lại các phần thưởng theo thứ tự ngược lại để tạo ra lợi nhuận. r bằng r.i cộng gamma nhân r. B. Giảm thiểu việc mất tác nhân.

Âm 1 lần gamma sub t lần số lượng. r trừ v của s t nhân pi của một s cho trước. Nhìn thấy. Giảm thiểu tổn thất chỉ trích. r trừ v bình phương.

4. Lặp lại cho tập mới.

Danh sách sau đây thực hiện các bước này trong Python.

Liệt kê 5.4. Mô hình phê bình diễn viên Cartpole.

Đối với Cartpole, chúng tôi có một mạng lưới thần kinh khá đơn giản, ngoài việc có hai đầu ra. Trong danh sách 5.4, trước tiên chúng ta chuẩn hóa đầu vào sao cho tất cả các giá trị trạng thái đều nằm trong cùng một phạm vi.

Sau đó, đầu vào chuẩn hóa được đưa qua hai lớp đầu tiên, là các lớp tuyến tính thông thường với các hàm kích hoạt ray-lew. Sau đó, chúng tôi chia mô hình thành hai đường dẫn.

Đường dẫn đầu tiên là đầu tác nhân lấy đầu ra của lớp 2 và áp dụng một lớp tuyến tính khác, sau đó là hàm softmax ghi nhật ký.

Nhật ký gạch dưới softmax tương đương về mặt logic với việc thực hiện logarit tự nhiên của softmax của dấu chấm lửng. Nhưng hàm kết hợp ổn định hơn về mặt số lượng, bởi vì nếu bạn tính toán hàm riêng biệt, bạn có thể nhận được xác suất tràn hoặc thiếu phần sau softmax.

Đường dẫn thứ hai là đầu phê bình, áp dụng một lớp tuyến tính và ray-lew cho đầu ra của lớp 2. Nhưng lưu ý rằng chúng ta gọi y.detach, nó tách nút y ra khỏi biểu đồ để tổn thất phê phán sẽ không lan truyền trở lại và sửa đổi các trọng số trong lớp 1 và 2, hình 5.11.

Chỉ tác nhân mới có thể khiến các trọng số này được sửa đổi. Điều này ngăn chặn xung đột giữa những gì tác nhân và nhà phê bình muốn khi tác nhân và nhà phê bình đang cố gắng thực hiện các cập nhật đối lập nhau cho các lớp trước đó.

Với mô hình hai đầu, thường hợp lý hơn khi để một đầu chiếm ưu thế và cho phép nó kiểm soát hầu hết các tham số bằng cách tách đầu kia khỏi một số lớp đầu tiên.

Cuối cùng, người phê bình áp dụng một lớp tuyến tính khác với chức năng kích hoạt tan giới hạn đầu ra trong khoảng, trừ 1, 1, lớp này hoàn hảo cho cuộc thăm dò giỏ hàng, vì phần thưởng là cộng 1 và trừ 1.

Hình 5.11. Đây là tổng quan về kiến ​​trúc cho mô hình phê bình diễn viên hai đầu của chúng tôi. Nó có hai lớp tuyến tính được chia sẻ và một điểm phân nhánh trong đó đầu ra của hai lớp đầu tiên được gửi đến lớp log softmax của đầu tác nhân và cả lớp ray-lew của đầu phê bình, trước khi cuối cùng đi qua lớp tan, đây là một hàm kích hoạt giới hạn đầu ra trong khoảng từ âm 1 đến 1. Mô hình này trả về một bộ hai tenxơ thay vì một tenxơ đơn.

Lưu ý rằng đầu phê bình được tách ra, được biểu thị bằng đường chấm, có nghĩa là chúng ta không truyền ngược từ đầu phê bình vào đầu tác nhân hoặc phần đầu của mô hình, chỉ có tác nhân truyền ngược qua phần đầu của mô hình.

Trong danh sách sau đây, chúng tôi phát triển mã cần thiết để phân phối nhiều phiên bản của mô hình phê bình tác nhân trên các quy trình khác nhau.

Liệt kê 5.5. Phân phối đào tạo.

Đây chính xác là cách thiết lập mà chúng ta đã có khi trình bày cách chia một mảng thành nhiều quy trình, ngoại trừ lần này chúng ta sẽ chạy một hàm có tên là worker để chạy thuật toán học tăng cường thăm dò giỏ hàng của chúng ta.

Tiếp theo, chúng ta sẽ xác định hàm worker, hàm này sẽ chạy một tác nhân duy nhất trong một phiên bản của môi trường thăm dò giỏ hàng.

Liệt kê 5.6, vòng lặp đào tạo chính.

Hàm worker là hàm mà mỗi tiến trình riêng lẻ sẽ chạy riêng biệt. Mỗi công nhân, tức là quy trình, sẽ tạo môi trường thăm dò giỏ hàng và trình tối ưu hóa riêng, nhưng sẽ chia sẻ mô hình phê bình tác nhân, được chuyển vào dưới dạng đối số cho hàm.

Vì mô hình được chia sẻ nên bất cứ khi nào một công nhân cập nhật các tham số của mô hình, chúng sẽ được cập nhật cho tất cả các công nhân. Điều này được thể hiện ở mức cao trong hình 5.12.

Hình 5.12. Trong mỗi quy trình, một tập của trò chơi được chạy bằng mô hình dùng chung. Sự mất mát được tính toán trong mỗi quy trình, nhưng trình tối ưu hóa có tác dụng cập nhật mô hình phê bình tác nhân dùng chung được mỗi quy trình sử dụng.

Vì mỗi công nhân được sinh ra trong một quy trình mới có bộ nhớ riêng nên tất cả dữ liệu mà công nhân cần phải được chuyển vào dưới dạng đối số cho hàm một cách rõ ràng. Điều này cũng ngăn ngừa lỗi.

Trong danh sách 5.7, chúng tôi xác định một hàm để chạy một phiên bản duy nhất của mô hình phê bình diễn viên thông qua một tập trong môi trường thăm dò giỏ hàng.

Liệt kê 5.7, đang chạy một tập.

Hàm chạy tập gạch dưới chỉ chạy qua một tập duy nhất của cuộc thăm dò giỏ hàng và thu thập các giá trị trạng thái được tính toán từ người phê bình, ghi lại xác suất về các hành động của tác nhân và phần thưởng từ môi trường.

Chúng tôi lưu trữ những thứ này trong danh sách và sử dụng chúng để tính hàm mất mát sau này. Vì đây là phương pháp phê bình diễn viên chứ không phải Q learning, nên chúng tôi thực hiện hành động bằng cách lấy mẫu trực tiếp từ chính sách thay vì tự ý chọn chính sách như Epsilon-Greedy trong Q learning.

Không có gì quá bất thường trong chức năng này, vì vậy hãy chuyển sang chức năng cập nhật.

Liệt kê 5.8, tính toán và giảm thiểu tổn thất.

Hàm thông số gạch dưới cập nhật là nơi diễn ra tất cả các hành động và đó là yếu tố khiến nhà phê bình diễn viên có lợi thế phân tán khác biệt với các thuật toán khác mà chúng ta đã học cho đến nay.

Đầu tiên, chúng tôi lấy danh sách phần thưởng, xác suất ghi nhật ký và giá trị trạng thái rồi chuyển đổi chúng thành thang đo PyTorch.

Sau đó, chúng tôi đảo ngược thứ tự của chúng vì chúng tôi muốn xem xét hành động gần đây nhất trước tiên và chúng tôi đảm bảo rằng chúng được làm phẳng các mảng 1D bằng cách gọi phương thức .view, trừ 1,.

Việc mất dấu gạch dưới của tác nhân được tính toán như chúng tôi đã mô tả trước đó trong phần này bằng toán học, sử dụng lợi thế, về mặt kỹ thuật là đường cơ sở vì không có phần khởi động thay vì phần thưởng thô.

Điều quan trọng là chúng ta phải tách các giá trị tenxơ khỏi biểu đồ khi chúng ta sử dụng phần mất dấu gạch dưới của tác nhân, nếu không chúng ta sẽ truyền ngược lại thông qua các đầu tác nhân và nhà phê bình và chúng ta chỉ muốn cập nhật đầu tác nhân.

Sự mất mát phê bình là một lỗi bình phương đơn giản giữa các giá trị trạng thái và kết quả trả về và chúng tôi đảm bảo không tách rời ở đây vì chúng tôi muốn cập nhật phần đầu phê bình.

Sau đó, chúng ta cộng tổng thiệt hại của tác nhân và nhà phê bình để có được tổng thiệt hại. Chúng tôi giảm mức tổn thất của nhà phê bình bằng cách nhân với 0,1 vì chúng tôi muốn tác nhân học nhanh hơn nhà phê bình.

Chúng tôi trả lại các khoản lỗ riêng lẻ và độ dài của tensor phần thưởng, cho biết thời lượng của tập phim, để theo dõi tiến trình của họ trong quá trình đào tạo.

Theo cách chúng tôi đã thiết lập ở đây, mỗi nhân viên sẽ cập nhật các tham số mô hình được chia sẻ một cách không đồng bộ bất cứ khi nào chạy xong một tập.

Chúng tôi có thể đã thiết kế nó sao cho chúng tôi đợi tất cả công nhân chạy xong một tập, sau đó tổng hợp các gradient của họ lại với nhau và cập nhật các tham số được chia sẻ một cách đồng bộ.

Nhưng điều này phức tạp hơn và cách tiếp cận không đồng bộ hoạt động tốt trong thực tế.

Tập hợp tất cả lại với nhau và chạy, bạn sẽ có được một nhân viên kéo xe đã qua đào tạo trong vòng một phút trên một máy tính hiện đại chỉ chạy trên một vài lõi CPU.

Nếu bạn vẽ biểu đồ lỗ theo thời gian cho điều này, có thể nó sẽ không phải là một đường có xu hướng đi xuống tốt đẹp như bạn mong đợi, bởi vì người thực hiện và nhà phê bình đang cạnh tranh với nhau, hình 5.13.

Người phê bình được khuyến khích mô hình hóa lợi nhuận tốt nhất có thể và lợi nhuận phụ thuộc vào những gì người thực hiện làm.

Nhưng diễn viên được khuyến khích để đánh bại sự mong đợi của nhà phê bình.

Nếu người diễn viên tiến bộ nhanh hơn người phê bình thì thiệt hại của người phê bình sẽ cao và ngược lại, do đó giữa hai người có phần nào đó có mối quan hệ đối nghịch.

Hình 5.13. Tác nhân và nhà phê bình có một chút mối quan hệ đối nghịch vì các hành động mà tác nhân thực hiện sẽ ảnh hưởng đến việc mất đi nhà phê bình và nhà phê bình đưa ra dự đoán về các giá trị trạng thái được đưa vào kết quả trả về ảnh hưởng đến việc đào tạo.

Do đó, biểu đồ tổn thất tổng thể có thể trông hỗn loạn mặc dù thực tế là tác nhân thực sự đang tăng hiệu suất.

Đào tạo đối nghịch như thế này là một kỹ thuật rất mạnh mẽ trong nhiều lĩnh vực học máy, không chỉ học tăng cường.

Ví dụ: mạng đối thủ tổng quát, GAN, là một phương pháp không được giám sát để tạo ra các mẫu dữ liệu tổng hợp có vẻ thực tế từ tập dữ liệu huấn luyện, sử dụng một cặp mô hình phù hợp với phạm vi dữ liệu.

Trên thực tế, chúng ta sẽ xây dựng một mô hình đối nghịch thậm chí còn phức tạp hơn ở chương 8.

Điều đáng hiểu ở đây là nếu bạn đang sử dụng một mô hình đối nghịch, thì sự mất mát phần lớn sẽ không mang tính thông tin, trừ khi nó về 0 hoặc bùng nổ về phía vô cực, trong trường hợp đó có thể có điều gì đó không ổn.

Bạn phải dựa vào việc đánh giá thực sự mục tiêu mà bạn quan tâm, trong trường hợp của chúng tôi là tác nhân hoạt động tốt như thế nào trong trò chơi và kết quả là việc mất mục tiêu là không giống nhau.

Đầu tiên là tập dữ liệu huấn luyện, cho biết tác nhân hoạt động tốt như thế nào trong trò chơi.

Hình 5.14 cho thấy cốt truyện có độ dài tập trung bình trong 120 sử thi đầu tiên, khoảng 45 giây luyện tập.

Hình 5.14. Độ dài tập trung bình theo thời gian đào tạo cho mô hình phê bình diễn viên có lợi thế được phân phối ở Monte Carlo của chúng tôi.

Nhà phê bình không khởi động trong quá trình đào tạo. Kết quả là hiệu quả tập luyện có sự chênh lệch cao.