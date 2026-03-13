# 6 -DQN trong Python (phần 1) đã dịch

---

Được rồi, trong video này chúng ta sẽ xem xét cách triển khai deep queue learning cho

carpool.

Được rồi, tôi sẽ bắt đầu bằng cách sao chép nội dung nhập giống như chúng ta đã làm trước đây.

Thật ngẫu nhiên, bạn biết đấy, đó là lúc để tính thời gian bạn bước đi, tập thể dục, tập thể dục, tập luyện,

lib và PyTorch.

Nhân tiện, đây là một bài tập tốt, bạn muốn làm gì trước khi xem video này

bài giảng là giải quyết các kịch bản học tập hàng đợi thông thường và sau đó sửa đổi nó để triển khai

học hàng đợi sâu.

Được rồi, vậy bạn có thể coi đây là giải pháp cho bài tập đó.

Vì vậy, nếu bạn chưa thử tự mình triển khai deep queue learning dựa trên những gì bạn

đã học trong phần này, tôi khuyên bạn nên thử trước khi xem phần này.

Được rồi, tiếp theo chúng ta có tất cả các cài đặt.

Và một lần nữa, tôi sẽ không gõ cái này chỉ vì nó khá tầm thường.

Vì vậy, tôi sẽ chỉ giải thích từng thứ này là gì.

Vì vậy, trong VID, chúng ta đã có điều đó trước đó sẽ là cartpool, numpy và v's.

Một lần nữa, đó sẽ là tổng cộng một bước thời gian.

Chúng ta sẽ giữ nguyên 100.000 đó.

Tỷ lệ học tập.

Vì vậy, đây là tốc độ học tập cho trình tối ưu hóa nguyên tử.

Vì vậy, điều đó cũng giống nhau.

Vì vậy phần này mới.

Vì vậy, chúng tôi có kích thước bộ đệm.

Vì vậy, kích thước của bộ đệm phát lại.

Tôi đã chọn ngẫu nhiên 10.000.

Bạn có thể chơi với các giá trị khác nếu bạn thích.

Chúng tôi có hệ số chiết khấu giống như trước đây.

Và điều tiếp theo là mới.

Vì vậy, đó là hằng số cập nhật mạng mục tiêu mà chúng tôi gọi là tau.

Vì vậy, bạn sẽ nhận thấy tau đó, chúng tôi đang đặt nó thành một trong mã này.

Và điều đó có nghĩa là gì?

Vì vậy, điều đó có nghĩa là nếu đây là một, chúng tôi luôn sử dụng theta, đó là theta trực tuyến, và

thì một trừ một bằng không.

Vì vậy, chúng tôi không sử dụng bất cứ thứ gì từ mạng mục tiêu cũ.

Được rồi.

Vì vậy, mặc dù chúng tôi có thể kết hợp cả hai trong kịch bản cụ thể này, nhưng chúng tôi chỉ

sẽ lấy bất cứ thứ gì có trong mạng trực tuyến.

Và chúng tôi cũng có một số bước thời gian giữa mỗi lần cập nhật mạng mục tiêu.

Vì vậy, chúng tôi sẽ chỉ sao chép qua mạng trực tuyến sang mạng mục tiêu sau mỗi 50 bước.

Được rồi.

Vì vậy, tiếp theo chúng ta có kích thước lô.

Vì vậy, điều này cũng mới.

Cần lấy bao nhiêu mẫu hoặc bao nhiêu lần chuyển tiếp để lấy mẫu từ bộ đệm phát lại mỗi lần chúng tôi

thực hiện một bước giảm độ dốc?

Được rồi.

Và chúng ta có một số thông số cho epsilon đang phân hủy.

Vì vậy, giá trị bắt đầu của chúng tôi sẽ là một.

Vì vậy, chúng ta sẽ khám phá 100% thời gian và sau đó chúng ta sẽ giảm tuyến tính xuống 0,01, tức là

1%.

Và vì vậy khi kết thúc khóa đào tạo, chúng ta sẽ khám phá 1% thời gian.

Được rồi.

Và cần bao nhiêu bước để bắt đầu epsilon đến kết thúc epsilon.

Chúng tôi chỉ đặt con số đó là 10% trong tổng số bước thời gian.

Vậy tổng số bước thời gian là 100.000.

Và 10% trong số đó sẽ là 10.000.

Và để ý rằng do trùng hợp thôi, bạn không cần phải làm như thế này, nhưng đó là cách

Tôi đã làm nó.

Tôi đã thiết lập điều đó.

Nó sẽ giống với kích thước bộ đệm.

Được rồi.

Vì vậy, chúng ta có một số bước trước khi bắt đầu đào tạo.

Vì vậy tôi đã đặt giá trị này là 5.000.

Vậy điều này có nghĩa là gì?

Vì vậy, hãy lưu ý rằng chúng tôi bắt đầu đào tạo sau 5.000 bước, nhưng số lần chuyển đổi sang lưu trữ

trong bộ đệm phát lại là 10.000.

Vì vậy, chúng tôi thậm chí sẽ không đợi trước khi bộ đệm đầy để bắt đầu đào tạo.

Vì vậy, nó sẽ đầy một nửa khi chúng tôi bắt đầu huấn luyện mạng.

Được rồi.

Và chúng ta cũng không muốn luyện tập theo từng bước.

Vì vậy, tần số tàu của chúng tôi chúng tôi cho.

Vì vậy, cứ bốn lần tương tác với môi trường sẽ lấy mẫu một lô từ bộ đệm phát lại và

sau đó đào tạo về điều đó.

Được rồi.

Và một lần nữa, tôi đặt C thành không.

Bạn biết tại sao không?

Đó là vì tôi muốn tập lệnh này mạnh mẽ và không chỉ hoạt động với một hạt giống cụ thể.

Và sau đó chúng ta có đường dẫn video nơi chúng ta sẽ lưu trữ các video đó.

Được rồi.

Vì vậy, hãy chạy cái này và chạy cái này.

Được rồi.

Và tiếp theo chúng ta có hàm tạo và hàm V.

Vì vậy, tôi sẽ sao chép và dán lần này vì nó giống hệt lần trước.

Vì vậy, chúng ta có đối số video quay và đối số hạt giống.

Và nếu quay video đúng thì chúng ta có chế độ kết xuất dưới dạng mảng RGB.

Chúng tôi bọc nó trong giấy gói video ghi lại.

Và sau đó chúng ta có số liệu thống kê về các tập kỷ lục.

Hãy nhớ rằng, như bạn đã biết, trả về kết quả ở cuối tập.

Và sau đó, tùy ý, chúng ta có thể đặt hạt giống cho lấy mẫu hành động.

Được rồi.

Vì vậy, hãy chạy cái này.

Được rồi.

Vậy là mạng Q cũng như trước.

Được rồi.

Vậy là chúng ta vẫn có một Feed Fordner đang làm việc với 128 đơn vị ẩn.

Vì vậy, điều này là hoàn toàn giống nhau.

Được rồi.

Vì vậy, tiếp theo chúng ta sẽ có một chức năng mới.

Và chức năng này sẽ dùng để trả về epsilon.

Được rồi.

Vì vậy, về cơ bản nó chỉ lấy mã này từ mã hiện có của tôi.

Vì vậy, tôi thực sự không cần phải gõ bất cứ điều gì.

Tôi sẽ giải thích nó.

Vì vậy, chúng ta có giá trị bắt đầu của epsilon, giá trị kết thúc của epsilon, tổng thời lượng,

và bước thời gian hiện tại t.

Như bạn đã biết, về cơ bản đây là một đường cong khúc côn cầu.

Phải.

Vì vậy, nó là một đường tuyến tính đi xuống mức tối thiểu và sau đó nó duy trì ở mức tối thiểu mãi mãi.

Vậy chúng ta thực hiện điều đó như thế nào?

Vì vậy, sẽ rất hữu ích khi nghĩ về phương trình của một đường thẳng.

Vì vậy, đường thẳng có độ dốc nhân với đầu vào cộng với điểm chặn.

Vì vậy, phần đánh chặn là epsilon bắt đầu.

Và rồi con dốc sẽ đưa chúng ta đi xuống theo từng bước thời gian.

Và vậy chúng ta nên đi xuống bao nhiêu?

Đó sẽ là epsilon trừ bắt đầu epsilon.

Vì vậy, tổng khoảng cách từ trên xuống dưới, chia cho thời lượng, là chiều ngang

chiều dài.

Phải.

Vì vậy, nó tăng hơn chạy.

Vậy chiều dài theo chiều dọc chia cho chiều dài ngang.

Và đó là độ dốc.

Được rồi.

Vậy điều đó có ý nghĩa gì?

Vì vậy, nếu bạn nghĩ về giá trị ở cuối, thì ở cuối, t sẽ bằng thời lượng,

hoặc xin lỗi, không phải ở cuối, mà là ở cuối epsilon đang phân hủy.

Vì vậy, t sẽ bằng thời lượng.

Vậy bạn sẽ có thời lượng ở đây nhân với cái này ở trên này.

Vì vậy, thời lượng ở đây là ở phía dưới.

Vì vậy, khoảng thời gian sẽ bị hủy bỏ và sau đó bạn có kết thúc trừ bắt đầu cộng với bắt đầu.

Vì vậy, n trừ bắt đầu cộng với bắt đầu, số lần bắt đầu hủy bỏ.

Và sau đó bạn chỉ kết thúc với end.

Vì vậy, đó sẽ là giá trị cuối cùng ở cuối dòng đó.

Và nếu bạn tiếp tục, thì t lớn hơn thời lượng, nên cái này sẽ nhỏ hơn epsilon cuối.

Và đó là lý do tại sao chúng tôi lấy mức tối đa vì chúng tôi muốn có epsilon tối thiểu

được kết thúc epsilon.

Được rồi.

Vì vậy, hãy chạy cái này.

Và sau đó chúng ta tạo ra vector env.

Vì vậy, điều này cũng giống như trước đây.

Vì thế tôi sẽ không giải thích nó nữa.

Và sau đó chúng tôi đã thiết lập thiết bị.

Hãy xem liệu nó có tự động hoàn thành cho tôi không.

Bây giờ nó không tự động hoàn thành lần này.

Thực sự ngọn đuốc.

Thiết bị đó.

Không.

Được rồi.

Chúng ta sẽ sao chép nó vào.

Vì vậy, thiết bị.

Điều này cũng giống như trước đây.

Vì vậy, một lần nữa, tôi nghĩ việc sử dụng CPU cho những môi trường nhỏ hơn này sẽ dễ dàng hơn.

Được rồi.

Vì vậy, tiếp theo chúng ta có mạng lưới thần kinh.

Vì vậy hãy tạo ra mạng lưới thần kinh.

Vì vậy, lần này, trước đây chúng tôi chỉ phải tạo một mạng vì chúng tôi chỉ có mạng Q.

Nhưng bây giờ chúng tôi có hai.

Chúng tôi có mạng Q, là mạng trực tuyến.

Và sau đó là mạng mục tiêu, là bản sao của mạng đó.

Vì vậy, chúng tôi sẽ nhấn enter để thực hiện việc này.

Chúng tôi chưa kết thúc.

Thêm những gì chúng ta cần thêm.

Vì vậy, với mạng Q, đây là thứ chúng tôi sẽ cập nhật.

Chúng tôi cần trình tối ưu hóa của chúng tôi.

Được rồi.

Vậy điều đó có đúng không?

Vâng, điều đó đúng.

Vì vậy, chúng tôi chuyển vào các tham số và sau đó là tốc độ học tập.

Và đối với mạng mục tiêu, chúng tôi muốn biến mạng này thành bản sao của mạng chính.

Vì vậy, chúng tôi đi đến mạng mục tiêu, tải trạng thái dict.

Phải?

Đó là cách Pie Torch thực hiện.

Mọi thứ đang tải.

Vì vậy, tải trạng thái dict và trạng thái dấu chấm.

Vì vậy, lệnh trạng thái chấm sẽ trả về một lệnh của các tham số và sau đó tải lệnh trạng thái.

Lấy các tham số đó và đặt chúng vào mạng riêng của nó.

Được rồi.

Vì vậy, sao chép chính vào mục tiêu.

Vì vậy, hãy chạy cái này.

Vì vậy, điều này sẽ mất một thời gian.

Vì vậy, tiếp theo tôi sẽ sao chép bộ đệm phát lại mà bạn đã thấy trong phần

bài giảng.

Vì vậy tôi đã giải thích cách thức hoạt động của nó.

Vì thế tôi sẽ không làm điều đó nữa.

Nhưng hãy thoải mái kiểm tra nó nếu bạn thích.

Và khi tự mình thực hiện điều này, bạn có thể đã sử dụng điều này.

Bạn cũng có thể sử dụng phương pháp danh sách Python.

Hoặc là sẽ ổn thôi.

Nhưng tôi nghĩ điều này sẽ hiệu quả hơn một chút.

Được rồi.

Vì vậy, chúng tôi tạo một phiên bản của bộ đệm phát lại.

Và bây giờ chúng ta cần một hàm trợ giúp nhỏ để chuyển đổi một mảng có nhiều mảng thành các tensor ngọn đuốc.

Vì vậy, chúng ta sẽ gọi cái này là numpy to torch trong bất kỳ mảng nào a.

Và điều này sẽ khác một chút so với trước đây vì tôi muốn sử dụng điều này theo nhiều cách

kịch bản.

Vì vậy, tôi sẽ có một đối số để float bằng true.

Được rồi.

Vì vậy, nếu float là đúng thì chúng ta sẽ đặt loại d thành torch.flow32.

Nếu không thì nó không tự động thụt lề đối với tôi.

Nếu không, chúng tôi sẽ đặt loại d thành dấu chấm đuốc ở 64.

Được rồi.

Và sau đó chúng tôi sẽ trả lại mã giống như trước.

Vậy dấu chấm đuốc dưới dạng tensor, truyền vào mảng a rồi kiểu d là kiểu d và thiết bị

thiết bị.

Được rồi.

Vì vậy, đó là chức năng trợ giúp của chúng tôi để chuyển đổi các mảng có nhiều mảng thành các tensor ngọn đuốc.

Được rồi.

Vì vậy, vì bài giảng này đã khá dài nên chúng ta sẽ dừng ở đây.

Và phần tiếp theo chúng ta sẽ tiếp tục với vòng lặp huấn luyện.

Được rồi.

Nhưng nếu bạn chưa tự mình thực hiện điều này, vui lòng lấy những gì chúng tôi có.

xa và cố gắng tự mình thực hiện phần còn lại bằng cách sử dụng những gì chúng ta đã học.