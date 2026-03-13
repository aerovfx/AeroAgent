# 67 - CNN trên MNIST Dữ liệu tiếng Anh

---

Chào mừng mọi người.

Bây giờ chúng ta đã hiểu lý thuyết đằng sau mạng lưới thần kinh tích chập, hãy tiếp tục và bắt đầu đào tạo

một trên M rất nổi tiếng tập dữ liệu này nằm trong phần một của loạt bài giảng.

Chúng tôi sẽ chỉ tập trung vào việc đọc dữ liệu và cũng đảm bảo rằng chúng tôi hiểu được một mã hóa nóng

của các nhãn.

Hãy bắt đầu.

Được rồi.

Ở đây tôi đang ở một cuốn sổ tay.

Tôi đã nhập ENPI Peaty Numpties của Pansy cũng như matplotlib và matplotlib để tải

lên M.

Tập dữ liệu này, nó thực sự được tích hợp vào ô tô nên chúng ta có thể nói từ dòng tensor.

Doc Harris, bộ dữ liệu đó hãy tiếp tục và nhập lệnh ân xá.

Và sau đó những gì chúng ta có thể làm là tải dữ liệu vào, vì vậy và cái này bây giờ đã có tải

cuộc gọi phương thức dữ liệu.

Và về cơ bản những gì nó làm chỉ là tải tập dữ liệu lớn cho chúng ta.

Vì vậy, chúng ta sẽ sử dụng một số thao tác giải nén bộ dữ liệu ở đây vì nó thực sự đã được sắp xếp cho chúng ta ở cả hai

X Train Y đào tạo và X kiểm tra Y kiểm tra.

Chúng ta không cần phải tự thực hiện bất kỳ sự phân chia nào.

Vì vậy chúng ta sẽ nói tàu X.

tàu Y.

Và sau đó tạo một bộ khác cho phép thử X, phép thử y.

Được rồi, hãy tiếp tục tải dữ liệu đó vào và sau đó chúng ta sẽ đặc biệt giải thích các hình dạng

dữ liệu và cách biểu diễn dữ liệu.

Vì vậy, nếu tôi nhìn vào tàu X, nó trông giống như một loạt các giá trị ở đây.

Vì vậy, hãy kiểm tra hình dạng của nó.

Bạn sẽ nhận thấy tia X về cơ bản là 60000 hình ảnh và mỗi hình ảnh có kích thước 28 x 28 pixel.

Hãy tiếp tục và lấy một hình ảnh từ nguồn này.

Một hình ảnh duy nhất.

Và chúng ta sẽ nói XStream zero và lấy mục đầu tiên, vì vậy nếu bây giờ tôi xem xét một hình ảnh,

hình dạng của nó là 28 x 28 và ở đây thực sự có tất cả các giá trị thô từ đơn lẻ đó

hình ảnh.

Thật may mắn, nếu tôi có một hình ảnh hai chiều, matplotlib có một thứ gọi là EMCO

có thể hiển thị đối tượng mảng hai chiều này.

Vì vậy, chúng tôi nói Pilton, IMNSHO và tôi lấy lại con số cơ bản là số năm.

Bây giờ hãy nhớ rằng m tập dữ liệu này có thang độ xám, vì vậy nó chỉ đi từ 0 đến giá trị tối đa của

đó là năm mươi lăm.

Vì vậy ở đâu đó quanh đây chúng ta có thể thấy những điểm sáng hơn hoặc tối hơn được gắn nhãn 250

năm hoặc gần như vậy.

Điều đôi khi khiến học sinh bối rối là các em nhìn thấy một hình ảnh màu ở đây và thắc mắc,

này, tôi tưởng dữ liệu này không phải là thang độ xám, tại sao tôi lại nhìn thấy màu tím và màu vàng?

Về mặt kỹ thuật, bạn có thể chọn bất kỳ ánh xạ màu nào để hiển thị hình ảnh này.

Và nếu bạn nhớ lại khóa học trực quan hóa dữ liệu của chúng tôi, chúng tôi đã nói về bản đồ màu

có sẵn trong matplotlib.

Cái mặc định chính là cái này chuyển từ màu tím sang xanh lam, xanh lục sang vàng.

Và về mặt kỹ thuật, những gì matplotlib đang làm chỉ là đặt số 0 vào thời điểm này.

Và sau đó một hoặc hai năm mươi lăm thực sự ở điểm màu vàng này.

Và sau đó tất cả các giá trị được sắp xếp ở giữa.

Và bạn có thể thay thế nó bằng bất kỳ ánh xạ màu nào bạn muốn, và bạn có thể xuống đây và

thay thế nó bằng màu xám hoặc thay thế bằng loại đen sang trắng.

Vì vậy, có màu xám có màu đen sang trắng hoặc xám.

Vì vậy, hơi khó hiểu vì cái này có chữ E và sau đó nó chuyển từ màu trắng sang màu đen.

Vì vậy, về mặt kỹ thuật, bạn có thể hiển thị điều này trong bất kỳ loại ánh xạ màu nào bạn muốn.

Điều quan trọng cần lưu ý ngay bây giờ là các giá trị đi từ 0 đến 255,

đó là điển hình của hình ảnh.

Về cơ bản, mỗi kênh màu thường có giá trị từ 0 đến 255.

Được rồi, vậy là chúng tôi có thể hiển thị dữ liệu của một hình ảnh mà không cần khám phá các nhãn thực tế nếu

chúng ta hãy nhìn vào con tàu màu trắng.

Bạn sẽ nhận thấy rằng mảng ngay bây giờ, giá trị đầu tiên là 5, tương ứng với

giá trị đầu tiên và tập huấn luyện của chúng tôi.

Vì vậy, chúng tôi đã đúng khi cho rằng đây là số 5.

Nhưng điều sắp xảy ra hiện nay là nhãn của chúng ta chính là con số mà chúng đại diện.

Và điều sẽ xảy ra ở đây là nếu chúng ta chuyển nhãn đào tạo của mình như vậy, mạng sẽ

giả sử đó là một loại giá trị liên tục nào đó và nó sẽ cố gắng dự đoán những thứ như năm phẩy năm hoặc

năm phẩy sáu, vân vân.

Và thực sự, đây là những phạm trù.

Vậy năm không phải là một giá trị liên tục, nhưng thực ra nó là Loại năm.

Vì vậy, thực sự những gì chúng tôi đang làm ở đây là một vấn đề phân loại và chúng tôi cần đảm bảo rằng mạng của chúng tôi

hiểu điều đó.

Như đã thảo luận trước đó trong phần mạng lưới thần kinh nhân tạo, chúng ta đã nói về lý thuyết đằng sau đa lớp

vấn đề phân loại.

Và điều chúng ta cần làm là chúng ta cần một đoạn mã nóng.

Điều này và may mắn thay, vì Flow thực sự có những tiện ích cho việc này nên chúng ta có thể nói từ đó.

Tenzer flow doc keris sử dụng tính năng nhập vào phân loại.

Chúng ta sẽ tiếp tục và thực hiện điều đó, sau đó điều chúng ta sẽ làm là xem xét hình dạng của lý do tại sao

tàu, nó chỉ ghi sáu mươi nghìn vì về cơ bản có sáu mươi nghìn con số được dán nhãn ở đó.

Điều chúng ta cần làm là chuyển đổi nó thành một mã hóa nóng để mỗi số này kết thúc

lên một mã hóa để thể hiện một danh mục.

Vì vậy những gì chúng tôi sẽ làm ở đây là chúng tôi sẽ nói.

Tại sao ví dụ?

Quá phân loại.

Và nếu chúng ta nói tại sao lại đào tạo và sau đó xem hình dạng của ví dụ Y, thì giờ đây nó đã tự động có điều này

lệnh gọi hàm quá phân loại mà chúng tôi vừa tuân thủ, về cơ bản chuyển đổi là một vectơ lớp của số nguyên

thành ma trận lớp nhị phân.

Vậy bây giờ nó là một hinako cho cái này, nên nếu tôi thực sự nhìn vào ví dụ y, nó sẽ siêu lớn

mảng.

Nhưng bây giờ hãy chú ý nếu tôi nhìn vào mục đầu tiên.

Hãy chú ý điều gì xảy ra ở đây, vị trí chỉ mục thứ năm, bây giờ về cơ bản nó là vị trí chỉ ra rằng điều này thuộc về

đến lớp năm, nên nó sẽ bằng 0 một, hai, ba, bốn và năm.

Vậy nó đã biến năm cái này thành toàn bộ hàng này.

Đó là lý do tại sao hiện nay chúng tôi có 60 nghìn x 10 cho mọi thứ.

Vì vậy, chúng ta sẽ làm là chuyển đổi cả nhãn kiểm tra và nhãn đào tạo thành nhãn phân loại

nhãn.

Vì vậy, nói tại sao không thể kiểm tra được bằng hai loại.

Tại sao phải kiểm tra ngay bây giờ, nếu bạn nhấn shift ở đây, bạn sẽ nhận thấy một tham số khả thi khác mà chúng tôi có thể chuyển vào là

số lượng lớp học.

Bây giờ, tôi đã không vượt qua được số lớp khi lần đầu tiên tôi gọi đến Categorical vì đến Categorical

thực sự có thể suy ra số lượng lớp học.

Và cách thực hiện điều này chỉ đơn giản bằng cách kiểm tra xem số lượng mục duy nhất trong nhãn này là bao nhiêu

tập dữ liệu.

Vì vậy, trong trường hợp này, các số là 0 ba chín.

Vậy có thể có mười số.

Vì vậy, 10 danh mục thực tế độc đáo.

Đó là lý do tại sao tôi cho rằng có 10 ở đây.

Bây giờ, có thể có một trường hợp hiếm hoi là vì lý do nào đó bạn thiếu một phiên bản của một lớp cụ thể.

Nếu trường hợp đó xảy ra, bạn luôn có thể đảm bảo số lượng lớp học như bạn mong đợi

bằng cách nhập thủ công số lớp trong trường hợp này bằng 10.

Và chúng ta sẽ tiếp tục làm điều tương tự với tàu hỏa.

Vì vậy, chúng tôi sẽ nói rằng chúng tôi đào tạo và bây giờ chúng tôi có thể chỉ định số lượng lớp theo cách thủ công.

Dù bằng cách nào thì nó cũng sẽ hoạt động, vì thực tế là cả tập kiểm tra và tập huấn luyện của chúng tôi đều chứa

trường hợp của tất cả các lớp có thể.

Vì vậy, chúng tôi cũng sẽ tiếp tục và chạy nó.

Và nói chung, để thực sự có một bộ dữ liệu machine learning phù hợp cần có những trường hợp

của mỗi lớp trong cả bài kiểm tra và đào tạo.

Và nếu không phải như vậy thì đó thường là dấu hiệu cho thấy có vấn đề với tập dữ liệu thực tế của bạn.

OK, bây giờ là lúc bình thường hóa dữ liệu huấn luyện.

Hãy nhớ lại rằng dữ liệu đào tạo của chúng tôi chỉ là dữ liệu hình ảnh.

Vì vậy, nếu tôi nhìn lại hình ảnh đó một lần nữa, giá trị của tôi sẽ tăng từ 0 đến 255.

Vì vậy, nếu tôi kiểm tra mức tối đa thực tế ở đây.

Đó là hai trăm năm mươi lăm và giá trị tối thiểu bằng 0, và để đảm bảo tôi không gặp phải bất kỳ độ dốc nào

các vấn đề, chúng phải có thang đo từ 0 đến 1.

Có một vài cách tiếp cận khác nhau mà chúng ta có thể thực hiện.

Chúng ta có thể thực hiện một cách tiếp cận cổ điển từ ESC, tìm hiểu rằng quá trình tiền xử lý nhập đại lượng vô hướng tối thiểu đó

và sau đó chạy nó trên cả tập kiểm tra và tập huấn luyện.

Và hãy nhớ lại khi chúng ta sử dụng đối tượng vô hướng tối thiểu hoặc bất kỳ đại lượng vô hướng nào từ lern, chúng ta phù hợp với

dữ liệu huấn luyện và sau đó chuyển đổi trên dữ liệu thử nghiệm.

Tuy nhiên, tôi tiếp tục đề cập đến điều đó bởi vì chúng tôi chỉ phù hợp với dữ liệu huấn luyện vì tôi không muốn giả định

kiến thức trước đây về dữ liệu thử nghiệm của tôi.

Nhưng chúng ta có một trường hợp đặc biệt ở đây vì chúng ta đang xử lý hình ảnh và tôi có thể giả định rằng

những hình ảnh trong tương lai mà tôi sắp đưa vào mô hình này mà nó chưa thấy sẽ được chia tỷ lệ thành

chỉ là những hình ảnh bình thường có phạm vi từ 0 đến 255.

Vì vậy, một cách dễ dàng để ngay lập tức giữ tất cả các giá trị từ 0 đến 1 là nói đơn giản X train là

bằng X tàu chia cho hai năm mươi lăm và sau đó tôi có thể thực hiện tương tự.

Chức năng ở đây trong bài kiểm tra X và cho biết bài kiểm tra X bằng bài kiểm tra X chia cho hai năm mươi lăm.

Và lý do, một lần nữa, tôi có thể làm điều đó là vì tôi biết rằng những hình ảnh trong tương lai, nhân tiện, chúng

được xây dựng với các kênh màu đỏ, lục, lam phải luôn có giá trị từ 0 đến 255.

Vì vậy, tỷ lệ của tôi về cơ bản sẽ không thay đổi.

Các tính năng này về cơ bản đã được biết đến cả ở thời điểm hiện tại và cho các hình ảnh trong tương lai.

Và bây giờ nếu tôi nhìn vào một hình ảnh được chia tỷ lệ, hãy tiếp tục và nói rằng hình ảnh được chia tỷ lệ bằng X tàu

ở mức không.

Bây giờ hãy nhìn vào hình ảnh được chia tỷ lệ và bạn sẽ nhận thấy tất cả các giá trị về cơ bản đi từ 0 đến

một.

Và điều đó sẽ hoạt động tốt hơn nhiều đối với mạng thực tế.

Và nếu chúng ta nhìn vào giá trị tối đa thì bây giờ nó là một.

Và hãy nhớ rằng nếu bạn nói IMNSHO, vì tỷ lệ của mọi thứ vẫn như nhau nên tỷ lệ

hình ảnh sẽ trông khá giống hệt trước đây.

Được rồi, bước cuối cùng để xử lý dữ liệu của chúng ta là định hình lại dữ liệu.

Ngay bây giờ, nếu chúng ta nhìn vào hình dạng của dữ liệu huấn luyện, nó sẽ là nghìn nhân hai mươi tám nhân hai mươi

tám.

Vì vậy, điều này đúng cho một mạng lưới thần kinh tích chập.

Nhưng chúng ta cần thêm một thứ nguyên nữa để cho mạng biết rằng chúng ta đang xử lý một kênh RGB duy nhất.

Về cơ bản, hình ảnh có màu đen và trắng.

Vì vậy, chúng tôi chỉ có một kênh màu hình ảnh duy nhất từ ​​0 đến 1 trong trường hợp của chúng tôi.

Và trước khi bình thường hóa thực tế, nó là từ 0 đến 255.

Trong loạt bài giảng tiếp theo.

Khi xử lý hình ảnh màu, chúng tôi sẽ đảm bảo chỉ định đây là kích thước ba, một cho màu đỏ,

một cho màu xanh lá cây và một cho màu xanh lam.

Vì vậy, tất cả những gì chúng ta sắp làm ở đây là chúng ta sẽ nói đoàn tàu X bằng đoàn tàu X.

Hãy đảm bảo rằng tôi tuân theo quy ước tương tự của mình và nói rằng hãy định hình lại.

Sáu mươi nghìn.

28 x 28, dấu phẩy, rồi chúng ta sẽ thêm một.

Vì vậy, về cơ bản những gì chúng ta có ở đây là.

Kích thước lô trong trường hợp này, các lô, tất cả các hình ảnh, vì vậy thực sự về cơ bản nó chỉ là tất cả các hình ảnh.

Lô này lớn cỡ nào?

Vì vậy, kích thước lô và sau đó chúng ta có chiều rộng.

Theo chiều cao.

Theo kênh màu, trong trường hợp của chúng ta, chúng ta chỉ có một kênh màu vì những hình ảnh này về cơ bản là

ở dạng đen trắng, nên chúng tôi chạy cái này và từ sáu mươi nghìn lần hai mươi tám lần, hai mươi tám lần

lần một bằng 60 nghìn lần, hai mươi tám lần hai mươi tám, không có vấn đề gì với

tôi định hình lại chúng tôi bằng cách thêm vào loại kênh màu trống khác này hoặc chỉ một phiên bản duy nhất của

kênh màu.

Và chúng ta sẽ làm điều tương tự cho bài kiểm tra X.

Kiểm tra X bằng kiểm tra X và chúng tôi định hình lại kết quả này thành mười nghìn.

Và bạn có thể xác nhận rằng đó là con số đúng bằng cách chỉ kiểm tra hình dạng dư thừa hiện tại.

Vì vậy, có 10000 hình ảnh trong bộ thử nghiệm.

Tất nhiên chúng cũng có kích thước 28 x 28 và chúng cũng có thang độ xám.

Được rồi, đó thực sự là cách xử lý trước dữ liệu khi chúng ta xử lý dữ liệu hình ảnh thực như PGS

và JPEG mà chúng ta sẽ thực hiện sau trong phần này của khóa học, sẽ có một chút

tham gia nhiều hơn vào việc xử lý trước dữ liệu, chia tỷ lệ và thực sự thực hiện các phép biến đổi

trên tập dữ liệu.

Nhưng thật may mắn cho chúng ta, tập dữ liệu này về cơ bản được thiết kế đặc biệt để tìm hiểu về tích chập

mạng lưới thần kinh.

Vì vậy, chúng tôi đã thiết lập mọi thứ cho đến khi xử lý trước dữ liệu.

Và điều tiếp theo chúng ta sẽ làm là thảo luận về việc đào tạo và tạo mô hình.

Cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.