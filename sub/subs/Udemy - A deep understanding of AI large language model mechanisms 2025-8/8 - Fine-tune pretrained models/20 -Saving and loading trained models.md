# 20 -Lưu và tải các mô hình đã đào tạo

---

Trong hai phần trước của khóa học, chúng tôi đã đào tạo rất nhiều mô hình, nhưng ở

ở cuối video, chúng tôi luôn thoát khỏi phiên Python và sau đó là tất cả công việc khó khăn của chúng tôi

biến mất khỏi vũ trụ.

Vì vậy, điều tôi sẽ dạy bạn trong video này là cách lưu mô hình sau khi bạn sửa đổi

chúng và sau đó là cách nhập chúng trở lại Python.

Thực tế có một số cách để lưu các tham số và thông tin mô hình tùy thuộc vào việc liệu

bạn đang làm việc với mô hình khuôn mặt ôm hoặc bất kỳ loại mô hình nào khác trong PyTorch.

Tôi sẽ bắt đầu bằng cách nhập mô hình GPT-2 đã được đào tạo trước mà bạn đã thấy nhiều lần.

Mình sẽ hướng dẫn các bạn cách lưu mô hình đó bằng các phương pháp trong mô hình ôm khuôn mặt.

Bây giờ, mô hình không thực sự được lưu trữ dưới dạng một tệp duy nhất,

nhưng thay vào đó là một thư mục

với một số tệp riêng lẻ có trong thư mục đó.

Vậy đây là những file JSON chứa thông tin

về mô hình, về cấu hình của mô hình.

Một số trong số này chúng ta có thể mở trực tiếp

và chỉ cần nhìn vào văn bản bên trong các tập tin này.

Cái này ở đây, có một tensor an toàn mở rộng,

cái này chứa tất cả các tham số mô hình,

tất cả các ma trận trọng số và thông tin PyTorch khác.

Tập tin này lớn hơn rất nhiều.

Ví dụ: nó nặng khoảng nửa gigabyte

cho tệp nhỏ GPT-2.

Sau đó chúng tôi sẽ sửa đổi trọng số mô hình

để thay thế ma trận nhúng bằng tất cả ma trận nhúng.

Bây giờ, không cần phải nói, đây không phải là một ý tưởng hay cho lắm

nếu chúng ta thực sự muốn sử dụng mô hình này,

nhưng tôi chỉ làm điều này để nó rất rõ ràng

khi chúng tôi nhập lại mô hình,

rằng chúng tôi đã lưu mô hình mà chúng tôi đã sửa đổi

và nhập lại nó một cách chính xác.

Và vâng, đó là thứ tôi sẽ cho bạn xem tiếp theo,

cách nhập mô hình mà bạn đã đào tạo và lưu.

Bây giờ, tất cả những điều này cho đến nay chỉ là lưu trữ

và tải dữ liệu bằng định dạng mô hình khuôn mặt ôm.

Tôi cũng sẽ chỉ cho bạn cách lưu mô hình

sử dụng định dạng của PyTorch mà bạn sẽ sử dụng

nếu bạn không làm việc với mẫu khuôn mặt ôm.

Và cuối cùng, tôi sẽ hướng dẫn bạn cách nén các thư mục này

để bạn có thể tải chúng xuống máy tính của mình.

Vì vậy, ở đây tôi nhập GPT-2,

và phải mất một phút để tải vào.

Và bây giờ tôi sẽ sử dụng phương pháp này

trên đối tượng GPT-2 có tên là lưu được đào tạo trước.

Và ở đây tôi sẽ mở biểu tượng thư mục này ở bên trái.

Điều này cho tôi thấy tất cả dữ liệu mà tôi đã lưu trữ.

Vì vậy, tất cả các tệp được đính kèm vào phiên Python này

trong Google Colab.

Hiện giờ chẳng có gì ở đó ngoại trừ

thư mục mặc định luôn được nhập

bất cứ khi nào bạn mở một phiên Python.

Vì vậy, nó đi kèm với một ít dữ liệu,

chỉ là một số ví dụ nổi tiếng trong thống kê

và học máy như tập dữ liệu MNIST,

bạn có thể quen với điều này.

Dù sao thì điều này vẫn luôn ở đó.

Được rồi, bây giờ tôi sẽ sử dụng GPT2.savePretraining.

Tôi sẽ gọi đây là HF gốc để ôm mặt.

Vì vậy, bạn có thể thấy thư mục đó vừa xuất hiện một cách kỳ diệu

ở đây.

Và bây giờ, vâng, như tôi đã đề cập trong các slide,

đây không phải là một tập tin dành cho mô hình,

nó là một thư mục cho mô hình.

Vậy chúng ta có thể mở nó ra, tập tin này là văn bản,

chúng ta chỉ có thể nhìn vào nó.

Và bạn sẽ nhận ra thông tin này ở đây.

Khi chúng ta gõ GPT-2, được rồi, hãy để tôi đóng nó lại.

Khi chúng ta gõ, hãy để tôi đặt nó ở đây, GPT-2,

Sau đó, xin lỗi, chúng tôi nhận được gpt2.config.

Sau đó chúng ta thấy tất cả thông tin cấu hình này,

một số chi tiết về việc bỏ mô hình,

số lượng kích thước nhúng, số lớp.

Đây là số khối máy biến áp, v.v.

Tất cả thông tin này được lưu trữ trong tập tin này ở đây.

Và chúng ta cũng có thể xem tập tin này.

Đây cũng là văn bản, chỉ cho chúng ta biết một chút thôi

của thông tin phiên bản.

Tệp này ở đây, model.safetensors,

cái này, bạn có thể thấy nó là 474 megabyte.

Đây không phải là một tập tin văn bản.

Điều này chứa tất cả các trọng số mô hình,

tất cả các con số thực tế bên trong mô hình.

Được rồi, vì vậy chúng tôi đã lưu nó.

Và bây giờ, vâng, điều này chỉ đang hiển thị

rằng phần nhúng mã thông báo Word có rất nhiều số.

Tất cả họ đều không phải là ai cả.

Vậy điều tôi sẽ làm là thay thế tất cả những con số này,

toàn bộ ma trận trọng số với một loạt các trọng số

và thể hiện điều đó như tôi đã đề cập,

đây hoàn toàn không phải là một cái gì đó

bạn sẽ muốn làm thực tế.

Toàn bộ vấn đề là những gì tôi sẽ làm

hiện đang lưu lại mô hình này với một tên khác.

Vì vậy, ở đây tôi có GPT gốc và bây giờ là GPT có GPT.

Và ý tưởng là bây giờ tôi sẽ xóa mẫu GPT-2 này.

Và bạn biết đấy, chúng ta có thể thử chạy cái này.

Chúng tôi vừa nhận được một thông báo lỗi.

Biến này không được xác định.

Tôi đã xóa nó khỏi không gian làm việc.

Tuy nhiên, nó vẫn được lưu trữ trên đĩa tạm thời mà chúng tôi có ở đây.

Được rồi, vậy việc tôi làm là tải hai mô hình này vào.

Vì vậy, từ khi được đào tạo trước, và bây giờ đây là tên tệp

hoặc tên thư mục cho mô hình gốc

và những mẫu đó, đó là những gì tôi gọi ở đây.

Và đây chỉ là để chứng minh

rằng chúng tôi đã thành công trong việc lưu các mô hình

và sau đó nhập lại hai mô hình.

Bây giờ hãy nói rằng bạn thực sự muốn có được điều này

trên máy tính của bạn, bởi vì vấn đề là,

ngay khi bạn ngắt kết nối, khi bạn khởi động lại phiên,

hoặc nếu bạn ngắt kết nối và xóa thời gian chạy,

những thư mục này sẽ biến mất và tất cả công sức của bạn

và sự sáng tạo của bạn và mọi thứ bạn làm đều không còn nữa.

Tất nhiên, bạn vẫn có mã,

nhưng bất cứ thứ gì bạn lưu trữ ở đây trong kho lưu trữ tệp cục bộ này

sẽ bị xóa khi bạn xóa phiên này.

Vậy vấn đề về những thư mục này trong Colab,

Theo tôi, điều này hơi khó chịu,

nhưng bạn có thể mở thư mục, bạn có thể tải lên,

bạn có thể làm tất cả những thứ này

Bạn không thể tải xuống toàn bộ thư mục này,

chỉ toàn bộ thư mục.

Vì vậy, bạn có thể vào, đây không phải là thư mục, đây là tập tin.

Vì vậy, bạn không thể tải xuống toàn bộ thư mục,

nhưng bạn có thể tải xuống các tệp riêng lẻ này.

Vì vậy, bạn có thể làm điều này ba lần,

và đối với ba tập tin, nó thực sự không quá tệ.

nhưng đó là lựa chọn một.

Tùy chọn thứ hai là bạn có thể nén toàn bộ thư mục này thành một tệp

và sau đó bạn có thể tải xuống tập tin đó.

Vì vậy, bạn có thể sử dụng thư viện Shutil này để tạo một kho lưu trữ

từ thư mục này nội dung gạch chéo là cơ sở ở đây.

Và sau đó là GPT gốc, chúng tôi muốn tạo một tệp zip,

kho lưu trữ thuộc loại zip.

Và đây là, xin lỗi, tôi đã nói ngược lại.

Đây là thư mục mà chúng ta muốn nén thành file zip.

Đây sẽ là tên của tệp zip.

Hơi khó hiểu, nếu bạn thực sự thêm tên .zip,

sau đó bạn sẽ nhận được một tệp .zip.zip.

Vì vậy, bạn loại trừ .zip.

Và nếu tên của tệp zip giống nhau

như tên của thư mục,

thì đó là lý do tại sao tôi lại bối rối ở đây.

Dù sao đi nữa, tôi sẽ không chạy nó.

Tôi sẽ chạy cái này.

Đây là sử dụng lệnh Unix hoặc tôi viết bang.

Vì vậy, một dấu chấm than khiến tôi thoát khỏi Python

và vào môi trường Unix bên dưới phiên Python

mà chúng ta đang giao tiếp thông qua sổ ghi chép này.

Vì vậy, zip và đây là tên của tệp zip.

Và đây là thư mục mà chúng ta muốn nén.

Dấu gạch ngang R là một tùy chọn cho đệ quy.

Bạn cần điều đó nếu bạn muốn đưa vào gói zip

tất cả các tập tin có trong thư mục này.

Vì vậy, chúng tôi đã có một số nén khiêm tốn.

Có vẻ như những tập tin này đã bị nén rất nhiều,

nhưng đây là các tệp JSON văn bản.

Vì vậy chúng rất dễ nén và chúng cũng rất nhỏ.

Vì vậy, nó thậm chí không thành vấn đề nếu chúng ta nén chúng.

Bản thân mô hình sẽ nén lại một chút,

nhưng đó là một tập hợp ma trận khá dày đặc.

Vì vậy, nó không thực sự nén nhiều như vậy.

Dù sao đi nữa, mục tiêu ở đây không phải là nén,

nhưng để cung cấp cho chúng tôi một tập tin mà chúng tôi thực sự có thể tải xuống.

Được rồi, vậy chúng ta có thể tải tập tin đó xuống.

Và bây giờ bạn thực sự đang tải xuống cái này

vào máy tính của bạn,

bất kỳ máy tính nào bạn đang làm việc ở đây.

Được rồi, giả sử bạn đào tạo một người mẫu,

bạn nén nó lại, bạn tải mô hình đó xuống,

và sau đó bạn muốn tải nó lên

vào một phiên Python khác.

Bạn có thể tải tập tin lên bằng nút này ở đây.

Điều này sẽ cho phép bạn tải lên các tập tin

từ máy tính cục bộ của bạn vào phiên Python này

mà chúng tôi đang làm việc ở đây.

Nhưng đây chỉ là một tệp zip

và chúng ta sẽ cần giải nén file zip đó.

Vì vậy, bạn cũng có thể làm điều đó bằng các lệnh Unix,

về cơ bản chỉ là giải nén.

Vì vậy, đây thực sự là lệnh duy nhất bạn cần, giải nén,

và sau đó là tên của tệp zip.

Những gì tôi đang làm ở đây là tạo một thư mục mới.

Vì vậy, mkdir là tạo một thư mục hoặc một thư mục mới,

xin lỗi, không phải là một tập tin.

Và sau đó tôi giải nén với đích đến

của thư mục mới này.

Và lý do duy nhất khiến tôi làm điều đó chỉ là để bạn thấy đấy

rằng nó thực sự đang mang đến cho chúng ta một phiên bản mới của điều này.

Vì vậy, nó thực sự được đặt ở một nơi khác

và không chỉ sao chép nó vào cùng một thứ.

Vì vậy, ở đây tôi có thư mục mới và bây giờ ở đây,

Tôi có HF gốc GPT.

Và đây chính xác là mẫu mà tôi đã nén từ đây

và có lẽ đã được tải xuống máy tính của tôi.

Và trong một phiên Python khác với một mô hình khác,

các nhiệm vụ khác nhau tôi tải lên mô hình mà tôi đã tinh chỉnh. Được rồi bây giờ mọi thứ tôi có

được mô tả hoạt động cho người mẫu được cung cấp bằng cách ôm mặt. Nếu bạn có mô hình của mình từ

ở một nơi nào khác như kiểu mẫu khuôn mặt không ôm sát hoặc nếu bạn đã tự tạo mẫu trong

PyTorch những phương pháp này sẽ không hoạt động. Vì vậy, từ việc được đào tạo trước sẽ không hiệu quả và

lưu được đào tạo trước sẽ không hoạt động. Thay vào đó, bạn có thể sử dụng phương pháp tích hợp sẵn của PyTorch. Vì vậy chúng tôi nhận được,

vì vậy bây giờ tôi sẽ lưu từ điển trạng thái, đó là trạng thái của tất cả các tham số trong

mô hình và tôi sẽ lưu trữ mô hình đó bằng hàm PyTorch.save, đây là

tên tệp tôi đang chọn và PT cho PyTorch.

Không có gì ngạc nhiên ở đó.

Được rồi, vậy là chúng ta sẽ tạo ra mô hình này ở đây.

Bây giờ đây không phải là một thư mục, đây là một tập tin.

Điều đó có nghĩa là chúng ta cũng có thể tải xuống tệp này,

tệp PT này từ phiên Python trong Colab

trên máy chủ xuống ổ cứng cục bộ của chúng tôi

từ máy tính mà bạn đang thực sự làm việc.

Và sau khi bạn làm điều đó, bạn có thể tải lại.

Vì vậy, torch.load, sau đó tôi nhúng nó vào trong LoadStateDict,

và nó sẽ tải mô hình đó

và thay thế tất cả các tham số trong mô hình này

với cái ở đây.

Vì vậy hãy nhớ, hình mẫu của một người, đó là hình mẫu

có ma trận nhúng mã thông báo Word

được viết lại hoàn toàn bởi một loạt người.

Nhưng bây giờ nó không còn là những cái đó nữa.

Và tại sao nó không còn là những cái đó nữa?

Bởi vì ở đây tôi đã lưu trữ mô hình gốc,

và sau đó ở đây tôi đã tải lại mô hình ban đầu

và ghi đè lên từ điển quốc gia,

vì vậy tất cả các tham số trong mô hình

với tất cả các tham số trong mô hình này.

Và đó là lý do tại sao đây không còn là những cái nữa.

Thành thật mà nói, tôi ước gì có một cách dễ dàng và phổ biến hơn để cứu các mô hình khỏi

bất kỳ thư viện nào, nhưng một khi bạn đã quen với nó thì nó không đến nỗi tệ.