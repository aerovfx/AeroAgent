# 7 -DQN trong Python (phần 2) đã dịch

---

Được rồi, trong video này chúng ta sẽ tiếp tục tập lệnh học sâu về hàng đợi cho Cartpool.

Vì vậy, trong bài giảng này, chúng ta sẽ tiếp tục phần chúng ta đã dừng lại, phần chúng ta sắp triển khai

vòng đào tạo.

Vì vậy, nó sẽ bắt đầu bằng cách khởi tạo danh sách của chúng tôi để lưu trữ kết quả.

Vì vậy, đó là tập, lợi nhuận, danh sách trống và tổn thất, danh sách trống.

Và sau đó chúng ta sẽ bắt đầu tính xem mọi thứ diễn ra trong bao lâu.

Và bước tiếp theo là thiết lập lại môi trường.

Vì vậy, quan sát ban đầu, đừng quan tâm đến thông tin.

Và cái này bằng với envis.reset và chúng ta sẽ chuyển hạt giống vào.

Và chúng tôi cũng cần mảng tự động đặt lại, mảng này sẽ cho chúng tôi biết khi nào mỗi môi trường được

tự động thiết lập lại.

Được rồi, vậy là đúng.

Được rồi, bây giờ chúng ta sẽ đi vào vòng lặp chính.

Vì vậy, đó là bước tổng thể trong phạm vi, tổng số bước thời gian.

Và khi đã vào đây, chúng ta sẽ bắt đầu phát tập phim ngay lập tức.

Vì vậy, chúng tôi sẽ chọn một hành động dựa trên epsilon tham lam.

Vì vậy, điều này có một chút khác biệt.

Vì vậy, trước tiên chúng ta cần lấy epsilon từ hàm epsilon của mình.

Vậy epsilon bằng lịch trình tuyến tính.

Và sau đó chúng tôi chuyển vào tất cả các tham số.

Vì vậy, thời gian bắt đầu và khám phá cũng như bước toàn cầu.

Và nó cũng điền vào vài dòng tiếp theo.

Được rồi, đây là những đầu vào của lịch trình tuyến tính, phải không?

Vậy đầu vào thứ ba là bao nhiêu bước và đầu vào thứ tư là bước hiện tại.

Được rồi.

Vì vậy, nếu các số ngẫu nhiên nhỏ hơn epsilon, chúng ta sẽ chọn một hành động ngẫu nhiên cho mỗi số

của các môi trường.

Được rồi, phần này cũng giống như phần trước.

Ngược lại, chúng ta sẽ nhận được các giá trị Q từ mạng nơ-ron.

Vì vậy, mạng Q.

Và bây giờ chúng tôi có hai mạng.

Vì vậy, đó là mạng mục tiêu hoặc mạng Q.

Nhưng đối với điều này, nó sẽ là mạng Q.

Vì vậy, đây là những gì trong bài giảng lý thuyết, chúng tôi gọi là mạng trực tuyến.

Vậy đó là mạng Q.

Và sau đó chúng ta phải chuyển đổi quan sát thành tensor ngọn đuốc trước khi chuyển nó vào.

Được rồi, và từ đây, hành động là argmax trên các giá trị Q.

Vì vậy, các hành động bằng torch dot argmax của giá trị Q trên chiều thứ hai.

Vì vậy, thứ nguyên đầu tiên là kích thước lô hoặc số lượng môi trường chúng ta có.

Vì vậy, nó được đề cập và sau đó đặt nó trở lại CPU.

Chuyển đổi thành mảng có nhiều mảng.

Được rồi.

Được rồi, từ đây, bây giờ chúng ta có hành động để có thể thực hiện một bước trong môi trường.

Được rồi, đó sẽ là phần thưởng quan sát tiếp theo.

Vì vậy, tôi vẫn gọi việc này là xong, mặc dù một số nguồn gọi nó là đã bị cắt bỏ.

Và sau đó chúng tôi đã cắt ngắn và thông tin.

Đây là hành động trong bước chấm v.

Hoặc đó phải là env.

Được rồi.

Vì vậy, bước tiếp theo là kiểm tra xem chúng tôi đã hoàn thành bất kỳ tập nào chưa và sau đó lưu những kết quả đó vào

danh sách các tập phim sẽ được vẽ sau.

Vì vậy, nó ghi lại lợi nhuận cho việc vẽ đồ thị và in ấn.

Được rồi, nó sẽ dành cho tôi.

Vì vậy, đây chỉ là chỉ mục và sau đó chúng tôi đã thực hiện việc cắt ngắn trong phần liệt kê và sau đó chúng tôi sẽ

lặp qua cả phần đã hoàn thành và phần bị cắt bớt cùng nhau.

Được rồi, vậy là chúng ta đã hoàn thành hoặc cắt bớt.

Vì vậy, tập phim đã kết thúc vì đó là tập phim hoặc chỉ đạt đến mức tối đa

số bước, có nghĩa là nó bị cắt ngắn.

Vậy là dù thế nào thì tập phim cũng đã kết thúc.

Vì vậy, lợi nhuận sẽ được lưu trữ ở đây.

Vì vậy, nó sẽ là tập của retinfo và nó ở phím R và sau đó sẽ là I.F. mục.

Và sau đó chúng tôi thêm vào phần trả về của tập.

Vì vậy, hãy thêm lưu kết quả trả về và sau đó chúng tôi sẽ in kết quả của mình.

Vì vậy chúng ta sẽ in ra bước này.

Bước hiện tại sẽ là bước toàn cầu.

Sự trở lại sẽ là sự trở lại và sau đó chúng tôi cũng muốn biết chúng tôi đang ở tập nào.

Vì vậy, tập phim bằng với độ dài của tập phim quay lại.

Được rồi.

Vậy đó là chuỗi và sau khi hoàn thành chuỗi đó, chúng ta có thể ký vào quan sát tiếp theo

đến quan sát hiện tại.

Vì vậy, một lần nữa, đừng quên điều này.

Mặc dù mọi thứ đang trở nên phức tạp, bạn vẫn cần dòng này.

Được rồi.

Và sau đó chúng tôi cũng phải cập nhật tự động thiết lập lại.

Vì vậy, đó sẽ là tự động thiết lập lại bằng logic hoặc giữa các duns và bị cắt bớt.

Được rồi.

Vì vậy, phần này là phần mà bạn sẽ muốn chú ý vì đây là nơi

chúng tôi thực hiện việc đào tạo.

Và có sự tinh tế cho điều này.

Rất dễ làm hỏng điều này nếu bạn bỏ lỡ một trong các chi tiết.

Vì vậy, trước tiên, hãy nhớ rằng chúng ta không luyện tập theo từng bước.

Chúng tôi đang thực hiện một số bước đầu tiên để thêm mẫu vào bộ đệm phát lại và chỉ thực hiện ngẫu nhiên

hành động.

Vì vậy, chúng tôi sẽ thực hiện nếu bước chung lớn hơn num bước trước khi đào tạo.

Và vì vậy hãy xem liệu điều này có đúng cho đến nay không.

Không, điều này không đúng.

Ồ, chúng tôi đã quên một cái gì đó.

Được rồi.

Thực ra, điều này làm tôi nhớ đến điều gì đó.

Vì vậy, điều này không đúng, nhưng chúng ta đã quên cập nhật bộ đệm phát lại ở đây.

Được rồi.

Vì vậy, chúng tôi sẽ làm điều đó bây giờ.

Vì vậy, đối với tôi và phạm vi tê liệt và Vs.

Được rồi.

Vì vậy, về cơ bản, đối với mỗi tập chưa kết thúc, chúng ta nên thêm phần chuyển tiếp này vào phần phát lại

bộ đệm.

Được rồi.

Vậy nếu không auto reset I thì có nghĩa là ở tập trước nó chưa kết thúc.

Và sau đó bạn nên quay lại bài giảng nơi chúng tôi đã giải thích cách hoạt động của tính năng tự động thiết lập lại.

Để hiểu tại sao điều này lại đến trước điều này.

Vậy nếu không auto reset I thì ta nên lưu trữ.

Vâng, điều đó không đúng.

Được rồi.

Vì vậy, RB dot store, đề xuất lần này phần lớn là đúng.

Vì vậy, điều này gần như đúng ngoại trừ nếu nó bị cắt bớt, chúng tôi vẫn muốn đưa vào phần tiếp theo

trạng thái trong tính toán.

Vì vậy, duns sẽ dùng để che dấu khi chúng ta tính toán mục tiêu.

Được rồi.

Và vì vậy bạn sẽ nhận thấy rằng có một chút khác biệt ở đây giữa cách thức này

được cấu trúc so với cách mã được cấu trúc khi tôi giới thiệu bộ đệm phát lại.

Vì vậy, khi tôi giới thiệu bộ đệm phát lại, điều tôi đã làm là nói rằng chúng ta có hai vòng lặp for riêng biệt.

Vì vậy, một vòng lặp for là để đào tạo và một vòng lặp for là để thu thập kinh nghiệm

thực hiện các hành động ngẫu nhiên.

Tuy nhiên, như bạn có thể thấy ở đây, chúng ta chỉ có một vòng lặp và sau đó chúng ta chỉ nói nếu hiện tại của chúng ta

bước thời gian lớn hơn số bước thời gian để thu thập tất cả dữ liệu này thì hãy sử dụng

để quyết định có nên đào tạo hay không.

Vì vậy, nó gần giống nhau ngoại trừ việc bạn chỉ ghép hai vòng lại với nhau.

Và điều này cũng có nghĩa là tổng số bước thời gian dành cho đào tạo của chúng tôi cũng bao gồm các bước thời gian này

chỉ là thu thập dữ liệu.

Vì vậy, nó hơi khác một chút so với cách tôi đã giới thiệu trước đây nhưng về cơ bản nó là

giống nhau, chỉ khác về cấu trúc.

Và vì vậy, có một sự khác biệt tinh tế mà tôi muốn chỉ ra, đó là sự khác biệt

out trong trường hợp này không thành vấn đề nhưng cá nhân tôi muốn nó theo cách khác.

Vì vậy, khi chúng tôi thực hiện Epsilon Gritty, khi chúng tôi thu thập dữ liệu, chúng tôi không thực hiện Epsilon Gritty, chúng tôi chỉ

thực hiện những hành động hoàn toàn ngẫu nhiên.

Nhưng đối với những gì chúng tôi đang làm ở đây, chúng tôi đang nói rằng mặc dù chúng tôi đang thu thập dữ liệu và chỉ

điền vào bộ đệm phát lại, chúng ta sẽ vẫn sử dụng chiến lược Epsilon Gritty này, chiến lược này

là ngẫu nhiên vì mạng Q là ngẫu nhiên nhưng có thể có vấn đề với mạng Q.

Nó có thể dựa trên các giá trị trong mạng Q.

Vì vậy, dựa trên các giá trị đó, có thể luôn xuất ra 1 hoặc luôn xuất ra 0.

Vì vậy, nó không thực sự ngẫu nhiên.

Vì vậy, đó là lý do tại sao nếu tôi cố gắng cải thiện điều này một chút, tôi sẽ nói như vậy đối với những người

khoảng 5.000 bước đầu tiên, chỉ đi qua nhánh này nơi chúng tôi lấy mẫu các hành động ngẫu nhiên.

Nhưng vì tính năng này vẫn đang hoạt động nên tôi sẽ không thay đổi nó.

Vì vậy, bây giờ chúng ta sẽ quay lại vòng lặp đào tạo hoặc phần của vòng lặp nơi chúng ta thực hiện đào tạo.

Vì vậy bây giờ chúng ta sẽ lấy mẫu một lô từ bộ đệm phát lại.

Vì vậy, bây giờ chúng tôi không còn học hỏi từ quá trình chuyển đổi mới nhất nữa.

Vì vậy, bất kể điều này là gì, chúng tôi chỉ học từ những gì chúng tôi đã lấy mẫu từ bộ đệm phát lại.

Vì vậy, với torch.nodegrad, nó tương tự như những gì tôi có, nhưng tôi sẽ thay đổi nó một chút.

Vì vậy tôi sẽ nói mục tiêu tối đa, bỏ qua giá trị này.

Và nó sẽ là mạng mục tiêu, chuyển đổi trạng thái này sang trạng thái tiếp theo thành tensor ngọn đuốc.

Và sau đó chúng ta sẽ lấy giá trị tối đa, 10 bằng 1.

Vì vậy, lý do tại sao mã được đề xuất từ AI không chính xác là vì mức tối đa này có thể

trả lại hai thứ

Và sau đó chúng ta sẽ thực hiện mục tiêu TD.

Vì vậy, về cơ bản nó bằng r cộng gamma nhân q ở trạng thái tiếp theo và lấy giá trị tối đa.

Vì vậy, nó sẽ trông hơi lộn xộn một chút vì chúng ta phải làm tất cả các NP cho đuốc.

Nhưng hãy xem liệu những gì nó mang lại cho chúng ta có đúng không.

Vì vậy, chúng tôi có phần thưởng, chuyển đổi nó thành tensor ngọn đuốc, chúng tôi có mục tiêu cộng gamma lần

max, là giá trị lớn nhất trên q.

Và sau đó chúng ta có mặt nạ.

Vậy nó là 1 âm tấn.

Và vì vậy tôi sẽ thay đổi điều này một chút.

Tôi thích làm phẳng những thứ này.

Vì vậy tôi sẽ làm phẳng điều này.

Hãy chuyển dòng này sang dòng tiếp theo.

Rồi NP này để đuốc, mình sẽ để nó ở ngoài.

Và thế là bây giờ chúng ta có thêm 1 khung phụ.

Và sau đó tôi sẽ nói làm phẳng cái này hoặc không, xin lỗi, làm phẳng bên trong.

Được rồi, không.

Được rồi, bây giờ thì tốt rồi.

Và vì vậy bây giờ chúng ta cần hành động.

Bởi vì chúng ta sử dụng các thao tác để lập chỉ mục qs a.

Vì vậy, các hành động sẽ là NP đối với các hành động hàng loạt.

Và lần này chúng ta phải sử dụng lập luận này.

Vì vậy, nổi bằng sai.

Và vậy tại sao chúng ta cần điều này?

Bởi vì các hành động được sử dụng để lập chỉ mục đầu ra của mạng lưới thần kinh.

Vậy về cơ bản những cột nào của đầu ra?

Và vì vậy, khi chúng ta lập chỉ mục cho một mảng hoặc một tenxơ ngọn đuốc hình tròn, chúng ta không thể sử dụng các số float.

Chúng ta cần sử dụng số nguyên.

Đó là lý do tại sao chúng ta chuyển sai.

Vì vậy, nếu nó sai, chúng ta sẽ nhận được ngọn đuốc detype ở 64.

Và khi đó các hành động sẽ ở dạng 64 thay vì luồng 32.

ĐƯỢC RỒI.

Vì vậy, sau đó chúng tôi định hình lại các hành động.

Và nhân tiện, nếu bạn không chắc tại sao chúng ta cần những thứ này, thì rất dễ dàng để

nhận xét chúng và xem liệu nó có còn hoạt động không hoặc xem bạn gặp phải loại lỗi nào.

Tôi nghĩ hầu hết chúng đều cần thiết.

Một số trong số chúng có thể là thừa.

Nhưng bạn có thể tự kiểm tra nếu muốn.

ĐƯỢC RỒI.

Vì vậy, chúng ta cần trạng thái hiện tại.

Vậy đó là s.

Điều đó đúng.

Và sau đó chúng ta cần chuyển những thứ này qua mạng q.

Vì vậy, tôi sẽ thực hiện việc này theo từng bước.

Vì vậy tôi sẽ gọi đây là qsa.

Và sau đó nó sẽ chuyển s tới mạng q.

Tôi sẽ không thu thập nữa.

Và vì vậy tôi sẽ nhắc bạn điều chúng tôi thực sự muốn làm là chúng tôi muốn qsa.

Trong đó a là hành động được thực hiện, trong đó a là hành động được thực hiện.

Vì thế nó muốn.

Và cách chúng ta làm điều này, giả sử nếu chúng ta là một người khó tính, thì cú pháp sẽ là một cú pháp khó hiểu.

Vì vậy, vì chúng tôi có qs đầu ra từ mạng nên về cơ bản chúng tôi muốn lập chỉ mục mảng này.

Vì vậy, kích thước đầu tiên là kích thước lô.

Chiều thứ hai sẽ là tất cả các hành động.

Vì vậy, chúng tôi chỉ muốn chọn các cột tương ứng với các hành động chúng tôi đã thực hiện.

Vì vậy, đây là những gì chúng tôi muốn làm.

Nhưng điều này chỉ hoạt động với cú pháp khó hiểu.

Nhưng với PyTorch, chúng tôi làm như thế này.

Vì vậy, dự đoán bằng qsa.

Và chúng tôi gọi là tập hợp1a.

Và sau đó chúng ta sẽ nén cái này để loại bỏ các kích thước thừa.

Vì vậy, từ đây, chúng ta có mục tiêu và dự đoán của mình.

Vì vậy, tại thời điểm này, nó khá dễ dàng.

Vì vậy, chúng tôi có trận thua, trận thua f.mc, dự đoán mục tiêu.

Ban đầu tôi đã đặt cái này ở đây.

Nó không thực sự quan trọng, nhưng dù sao đi nữa.

Trên thực tế chúng ta hãy xem.

Tôi đã làm ngược lại trước khi tôi thay đổi lại.

Rõ ràng là cách nào cũng được.

Và sau đó chúng tôi nối thêm sự mất mát.

Vì vậy, chúng tôi thực hiện loss.item để nhận giá trị thực tế và thêm giá trị này vào khoản lỗ của chúng tôi.

Và sau đó chúng tôi thực hiện bước giảm độ dốc.

Vì vậy hãy tối ưu hóa mô hình.

Vì vậy, nó là 0 grad, loss.backward, hãy tối ưu hóa nó theo bước của chúng tôi.

ĐƯỢC RỒI.

ĐƯỢC RỒI.

Vì vậy bây giờ chúng ta sẽ in một số thứ ra.

Vì vậy, nếu bước chung ở bước thứ 1.000, chúng tôi sẽ in các bước mỗi giây.

Và đây chỉ là bước hiện tại chia cho thời gian đã trôi qua.

Vì vậy, thời gian hiện tại có thể có thời gian bắt đầu.

ĐƯỢC RỒI.

Và một điều nữa chúng tôi cần là chúng tôi muốn,

vì vậy đây chỉ là trong thời gian đào tạo.

Vì vậy, chúng tôi muốn cập nhật mạng mục tiêu.

Và chúng ta sẽ làm điều đó bằng cách nào

Để kiểm tra xem đó có phải là lần lặp lại hay không, chúng ta nên cập nhật mạng mục tiêu.

Vì vậy, chỉ có mỗi số bước này.

Và sau đó chúng ta sẽ nói, đối với tham số mạng mục tiêu, tham số mạng Q,

trong một zip.

Vâng.

Vì vậy, chúng tôi nén qua tất cả các tham số.

Mục tiêu tham số mạng, có thể tham số mạng.

Và sau đó ở đây, điều này có vẻ như sẽ đúng.

Vì vậy, đó là điểm sao chép tham số mạng mục tiêu.

Và sau đó chúng ta muốn sao chép giá trị gì?

Đó là tau lần các thông số mới.

Vậy đó là từ tham số mạng Q cộng 1 trừ tau nhân với tham số cũ.

Vì vậy, dữ liệu chấm tham số mạng mục tiêu.

ĐƯỢC RỒI.

Vì vậy, điều đó có vẻ đúng.

Và cuối cùng, điều tương tự như chúng ta đã có trong tập lệnh dòng Q trước đó.

Vì vậy, nếu chúng ta đạt được phần thưởng tối đa 10 lần liên tiếp,

chúng tôi sẽ coi đó là đủ tốt để bỏ thuốc lá.

Và một lần nữa, điều này là do việc đào tạo và học tập củng cố,

ngay cả dòng Q sâu cũng không ổn định.

Vì vậy, mọi thứ có thể sụp đổ nếu bạn tiếp tục.

Vì vậy, nếu chúng ta tìm thấy một bộ thông số phù hợp,

chúng ta sẽ thoát ra và sau đó đánh giá chúng.

Vì thế chúng ta sẽ nói, hãy giải lao thôi.

Chà, tôi sẽ không gõ cái này vì nó giống với những gì chúng ta đã có trước đây.

Vì vậy, nếu độ dài của tập đó lớn hơn 10,

vì vậy chúng tôi có ít nhất 10 cho đến nay.

Và 10 cuối cùng, vậy trừ 10 đến cuối, chúng đều bằng 500.

Vì vậy NP chấm tất cả.

Chúng tôi sẽ nói rằng phần thưởng tối đa đã đạt được và sau đó thoát ra khỏi vòng lặp for.

ĐƯỢC RỒI.

Vì vậy, hãy chạy cái này.

Vì vậy, như bạn có thể thấy, nó diễn ra khá nhanh, mặc dù chúng tôi đang sử dụng CPU.

ĐƯỢC RỒI.

Vậy là chúng ta đã đi được một nửa tổng số bước.

Vậy là khoảng 49, 50.000.

Chúng tôi đã nhận được 500 liên tiếp 10 lần.

Vì vậy, tại thời điểm này, chúng ta có thể đóng môi trường của mình.

Vì vậy, đóng ở V, ENV đóng dấu chấm.

Và sau đó một vài bước tiếp theo chỉ là lập sơ đồ.

Vì vậy, tôi sẽ sao chép nó từ những gì chúng ta đã có trước đây.

Vì vậy, chúng ta có chức năng làm mịn để làm mịn lợi nhuận.

Và sau đó chúng ta sẽ vẽ biểu đồ lợi nhuận liền mạch cùng với lợi nhuận thô thực tế.

Vì vậy, bạn có thể thấy ở đây.

Và tôi cũng thấy điều này khi nó đang được in ra.

Chúng tôi đã đạt gần 500 và sau đó nó giảm xuống rồi lại tăng lên.

ĐƯỢC RỒI.

Vì vậy, đó chính xác là những gì chúng ta đang thấy trong tập phim trở lại.

ĐƯỢC RỒI.

Nhưng cũng để ý, nó kết thúc nhanh hơn.

Và trung bình nó sẽ hoàn thành nhanh hơn khi bạn chạy đi chạy lại với DQN

so với việc chỉ học Q đơn giản.

ĐƯỢC RỒI.

Và sau đó chúng ta sẽ tính toán tổn thất của mình.

Vì vậy, có vẻ như số thua lỗ đã tăng lên vào thời điểm mà hiệu suất đang giảm xuống.

Vì vậy, nó có phần hữu ích để xem xét.

Nhưng nó sẽ không giống như cách học có giám sát và không giám sát.

ĐƯỢC RỒI.

Vì vậy, bây giờ các tổng đài viên đã hoàn tất đào tạo, chúng ta sẽ thực hiện tất cả các bước tương tự để đánh giá

mô hình và làm tất cả những thứ đó.

Vì vậy, chúng ta sẽ lưu mô hình, tải lại nó, tạo một môi trường mới, v.v.

Vì vậy hãy lưu mô hình.

Vì vậy, đường dẫn mô hình bằng DQN cartpold.pth.

Ngoài ra, tôi khuyên bạn nên sử dụng các đường dẫn khác nhau cho mô hình và video.

Vậy là nó đã ở trên này.

Vì vậy, cái này, tôi cho rằng chúng ta cũng có thể đặt cái này lên đó, nhưng nó không thành vấn đề.

Vì vậy, tôi khuyên bạn nên sử dụng các đường dẫn khác nhau cho tất cả những điều này vì rất có thể đối với khóa học này,

bạn sẽ đặt tất cả những thứ này vào cùng một thư mục và bạn không muốn chúng ghi đè lên

lẫn nhau khi bạn đang thực hiện khóa học này.

Vì vậy, chúng ta sẽ thực hiện torch.save, mạng Q, nợ trạng thái và sau đó là đường dẫn mô hình.

ĐƯỢC RỒI.

Được rồi.

Và bây giờ chúng ta sẽ tải mô hình và tạo môi trường thử nghiệm.

Vì vậy hãy tải mô hình.

Mô hình cho eval cộng với tạo môi trường thử nghiệm.

Vì vậy, chúng tôi sẽ gọi đây là đánh giá ENV.

Vì vậy, hãy là một môi trường vector.

Và chúng ta sẽ chỉ tạo một môi trường cho việc này.

Và chúng tôi xác nhận là đúng vì chúng tôi muốn quay video.

ĐƯỢC RỒI.

Vì vậy, nó sẽ là mô hình bằng mạng Q.

Điều đó có vẻ đúng ngoại trừ việc chúng tôi sẽ nói vị trí trên bản đồ.

Ồ, không, nó ở trong này.

Vị trí bản đồ bằng thiết bị.

Và điều này sẽ tạo thành chữ V hoặc tạo thành chữ V.

Và sau đó chúng ta cũng sẽ đưa mô hình vào chế độ eval.

ĐƯỢC RỒI.

Vì vậy bây giờ chúng ta có thể đánh giá mô hình.

Đánh giá mô hình.

Vì vậy, điều này phần lớn sẽ giống như lần trước.

ĐƯỢC RỒI.

Chúng tôi có 10 tập để đánh giá.

Chúng tôi sẽ tạo một mảng trả về và tập trống.

Đánh giá.

Vì vậy bây giờ chúng ta thiết lập lại môi trường.

Vậy là được rồi.

Đừng quan tâm.

ENV eval.reset.

Và sau đó chúng tôi lặp lại từng tập phim.

Vậy đối với tôi trong phạm vi và các tập đánh giá, tại sao nó lại biến mất?

ĐƯỢC RỒI.

Vì vậy, bây giờ chúng ta có một tập cờ được thực hiện bằng sai.

Và sau đó trong khi chưa hoàn thành tập phim.

Vì vậy, chúng tôi sẽ sử dụng mạng Q để xác định hành động nào chúng tôi nên thực hiện.

Vì vậy, chúng tôi sẽ nói giá trị Q.

Hãy xem điều này có đúng không.

Vâng, nhấn quan sát.

Nhận hành động bằng cách thực hiện tối đa.

Và sau đó nhận được trạng thái tiếp theo cũng như tất cả phần thưởng và nội dung.

ĐƯỢC RỒI.

Vì vậy, một lần nữa, bạn có thể nói các hoạt động tiếp theo ở đây.

Và sau đó chỉ định các hoạt động tiếp theo cho các hoạt động.

Nhưng vì chúng ta không cần sử dụng biến này nữa nên

chúng ta có thể chỉ định trực tiếp điều này cho ops.

ĐƯỢC RỒI.

Vì vậy, khi thực hiện xong hành động, chúng ta có thể lưu trữ phần thưởng.

Vì chúng ta chỉ có một môi trường,

chúng ta chỉ có thể kiểm tra giá trị đầu tiên.

Vì vậy, đừng ở mức 0.

Tự động hoàn thành biến mất.

Và điều đó không đúng.

Bị cắt bớt 0.

Đặt quay lại thông tin là ở đây.

Hãy xem điều đó có đúng không.

Vì vậy, dường như đây luôn là lần đầu tiên nó gợi ý điều gì đó.

Điều đó đúng.

Và sau đó tôi sẽ gõ một cái gì đó.

Hoặc tôi sẽ đợi quá lâu và nó sẽ biến mất.

Và lần tự động hoàn thành tiếp theo còn tệ hơn lần đầu tiên.

Đó là lý do tại sao tôi không giữ chúng.

ĐƯỢC RỒI.

Vì vậy, chúng tôi nhận được lợi nhuận.

Chúng tôi lưu nó để đánh giá lợi nhuận.

Chúng tôi in ra kết quả.

Và chúng tôi lưu một việc làm là đúng.

Vì vậy, điều đó có vẻ đúng.

Và sau khi chúng ta làm xong mọi việc,

chúng tôi đóng cửa môi trường.

Đóng lại sự ghen tị.

Env là e-bow.close.

ĐƯỢC RỒI.

Vì vậy, hãy chạy cái này.

Chuyện gì đã xảy ra thế?

Env là ồ, tôi hiểu rồi.

Tôi đã tự hỏi tại sao điều đó được gạch chân.

ĐƯỢC RỒI.

Chạy lại lần nữa.

ĐƯỢC RỒI.

Vì vậy, tôi nhận ra AI đã gợi ý điều gì đó không đúng, điều đó

đó là lý do tại sao bạn vẫn phải biết cách viết mã trong thời đại AI.

Việc này có nên kết thúc hay không.

ĐƯỢC RỒI.

Vì vậy, hãy chạy lại cái này.

ĐƯỢC RỒI.

Vì vậy, điều này khá được mong đợi vì mô hình đã hoạt động khá tốt khi chúng tôi dừng hoạt động.

ĐƯỢC RỒI.

Vì vậy, một lần nữa, không thực sự quá sâu sắc để vẽ biểu đồ lợi nhuận.

Nhưng nếu bạn nhận được lợi nhuận khác nhau,

thì nó sẽ có ích.

Và đây là eval trả về tất cả 500.

Và chúng ta cũng có thể xem một đoạn video.

Chỉ cần lấy bất cứ ai.

Ở đây, lần này chúng ta sẽ chọn năm.

Và chúng ta sẽ xem mô hình hoạt động như thế nào.

ĐƯỢC RỒI.

Vậy là nó đang trôi dạt sang một bên.

Nhưng nó làm việc đó chậm đến mức nó vẫn còn

có thể đạt được 500 bước.

ĐƯỢC RỒI.

Vậy đó là DQN cho nhóm thẻ.