# 5 -RAG Pipeline – Cơ chế truy xuất ở Depth.en US

---

Được rồi, hãy xem thế nào

việc thu hồi xảy ra.

Được rồi, vậy tôi đi đây

để nói, chúng ta hãy nói bây giờ chúng ta

đang trong giai đoạn truy xuất.

Bây giờ đang trong quá trình truy xuất

giai đoạn, điều gì xảy ra?

Nó bắt đầu, nó bắt đầu

khi người dùng cố gắng trò chuyện.

Được rồi, vậy đầu vào là gì

cho giai đoạn truy xuất?

Người dùng về cơ bản cung cấp

bạn một truy vấn, một tin nhắn.

Được rồi, về cơ bản người dùng sẽ đưa ra một truy vấn

cái đó, này, bạn có thể kể cho tôi nghe về

cái này hay cái kia hay cái gì đó như thế này?

Bây giờ hãy xem bạn làm gì về mặt kỹ thuật, người dùng

đang cố gắng hỏi về điều gì đó.

Được rồi, chúng tôi không biết gì

bạn đang cố hỏi.

Vậy điều tôi sắp làm là

tôi có thể chuyển đổi truy vấn người dùng này không

vào việc nhúng vector?

Vâng, tôi có thể, phải không?

Tôi có thể.

Vì vậy, bất kể người dùng nào đang cố gắng hỏi,

bất kể anh ấy có ý gì trong thế giới thực, tôi

cũng sẽ chuyển đổi cái này thành vector

nhúng bằng cách sử dụng cùng một mô hình này.

Vậy hãy để tôi sao chép mô hình

và tôi sẽ giữ nó ở đây.

Vậy bây giờ những gì bạn đã làm

đang sử dụng truy vấn của người dùng.

Được rồi, để tôi mang nó xuống.

Sử dụng truy vấn của người dùng, bạn có

đã chuyển đổi nó thành nhúng vector.

Và bây giờ tại thời điểm đặc biệt này

bạn có nhúng vector

về những gì người dùng đang cố gắng hỏi bạn.

Hãy để tôi chỉ nói truy vấn.

Được rồi, giờ xem nào, chúng ta hãy nói điều này

tài liệu có tiêu đề hoặc ở đâu đó.

Nó được viết như thế này, bạn

biết, trường hợp số 32.

Người dùng cũng đang cố gắng hỏi

về trường hợp số 32.

Vì vậy, những nhúng vector này

chứa dữ liệu mà vectơ

về trường hợp số 32.

Bây giờ, trong cùng một cơ sở dữ liệu

ngay tại đây nơi bạn có

được lưu trữ, bạn sẽ thực hiện một truy vấn.

Những gì bạn định làm, bạn là

sẽ thực hiện một truy vấn được gọi là

tìm kiếm tương tự vector.

Được rồi, bạn sẽ làm

một tìm kiếm tương tự vector,

tìm kiếm tương tự vector này.

Bạn đang định nói điều đó, này,

người dùng đang cố gắng hỏi điều này.

Có thể, bạn có thể vui lòng tìm kiếm

cho các vectơ này và đưa ra

tôi các tài liệu liên quan?

Hãy cho tôi những phần có liên quan?

Tôi sẽ nói.

Vì vậy, về cơ bản chúng ta hãy nói bất kỳ người dùng nào

đã thử hỏi vectơ C

ngay tại đây, tôi sẽ chọn

và vectơ A rất phù hợp.

Được rồi, đây là hai cái

những phần được trả lại, được chứ?

Đây là hai khối

đã được cây thông trả lại

hình nón, vectơ db này.

Được rồi, vậy bây giờ chuyện gì đã xảy ra?

Bạn có những phần có liên quan.

Vì vậy trong điều đặc biệt này

giai đoạn, chuyện gì đã xảy ra?

Về cơ bản bạn chỉ có

và chỉ những phần có liên quan.

Bạn chưa có.

Bạn không nhận được tất cả các khối.

Hãy xem, trong thực tế bạn sẽ có như thế,

bạn biết đấy, có thể có 50.000 khối ở đây.

Nhưng tôi không quan tâm

trong tất cả 50.000 khối.

Tôi chỉ quan tâm đến những gì có liên quan

những khối chỉ có hai.

Bây giờ những cái này làm gì

hai khối chứa?

Thứ nhất, nó chứa các vectơ.

Bây giờ tôi thực sự không quan tâm

trong các vectơ.

Vì vậy chúng ta có thể bỏ đi các vectơ.

Tôi đã nhận được nội dung thực tế.

Điều này giống như đoạn văn.

Tôi đã nhận được số trang và tài liệu.

Bây giờ điều tôi có thể làm là

Tôi thực sự có thể sử dụng một mô hình biểu đồ.

Giả sử chúng ta có thể sử dụng GPT, năm.

Được rồi, giống như GPT 5.

Những gì chúng tôi có thể làm, về cơ bản chúng tôi có thể cho đi

đây là dữ liệu.

Bạn biết đấy, bạn nhớ điều đó

lời nhắc hệ thống nơi chúng tôi

đã truyền tất cả dữ liệu?

Bây giờ chúng ta sẽ không vượt qua

tất cả dữ liệu đang diễn ra

để truyền dữ liệu liên quan.

Vì vậy, bây giờ lời nhắc hệ thống của tôi là

thực tế đã bị thu hẹp lại.

Điều này chỉ chứa dữ liệu có sẵn.

Nhiều thế này, chỉ có hai khối thôi.

Được rồi, và người dùng ban đầu là gì

đã hỏi, tôi sẽ chuyển nó

để trò chuyện về GPT hoặc mô hình LLM của tôi.

Vì vậy tôi sẽ nói rằng này,

đây là dữ liệu liên quan

Đây là bối cảnh có liên quan

về dữ liệu có sẵn.

Tôi chỉ định nói đây là

số trang, tài liệu, bất cứ thứ gì

bạn biết đấy, là nội dung

về trong đoạn đó.

Ngoài ra đây là những gì người dùng đang yêu cầu

rằng bây giờ nó có thể trả lời lại

người dùng này, đây là dữ liệu

về bạn, giả sử, bạn biết đấy,

trường hợp của bạn số 32 + đây là

số trang nơi bạn có thể tìm thấy

dữ liệu này.

Đây là giẻ lau của bạn.

Đây là đường dẫn RAG của bạn.

Vì vậy, đây là giai đoạn phục hồi của bạn.

Vì vậy, đây là cách bạn thực hiện truy xuất

và đây là cách bạn có thể

thực sự tạo ra một AI có thể

biểu đồ trên các tài liệu lớn.

Hiểu rồi.

Vì vậy giai đoạn lập chỉ mục

và một giai đoạn thu hồi.

Vì vậy, đây là cách toàn bộ

Đường ống Rack hoạt động.

Vì vậy nếu tôi đi đến đây và đi

vào hình ảnh, bạn có thể thấy đây là

toàn bộ câu chuyện ngắn gọn.

Vậy hãy để tôi mở

một bức ảnh ngẫu nhiên từ đây.

Mở hình ảnh trong tab mới.

Vì vậy, những gì bạn có thể thấy ở đây là.

Hãy để tôi, chúng ta hãy chờ đợi

để nó tải.

Ồ, đây là một hình ảnh rất nhỏ.

Hãy để tôi nhấp chuột vào nó.

Có lẽ tôi có thể phóng to điều này

hình ảnh hoặc có thể, có thể chúng ta

cũng có thể chụp một số hình ảnh khác.

Bởi vì đường ống Rack

luôn giống nhau phải không?

Vâng.

Vì vậy tôi có thể mở phiên bản beta ở đây để bạn

có thể thấy điều gì đang xảy ra.

Chuẩn bị dữ liệu, bạn đã có được bản thô

nguồn dữ liệu và nó có thể là bất cứ thứ gì.

Thấy chưa, nó có thể là cơ sở dữ liệu, nó có thể

là PDF, nó có thể là tài liệu.

Bạn thực hiện việc trích xuất thông tin

ở bước B bạn thực hiện chunking.

Bạn gọi một mô hình nhúng và lưu trữ

dữ liệu vào cơ sở dữ liệu vector.

Phải.

Vì vậy, A, B, C, D của bạn là chỉ mục.

Bây giờ trong quá trình truy xuất được tăng cường

thế hệ, đó là truy vấn của bạn

người dùng giai đoạn cung cấp cho bạn một truy vấn,

bạn chuyển đổi các phần nhúng, bạn tìm kiếm.

Bạn thực hiện tìm kiếm tương tự

trong việc nhúng vector.

Bạn chỉ có dữ liệu liên quan.

Bạn vượt qua điều này có liên quan

dữ liệu tới LLM.

Ngoài ra, bạn cũng chuyển truy vấn tới

LLM và bạn nhận được phản hồi.

Đây là cách bạn tạo ra một miếng giẻ

đường dẫn biểu đồ

trên các nguồn dữ liệu lớn.

Được rồi, trong video tiếp theo,

chúng tôi thực sự sẽ

mã hóa một đường dẫn giẻ rách đơn giản.

Vậy đó là tất cả về

video đặc biệt này.

Hẹn gặp lại bạn ở phần tiếp theo.