# Chương 9. Trò chơi hợp tác-cạnh tranh hỗn hợp Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Mục 9.5.

Trò chơi cạnh tranh hợp tác hỗn hợp

Nếu bạn coi mô hình đóng băng là một trò chơi nhiều người chơi thì nó sẽ được coi là một trò chơi hợp tác thuần túy.

trò chơi nhiều người chơi, vì tất cả các đặc vụ đều có cùng mục tiêu và phần thưởng của họ được tối đa hóa

khi họ làm việc cùng nhau để tất cả đều đi theo cùng một hướng.

Ngược lại, cờ vua là một trò chơi mang tính cạnh tranh thuần túy, bởi vì khi một người chơi thắng

người chơi khác thua thì tổng bằng 0.

Các trò chơi mang tính đồng đội như Bóng rổ hoặc Bóng đá được gọi là cạnh tranh hợp tác hỗn hợp

trò chơi, vì các đặc vụ trong cùng một đội cần hợp tác để tối đa hóa

phần thưởng.

Nhưng khi toàn bộ một đội chiến thắng thì đội kia chắc chắn đang thua, vì vậy đội đó phải

cấp độ đồng đội, đó là một trò chơi mang tính cạnh tranh.

Trong phần này, chúng ta sẽ sử dụng một trò chơi dựa trên thế giới lưới nguồn mở được thiết kế đặc biệt

được thiết kế để thử nghiệm các thuật toán học tăng cường đa tác nhân trong hợp tác,

kịch bản cạnh tranh cạnh tranh hoặc hợp tác hỗn hợp, Hình 9.23.

Trong trường hợp của chúng tôi, chúng tôi sẽ thiết lập một kịch bản cạnh tranh hợp tác hỗn hợp với hai đội thế giới lưới

các tác nhân có thể di chuyển trong lưới và cũng có thể tấn công các tác nhân khác trên đối phương

đội.

Mỗi đặc vụ bắt đầu với một điểm máu, HP và khi họ bị tấn công, HP sẽ giảm đi

từng chút một cho đến khi nó về 0, lúc đó tác nhân chết và bị xóa

ra khỏi lưới điện.

Điều này nhận được phần thưởng khi tấn công và tiêu diệt các đặc vụ của đội đối phương.

Hình 9.23.

Ảnh chụp màn hình từ Trò chơi thế giới lưới nhiều người chơi M-Agent với hai đội đối lập nhau trong thế giới lưới

đại lý.

Mục tiêu là để mỗi đội tiêu diệt đội kia.

Vì tất cả các tác nhân trong một nhóm đều có chung mục tiêu và do đó có chính sách tối ưu,

chúng ta có thể sử dụng một DQN duy nhất để kiểm soát tất cả các đặc vụ trong một nhóm và một DQN khác để

kiểm soát các đặc vụ của đội khác.

Về cơ bản đây là trận chiến giữa hai DQN, vì vậy đây sẽ là cơ hội hoàn hảo để thử

ra các loại mạng lưới thần kinh khác nhau và xem cái nào tốt hơn.

Tuy nhiên, để đơn giản hóa mọi thứ, chúng tôi sẽ sử dụng cùng một DQN cho mỗi nhóm.

Bạn sẽ cần cài đặt thư viện M-Agent từ liên kết này bằng cách làm theo hướng dẫn

trên trang ReadMe.

Từ thời điểm này trở đi, chúng tôi sẽ cho rằng bạn đã cài đặt nó và bạn có thể thành công

chạy import M-Agent trong môi trường Python của bạn.

Liệt kê 9.13, tạo môi trường M-Agent.

M-Agent có khả năng tùy biến cao, nhưng chúng tôi sẽ sử dụng cấu hình tích hợp có tên

Trận chiến để thiết lập một kịch bản chiến đấu hai đội.

M-Agent có API tương tự OpenAI Jim nhưng có một số khác biệt quan trọng.

Đầu tiên, chúng ta phải thiết lập tay cầm cho mỗi đội trong số hai đội.

Đây là các đối tượng, nhóm 1 và nhóm 2, có các phương thức và thuộc tính phù hợp với từng đối tượng

đội.

Chúng ta thường chuyển các thẻ điều khiển này cho một phương thức của đối tượng môi trường, N-V.

Ví dụ: để lấy danh sách tọa độ của từng đặc vụ trong đội 1, chúng tôi sử dụng N-V dot get

tư thế nhấn mạnh của đội 1.

Chúng ta sẽ sử dụng kỹ thuật tương tự để giải quyết môi trường này như chúng ta đã làm với cả hai

Mô hình D-I-Zing, nhưng với hai DQN, chúng ta sẽ sử dụng chính sách softmax và trải nghiệm phát lại

bộ đệm.

Các đội sẽ trở nên phức tạp một chút vì số lượng đại lý thay đổi trong quá trình đào tạo,

vì các đặc vụ có thể chết và bị loại khỏi mạng lưới.

Với mô hình I-Zing, trạng thái của môi trường là những hành động chung.

Không có thông tin bổ sung của tiểu bang.

Trong M-Agent, chúng tôi còn có vị trí và điểm sức khỏe của các đặc vụ dưới dạng thông tin trạng thái.

Hàm Q sẽ là QJ của S, T, A0J trong đó A0J là trường trung bình của các tác nhân trong

tầm nhìn, FOV hoặc vùng lân cận của đặc vụ J.

Theo mặc định, mỗi tác nhân có FOV của lưới 13 x 13 xung quanh chính nó.

Do đó, mỗi tác nhân sẽ có trạng thái của lưới FOV nhị phân 13 x 13 này hiển thị số 1 trong đó

có những đại lý khác.

Tuy nhiên, M-Agent tách ma trận FOV theo nhóm nên mỗi tác nhân có 2 13 x 13 FOV

lưới, 1 cho đội của mình và 1 cho đội khác.

Chúng ta sẽ cần kết hợp chúng thành một vectơ trạng thái duy nhất bằng cách làm phẳng và ghép nối

chúng cùng nhau.

M-Agent cũng cung cấp điểm sức khỏe của các tác nhân trong FOV, nhưng để đơn giản,

chúng tôi sẽ không sử dụng những thứ này.

Chúng tôi đã khởi tạo môi trường nhưng chưa khởi tạo tác nhân trên lưới.

Bây giờ chúng tôi phải quyết định có bao nhiêu đặc vụ và đặt chúng ở đâu trên lưới cho mỗi đội.

Liệt kê 9.14, thêm các tác nhân.

Ở đây chúng tôi đã thiết lập các tham số cơ bản của mình.

Chúng tôi đang tạo một lưới 30 x 30 với 16 tổng đài viên cho mỗi nhóm để duy trì chi phí tính toán

thấp, nhưng nếu bạn có GPU, hãy thoải mái tạo một lưới lớn hơn với nhiều tác nhân hơn.

Chúng ta khởi tạo 2 vectơ tham số, 1 cho mỗi đội.

Một lần nữa, chúng tôi chỉ sử dụng mạng thần kinh 2 lớp đơn giản là DQN.

Bây giờ chúng ta có thể hình dung lưới.

Xem mã này.

M-Agent 2 ở bên trái và đội 1 ở bên phải, hình 9.24.

Tất cả các tác nhân được khởi tạo theo mẫu hình vuông và các nhóm được phân tách bằng

một lưới ô vuông.

Không gian hành động của mỗi tác nhân là một vectơ có độ dài 21 được mô tả trong hình 9.25.

Trong danh sách 9.15, chúng tôi giới thiệu một hàm để tìm các tác nhân lân cận của một tác nhân cụ thể

đại lý.

Trong hình 9.24, vị trí xuất phát của hai nhóm tác nhân trong môi trường M-Agent,

các ô vuông ánh sáng là các tác nhân riêng lẻ.

Hình 9.25 mô tả không gian hành động của các tác nhân trong thư viện M-Agent.

Mỗi đặc vụ có thể di chuyển theo 13 hướng khác nhau hoặc tấn công theo 8 hướng ngay lập tức xung quanh

nó.

Các hành động lần lượt bị tắt theo mặc định, vì vậy không gian hành động là 13 cộng 8 bằng 21.

Vào 9.15, việc tìm kiếm hàng xóm.

Chúng ta cần hàm này để tìm các láng giềng trong FOV của từng tác nhân để có thể tính toán

vectơ hành động trung bình.

Chúng ta có thể sử dụng NV.getUnderscorePoseOfTeam1 để lấy danh sách tọa độ của từng tác nhân

trên Team1, sau đó chúng ta có thể chuyển phần này vào hàm GetUnderscoreNabors cùng với

một chỉ số J để tìm những người hàng xóm của AgentJ.

Xem mã này.

Vậy Đặc vụ5 có 10 đặc vụ khác trong Đội 1 trong phạm vi 13 x 13 FOV của nó.

Bây giờ chúng ta cần tạo một vài hàm trợ giúp khác.

Các hành động mà môi trường chấp nhận và trả về là các số nguyên từ 0 đến 20, vì vậy chúng ta cần

để có thể chuyển đổi vectơ này thành vectơ hành động một lần và trở lại dạng số nguyên.

Chúng ta cũng cần một hàm lấy vectơ trường trung bình cho các lân cận xung quanh một

đại lý.

Liệt kê 9.16, tính toán hành động trường trung bình.

Để có được hàm trường gạch dưới trung bình dưới đây, trước tiên hãy gọi hàm GetUnderscoreNabors

để có được tọa độ của tất cả các đặc vụ cho AgentJ.

Để có được hàm trường gạch dưới trung bình dưới đây, hãy sử dụng các tọa độ này để lấy

vectơ hành động của tác nhân, cộng chúng lại và chia cho tổng số tác nhân cần chuẩn hóa.

Để có được hàm trường gạch dưới trung bình gạch dưới, hãy mong đợi vectơ hành động tương ứng

danh sách gạch dưới hành động, danh sách các hành động dựa trên số nguyên, trong đó các chỉ mục trong POS gạch dưới

list và hành động khớp danh sách gạch dưới với cùng một tác nhân.

Tham số R đề cập đến bán kính trong các ô vuông xung quanh AgentJ mà chúng tôi muốn đưa vào

là hàng xóm và L là kích thước của không gian hành động, là 21.

Không giống như các ví dụ về mô hình Ising, chúng ta sẽ tạo các hàm riêng biệt để chọn các hành động

cho mỗi đại lý và thực hiện đào tạo vì đây là môi trường phức tạp hơn và chúng tôi muốn

để mô-đun hóa thêm một chút.

Sau mỗi bước trong môi trường, chúng ta sẽ nhận được một tenxơ quan sát cho tất cả các tác nhân cùng một lúc.

Quan sát được EnV.GetUnderscoreObservationOfTeam1 trả về thực tế là một bộ dữ liệu có hai

tensor.

Tensor đầu tiên được hiển thị ở phần trên cùng của Hình 9.26.

Nó là một tenxơ bậc cao phức tạp, trong khi tenxơ thứ hai trong bộ có một số bổ sung

thông tin mà chúng tôi sẽ bỏ qua.

Từ giờ trở đi, khi chúng ta nói quan sát hoặc trạng thái, chúng ta muốn nói đến tensor đầu tiên như được mô tả trong Hình

9,26.

Hình 9.26, cấu trúc của tensor quan sát.

Đó là một tensor N x 13 x 13 x 7, trong đó N là số lượng đặc vụ trong nhóm.

Hình 9.26 cho thấy tensor quan sát này được sắp xếp thành từng lát.

Quan sát là một tensor N x 13 x 13 x 7, trong đó N là số lượng tác nhân, trong

trường hợp 16.

Mỗi lát 13 x 13 của tensor cho một tác nhân duy nhất hiển thị FOV cùng với vị trí của

tường, lát 0, đặc vụ Team1, lát 1, HP đặc vụ Team1, lát 2, v.v.

Chúng tôi sẽ chỉ sử dụng lát 1 và 4 cho vị trí của các đại lý trong Nhóm 1 và Nhóm

2 trong FOV.

Vì vậy, tenxơ quan sát của một tác nhân sẽ là 13 x 13 x 2 và chúng ta sẽ làm phẳng điều này

thành một vectơ để có được vectơ trạng thái có độ dài 338.

Sau đó chúng ta sẽ ghép vectơ trạng thái này với vectơ trường trung bình có độ dài 21,

để có được vectơ có chiều dài 338 cộng 21 bằng 359, điều đó sẽ được cấp cho hàm Q.

Sẽ là lý tưởng nếu sử dụng mạng nơ-ron hai đầu như chúng ta đã làm trong Chương 7.

Bằng cách đó, một đầu có thể xử lý vectơ trạng thái và đầu kia có thể xử lý giá trị trung bình

vector hành động trường.

Và sau đó chúng tôi có thể kết hợp lại thông tin đã xử lý ở lớp sau.

Chúng tôi không làm điều đó ở đây vì đơn giản nhưng đây là một bài tập tốt để bạn thử.

Trong danh sách 9.27, chúng ta định nghĩa một hàm để chọn hành động cho một tác nhân, dựa trên quan sát của nó,

trường trung bình của các tác nhân lân cận của nó.

Liệt kê 9.17, chọn các hành động.

Đây là chức năng chúng tôi sẽ sử dụng để chọn tất cả các hành động cho mỗi tác nhân sau khi chúng tôi nhận được

một quan sát.

Nó sử dụng hàm Q trường trung bình được tham số hóa bởi tham số và các lớp để lấy mẫu hành động cho

tất cả các tác nhân sử dụng chính sách softmax.

Hàm hành động gạch dưới suy ra có các tham số, kích thước vectơ sau và

dấu ngoặc đơn cho mỗi.

OBS là tensor quan sát, N x 13 x 13 x 2.

Các trường gạch dưới trung bình là tensor chứa tất cả các hành động trường trung bình cho mỗi tác nhân,

N vào ngày 21.

Danh sách gạch dưới QS là danh sách các vị trí cho từng tác nhân được môi trường trả về, nhận

vị trí có dấu ba chấm.

Ax là một vectơ gồm các hành động được biểu thị bằng số nguyên của mỗi tác nhân, N. NUM gạch dưới ITER là

số lần lựa chọn giữa lấy mẫu hành động và cập nhật chính sách.

Temp là nhiệt độ chính sách softmax để kiểm soát tốc độ thăm dò.

Hàm trả về một bộ dữ liệu.

Dấu gạch dưới Ax là vectơ của các hành động số nguyên được lấy mẫu từ chính sách, N.

Dấu gạch dưới của trường trung bình là một tenxơ của vectơ trường trung bình cho mỗi tác nhân, N21.

QVAL là một tensor của các giá trị Q cho mỗi hành động đối với mỗi tác nhân, N21.

Cuối cùng, chúng ta cần chức năng thực hiện việc đào tạo.

Chúng ta sẽ cung cấp cho hàm này vectơ tham số và bộ đệm phát lại trải nghiệm và để nó

thực hiện giảm độ dốc ngẫu nhiên hàng loạt nhỏ.

Liệt kê 9.18, hàm đào tạo.

Chức năng này hoạt động khá giống với cách chúng ta trải nghiệm tính năng phát lại với hai chức năng khử hóa.

mô hình và danh sách 9.12, nhưng thông tin trạng thái phức tạp hơn.

Hàm train huấn luyện một mạng nơ-ron đơn bằng cách sử dụng các trải nghiệm được lưu trữ trong một trải nghiệm

phát lại bộ nhớ đệm.

Nó có các đầu vào và đầu ra sau đây.

Kích thước gạch dưới hàng loạt int.

Danh sách phát lại các bộ OBS gạch dưới một gạch dưới các hành động nhỏ gạch dưới một phần thưởng một hành động gạch dưới có nghĩa là một Q tiếp theo.

Danh sách các lớp vectơ tham số mạng thần kinh vectơ tham số chứa hình dạng của các lớp mạng thần kinh J int số tác nhân trong nhóm này gamma float bằng 0.

Hệ số chiết khấu Tỷ lệ học thả nổi LR cho SGD trả về khoản lỗ thả nổi.

Bây giờ chúng tôi đã thiết lập môi trường thiết lập các tác nhân cho hai nhóm và xác định một số chức năng để cho phép chúng tôi huấn luyện hai DQN đang sử dụng cho việc học Q trường trung bình.

Bây giờ chúng ta đi vào vòng lặp chính của trò chơi.

Xin lưu ý rằng có rất nhiều mã trong một số danh sách tiếp theo, nhưng hầu hết trong số đó chỉ là bản soạn sẵn và không quan trọng để hiểu thuật toán tổng thể.

Trước tiên hãy thiết lập cấu trúc dữ liệu sơ bộ của chúng ta như bộ đệm phát lại.

Chúng tôi sẽ cần bộ đệm phát lại riêng cho đội một và đội hai.

Trên thực tế, chúng tôi sẽ cần hầu hết mọi thứ riêng biệt cho đội một và đội hai.

Liệt kê 9.19 khởi tạo các hành động.

Các biến trong danh sách 9.19 cho phép chúng ta theo dõi các số nguyên hành động có nghĩa là phần thưởng vectơ hành động trường và giá trị Q trạng thái tiếp theo cho mỗi tác nhân.

Để chúng tôi có thể gói những thứ này thành trải nghiệm và thêm chúng vào hệ thống phát lại trải nghiệm.

Trong danh sách 9.20, chúng tôi xác định một hàm để thực hiện các hành động thay mặt cho một nhóm tác nhân cụ thể và một hàm khác để lưu trữ các trải nghiệm trong bộ đệm phát lại.

Liệt kê 9.20 thực hiện một bước nhóm và thêm vào phần phát lại.

Hàm bước gạch dưới của nhóm là nơi làm việc của vòng lặp chính.

Chúng tôi sử dụng nó để thu thập tất cả dữ liệu từ môi trường và chạy DQN để quyết định những hành động cần thực hiện.

Hàm phát lại thêm dấu gạch dưới vào dấu gạch dưới lấy tenxơ trường trung bình hành động tensor quan sát tensor hành động tensor và tensor giá trị Q trạng thái tiếp theo, đồng thời thêm từng trải nghiệm tác nhân riêng lẻ vào bộ đệm phát lại riêng biệt.

Phần còn lại của mã đều nằm trong một vòng lặp while khổng lồ nên chúng ta sẽ chia nó thành nhiều phần nhưng chỉ cần nhớ rằng tất cả đều là một phần của cùng một vòng lặp.

Ngoài ra, hãy nhớ rằng tất cả mã này đều nằm trong sổ ghi chép Jupyter trên trang GitHub của cuốn sách này tại liên kết này.

Nó chứa tất cả mã mà chúng tôi sử dụng để tạo hình ảnh trực quan và nhiều nhận xét hơn.

Cuối cùng chúng ta cũng đến được vòng huấn luyện chính của thuật toán trong danh sách 9.21.

Liệt kê 9.21 vòng lặp huấn luyện.

Vòng lặp while chạy cho đến khi trò chơi chưa kết thúc.

Trò chơi kết thúc khi tất cả các đặc vụ trong một đội chết trong chức năng bước gạch dưới của đội.

Trước tiên, chúng ta lấy tensor quan sát và tập hợp phần mà chúng ta muốn như đã mô tả trước khi tạo ra tensor 13 x 13 x 2.

Chúng tôi cũng nhận được IDS gạch dưới một chỉ số dành cho các đặc vụ vẫn còn sống trong nhóm một.

Chúng ta cũng cần có được vị trí tọa độ của từng đặc vụ trong mỗi đội.

Sau đó, chúng tôi sử dụng chức năng suy luận hành động gạch dưới để chọn hành động cho từng tác nhân và khởi tạo chúng trong môi trường, rồi cuối cùng thực hiện một bước môi trường sẽ tạo ra các quan sát và phần thưởng mới.

Hãy tiếp tục trong vòng lặp while.

Liệt kê 9.22 việc thêm vào bản phát lại vẫn nằm trong vòng lặp while từ danh sách 9.21.

Trong phần cuối cùng của mã này, tất cả những gì chúng ta làm là thu thập tất cả dữ liệu vào một bộ dữ liệu và thêm nó vào bộ đệm phát lại trải nghiệm để đào tạo.

Điểm phức tạp của tác nhân M là số lượng tác nhân giảm dần theo thời gian khi chúng chết.

Vì vậy, chúng tôi cần thực hiện một số công việc quản lý mảng của mình để đảm bảo rằng chúng tôi luôn khớp dữ liệu với các tác nhân phù hợp theo thời gian.

Nếu bạn chạy vòng huấn luyện chỉ trong một số ít sử thi, các đặc vụ sẽ bắt đầu thể hiện một số kỹ năng trong trận chiến vì chúng tôi đã tạo lưới rất nhỏ

và chỉ có 16 đặc vụ trong mỗi đội.

Bạn có thể xem video về trò chơi đã ghi bằng cách làm theo hướng dẫn tại liên kết này.

Bạn sẽ thấy các đặc vụ tấn công lẫn nhau và nếu bạn bị giết trước khi video kết thúc, hình 9.27 là ảnh chụp màn hình ở cuối video của chúng tôi cho thấy rõ ràng một trong các đội đã đánh bại đội kia bằng cách tấn công họ vào một góc.

Hình 9.27 ảnh chụp màn hình của trò chơi chiến đấu với đặc vụ M sau khi huấn luyện với trường Q trung bình khi biết được đội bóng tối đã ép đội ánh sáng vào góc và tấn công họ.