# 019 Nối một lát dây vi

---

Người hướng dẫn: Ở phần trước chúng ta đã khám phá được

rằng bằng cách nào đó chúng ta phải chọn loại bộ bài của mình

và tìm ra cách giảm nó xuống còn một byte.

Vì vậy, chúng tôi vừa tạo một hàm gọi là chuỗi ngay tại đây.

Nó có một bộ thu loại boong

và sau đó nó sẽ trả về một chuỗi.

Vì vậy, hãy tìm hiểu chính xác cách chúng ta sẽ làm điều này.

Vậy bước một là chúng ta sẽ lấy bộ bài này

và chúng ta sẽ biến nó trở lại thành một đoạn chuỗi kiểu.

Để làm như vậy, chúng ta sẽ sử dụng công cụ chuyển đổi kiểu tương tự

mà chúng ta vừa xem xét cách đây không lâu.

Vì vậy chúng ta sẽ nói lấy, hoặc những gì tôi muốn có,

loại tôi muốn có sẽ là một lát

thuộc loại chuỗi.

Và tôi sẽ chuyển giá trị mà tôi có

đó là D, đó là máy thu,

đó chính là bộ bài thực sự mà chúng tôi đang sử dụng.

Vì thế cái này ở đây sẽ trả lại cho tôi

một danh sách các chuỗi hoặc một lát chuỗi.

Bây giờ chúng tôi có thể thực hiện chuyển đổi này ngay tại đây

của một bộ bài thành một lát dây.

Bạn sẽ nhớ lại, vì về cơ bản loại bộ bài của chúng tôi

dù sao cũng là một đoạn chuỗi,

vì vậy chúng ta có thể tự do chuyển đổi sao lưu chuỗi ở đây

sang loại mà chúng tôi đã mở rộng từ đó.

Vì vậy, với tuyên bố này ngay tại đây

chúng ta có một lát dây.

Bây giờ bước tiếp theo là bằng cách nào đó

lấy đoạn dây đó

và cô đọng nó thành một chuỗi duy nhất.

Và vì vậy điều này thực sự sẽ không tệ đến thế.

Tôi nghĩ điều chúng ta có thể làm là lấy đoạn dây đó

và chúng ta có thể nối mọi giá trị bên trong nó

bằng dấu phẩy ở giữa mỗi giá trị.

Nói cách khác, nếu chúng ta có một lát chuỗi

của thứ gì đó như đỏ, vàng và xanh,

Tôi nghĩ chúng ta có thể cô đọng điều này lại

đến một chuỗi dấu phẩy màu đỏ màu vàng, dấu phẩy màu xanh, như vậy.

Và đó là điều chúng ta sẽ làm

để biến lát chuỗi thành một chuỗi duy nhất.

Bây giờ chúng ta không phải làm

quá trình chuyển đổi thực tế đó theo cách thủ công.

Có một gói trợ giúp nhỏ khác

mà chúng ta có thể tận dụng

để lấy đoạn dây này và nối chúng lại

tất cả cùng nhau tự động.

Vì vậy, một lần nữa, hãy đi sâu vào tài liệu về cờ vây của chúng tôi.

Tôi sẽ mở lại trình duyệt của mình.

Tôi sẽ quay lại IOU cho đến khi có tài liệu.

Tôi sẽ quay lại với danh sách lớn các gói hàng.

Nó ở ngay đây này.

Và tôi sẽ đi tìm

một gói rất cụ thể được gọi là strings.

Vì vậy, đây là chuỗi ngay tại đây.

Các chuỗi gói có một số chức năng rất phổ biến

để làm việc hoặc xử lý các chuỗi

như bạn có thể đoán bằng tên gói.

Vì vậy, nếu chúng ta nhìn vào tài liệu

rồi cuộn xuống danh sách

của tất cả các chức năng khác nhau ở đây,

có một chức năng trông rất thú vị

được gọi là tham gia ngay tại đây.

Vì vậy, chúng tôi sẽ nhấp vào nó và kiểm tra tài liệu.

Hàm nối lấy một lát chuỗi,

đó chính xác là những gì chúng ta có,

và nó kết hợp tất cả chúng lại với nhau để tạo ra

một màn hình riêng biệt hoặc một màn hình duy nhất, xin lỗi.

Ở giữa mỗi phần tử bên trong lát chuỗi

chúng tôi đặt bất cứ điều gì chúng tôi chuyển vào làm đối số thứ hai.

Sep ở đây là viết tắt của dấu phân cách.

Vì vậy, về cơ bản nếu chúng ta gọi strings.join,

hoặc nếu chúng ta gọi hàm nối này ở đây

và sau đó chuyển vào làm đối số thứ hai, dấu phẩy,

nó sẽ lấy đoạn dây của chúng ta

và giảm nó xuống còn một chuỗi duy nhất.

Được rồi, hãy quay lại trình soạn thảo mã của chúng ta

và làm cho điều này xảy ra.

Bây giờ điều đầu tiên chúng ta phải làm ở đây

hãy đảm bảo rằng chúng tôi nhập vào gói chuỗi đó.

Vì vậy chúng ta phải nhập nó

trước khi chúng ta thử sử dụng chức năng đó.

Vì vậy, ở đầu tập tin

bạn sẽ nhận thấy rằng chúng tôi đã có một báo cáo nhập khẩu

cho fmt ngay tại đây.

Để nhập vào nhiều thư viện,

chúng tôi không viết trong một tuyên bố nhập khẩu riêng biệt như vậy.

Thay vào đó, chúng tôi sẽ kết thúc câu lệnh nhập hiện có của mình

với một bộ dấu ngoặc đơn.

Chúng tôi sẽ đặt cái này lên một dòng mới như vậy.

Và ngay bên dưới nó chúng ta sẽ liệt kê ra

mọi gói khác mà chúng tôi muốn nhập

cũng vào đây.

Vì vậy, đối với chúng tôi, chúng tôi muốn nhập gói chuỗi.

Vì vậy, chúng ta sẽ nói chuỗi, như vậy.

Bạn sẽ nhận thấy rằng chúng tôi không tách chúng ra

bằng dấu phẩy hoặc bất cứ thứ gì tương tự.

Vì vậy chúng ta chỉ liệt kê từng chuỗi một

không có dải phân cách ở giữa chúng

tất cả các gói khác nhau mà chúng tôi muốn có quyền truy cập.

Vậy bây giờ hãy quay lại phần dưới cùng ở đây,

bên trong hàm hai chuỗi của chúng tôi,

bây giờ chúng ta có thể truy cập chức năng tham gia đó ngay tại đây

bằng cách gọi strings.Join.

Và ngay khi tôi gõ chữ tham gia,

bạn sẽ thấy kiểu kích hoạt tự động hoàn chỉnh ở đây.

Và đó là tín hiệu của bạn về,

được rồi, ừ có vẻ như chúng ta đang đi đúng đường.

Vì vậy bây giờ là đối số đầu tiên

chúng ta sẽ chuyển vào lát chuỗi của mình,

đó là tuyên bố mà chúng tôi vừa thêm vào ngay tại đây.

Vì vậy, tôi sẽ cắt nó, dán nó vào làm đối số đầu tiên

và trong lập luận thứ hai tôi sẽ nói,

Này, tôi muốn nối mọi thứ bằng dấu phân cách bằng dấu phẩy.

Và dấu phân cách được coi là kiểu chuỗi.

Và đó là lý do tại sao chúng ta đang tạo ra một chuỗi.

Được rồi, vậy strings.Tham gia ngay tại đây

sẽ lấy đoạn dây của chúng ta,

nối tất cả thành một chuỗi duy nhất được phân tách bằng dấu phẩy.

Và chúng ta cần đảm bảo rằng từ hàm hai chuỗi

cuối cùng chúng tôi trả về một cái gì đó thuộc loại chuỗi.

Vì vậy tôi sẽ thêm vào câu lệnh return ngay tại đó.

Được rồi, bây giờ chúng ta sẽ lưu tập tin.

Khi làm thì không thấy lỗi gì cả

nên có vẻ như chúng ta ổn.

Bây giờ chúng ta hãy kiểm tra điều này bên trong tệp dot go chính của chúng ta.

Vậy nên tôi sẽ lật ngược lại.

Tôi sẽ xóa câu nói chơi đùa đó

chúng tôi có ngay tại đây.

Tôi sẽ làm một bộ bài mới.

Vì vậy, tôi sẽ nói bộ bài mới.

Và bạn biết không, chúng ta có thể xóa mọi thứ

mà chúng tôi đã nhận xét rồi.

Vậy nên tôi sẽ làm bộ bài mới của mình

và sau đó chúng ta sẽ gọi nó là cards.toString.

Và tất nhiên tôi muốn in cái này ra thiết bị đầu cuối

để đảm bảo nó hoạt động chính xác.

Vì vậy tôi sẽ nói fmt.Print ln,

rồi chuyển kết quả của chuỗi đó vào.

Được rồi, hãy lưu lại và kiểm tra nó.

Tôi sẽ chuyển sang thiết bị đầu cuối của mình.

Chúng ta sẽ chạy, chạy, chạy chính.

Và đừng quên thêm deck.go vào đây.

Và khi tôi làm vậy,

chúng tôi lấy ra danh sách các thẻ được phân tách bằng dấu phẩy.

Và đây là một chuỗi duy nhất.

Vì vậy, vào thời điểm này, điều đó thực sự dễ dàng

để tưởng tượng chúng ta sẽ thực sự kết thúc việc này như thế nào

và sử dụng IOU đó cho đến khi hoạt động.

Vì vậy, hãy quay lại IOU cho đến ngay tại đây, ngay để nộp hồ sơ.

Vì vậy, tại thời điểm này chúng ta có một chuỗi

bao gồm tất cả các dữ liệu

mà chúng ta muốn lưu vào ổ cứng.

Vậy bây giờ điều cuối cùng chúng ta phải làm

là biến cái này thành một lát byte,

mà chúng ta gần như đã thấy rồi

và sau đó gọi chức năng ghi tập tin này.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng

và giải quyết vấn đề này trong phần tiếp theo.