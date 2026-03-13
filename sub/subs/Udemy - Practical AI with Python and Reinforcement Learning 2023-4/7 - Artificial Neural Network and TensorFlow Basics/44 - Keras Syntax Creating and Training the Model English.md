# 44 - Cú pháp Keras Tạo và huấn luyện tiếng Anh mô hình

---

Chào mừng mọi người đến với phần hai của Keris, Syntex, BASIX, trong phần hai.

Chúng tôi sẽ tập trung vào việc tạo mô hình, chạy mô hình của mình và sau đó thực sự tạo ra các dự đoán

từ mô hình ở phần ba.

Sau phần này, chúng ta sẽ tập trung vào cách đánh giá thực tế hiệu suất của mô hình cũng như cách dự đoán

trên các tập dữ liệu hoàn toàn mới, lưu và tải các mô hình của chúng tôi.

Hãy quay lại sổ ghi chép để tiếp tục nơi chúng ta đã dừng lại lần trước.

Được rồi.

Tôi đang ở cuốn sổ mà chúng ta đã dừng lại lần trước.

Vì vậy, chúng tôi đã đọc dữ liệu của mình và sau đó chỉ phân tích một chút về nó.

Về cơ bản, hãy hình dung cốt truyện đó và chúng tôi đã thu nhỏ dữ liệu nổi bật của mình.

Vì vậy, bây giờ bước tiếp theo là tạo mô hình theo cú pháp.

Và để làm được điều này, chúng ta cần phải làm gì với việc nhập khẩu.

Chúng ta sẽ nói từ luồng Tenzer mang theo và đây là cách API được đóng gói bên trong luồng Tenzer,

chúng tôi chỉ nói từ luồng cảm biến mang theo và sau đó chúng tôi có thể thực hiện bất kỳ thao tác nhập nào mà chúng tôi muốn, như thể chúng tôi đã thực hiện rồi

đã cài đặt Castlebury riêng biệt.

Và cái đầu tiên chúng ta sẽ nhập là mô hình tuần tự.

Và điều tiếp theo chúng ta sẽ làm là nói từ Tenzer Flow, Dakara, Stop Layer's.

Chúng tôi sẽ nhập khẩu từ chối.

Và tất cả những gì chúng ta cần để xây dựng một mô hình rất đơn giản về cơ bản là những gì chúng ta làm là thiết lập một chuỗi cơ sở

mô hình và sau đó tiếp tục thêm các lớp vào đó.

Và trường hợp này sẽ chỉ thêm một lớp đơn giản, dày đặc.

Tôi cũng thực sự khuyên bạn rằng nếu bạn gọi trợ giúp theo một trong hai cách này, chẳng hạn như trợ giúp tuần tự, thì sẽ có

tài liệu thực sự hay và nhiều ví dụ khác nhau bên trong tài liệu.

Vì vậy, nó thực sự cho bạn thấy rất nhiều điều chúng ta sẽ làm, đó là cách xây dựng mô hình và sau đó

làm thế nào để thêm các lớp vào nó, v.v.

Vì vậy, có rất nhiều ví dụ thực sự thú vị ở đây, không chỉ về trình tự, mà nếu bạn cũng xem qua dence,

nó sẽ cung cấp cho bạn nhiều thông tin về các thông số khác nhau cần có.

Và nếu bạn cuộn xuống, cuối cùng bạn cũng sẽ thấy một số ví dụ.

Nhưng hãy tiếp tục và tìm hiểu xem chúng ta có thể thực sự làm được điều này như thế nào ngay bây giờ.

Có hai cách để tạo mô hình dựa trên KERIS.

Một cách là gọi tuần tự.

Và sau đó chuyển danh sách các lớp thực tế mà bạn muốn, vì vậy tôi sẽ chuyển qua một lớp dày đặc và nếu

chúng ta hãy nhìn vào dence, tất cả điều này có nghĩa là nếu chúng ta mở rộng về điều này, đó là một sự kết nối thường xuyên, dày đặc

lớp mạng nơ-ron.

Và tất cả điều đó có nghĩa là nếu thứ gì đó được kết nối dày đặc, thì đó sẽ là mạng chuyển tiếp thông thường

trong đó mọi nơ-ron được kết nối với mọi nơ-ron khác ở lớp tiếp theo.

Sau này, chúng ta sẽ tìm hiểu về các lớp phức tạp hơn.

Nhưng lớp dày đặc là thứ chúng tôi đang làm việc với mạng lưới thần kinh nhân tạo cơ bản của chúng tôi.

Bạn cũng sẽ nhận thấy rằng nó có khá nhiều lệnh gọi tham số bên trong.

Hai lệnh gọi tham số mà chúng ta cần lưu ý lúc này là đơn vị và đơn vị kích hoạt chỉ là

một từ khác cho tế bào thần kinh.

Về cơ bản, có bao nhiêu nơ-ron thực sự có trong Slayer?

Và sau đó quá trình kích hoạt thực hiện một lệnh gọi chuỗi để biết các nơ-ron này sẽ sử dụng chức năng kích hoạt nào,

họ có nên sử dụng kích hoạt sigmoid, đơn vị tuyến tính được chỉnh lưu, v.v.

Vì vậy ngay bây giờ, điều chúng tôi sắp làm là chỉ cho bạn cách chúng tôi có thể xây dựng một mạng lưới.

Hãy tưởng tượng tôi muốn lớp đầu tiên của mình có bốn nơ-ron, được kết nối chặt chẽ với nhau, nghĩa là mọi nơ-ron đều

được kết nối với mọi nơ-ron khác.

Và sau đó chúng ta có thể nói kích hoạt của tôi.

Và tôi có thể nói điều gì đó giống như ELU của chúng tôi, viết tắt của đơn vị Rectified Linnear, và nếu bạn bối rối

về các hàm kích hoạt này, hãy đảm bảo bạn quay lại và xem các phần lý thuyết của phần này

của khóa học.

Nhưng hy vọng bạn có thể thấy mối liên hệ ở đây giữa những gì chúng ta đã thảo luận trên lý thuyết với những gì chúng ta đang

thực sự triển khai mã ở đây.

Và nếu tôi muốn thêm một lớp khác, tôi chỉ cần tiếp tục chuyển những lớp này vào danh sách của mình.

Vì vậy, có lẽ tôi muốn lớp tiếp theo có hai nơ-ron và một chức năng kích hoạt khác của tuyến tính fructify

đơn vị.

Tôi cũng có thể chuyển một số chuỗi như sigmoid cetera và bạn có thể xem tài liệu trực tuyến

cho các lệnh gọi chuỗi khác nhau cho các chức năng kích hoạt khác nhau.

Và hãy tưởng tượng tôi muốn có một lớp đầu ra cuối cùng với một đơn vị.

Tôi chỉ muốn nói đó là một.

Một lần nữa, tôi có thể thử chức năng kích hoạt ở đó, nhưng đây chỉ là một cách chúng tôi có thể xây dựng

ra mô hình.

Vì vậy, theo yêu cầu của bạn về tính tuần tự, bạn thực sự chuyển vào danh sách các lớp đó.

Chúng ta có thể làm điều này theo cách khác và đây sẽ là phương pháp ưa thích của chúng tôi trong suốt khóa học và

trong giây lát bạn sẽ hiểu tại sao nên tạo một mô hình tuần tự trống.

Và sau đó tắt biến mô hình đó, bạn thêm các lớp riêng biệt, từng lớp một.

Vì vậy, bạn sẽ nói kích hoạt đơn vị linnear được chỉnh sửa, sau đó tôi chỉ cần sao chép và dán lệnh này.

Như vậy, và sau đó là đi chơi quanh các thung lũng ở đây, có lẽ tôi muốn cái này, và vì đây là cái cuối cùng của tôi

lớp, tôi thực sự không muốn kích hoạt, v.v.

Vậy tế bào này và tế bào này thực sự sẽ tạo ra cùng một mô hình.

Vậy sự khác biệt giữa chúng là gì về sự tiện lợi?

Chà, có gì thực sự tiện lợi khi thực hiện việc này trong các dòng riêng biệt như thế này thay vì một dòng khổng lồ,

cuộc gọi này là nếu tôi muốn chỉnh sửa nhanh hoặc tắt một lớp, tôi chỉ cần nhận xét nó

như vậy và sau đó chạy lại ô.

Và bây giờ tôi sẽ đi thẳng vào bốn nơ-ron của mình cho đến một năm cuối cùng trên lớp đầu ra.

Việc đó khó thực hiện hơn một chút ở đây.

Khi xử lý một danh sách, chúng ta sẽ phải xóa danh sách này hoặc để nó trên các dòng riêng biệt

và hãy cẩn thận trong cách chúng tôi bình luận mọi thứ.

Vì vậy, đó là lý do tại sao chúng ta sẽ tập trung vào việc sử dụng phương pháp này để xây dựng mô hình của mình.

Chúng ta sẽ tạo một mô hình tuần tự trống và sau đó chúng ta sẽ thêm từng lớp một vào.

Vì vậy, hãy tiếp tục và làm điều đó cho tập dữ liệu cụ thể của chúng ta.

Trong trường hợp này, điều chúng ta sắp làm là chúng ta sẽ có.

Ba lớp với bốn nơ-ron, mỗi lớp sử dụng một đơn vị tuyến tính đã được chỉnh lưu, và sau đó lớp cuối cùng của chúng ta sẽ

chỉ là một nút đầu ra cuối cùng.

Vì vậy, lớp đầu ra cuối cùng thực sự khá quan trọng.

Và điều đó sẽ được xác định bởi dữ liệu thực tế của bạn và tình hình thực tế của bạn về những gì bạn đang cố gắng

để dự đoán.

Hãy nhớ lại rằng với tập dữ liệu cụ thể này, chúng tôi dự đoán một giá trị số duy nhất.

Vì vậy, điều tôi muốn là lớp cuối cùng của tôi là một nơ-ron duy nhất tạo ra một loại giá nào đó.

Vì vậy, nó sẽ dự đoán có thể là bốn trăm năm mươi đô la hoặc sáu trăm đô la, v.v. Đó là lý do tại sao

Tôi đang chọn lớp cuối cùng đó để chỉ có một lớp nơi nó sẽ cố gắng dự đoán giá

do đó sản lượng cuối cùng sẽ được đo lường theo giá thực tế.

Và chúng ta sẽ làm điều đó với một số loại chức năng bị mất.

Và đó là lúc dòng cuối cùng này phát huy tác dụng, đó là biên dịch mô hình của bạn và biên dịch

mô hình.

Chúng ta hãy xem tab shift ở đây.

Nó lại có rất nhiều lệnh gọi tham số khác nhau và chúng ta sẽ khám phá những lệnh gọi này sau trong phần

tất nhiên.

Nhưng những cái chính mà chúng ta muốn xem xét bây giờ là trình tối ưu hóa và hàm mất mát.

Trình tối ưu hóa về cơ bản chỉ là hỏi bạn, bạn thực sự muốn thực hiện gradient này như thế nào

đi xuống?

Bạn có muốn sử dụng Armus prop không?

Hoặc như chúng ta đã thảo luận, có các phương pháp tối ưu hóa khác, chẳng hạn như trình tối ưu hóa nguyên tử.

Vì vậy, tôi cũng có thể nói trình tối ưu hóa bằng và sau đó là String Passan Atom, là mã chuỗi

cho bộ tối ưu hóa nguyên tử.

Và bạn có thể tham khảo tài liệu để xem những trình tối ưu hóa nào có sẵn cho bạn.

Và điều thực sự quan trọng ở đây là tham số tổn hao và tham số tổn hao.

Mã chuỗi đó sẽ thay đổi tùy thuộc vào những gì bạn thực sự đang cố gắng thực hiện ở đây.

Và nếu bạn xem sổ ghi chép Keris Syntax BASIX của chúng tôi, nếu bạn cuộn xuống, chúng tôi thực sự có một

phần nhỏ ở đây về việc chọn một trình tối ưu hóa và mất mát.

Vì vậy, nếu bạn đang thực hiện một bài toán phân loại nhiều lớp, bạn thực sự có thể chọn nhiều trình tối ưu hóa khác nhau.

Nhưng tham số chuỗi mất mát mà bạn nên gọi là entropy chéo phân loại.

Nếu bạn đang thực hiện một bài toán phân loại nhị phân, bạn có thể chọn lại các trình tối ưu hoá khác nhau, nhưng

sự mất mát ở đây sẽ là entropy chéo nhị phân.

Và trong trường hợp của chúng tôi, chúng tôi đang thực hiện một bài toán hồi quy vì nhãn của chúng tôi là một giá trị liên tục.

Vì vậy, trong trường hợp của chúng tôi, chúng tôi sẽ sử dụng sai số bình phương trung bình làm hàm mất mát.

Vậy có nghĩa là nước có ý nghĩa vì về cơ bản chúng ta sẽ lấy bình phương chính của dự đoán của mình chống lại

các giá trị thực và đang cố gắng giảm thiểu giá trị đó thông qua lệnh gọi trình tối ưu hóa của chúng tôi.

Vì vậy, hãy quay lại sổ ghi chép của chúng ta ở đây và sau đó làm theo điều đó.

Chúng tôi sẽ nói trình tối ưu hóa của chúng tôi bằng.

Cánh tay chống đỡ.

Và quan trọng hơn, tổn thất của chúng tôi do chúng tôi đang thực hiện một nhiệm vụ dựa trên hồi quy là M.S., đây là

có nghĩa là lỗi bình phương và khi chúng tôi chạy nó, chúng tôi có sẵn một mô hình đầy đủ.

Và tôi sẽ tiếp tục xóa ô này để chúng ta chỉ thấy mô hình đó đang được tạo.

Vì vậy, chúng tôi có mô hình của chúng tôi tuần tự.

Chúng tôi thêm vào bất kỳ lớp nào chúng tôi muốn với số lượng nơ-ron và chức năng kích hoạt mà chúng tôi muốn.

Chúng tôi cẩn thận để đảm bảo lớp đầu ra cuối cùng của chúng tôi cũng phù hợp với nhiệm vụ thực tế mà chúng tôi đang cố gắng giải quyết

như khi chúng tôi biên dịch nó, hãy đảm bảo lệnh gọi hàm mất mát hoặc tham số mất mát khớp với những gì chúng tôi đang

thực sự đang cố gắng giải quyết.

Sau khi hoàn tất, chúng ta đã sẵn sàng huấn luyện mô hình hoặc điều chỉnh mô hình phù hợp với dữ liệu huấn luyện.

Và chúng ta có thể làm điều này bằng cách nói mô hình phù hợp.

Và một lần nữa, nếu bạn thực hiện tab shift ở đây, bạn sẽ nhận thấy rất nhiều tham số, một số trong đó

chúng ta sẽ đề cập đến trong bài giảng sau.

Nhưng những vấn đề chính mà tôi muốn bạn quan tâm lúc này là X, Y và sau đó là các kỷ nguyên.

Vậy X chỉ đơn giản là những tính năng mà chúng ta đang đào tạo trong trường hợp này là gì, X train?

Và tại sao các nhãn đào tạo thực tế tương ứng với các điểm tính năng đào tạo đó là gì,

trong trường hợp của chúng tôi là tại sao đào tạo?

Và sau đó là các kỷ nguyên, viết tắt của một kỷ nguyên có nghĩa là bạn đã xem qua toàn bộ tập dữ liệu một

hết lần này đến lần khác.

Xin lưu ý nhanh, nếu bạn xem sổ ghi chép A của chúng tôi, về cơ bản chúng tôi cung cấp danh sách tóm tắt về

đợt này và thời đại có ý nghĩa gì.

Vì vậy, kỷ nguyên này về cơ bản là một điểm cắt tùy ý được xác định là một lần chuyển qua toàn bộ tập dữ liệu.

Vì vậy, nếu tôi đã trải qua toàn bộ chuyến tàu X một lần thì đó là một kỷ nguyên.

Vì vậy, tôi sẽ tiếp tục và nói rằng mô hình của tôi sẽ trải qua tập huấn luyện 250

lần, vậy là hai trăm năm mươi kỷ nguyên.

Sau này chúng ta sẽ thảo luận về cách thực sự chọn số đó một cách chính xác và cách chúng ta thực sự có thể sử dụng lệnh gọi lại

các truy vấn cần thêm vào tính năng dừng sớm để chúng ta có thể chọn một số số kỷ nguyên lớn tùy ý.

Và khi đó mô hình của chúng tôi sẽ đủ thông minh để dừng lại ở một thời điểm cụ thể được tối ưu hóa

dựa trên một số mất mát xác nhận.

Vì vậy, hãy nhớ rằng, đây là cách đơn giản nhất mà chúng ta có thể phù hợp, nhưng về sau sẽ trở nên phức tạp hơn

về khả năng của chúng tôi và thực sự phù hợp với mô hình của chúng tôi.

Vì vậy, chúng ta sẽ xử lý những thứ như kích thước lô, lệnh gọi lại, xác thực, dữ liệu, v.v.

Bây giờ chúng ta sẽ làm cho nó rất đơn giản và chúng ta sẽ chỉ khớp cực đại tương ứng với y tàu cho hai người

trăm năm mươi kỷ nguyên.

Điều cuối cùng tôi muốn lưu ý ở đây là có một lệnh gọi dài dòng, do đó, dài dòng tương đương với một lệnh gọi về cơ bản

cho biết đầu ra được in trong quá trình đào tạo.

Vì vậy, nếu tôi chạy ô này, bạn sẽ nhận thấy rằng khi tôi luyện tập liên tục qua các kỷ nguyên này, nó sẽ in ra

những báo cáo nhỏ này

Đối với tôi, số trong lệnh gọi tham số dài dòng càng cao, điều đó có nghĩa là càng nhiều thông tin được hiển thị.

Và nếu bạn đặt chi tiết bằng 0, điều đó có nghĩa là nó sẽ không thực sự xuất ra bất cứ thứ gì.

Tuy nhiên, tôi khuyên bạn nên viết chi tiết bằng một số khác 0, để bạn có thể

biết được bạn đang ở đâu trong giai đoạn đào tạo thực tế của mình.

Nếu không, bạn chỉ thấy một ô đang chạy và bạn sẽ không biết nó ở kỷ thứ mười hay thứ hai trăm

kỷ nguyên.

Bây giờ, đây là một tập dữ liệu rất đơn giản và nhỏ.

Bạn sẽ nhận thấy rằng về cơ bản chúng tôi đã hoàn thành khóa đào tạo của mình.

Và bạn cũng nên lưu ý rằng sai số bình phương trung bình R ban đầu rất lớn vì về cơ bản nó

bắt đầu chỉ với các trọng số và độ lệch ngẫu nhiên.

Nhưng khi nó bắt đầu điều chỉnh những trọng số và thành kiến ​​này.

Vì vậy, chúng ta sẽ cuộn xuống các kỷ nguyên sau này.

Bạn sẽ nhận thấy mức lỗ đang giảm dần và lúc đầu nó sẽ giảm rất nhanh, sau đó sẽ giảm dần.

từ từ khi nó đi xa hơn và xa hơn cho đến khi kết thúc, nó sẽ bắt đầu điều chỉnh theo một số loại

có giá trị bình phương trung bình nên chúng ta có thể tiếp tục và xem điều này bằng cách vẽ đồ thị.

Vậy nên tôi sẽ làm vậy.

Hãy đến phòng giam mới này và chỉ cho bạn cách chúng tôi thực sự có thể xem xét.

Lúc này luyện lịch sử bằng cách nói mẫu lịch sử đó.

Lịch sử đó và lịch sử đó quay trở lại từ điển về những mất mát lịch sử tương ứng, mà

có nghĩa là tôi có thể chuyển cái này vào khung dữ liệu.

Và giả sử mô hình, lịch sử đó, lịch sử đó chạy mà tôi không có được khung dữ liệu đẹp này, vì vậy tôi sẽ đặt

như vậy.

Trạng thái khung hình bị mất của tôi và sau đó tôi thực sự có thể vạch ra điều này bằng cách đơn giản nói mất mát đã nhấn mạnh

Âm mưu F.

Chạy nó và tôi thấy một cái gì đó trông như thế này.

Đây là điều rất điển hình của việc huấn luyện mạng lưới thần kinh.

Bạn bắt đầu với mức thua lỗ rất cao trong vài lần chạy kỷ nguyên đầu tiên.

Và sau đó khi trọng lượng và Bisi bắt đầu được điều chỉnh, bạn hy vọng sẽ thấy một sự ổn định nhưng dốc

từ chối sự mất mát hoặc lỗi lầm của bạn.

Và cuối cùng nó sẽ chững lại khi bạn không thực sự cải thiện được hiệu suất của mình

khi bạn đào tạo ngày càng nhiều và sau này bạn sẽ có thể so sánh điều này với luật xác thực của chúng tôi để thực sự

kiểm tra những thứ như trang bị quá mức.

OK, vậy là chúng ta vừa tìm hiểu cách tạo mô hình cũng như cách điều chỉnh mô hình.

Tiếp theo, chúng ta sẽ đi sâu hơn vào việc đánh giá mô hình này qua thử nghiệm

cũng như cách đánh giá theo điểm dữ liệu hoàn toàn mới.

Cảm ơn.

Và tôi sẽ gặp bạn lúc ba giờ.