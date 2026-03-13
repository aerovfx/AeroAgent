# Chương 8. Mô-đun tò mò nội tại Học tập củng cố sâu trong hành động, Phiên bản video được dịch

---

Phần 8.6 Mô-đun tò mò nội tại

Như chúng tôi đã mô tả trước đó, Mô-đun tò mò nội tại, ICM, bao gồm ba mô hình mạng thần kinh độc lập

Mô hình thuận, Mô hình nghịch đảo và Bộ mã hóa, Hình 8.13.

Mô hình chuyển tiếp được đào tạo để dự đoán trạng thái được mã hóa tiếp theo, dựa trên trạng thái hiện tại, được mã hóa và hành động.

Mô hình nghịch đảo được đào tạo để dự đoán hành động đã được thực hiện, cho hai trạng thái liên tiếp, được mã hóa, năm trạng thái viết hoa S, T và năm trạng thái viết hoa S, T cộng một.

Bộ mã hóa chỉ đơn giản chuyển đổi trạng thái ba kênh thô thành một vectơ có chiều thấp duy nhất.

Mô hình nghịch đảo hoạt động gián tiếp để huấn luyện bộ mã hóa mã hóa các trạng thái theo cách chỉ lưu giữ thông tin liên quan đến việc dự đoán hành động.

Hình 8.13, tổng quan cấp cao về Mô-đun tò mò nội tại, ICM.

ICM có ba thành phần, mỗi mạng thần kinh riêng biệt.

Mô hình Bộ mã hóa mã hóa các trạng thái thành một vectơ chiều thấp và được huấn luyện gián tiếp thông qua Mô hình nghịch đảo, mô hình này cố gắng dự đoán hành động đã được thực hiện, cho hai trạng thái liên tiếp.

Mô hình chuyển tiếp dự đoán trạng thái được mã hóa tiếp theo và lỗi của nó là lỗi dự đoán được sử dụng làm Phần thưởng nội tại.

Các loại đầu vào và đầu ra của từng thành phần của ICM được hiển thị trong Hình 8.14.

Mô hình chuyển tiếp là một mạng lưới thần kinh hai lớp đơn giản, với các lớp tuyến tính.

Đầu vào của Mô hình Chuyển tiếp được xây dựng bằng cách ghép trạng thái năm của chữ S, T, với hành động A, T.

Trạng thái được mã hóa Năm của Chữ hoa S, T, là một tensor B x 288 và biến hành động A, T, có kích thước B x 1, là một tập hợp các số nguyên biểu thị chỉ số hành động.

Vì vậy, chúng tôi tạo một vectơ được mã hóa một lần bằng cách tạo một vectơ có kích thước 12 và đặt chỉ mục A, T tương ứng thành 1.

Sau đó, chúng ta ghép hai tensor này để tạo ra một lô 288 cộng 12 bằng lô tensor 300 chiều.

Chúng tôi sử dụng đơn vị kích hoạt Ray-Lew tuyến tính đã được chỉnh lưu sau lớp đầu tiên, nhưng chúng tôi không sử dụng chức năng kích hoạt sau lớp đầu ra.

Lớp đầu ra tạo ra một tensor B x 288.

Hình 8.14. Hình này cho thấy loại và kích thước của đầu vào và đầu ra của từng thành phần của ICM.

Mô hình nghịch đảo cũng là một mạng nơ-ron hai lớp đơn giản với các lớp tuyến tính.

Đầu vào là hai trạng thái được mã hóa, viết hoa S, T và viết hoa S, T cộng 1, được ghép nối để tạo thành một tenxơ có kích thước bằng 288 cộng với 288 bằng lô bằng 576.

Chúng tôi sử dụng chức năng kích hoạt Ray-Lew sau lớp đầu tiên.

Lớp đầu ra tạo ra một tensor có lô kích thước 12, với hàm softmax được áp dụng, dẫn đến phân bố xác suất rời rạc cho các hành động.

Khi huấn luyện Mô hình nghịch đảo, chúng tôi tính toán lỗi giữa phân phối rời rạc này theo các hành động và vectơ được mã hóa một lần của hành động thực được thực hiện.

Bộ mã hóa là một mạng lưới thần kinh bao gồm bốn lớp tích chập, có kiến ​​trúc giống hệt DQN, với chức năng kích hoạt ELU sau mỗi lớp.

Đầu ra cuối cùng sau đó được làm phẳng để có đầu ra vectơ phẳng 288 chiều.

Mục đích chung của ICM là tạo ra một đại lượng duy nhất, lỗi dự đoán mô hình chuyển tiếp, hình 8.15.

Theo nghĩa đen, chúng tôi coi lỗi do hàm mất tạo ra và sử dụng lỗi đó làm tín hiệu phần thưởng nội tại cho DQN của chúng tôi.

Chúng ta có thể thêm phần thưởng nội tại này vào phần thưởng bên ngoài để nhận được tín hiệu phần thưởng cuối cùng, RT bằng RI cộng RE.

Chúng ta có thể mở rộng quy mô phần thưởng bên trong hoặc bên ngoài để kiểm soát tỷ lệ của tổng phần thưởng.

Hình 8.15. DQN và ICM đóng góp vào một hàm tổn thất tổng thể duy nhất được cung cấp cho trình tối ưu hóa để giảm thiểu các tham số DQN và ICM.

Dự đoán giá trị Q của DQN được so sánh với phần thưởng quan sát được. Tuy nhiên, phần thưởng quan sát được sẽ được tổng hợp cùng với lỗi dự đoán của ICM để có giá trị phần thưởng mới.

Hình 8.16. Hiển thị ICM chi tiết hơn, bao gồm cả mô hình đại lý, DQN. Hãy xem mã cho các thành phần của ICM.

Hình 8.16. Một cái nhìn đầy đủ về thuật toán tổng thể, bao gồm cả ICM.

Đầu tiên, chúng tôi tạo các mẫu B từ bộ nhớ phát lại trải nghiệm và sử dụng các mẫu này cho ICM và DQN.

Chúng tôi chạy chuyển tiếp ICM để tạo ra lỗi dự đoán, sau đó lỗi này được cung cấp cho hàm lỗi của DQN.

DQN học cách dự đoán các giá trị hành động không chỉ phản ánh phần thưởng bên ngoài, môi trường được cung cấp mà còn phản ánh phần thưởng nội tại, dựa trên lỗi dự đoán.

Liệt kê 8.6 các thành phần ICM.

Không có thành phần nào trong số này có kiến ​​trúc phức tạp. Chúng khá trần tục, nhưng cùng nhau chúng tạo thành một hệ thống mạnh mẽ.

Bây giờ chúng ta cần đưa vào mô hình DQN của mình, đây là một tập hợp đơn giản gồm một vài lớp chập.

Liệt kê 8.7 mạng deepQ.

Chúng tôi đã đề cập đến các thành phần ICM. Bây giờ hãy đặt chúng lại với nhau. Chúng ta sẽ định nghĩa một hàm chấp nhận,

viết hoa S, TAT, viết hoa S, T cộng 1 và trả về lỗi dự đoán mô hình thuận và lỗi mô hình nghịch đảo.

Lỗi mô hình chuyển tiếp sẽ không chỉ được sử dụng để truyền ngược và huấn luyện mô hình chuyển tiếp mà còn là phần thưởng nội tại cho DQN.

Lỗi mô hình nghịch đảo chỉ được sử dụng để truyền ngược và huấn luyện các mô hình nghịch đảo và bộ mã hóa.

Đầu tiên chúng ta sẽ xem xét việc thiết lập siêu tham số và khởi tạo các mô hình.

Liệt kê 8.8 siêu tham số và khởi tạo mô hình.

Một số tham số trong từ điển của Param sẽ trông quen thuộc, chẳng hạn như kích thước gạch dưới hàng loạt, nhưng những tham số khác có thể không quen thuộc.

Chúng ta sẽ xem xét chúng, nhưng trước tiên hãy xem xét hàm mất mát tổng thể.

Đây là công thức tính tổn thất chung cho cả bốn mẫu xe, bao gồm cả DQN.

Xem công thức này.

Công thức này cộng tổn thất DQN vào tổn thất mô hình thuận và nghịch đảo, mỗi tổn thất được tính theo một hệ số.

Tổn thất DQN có tham số chia tỷ lệ tự do, lambda, trong khi tổn thất mô hình thuận và nghịch đảo có chung tham số tỷ lệ, beta, do đó chúng có liên quan nghịch đảo.

Đây là hàm mất mát duy nhất mà chúng tôi truyền ngược lại, vì vậy ở mỗi bước huấn luyện, chúng tôi truyền ngược qua cả bốn mô hình bắt đầu từ hàm mất mát đơn này.

Các tham số tiến trình gạch dưới tập gạch dưới tối đa len và tối thiểu được sử dụng để đặt mức tiến trình chuyển tiếp tối thiểu mà Mario phải thực hiện hoặc chúng tôi sẽ đặt lại môi trường.

Đôi khi Mario sẽ bị mắc kẹt sau một chướng ngại vật và chúng ta sẽ cứ thực hiện cùng một hành động mãi mãi, vì vậy nếu Mario không tiến về phía trước đủ trong một khoảng thời gian hợp lý, chúng ta sẽ cho rằng anh ấy bị mắc kẹt.

Trong quá trình đào tạo, chẳng hạn, nếu hàm chính sách yêu cầu thực hiện hành động thứ ba, chúng tôi sẽ lặp lại hành động đó sáu lần, được đặt theo tham số lặp lại dấu gạch dưới hành động thay vì chỉ một lần.

Điều này giúp DQN tìm hiểu giá trị của hành động nhanh hơn.

Trong quá trình thử nghiệm, đó là suy luận, chúng ta chỉ thực hiện hành động một lần.

Tham số gamma giống với tham số gamma trong chương DQN.

Khi đào tạo DQN, giá trị mục tiêu không chỉ là RT phần thưởng hiện tại mà còn là giá trị hành động được dự đoán cao nhất cho trạng thái tiếp theo, do đó, mục tiêu đầy đủ là phần thưởng tại thời điểm, T cộng gamma nhân với mức tối đa của Q tại vốn thời điểm S, T cộng một.

Cuối cùng, thông số khung hình gạch dưới trên mỗi trạng thái gạch dưới được đặt thành ba, vì mỗi trạng thái là ba khung hình cuối cùng của trò chơi.

Liệt kê 8.9, hàm mất và môi trường thiết lập lại.

Cuối cùng, chúng ta có được chức năng ICM thực tế.

Liệt kê 8.10, tính toán lỗi dự đoán ICM.

Cần phải nhắc lại tầm quan trọng của việc tách các nút khỏi biểu đồ một cách chính xác khi chạy ICM.

Hãy nhớ lại rằng PyTorch và hầu hết các thư viện máy học khác đều xây dựng một biểu đồ tính toán trong đó các nút là các hoạt động, tính toán và kết nối, còn được gọi là các cạnh.

Giữa các nút là các tensor đi vào và ra khỏi các hoạt động riêng lẻ.

Bằng cách gọi phương thức tách dấu chấm, chúng tôi ngắt kết nối tensor khỏi biểu đồ tính toán và xử lý nó giống như dữ liệu thô.

Điều này ngăn PyTorch truyền ngược qua cạnh đó.

Nếu chúng ta không tách trạng thái một mũ gạch dưới và nêu hai tensor mũ gạch dưới khi chúng ta chạy mô hình chuyển tiếp và sự mất mát của nó, thì mô hình chuyển tiếp sẽ truyền ngược vào bộ mã hóa và sẽ làm hỏng mô hình bộ mã hóa.

Bây giờ chúng ta đã tiếp cận vòng đào tạo chính.

Hãy nhớ rằng, vì chúng ta đang sử dụng tính năng phát lại trải nghiệm nên việc đào tạo chỉ diễn ra khi chúng ta lấy mẫu từ bộ đệm phát lại.

Chúng ta sẽ thiết lập một hàm lấy mẫu từ bộ đệm phát lại và tính toán các lỗi mô hình riêng lẻ.

Liệt kê 8.11, đào tạo theo đợt nhỏ sử dụng tính năng phát lại kinh nghiệm.

Bây giờ chúng ta hãy giải quyết vòng huấn luyện chính, được hiển thị trong danh sách 8.12.

Chúng tôi khởi tạo trạng thái đầu tiên bằng cách sử dụng hàm trạng thái gạch dưới ban đầu chuẩn bị với các đối số bên trong dấu ngoặc đơn mà chúng tôi đã xác định trước đó, chỉ lấy khung đầu tiên và lặp lại ba lần dọc theo chiều kênh.

Chúng tôi cũng thiết lập một phiên bản boong mà chúng tôi sẽ thêm từng khung hình vào đó khi chúng tôi quan sát chúng.

Bộ bài được đặt ở dòng tối đa là ba, vì vậy chỉ có ba khung hình gần đây nhất được lưu trữ.

Trước tiên, chúng tôi chuyển đổi bộ bài thành một danh sách, sau đó thành một tenxơ PyTorch có kích thước 1 x 3 x 42 x 42, trước khi chuyển nó sang mạng Q.

Liệt kê 8.12, vòng lặp huấn luyện.

Mặc dù hơi dài nhưng vòng đào tạo này khá đơn giản.

Tất cả những gì chúng tôi làm là chuẩn bị đầu vào trạng thái cho DQN, nhận giá trị hành động, giá trị Q, đầu vào chính sách, thực hiện hành động và sau đó gọi hàm bước môi trường của phương thức hành động để thực hiện hành động.

Sau đó chúng tôi nhận được trạng thái tiếp theo và một số siêu dữ liệu khác. Chúng tôi thêm trải nghiệm đầy đủ này dưới dạng một bộ, viết hoa S, T, A, T, R, T, viết hoa S, T cộng 1, vào bộ nhớ phát lại trải nghiệm.

Hầu hết hành động diễn ra trong chức năng đào tạo hàng loạt nhỏ mà chúng tôi đã đề cập.

Đó là mã chính bạn cần để xây dựng DQN và ICM từ đầu đến cuối để đào tạo về Super Mario Brothers.

Hãy kiểm tra nó bằng cách huấn luyện trong 5.000 kỷ nguyên, mất khoảng 30 phút hoặc lâu hơn để chạy trên MacBook Air, không có GPU.

Chúng ta sẽ huấn luyện bằng cách sử dụng dấu gạch dưới bên ngoài bằng sai trong hàm lô nhỏ, vì vậy nó chỉ học từ phần thưởng nội tại.

Bạn có thể vẽ biểu đồ tổn thất riêng lẻ cho từng thành phần ICM và DQN bằng mã sau.

Chúng tôi sẽ ghi nhật ký chuyển đổi dữ liệu bị mất để giữ chúng ở quy mô tương tự.

Xem mã này.

Như được hiển thị trong Hình 8.17, tổn thất DQN ban đầu giảm xuống và sau đó tăng dần ở mức ổn định.

Sự mất mát kỳ hạn dường như giảm dần nhưng khá ồn ào.

Mô hình nghịch đảo trông có vẻ phẳng, nhưng nếu bạn phóng to, nó dường như giảm rất chậm theo thời gian.

Các ô thua lỗ trông đẹp hơn rất nhiều nếu bạn đặt sử dụng dấu gạch dưới bên ngoài bằng đúng và sử dụng phần thưởng bên ngoài.

Nhưng đừng cảm thấy thất vọng bởi những âm mưu thua lỗ.

Nếu chúng tôi kiểm tra DQN đã được huấn luyện, bạn sẽ thấy rằng nó hoạt động tốt hơn rất nhiều so với biểu đồ tổn thất gợi ý.

Điều này là do ICM và DQN đang hoạt động giống như một hệ thống động đối nghịch, vì mô hình chuyển tiếp đang cố gắng giảm sai số dự đoán của nó.

Nhưng DQN đang cố gắng tối đa hóa lỗi dự đoán bằng cách hướng tác nhân tới các trạng thái môi trường không thể đoán trước.

Hình 8.18

Hình 8.17. Đây là những tổn thất đối với các thành phần riêng lẻ của ICM và DQN.

Tổn thất không giảm một cách suôn sẻ như chúng ta vẫn quen với một mạng lưới thần kinh được giám sát duy nhất, vì DQN và ICM được đào tạo theo hướng đối nghịch.

Hình 8.18. Tác nhân DQN và mô hình chuyển tiếp đang cố gắng tối ưu hóa các mục tiêu đối kháng và do đó tạo thành một cặp đối nghịch.

Nếu bạn nhìn vào biểu đồ tổn thất của một mạng đối thủ tổng hợp, GAN. Sự mất mát của trình tạo và bộ phân biệt đối xử trông hơi giống với DQN của chúng tôi và việc mất mô hình chuyển tiếp khi sử dụng dấu gạch dưới bên ngoài bằng sai.

Tổn thất không giảm đi một cách suôn sẻ như bạn vẫn quen khi huấn luyện một mô hình học máy duy nhất.

Đánh giá tốt hơn về mức độ hiệu quả của quá trình đào tạo tổng thể là theo dõi độ dài của tập theo thời gian.

Độ dài tập phim sẽ tăng lên nếu đặc vụ đang học cách phát triển trong môi trường hiệu quả hơn.

Trong vòng đào tạo của chúng tôi, bất cứ khi nào tập kết thúc, tức là khi biến done trở thành đúng do tác nhân chết hoặc không thực hiện đủ tiến trình chuyển tiếp, chúng tôi sẽ lưu giá trị hiện tại của dấu gạch dưới X từ từ điển thông tin vào danh sách độ dài dấu gạch dưới EP.

Chúng tôi hy vọng rằng độ dài tập tối đa sẽ ngày càng dài hơn theo thời gian đào tạo.

Xem mã này.

Trong Hình 8.19, chúng ta thấy rằng ngay từ đầu, mức tăng đột biến lớn nhất là đạt đến mốc 150, tức là vị trí X trong trò chơi.

Nhưng theo thời gian huấn luyện, khoảng cách xa nhất mà đặc vụ có thể đạt được, biểu thị bằng chiều cao của các gai, tăng đều đặn, mặc dù có một số ngẫu nhiên.

Hình 8.19, thời gian đào tạo trên trục X và độ dài tập trên trục Y.

Chúng tôi nhận thấy mức tăng đột biến ngày càng lớn hơn trong thời gian đào tạo, đó là những gì chúng tôi mong đợi.

Cốt truyện dài tập có vẻ đầy hứa hẹn nhưng hãy chiếu một video về đặc vụ được đào tạo của chúng ta chơi Super Mario Brothers.

Nếu bạn đang chạy ứng dụng này trên máy tính của riêng mình, OpenAI Jim sẽ cung cấp chức năng kết xuất sẽ mở một cửa sổ mới với lối chơi trực tiếp.

Thật không may, điều này sẽ không hoạt động nếu bạn đang sử dụng máy từ xa hoặc máy ảo trên đám mây.

Trong những trường hợp đó, giải pháp thay thế dễ dàng nhất là chạy một vòng lặp của trò chơi, lưu từng khung quan sát vào một danh sách và khi vòng lặp kết thúc, hãy chuyển đổi nó thành một mảng có nhiều mảng.

Sau đó, bạn có thể lưu mảng khung hình video phức tạp này dưới dạng video và phát nó trong sổ ghi chép Jupyter.

Xem mã này.

Trong danh sách 8.13, chúng tôi sử dụng phương thức kết xuất OpenAI Jim tích hợp sẵn để xem trò chơi trong thời gian thực.

Liệt kê 8.13, kiểm tra tác nhân đã được đào tạo.

Không có nhiều điều để giải thích ở đây nếu bạn tuân theo vòng đào tạo.

Chúng tôi chỉ trích xuất phần chạy mạng về phía trước và thực hiện hành động.

Lưu ý rằng chúng tôi vẫn sử dụng chính sách tham lam của Epsilon với Epsilon được đặt thành 0,1.

Ngay cả trong quá trình suy luận, tác nhân cần một chút ngẫu nhiên để giữ cho nó không bị mắc kẹt.

Một điểm khác biệt cần lưu ý là trong chế độ kiểm tra hoặc suy luận, chúng tôi chỉ thực hiện hành động một lần chứ không phải sáu lần như khi đào tạo.

Giả sử bạn nhận được kết quả tương tự như chúng tôi, nhân viên được đào tạo của bạn sẽ đạt được tiến bộ khá nhất quán về phía trước và có thể nhảy qua chướng ngại vật.

Hình 8.20.

Hình 8.20.

Đặc vụ Mario chỉ được đào tạo từ phần thưởng nội tại để nhảy qua vực thẳm thành công.

Điều này chứng tỏ nó đã học được các kỹ năng cơ bản mà không cần bất kỳ phần thưởng rõ ràng nào để làm điều đó.

Với chính sách ngẫu nhiên, đặc vụ thậm chí sẽ không thể tiến về phía trước chứ đừng nói đến việc học cách nhảy qua chướng ngại vật.

Nếu bạn không nhận được kết quả tương tự, hãy thử thay đổi các siêu tham số, đặc biệt là tốc độ học tập, kích thước lô nhỏ, thời lượng tập tối đa và tiến trình chuyển tiếp tối thiểu.

Việc đào tạo trong 5.000 kỷ nguyên trong phần thưởng nội tại có hiệu quả, nhưng theo kinh nghiệm của chúng tôi, nó rất nhạy cảm với các siêu tham số này.

Tất nhiên, 5.000 kỷ nguyên không phải là dài lắm, vì vậy việc huấn luyện lâu hơn sẽ mang lại những hành vi thú vị hơn.

Điều này sẽ hoạt động như thế nào trong các môi trường khác?

Chúng tôi đã đào tạo đại lý DQN của mình bằng phần thưởng dựa trên ICM trên một môi trường duy nhất, Super Mario Bros.

Nhưng bài báo, Nghiên cứu quy mô lớn về việc học tập theo hướng tò mò của Yuri Burda, năm 2018, đã chứng minh rằng chỉ riêng phần thưởng nội tại có thể hiệu quả như thế nào.

Họ đã tiến hành một số thử nghiệm bằng cách sử dụng phần thưởng dựa trên sự tò mò trên nhiều trò chơi và phát hiện ra rằng một đặc vụ tò mò có thể tiến bộ qua 11 cấp độ trong Super Mario Bros.

và có thể học chơi bóng bàn trong số các trò chơi khác.

Về cơ bản, họ đã sử dụng cùng một ICM mà chúng tôi vừa xây dựng, ngoại trừ việc họ sử dụng mô hình phê bình tác nhân phức tạp hơn có tên là Tối ưu hóa chính sách gần nhất, PPO, thay vì DQN.

Một thử nghiệm bạn có thể thử là thay thế mạng bộ mã hóa bằng phép chiếu ngẫu nhiên.

Phép chiếu ngẫu nhiên chỉ có nghĩa là nhân dữ liệu đầu vào với ma trận được khởi tạo ngẫu nhiên.

Ví dụ: một mạng nơ-ron được khởi tạo ngẫu nhiên được cố định và không được huấn luyện.

Bài báo Burda 2018 đã chứng minh rằng phép chiếu ngẫu nhiên hoạt động gần như tốt như bộ mã hóa được đào tạo.