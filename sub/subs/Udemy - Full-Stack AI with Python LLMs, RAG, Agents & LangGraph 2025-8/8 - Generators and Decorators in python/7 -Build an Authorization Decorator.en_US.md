# 7 -Xây dựng Trình trang trí ủy quyền.en US

---

Được rồi, thêm một loại nữa

trang trí mà chúng tôi sẽ xây dựng.

Và trên thực tế, chúng tôi thực sự

xây dựng nó bằng tay.

Nhưng bạn sẽ thấy chúng trong

các khung và thư viện lớn,

đặc biệt là ở Django, nó

được sử dụng ở mọi nơi.

Vì vậy chúng ta sẽ xây dựng

một người trang trí đơn giản.

Chúng ta sắp phải đối mặt với một sai lầm,

và bất ngờ nó sẽ đến

và sau đó chúng ta sẽ đi

để tìm hiểu cách khắc phục chúng.

Và đây là những điều bạn học được

chỉ trong sản xuất.

Vậy hãy để tôi tiếp tục và chia sẻ

màn hình với bạn.

Vì vậy tôi đã tạo một cách đơn giản

tập tin mới là trang trí xác thực.

Một lần nữa, đó thực sự là một

kiểu trang trí đơn giản.

Bạn sẽ thấy điều này rất nhiều.

Bước đầu tiên luôn giống nhau, vì vậy

chúng ta sẽ mượn một số mật mã.

Vì vậy, chúng tôi sẽ sao chép cái này và dán nó.

Bất cứ khi nào chúng tôi đang xác định bất kỳ

trang trí, đây là thứ nhất

điều phổ biến mà bạn phải làm.

Hãy cứ nói rằng chúng tôi muốn

để xác định một trang trí đơn giản

trong đó nói yêu cầu quản trị viên.

Vì vậy, chúng tôi đang tạo một hàm bao bọc

rằng nếu bất kỳ chức năng nào được thực thi,

và tôi gói nó lại mà không có

một chức năng, nghĩa là chỉ có quản trị viên

thực sự có thể thực hiện chức năng đó.

Chức năng khá hữu ích

thành thật mà nói.

Và tôi tiếp tục và đơn giản chấp nhận

hoạt động giống như thế này

Và chúng tôi biết điều này ở mức độ

bọc lại để bảo quản tất cả

của siêu dữ liệu giống như thế này.

Và sau đó tôi có thể nói,

giả sử chúng ta định nghĩa một trình bao bọc,

lần này sẽ đảm nhận vai trò của người dùng.

Bây giờ trình bao bọc không phải lúc nào cũng

cần phải lấy tất cả

những lý lẽ chỉ như thế này.

Nếu bạn biết rằng chúng tôi mong đợi

chỉ có một lý lẽ

đã qua rồi, cứ lấy cái đó đi.

Nếu bạn nghĩ thêm về điều đó

sẽ xuất hiện.

Không có hại gì khi nói tranh luận

và từ khóa args, tất cả chúng.

Vì vậy, tất cả chúng đều tự động chuyển tiếp.

Nhưng nó không thực sự chính xác

và tôi thích mã chính xác.

Được rồi, vậy chúng ta đi thôi

phía trước và kiểm tra xem người dùng

vai trò không bằng quản trị viên.

Chúng tôi chỉ đơn giản là tiếp tục và nói

giống như thế này, một bản in đơn giản

tin nhắn nói rằng,

một cái gì đó như thế này, quyền truy cập bị từ chối.

Và chúng tôi sẽ chỉ nói quản trị viên.

Vì vậy, đây là khu vực chỉ dành cho quản trị viên.

Và sau đó chúng tôi

đưa ra một phần khác.

Và trong trường hợp khác chúng ta chỉ cần đi

về phía trước và nói trả lại bất cứ điều gì

chức năng bạn đang cố gắng chạy với

vai trò người dùng, chúng tôi sẽ quay lại

cứ như vậy để nó có thể tiếp tục

thực hiện.

Và chúng ta cũng sẽ tiếp tục

và nói trả lại giấy gói.

Khá đơn giản.

Chúng tôi đã thấy điều này nhiều

nhiều lúc, không có vấn đề gì cả.

Bây giờ chúng ta sẽ thấy rằng điều này

là cách chúng tôi sử dụng Decorator.

Và một khi người trang trí này ở đây,

chúng ta chỉ cần tiếp tục và nói rằng tôi muốn

để tạo ra một phương pháp khác

trong đó có nội dung truy cập kho trà.

Và đây là một điều phổ biến mà

bạn muốn truy cập vào kho.

Ai đó sẽ giao cho tôi một vai diễn

bạn có vai trò gì để bạn

có thể truy cập vào kho và in

một tuyên bố đơn giản cho biết quyền truy cập

cấp cho tồn kho chè.

Thế đấy.

Bây giờ chúng ta hãy tiếp tục và chạy cái này.

Tôi muốn chạy nó hai lần.

Truy cập vào hàng tồn kho.

Ối.

Ồ, tại sao tôi lại làm thế.

Truy cập vào hàng tồn kho.

Và trước hết chúng ta sẽ vượt qua

trên một người dùng và sau đó chúng ta sẽ bắt đầu

phía trước và vượt qua quản trị viên.

Vậy bạn nghĩ điều gì sẽ xảy ra

với đoạn mã này?

Khá dễ đoán,

nhưng việc hành quyết

thực sự sẽ gây sốc cho bạn một chút.

Vì vậy, nếu vai trò người dùng là người dùng thì

chúng ta chỉ đơn giản là đi tiếp và quay trở lại

Đây không phải là quản trị viên, vì vậy chúng tôi sẽ

cứ tiếp tục và in cái này ra.

Này, đây là quản trị viên, không được phép.

Nếu là quản trị viên thì chúng ta chỉ cần

hãy tiếp tục và thực hiện điều này.

Vì vậy, điều này sẽ thực hiện như nó vốn có.

Chúng tôi không ngăn cản bất cứ điều gì.

Nhưng trước sự ngạc nhiên của bạn, nếu tôi chạy

toàn bộ đoạn mã này

và tại sao nó lại hành xử như vậy?

Và tôi phải nói là thoát ra.

Thế đấy.

Không biết chuyện gì đã xảy ra.

Tôi sẽ chỉ nói Python03.

Thực ra tôi đang vào nhầm thư mục

bằng cách nào đó mở một thiết bị đầu cuối tích hợp.

Lần này tôi đang ở đúng nơi.

Hãy chạy cái này.

Và cái này là 03 và chúng ta bắt đầu.

Chỉ quản trị viên và trà

hàng tồn kho được cấp.

Vì vậy trước hết nó

thực sự đã ngăn cản tôi.

Được rồi, tốt quá.

Và quyền truy cập được cấp.

Tôi đã mong đợi rằng sẽ có

là một lỗi, nhưng nó đã không đến.

Nó có thể đến ở một số nơi.

Vì vậy, không sao cả

đã đến, nhưng tôi đã mong đợi, sẽ

Thành thật mà nói, tôi đã mong đợi một lỗi

trong cái này, nhưng không sao cả.

Tôi sẽ cho bạn biết lý do tại sao.

Nó đôi khi xảy ra.

Bây giờ đôi khi khi bạn thực sự

chạy những thứ này, bạn thực sự có

để trả lại một cách rõ ràng một cái gì đó.

Trong tất cả các trường hợp.

Trong trường hợp này chúng ta không

trả lại bất cứ điều gì.

Không sao đâu.

Không biết ở phiên bản gần đây có không

của Python họ đã thay đổi nó.

Trong hầu hết các trường hợp.

Trong mọi trường hợp, nếu bạn

có câu lệnh switch, bạn có

phải trả lại một cái gì đó

Một sự trở lại rõ ràng là

được yêu cầu trong Python.

Vì vậy, để đảm bảo an toàn bạn có thể

cứ tiếp tục và nói quay lại

và bạn có thể chỉ cần trả lại không,

đó cũng là một khoản hoàn trả mặc định.

Điều này sẽ làm cho chương trình của bạn trở nên hoàn hảo

và trong hầu hết các trường hợp bạn

sẽ thấy cái này, chúng tôi không hiểu

có lẽ con trăn của tôi được cập nhật nhiều nhất 1

Tôi đã mong đợi một lỗi xảy ra

trung thực nhưng đôi khi python cập nhật

vì vậy cái này vẫn sẽ chạy cái này và bạn

phải học điều gì đó mới đây

một lần nữa tôi sẽ nói điều này rất

dòng tùy chọn bạn sẽ thấy chúng trong

một số cơ sở mã cũ hơn bây giờ tôi

có thể nói vậy nhưng hãy luôn ghi nhớ

viết điều này một cách rõ ràng là không bao giờ

sẽ làm tổn thương bạn đặc biệt nếu bạn

đây là những người trang trí tòa nhà

một cái gì đó mà chúng tôi luôn sử dụng để lấy

quan tâm có lẽ tôi sẽ không quan tâm

chúng trong tương lai nếu nó hoạt động tốt

như thế nhưng tôi vẫn sẽ học thêm

về điều này và đó là cách chúng tôi làm việc

luôn luôn nghiên cứu tất cả chúng ta

liên tục tìm hiểu về những điều

điều đó xảy ra trong ngôn ngữ nếu tôi

tình cờ phát hiện ra điều gì đó mới mẻ và

thú vị tôi chỉ chia sẻ điều đó trên

YouTube cũng như trên

các khóa học udemy dành cho việc này

video.

Chúng ta hãy bắt kịp phần tiếp theo.