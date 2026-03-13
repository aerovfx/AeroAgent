# 51 - Phân loại và đánh giá quá mức của Keras

---

Chào mừng mọi người quay trở lại với phần hai của mã phân loại của chúng ta trong phần hai, chúng ta sẽ chuyển sang

tạo mô hình và sau đó chỉ cho bạn cách giúp ngăn ngừa việc trang bị quá mức cho mô hình.

Hãy quay lại cuốn sổ và tiếp tục nơi chúng ta đã dừng lại lần trước.

Được rồi, tôi sẽ bắt đầu bằng cách nhập luồng tensor, thực ra, chúng ta sẽ nói từ luồng cảm biến.

Từ luồng Tenzer mang các mô hình đó nhập tuần tự.

Hãy chắc chắn rằng bạn đánh vần là nhập khẩu, phải không?

Chạy nó và sau đó chúng ta cũng sẽ nói từ luồng Tenzer mang quá trình nhập của lớp đó và trước tiên sẽ bắt đầu

không sử dụng các lớp dày đặc nữa, nhưng chúng tôi cũng sẽ thêm các lớp bỏ đi sau này.

Được rồi, vậy hãy tạo một mô hình rất đơn giản dựa trên những gì chúng ta đã biết cho đến nay về việc tạo mô hình.

Vì vậy, ngay bây giờ trong tập huấn luyện của tôi, tôi có 426 hàng, vì vậy không có nhiều hàng và

sau đó là 30 tính năng.

Vì vậy điều tôi sẽ làm là tạo ra một mô hình tuần tự.

Và sau đó tôi sẽ thêm vào.

Một lớp đầu tiên.

Trong số 30 nơron, và bạn có thể nói đơn vị bằng 30 nếu muốn.

Và khi đó kích hoạt sẽ chỉ là một đơn vị tuyến tính được chỉnh lưu và sau đó chúng ta sẽ lặp lại điều đó.

Ngoại trừ việc chúng ta sẽ tiếp tục cắt nó làm đôi để lớp tiếp theo sẽ giảm xuống còn 15 và chúng ta sẽ giữ mọi thứ

đơn giản để chúng ta có một lớp đầu ra cuối cùng và việc này sẽ diễn ra sau một năm nữa.

Tuy nhiên, kích hoạt và quan trọng sẽ là sigmoid vì đây là vấn đề phân loại nhị phân.

Vì vậy, đối với vấn đề phân loại nhị phân, chúng tôi muốn kích hoạt cuối cùng là sigmoid.

Kiểm tra các bài giảng lý thuyết về điều này.

Nếu bạn hơi mơ hồ về lý do tại sao chúng tôi chọn kích hoạt cụ thể đó.

Vì vậy, chúng ta có sự phân loại nhỏ, một nơ-ron xuất ra thứ gì đó giữa 0 và 1, và điều đó

sẽ quyết định xem nó thuộc loại nào, ác tính hay lành tính.

Và sau đó chúng tôi sẽ biên dịch cái này.

Chúng ta sẽ nói biên dịch mô hình.

Và chúng ta cũng phải đảm bảo rằng cuộc gọi cuối cùng này là chính xác.

Đây phải là entropy chéo gạch dưới nhị phân để nó hoạt động chính xác và sau đó là trình tối ưu hóa,

chúng tôi có nhiều tùy chọn khác nhau ở đây, nhưng chúng tôi sẽ tiếp tục và chỉ chọn một trình tối ưu hóa nguyên tử.

Vì vậy, chúng tôi đã tạo mô hình của mình và bây giờ là lúc đào tạo mô hình, chúng tôi sẽ xem mô hình phù hợp.

Và chúng ta sẽ nói X bằng cực trị, Y bằng Y train.

Và sau đó là các kỷ nguyên và tôi sẽ chọn một số lượng rất lớn các kỷ nguyên ở đây, vậy có lẽ là sáu trăm

có quá nhiều thứ cho khóa đào tạo cụ thể này, nhưng tôi thực sự muốn cho bạn thấy cụ thể nó trông như thế nào

giống như khi bạn quá khớp với dữ liệu huấn luyện của mình.

Và để làm điều đó, chúng tôi cũng sẽ chuyển dữ liệu xác thực của mình, chẳng hạn như dữ liệu xác thực, và chúng tôi sẽ

vượt qua bài kiểm tra X và chúng tôi kiểm tra.

Vì vậy, hãy tiếp tục và chạy cái này, việc này sẽ mất một lúc vì chúng ta đang chạy nó trong rất nhiều kỷ nguyên,

vì vậy tôi sẽ tua nhanh thời gian cho đến khi hoàn thành phần đào tạo về kỷ nguyên 600.

Vậy đó là 600 lần trong toàn bộ tập huấn luyện.

Vậy hãy để tôi tua nhanh thời gian, được chứ?

Đây vừa là khóa đào tạo hoàn thành cho 600 kỷ nguyên đó.

Việc chúng ta sắp làm bây giờ là tiếp tục và vạch ra tổn thất và ghi nhớ ai đã vượt qua quá trình xác thực của chúng ta

dữ liệu trong quá trình huấn luyện.

Vì vậy, chúng ta sẽ có thể biểu diễn cả tổn thất huấn luyện và tổn thất xác nhận.

Hãy nhớ lại rằng tôi có thể mô hình hóa lịch sử đó, lịch sử đó và tôi có thể chuyển nó vào một cái chảo, dữ liệu này

khung.

Và chúng ta sẽ gọi đó là tổn thất.

Và đây là tổn thất của tôi, tôi có tổn thất huấn luyện và tổn thất xác nhận.

Chúng ta hãy tiếp tục vẽ sơ đồ này và xem nó trông như thế nào.

Vì vậy, đây là những mất mát của tôi và đây là một ví dụ hoàn hảo về việc trang bị quá mức, vậy đặc điểm chính là gì

đây là Overfitting?

Bạn sẽ nhận thấy ngay từ đầu, trong vài kỷ nguyên đầu tiên, cả xác nhận và tổn thất giao dịch

đều đang giảm dần.

tốt đấy.

Điều đó có nghĩa là chúng tôi chưa phù hợp với dữ liệu đào tạo của mình.

Và khi tiếp tục, chúng tôi sẽ giảm tổn thất trong cả tập xác thực và tập huấn luyện.

Tuy nhiên, tại một thời điểm nhất định, hãy lưu ý rằng mức độ mất tập luyện ở đây trong màu xanh lam của chúng tôi vẫn đang giảm dần.

Tuy nhiên, tổn thất xác thực của chúng tôi đang bắt đầu tăng lên.

Về cơ bản, điều đó cho chúng ta biết rằng chúng ta đang trang bị quá mức cho tập dữ liệu huấn luyện của mình.

Vì vậy, chúng tôi có một dấu hiệu rõ ràng ở đây rằng chúng tôi đang đào tạo chỉ vì quá nhiều kỷ nguyên nhận thấy việc xác thực

sự mất mát ngày càng trở nên tồi tệ hơn sau những thời kỳ này.

Vì vậy, chúng ta sẽ xem liệu chúng ta có thể sử dụng phương pháp dừng sớm hay không.

Vì vậy, rõ ràng là chúng ta đã được đào tạo quá nhiều.

Và chúng tôi sẽ chỉ cho bạn cách sử dụng lệnh gọi lại keris dòng tensor để thực sự dựa trên xác thực của bạn

pháp luật, hãy dừng việc đào tạo trước khi nó vượt quá tầm kiểm soát như minh họa ở đây.

Vì vậy tôi sẽ sao chép và dán lại mô hình của chúng ta.

Và đây là điều quan trọng để thể hiện điều này, bởi vì chúng tôi không muốn tiếp tục đào tạo

cùng một mô hình.

Tôi muốn tạo lại mô hình mới nên tôi sẽ sao chép và dán.

Hãy cuộn xuống các lệnh này, tiếp tục và xác định lại mô hình của bạn một lần nữa, sau đó để tôi hiển thị

bạn cách chúng tôi có thể sử dụng lệnh gọi lại.

Và đây không phải là lệnh gọi lại duy nhất mà chúng tôi sẽ sử dụng trong suốt khóa học.

Chúng tôi sẽ nói rằng đây là trường hợp đầu tiên sử dụng một công cụ từ Tenzer float mang tính năng nhập lệnh gọi lại DOT.

Và lệnh gọi lại mà chúng ta đang tìm hiểu bây giờ được gọi là dừng sớm.

Và tôi khuyến khích bạn gọi trợ giúp về việc cắt sớm để xem chi tiết đầy đủ về nó.

Nhưng về cơ bản điều đang diễn ra ở đây là chúng ta phải chọn một thước đo để theo dõi.

Trong trường hợp của chúng tôi, đó sẽ là mất xác thực, số liệu màu cam này ở ngay đây.

Vì vậy, chúng tôi sẽ theo dõi việc mất xác thực đó.

Và sau đó bạn cũng có thể chỉ định những thứ như thay đổi tối thiểu cần thiết.

Ngoài ra còn có sự kiên nhẫn, đó là số lần không tiến bộ, sau đó quá trình đào tạo sẽ

được dừng lại.

Vì vậy, nó không chỉ dừng lại.

Ngay khi mức độ mất xác thực tăng lên một chút, bạn có thể thấy rằng trong suốt quá trình đào tạo có

một chút tiếng ồn.

Vì vậy, có lẽ chúng ta muốn đợi một vài kỷ nguyên để có thể có thông số kiên nhẫn ở đó.

Và chúng ta sẽ có những phương thức đào tạo khác nhau.

Rất nhiều thứ khác nhau mà bạn có thể khám phá ở đây và thậm chí bạn có thể xem ví dụ đầy đủ có sẵn

cho bạn trong luồng bến tàu.

Nhưng hãy để tôi chỉ cho bạn cách sử dụng tính năng dừng sớm này.

Và việc dừng sớm về cơ bản có hai bước.

Một là định nghĩa biến dừng sớm bằng.

Dừng sớm, vì vậy chúng tôi thực hiện cuộc gọi thực tế đó và trong trường hợp của chúng tôi, chúng tôi sẽ kiểm duyệt, giám sát,

xác nhận, mất mát.

Và chế độ mà chúng tôi thực sự đang tìm kiếm là nam giới, vì vậy có một vài chế độ khác nhau ở đây,

chúng ta có thể quay lại đây và kiểm tra chúng.

Hãy nhớ lại rằng chế độ này về cơ bản là điều bạn thực sự đang cố gắng làm ở đây hay bạn đang cố gắng giảm thiểu

thứ bạn đang theo dõi hay bạn đang cố gắng tối đa hóa thứ bạn đang theo dõi, v.v.?

Vì vậy, bạn có thể tưởng tượng nếu số liệu của chúng tôi là độ chính xác, độ chính xác, thứ bạn muốn tối đa hóa, nếu số liệu của chúng tôi

là mất mát, về cơ bản là mặt trái của độ chính xác.

Mất mát là điều bạn muốn giảm thiểu.

Vì vậy, hãy ghi nhớ điều đó.

Và còn có một chuỗi tự động nhỏ xinh này về cơ bản hướng được tự động suy ra

từ tên của số lượng màn hình.

Vì vậy, nó sẽ suy ra nó dựa trên chuỗi.

Điều đó thường hầu như luôn luôn hoạt động.

Nhưng trong trường hợp không, tôi khuyên bạn nên đặt Min hoặc Max theo cách thủ công.

Nó cũng cho bạn biết rằng bạn biết đủ về số liệu bạn thực sự đang theo dõi để hiểu điều gì

bạn nên làm gì để dừng lại sớm.

Vì vậy, trong trường hợp này, chúng tôi đang theo dõi việc mất xác thực, đây là điều chúng tôi muốn giảm thiểu, bởi vì nếu

chúng ta có lỗ bằng 0, điều đó có nghĩa là chúng ta có sự phù hợp hoàn hảo.

Vì vậy, chúng tôi sẽ đi vào và nói rằng việc dừng sớm quá trình giám sát hoặc mất xác thực, hãy cố gắng giảm thiểu điều đó.

Và chúng ta cũng sẽ nói ferbos bằng một.

Về cơ bản, chỉ cần có một báo cáo nhỏ và sau đó chúng tôi sẽ đặt số bệnh nhân là 25.

Điều đó có nghĩa là chúng tôi sẽ đợi 25 kỷ nguyên ngay cả sau khi chúng tôi phát hiện ra điểm dừng do nhiễu

có thể xảy ra.

Vì vậy, chúng tôi tạo biến dừng sớm này và sau đó gọi mô hình phù hợp và tôi sẽ sao chép

lệnh tương tự chúng ta đã sử dụng trước đây.

Như vậy ở đây chúng ta có lệnh phù hợp với mô hình ban đầu.

Chỉ cần tiếp tục và sao chép nó.

Vì vậy chúng ta sẽ đi và sao chép nội dung của ô đó.

Hãy đảm bảo rằng bạn đã xác định lại mô hình, nếu không bạn sẽ vô tình huấn luyện mô hình cũ.

Vì vậy, chúng tôi vừa xác định lại mô hình và tôi đang gọi mô hình phù hợp với mọi thứ trông giống nhau, ngoại trừ

bây giờ tôi sẽ thêm vào một vài dòng nữa ở đây.

Chúng tôi sẽ nói tham số gọi lại hoặc số lần gọi lại bằng và bạn thực sự vượt qua Thượng viện dưới dạng danh sách,

ngay cả khi đó chỉ là một và bạn vượt qua cuộc gọi lại dừng sớm đó.

Vì vậy, hãy tiếp tục và chạy cái này và bây giờ điều đó sẽ xảy ra là nó sẽ cố gắng chạy trên 600 kỷ nguyên

trừ khi lệnh dừng sớm được kích hoạt và trong trường hợp này, hãy biết rằng lệnh dừng sớm đã được kích hoạt.

Và nếu bạn cuộn xuống đây, trời sẽ ngừng mưa sau 81 giờ.

Vì vậy, nó có cuộc gọi dừng sớm.

Thật tốt khi chúng ta biết rằng sáu trăm là quá nhiều.

Và điều thú vị ở đây là giờ đây bạn có thể dừng sớm ở một số lượng lớn tùy ý

của các kỷ nguyên và sau đó cho biết rằng bạn muốn nó dừng sớm bằng lệnh gọi lại này.

Vì vậy, bây giờ bạn không phải lo lắng quá nhiều về việc chọn số chính xác cho các kỷ nguyên kể từ khi gọi lại

với điểm dừng sớm sẽ tự động xử lý việc đó cho bạn.

Bây giờ chúng ta hãy kiểm tra sự mất mát của mô hình đó.

Vì vậy, chúng tôi sẽ nói rằng việc mất mô hình bằng với lệnh gọi khung dữ liệu của chú gấu trúc này trong lịch sử mô hình, lịch sử.

Và sau đó chúng ta sẽ nói mất mô hình cốt truyện.

Hãy tiếp tục và chạy cái này, và đây chính xác là loại cốt truyện mà chúng tôi muốn xem hoặc mất và xác thực

sự mất mát đều bắt đầu giảm dần và ngay khi chúng bắt đầu lan rộng, đó có lẽ là một dấu hiệu tốt

về nơi chúng ta nên ngừng đào tạo.

Vì vậy, hãy chú ý điều này làm phẳng đi.

Không sao đâu.

hành vi.

Vâng, chúng tôi muốn ngăn chặn tình trạng mất xác nhận bắt đầu gia tăng.

Và đó là điều đã xảy ra quá sớm.

Đã dừng được kích hoạt.

Được rồi.

Vì vậy, điều thứ ba chúng ta có thể làm là cố gắng ngăn chặn việc trang bị quá mức bằng cách thêm vào các lớp bỏ đi.

Vì vậy, các lớp bị loại bỏ về cơ bản sẽ tắt một phần trăm tế bào thần kinh một cách ngẫu nhiên.

Vì vậy, hãy quay lại đây và tôi sẽ sao chép và dán lại mô hình của mình để đảm bảo rằng tôi không vô tình

tiếp tục đào tạo mô hình cũ của tôi.

Vậy là lại có mô hình của tôi và điều tôi sắp làm là tôi cũng vậy, bạn có thể thực hiện việc này trong cùng một ô hoặc

trong ô phía trên nó, chúng ta sẽ nói từ dòng tensor.

Việc bỏ nhập khẩu của lớp suy nghĩ tò mò về mặt kỹ thuật đã được thực hiện, tôi chỉ muốn làm rõ

rằng cuộc gọi bỏ học đến từ các lớp ký tự và lẽ ra bạn phải nhập cái này trước đó,

nhưng hãy tiếp tục và làm lại.

Và những gì chúng ta sắp làm là sau mỗi lớp trong số hai lớp dày đặc này, chúng ta sẽ thêm vào Colonsay bị bỏ rơi

mô hình ADD.

Và sau đó chúng ta nói drop out và khi đó tham số chính bạn chọn sẽ drop out.

Bạn có thể thực hiện tab shift ở đây và bạn sẽ nhận thấy rằng điều chính về cơ bản là tỷ lệ và tỷ lệ là

xác suất mà bạn sẽ ngẫu nhiên tắt các nơ-ron thực sự.

Vì vậy, đó là phần mà bạn tắt chúng một cách ngẫu nhiên.

Vì vậy, nếu bạn đặt số 0, điều đó có nghĩa là bạn đang lấy 0% số nơ-ron và biến chúng một cách ngẫu nhiên

tắt trong quá trình đào tạo.

Nếu bạn đặt một cái ở đây, bạn thường sẽ không bao giờ làm điều đó.

Nhưng về cơ bản điều đó có nghĩa là 100% tế bào thần kinh sẽ bị tắt một cách ngẫu nhiên

cho từng đợt đào tạo.

Vì vậy, một giá trị thực sự phổ biến nằm ở đâu đó giữa 0 phẩy 2 và 0 phẩy 5.

Và về cơ bản điều đó có nghĩa là một nửa số nơ-ron trong mỗi đợt, về cơ bản mỗi đợt là một toàn bộ

kỷ nguyên đào tạo trong trường hợp của chúng tôi, bởi vì chúng tôi chưa chỉ định ở kích thước đó một nửa số nơ-ron đó trong trường hợp này

lớp 30 sẽ bị tắt.

Vì vậy, trọng số và thành kiến ​​sẽ không được cập nhật.

Vì vậy chúng ta sẽ tiếp tục và đặt nó ở đây.

Và điều đó có nghĩa là, một lần nữa, khoảng một nửa số nơ-ron này sẽ bị tắt một cách ngẫu nhiên, nên điều đó không phải

cùng một nơ-ron mỗi lần chọn ngẫu nhiên 50% số nơ-ron.

Được rồi, vậy thì về cơ bản mỗi nơ-ron có xác suất 50% bị tắt trong mỗi đợt.

Vì vậy, hãy tiếp tục và chạy lại cái này.

Vì vậy, chúng tôi xác định lại mô hình của mình và sau đó chúng tôi sẽ sử dụng mô hình này kết hợp với việc loại bỏ để chúng tôi vẫn có thể giữ lại

tương tự dừng sớm ở đây.

Nhưng tôi sẽ sao chép và dán nội dung của mô hình này cho phù hợp.

Chúng tôi vẫn còn điểm dừng sớm và bây giờ chúng tôi đã thêm những người bỏ học này.

Vì vậy, cả hai điều này thực sự sẽ giúp ngăn ngừa tình trạng Overfitting.

Chúng ta sẽ tiếp tục và chạy cái này.

Và chúng ta không nên mong đợi điều này sẽ chạy trên tất cả 600 kỷ nguyên.

Vì vậy, hãy tiếp tục và đợi một chút và cuối cùng nó sẽ ngừng chạy.

Lưu ý rằng nó đã chạy lâu hơn một chút và điều đó thực sự tốt vì điều đó có nghĩa là nó vẫn đang học

ngay cả ở những kỷ nguyên xa hơn, và đó là do thực tế của các lớp bỏ học này.

Vì vậy, hãy tiếp tục và phân tích ngay bây giờ.

Những mất mát ở đây sẽ nói.

Mất mô hình bằng khung dữ liệu PD.

Lịch sử mô hình.

Và sau đó chúng ta sẽ tiếp tục và vạch ra điều này, và đây thậm chí còn là hành vi tốt hơn, trên thực tế, đây hoàn toàn là

tuyệt vời.

Lưu ý rằng luật đào tạo và luật xác nhận đều nhanh chóng giảm xuống và về cơ bản chúng

đang bị san phẳng với tốc độ như nhau.

Đây chính xác là loại hành vi bạn muốn thấy.

Điều này được cải thiện nhiều so với những gì chúng ta đã thấy trước đó.

Hãy nhớ lại cốt truyện ban đầu của chúng tôi ở đây, ngay cả ở thời điểm đó, chúng tôi rõ ràng đã trang bị quá mức.

Vì vậy, việc không thêm tính năng dừng sớm và thêm các lớp bỏ học đó đã tăng hiệu suất đáng kể.

Vì vậy, bây giờ chúng ta hãy thực hiện đánh giá đầy đủ về các lớp học của chúng ta.

Hãy nhớ lại rằng chúng ta đang thực hiện một nhiệm vụ phân loại.

Vì vậy, về cơ bản chúng tôi dự đoán là số 0 hoặc số 1.

Và cách Charise làm việc này là thay vì nói mô hình dự đoán, giờ đây chúng tôi thực sự nói mô hình

dự đoán, gạch dưới các lớp.

Chúng tôi chuyển vào tập dữ liệu thử nghiệm của mình.

Và cuối cùng nó sẽ hiển thị cho bạn các lớp mà nó dự đoán cho tập dữ liệu thử nghiệm và gọi lại ngay cả khi

bạn có một số khối u mới với tất cả những đặc điểm này, nó vẫn chỉ là các lớp.

Một điểm dữ liệu mới về cơ bản giống hệt như một tập kiểm tra.

Vì vậy, chúng ta sẽ tiếp tục và nói, đây là những dự đoán của chúng tôi và bây giờ hãy tiếp tục và nói từ Escalon

số liệu đó quan trọng và có hai thứ chính mà chúng tôi nhập vào cho vấn đề phân loại và đó

là một báo cáo phân loại.

Và họ nhầm lẫn ma trận và chắc chắn hãy xem các bài giảng lý thuyết máy học, nếu bạn có

bất kỳ câu hỏi nào về những thứ như độ chính xác, độ chính xác, hãy nhớ lại điểm F1 của chúng tôi.

Chúng tôi thực sự đã đề cập đến những gì chúng đại diện.

Vì vậy, chúng tôi sẽ tiếp tục và in ra báo cáo phân loại của mình và điều này sẽ có màu trắng đúng trong trường hợp đó,

đó là lý do tại sao chúng tôi phải kiểm tra và so sánh trực tiếp với các dự đoán.

Vì vậy, hãy tiếp tục và chạy nó và chúng ta có thể thấy kết quả ở đây.

Vì vậy, hãy lưu ý rằng chúng tôi đang có hiệu suất rất tốt và chúng tôi có thể kiểm tra hiệu suất bằng cách in ra sự nhầm lẫn của mình

ma trận.

Hiển thị so sánh các thử nghiệm trắng với dự đoán của chúng tôi và điều đó về cơ bản cho thấy rằng mạng của chúng tôi

chỉ phân loại sai một điểm trong tập kiểm tra của chúng tôi, điểm của bạn có thể hơi khác một chút.

Bạn có thể phân loại sai một số tập hợp cụ thể hơn, đặc biệt nếu bạn đang sử dụng cách phân chia ngẫu nhiên khác với

chúng tôi.

Nhưng nhìn chung, về tổng thể, bạn lẽ ra phải đạt được hiệu suất tốt hơn 0,95 về độ chính xác

và nhớ lại.

Được rồi, vậy bạn cũng có thể kiểm tra độ chính xác hoặc độ chính xác 99 phần trăm.

Và chúng tôi đang làm rất tốt về độ chính xác và nhớ lại rằng ở đây độ chính xác là một thước đo tốt

bởi vì chúng tôi thấy rằng chúng tôi có các lớp học tương đối cân bằng.

Chúng không hoàn toàn cân bằng nhưng cũng không phải là cực kỳ mất cân bằng.

Và đó chính là mục đích của việc ghi nhãn thực tế này.

Được rồi.

Vì vậy, bây giờ chúng tôi có nhiều công cụ hơn trong kho vũ khí của mình để học sâu.

Bây giờ chúng tôi đã hiểu rằng chúng tôi có thể thêm vào và thả các lớp và chúng tôi cũng có thể sử dụng tính năng dừng sớm để không có

phải lo lắng về số lượng kỷ nguyên mà chúng ta đang đào tạo.

Rất nhiều thứ khác nhau mà chúng tôi sẽ tiếp tục bổ sung vào bộ công cụ của mình để trở nên tốt hơn

những người thực hành học sâu với dòng tensor.

Được rồi, cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.