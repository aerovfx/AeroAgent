# 12 -Tinh chỉnh hiệu quả tham số (PEFT)

---

Trong video này, tôi sẽ giới thiệu với bạn một nhóm kỹ thuật được gọi là hiệu quả tham số

tinh chỉnh, thường được viết tắt là PEFT.

Nó liên quan chặt chẽ đến các thông số đóng băng trong quá trình đào tạo.

Trên thực tế, hầu hết các phương pháp PEFT đều liên quan đến việc đóng băng hầu hết hoặc tất cả các tham số có thể huấn luyện được.

trong một mô hình.

Tôi sẽ không đi sâu vào chi tiết về bất kỳ kỹ thuật riêng lẻ nào, nhưng

là một bộ sưu tập, những kỹ thuật này đáng để biết nếu bạn định tinh chỉnh

các mô hình lớn và nếu bạn không có quyền truy cập vào nhiều tài nguyên tính toán.

Bây giờ, đây không phải là những loại phương pháp mà bạn cần để đào tạo mô hình, hãy cùng

giả sử, 100 triệu tham số hoặc có thể lên tới một tỷ tham số.

Những phương pháp này thực sự được thiết kế khi bạn làm việc với các mô hình rất lớn trên

thứ tự 100 tỷ tham số.

Và vẫn có trường hợp bạn cần ít nhất một, và lý tưởng nhất là nhiều, mạnh mẽ

GPU.

Vì vậy, bạn không thể sử dụng một số thủ thuật thông minh để tinh chỉnh GPT-3 trên CPU máy tính xách tay.

Vâng, như tôi đã đề cập,

PEFT không phải là một phương pháp duy nhất,

mà là một nhóm các phương pháp cho phép bạn tinh chỉnh LLM.

Đây cũng không phải là thứ bạn sẽ sử dụng để đào tạo trước.

Đây là những kỹ thuật mà bạn sẽ áp dụng

đến các mô hình được đào tạo trước lớn mà bạn muốn tinh chỉnh

vào một số nhiệm vụ hẹp.

Bây giờ, có thể nhiệm vụ đó đang tạo ra văn bản mới giống như một chatbot,

mặc dù các phương pháp PEFT có xu hướng hoạt động tốt hơn

cho các nhiệm vụ đơn giản và có tính chất rõ ràng hơn

giống như sự phân loại.

Vì vậy, ý tưởng là đóng băng càng nhiều tham số

trong mô hình càng tốt

trong khi chỉ huấn luyện một số lượng nhỏ các tham số.

Một số phương pháp liên quan đến việc chèn các lớp mới

thành một mô hình cố định có thể áp dụng một số phép biến đổi

đến dữ liệu tạo nên mô hình được huấn luyện trước cố định

làm việc tốt hơn ở một nhiệm vụ cụ thể.

Như tôi đã đề cập, ưu điểm chính là nó cho phép bạn

để tinh chỉnh LLM nếu bạn không có quyền truy cập

sức mạnh tính toán mà bạn sẽ cần

để huấn luyện toàn bộ mạng.

Mặt khác, thậm chí thực hiện một đường chuyền về phía trước

với mô hình tham số 100 tỷ

vẫn có thể mất vài giây

thậm chí chỉ với một số ít token.

Vì vậy, nguồn lực hạn chế ở đây thực sự đang đề cập đến

đến một số GPU rất mạnh.

Và bạn có thể đối chiếu điều đó với hàng trăm hoặc hàng nghìn

GPU hàng đầu.

Bây giờ, như bạn có thể tưởng tượng,

nhược điểm chính của PEFT

là khó có khả năng đóng băng hầu hết mô hình

và thêm một vài tham số bổ sung ở đây và ở đó

sẽ mang lại cho bạn hiệu suất thực sự tốt hơn

hơn những gì bạn sẽ nhận được

từ một mô hình tinh chỉnh, có thể đào tạo hoàn toàn.

Người ta thường sử dụng PEFT để huấn luyện các mô hình cho các nhiệm vụ cụ thể,

như phân loại tài liệu trong một miền cụ thể.

Và điều đó thật tuyệt vời cho tên miền đó.

Nó có thể hoạt động rất tốt trong lĩnh vực đó,

nhưng mô hình được huấn luyện bằng PEFT

có thể khó khái quát hóa cho các nhiệm vụ mới

bởi vì luôn có sự cân bằng,

có một sự đánh đổi ở đây sao cho càng thu hẹp

và xác định rõ nhiệm vụ,

nó sẽ càng dễ dàng và thành công hơn

để tinh chỉnh một mô hình gần như bị đóng băng.

Nhưng điều đó không có nghĩa là mô hình ít có khả năng

để khái quát hóa các nhiệm vụ mới.

Có lẽ có hàng tá kỹ thuật cụ thể

nằm dưới sự bảo trợ của PEFT.

Trong slide này, tôi sẽ làm nổi bật bốn trong số đó,

chỉ để cho bạn biết cách chúng hoạt động.

Vì vậy, một loại phương pháp tiếp cận được gọi là bộ điều hợp.

Ý tưởng ở đây là bạn cố định toàn bộ mô hình,

nhưng sau đó bạn thêm vào một số lớp bổ sung,

như các mô-đun tại các vị trí quan trọng.

Nhiều mô-đun bộ điều hợp này, những lớp nhỏ này,

nằm giữa lớp con chú ý và lớp con MLP,

nhưng chúng cũng có thể được đặt giữa các khối máy biến áp.

Sau đó, ý tưởng là những mô-đun mạng thần kinh nhỏ này

tìm hiểu một số nhiệm vụ chuyển đổi liên quan

mà không cần phải thay đổi các thông số

và kiến thức thế giới mà mô hình đã thu được

trong quá trình đào tạo trước.

Bây giờ những mô-đun nhỏ được thêm vào này thực sự trông

giống như đối diện với lớp MLP,

theo nghĩa là chúng có xu hướng có nhiều chiều

ở đầu và ở cuối,

và có một lớp ẩn ở giữa

đó là chiều thấp cộng với một số tính phi tuyến,

giống như một Galoom.

Vì vậy, chúng thực sự có kiến ​​trúc giống như bộ mã hóa tự động.

Bây giờ, nếu bạn chưa quen với bộ mã hóa tự động,

thì đừng lo lắng, tôi sẽ mô tả chúng sau trong khóa học,

trong phần về khả năng diễn giải cơ học.

Vì vậy, đó là một chút về bộ điều hợp.

Có một bộ kỹ thuật khác

dựa vào sự phân tách thứ hạng thấp

của ma trận trọng số.

Nếu bạn không quá quen thuộc với đại số tuyến tính,

thì ý tưởng về một xấp xỉ thứ hạng thấp

đó là một ma trận nhỏ hơn

so với ma trận ban đầu, do đó có ít tham số hơn,

và nó giống như một biểu diễn được nén hoặc gần đúng

của ma trận đầy đủ.

Ví dụ, hãy tưởng tượng rằng sự chú ý có trọng lượng

là 1.000 x 1.000.

Và bây giờ hãy tưởng tượng rằng chúng ta có thể ước chừng ma trận đó bằng cách sử dụng

một ma trận 100 x 100.

Vậy điều đó có nghĩa là thay vì có

1 triệu tham số có thể huấn luyện được, chúng ta chỉ có 10.000 tham số có thể huấn luyện được

các thông số. Tất nhiên, phép tính gần đúng thứ hạng thấp không bao giờ hoàn hảo, vì vậy chúng ta sẽ mất

thông tin. Chúng tôi sẽ mất một số độ chính xác, nhưng hy vọng rằng thông tin và những chi tiết đó

những thứ bị mất không quá quan trọng đối với nhiệm vụ mà chúng ta đang thực hiện. Và sau đó ý tưởng là nó

việc đào tạo 10.000 tham số dễ dàng hơn nhiều so với một triệu tham số. Và tất nhiên đó chỉ là

cho một ma trận. Nếu bạn lặp lại điều này với nhiều ma trận trọng số trong toàn bộ mô hình,

điều này thực sự có thể tăng lên. Vì vậy, Laura và Dora là hai phương pháp cụ thể nằm trong danh mục

huấn luyện các phép tính gần đúng cấp thấp dựa trên phân tách ma trận thay vì toàn bộ trọng số

ma trận. Tiếp theo tôi sẽ cho bạn biết về ý tưởng của mô-đun tiền tố. Ý tưởng ở đây là đóng băng

toàn bộ mô hình và sau đó thêm một lớp khác trước phần nhúng ở đầu mô hình,

mà bạn thực sự đào tạo về nhiệm vụ cụ thể của mình. Và sau đó mô-đun tiền tố này sẽ học

cách chuyển đổi mã thông báo của bạn thành vectơ nhúng đã sửa đổi

được tối ưu hóa cho nhiệm vụ cụ thể của bạn.

Được rồi, cách tiếp cận cuối cùng mà tôi sẽ đề cập

là đóng băng tất cả trọng số trong mô hình

và đào tạo tất cả các điều khoản thiên vị.

Ở đây ý tưởng là có tương đối ít thuật ngữ sai lệch

so với tạ nên việc huấn luyện chúng dễ dàng hơn.

Bây giờ các số hạng sai lệch có thể khá mạnh trong các mô hình,

mặc dù phần lớn là tác động của chúng

là dịch chuyển xung quanh các phân phối.

Chúng có ít tác động hơn trong việc định hình lại không gian

trong đó các phần nhúng được thể hiện.

Được rồi, đây chắc chắn không phải là tất cả

của các kỹ thuật PEFT,

nhưng những kỹ thuật khác mà bạn sẽ gặp

bằng cách nào đó sẽ có liên quan đến những ý tưởng này.

Tôi sẽ không thảo luận thêm bất kỳ chi tiết toán học hoặc thực hiện cụ thể nào về

những phương thức này, nhưng có một số thư viện và hàm trong Python mà mọi người đã viết

để thực hiện các kỹ thuật này.

Ảnh chụp màn hình ở đây hiển thị trang web Ôm Mặt về PEFT.

Chắc chắn không phải trường hợp nào bạn cũng chỉ có thể sử dụng những phương pháp này thông qua Ôm Mặt,

Nhưng đó là trường hợp nếu bạn đang tải xuống và sử dụng mô hình được đào tạo trước từ Hugging

Face, thật thuận tiện khi sử dụng thư viện của họ cho các phương pháp PEFT.

Được rồi, vậy điểm mấu chốt ở đây về cơ bản chỉ là nhắc lại những gì tôi đã nói trong

đầu bài giảng.

Các phương pháp PEFT này không bao giờ thực sự tốt bằng việc tinh chỉnh hoàn toàn một mô hình,

nhưng chúng có thể hoạt động khá tốt nếu bạn có một nhiệm vụ dễ định lượng về mặt

một hàm mất mát và ít kiểu mở và khó đánh giá hơn như tạo văn bản

về một loạt các chủ đề.