# 4 -Policy gradient Methods (phần 3) đã dịch

---

Được rồi, trong video này chúng ta sẽ tiếp tục tìm ra thuật toán gradient chính sách.

Vì vậy, trước đây chúng ta đã xem xét cách tính gradient của vật kính, ở một mức độ nào đó.

Và điều chúng tôi muốn làm là tiếp tục làm điều đó.

Vì vậy, chúng ta có thể đặt mục tiêu theo những thuật ngữ mà chúng ta thực sự biết cách tính toán.

Được rồi, vậy những gì chúng ta có cho đến nay là độ dốc của mục tiêu đối với các tham số theta.

Đây là giá trị mong đợi của độ dốc của log xác suất của một số quỹ đạo omega,

đưa ra các tham số theta.

Và sau đó lợi nhuận mà chúng ta nhận được sẽ nhân lên khi đi theo quỹ đạo đó.

Được rồi, và chúng tôi cũng lưu ý rằng chúng tôi có thể tính gần đúng giá trị này bằng giá trị trung bình mẫu bằng cách thu thập mẫu.

Vì vậy, chúng tôi nói rằng tôi sẽ triển khai,

như thể nó là 1 lên đến m,

và sau đó chúng tôi tính toán vật bên trong bằng cách sử dụng quỹ đạo IF.

Và tất nhiên điều này, chẳng hạn, bạn sẽ không cần phải tính toán, bạn chỉ cần cộng phần thưởng bạn nhận được.

Được rồi, như đã đề cập, mục tiêu của chúng tôi là cố gắng loại bỏ thứ omega này hoặc thực sự biến nó thành thứ mà chúng tôi biết ngoài tính toán.

Được rồi, vậy nên bạn sẽ gọi rằng có hai khả năng mà chúng ta quan tâm đến trong hệ thống học tập tăng cường hoặc MDP.

Đúng vậy, chúng ta có các đặc vụ.

Được rồi, và điều này được đặc trưng bởi chính sách.

Và sau đó chúng ta có môi trường.

Vì vậy, cây trên núi trong hồ, nếu bạn có thể nói.

Và vì vậy đây sẽ là p(s) nguyên tố hoặc cho trước s(a).

Và chúng chỉ tương tác với nhau theo một vòng lặp.

Được rồi, điều quan trọng là phần này được đánh dấu.

Vì vậy, về cơ bản, quỹ đạo chỉ là phép nhân các xác suất để đi từ bước này sang bước tiếp theo.

Được rồi, tôi nghĩ sẽ hữu ích nếu tôi viết nó ra và chúng ta có thể lý luận về những gì chúng ta thấy.

Vì vậy, yêu cầu của tôi là thế này.

Xác suất của một quỹ đạo là tích của.

Vì vậy, đây là những động lực môi trường.

Và chúng ta đi từ trạng thái này sang trạng thái tiếp theo nếu chúng ta đang ở trong một trạng thái và thực hiện một số hành động trong trạng thái đó.

Và sau đó là chính sách.

Chọn hành động cho một trạng thái nhất định.

Được rồi, vì vậy tôi muốn giúp làm cho điều này trở nên có ý nghĩa hơn trong trường hợp nó chưa rõ ràng.

Vì vậy, ví dụ: với nhãn mô hình thông thường không có hành động nào, chỉ có trạng thái.

Vì vậy, nhãn hiệu thông thường của mẫu mã hoặc nhãn hiệu của dây chuyền.

Vì vậy, giả sử chúng ta có một số chuỗi trạng thái, phải không?

Vậy là một.

S hai.

S ba, v.v.

Được rồi, vậy chúng ta sẽ tính xác suất của một chuỗi như thế nào.

Vậy P của S một tới S hai tới S ba, v.v.

sẽ chỉ là xác suất bắt đầu từ S một.

Nhân với xác suất về S hai khi bạn ở S một.

Nhân với xác suất mà bạn đạt được S ba.

Cho S hai và vân vân.

Được rồi, và đây thực sự là một trường hợp đặc biệt của quy tắc xác suất dây chuyền.

Vì vậy, bạn có thể xem lại ghi chú xác suất của mình nếu bạn quên điều đó.

Được rồi, về cơ bản cách bạn chuyển đổi những sơ đồ này thành giá trị xác suất là bạn lấy các trạng thái.

Và sau đó bạn nhân lên.

Vì vậy, giả sử xác suất để bắt đầu ở đây là xác suất để đi từ đây đến đây là xác suất B.

Xác suất để đi từ đây đến đây là C.

Và đây sẽ là D, v.v.

Vì vậy, bạn chỉ cần nhân tất cả chúng A nhân B nhân C nhân D, v.v.

Được rồi, vậy điều này sẽ hoạt động như thế nào với MDP?

Vì vậy, trong MDP, bạn sẽ nhận thấy rằng ở đây không có xác suất nào cho trạng thái ban đầu.

Nhưng chúng ta có thể làm điều đó mà không mất tính tổng quát vì chúng ta chỉ có thể giả sử rằng trạng thái đầu tiên là tất định.

Và sau đó chúng ta tiếp tục từ đó.

Và ngay cả nếu không, chúng ta luôn có thể đưa ra một trạng thái mới đi trước mang tính quyết định.

Được rồi, vậy để học tăng cường.

Giả sử chúng ta bắt đầu ở trạng thái S nào đó, trạng thái này mang tính quyết định.

Và sau đó chúng ta muốn xác định hành động nào cần thực hiện ở trạng thái S một.

Và sau đó thực hiện hành động đó sẽ đưa chúng ta đến trạng thái thứ hai.

Khi chúng ta ở trạng thái thứ hai, chúng ta muốn xác định hành động tiếp theo của mình là gì.

Vậy đó sẽ là số hai.

Chúng tôi thực hiện hai trong môi trường.

Sau đó, chúng ta quay lại trạng thái S ba, v.v.

Vậy những xác suất này là gì?

Vậy đây sẽ là số pi của một cho trước S một.

Và đây sẽ là p của S hai cho S một một một.

Điều này sẽ như vậy bây giờ chúng ta thấy trạng thái hai.

Chúng tôi muốn biết phải làm gì.

Vậy hãy tính pi của hai cho S hai, v.v.

Vì vậy, bạn có thể thấy nó giống hệt như sơ đồ chúng ta đã có ở trên với chuỗi Markov thông thường, mô hình Markov.

Và nhân tiện, nếu bạn muốn thực hành nhiều hơn với những thứ này để làm cho nó cụ thể hơn.

Và để củng cố những khái niệm này, bạn có thể muốn xem một khóa học NLP mà tôi đã tạo để dạy bạn về các mô hình ngôn ngữ.

Và cũng chỉ xin nhắc lại, đây là quy luật dây chuyền xác suất.

Được rồi.

Vì vậy, dù sao đi nữa, tôi hy vọng bạn tin rằng chuỗi sự kiện này thực sự giống với những gì chúng ta đã có ở trên.

Được rồi, bây giờ chúng ta có thể thay thế.

Vậy chúng ta vừa nói rằng chúng ta có biểu thức này cho xác suất của omega.

Và tiếp theo điều chúng ta sẽ làm, vì chúng ta có log của cái này và mục tiêu, chúng ta sẽ lấy log của cái kia.

Được rồi, tôi sẽ viết nó ra và bạn có thể cố gắng thuyết phục bản thân rằng nếu bạn lấy log của biểu thức trên thì đây là kết quả bạn sẽ nhận được.

Và về cơ bản đó là do nhật ký của một sản phẩm bằng tổng nhật ký của các mặt hàng riêng lẻ.

Được rồi, vậy toàn bộ điều này sẽ trở thành một tổng.

Vậy tổng của nó bằng một đến T lớn.

Và khi đó chúng ta có log của P của S của T hay tôi nên nói S của T cộng một.

S của T cộng với một S của T của T cộng với nhật ký của chính sách.

A của T cho S của T.

Được rồi.

Và bước tiếp theo là bạn sẽ nhớ lại rằng trong mục tiêu của chúng ta, chúng ta không có hoặc xin lỗi không phải mục tiêu của chúng ta, mà là mục tiêu gradient chính sách, gradient của mục tiêu, chúng ta có gradient của log của P.

Vì vậy, hãy lấy gradient của cái này theo theta và hãy xem chúng ta nhận được gì.

Vì vậy, bạn muốn điều này?

Chà, chúng ta thực sự không thể tính được gradient của cái này vì chúng ta không biết những thứ ở phía bên phải là gì.

Nhưng điều chúng ta biết là thứ này không phụ thuộc vào theta.

Chỉ điều này phụ thuộc vào theta vì theta là thứ tham số hóa chính sách không liên quan gì đến môi trường.

Môi trường không đổi đối với theta.

Vì vậy, không phụ thuộc vào theta, nghĩa là khi bạn lấy đạo hàm, nó bằng 0.

Vì vậy, loại hết không gian.

Hãy xem liệu tôi có thể chọn cái này không.

Thế đấy.

Được rồi.

Vì vậy, cái này bằng để chúng ta có thể mang lại độ dốc.

Vì vậy chúng tôi đặt nó ở đây, phải không?

Độ dốc, nhưng chúng ta có thể tính nó vào trong tổng.

Vì vậy, chúng ta sẽ có tổng bằng một đến T lớn.

Độ dốc của nhật ký, đây là thứ duy nhất còn lại bây giờ.

Vì vậy, điều này phụ thuộc vào theta.

Vì vậy chúng ta phải lấy gradient của cái này.

Và điều này chúng ta có thể làm được, đây chỉ là mã TensorFlow chém PyTorch bình thường.

Đây là những gì các thư viện đó làm, phải không?

Vậy là bạn có một mạng lưới thần kinh.

Và bạn muốn lấy độ dốc của đầu ra mạng thần kinh đối với các tham số.

Đó chính xác là những gì xảy ra khi bạn sử dụng PyTorch hoặc TensorFlow.

Được rồi.

Vì vậy đây là biểu thức chúng ta muốn cho log của p của omega.

Và bây giờ hãy kết nối nó với vật kính hoặc độ dốc của vật kính.

Và bây giờ đây là E bằng một hoặc hai T lớn.

Độ dốc của thứ chúng ta có ở trên.

Được rồi. Và bây giờ chúng ta vẫn còn G của omega.

Vậy là chúng ta có thêm một omega cần loại bỏ.

Vậy đây thực sự là gì?

Vì vậy, chúng tôi có một chuỗi phần thưởng mà chúng tôi nhận được trong suốt tập phim.

Chúng tôi sẽ cho rằng phần thưởng là xác định.

Vì vậy, với một trạng thái và một hành động, chúng ta biết rằng phần thưởng sẽ thực sự có trong thực tế.

Đó chỉ là trạng thái, nhưng chúng ta sẽ nói chung hơn.

Chúng tôi sẽ nói.

Sự trở lại là S1 A1 của chúng tôi.

Đó là S2 A2 của chúng tôi, v.v.

S2 A2 của chúng tôi.

Được rồi. Vì vậy, mấu chốt ở đây là có hai khoảng thời gian chúng ta nên xem xét.

Vậy 1 khoảng thời gian tính đến thời điểm hiện tại bé T.

Và sau đó ở phần khác sẽ là sau đó.

Vì vậy, chúng tôi có thể chia người gửi thành tổng.

Vì vậy chúng tôi sẽ nói.

Vì vậy chúng ta sẽ sử dụng biến giả tau.

tau bằng 1 đến T.

R của S tau.

Một tau.

Vì vậy, điều này tùy thuộc vào T.

Và sau đó cộng thêm.

Một lần nữa, chúng ta sẽ sử dụng tau.

Và lần này thực sự nó bắt đầu vào lúc nào.

T cộng 1 lên đến T lớn.

R của S tau.

Một tau.

Và thế là sau T.

Và vì vậy khẳng định của tôi là chỉ có phần này là quan trọng.

Và lý do tại sao phần này chỉ có phần này quan trọng là vì khi chúng ta lựa chọn.

Vì vậy, nếu chúng ta muốn tối ưu hóa số pi, hãy đặt theta vào đó.

Chúng ta đang cố gắng tối ưu hóa số pi để thực hiện hành động tối ưu tại thời điểm T.

Nhưng tại thời điểm T, tính đến thời điểm T bạn đã nhận được toàn bộ phần thưởng.

Vì vậy, bất cứ điều gì bạn làm bây giờ, bất kỳ hành động nào bạn chọn sẽ chỉ ảnh hưởng đến phần thưởng bạn nhận được trong tương lai.

Và đó là lý do tại sao khi chúng ta viết điều này vào mục tiêu, chúng ta chỉ quan tâm đến tổng này.

Vì vậy, chúng ta có thể viết lại độ dốc của mục tiêu của mình thành thế này.

Là T gradient log pi theta tại ST.

Và sau đó nhân tổng.

Tau bằng T cộng 1 cho đến T lớn.

Và sau đó là R của S tau.

Một tau.

Được rồi.

Và tại thời điểm này, chúng ta có thể thay thế cái này bằng.

Nói G của T.

Nó thực sự có ý nghĩa tương tự như.

G của ST.

TẠI.

Bây giờ điều này không quá quan trọng.

Chúng tôi chỉ giới thiệu các biểu tượng mới cho cùng một thứ.

Nhưng tôi hy vọng bạn có được ý tưởng.

Vì vậy, tại thời điểm này, chúng tôi đã sẵn sàng hiển thị một số mã giả về cách thực sự sử dụng thuật toán này.

Và tôi nghĩ điều đó sẽ thực sự giúp củng cố những gì bạn đã học và diễn đạt điều này thành những thuật ngữ cụ thể hơn.

Nhưng trước khi chúng ta làm điều đó, điều tôi muốn làm là tôi muốn giải thích tại sao mục tiêu này hoặc độ dốc của mục tiêu này lại có ý nghĩa.

Vì vậy, hãy nói về lý do tại sao điều này có ý nghĩa.

Được rồi.

Vì vậy, có thể hữu ích khi nghĩ đến một kịch bản hạn chế trong đó G chỉ có thể cộng 1 hoặc trừ 1.

Được rồi.

Vì vậy, nếu đúng như vậy thì điều đó có nghĩa là khi G cộng 1, điều đó có nghĩa là chúng ta đang thắng hoặc chúng ta đang nhận được phần thưởng tích cực.

Và vì vậy chúng tôi muốn tăng khả năng xảy ra hành động đó.

Phải. Vậy nếu G tăng thì phải.

Vì vậy, để có được phần thưởng lớn hơn, khi xác suất hành động đó tăng lên, vì bạn muốn trong tương lai, hãy nhận lại phần thưởng tích cực đó.

Được rồi. Vì vậy, ngược lại với G nhỏ hơn, bạn muốn xác suất xảy ra hành động đó giảm đi, vì bạn không muốn thực hiện hành động đó nữa.

Được rồi.

Và đó chính xác là những gì nó đang làm.

Vì vậy, bạn có thể bỏ qua nhật ký vì nhật ký là một hàm tăng đơn điệu.

Phải. Vậy khi pi lớn hơn thì log của pi lớn hơn, khi pi nhỏ hơn thì log của pi nhỏ hơn.

Vì vậy, thực sự bạn chỉ cần nghĩ đến hướng pi đi lên hay đi xuống.

Vì vậy tôi nghĩ cách giải thích này có lý.

Vì vậy, khi lợi nhuận cao hơn, bạn nhân xác suất với lợi nhuận đó bởi vì hoặc log của xác suất đó, vì bạn muốn tăng xác suất của hành động đó.

ngược lại nếu G nhỏ hơn hoặc âm thì bạn đi theo hướng ngược lại. Bạn thoát khỏi hành động đó.

Được rồi. Vì vậy, thuật toán cụ thể này, khi chúng ta nhìn vào G, kết quả trả về, đây được gọi là thuật toán tăng cường.

Được rồi. Vì thế tôi phải chuyển trang, nhưng hy vọng bạn không phiền.

Vì vậy, vị trí của chúng tôi là độ dốc của mục tiêu của chúng tôi là, chúng tôi có thể viết nó dưới dạng lợi nhuận thực tế mà chúng tôi nhận được.

Vậy một trên M bằng một trên M.

Nói G của tôi. Chúng tôi luôn làm quá tải G, nhưng hy vọng bạn hiểu điều này có nghĩa là gì.

Và gradient của log của i của theta, sau đó a t ở thứ i tung ra, và thứ i tung ra.

Và tôi đoán cái này nên có t2. Thực ra, điều này không có nhiều ý nghĩa vì chúng ta cũng muốn làm điều này với mọi t.

Được rồi. Vì vậy, chúng ta sẽ nói t, nó là một đến t lớn, và sau đó bạn cũng muốn tính trung bình cộng của nó. Vì vậy, chia cho t và M.

Nhưng tôi đoán mỗi tập cũng có thể có độ dài khác nhau phải không? Vậy ngay cả cái này, t lớn sẽ là thứ i, t lớn.

Và vì vậy bạn sẽ không muốn nó ở phía trước như thế. Bạn muốn nó, nói ở đây, một trên ti.

Dù sao thì, điều này hơi quá trang trọng, chỉ vì trong thực tế, chúng ta sẽ thực hiện giảm độ dốc.

Vì vậy, về cơ bản sẽ là giảm độ dốc ngẫu nhiên, trong đó chúng tôi lấy từng mẫu và thực hiện cập nhật sau.

Đúng vậy, cộng với tỷ lệ hạ cánh. Vì vậy, bây giờ là độ dốc tăng dần vì đây là mục tiêu mà chúng tôi muốn tối đa hóa. Phải.

Vì vậy, tôi sẽ chỉ viết độ dốc tăng dần đó vì chúng ta muốn tối đa hóa.

Được rồi. Và vì vậy nó nhân GT, gradient, pi theta, AT, cho ST.

Được rồi. Vì vậy bây giờ chúng ta hãy xem mã giả đầy đủ. Và nhân tiện, một lần nữa, thuật toán này được gọi là tăng cường.

Và do đó, việc tăng cường sử dụng mã giả trả về đầy đủ.

Được rồi. Vì vậy, đây là cách thiết lập điển hình mà chúng tôi bắt đầu bằng việc khởi tạo ngẫu nhiên. Vì vậy theta là ngẫu nhiên.

Sau đó làm lại một vòng lặp, chúng ta phát nhiều tập. Được rồi. Vì vậy chúng ta sẽ nói omega. Vâng, không tốt.

Vâng, vâng, hãy cứ nói omega ngang bằng với tập phim.

Được rồi. Vì vậy, giả sử chúng ta phát tập này sẽ trả về toàn bộ chuỗi trạng thái, hành động và phần thưởng.

Vì vậy, nó sẽ trông như thế này. Vì vậy, omega, tôi đặt trong ngoặc tương đương với một số chuỗi trạng thái, hành động và phần thưởng.

Vậy S1, A1. Vì vậy, ở trạng thái một, trạng thái ban đầu, không có phần thưởng. Bạn không nhận được bất kỳ phần thưởng nào khi đến đó.

Được rồi. Vậy rồi đến S2, A2, R2, cho đến hết, và cuối cùng chúng ta có. Vậy ST.

Vậy khi bạn ở trạng thái cuối, chữ T lớn nào sẽ là bạn không thực hiện hành động nào phải không?

Bởi vì đó là trạng thái cuối cùng. Không còn gì để làm nữa. Trò chơi đã kết thúc. Được rồi. Nhưng bạn nhận được một phần thưởng.

Được rồi. Vì vậy bạn có thể thấy nó hơi mất cân bằng một chút. Và luôn có những tình huống tương tự xảy ra trong một tình huống. Phải.

Vì vậy, bạn có đầy đủ các trạng thái, nhưng hành động cuối cùng không có ở đó. Và sau đó phần thưởng đầu tiên không có ở đó.

Vì vậy, có thể hơi khó khăn để sắp xếp mọi thứ một cách chính xác. Nhưng bây giờ tôi không muốn đi sâu vào những chi tiết đó vì tôi chỉ muốn cung cấp cho các bạn ý tưởng chính, tổng quan cấp cao về cách hoạt động của mã giả này.

Và nếu bạn muốn xem chi tiết hoặc cố gắng tự mình thực hiện điều này, bạn có thể thoải mái thực hiện.

Vì vậy, khi bạn viết mã này trên máy tính, rõ ràng là bạn không thể mắc bất kỳ lỗi nào. Vì vậy, điều đó sẽ buộc bạn phải suy nghĩ xem từng việc sẽ đi đến đâu một cách rõ ràng.

Được rồi. Vì vậy, trong mọi trường hợp, giả sử bây giờ chúng ta lặp lại từng bước thời gian mà chúng ta gặp trong tập phim.

Và bên trong vòng lặp này, bây giờ chúng ta sẽ thực hiện cập nhật này. Vì vậy trước tiên chúng ta tính G. Vậy G của T sẽ là R của T cộng 1 cộng gamma R của T cộng 2.

Đang trên đường tới gamma T lớn trừ T nhỏ trừ 1 R của T.

Được rồi. Vì vậy, mỗi lần lặp của vòng lặp, chúng tôi tính toán lợi nhuận là gì, lợi nhuận chiết khấu. Và sau đó sử dụng cái này, chúng ta có thể cắm nó vào bản cập nhật của mình.

Vì vậy, theta cộng với tốc độ học tập, GT, mà chúng ta vừa tính toán ở trên, và sau đó là gradient, mà chúng ta có thể sử dụng, chẳng hạn như đèn pin pi cho luồng tensor của chúng ta để tính toán gradient của mạng nơ-ron đối với các tham số.

Được rồi. Và vì vậy ATST được cung cấp, đúng vậy, bởi vì chúng tôi đã tìm thấy những thứ đó khi phát tập phim. Vì vậy, về cơ bản chúng ta có tất cả những thứ này.

Được rồi. Vì vậy, đó là mã giả để củng cố. Bây giờ, có một điều có thể làm cho việc này hiệu quả hơn một chút, bạn sẽ nhận thấy rằng với mỗi lần lặp của vòng lặp này, chúng ta phải tính một tổng.

Đó là theo thứ tự của T, có nghĩa là chúng ta phải thực hiện tất cả T việc T lần, nghĩa là tất cả đều bằng T bình phương.

Vì vậy, vòng lặp trên là tất cả T bình phương.

Được rồi. Và vì vậy khẳng định của tôi là đây không phải là cách hiệu quả nhất. Thay vào đó, những gì chúng ta có thể làm, thay vì T, bạn có thể thực hiện một vòng lặp ngược.

Vì vậy, nếu T ở chữ T lớn giảm xuống một, và sau đó bạn khởi tạo tiền lãi của mình, chẳng hạn, GT bằng 0. Và sau đó bên trong vòng lặp, hoặc bạn có thể nói, trời ơi, không có chỉ mục.

Vì vậy G cứ tiếp tục cập nhật. Vì vậy, nó là R(T cộng gamma G. Và cái này sử dụng tính chất đệ quy của kết quả để tính nó trong một bước thay vì có T bước.