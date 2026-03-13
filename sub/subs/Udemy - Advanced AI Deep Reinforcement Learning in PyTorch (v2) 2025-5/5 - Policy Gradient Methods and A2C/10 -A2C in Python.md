# 10 -A2C trong Python được dịch

---

Được rồi, video này sẽ hướng dẫn bạn cách triển khai A2C cho đi chung xe và Python.

Vì vậy, việc nhập khẩu về cơ bản giống như trước ngoại trừ việc chúng tôi cũng có sự phân bổ theo phân loại

như bạn biết đó là sự phân bổ cho chính sách của chúng tôi.

Bởi vì chúng ta sẽ chọn từ một nhóm danh mục riêng biệt.

Được rồi, ồ và cấu trúc của tập lệnh này cũng sẽ rất giống với

những gì chúng tôi đã có trước đây trong khóa học này.

Vì vậy, một trong những điều thú vị về bản cập nhật khóa học này là hầu hết mã đều tuân theo

cùng một mẫu trong khi ở lần lặp trước của khóa học này, tất cả các mã đều rất khác nhau

cho từng thuật toán. Vì vậy, tôi nghĩ điều đó làm cho việc theo dõi dễ dàng hơn một chút.

Được rồi, vậy là chúng ta có các cài đặt khác gần giống như trước đây.

Vì vậy, môi trường đi chung xe. Vì vậy, bây giờ vì chúng tôi đang thực hiện A2C nên chúng tôi sẽ đặt số lượng môi trường

đến một cái gì đó khác hơn một. Vì vậy, với ví dụ này, chúng ta sẽ thiết lập bốn môi trường.

Ngoài ra chúng ta có 100.000 bước thời gian. Một lần nữa tốc độ học tập của Adam sẽ là

tám nhân 10 đến âm bốn. Hệ số chiết khấu Gamma 0,99, không có hạt giống như chúng ta đã thảo luận trước đây.

Và chúng tôi có thêm một vài siêu tham số cho tập lệnh. Vì vậy, như bạn biết về sự mất mát của chúng tôi, chúng tôi có một

hệ số của hai số hạng bổ sung. Vì vậy, chúng ta có một hệ số cho entropy mà tôi đã đặt thành

0,01 và chúng tôi có một hệ số cho giá trị là 0,25. Và một điều tùy chọn khác bạn có thể làm

là bạn có thể cắt bớt độ dốc khi luyện tập. Về cơ bản đây là một cách khác để kiểm soát

độ lớn của độ dốc mà chúng tôi sử dụng để cập nhật. Vì vậy, điều này có nghĩa là thiết lập định mức tối đa

đối với vectơ đó, vectơ gradient là 0,5. Và điều này cũng giúp ích cho việc đào tạo.

Và một điều khác bạn sẽ thấy chúng tôi có thể làm là chúng tôi có thể bình thường hóa lợi thế hoặc tiêu chuẩn hóa

lợi thế. Vì vậy, chúng tôi trừ giá trị trung bình của nó và chia cho độ lệch chuẩn của lô hiện tại

đang được xử lý. Chúng tôi có thể sẽ không sử dụng nó nhưng chúng tôi sẽ xem. Và như mọi khi, bạn có thể thử nếu muốn.

Được rồi, đối với chức năng tạo trong V, nó sẽ giống hệt như trước nên tôi chỉ

sẽ sao chép và dán nó. Và sau đó chúng ta có mạng lưới thần kinh của mình. Vì vậy cái này mới nên chúng ta sẽ gọi nó là

nhà phê bình diễn viên. Vì vậy, phần này chỉ là bản tóm tắt. Chúng tôi có init, self-inv và ẩn.

Đặt nó thành 128. Vì vậy, kiến trúc của nó sẽ khá giống với tập lệnh DQN chỉ để

giữ mọi thứ công bằng để so sánh. Vậy chúng ta có 128 đơn vị ẩn và chỉ có một lớp ẩn.

Vì vậy, siêu chấm trong đó. Đúng và sau đó chúng tôi có. Vì vậy, bây giờ mạng lưới của chúng tôi sẽ có hai phần. Vì vậy

đầu tiên chúng ta sẽ có quyền. Vì vậy, lớp đầu tiên đi lên lớp ẩn đầu tiên. Vậy đó là

sẽ là tuyến tính nn chấm. Nhìn thấy tất cả hình dạng không gian trốn tránh này là 0. Đúng, điều đó đúng và ẩn giấu.

Và sau đó liên hệ với bạn. Vâng, được rồi, bây giờ đó chỉ là phần đầu tiên của mạng. Đó là những gì tôi đã vẽ

trong sơ đồ trước đó như phần thân. Vậy bây giờ chúng ta phải xác định phần đầu sẽ là hai phần khác nhau

đầu gắn vào cùng một cơ thể. Vì thế chúng ta sẽ có diễn viên chém đầu chính sách. Và điều đó sẽ xảy ra

một lớp tuyến tính khác. Và vì vậy hãy thử đoán xem nó sẽ trông như thế nào khi cho chúng ta thấy. Vậy hãy xem nào

cái này sẽ điền vào. Được rồi, đối với diễn viên hoặc chính sách, nó được kết nối với cái này nên nó phải có và

ẩn làm đầu vào. Và đầu ra là số lượng hành động trong không gian hành động. Và vì thế cũng để ý

cái này không có kích hoạt vì như bạn biết trong học sâu ngay cả khi chúng tôi muốn áp dụng softmax

để có được phân phối xác suất, chúng tôi thực sự không thực hiện đúng softmax trong mã. Vậy cái này

sẽ cung cấp cho chúng tôi nhật ký và từ đó chúng tôi có thể suy ra xác suất sẽ là bao nhiêu hoặc chúng tôi

có thể tính toán xác suất bằng cách áp dụng softmax nếu cần. Nhưng thông thường sẽ tốt hơn cho

đào tạo nếu bạn bao gồm softmax và hàm loss cùng nhau. Được rồi và sau đó cho

nhà phê bình vì vậy hàm giá trị chính xác và ẩn thành một bởi vì dự đoán cái nào là một chuyện

là giá trị Được rồi, bây giờ đối với chức năng chuyển tiếp của chúng ta, hãy xem điều đó khá chính xác. Vì vậy

chúng tôi truyền dữ liệu x của mình qua phần thân của mạng. Và sau khi nó đi qua cơ thể nên bây giờ x là

các tính năng ẩn. Vì vậy, chúng tôi chuyển các tính năng ẩn này thông qua tác nhân, điều này sẽ trả về

đăng nhập cho chính sách và sau đó chúng tôi chuyển x tương tự thông qua nhà phê bình và điều đó sẽ trả về giá trị

chức năng. Được rồi, hãy chạy cái này. Được rồi, tiếp theo chỉ là nội dung soạn sẵn mà chúng ta sẽ thực hiện

môi trường giống như trước đây. Đặt những lập luận này xuống đây để bạn có thể nhìn thấy chúng.

Đó là video ghi lại VID sai vì chúng tôi đang đào tạo và sau đó chuyển hạt giống nếu bạn muốn.

Và điều quan trọng là bạn không muốn chuyển cùng một hạt giống cho mọi môi trường vì bạn

không muốn chúng giống nhau. Vì vậy, đây là điều bạn có thể làm và rõ ràng là bạn không cần phải làm điều đó

hướng này tới đó. Nhiều tùy chọn khác nhưng điều này sẽ đảm bảo rằng tất cả các môi trường đều khác nhau.

Vì vậy, hãy chạy nó và sau đó chúng ta có cài đặt thiết bị. Vì vậy, một lần nữa chúng ta sẽ không sử dụng GPU

cho colab nhưng bạn có thể thử nếu muốn. Tôi thấy CPU thường hoạt động nhanh hơn.

Được rồi, tiếp theo chúng ta sẽ tạo ra mạng lưới thần kinh. Vì vậy hãy tạo ra mạng lưới thần kinh.

Điều này khá giống với trước đây nhưng những thứ này bây giờ có tên khác nên tôi sẽ gõ nó lên.

Vì vậy, sau khi nhà phê bình lấy bất kỳ thứ gì trong V, hãy đặt nó vào thiết bị và sau đó chúng ta có trình tối ưu hóa bằng

và điều đó đúng. Được rồi, đó là một mạng lưới thần kinh.

Được rồi bây giờ chúng ta có một cái gì đó mới. Vì vậy, hãy lấy mẫu và hành động từ nhật ký.

Vì vậy, chúng ta sẽ cần điều này trước khi bắt đầu đào tạo vì đây là những gì chúng ta sẽ sử dụng trong vòng lặp của mình

để chọn các hành động từ nhật ký mà mạng lưới thần kinh cung cấp cho chúng ta. Được rồi, cái chết, hành động mẫu.

Vì vậy, cũng tốt nếu bạn nghĩ về cách bạn sẽ thực hiện điều này. Đúng vậy nếu bạn có khả năng

bạn có thể làm gì, giả sử nếu cái này bị vón cục, thì có một chức năng trong đó để chọn từ danh sách

số nguyên hoặc từ danh sách các mục dựa trên danh sách xác suất mà bạn đưa ra.

Vì vậy, đối với PyTorch thì hơi khác một chút. Cách bạn làm điều đó là trước tiên bạn xác định một phân phối.

Vì vậy, chúng ta sẽ nói về phân phối phân loại với các log này và sau đó chúng ta có thể

từ bản phân phối đó, hãy gọi hàm mẫu sẽ trả về một mẫu và chúng ta không cần thực hiện item.

Được rồi, tôi đoán là chúng ta có thể. Hãy để tôi kiểm tra. Chức năng này được sử dụng như thế nào trong mã của tôi?

Được rồi, vậy nên trong mã trước đây của tôi, mỗi khi tôi sử dụng cái này, tôi chỉ tách nó ra nên chúng ta không cần

độ dốc rồi chuyển đổi nó hoặc đặt nó vào CPU rồi chuyển đổi nó thành mảng trọng tài.

Được rồi, vì trường hợp đó nên tôi sẽ sửa đổi mã của mình một chút và chúng ta sẽ sử dụng mục này làm

được đề xuất bởi colab. Được rồi, nó sẽ trả về mảng có nhiều mảng hoặc chỉ là một số.

Được rồi, vậy chúng ta có entropy tính toán để tính toán entropy để điều chỉnh tổn thất.

Và đây là những gì sẽ trông giống như tính toán entropy cho các log đã cho.

Ừm, điều đó thật thú vị nên vâng, ban đầu những gì tôi có về cơ bản là tính toán entropy

bạn có thể làm thủ công nhưng tôi thích điều này hơn vì nó được tích hợp vào PyTorch nên tôi muốn

sử dụng cái này ừm hy vọng nó hoạt động đôi khi mã i không hoạt động nhưng tôi nghĩ nó sẽ hoạt động dựa trên

dựa trên những gì tôi thấy nên tôi đã dán vào đây những gì trước đây trông giống phiên bản gốc của mã này

Dù sao thì tôi cũng muốn giải thích điều đó để chính sách ghi lại là thông tin đầu vào sẽ trả về nếu chúng tôi áp dụng

softmax cái này sẽ trả về xác suất thực tế nhưng chúng ta cũng cần cho phép tính này

xác suất log đúng vì nó bằng p nhân log p và sau đó tính tổng tất cả các xác suất khác nhau

giá trị của biến ngẫu nhiên. Được rồi, chúng ta cũng cần nhật ký của softmax và có một chức năng

đối với cái đó đã được gọi là log softmax nên chúng tôi cũng tính toán nó rồi nhân chúng lại với nhau

đúng vậy p nhân log p và sau đó chúng ta tính tổng để tính entropy.

Được rồi, tôi đoán nhược điểm duy nhất của việc này là nó không trả về xác suất nhật ký mà chúng ta

cần và nhân tiện tại sao chúng ta lại cần xác suất nhật ký? Câu trả lời là chúng ta cần chúng vì

bởi vì đó là phần chính của hàm mất mát của chúng tôi nên độ dốc chính sách khi bạn nhớ lại

là độ dốc của log của các xác suất này và sau đó nhân với lợi thế nhưng

Lợi thế là chúng tôi không lấy độ dốc đối với điều đó. Vậy hãy để tôi kiểm tra thật nhanh nếu chúng ta có thể

lấy xác suất nhật ký từ phân phối nên tôi sẽ tra cứu nó ngay bây giờ.

Được rồi, theo những gì tôi thấy thì có một hàm tính xác suất nhật ký nhưng chúng ta cần phải

thực hiện các hành động cùng lúc nên điều này sẽ không xảy ra nên điều này sẽ không hữu ích như hiện tại.

Vậy lý do là vì từ đối tượng phân phối này chúng ta có thể gọi một hàm gọi là log

có vấn đề nhưng điều này sẽ yêu cầu chúng ta chuyển vào các hành động và chúng ta không có hành động nào làm đầu vào cho hàm này

vì vậy chúng ta có thể làm điều đó chúng ta sẽ gọi nó là entropy tính toán và thăm dò nhật ký

thực hiện các hành động và sau đó trả lại điều này.

Vì vậy, hãy thử theo cách đó và xem nó diễn ra như thế nào.

Được rồi, một lần nữa chúng ta có chức năng numpy to torch nên numpy to torch sẽ có một số mảng và

Loại D theo mặc định sẽ là luồng ngọn đuốc 32 và sau đó vâng, chúng tôi cũng có thể chuyển vào thiết bị mặc dù

Trước đây tôi không có thứ đó. Vâng, đó là hoặc chúng tôi đã làm như vậy với tư cách là tensor.

Được rồi, tiếp theo chúng ta có vòng huấn luyện để tập quay lại

danh sách trống mất danh sách trống.

Được rồi, phần tiếp theo là phần cốt lõi của mã của chúng ta, nó sẽ là vòng lặp đào tạo thực sự.

Vì vậy, nó bắt đầu rất giống như trước đây, toàn bộ mọi thứ cũng rất giống như trước đây nên chúng tôi

sắp xếp thời gian cho toàn bộ sự việc, chúng tôi thiết lập lại môi trường, điều này mang lại cho chúng tôi quan sát đầu tiên

ENV đặt lại dấu chấm trong hạt giống và sau đó chúng tôi cũng sẽ tự động đặt lại các số 0 dấu chấm NP

không phải ENV loại D là bò. Được rồi, có vẻ như chúng ta chưa xác định được lý do tại sao ENV của mình.

Tôi không biết chúng ta có ENV ở đây. Vì vậy, thật kỳ lạ khi đây là

được tô sáng màu đỏ ồ vì tôi quên mất giá trị bằng. Được rồi thế tốt hơn. Được rồi bây giờ chúng ta có thể làm

vòng lặp chính vì vậy đối với bước tổng thể trong phạm vi tổng thời gian và sau đó ở đây chúng ta sẽ nhận được đầu ra mô hình của mình

vì vậy chúng tôi xác định hành động nào chúng tôi muốn thực hiện dựa trên trạng thái vì vậy hãy lưu ý rằng bây giờ nó khác với

những gì chúng tôi có trước đây trong tqn bởi vì với dqn, chúng tôi đã làm epsilon một cách tham lam và bây giờ chúng tôi không cần phải làm

bất kỳ hình thức sửa đổi hành động nào mà mạng chỉ cung cấp cho chúng tôi hành động hoặc chỉ cung cấp cho chúng tôi

nhật ký nên chúng tôi sẽ gọi nhật ký hành động này là nhật ký và giá trị vì vậy chúng tôi sẽ gọi mạng AC chuyển đổi quan sát của chúng tôi thành

một tensor ngọn đuốc và chuyển nó vào. Được rồi được rồi, tiếp theo chúng ta sẽ chọn hành động dựa trên chính sách hiện tại.

Được rồi, các hành động này sẽ tương đương với hành động mẫu chuyển vào nhật ký mà chúng ta vừa nhận được.

Được rồi và tôi nhấn enter để nó điền tất cả những thứ này cho tôi vì vậy hãy để tôi đảm bảo rằng nó giống như

những gì tôi có nên phần thưởng quan sát tiếp theo được thực hiện sẽ bị cắt bớt, đó là thông tin và sau đó là ENVs.step, được rồi, điều đó đúng

bước đi môi trường Tôi không biết Tôi không thích điều đó bước một bước bước một bước trong môi trường được chứ

được rồi, tiếp theo chúng ta sẽ ghi lại tờ khai vì vậy chúng ta sẽ kiểm tra xem chúng ta đã làm xong chưa nếu đã làm xong rồi

uh ghi lại lợi nhuận. Ghi lại các lượt vẽ để lặp lại các đoạn và cắt bớt hoặc

việc này sẽ được thực hiện bằng cách cắt ngắn, không cắt ngắn và liệt kê số nhiều và chúng ta sẽ duyệt qua tất cả

duns và cắt ngắn với nhau. Được rồi, hãy xem điều này có đúng không nên có vẻ không ổn nên vậy

để ý xem nó diễn ra thế nào i tập r trên thực tế nó phải là tập r i nên ret bằng infos tập

r i và sau đó chúng tôi sẽ thêm thông tin này vào danh sách trả lại của mình và sau đó chúng tôi sẽ in

sự trở lại này là gì vậy tôi sẽ sao chép nó vì nó khá dài

chúng tôi sẽ giúp đỡ nếu tôi đặt nó ở đây có lẽ sẽ ổn một chút ừm vậy hãy đặt nó trở lại để chúng tôi in ra

bước hiện tại một số lợi nhuận được thu thập cho đến nay chỉ là số tập và sau đó là

thực tế thì nó sẽ tự trả lại thôi và sau đó colab đã đề xuất điều này. Tôi sẽ giữ nó chỉ vì nó hơi ít

khác với trước đây ừm ồ không, chúng tôi không thể làm điều này nên lý do tại sao chúng tôi không thể làm điều này là vì chúng tôi

cần sử dụng tính năng tự động đặt lại trước khi chúng ta thực hiện việc này một cách ổn thỏa, vì vậy hãy quay lại bài giảng nơi tôi đã giải thích cách thực hiện.

tự động thiết lập lại hoạt động tốt và chúng tôi phải thực hiện theo thứ tự nào để hiểu lý do tại sao nó không nên ở đây

được nhưng điều chúng ta có thể làm để điều không quên là chỉ định obbs cho obb tiếp theo và cũng chỉ để

hãy nhớ lưu ý nếu tự động đặt lại là đúng thì obbs tiếp theo là nội dung thời gian một lần ở bước một vì vậy đây là nội dung đào tạo

và vì vậy ở đây đây là những gì chúng tôi sử dụng tính năng tự động đặt lại vì vậy chúng tôi phải sử dụng tính năng tự động đặt lại trước khi đặt thành

giá trị mới của nó nên tôi có một mặt nạ về cơ bản trái ngược với tự động đặt lại, nói cách khác cho bất kỳ

các tập chưa kết thúc, chúng ta có thể thực hiện phép tính này được, vì vậy đây chỉ là lấy tất cả

các giá trị có liên quan trong mỗi tập, vì vậy, giả sử chúng tôi đang chạy khoảng 20 tập mà chúng tôi chỉ muốn

những cái chưa kết thúc những cái mà obbs tiếp theo không phải là trạng thái ban đầu của tập tiếp theo

đúng bởi vì chúng tôi muốn tất cả các trạng thái mà chúng tôi sử dụng trong tính toán của mình đều xuất phát từ cùng một tập

được rồi, vậy hãy nói giá trị này bằng vì vậy chúng ta sẽ chỉ đặt dấu gạch dưới uh ở trước hoặc sau

tất cả các tên biến để biểu thị những thứ chúng ta thực sự sử dụng để tính toán

vì vậy chúng tôi chỉ lập chỉ mục mọi thứ theo mặt nạ nên obbs obbs hành động của mặt nạ bằng hành động mặt nạ

Tôi nghĩ tôi đã quên đăng ký bằng nhau ở đây ừ được rồi, chúng ta có nhật ký hành động

hành động nhật ký mặt nạ phần thưởng mặt nạ uh tiếp theo obbs

vâng tiếp theo là mặt nạ obbs và sau đó là mặt nạ cồn cát được rồi, bây giờ chúng ta sẽ tính toán từng

các thành phần của sự mất mát, từng cái một, vì vậy chúng ta sẽ bắt đầu với việc mất giá trị một cách dễ dàng, nó chỉ là

có nghĩa là lỗi bình phương với torch.no grad

bởi vì hãy nhớ rằng chúng tôi không chuyển gradient qua mục tiêu nên nhật ký mà chúng tôi không quan tâm

và lý do tại sao chúng ta phải làm điều này là vì mạng này luôn trả về cả

nó trả về nhật ký cho hành động từ chính sách và giá trị

vì vậy chúng ta sẽ chỉ nói đây là giá trị tiếp theo bằng mạng ac và chúng ta chuyển vào và p để chuyển tiếp obbs tiếp theo

và sau đó tôi không biết tại sao nó lại đề xuất cái này uh chúng tôi không cần cái đó hoặc tôi đoán chúng ta có thể sử dụng cái này

hãy suy nghĩ về điều đó để nếu tập đó hoàn thành thì chúng ta sẽ không có bất kỳ phần thưởng nào trong tương lai nên chúng ta

biết giá trị bằng 0 nhưng chúng tôi đã bao gồm giá trị này khi tính toán mục tiêu

vì vậy chúng tôi không cần điều đó vì vậy mục tiêu td là đúng, chúng ta hãy xem điều này và xem nó có đúng không

vì vậy và phần thưởng ngọn đuốc beta uh tôi sẽ làm phẳng những thứ này không phải là chúng ta cần ừm để tôi cố gắng không làm phẳng những thứ này

xem chuyện gì sẽ xảy ra nhé, vậy nên tôi sẽ thưởng thêm phần thưởng ngọn đuốc beta

và tôi sẽ chuyển nó sang dòng tiếp theo để nó có gamma nhân một trừ

và beta torch uh duns và tôi sẽ đặt im beta torch duns ở bên ngoài

như thế và sau đó đặt giá trị tiếp theo nên điều này có thể không hiệu quả vì tôi đang làm hơi khác một chút ừm

bản gốc tôi đã làm phẳng tất cả những thứ này nhưng miễn là bạn không làm phẳng bất cứ thứ gì ừ thì nó sẽ hoạt động bình thường

giống nhau nên chúng ta sẽ nói dự đoán bằng giá trị mà chúng ta thậm chí không cần phải làm điều đó tôi đang nói siết chặt

trước đây nhưng vì tôi không làm phẳng những thứ này nên chúng tôi không cần phải ép nên chúng tôi sẽ nói là mất giá trị

bằng với tôi đoán chúng ta có thể mang lại sự mất giá trị bên ngoài này bằng với f dot msc loss và td target

và ồ nó quay ngược lại bạn biết đầu vào nào đến trước và sau đó mới là mục tiêu

vì vậy chúng ta sẽ nói pred td target như thế hoặc tôi đoán pred chỉ có giá trị như thế

được rồi, vậy hãy giảm giá trị của chúng ta và sau đó chúng ta sẽ mất chính sách mất chính sách được rồi, vậy nên chúng ta nhận được entropy và

log prob từ hàm của chúng ta ở trên tính toán entropy và log prob thực hiện nhật ký hành động và

hành động và sau đó chúng tôi tính toán lợi thế để mục tiêu td trừ đi giá trị ồ và nhân tiện

vì vậy đối với tập lệnh này rõ ràng chúng tôi chỉ sử dụng lỗi td uh cho cả cập nhật giá trị và

cập nhật chính sách nên như đã đề cập, có một số tùy chọn khác nhau, bạn có thể sử dụng bước n

các phương thức bạn có thể sử dụng toàn bộ lợi nhuận, v.v. vì vậy, đối với tập lệnh cụ thể này, tôi đã chọn sử dụng

chỉ là lỗi td một bước cho mục tiêu thôi được rồi nên giá trị trừ của mục tiêu td là chính xác

và chúng tôi ừ được rồi, vậy nên trước đây trong phiên bản trước của kịch bản này tôi đã làm một điều gì đó

hơi khác một chút vì hàm này trước đây chỉ tính toán entropy nên tôi sẽ sử dụng

nhật ký và sau đó trong hàm chúng tôi đã tính toán các thăm dò nhật ký từ các nhật ký mà chúng tôi đang tính toán

ghi nhật ký các thăm dò cho tất cả các hành động so với những gì nó đang thực hiện trong chức năng của chúng tôi bây giờ nó đang tính toán nhật ký

các thăm dò chỉ dành cho những hành động này thôi được rồi, vậy nên trong tập lệnh gốc, chúng ta sẽ nhận được các thăm dò nhật ký cho tất cả các hành động

hành động và sau đó lập chỉ mục theo hành động tương tự như những gì chúng tôi đã làm trong tập lệnh dqn khi chúng tôi muốn chọn

chỉ các giá trị q cho các hành động chúng ta đã thực hiện và không phải tất cả các hành động đều ổn vì hàm

hiện tại chúng tôi đã làm điều đó rồi, chúng tôi không cần phải làm điều đó nữa, được rồi, vì vậy các vấn đề về nhật ký vẫn ổn

và sau đó là lợi thế nên lợi thế tôi nghĩ chúng ta sẽ cần tách ra

được rồi, bây giờ chúng ta sẽ loại bỏ độ dốc vì chúng ta không muốn như đã đề cập

chúng tôi không muốn tính toán độ dốc thông qua lợi thế, lợi thế chỉ là hệ số tỷ lệ

mà chúng tôi đang sử dụng để chia tỷ lệ độ dốc và ừm, vậy nên dấu chấm của ngọn đuốc có nghĩa là ổn

được rồi, đây là khoản lỗ hợp đồng của chúng tôi và bây giờ tổng thiệt hại của chúng tôi sẽ là khoản lỗ hợp đồng cộng với hãy xem

trọng lượng entropy ừm hoặc được thôi nên sẽ hơi khó hiểu nên tôi sẽ trừ đi

trọng số entropy và lý do là vì entropy như đã đề cập là thứ chúng ta muốn tăng

vì vậy bởi vì ngọn đuốc tròn sử dụng tổn thất và nó cố gắng giảm mục tiêu nên chúng ta nên phủ nhận entropy

đối với sự mất entropy của chúng ta nên đó là lý do tại sao có một điểm trừ ở đây được rồi và sau đó giá trị trọng số nhân giá trị

thua đó là dương vì nó có nghĩa là chiếm đoạt được, vì vậy một khi chúng ta thua, chúng ta có thể

hãy thêm nó vào danh sách bị mất của chúng tôi, vì vậy hãy thêm mục bị mất vào và sau đó chúng tôi sẽ in nội dung ra

nếu bước toàn cầu đúng vì ở bước thứ 100, chúng tôi sẽ in các bước trên giây cho đến nay, điều đó sẽ là

số lẻ được điền vào và sau đó nó biến mất bước toàn cầu chia cho time.time trừ đi thời gian bắt đầu

được rồi được rồi, tiếp theo chúng ta sẽ thực hiện bước giảm độ dốc

được rồi, trình tối ưu hóa là điểm tốt nghiệp của bạn bị lạc ngược nên lần này tôi sẽ không sử dụng nó

bạn có thể đưa vào nếu muốn nhưng tôi sẽ không chỉ xem nó hoạt động như thế nào và làm cho nó

gần hơn với những gì tôi có ban đầu nên bạn có thể thử nếu bạn thích, rõ ràng đó chỉ là một dòng

bạn có thể bật hoặc tắt nó và bây giờ chúng tôi sẽ cập nhật tính năng tự động thiết lập lại sau khi hoàn tất

nên tự động thiết lập lại Tôi đoán ký hiệu này có tác dụng bạn có thể thử nó Tôi sẽ giữ nó

những gì trước đây rất hợp lý hoặc được thực hiện sẽ bị cắt bớt và sau đó lại ừm nếu mô hình của chúng tôi hoạt động tốt

chúng ta sẽ thoát khỏi vòng lặp này ngay nên hãy tạm dừng nếu 10 tập cuối cùng

có phần thưởng tối đa được rồi, vậy nên đó sẽ là nếu tập đó trả về lớn hơn 10

Tôi nghĩ tôi đã nói lớn hơn 10 trong bản gốc không thành vấn đề vì nó sẽ như thế này đây.

Dù sao thì cũng đều hơn 10 và sau đó tôi không biết tại sao nó lại làm như vậy, mã của ai đã làm điều này

đây không phải là điều tôi muốn nên tôi muốn np.all np.equal

được rồi, xin lỗi, bạn không thể xem được, vậy thì chúng tôi muốn 10 phần thưởng cuối cùng bằng 500 nên tập này

trả về trừ 10 cho đến cuối tất cả đều bằng 500 nếu đó là trường hợp của tất cả chúng và chúng tôi nói tối đa

phần thưởng đã đạt được và sau đó chúng ta nghỉ ngơi được rồi nên hãy chạy cái này ừm, chúng ta có thể gặp vấn đề đấy

một tensor có bốn phần tử không thể chuyển đổi thành vô hướng uh chúng tôi đã làm uh dot item

được rồi, tôi cảm thấy chúng ta nên thay đổi lại điều này

vâng vì mục trả về một đại lượng vô hướng nên đây là điều AI đã đề xuất

rõ ràng là nó không hoạt động

chúng tôi sẽ trả lại tất cả các hành động

được rồi và giờ thì thế này

chúng tôi sẽ viết như vậy và chúng tôi cũng cần một phần tách ra

được rồi, cái này sẽ trả về một tensor ngọn đuốc, tháo nó ra để loại bỏ độ dốc đặt nó trên CPU

chuyển đổi thành mảng có nhiều mảng để đây sẽ là các hành động có nhiều mảng và trong môi trường chúng ta thực hiện các hành động không có nhiều mảng

hành động của ngọn đuốc tensor được rồi, còn điều gì khác phải thay đổi nên bây giờ tôi nghĩ mọi chuyện sẽ ổn thôi, hãy bắt đầu

hãy thử lại nhé, vậy là bạn đang ở trên cùng, chúng tôi có một cảnh báo nhỏ về việc sử dụng kích thước mục tiêu

khác với kích thước đầu vào vâng, vậy nên đây có thể là từ đâu

được rồi vì vậy tất cả những thứ mới mà chúng tôi đã làm sẽ không tốt nếu bạn thử nghiệm điều này khi bạn đang viết mã trực tiếp

vậy tôi sẽ làm gì vậy nên tôi sẽ thay đổi cái này trở lại cái tôi đã có và sau đó có lẽ tôi sẽ

tự mình thử nghiệm cái này một chút để xem liệu tôi có thể làm được việc này không, thay vào đó chỉ cần làm những gì

Tôi đã có trước đó nên đây sẽ chỉ là entropy tính toán và nó sẽ trả về toàn bộ thăm dò nhật ký và entropy

được rồi và vì vậy tôi nghĩ chúng ta còn có gì nữa mà tôi cần nó thay đổi được rồi nên nó đang phàn nàn về

hình dạng không phù hợp vì vậy đối với mục tiêu giảm giá trị, tôi sẽ làm phẳng mọi thứ nên tôi

sẽ quay lại làm việc đó nên phần thưởng làm phẳng hàng tấn làm phẳng giá trị tiếp theo làm phẳng và sau đó

Fred sẽ là Fred có giá trị bằng giá trị chấm bóp, về cơ bản giống như làm phẳng và điều này sẽ là

vì vậy chúng ta sẽ quay lại những gì chúng ta đã có trước khi tính toán entropy không chuyển vào các hành động và sau đó chúng ta sẽ tính toán

mọi thứ đều được thực hiện thủ công ở đây nên dù sao thì bạn cũng có thể xem những gì tôi có ban đầu được rồi, vậy trước tiên chúng ta sẽ làm

về cơ bản điều đó là đúng nên chúng tôi chỉ đặt tên chúng khác nhau để các thăm dò nhật ký được chọn sẽ thu thập các thăm dò nhật ký

một hành động unsqueez, yep nên điều đó đúng nên về cơ bản một lần nữa điều này thật khó hiểu nhưng thực sự

những gì nó đang làm là ghi lại các thăm dò và chúng tôi chỉ muốn chọn những hành động được thực hiện duy nhất

đúng vậy đây sẽ là cú pháp khó hiểu đây là cú pháp ngọn đuốc pi phức tạp hơn một chút

được rồi, vậy thì chúng ta có luật chính sách. Tôi có ý nghĩa ở bên ngoài nên bạn có thể chỉ cần thực hiện dấu chấm thay vì

ngọn đuốc có nghĩa tương tự như numpy nhưng cái này cũng có tác dụng nên tôi sẽ để nó ổn nên hãy thử

lần nữa xem chuyện gì xảy ra uh không được rồi bây giờ không ổn được rồi nên đây thực sự là một cơ hội tốt để thể hiện

Các bạn biết cách gỡ lỗi. Tôi sẽ nói khi nghi ngờ hãy in nó ra để ghi lại hình dạng đó và chúng tôi chỉ muốn

log các vấn đề có hình dạng ồ đúng rồi, thật dễ dàng, anh ấy chỉ vì tôi đã tính toán cái này nhưng tôi thực sự không sử dụng nó

vâng được rồi vì vậy chúng ta có thể không cần phải làm điều này vì vậy hãy thử chạy lại và vâng và

đang hoạt động. Điều quan trọng ở trên đó là gì khi sử dụng lại kích thước mục tiêu

khác với kích thước đầu vào trống, điều đó đáng nghi ngờ được thôi, có lẽ chúng tôi không muốn điều đó

tại sao điều đó lại xảy ra nhưng dù sao thì có vẻ như nó đang được luyện tập nên điều đó tốt

nhưng tôi muốn loại bỏ cảnh báo đó vì điều đó không nên xảy ra

được rồi, dù thế nào đi nữa bạn cũng sẽ thấy phiên bản hoạt động đầy đủ của tập lệnh này trong mã chính thức phải không

vì vậy tôi đã cố gắng thay đổi nó một chút trong bài giảng này nhưng bạn biết đấy, hãy quay lại bản gốc

nếu bạn muốn xem phiên bản đang chạy mà không có bất kỳ cảnh báo nào trong số này

chỉ cần đợi việc này kết thúc

trước khi chúng ta bắt đầu cố gắng chạy lại

được rồi vậy là xong và tại sao nó lại thoát vì chúng tôi đã đạt được phần thưởng tối đa

được rồi, ý tôi là nó vẫn hoạt động, chỉ có một chút vấn đề ở giữa nhưng tôi không thích điều đó

vấn đề nên tôi muốn khắc phục nó để mọi việc vẫn giống như trước đây chúng ta chỉ lập biểu đồ trả về

đúng vậy nên chúng ta đã đạt được phần thưởng tối đa nên điều này khá giống mong đợi nhưng hãy lưu ý rằng nó vẫn như vậy

giống như đi xuống phải nó lên đến đỉnh rồi đi xuống rồi lại đi lên

và sự mất mát thường không hữu ích lắm trong việc học tăng cường nhưng chúng ta sẽ kiểm tra chúng

dù sao đi nữa và sau đó chúng tôi phải lưu mô hình và đánh giá thực sự có thể chúng tôi sẽ làm gì

và bây giờ chúng ta hãy giữ nó chỉ vì dù sao thì chúng ta cũng gần như đã hoàn thành rồi nên hãy lưu mô hình vào đường dẫn này

vì vậy, điều này giống như trước khi tải lại mô hình vì vậy điều này sẽ hiển thị lại cho bạn thấy rõ ràng bạn sẽ làm như thế nào

không dành cho tập lệnh này nhưng nếu bạn muốn lưu mô hình này và sau đó triển khai ở một nơi khác trong

trong tương lai đây sẽ là mã phù hợp nên chúng tôi sẽ chuyển sang và mã này dành cho eVal nên chúng tôi sẽ chuyển sang

tạo một môi trường mới và bây giờ chúng tôi sẽ đặt chế độ quay video thành true vì chúng tôi muốn lưu

video chúng ta sẽ tạo một mạng lưới thần kinh mới sử dụng môi trường này, đặt nó ở trạng thái tải thiết bị

dict nghĩa là tải mô hình từ đường dẫn mô hình mà chúng tôi đã lưu và sau đó chúng tôi sẽ đặt nó ở chế độ eVal

được rồi vậy là chúng ta đã tải mô hình và bây giờ hãy chạy mã của chúng ta để đánh giá mô hình để đánh giá

mô hình nên phần này cũng sẽ giống phần lớn như trước nên cuối tập eVal 10

eVal trả về đặt nó thành một mảng trống và các tập eVal

Tôi vừa đặt lại môi trường trong vzval.reset và sau đó chúng ta sẽ lặp lại từng tập

với tư cách là tập, tôi gọi đó là tập đã hoàn thành sai và chúng ta không cần điều này, hãy đặt nó vào bên trong

vì vậy trong khi chưa hoàn thành tập, chúng tôi sẽ nhận được nhật ký hành động và đây là những gì

vâng, hãy làm mẫu cho đèn pin được quy định và sau đó chọn hành động dựa trên chính sách hiện tại để chúng tôi sẽ nói hành động

bằng hành động mẫu từ các bản ghi, biến chúng thành các mảng gọn gàng của bạn giống như trước khi thực hiện một bước

môi trường, v.v. nên nó không đề xuất vào lúc này vì nó chỉ sao chép mã mà chúng tôi

đã ở trên nhưng bạn không cần phải gọi nó là obs tiếp theo vì chúng tôi không sử dụng nó nữa, được rồi và

bị cắt cụt và kẻ thù và sau đó chúng tôi sẽ nói vì chúng tôi chỉ có một môi trường nên chúng tôi có thể kiểm tra nó như thế này

vì vậy nếu thực hiện bằng 0 hoặc cắt bớt số 0 thì chúng ta biết mình đã hoàn thành, chúng ta sẽ gọi đây là g

vì đó là cách chúng tôi gọi nó và sau đó chúng tôi sẽ nói rằng tập phim này được thực hiện đúng và sau đó chúng tôi sẽ

chỉ cần in tiến trình của chúng tôi để in f tập i rồi quay lại g và sau đó chúng tôi sẽ đóng

môi trường một khi chúng ta đã hoàn thành vzvl, điều đó sẽ ổn thôi, vì vậy điều này sẽ hoạt động và chúng ta sẽ tiến gần đến

500 mỗi lần vì đó là số tiền chúng tôi nhận được trước khi bỏ cuộc

được rồi, vậy bây giờ, việc vẽ biểu đồ phân phối khi bạn có cùng một giá trị sẽ không còn hữu ích nữa

nhưng dù sao thì chúng ta cũng sẽ làm điều đó chỉ vì đây thường là điều bạn có thể muốn làm

sau đó chúng ta sẽ phát video để xem người mẫu đã học được cách làm như thế nào

được rồi, việc giữ nó ở gần trung tâm trong hầu hết thời gian cũng không tệ nhưng thực tế là vậy

trôi sang bên trái để bạn nhận thấy đôi khi khi bạn chạy mô hình này, mô hình sẽ thực sự học được

giữ nó ở giữa mặc dù cũng đáng để suy nghĩ tại sao nó không làm như vậy và

Câu trả lời là vì không cần phải làm điều đó để nhận được phần thưởng tối đa cho môi trường này

đúng vì chúng tôi giới hạn ở mức 500 nên mặc dù nó di chuyển chậm sang trái nhưng nó vẫn có thể

đạt tới 500, điều đó có nghĩa là nó sẽ sang trái không thành vấn đề nhưng nếu bạn được yêu cầu không cắt

ra khỏi môi trường sau 500 bước, nó có thể biết rằng để nhận được phần thưởng cao hơn, nó phải ở giữa

được rồi và cũng liên quan đến cảnh báo này, chúng tôi sẽ thêm vào đây. Tôi sẽ xem xét vấn đề này và nếu tôi đã sửa nó

Tôi sẽ cập nhật một chút nếu không mã chính thức có thể sẽ không có mã đó trong đó

được rồi, tôi chỉ mất vài phút để tìm ra điều gì sai nhưng tôi muốn giải thích điều này vì

Tôi vẫn ở đây nên về cơ bản, chiến lược của tôi cho việc này là luôn in ra nhiều thứ

hãy in ra những thứ hữu ích và sử dụng nó để tìm ra lỗi sai

vì vậy trong trường hợp này những gì đang xảy ra là sự siết chặt có vẻ như là quá hung hãn và thực tế là nó đã xảy ra

đề xuất làm phẳng trước đó có lẽ là một ý tưởng hay đúng không, vậy nên hãy tưởng tượng chúng ta có

bốn môi trường và tất cả chúng ngoại trừ một môi trường đã kết thúc và vì vậy điều đã xảy ra là vì tất cả chúng ngoại trừ một

đã kết thúc, chúng tôi chỉ có một giá trị và vì vậy khi bạn nén một giá trị, nó sẽ không trở thành một mảng

kích thước một, nó nén càng nhiều càng tốt để biến nó thành vô hướng, đó là lý do tại sao chúng tôi nhận được

cảnh báo đó tôi đoán bây giờ cảnh báo đã biến mất vì tôi đã thoát ra trước nhưng bạn có thể thấy

hình dạng của dự đoán không là gì vì nó chỉ là vô hướng trong khi hình dạng của mục tiêu là một

bởi vì chúng tôi đã san phẳng được nên chúng tôi cũng có thể siết chặt mục tiêu, đó là một khả năng khác nhưng

điều này sẽ khắc phục mọi thứ một cách ổn thỏa vì vậy nếu chúng ta nói làm phẳng thay vì nén thì nó sẽ hoạt động tốt

chúng ta sẽ chạy cái này và sau đó tôi đoán là không đáng để chờ đợi vì bây giờ chúng ta sẽ không nhận được

cảnh báo nữa nhưng điều đó cũng giải thích tại sao trước đây nó hoạt động là vì mặc dù

có nhiều hình dạng khác nhau, giá trị vẫn ở đó nên PyTorch biết phải làm gì

được rồi, vậy là xong bài giảng này và hãy xem phiên bản chính thức của mã để xem chúng ta đã kết thúc những gì

ổn rồi nên tôi chỉ muốn cập nhật nhanh một lần nữa vì tôi vẫn còn ở đây và tôi đã nói là tôi

tôi sẽ làm điều này là tôi muốn chức năng này hoạt động vì nó đẹp hơn nhiều và chúng tôi không có

để thực hiện tất cả các tính toán thủ công này nên chúng tôi đang tính toán xác suất nhập chéo và nhật ký

cụ thể là xác suất nhật ký được chọn cùng lúc thay vì tính toán tất cả nhật ký

xác suất vì vậy đó là những gì nó đang làm và bây giờ chúng ta sẽ xem cách sử dụng hàm này

vì vậy tôi đã nhận xét về hàm cũ bây giờ chúng tôi đang gọi hàm mới và chúng tôi cũng vậy

không cần phải tính toán các thăm dò nhật ký đã chọn nữa vì điều này sẽ trả lại cho chúng tôi nhật ký đã chọn

probs vì vậy đó là entropy nhật ký được chọn probs gọi hàm truyền trong nhật ký hành động và hành động

có dấu gạch dưới vì phần này chỉ dành cho những tập chưa kết thúc và sau đó khi bạn

có thể thấy điều này đang hoạt động như mong đợi được rồi vì vậy có lẽ chúng ta hãy đợi một chút để nó hoàn thành vâng

vậy là nó đã lên tới 500 khi nó giảm xuống

vì vậy điều đó sẽ xảy ra mỗi lần nó sẽ khác nhau nhưng tôi không nghĩ điều này đã thay đổi cách hoạt động của mã

đó chỉ là một cách khác để làm điều tương tự