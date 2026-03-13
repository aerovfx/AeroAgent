# 7 -CodeChallenge Định lượng tinh chỉnh AliceEdgar

---

Thử thách viết mã này sẽ bắt đầu từ phần chúng ta đã dừng lại trong video trước.

Đặc biệt, các bạn sẽ tiếp tục tinh chỉnh hai mô hình để áp dụng phong cách Alice ở xứ sở thần tiên.

hoặc Edgar Allan Poe.

Và ở đây bạn cũng sẽ thực hiện cả đánh giá định lượng và định tính

về hiệu quả hoạt động của các mô hình này.

Phần đầu tiên của bài tập một là nhập và mã hóa cả hai văn bản mà chúng tôi đã sử dụng

trong video trước.

Bây giờ phần đó rất đơn giản.

Bạn chỉ có thể sao chép và dán nó từ sổ ghi chép trước đó.

Phần tiếp theo của bài tập này là tìm 100 token xuất hiện phổ biến nhất trong

từng văn bản.

Bây giờ bạn đã từng làm điều gì đó tương tự như vậy trước đây với Gulliver's Travels, nhưng

ở đây điều này hơi khác một chút vì ở đây tôi muốn bạn bỏ qua bất kỳ mã thông báo nào

có một hoặc hai ký tự.

Vì vậy, bạn muốn tìm 100 mã thông báo thường xuyên nhất có ít nhất ba ký tự

dài.

Và tất nhiên việc đó được thực hiện riêng biệt cho văn bản Alice và văn bản Edgar.

Bây giờ, lý do tại sao tôi yêu cầu bạn làm điều này

đó là khi kết thúc thử thách viết mã này,

bạn sẽ có hai mô hình được tinh chỉnh để tạo văn bản

và sau đó đếm tỷ lệ văn bản được tạo ra

có trong mỗi danh sách này

để xác định liệu các mô hình

thực sự bắt đầu thích sử dụng token

từ văn bản mà họ đã được đào tạo

trái ngược với văn bản mà họ không được đào tạo.

Vì vậy, tôi thấy rằng gần một nửa số token trong mỗi cuốn sách này có ít hơn ba

mã thông báo.

Bây giờ, điều đó ban đầu có vẻ đáng ngạc nhiên, nhưng nó bao gồm dấu chấm câu và dòng mới

nhân vật.

Vì vậy, đây là ảnh chụp màn hình của một số trong 100 từ thường gặp nhất của Edgar Allan Poe

văn bản.

bạn có thể thấy rằng rất nhiều từ này

vẫn chưa thực sự cụ thể để đặt ra thơ.

Đó chỉ là những từ rất thông dụng.

Vì vậy sẽ rất thú vị để xem điều gì sẽ xảy ra

với việc định lượng này.

Và trên thực tế, khi kết thúc thử thách viết mã này,

Tôi muốn có một vài điểm thảo luận

về những thách thức của việc định lượng hiệu suất

của các mô hình sáng tạo.

Vì vậy, bạn đã có thể bắt đầu suy nghĩ về những lời phê bình có thể có

của phương pháp này và bất kỳ cải tiến nào bạn có thể nghĩ ra.

Nhưng dù sao thì hãy tạm dừng video ngay nhé

và thực hiện bài tập này.

Và bây giờ tôi sẽ thảo luận về giải pháp của tôi.

Vì vậy, đây là một số thư viện mà chúng tôi sẽ sử dụng.

Và ở đây tôi đang mã hóa và tìm kiếm các mã thông báo phổ biến nhất.

Được rồi, mã này ở đây giống hệt nhau,

nghĩa đen chỉ là sao chép dán từ video trước đó.

và cả mã này nữa.

Được rồi, đây là nơi chúng ta bắt đầu tìm hiểu những nội dung mới.

Được rồi, điều tôi đã làm ở đây là tạo một vectơ mã thông báo mới

mà tôi gọi là thẻ Alice, Filt.

Bộ lọc dành cho bộ lọc.

Và bạn có thể thấy rằng tôi đang định nghĩa cái này có cùng độ dài

giống như mã thông báo Alice, nhưng chứa đầy dấu trừ.

Vậy vectơ này ở đây chỉ toàn là số âm,

nhưng chính xác là cùng số lượng token

như những gì xuất hiện trong cuốn sách Alice.

Được rồi, sau đó việc tôi làm là lặp lại

tất cả các thẻ Alice,

và tôi nói với mỗi token này,

sau đó tôi giải mã chúng,

và nếu độ dài của chỉ mục mã thông báo được giải mã đó

lớn hơn hai,

sau đó tôi thay thế số trừ bằng giá trị mã thông báo thực tế.

giá trị. Được rồi, tôi hy vọng điều đó có ý nghĩa. Về cơ bản, nếu chỉ mục mã thông báo có thể được giải mã thành mã thông báo

chuỗi có ba ký tự trở lên thì chỉ mục mã thông báo đó được giữ nguyên trong chuỗi được lọc này

vectơ. Ngược lại, nó vẫn là âm một. Được rồi, sau đó tôi lặp lại điều đó cho văn bản của Edgar.

Vậy thì, được rồi, đây là nơi tôi tạo ra ảnh chụp màn hình mà tôi đã trình chiếu trước đó.

Vì vậy, ở đây tôi chỉ đếm tổng số mã thông báo đã lọc bằng âm một và chia số đó cho tổng số mã thông báo.

Vì vậy, điều đó cho tôi biết rằng gần một nửa số mã thông báo trong cuốn sách của cả hai cuốn sách này là một hoặc hai ký tự.

nhân vật. Được rồi, từ đây việc định lượng top 100 thực sự rất đơn giản

token thường xuyên nhất. Tất cả những gì chúng ta cần làm là bỏ qua dấu trừ một và cách tôi làm điều đó

là bằng cách sử dụng cùng một mã mà tôi đã sử dụng trước đó, nhưng nó nằm trên vectơ đã được lọc. Và ở đây, bạn biết đấy,

trước khi tôi làm điều này, tôi đã có từ đầu đến 100.

Nhưng mã thông báo phổ biến nhất xuất hiện ở khoảng 50%

trong số các mã thông báo trong vectơ này có giá trị trừ một.

Vì vậy, trừ một sẽ là mã thông báo phổ biến nhất cho đến nay.

Vì vậy, tất cả những gì tôi đang làm là bỏ qua mã thông báo đó.

Đó sẽ là chỉ số 0.

Vì vậy tôi chỉ đi chuyến đầu tiên tới phòng 101

chỉ số mã thông báo, chỉ mục mã thông báo tần số.

Được rồi, vậy đi thôi.

Bạn thấy đó cũng là hai đầu của nó.

Cô ấy nói với bạn rằng Alice đang ở đây.

Và hãy xem, sau đó chúng ta đến với Edgar Allen Poe.

Và đây cũng thực sự không phải là những token độc đáo.

Đây là những token rất phổ biến mà bạn thường xuyên tìm thấy

về cơ bản là bất kỳ ngôn ngữ văn bản nào.

Đối với bài tập thứ hai, bạn sẽ viết mã

điều đó sẽ định lượng tỷ lệ mã thông báo tần số cao

cho hai mô hình và hai văn bản.

Mã này tương tự như mã bạn đã viết trước đây,

vì vậy bạn chắc chắn có thể bắt đầu bằng cách tìm mã đó

và sao chép và dán nó vào tập tin sổ ghi chép này,

nhưng ở đây đối với bài tập hai thì hơi khác một chút.

Vì vậy hãy đảm bảo bạn xem qua mã một cách cẩn thận

sau khi bạn dán nó vào.

Bây giờ đến bài tập thứ hai,

bạn không thực sự tạo ra bất kỳ hình dung nào.

Đây là một biểu đồ thanh mà bạn sẽ tạo

trong bài tập bốn trong tương lai.

Nhưng bây giờ tôi đang cho bạn xem nó.

Vậy là bạn đã có ý tưởng về cách sắp xếp dữ liệu

vậy bạn biết bạn sẽ làm gì

với những dữ liệu này trong tương lai.

Vì vậy, bạn có thể thấy rằng những gì chúng ta có ở đây là một biểu đồ dạng vạch

nơi chúng tôi có hai nhóm theo mô hình.

Vậy mô hình Alice và mô hình Edgar.

Và sau đó chúng ta có hai bộ mã thông báo thường xuyên nhất.

Vì vậy tôi gọi chúng là token Alice và token Edgar.

Và sau đó chúng tôi định lượng tỷ lệ mã thông báo được tạo

từ mỗi mô hình và từ mỗi văn bản,

cả trước khi tinh chỉnh và sau khi tinh chỉnh.

Vì vậy, điều đó có nghĩa là tập dữ liệu này là hai nhân hai.

Vì vậy bạn phải suy nghĩ cẩn thận về cách bạn muốn

tổ chức và tạo ra các biến này

để giảm thiểu nguy cơ nhầm lẫn.

Được rồi, một khi bạn có ý tưởng đó,

thì bạn thực sự muốn chạy quá trình tạo mã

và tính toán những dữ liệu này trước khi đào tạo.

Vì vậy, bạn thực sự có thể vẽ biểu đồ thanh này.

Bây giờ, mặc dù bạn không cần phải làm điều đó bây giờ,

bạn có thể thực hiện việc hình dung sau,

nhưng bạn chắc chắn muốn định lượng dữ liệu

mà tôi đang trình bày ở đây trước khi bạn thực hiện việc tinh chỉnh

bởi vì đó sẽ là đường cơ sở của chúng tôi.

Vậy đó là bài tập thứ hai.

Vui lòng tạm dừng video ngay bây giờ và thực hiện bài tập này.

Và bây giờ tôi sẽ chuyển sang mã.

Như vậy trong ô mã này các bạn sẽ nhận ra rất nhiều mã

mà bạn đã thấy trước đây trong chuyến du hành của Gulliver.

Vậy 10 lần lặp lại của 100 thẻ,

và sau đó tôi tạo ra 100, tạo ra những mã thông báo đó

bắt đầu từ một chỉ số hoàn toàn ngẫu nhiên.

Vì vậy, một số đại diện, từng đợt một,

vì vậy các token đơn lẻ hoàn toàn ngẫu nhiên

mà chúng tôi đang cung cấp cho mô hình để tạo ra một số văn bản từ đó.

Vì vậy, đây là kết quả của mô hình Alice,

và đây là kết quả của mô hình Edgar.

Trong trường hợp này, chúng tôi không thực sự quan tâm

về những gì văn bản nói,

chúng tôi chỉ quan tâm đến việc đếm số lượng token

nằm trong top 100 token thường xuyên nhất

trong cuốn sách Alice và trong cuốn sách Edgar.

Vì vậy, tôi chỉ định hình lại cái này thành một vectơ.

Nó chỉ làm cho nó dễ dàng hơn một chút

để kiểm tra việc sử dụng.

Và bạn cũng có thể thấy ở đây,

Tôi không lấy toàn bộ đầu ra, không phải tất cả các mã thông báo.

Tôi đang bỏ qua cái đầu tiên.

Và đó là vì token đầu tiên

là mã thông báo ngẫu nhiên mà tôi nhập vào.

Điều đó không được kiểm soát bởi mô hình.

Được rồi, và ở đây có cùng mã với mã này.

Nó chỉ dành cho mô hình Edgar và tôi đã nén nó.

Tôi không nhớ tại sao tôi lại làm vậy, nhưng tôi đã làm vậy.

Được rồi, rồi, được rồi, bây giờ hãy để tôi cuộn lên

và giải thích điều này ở đây.

Bây giờ ban đầu tôi nghĩ đến việc lưu trữ tất cả các kết quả này

trong tensor 2 x 2 x 2, nên một khối dữ liệu.

Nhưng bởi vì nó có hai chiều xung quanh,

Tôi nhận ra rằng tôi đang bối rối

về kích thước nào tương ứng với mô hình

so với văn bản và trước và sau.

Vì thế tôi quyết định chia tay

thành hai biến riêng biệt.

Đó là những gì bạn thấy ở đây.

Biến này tương ứng với văn bản Alice

và biến này tương ứng với văn bản Edgar.

Và sau đó hai nhân hai tương ứng

tinh chỉnh trước và sau

và mô hình Alice và Edgar.

Vì vậy bây giờ nếu chúng ta cuộn xuống đây để đến nơi tôi tính toán dữ liệu,

bạn có thể thấy, hãy để tôi di chuyển qua hướng này.

Được rồi, hầu hết mã này nằm trong bốn dòng này

giống hệt nhau, chỉ khác tên biến.

Đây là mô hình Alice,

các mã thông báo được tạo bởi mô hình Alice,

và tần suất các mã thông báo do mô hình Alice tạo ra đó xuất hiện như thế nào

xuất hiện trong top 100 từ cuốn sách Alice.

Và đây là mô hình Edgar,

và tần suất nó tạo ra mã thông báo thường xuyên của Alice như thế nào?

Được rồi, và ở đây, điều này cũng tương tự.

Vì vậy, điều này ngoại trừ nó dành cho mã thông báo Edgar.

Đây là mô hình Alice tạo ra mã thông báo Edgar,

và mô hình Edgar tạo ra mã thông báo Edgar,

và những tỷ lệ đó

Được rồi, thậm chí còn khó hiểu khi chỉ nói về điều này.

Vì vậy chúng ta có thể xem xét điều này,

nhưng đây không phải là thông tin hữu ích.

Hầu hết những gì chúng tôi muốn làm là lấy điều này làm cơ sở.

Tuy nhiên, chúng tôi kỳ vọng hai con số này

có thể so sánh một cách đại khái.

Trên thực tế, chúng tôi mong đợi chúng giống hệt nhau

và bất kỳ sự khác biệt nào giữa chúng chỉ là do

đến việc lấy mẫu ngẫu nhiên mà bạn nhận được

từ các mô hình tổng quát thực hiện xử lý ngẫu nhiên này.

Vì vậy, vâng, khoảng 25% số token

mà các mô hình này tạo ra đều có trong một trong những cuốn sách này.

Bây giờ là bài tập thứ ba.

Ở đây bạn muốn tinh chỉnh hai mô hình.

Bạn có thể sao chép mã từ video trước,

nhưng một lần nữa, hãy cẩn thận kiểm tra từng dòng

bạn đang dán vào, hãy đảm bảo điều đó phù hợp với mục tiêu của thử thách mã này. Đây là

một số tham số để sử dụng cho việc huấn luyện và sau khi huấn luyện, bạn có thể tạo các biểu đồ đường hiển thị

tổn thất cho cả hai mô hình. Về tổng thể, nó sẽ trông giống với hồ sơ tổn thất từ phiên bản trước.

video. Được rồi, bây giờ bạn có thể tạm dừng video và viết mã, còn bây giờ tôi sẽ chuyển sang viết mã.

Vì vậy, đây là hai trình tối ưu hóa.

Một lần nữa, tôi đang lặp đi lặp lại,

nhưng bạn thực sự không cần phải tạo

một hàm mất riêng biệt nếu bạn đang sử dụng

những mẫu máy biến áp được đào tạo trước khuôn mặt ôm này.

Được rồi, và đây, ừ, để tôi xem.

Tất cả những thứ này về cơ bản là giống nhau.

Tôi không nghĩ bạn thực sự cần nó để thay đổi nhiều như vậy.

Tôi nghĩ khi tôi nói bạn thực sự cần

để kiểm tra mã của bạn một cách cẩn thận,

đó là về việc khuyến khích bạn

xem kỹ mã

thay vì chỉ sao chép một cách mù quáng và dán nó.

Tôi không nghĩ tôi thực sự đã thay đổi bất cứ điều gì

so với video trước.

Được rồi, việc đó mất khoảng bảy phút.

Nhìn chung, không quá tệ.

Và chúng ta hãy nhìn vào những mất mát.

Tương tự như video trước,

chúng ta thấy rằng tổn thất của Alice rất lớn.

Chúng đi xuống đến mức không chính xác bằng 0,

nhưng chúng tiến gần đến con số 0.

và chắc chắn tổn thất của Edgar giảm dần theo thời gian,

nhưng không quá xa như mã thông báo Alice.

Và ngoài ra, như chúng ta đã thấy trong video trước,

điều đó không nhất thiết có ý nghĩa như vậy.

Ý tôi là, điều này cho chúng ta biết điều gì đó về hai mô hình này

và các văn bản, tập dữ liệu, v.v.,

nhưng điều này không nhất thiết có nghĩa là

rằng mô hình này không học theo phong cách của Edgar Allan Poe.

Nó chỉ có nghĩa là tổn thất là khác nhau

và có một số lý do

vì sao điều đó có thể xảy ra.

Và điều đó đưa chúng ta đến bài tập thứ tư.

Vậy là bây giờ chúng ta đã hoàn thành tất cả phần đào tạo

và vì vậy điều bạn muốn làm là hoàn thành việc đánh giá

mà bạn đã bắt đầu ở bài tập hai

và cách bạn thực sự có thể tạo và hiển thị biểu đồ thanh này

hình mà tôi đã trình bày trước đó trong bài tập hai.

Bây giờ kết quả có thể hơi khó diễn giải.

Vì vậy, nếu bạn đã tạo cốt truyện,

nhưng bạn không chắc chắn nên làm gì với nó,

thì đừng lo lắng, tôi sẽ thảo luận về vấn đề đó

khi tôi sử dụng Python.

Bây giờ là phần đánh giá định lượng.

Tiếp theo, bạn muốn thực hiện một đánh giá định tính.

Vì vậy, ý tưởng ở đây là tạo ra

khoảng 100 token từ cả hai mô hình

sau khi đưa ra lời nhắc giống nhau cho cả hai mô hình.

Vì vậy tôi đã sử dụng lời nhắc này,

nữ hoàng đỏ đã nói gì với Alice?

Bạn có thể sử dụng lời nhắc khác nếu muốn,

nhưng thật thú vị khi đưa ra lời nhắc tương tự

cả hai mô hình để xem chúng khác nhau như thế nào.

Và tôi cũng muốn bạn thêm vào việc lấy mẫu ngẫu nhiên

trong thế hệ để bạn có thể chạy mã

nhiều lần và cố gắng cảm nhận một chút

về cách các mô hình tạo ra văn bản.

Bây giờ, một phần khác của bài tập 4 là suy nghĩ về hai hình thức đánh giá này.

Chúng tôi có đánh giá định lượng và đánh giá định tính.

Vậy bạn nghĩ thế nào là tốt?

Bạn nghĩ điều gì là không tốt?

Làm thế nào bạn có thể phát triển các đánh giá định lượng hoặc định tính tốt hơn cho một dự án như

cái này à?

Không có câu trả lời đúng hay sai cho điều này.

Tôi sẽ nói nhiều hơn về việc đánh giá LLM

trong suốt phần này và cả trong phần dành riêng

một chút sau đó trong khóa học.

Nhưng cũng đủ để nói rằng thật khó để đánh giá

những loại mô hình sáng tạo này.

Mã này ở đây được sao chép theo đúng nghĩa đen

từ mã từ trước khi đào tạo.

Sự khác biệt chính là tôi không đặt lại các biến ở đây

bởi vì tôi đã định nghĩa chúng rồi

và tập trung một phần chúng ở trên.

Được rồi, vậy hãy chạy mã này.

Việc tạo ra mất vài giây, hai giây.

Vì vậy, nhìn chung không quá tệ.

Được rồi, và ở đây chúng ta có thể nhìn vào sơ đồ thanh.

Vậy cái này trông như thế nào?

Chúng ta thấy gì ở đây?

Vì vậy, một lần nữa, hãy để tôi hướng dẫn bạn một chút ở đây.

Đây là trước khi đào tạo,

và đây là sau khóa đào tạo.

Vì vậy nếu chúng ta chỉ xem xét trước khi đào tạo,

sau đó chúng ta thấy rằng mô hình Alice tạo ra mã thông báo Alice

và mã thông báo Edgar với tỷ lệ phần trăm chính xác bằng nhau.

Mô hình Edgar cũng thích mã thông báo Edgar hơn,

nhưng tôi sẽ không giải thích điều này.

Về cơ bản sự khác biệt này ở đây,

vì đây là mô hình chưa qua đào tạo,

bất kỳ sự khác biệt nào bạn thấy ở đây chỉ là do ngẫu nhiên.

Bạn có thể coi cường độ này nằm trong phạm vi dự kiến

độ biến thiên của việc lấy mẫu.

Điều thú vị hơn là hãy xem điều gì sẽ xảy ra sau khóa đào tạo.

Và những gì bạn thấy là sự tương tác chéo.

Vì vậy, mô hình Alice tạo ra mã thông báo Alice nhiều hơn là tạo ra mã thông báo Edgar.

Trong khi đó, mô hình Edgar tạo ra nhiều mã thông báo Edgar hơn mã thông báo Alice.

Vì vậy, mặc dù những token này không phải là siêu độc đáo

đối với những cuốn sách cụ thể này, chúng là những từ thông dụng

như và, với, của, cái, vân vân,

chúng ta vẫn thấy có điều gì đó có ý nghĩa

trong các mã thông báo tần số cao này có thể

để phân biệt hai mô hình này.

Vì vậy, có được mô hình giao nhau tốt đẹp được mong đợi này.

Tôi đã chạy mã này và kiểm tra cốt truyện này nhiều lần

và mẫu mã luôn trông hơi khác một chút

nhưng bạn sẽ luôn thấy một số loại

của sự tương tác chéo như thế này.

Đôi khi bạn có thể thấy rằng thẻ Alice

không thực sự thay đổi nhiều đến vậy.

Vậy có thể hai thanh màu xanh này có tỷ lệ khá giống nhau

nhưng bạn sẽ thấy tùy chọn này

của mô hình Alice cho mã thông báo Alice

và mô hình Edgar cho token Edgar.

Được rồi, bây giờ chúng ta hãy đi đến phần đánh giá chất lượng.

Vâng, đây chính là văn bản mà tôi đang trình bày

cho cả mô hình Alice và mô hình Edgar.

Đây thực sự là đánh giá tương tự

mà chúng tôi đã làm trong video trước.

Tôi luôn thấy điều này thực sự hấp dẫn

và đáng yêu và kích thích tư duy.

Tôi thích đọc những điều này.

Nếu bạn tình cờ nhận được một điều thực sự thú vị

hoặc phản hồi hài hước từ những người mẫu này,

vui lòng chụp ảnh màn hình và đăng lên phần Hỏi đáp.

Tôi nghĩ tất cả chúng ta đều có cảm giác rằng điều đó sẽ tốt đẹp

nếu chúng ta có thể gắn những con số vào mọi thứ

mà chúng ta cần đánh giá ở con người.

Việc định lượng có vẻ như sẽ làm nên mọi thứ

tốt hơn, giảm bớt thành kiến, cho phép thực hiện hiệu quả hơn

và xã hội dựa trên thành tích, v.v.

Nhưng nhìn chung nó thực sự khó khăn

để định lượng chính xác rất nhiều thứ.

Và điều đó bao gồm nỗ lực của con người,

nhưng nó cũng bao gồm đầu ra

của các mô hình ngôn ngữ sáng tạo.

Và vâng, điều đó cũng áp dụng cho các mô hình tạo hình ảnh

cũng vậy.

Và bạn biết rằng văn bản đó rất hay khi bạn đọc nó,

nhưng thật khó để đưa ra một con số cho cảm giác chủ quan đó.

Dù sao, tôi hy vọng bạn thích thử thách viết mã này.

Trong video tiếp theo, chúng ta sẽ có hai mô hình này

thực sự có một cuộc trò chuyện nhỏ với nhau.