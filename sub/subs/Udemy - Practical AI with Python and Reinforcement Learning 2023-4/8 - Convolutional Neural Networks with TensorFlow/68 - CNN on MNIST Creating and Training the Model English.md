# 68 - CNN về MNIST Tạo và đào tạo tiếng Anh mẫu

---

Chào mừng trở lại, mọi người.

Trong bài giảng này, chúng ta sẽ tập trung vào việc tạo mô hình và đào tạo mô hình, đồng thời chúng ta cũng

sẽ nhấn mạnh các khía cạnh của mô hình mà bạn có thể thử nghiệm và chỉnh sửa so với các khía cạnh

điều đó, dựa trên những hạn chế của vấn đề của bạn, về cơ bản phải luôn được khắc phục.

Được rồi, hãy bắt đầu bằng cách quay lại sổ ghi chép.

Được rồi.

Đây là sổ ghi chép mà chúng ta đã dừng lại lần trước, giống như trước đây, khi chúng ta tạo mô hình,

chúng ta sẽ nói từ.

Các bác sĩ về dòng chảy căng thẳng cho rằng các mô hình nhập và sẽ nhập, trình xây dựng mô hình tuần tự vẫn sẽ xây dựng

mô hình của chúng tôi một cách tuần tự bằng cách thêm các lớp.

Sự khác biệt chính là loại lớp mà chúng tôi thực sự thêm vào này.

Vì vậy, chúng tôi sẽ nói từ dòng chảy Tensor, Tiến sĩ Harris, rằng các lớp nhập và chúng tôi sẽ nhập một lớp dày đặc

giống như chúng ta đã làm trước đây, nhưng cũng là lớp tích chập để xử lý hình ảnh 2D, điều này rất phổ biến

đến Capital D và sau đó cũng tối đa hóa số tiền này.

Và cuối cùng, chúng ta cần làm phẳng những hình ảnh này để đưa nó vào các lớp dày đặc cuối cùng,

sẽ thực sự thực hiện việc phân loại.

Vì vậy, có một lớp phẳng đặc biệt cho việc đó.

Được rồi, vậy hãy bắt đầu xây dựng mô hình của chúng ta và chúng ta sẽ tập trung vào một vài tham số xuyên suốt

việc thêm các lớp thực tế.

Vì vậy, ngay trước khi chúng ta bắt đầu xây dựng mô hình tuần tự, điều tiếp theo cần làm thường là

cho một mạng lưới thần kinh tích chập.

Lớp đầu tiên mà nó gặp phải là lớp tích chập.

Vì vậy, chúng ta sẽ nói mô hình cộng và tôi sẽ thêm tích chập.

Để viết hoa dấu ngoặc đơn và nếu bạn thực hiện tab shift ở đây, nó sẽ hiển thị cho bạn chuỗi tài liệu.

Hãy nhớ rằng chúng tôi đã nhập nó và chúng tôi có dấu ngoặc đơn ở đây để tôi có thể xem tài liệu

chuỗi khác.

Nó được gọi là trợ giúp trong cuộc gọi lớp thực tế.

Nhưng có bốn thông số chính mà tôi muốn giải thích cơ bản cho bạn ở đây, đó là các bộ lọc,

kích thước hạt nhân, các bước tiến và chuỗi đệm.

Bây giờ chúng ta thực sự đã hiểu các bộ lọc, kích thước hạt nhân, Streit và phần đệm dựa trên lý thuyết

tắt các bài giảng lý thuyết mà chúng ta vừa xem qua.

Điều chính chúng ta phải tìm ra là tôi chọn những giá trị nào cho việc này?

Và nhiều khi không có câu trả lời đúng một trăm phần trăm.

Nó gần như dựa trên dữ liệu đầu vào được đưa vào.

Vì vậy, các giá trị thực sự điển hình cho số lượng bộ lọc là tập dữ liệu càng phức tạp.

Vì vậy, về cơ bản, hình ảnh càng lớn thì hình ảnh càng đa dạng và bạn càng thử nhiều lớp học

để phân loại thì bạn càng nên có nhiều bộ lọc.

Và việc chọn các bộ lọc dựa trên lũy thừa của hai là điều thực sự phổ biến.

Vì vậy, điểm khởi đầu rất phổ biến cho một số bộ lọc có thể là khoảng 32.

Nhưng bạn có thể tưởng tượng rằng nếu bạn đang xử lý một tập hợp các hình ảnh thực sự lớn và có thể

bạn đang cố gắng phân loại thứ gì đó như số lượng hoặc loại biển báo đường bộ.

Vì vậy, bạn có biển báo dừng, biển báo nhường đường, rẽ trái, rẽ phải và bạn có rất nhiều lớp học.

Có lẽ sẽ hợp lý nếu bạn thêm nhiều bộ lọc hơn để cố gắng bắt đầu hiểu hoặc hiểu được phép tích chập của mình.

mạng lưới thần kinh hiểu được các hình dạng khác nhau đi kèm với tất cả các dấu hiệu khác nhau này.

Bây giờ, trong trường hợp của chúng tôi, chúng tôi có tập dữ liệu thực sự đơn giản chỉ gồm các số viết tay trong đó chúng tôi có mười lớp.

Vì vậy, nó lọc với công suất ba mươi hai hoặc xin lỗi, với giá trị được chọn là ba mươi hai là tốt

bước để bắt đầu ở bước tiếp theo.

Chúng ta cần phải quyết định rằng kích thước hạt nhân hình ảnh và một lần nữa, kích thước điển hình của hạt nhân hình ảnh là một cái gì đó

trong phạm vi hai nhân hai hoặc bốn nhân bốn, sau đó bạn có thể tiếp tục mở rộng nó dựa trên

dữ liệu.

Điểm khởi đầu tốt cho việc này là 4/4.

Được rồi, vậy còn hai thông số còn lại mà chúng ta đã thảo luận trên lý thuyết thì sao?

Vì vậy, cái tiếp theo là cạnh hoặc kích thước của Streit.

Và có hai chiều ở đây, bởi vì bạn có thể nhìn thấy ngay cả X và Y và nhớ lại rằng sải chân

về cơ bản thì chúng ta đã đạt được bước tiến lớn như thế nào khi di chuyển hạt nhân dọc theo hình ảnh này?

Trong trường hợp của chúng tôi, hình ảnh thử nghiệm thực sự khá nhỏ.

Chúng chỉ có kích thước 28 x 28 pixel.

Và vì hạt nhân của chúng tôi có kích thước 4 x 4 nên chúng tôi thực sự có thể xác định thời gian hoặc về cơ bản là bao lâu.

sẽ cần bao nhiêu pixel để vượt qua chỉ bằng cách nói hai mươi tám chia cho bốn.

Bạn có thể hình dung được việc quét hình ảnh đó.

Nếu bạn đang xử lý những hình ảnh thực sự lớn và bạn vẫn đang xử lý một hạt nhân nhỏ hơn, bạn sẽ

có lẽ muốn mở rộng kích thước sải chân đó trong trường hợp của chúng tôi.

Vì vậy, chúng ta sẽ tiếp tục và để mặc định chỉ từng pixel một.

Vì vậy, về cơ bản chỉ cần di chuyển theo mặc định, pixel này sang pixel tiếp theo, pixel 10x, v.v. và sau đó là

tiếp theo là phần đệm.

Và nếu bạn nhìn vào phần đệm, nó sẽ hợp lệ.

Vì vậy, đó là một mã chuỗi hợp lệ.

Và nếu chúng ta cuộn xuống đây, bạn sẽ nói rằng nó hợp lệ hoặc giống nhau và đó là hai điều duy nhất của bạn

tùy chọn.

Vậy những chuỗi này thực sự có ý nghĩa gì nếu bạn thực hiện tìm kiếm nhanh trên Google để biết sự khác biệt giữa

hợp lệ và giống nhau trong chuỗi, bạn sẽ nhận được liên kết tuyệt vời này tới một bài đăng tràn ngăn xếp về cơ bản nói về

về sự khác biệt giữa phần đệm giống nhau và phần đệm hợp lệ này là gì?

Và điều này thực sự liên quan đến dòng chảy căng thẳng của Mac.

Nhưng đó cũng là mã dành cho Keris.

Và nếu chúng ta đến đây, sẽ có một ví dụ ở đây nói về bảng giống nhau và bảng hợp lệ.

Nhưng tôi thích một số ví dụ trực quan hơn.

Và có lẽ lời giải thích rõ ràng nhất là nếu bạn kéo xuống đây, điều rõ ràng nhất đối với tôi về cơ bản là

lời giải thích nhanh chóng này ngay tại đây.

Và nó hướng về phía dưới.

Tất cả những lời giải thích này về cơ bản đều nói lên cùng một điều, nhưng về cơ bản, chuỗi hợp lệ sẽ cho bạn biết

không áp dụng bất kỳ phần đệm nào.

Điều chúng ta sắp làm là giả sử rằng tất cả các kích thước đều hợp lệ để hình ảnh đầu vào

hoàn toàn được bao phủ bởi bộ lọc và bước tiến mà tôi đã chỉ định.

Vậy điều đó có xảy ra ở đây không?

Vâng, chúng ta hãy suy nghĩ về điều này.

Nếu tôi có hai mươi tám và tôi chia nó cho bốn, thì sẽ bằng bảy lần và tôi chỉ đang cưỡi ngựa

của một.

Vì vậy, nếu tôi chỉ di chuyển hạt nhân của mình, có kích thước 4 x 4 dọc theo hình ảnh 28 x 28, tôi

không cần phải có đệm vì tôi thực sự sẽ không vượt quá giới hạn vì tôi hoàn toàn phù hợp với

bước tiến của một.

Nhưng nếu nó bắt đầu đưa ra các số thập phân, bạn có thể gặp phải một số lỗi vì bạn đang

vượt mức.

Và trong trường hợp đó, chúng ta phải quyết định liệu chúng ta có bỏ những điểm đó không?

Chúng ta sẽ đệm nó bằng số không hay số một, v.v.?

Và do đó, điều chúng tôi làm là phải chỉ định chuỗi.

Giống nhau, rất đẹp.

Điều thú vị là chúng tự động tìm ra phần đệm sẽ là gì.

Vì vậy, những gì xảy ra ở đây là.

Nó sẽ chỉ áp dụng phần đệm cho đầu vào nếu cần để hình ảnh đầu vào được bao phủ hoàn toàn bởi

bộ lọc và stria mà bạn đã chỉ định.

Vì vậy, ví dụ: nếu chúng tôi quyết định chọn trạng thái đảm bảo rằng kích thước hình ảnh đầu ra giống nhau

làm hình ảnh đầu vào.

OK, vậy có rất nhiều cách giải thích khác ở đây, một cách giải thích về mặt toán học và một cách giải thích khác

ở đây cho bạn thấy về cơ bản điều này đang thực hiện thông qua một chút giải thích trực quan.

Vì vậy, tôi khuyến khích bạn rằng nếu bạn chỉ tìm kiếm trên Google, nếu chúng tôi quay lại đây hợp lệ so với cùng một phần đệm, thì bạn

nhận được rất nhiều kết quả đầu ra ở đây.

Được rồi, một lần nữa, bạn có thể xem những giải thích đó trong trường hợp của chúng ta, chúng ta sẽ tiếp tục và giữ nguyên mặc định,

cái này sẽ hoạt động tốt với chúng tôi trong trường hợp của chúng tôi hoặc chúng tôi chỉ có vậy.

Phần đệm là hợp lệ.

OK, đó là bộ lọc và ký hiệu đại tá của chúng tôi, một số thứ chúng tôi cần thêm vào bây giờ là xác định

hình dạng đầu vào mà chúng ta mong đợi ở đây là gì.

Vậy là nó sẽ như vậy.

Hình dạng đầu vào bằng và trong trường hợp của chúng tôi, đó chỉ là hình dạng đầu vào cho một hình ảnh, bằng hai mươi

tám x hai mươi tám kênh một màu.

Và cuối cùng, chúng tôi chọn loại chức năng kích hoạt mà chúng tôi muốn.

Vì vậy hàm kích hoạt sẽ chọn được hiệu chỉnh.

Đơn vị tuyến tính.

Vì vậy, nói kích hoạt.

Bằng đơn vị tuyến tính được chỉnh lưu.

Được rồi, hãy đặt tất cả những điều này trên một dòng ở đây và tôi có thể thu nhỏ lại một chút để chúng ta có thể thấy

toàn bộ cuộc gọi.

Tích chập của chúng tôi ở đây có một số số lượng bộ lọc được xác định.

Đó là kích thước hạt nhân.

Nếu muốn, chúng ta có thể chỉ định phần đệm.

Nhưng trong trường hợp này, chúng tôi không cần phải làm vậy.

Và sau đó chúng ta có thể chỉ định hình dạng đầu vào và hàm kích hoạt.

OK, đó là lớp chập của chúng ta.

Sau lỗi chập, bạn sẽ có một lớp kéo.

Bạn sẽ nói mô hình thêm.

Và ở đây tôi sẽ gọi Max Poole đến.

Và điều chính cần chọn ở đây là kích thước hồ bơi.

Bạn cũng có thể thêm vào những thứ như bước tiến, lớp đệm, v.v., nhưng yếu tố thực sự quan trọng là kích thước hồ bơi.

Và chúng ta sẽ tiếp tục và tạo kích thước nhóm bằng một nửa kích thước hạt nhân của chúng ta.

Hai nhân hai là một điều thực sự phổ biến.

Số liệu ở đây.

Vì vậy, chúng ta sẽ tiếp tục và chỉ nói kích thước nhóm là hai nhân hai, đó là mặc định.

Vì vậy, về mặt kỹ thuật, tôi không cần phải chỉ rõ điều đó, nhưng tôi muốn mọi người biết rõ những gì tôi đang làm ở đây.

OK, bây giờ chúng ta sẽ giữ nó như có một lớp không khí xoắn và một lớp kéo.

Vì vậy, mạng lưới thần kinh tích chập rất đơn giản.

Bây giờ, những gì tôi có thể làm là tiếp tục thêm các lớp xoắn và lớp kéo, và chúng ta sẽ làm điều đó sau cho

hình ảnh phức tạp hơn.

Nhưng bây giờ, chúng ta sẽ chỉ làm nó đơn giản thôi.

Một lớp chập, một lớp kéo sau hàng loạt lớp chập và lớp đệm của bạn.

Bạn sẽ cần phải làm phẳng các hình ảnh.

Vì vậy, khi chúng ta làm phẳng các hình ảnh, điều đó về cơ bản có nghĩa là lấy một hình ảnh có kích thước 28 x 20 và

sau đó làm phẳng nó thành một mảng duy nhất trong trường hợp của chúng ta, bảy trăm tám mươi bốn điểm.

Vì vậy, hãy lấy một trong hai hình ảnh này rồi làm phẳng nó thành một mảng bảy tám mươi bốn.

là hai mươi tám lần hai mươi tám.

Vì vậy, chúng ta có thể làm điều đó bằng cách nói thêm mô hình.

Và sau đó chúng ta làm phẳng hình ảnh khi chúng ta có thể làm phẳng hình ảnh, điều chúng ta có thể làm là chúng ta có thể

bắt đầu thêm vào các lớp dày đặc của chúng ta và thông thường bạn nên thêm vào một lớp dày đặc cuối cùng.

Điều đó ít nhiều phù hợp với cùng một thang đo của cái này, vì vậy thang đo phải nằm ở khoảng từ 0 đến

một nghìn.

Chúng ta sẽ tiếp tục nói dày đặc và chúng ta sẽ giữ sức mạnh của hai chủ đề ở đây.

Và chúng ta sẽ nói 120 nơ-ron trong quá trình kích hoạt Stanzler bằng đơn vị tuyến tính được chỉnh lưu.

Và nếu muốn, bạn có thể tiếp tục thêm các lớp dày đặc.

Nhưng cuối cùng chúng ta cũng có lớp đầu ra cuối cùng.

Vậy lớp đầu ra cuối cùng của tôi nên có bao nhiêu nơ-ron?

Trong trường hợp phân loại này, tôi nên có một nơron cho mỗi lớp.

Vì vậy, đó sẽ là một lớp dày đặc với 10 nơ-ron.

Và trong trường hợp này, tôi cũng phải nghĩ đến chức năng kích hoạt, chức năng này dành cho phân loại nhiều lớp

vấn đề.

Không phải là lớp nhị phân, mà là đa lớp phải là hàm kích hoạt softmax.

Vì vậy, một lần nữa, nó sẽ là softmax vì đây là a.

Vấn đề đa lớp.

Cuối cùng, tôi sẽ biên dịch mô hình này.

Biên dịch.

Mất mát bằng phân loại.

Entropy chéo.

Xuyên quốc gia được phân loại, vì đây là vấn đề đa lớp nên trình tối ưu hóa sẽ tiếp tục và chọn

Atem dành cho Trình tối ưu hóa và ở đây, nếu muốn, tôi có thể chỉ định các số liệu bổ sung, đây thực sự là một thứ gì đó

chúng tôi chưa từng thấy trước đây

Nhưng tôi có thể nói.

Hãy tiếp tục và thêm vào một số số liệu bổ sung, thông thường những gì chúng tôi làm là sử dụng tổn thất làm thước đo của mình, về cơ bản

tính toán tổn thất từ hàm mất mát của chúng tôi, đó là entropy phân loại.

Nhưng điều tôi có thể làm là tôi cũng có thể theo dõi những thứ như độ chính xác.

Và nếu bạn muốn kiểm tra xem mã chuỗi nào có sẵn cho bạn hoặc số liệu nào có sẵn cho bạn

bạn, bạn có thể truy cập số liệu cắt giảm Kerrisdale Io.

Vì vậy, nếu tôi tiếp tục và sao chép cái này rồi dán nó vào đây vào tài liệu gây tò mò, nó thực sự sẽ

hiển thị cho bạn các số liệu có sẵn.

Trên thực tế, có chủ đề về độ chính xác theo phân loại, nhị phân, v.v. sao chép số liệu của câu lạc bộ và bạn có thể

thậm chí tạo số liệu tùy chỉnh của riêng bạn.

Vì vậy, có rất nhiều lựa chọn ở đây mà chúng ta có thể tiếp tục xem xét.

Vì vậy, chúng tôi sẽ tiếp tục và chỉ chọn độ chính xác, về cơ bản là độ chính xác trên tất cả các danh mục trong trường hợp của chúng tôi

và chúng ta sẽ để nó như vậy, chúng ta vẫn có thể tính được tổn thất.

Nhưng đây chỉ là một số liệu khác mà chúng tôi có thể ghi lại trong quá trình đào tạo.

Chúng tôi sẽ tiếp tục và biên dịch mô hình, đảm bảo rằng chúng tôi không mắc bất kỳ lỗi chính tả nào và chúng tôi đã sẵn sàng.

Được rồi.

Vì vậy, tôi muốn nhanh chóng làm nổi bật những gì bạn có thể chơi và những gì phải nói.

Hãy bắt đầu bằng cách thảo luận về các tham số cố định và cần được xác định theo thực tế của bạn.

tập dữ liệu.

Những thông số đó là hình dạng đầu vào của bạn.

Hình dạng đầu vào về cơ bản phải khớp với hình ảnh sẽ trông như thế nào.

Trong trường hợp của chúng tôi, đó là hình ảnh kênh 28 x 28 một màu.

Tham số hình dạng đầu vào này được xác định bởi dữ liệu của bạn.

Sau các lớp chập và bạn đang kéo các lớp, cuối cùng bạn sẽ phải làm phẳng

dữ liệu của bạn.

Vì vậy, đây là một tham số khác, về cơ bản là một lớp sẽ nằm ở đâu đó trong mạng của bạn.

Sau đó, một vài tham số cuối cùng mà bạn sẽ chỉnh sửa và nên được đặt dựa trên dữ liệu của bạn là đây

lớp dày đặc cuối cùng.

Lớp dày đặc này phải bằng số lượng nơ-ron trong lớp của bạn.

Vì vậy, chúng tôi có mười lớp học có thể.

Các số từ 0, 2, 3 cho đến chín.

Vậy tôi nên có 10 nơ-ron ở đây.

Và hàm kích hoạt khi đó sẽ là softmax.

Nếu bạn đang giải quyết một vấn đề phân loại nhị phân, chẳng hạn như chỉ là hình ảnh của một con mèo so với một con chó,

thì đây sẽ là phân loại nhị phân chỉ có một năm đầu ra, với việc kích hoạt sigmoid.

Và điều khác được xác định bởi vấn đề của bạn là loại tổn thất.

Và ở đây trong trường hợp của chúng ta, đó là entropy chéo phân loại.

Được rồi, bây giờ vấn đề là bạn có thể chơi đùa với một số ở đây.

Bạn có thể thêm bao nhiêu lớp xoắn và lớp kéo tùy thích.

Và sau đó, trong đó bạn có thể thử nghiệm với một số bộ lọc, kích thước hạt nhân cũng như

kích thước hồ bơi.

Và bạn cũng có thể chơi đùa với phần đệm.

Sau đó, sau khi bạn làm phẳng nó ra, bạn có thể thử nghiệm với số lớp dày đặc như

cũng như số lượng tế bào thần kinh trong các lớp đó.

Và thông thường mọi người chỉ sử dụng một lớp dày đặc, có thể là hai lớp, sau khi họ làm phẳng nó ra.

Chúng không có nhiều lớp dày đặc như vậy.

Sau khi làm phẳng phần lớn công việc đối với dữ liệu ảnh, cần thực hiện bằng phép chập và kéo

lớp?

Được rồi, tôi chỉ muốn thảo luận ngắn gọn về những gì bạn có thể sử dụng

với và những gì nên được thiết lập bởi dữ liệu của bạn.

Được rồi, bây giờ, điều cuối cùng chúng ta muốn thiết lập là huấn luyện mô hình để đảm bảo rằng chúng ta không cần

phải lo lắng về việc chọn một số thời đại.

Hãy tiếp tục và thiết lập điểm dừng sớm trong cuộc gọi lại, chúng tôi sẽ nói, từ Tenzer flow, Doc Harris,

doc dự phòng.

Hãy tiếp tục và nhập khẩu.

Dừng sớm rồi dừng sớm sẽ bằng dừng sớm, chúng ta quyết định muốn theo dõi điều gì.

Theo mặc định, chúng tôi theo dõi việc mất xác thực, nhưng hãy nhớ rằng số liệu khác mà chúng tôi có thể theo dõi

là độ chính xác xác thực vì tôi đã thêm độ chính xác của số liệu ở đây, tôi có thể nói độ chính xác gạch dưới của Vall

với tư cách là người giám sát thiết bị của tôi, nhưng chúng tôi sẽ tiếp tục và giữ nó ở mức tổn thất do kết quả đầu ra theo phân loại chéo

entropy.

Và sau đó chúng tôi chỉ định một số bệnh nhân để chúng tôi có thể chỉ định một số thứ như bệnh nhân một hoặc bệnh nhân hai.

Chúng ta sẽ vào và đặt nó cho bệnh nhân.

Vì vậy, một kỷ nguyên chạy theo điều đó và bây giờ chúng ta sẽ nói mô hình phù hợp.

Chuyển dữ liệu huấn luyện của chúng tôi và sau đó để biết lý do thu hồi, chúng tôi muốn chuyển vào phiên bản phân loại của những dữ liệu này

nhãn, cũng đạt kỷ nguyên tương đối cao 10 và sau đó chúng tôi cần đảm bảo rằng chúng tôi cũng vượt qua được

tập dữ liệu xác thực.

Vậy đây sẽ là bài kiểm tra X.

Và cũng nên có sự phân loại như bài kiểm tra đó.

Và cuối cùng, để đảm bảo rằng chúng ta thực sự dừng sớm, chúng ta sẽ nói số lần gọi lại bằng.

Dừng sớm.

OK, chúng ta hãy tiếp tục và điều chỉnh mô hình đó, đảm bảo chúng ta không mắc bất kỳ lỗi chính tả nào ở trên và có vẻ như nó

đang làm việc cho chúng tôi.

Bạn luôn có thể thấy chúng tôi đạt được độ chính xác rất cao ngay lập tức.

Đây là một bộ dữ liệu khá dễ dàng để làm việc.

OK, vậy thì trong bài giảng tiếp theo, sau khi huấn luyện xong mô hình, chúng ta sẽ đánh giá khả năng của mô hình

hiệu suất.

Tôi sẽ gặp bạn ở đó.