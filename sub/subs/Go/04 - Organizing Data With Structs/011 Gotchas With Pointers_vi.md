# 011 Vấn Đề Với Con Trỏ vi

---

Tại thời điểm này, chúng tôi đã có một ý tưởng khá tốt về cách con trỏ hoạt động và hoạt động.

Hãy nhớ rằng, go là một ngôn ngữ ngang bằng giá trị.

Vì vậy, bất kể khi nào chúng tôi truyền một giá trị cho một hàm, bằng cách nhận hoặc là một đối số, thì dữ liệu đó sẽ được sao chép

vào bộ nhớ.

Và vì vậy, theo mặc định, hàm sẽ luôn hoạt động trên một dữ liệu cấu trúc bản sao của chúng ta.

Chúng tôi có thể giải quyết vấn đề này và sửa đổi cấu trúc cơ sở dữ liệu thực tế thông qua việc sử dụng con trỏ

và bộ nhớ địa chỉ.

Bây giờ chúng ta sẽ bắt đầu nói về một chút gotcha xung quanh các mẹo để tìm ra gotcha chính xác này là

bất cứ điều gì và nó hoạt động như thế nào.

Chúng tôi sẽ cùng nhau thực hiện một dự án nhỏ khác trong một sân chơi cờ vây.

Vì vậy, tôi sẽ tự mình duyệt lại trình duyệt của mình và tôi sẽ điều chỉnh để chơi dot golang dot org.

Bây giờ khi ở đây, chúng tôi sẽ chỉ thêm một chút mã ở đây.

Và hãy tin tôi, nó chỉ có một vài dòng.

Và trong một số dòng đó, chúng tôi sẽ hiểu rõ hơn về món đồ lớn này là gì.

Vì vậy, họ sử dụng nó trong các chức năng chính.

Tôi sẽ xóa lệnh hiện có và sau đó tôi sẽ thay thế nó bằng một khai báo

báo về một lát cắt mới.

Vì vậy, tôi sẽ tạo một biến có tên là phần cắt của tôi.

Tôi sẽ sử dụng cú pháp dấu chấm bằng và sau đó khai báo một đoạn chuỗi.

Và bên trong nó, chúng tôi sẽ cung cấp văn bản cho nó.

Chào bạn.

Bạn khỏe không?

Vì vậy, đây là lát của chúng tôi.

Nó có một chút yếu tố bên trong nó.

Bây giờ tôi sẽ tạo một chức năng đặc biệt là cắt lát và cập nhật một trong các phần tử bên trong

nó.

Vì vậy, chúng tôi sẽ nói lát cập nhật chức năng.

Sẽ có một đối số mà chúng ta sẽ gọi là S viết tắt của lát cắt.

Đó sẽ là loại, lát của chuỗi.

Và bên trong đây, hãy tưởng tượng rằng chúng ta muốn thay thế phần tử đầu tiên bên trong lát cắt.

Vì vậy, tôi sẽ nói s ở số không, đó là phần tử đầu tiên bên trong.

Cung cấp cho nó bản văn của.

Vì vậy, chỉ cần thay thế toàn bộ bản văn trong phần tử đầu tiên này và sau đó bên dưới lát ban đầu

ngay tại đây, hãy gọi hàm mới đó.

Vì vậy, chúng tôi sẽ thông báo cập nhật lát và chuyển trong lát của tôi.

Và ngay sau đó chúng tôi sẽ đăng sản phẩm cắt của tôi có giá trị cao.

Vì vậy, chúng tôi sẽ nói dòng trong Fmt theo từng lát như vậy.

Bây giờ đoạn mã mà chúng ta có ở đây nhìn rất giống với tất cả các đoạn mã mà chúng ta

đã viết cho đến đây xung quanh một cấu trúc.

Chúng tôi khai báo một giá trị mới.

Trong trường hợp này, lát cắt trước đây là một cấu trúc.

Sau đó, chúng tôi chuyển giá trị đó cho một hàm.

Chúng tôi sửa đổi giá trị và sau đó chúng tôi cố gắng hoàn thiện cơ sở dữ liệu cấu trúc sau khi nó

được chuyển cho hàm.

Và vì vậy, như chúng ta vừa thấy 2 phút trước, giống như trong tất cả các video trước đây mà

chúng tôi đã xem qua, chúng tôi đã không ngừng nói rằng khi chúng tôi đang làm việc với một cấu trúc hoặc

bất kỳ loại giá trị nào, bất kỳ loại biến thể nào và chúng tôi chuyển nó cho một chức năng, dữ liệu cấu trúc đó sẽ được sao chép và sao chép

được vận hành bên trong hàm.

Chúng tôi đã nói điều đó không ngừng cho đến thời điểm này.

Vì vậy, hãy chạy đoạn mã này ngay tại đây và xem điều gì xảy ra với lệnh cập nhật này.

Bây giờ, nếu cắt hoạt động tương tự như cách làm cấu trúc, khi chúng tôi đăng xuất cắt của tôi ngay tại

ở đây, chúng tôi mong đợi thành phần tử đầu tiên vẫn ở mức cao.

Vì vậy, hãy chạy điều này và xem điều gì sẽ xảy ra.

Vì vậy, khi chúng tôi chạy nó, rất ngạc nhiên, chúng tôi đã tìm thấy văn bản ngay tại đây.

Vì vậy, mặc dù chúng tôi không sử dụng con trỏ, không có gì giống như vậy, không có bộ nhớ nào để giải quyết bất cứ điều gì.

Có vẻ như một lát cắt, khi chúng tôi sửa đổi nó bên trong hàm này, nó thực sự đã sửa đổi giá trị

cấm đầu, điều này hoàn toàn trái ngược với cấu trúc hoạt động của chúng tôi.

Vì vậy, đây là điều tôi đã nói đến.

Đây là điều quan trọng mà nó giống như ồ, điều này không hoàn toàn hoạt động theo cùng một cách

với cấu hình như một lát cắt.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại phần tiếp theo và chúng ta sẽ tìm hiểu chính xác tại sao đoạn

Mã này hoạt động khác với một lát cắt cho một cấu trúc.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ nói về những gì đang xảy ra ở đây.