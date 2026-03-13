# 020 Lưu dữ liệu vào ổ cứng vi

---

Trong phần trước, chúng tôi đã hoàn thành chức năng hai chuỗi này, bây giờ có thể lấy một bộ bài và sau

biến đó thành một chuỗi duy nhất.

Vì vậy, hiện tại chúng tôi đã sẵn sàng để thực hiện việc sử dụng các chức năng phù hợp này được bao gồm trong I. Ô. U. thư viện

công cụ hoặc gói IOU.

Vì vậy, hay thực hiện ngay bây giờ.

Vâng, trước tiên hãy bắt đầu bằng cách xác định hàm lưu vào tệp của chúng ta và sau đó chúng ta sẽ điền vào một

các đối số khác nhau mà chúng ta cần chuyển vào tệp bên phải.

Vì vậy, tôi sẽ lại chỉnh sửa mã của mình và chúng tôi sẽ tạo một chức năng mới có tên

là Save to File.

Bây giờ, như thường lệ, chúng ta cần suy nghĩ một chút về chữ ký hàm ở đây hoặc tất cả các phần nhỏ

Các câu hỏi khác nhau mà chúng ta cần phải gắn vào.

Vì vậy, trước tiên, tôi nghĩ rằng việc lưu trữ vào tệp chắc chắn sẽ muốn có một bộ thu loại bộ bài vào một lúc nào đó

chúng tôi có thể làm điều đó như thẻ gọi điện thoại chấm lưu vào tệp tin.

Vì vậy, tôi sẽ bổ sung vào một bộ thu loại boong sau đó để có chức năng lưu vào tệp chính nó, không có yêu cầu bất kỳ đối lập nào

số nào không?

Chà, bạn sẽ nhớ lại rằng các chức năng phù hợp, quyền lợi chức năng mà chúng ta phù hợp

chúng tôi yêu cầu xem xét chúng tôi chuyển vào chuỗi tệp tên.

Và vì vậy tôi nghĩ rằng điều hợp lý là chúng ta nên cho phép ai đang sử dụng

Gói này mà chúng tôi đang tập hợp lại với nhau để chuyển tên tệp và sau đó chúng tôi sẽ chuyển điều đó vào hàm đúng

tệp này cuối cùng chúng tôi gọi nó.

Vì vậy, đối với danh sách đối số của chúng ta ngay tại đây, tôi sẽ mong đợi một chuỗi loại tệp tên đối số.

Bây giờ, điều cuối cùng ở đây mà tôi muốn hỏi bạn.

Chúng tôi có sự thực tế cần thiết bất kỳ giá trị trả về nào từ đây không?

Như vậy, có điều gì mà chúng ta có thể muốn trả lại từ công việc này không?

Chà, có lẽ không có giá trị nào mà bạn và tôi nhất thiết phải trả lại.

Nhưng nếu bạn cô gái lại tài liệu phù hợp tài liệu, bạn sẽ nhận thấy rằng nó thông báo rằng nếu

xảy ra lỗi, nó sẽ được trả về từ tính năng phù hợp.

Vì vậy, tôi nghĩ rằng thay vì chúng tôi cố gắng tìm kiếm điều gì đang xảy ra với một số loại lỗi được tạo ra bằng cách

ghi bất kỳ nội dung nào vào tệp, chúng tôi chỉ nên trả lại lỗi này có thể được tạo ra khi chúng tôi cố gắng vượt qua

ghi thứ gì đó vào ổ cứng.

Nhân tiện, chúng tôi sẽ nói nhiều hơn về các lỗi ở phần sau của khóa học.

Nhưng ngay bây giờ, chúng tôi đã xử lý lỗi này và loại bỏ nó trở lại.

Vì vậy, chúng tôi sẽ nói rằng chúng tôi có chức năng lưu trữ vào tệp sẽ giải quyết một số lỗi thuộc về loại nào đó.

Vì vậy, đây là một loại thực tế ngay tại đây.

Và như bạn có thể tưởng tượng, nó đại diện cho một số loại lỗi hoặc thông báo lỗi hoặc điều gì đã xảy ra

ra with code của chúng tôi.

Vì vậy, ngay bây giờ bên trong hàm này, chúng ta có thể bắt đầu viết lệnh gọi hàm thực thi của chúng ta để lưu tinh ranh giới

this vào ổ cứng.

Vì vậy, chúng tôi sẽ tham khảo việc sử dụng gói io, cụ thể là chức năng phù hợp.

Đối số đầu tiên sẽ là tên tệp.

Vì vậy, hãy nhớ rằng, đó là một số ở đây.

Và sau đó, đối số thứ hai phải là byte dữ liệu mà chúng tôi đang cố gắng ghi hoặc lưu

vào ổ cứng.

Vì vậy, chúng tôi có khả năng biến bộ bài của mình thành một chuỗi, nhưng sau đó chúng tôi cần biến nó thành một byte byte.

Vì vậy, trước tiên hãy bắt đầu bằng cách chuyển nó thành một chuỗi, chúng tôi sẽ nói dấu chấm thành chuỗi.

Vì vậy, chúng tôi có chuỗi.

Và sau đó để biến chuỗi thành một lát byte, chúng tôi có thể thực hiện chuyển đổi cùng loại mà chúng tôi đã tìm thấy

một giây trước.

Vì vậy, chúng tôi sẽ nói rằng chúng tôi muốn có một lát byte kiểu gì đó.

Vì vậy, chúng tôi sẽ viết các kiểu và sau đó trong một tập hợp các dấu đơn, chúng tôi sẽ chuyển giá trị mà chúng tôi có.

Đó là do string hoặc về chất là một chuỗi.

Bây giờ, chúng tôi có rất nhiều dấu ngoặc đơn ở đây, vì vậy hãy chắc chắn rằng bạn đang có các dấu ngoặc đơn

Cân đối.

Chúng tôi có một tập hợp các dấu ngoặc đơn hoặc một tập hợp các dấu ngoặc đơn cho hai chuỗi.

Chúng tôi có một cái khác cho kiểu chuyển đổi và sau đó là cái cuối cùng cho lệnh gọi chức năng phù hợp.

Bây giờ, hãy ghi tệp lấy một đối số cuối cùng ở đây.

Hãy nhớ rằng, đối số cuối cùng là điều khoản được phép.

Quyền này được sử dụng trong trường hợp tệp này chưa tồn tại.

Bên cạnh hàm tệp phải thiết lập một số mặc định quyền trên tệp tin, về cơ bản là ai có

quyền truy cập vào tệp?

Ai có thể đọc nó, ai có thể viết nó?

Vì vậy, chúng tôi sẽ chỉ sử dụng một số quyền rất mặc định của 0666.

Về cơ bản, điều đó có nghĩa là bất kỳ ai cũng có thể đọc và ghi tệp này.

Bây giờ, điều cuối cùng chúng ta phải nhớ rằng chúng ta đã nói rằng hàm của chúng ta sẽ trả về một lỗi nếu

một lỗi xảy ra bất cứ khi nào chúng tôi cố gắng ghi điều này ra một tệp.

Vì vậy, hàm tệp phải tự động trả về một lỗi và đó là những gì chúng tôi thực sự muốn trả lại.

Vì vậy, chúng tôi sẽ hoàn trả toàn bộ kết quả của lệnh như vậy.

Và tôi sẽ thu nhỏ chỉ 1/2 để bạn có thể nhìn thấy toàn bộ đường nét.

Vì vậy, bây giờ khi tôi lưu trữ điều này, hãy nhớ rằng chúng tôi chưa nhập IOU gói.

Vì vậy, tôi chỉ cần lưu nó trong một VTS mã hóa.

Nếu bạn đang sử dụng VTS code và VTS code cho thấy rằng bạn đang cố gắng sử dụng một gói mà bạn

chưa được nhập.

Mã sẽ tự động thêm vào lệnh nhập cho bạn.

Và đây là lệnh nhập để đưa IOU vào thư viện hoặc IOU gói.

Chú ý trong trường hợp này nó nói IO sẽ cắt IOU cho đến khi nào.

Vì vậy, gói công cụ IOU là một gói phụ trong IO.

Và chúng tôi thực sự thấy điều đó khi xem tài liệu.

Vì vậy, nếu chúng tôi quay lại tài liệu và sau đó xem lại nơi chúng tôi đã tìm thấy công cụ IOU, bạn sẽ nhận thấy rằng

IOU Till là loại được lồng trong IO ngay tại đây.

Và vì vậy chúng tôi gọi đây là một gói phụ.

Và vì vậy, ngay cả bên trong IOU, cho đến khi nó nói rất rõ ràng, oh yeah, để nhập use this, enter IO, gạch lát

chéo IOU cho đến.

Được chứ.

Vì vậy, hãy quay lại bên trong trình soạn thảo mã của chúng tôi, tôi nghĩ rằng tất cả chúng đều đã có sẵn để cuối cùng kiểm tra điều này.

Vì vậy, tôi sẽ lại hồ sơ đi chính của chúng ta.

Chúng tôi hiện đang tạo một bộ bài mới.

Chúng ta không cần thiết phải ra danh sách các thẻ dưới dạng một chuỗi nữa.

Hãy cố gắng lưu danh sách các thẻ này ngay tại đây hoặc loại bộ bài này vào ổ cứng của chúng tôi.

Vì vậy, giả sử thẻ dấu chấm lưu vào tệp và tôi cần chuyển vào một chuỗi cho tệp tên để sử dụng.

Vì vậy, tôi sẽ chuyển sang một chuỗi thứ tương tự như các thẻ của tôi.

Được chứ.

Vì vậy, chúng tôi sẽ lưu điều này.

Tôi sẽ thay đổi lại thiết bị đầu cuối của chúng tôi và tôi sẽ chạy.

Đi đi, Chính.

Đi đi.

Khi tôi làm như vậy, có vẻ như mọi thứ đã chạy đều thành công.

Bây giờ, nếu tôi thay đổi lại trình soạn thảo của mình, bạn sẽ tìm thấy một tệp mới trong thư mục làm việc hiện tại

của chúng tôi.

Và đây là tệp được ghi bằng lệnh gọi hàm lưu vào tệp afile.

Nếu chúng tôi mở nó lên, bạn sẽ thấy nó mở ra dưới dạng một văn bản tinh túy.

Về cơ bản, nó hiển thị danh sách các thẻ mà chúng tôi vừa lưu vào ổ cứng.

Vì vậy, có vẻ như điều này chắc chắn đã hoạt động thành công.

Chúng ta hãy giải lao nhanh chóng và sau đó tiếp tục trong phần tiếp theo và bắt đầu công việc với các chức năng tiếp theo của chúng ta.

Vì vậy, tôi sẽ gặp bạn chỉ sau một phút.