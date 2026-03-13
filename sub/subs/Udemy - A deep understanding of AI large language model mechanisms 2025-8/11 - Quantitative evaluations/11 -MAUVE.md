# 11 -MAUVE dịch

---

Trong video này tôi sẽ giới thiệu cho các bạn phương pháp đánh giá dựa trên phân phối có tên là MOV.

Cách đơn giản để nghĩ về MOV là khoảng cách KL giữa một xác suất

phân phối mã thông báo được tạo bởi LLM so với phân phối xác suất của mã thông báo

do con người tạo ra.

Thật không may, chúng tôi cần cân nhắc thêm vì số lượng token quá lớn,

số lượng mã thông báo có thể có là rất lớn và số lượng mã thông báo thực tế

được tạo ra trong một đoạn văn bản nhất định là tương đối nhỏ.

Ví dụ: GPT2 có 50.000 mã thông báo, nhưng thông thường chúng tôi đang nghĩ đến việc tạo mô hình

kích thước của hàng chục hoặc hàng trăm mã thông báo.

Vì vậy, để có được ước tính chất lượng cao về phân bổ xác suất mã thông báo, chúng tôi thực sự muốn

các mẫu lớn, có thể lên tới hàng triệu token.

Và điều đó là không khả thi đối với bất kỳ mô hình cụ thể nào.

Và do đó, ý tưởng của MOV là đưa ra một số sơ đồ lượng tử hóa thông minh cho phép

để sử dụng phân kỳ KL mà không cần lượng dữ liệu cực lớn.

Vì vậy, MOV được phát triển bởi nhóm này và tôi nghĩ bài viết này thực sự là phần tiếp theo của

bài báo gốc đã được xuất bản vài năm trước đó.

Về cơ bản nó vẫn dựa trên sự phân kỳ của KL.

Vì vậy, đây là cách nghĩ về điểm MOV.

Nhưng như tôi đã đề cập, số lượng token có thể có rất cao so với số lượng

dữ liệu mà chúng tôi có trong thực tế để ước tính phân bố xác suất mà ý tưởng là

sau đó rời rạc hóa, phân vùng hoặc lượng tử hóa các phân phối này.

Vì vậy, thay vì có 50.000 token riêng lẻ, có thể có vài chục token được lượng tử hóa

phân vùng.

Việc lượng tử hóa đó được thực hiện dựa trên các đặc điểm thống kê chung của dữ liệu con người và mô hình.

Vì vậy, điều đó giải quyết một vấn đề với cách tiếp cận ngây thơ về phân kỳ KL.

Vấn đề thứ hai là không có giới hạn trên về khoảng cách KL.

Vì vậy thước đo khoảng cách KL có thể lớn tùy ý và điều đó sẽ phụ thuộc vào dữ liệu

đặc điểm và kích thước mẫu và số lượng phân vùng.

Và điều đó có vấn đề vì nó có nghĩa là các mô hình khác nhau với số liệu khác nhau

số mã thông báo và số lượng phân phối xác suất chung được lượng tử hóa khác nhau có thể mang lại

kết quả khác nhau, thậm chí ngoài khả năng của chính mô hình.

Nói cách khác, bạn có thể nhận thấy sự khác biệt rõ ràng giữa các mô hình về phân kỳ KL, đơn giản vì

của quá trình mã thông báo và lượng tử hóa, không phải do khả năng của mô hình.

Vì vậy, điều đó dẫn đến thủ thuật thông minh thứ hai trong MOV, đó là sử dụng một thứ gọi là biên giới

phân tích.

Về cơ bản, đây là một cách để giới hạn khoảng cách KL trong khoảng từ 0 đến 1.

Ở đây ý tưởng là kết hợp các phân bố xác suất của con người và văn bản mô hình với các mức độ khác nhau.

số tiền.

Vậy đó là cho R lambda ở đây.

Vì vậy, đối với bất kỳ giá trị đã cho nào của lambda, bạn có thể thêm phân bố xác suất theo tỷ lệ của

dữ liệu mô hình và dữ liệu con người.

Vì vậy, hãy lấy P là dữ liệu mô hình và Q là dữ liệu con người.

Bây giờ với lambda là 0 thì R là 100% dữ liệu con người và 0% dữ liệu mô hình.

Và khi lambda bằng 1 thì R là 100% dữ liệu mô hình và 0% dữ liệu con người.

Và khi lambda là 0,5 thì có mức trung bình chính xác của hai nguồn dữ liệu.

Vì vậy, bây giờ ý tưởng là thay đổi lambda trong khoảng từ 0 đến 1 và điều đó sẽ tạo ra đường cong này

dòng trong không gian này ở đây.

Đây được gọi là đường cong phân kỳ.

Và sau đó bạn tính diện tích dưới đường cong đó, tất cả những thứ màu xanh này được biểu thị

ở đây.

Vùng đó được giới hạn bởi 0 và 1 và đó là điểm MOV.

Đừng lo lắng về chiếc hộp màu cam này.

Đó là một thước đo khác mà họ thảo luận trong bài báo của mình, nhưng đó không phải là thước đo chính

điểm số mà chúng tôi sẽ làm việc cùng.

Vì vậy, tôi hy vọng lời giải thích này có ý nghĩa.

Đó là một trình độ hơi cao và có rất nhiều chi tiết toán học có trong

bài viết mở rộng những ý tưởng này và chứng minh rằng chúng phù hợp.

Để giành điểm về nhà, kết quả cuối cùng là điểm MOV thay đổi từ 0 đến 1 và điểm

càng gần 0 cho biết đầu ra của mô hình trông không giống dữ liệu của con người và điểm số

gần hơn 1 cho thấy rằng dữ liệu mô hình sẽ không thể phân biệt được với dữ liệu của con người vì

phân phối xác suất của các mã thông báo là như nhau.

Ồ, còn một điều nữa tôi muốn đề cập.

Bạn đã thấy trong video trước rằng việc bạn chọn P hay Q làm dữ liệu mô hình đều quan trọng

bởi vì điều đó ảnh hưởng đến điểm phân kỳ KL.

Trong MOV, điều đó thực sự không quan trọng vì tính đối xứng của hai xác suất này

phân phối được trộn lẫn.

Diện tích dưới đường cong này, dưới đường cong phân kỳ là như nhau bất kể

bạn lấy P hoặc Q làm mô hình hoặc dữ liệu về con người.

Ít nhất chúng giống nhau trong mức độ chịu đựng hợp lý.

Điểm này có thể rất khác một chút so với lượng tử hóa, v.v.

Được rồi, bây giờ hãy để tôi kể cho bạn nghe về bản demo Python.

Chúng ta sẽ lấy một loạt dữ liệu về con người từ tập dữ liệu WikiText và cùng một lượng dữ liệu

dữ liệu được tạo bởi GPT2.

Trong trường hợp này, tôi đang tạo dữ liệu mà không có bất kỳ lời nhắc cụ thể nào.

Tôi chỉ cần nhập một mã thông báo và để mô hình tạo ra bất cứ thứ gì nó muốn.

Nhưng nó có cùng lượng dữ liệu với dữ liệu của con người.

Và sau đó tôi sẽ chạy phân tích MOV dựa trên thư viện của họ và cho bạn xem biểu đồ

của những sự phân bổ mà bạn thấy ở đây.

Đây là những biểu đồ lượng tử hóa.

Và đường cong phân kỳ được áp dụng ở đây và diện tích bên dưới đường cong đó, trong trường hợp này, nó

cuối cùng là 0,65.

Nhưng vì đây là văn bản mẫu được tạo ngẫu nhiên nên nó sẽ thay đổi đôi chút khi tôi thực sự

chạy mã.

Dưới đây là một số thư viện chúng tôi sẽ sử dụng.

Tôi thực sự chưa nhập MOV.

Tôi sẽ đề cập đến điều đó sau một chút trong đoạn mã.

Chúng tôi chắc chắn muốn sử dụng GPU ở đây vì chúng tôi sẽ tạo ra nhiều văn bản,

nó sẽ chiếm mãi CPU.

Vì vậy, bạn chắc chắn muốn chạy cái này trên GPU.

Được rồi, ở đây tôi đang nhập GPT2 lớn, đẩy nó vào GPU và cũng chuyển sang chế độ eval.

Và tất nhiên, chúng ta cũng cần tokenizer.

Được rồi, tôi đang nhập tập dữ liệu WikiText.

Bạn đã nhìn thấy điều này nhiều lần trước đây.

Và về cơ bản những gì tôi đang làm ở đây chỉ là thu thập nhiều luồng dữ liệu văn bản

Dài 200 token.

Giờ đây, cách MOV hoạt động trong thực tế và triển khai là bạn không chỉ nhập

một vectơ mã thông báo hoặc một chuỗi văn bản.

Thay vào đó, thư viện MOV mong đợi một danh sách, do đó, một danh sách Python có nhiều phần tử và mỗi phần tử

là một đoạn văn bản.

Tôi sẽ cho bạn thấy nó trông như thế nào ở đây.

Vì vậy, chúng tôi có, thực sự cho tôi xem.

Vì vậy hãy gõ dữ liệu của con người.

Vì vậy, đây là một danh sách Python và chúng ta có thể xem xét, ví dụ, chỉ phần tử đầu tiên trong danh sách này

hoặc thành phần thứ tư trong danh sách này, bạn có thể thấy nó chỉ là một chuỗi văn bản.

Vì vậy, những gì tôi làm ở đây là khởi tạo biến này thành một danh sách trống và sau đó tôi bị mắc kẹt bên trong

vòng lặp while này cho đến khi độ dài của danh sách này dài tới 100 phần tử.

Vì vậy, tôi sẽ xem qua từng mẫu văn bản của tập dữ liệu này, mã hóa nó và sau đó,

nó mang lại cho tôi những mã thông báo này và sau đó tôi đếm số lượng mã thông báo.

Tôi muốn có ít nhất 200 token.

Đó là vì một số mẫu văn bản này có rất ít mã thông báo.

Đôi khi chúng trống rỗng.

Vì vậy, tôi muốn có 200 token cho mỗi thành phần trong danh sách này.

Vì vậy, tôi có phần bổ sung và tokenizer.deco.

Vì vậy, tôi đang mã hóa văn bản ở đây và sau đó tôi sẽ hủy mã hóa văn bản ở dưới đây.

Lý do tôi làm vậy là vì tôi muốn có chính xác 200 token vì

đó là những gì tôi sắp có với dữ liệu mô hình.

Mod phân tích này nhạy cảm với kích thước mẫu.

Vì vậy, cỡ mẫu không cần phải khớp chính xác một cách hoàn hảo giữa bao nhiêu

dữ liệu con người và số lượng dữ liệu mô hình bạn có.

Nhưng tốt nhất là để hai nguồn dữ liệu càng gần nhau càng tốt trong

điều kiện về cỡ mẫu.

Được rồi, vâng.

Vì vậy, sau đó chúng ta thấy rằng đây là một danh sách.

Nó có 100 phần tử và vâng, đây là một trong những phần tử đó.

Bây giờ nếu chúng ta nhìn vào đây, độ dài của cái này là, ví dụ, 900.

Chiều dài của một cái khác là 1000.

Vì vậy số lượng ký tự khác nhau.

Nhưng khi chúng tôi mã hóa lại những văn bản này, nó sẽ luôn là 200 mã thông báo.

Đó là lý do tôi làm việc này ở đây.

Được rồi, đó là dành cho dữ liệu của con người.

Bây giờ để tạo dữ liệu từ mô hình, điều tôi đang làm ở đây là tạo dữ liệu mô hình cho một

mã thông báo cụ thể mà tôi đang bắt đầu.

Đây là ID mã thông báo của ông chủ.

Đây là phần đầu của ID mã thông báo chuỗi.

Trong mã thông báo này, nó thực sự giống với phần cuối của chuỗi.

Vậy là đã kết thúc trình tự.

Đó là mã thông báo cuối cùng mà họ có.

Và sự bắt đầu của trình tự này cũng giống như vậy.

Đó chỉ là cách triển khai mã thông báo.

Vì vậy, 100 lần lặp khác nhau của 200 mã thông báo.

Tôi thực sự muốn lấy mẫu và ở đây tôi đang thêm những thứ này chỉ để nhận được những mã thông báo có khả năng nhất.

Vì vậy, mô hình này thận trọng hơn một chút trong cách chọn mã thông báo.

Vì vậy, kết quả cuối cùng của mã này là chúng ta sẽ nhận được 100 mẫu, mỗi mẫu có 200 mã thông báo.

Và kích thước đó sẽ tương đương với dữ liệu của con người, mỗi dữ liệu cũng có kích thước 100 x 200.

Về lý thuyết, bạn thực sự có thể tăng tốc độ tính toán một chút bằng cách thực hiện điều này

một lô thay vì chỉ một lô có kích thước một và lặp qua 100.

Và thay vì biến nó thành các lô lớn hơn và chạy qua ít vòng lặp for hơn, tôi sẽ

thảo luận chi tiết hơn về thử thách viết mã ở video tiếp theo.

Nhưng nói ngắn gọn là nếu bạn cố gắng tạo một lô 100 x 200 mã thông báo thì đó là

chỉ bắt đầu lớn dần và bạn sẽ có nguy cơ gặp sự cố về bộ nhớ, làm hỏng hệ thống của bạn.

Phiên Python.

Vì vậy, trong trường hợp này, tôi sẽ giữ nó đơn giản và dễ hiểu và chỉ tạo một

trình tự văn bản tại một thời điểm.

Quá trình đó mất khoảng tám phút và ở đây chúng ta có thể xem dữ liệu mô hình.

Lưu ý rằng dữ liệu mô hình tôi cũng đã chuyển đổi thành văn bản.

Vì vậy, đây không phải là mã thông báo trong chỉ số mã thông báo.

Thay vào đó, đây là tất cả văn bản xuất phát từ mô hình mà tôi đã giải mã ở đây.

Vì vậy, dữ liệu của con người là văn bản và dữ liệu mô hình là văn bản.

Trong video tiếp theo trong thử thách viết mã, tôi cũng sẽ chỉ cho bạn cách sử dụng MoV bằng cách nhập

mã thông báo thay vì văn bản.

Nhưng ở đây, chúng ta đang làm việc với văn bản.

Được rồi, ở đây chúng ta có thư viện MoV.

Nó không được đóng gói trong colab nên chúng tôi phải cài đặt nó và sau đó chúng tôi có thể nhập

nó.

Bây giờ đối với thư viện này, bạn không cần phải khởi động lại phiên của mình.

Bạn không cần phải làm điều đó.

Bạn có thể nếu bạn thực sự muốn, nhưng chắc chắn bạn không muốn làm điều đó bây giờ bởi vì chúng tôi chỉ

đợi tám phút để tất cả những thứ này được xử lý.

Được rồi, vậy là đã nhập thư viện MoV.

Như tôi đã đề cập nhiều lần trước đây, bất cứ khi nào bạn nhập một lớp mới, một thư viện mới,

một loại cấu trúc dữ liệu mới trong Python mà bạn chưa quen, nó luôn là một giải pháp tốt

ý tưởng chỉ là gõ DUR và sau đó là tên của thư viện hoặc lớp hoặc bất cứ thứ gì, chỉ để

có được cảm giác về những loại thuộc tính mà nó gắn liền với nó.

Vì vậy, trong trường hợp này, thực sự chỉ có một thứ chúng ta sẽ sử dụng, đó là tính toán MoV.

Vì vậy, đó là những gì bạn thấy ở đây.

Vì vậy, MoV.computemov và sau đó chúng tôi cung cấp một số thông tin đầu vào.

Chúng ta có P và Q và dài dòng, có lẽ tôi sẽ biến điều đó thành sự thật.

Và sau đó là ID thiết bị, điều này có nghĩa là sử dụng GPU.

Vì vậy, bây giờ chức năng MoV sẽ cố gắng sử dụng GPU nếu có sẵn và một GPU có sẵn

ở đây.

Vậy là tốt rồi.

Chúng ta có thể chạy cái này trên GPU.

Và bây giờ như tôi đã đề cập trong các slide, việc nào trong số này thực sự không quan trọng,

mô hình hoặc dữ liệu con người mà bạn gán cho P hoặc Q, đó là điều gì đó đặc biệt về

phân tích phân kỳ biên giới, đường cong phân kỳ mà chúng ta sắp tạo ra nói chung,

nếu bạn đang thực hiện một số loại phân tích khác với phân kỳ KL, điều quan trọng là phải suy nghĩ

cẩn thận về cái nào trong hai cái này bạn đang sử dụng để tham khảo và cái nào bạn đang sử dụng

cho đầu vào.

Bây giờ mặc dù có sự đối xứng giữa P và Q và MoV, tôi vẫn thích sử dụng P để coi P là

làm người mẫu và Q làm người chỉ vì điều đó giúp tôi sắp xếp suy nghĩ của mình.

Được rồi, hãy lưu ý rằng tôi đang viết văn bản P.

Nếu bạn có mã thông báo mà bạn muốn nhập thay vì văn bản thì điều đó thực sự đơn giản.

Bạn chỉ cần viết mã thông báo P.

Tôi quên đó là token hay token nhưng chúng ta sẽ tìm hiểu điều đó trong video tiếp theo.

Vì vậy, điều đó rất đơn giản.

Được rồi, nhưng ở đây chúng ta có văn bản nên chúng ta đang nhập văn bản.

Inverboast chỉ có nghĩa là nó sẽ cung cấp thêm một số đầu ra.

Vì vậy, chúng ta có thể chạy cái này.

Nó không mất quá nhiều thời gian.

Trước tiên, nó phải nhập lại mã thông báo GPT khác.

Và sau đó nó sẽ mô tả P và Q. Về cơ bản, đây là quá trình lượng tử hóa

của hai vectơ mà chúng ta quan tâm.

Vì vậy, nó cung cấp cho bạn một số thông tin.

Có một phân tích phân cụm là bước cuối cùng trong quá trình lượng tử hóa

phân tích.

Được rồi, và hãy xem.

Vì vậy, chúng tôi nhận được số điểm là 0,81.

Như vậy là cao hơn một chút.

Ồ vâng, ở đây tôi chỉ muốn cho bạn thấy đối tượng đầu ra này trông như thế nào, nó như thế nào

những đặc tính mà nó có.

Vì vậy, nó có một đường cong phân kỳ, tích phân biên.

Xem nào, chúng ta không cần phải lo lắng về điều đó.

Vì vậy, chúng ta sẽ xem xét điểm MOV, biểu đồ và đường cong phân kỳ.

Đó là những phần của đối tượng lớp này mà chúng ta sẽ xem xét.

Vì vậy, hãy xem ở đây tôi đang vẽ các biểu đồ thanh ở đây, biểu thị sự phân bố lượng tử hóa.

Và ở đây là đường cong phân kỳ.

Hãy nhớ rằng đây là đường cong liên quan đến việc lấy phân bố xác suất, lượng tử hóa

phân phối dữ liệu của con người, lượng tử hóa phân phối dữ liệu mô hình và sau đó trộn

chúng cùng nhau.

Và điều đó mang lại cho bạn đường cong này.

Bây giờ có thêm một chút chi tiết về ý nghĩa thực sự của những trục này.

Nhưng bạn có thể đọc về điều đó trên báo nếu bạn tò mò.

Và sau đó chúng ta muốn diện tích dưới đường cong này.

Và trong trường hợp đó, đó là 0,81.

Và điều đó chỉ ra rằng có một mối quan hệ khá tốt giữa việc phân phối

văn bản do mô hình tạo ra và văn bản do con người tạo ra từ tập dữ liệu văn bản wiki.

Vì vậy, đó là ý tưởng tính điểm MOV.

Đó là một biện pháp tốt đẹp.

Và tôi thích nó phản ánh các đặc điểm phân phối chứ không phải đặc điểm cấp độ mã thông báo.

Vì thế nó có trình độ cao hơn một chút.

Nhắc nhở ngày đầu tiên rằng tôi chỉ sử dụng 100 mẫu tương đối ngắn.

Trong khi các tác giả của bài viết này, những người phát triển phương pháp này khuyên bạn nên sử dụng hàng nghìn hoặc

thậm chí bút của hàng ngàn mẫu dài hơn để có được một thống kê ổn định hơn và

ước tính đáng tin cậy.

Có một số lưu ý và sắc thái quan trọng khác cần hiểu về điểm MOV này, làm thế nào

nó hoạt động và cách diễn giải nó cũng như ý nghĩa của nó.

Và tôi sẽ thảo luận chi tiết hơn trong video tiếp theo.