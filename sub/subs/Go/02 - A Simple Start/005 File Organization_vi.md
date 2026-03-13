# 005 Tổ chức tập tin vi

---

Được chứ.

Chỉ còn hai câu hỏi nhanh nữa.

Và chúng tôi sẽ giải quyết cả hai điều này trong một phần này.

Vì vậy, điều đầu tiên tôi muốn nói đến là chức năng thứ hai trong tệp chính của chúng tôi.

Cụ thể là Funk Main ngay tại đây.

Vâng, như bạn có thể tưởng tượng, funk là cách viết tắt của các hàm bên trong hàm go, giống như

các chức năng khác trong trình lập ngôn ngữ.

Vì vậy, nếu bạn đã quen thuộc với các hàm trong Ruby Python JavaScript, rất giống về chức năng, chúng tôi khai báo một

function bằng cách đặt func từ khóa, sau đó là tên của hàm và sau đó là danh sách

đối số.

Nếu tôi đặt nó ở dạng sơ đồ, nó có thể trông giống như vậy, hãy xem liệu tôi có thể tìm thấy nó ngay tại

đây.

Chúng ta bắt đầu.

Vì vậy, trước tiên, chúng tôi tuyên bố rằng chúng tôi sẽ tạo ra một hàm mới với chức năng từ khóa.

Sau đó, chúng tôi đặt tên cho hàm, một tập hợp các dấu ngoặc đơn mà chúng tôi sẽ chỉ định danh sách các đối số

mà chúng tôi muốn truyền tải chức năng này.

Sau đó, họ đặt các dấu ngoặc nền và bên trong các dấu ngoặc đó là phần thân của chúng ta.

Bây giờ đây là lần đầu tiên chúng ta nếm thử một số cú pháp xung quanh.

Hãy đi và tin tưởng tôi.

Chúng tôi sẽ có rất nhiều thời gian và thực hiện nhiều thao tác với một số cú pháp cơ bản cho những thứ như

chức năng và những gì không.

Vì vậy, tôi nghĩ rằng bây giờ có lẽ là đủ để giải quyết và nói rằng, Vâng, chúng tôi

chỉ tuyên bố một hàm.

Bây giờ điều cuối cùng tôi muốn nói đến hoặc câu hỏi lớn nhất mà chúng tôi có là cách tổ chức

file go chính.

Vì vậy, hiện tại chúng tôi đã hiểu rõ hơn về gói là gì, lệnh nhập là gì và chức năng ở đó

Dưới cùng, làm cách nào để chúng tôi sắp xếp lại tất cả các khía cạnh khác nhau trong một

tệp duy nhất?

Chà, trong thực tế, nó luôn có cùng một mẫu.

Chúng tôi đã tìm thấy sơ đồ của tôi ở đây thực sự nhanh chóng.

Chúng ta bắt đầu.

Vì vậy, nó sẽ luôn là một mẫu bên trong mọi đơn lẻ tệp mà chúng tôi từng tạo ở đó

trên cùng.

Chúng tôi sẽ thông báo gói hàng của mình.

Vì vậy, hãy nhớ chúng tôi nói, Ồ, tệp này là một phần của gói, blah, blah, blah.

Trong trường hợp này, gói chính.

Sau đó, ngay bên dưới, chúng tôi sẽ liệt kê tất cả các gói khác mà chúng tôi có thể cần nhập

vào tệp này.

Vì vậy, hãy nhập lệnh cho FMT và sau đó có thể chọn IO hoặc O hoặc bất kỳ gói nào khác mà chúng tôi muốn có quyền truy cập từ thư viện danh sách

Tiêu chuẩn của các gói mà chúng tôi nhớ là chúng tôi vừa xem 2 giây trước hoặc chúng tôi cũng có

có thể chỉ định câu lệnh cho các gói tùy chỉnh thích hợp như các gói có thể sử dụng lại mà bạn và tôi

đã tự động tạo ra.

Sau gói lệnh và nhập vào, chúng tôi sẽ đi xuống phần nội dung của tệp, đây là nơi chúng tôi bổ sung

vào một chuỗi logic thực hiện một điều gì đó.

Vì vậy, nó sẽ là một tập hợp các hàm khác nhau, khai báo các biến và tất cả các hàm đó

thứ tốt khác.

Vì vậy, nói chung, chúng ta sẽ làm quen với các mẫu mã giống nhau này trong mọi tệp cuối cùng mà chúng ta tập hợp

lại với nhau.

Vì vậy, tôi nghĩ rằng điều đó sẽ kết thúc một năm câu hỏi lớn về hồ sơ chính của chúng tôi.

Vì vậy, chúng tôi đã nói về mô hình, chúng tôi đã nói về các gói, nhập, chúng tôi đã đề xuất truy cập các chức năng

năng lực một chút và chúng tôi có ý tưởng tốt hơn về những gì gói FMT này đang làm cụ thể.

Vì vậy, tôi nghĩ rằng điều đó đã kết thúc nó cho một cái nhìn tổng quan rất cơ bản về chương trình rất, rất cơ bản này.

Hy vọng rằng bây giờ bạn đồng ý với tôi rằng mặc dù nó là một chương trình Hello World mệt mỏi, chúng tôi vẫn thu

được một số tiền khá tốt từ nó.

Tuy nhiên, đây là một chương trình rất đơn giản, dễ hiểu.

Vì vậy, chúng tôi hãy tiếp tục phần tiếp theo, nơi chúng tôi sẽ bắt đầu nói về một dự án phức tạp hơn

nhiều người chúng ta sẽ bắt đầu công việc.

Vì vậy, hãy bình tĩnh nhanh chóng và chúng tôi sẽ đi sâu vào dự án tiếp theo trong phần tiếp theo.