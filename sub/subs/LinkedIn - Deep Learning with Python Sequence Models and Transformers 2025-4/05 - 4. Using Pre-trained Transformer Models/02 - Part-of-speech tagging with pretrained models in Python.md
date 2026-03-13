# 02 - Gắn thẻ một phần lời nói với các mô hình được đào tạo trước trong Python

---

- [Người kể chuyện] Trong video này,

chúng ta sẽ sử dụng một mô hình được đào tạo trước

để thực hiện một phần gắn thẻ lời nói hoặc gắn thẻ POS trên văn bản.

Ý tưởng đằng sau việc gắn thẻ POS

là gán từng mã thông báo trong một câu

phạm trù ngữ pháp tương ứng của nó,

như danh từ, động từ hoặc tính từ.

Vì vậy, điều đầu tiên chúng ta làm ở đây là chỉ định kernel của mình,

điều mà tôi đã làm rồi, Python 3.1.

Sau đó chúng ta sẽ đi tiếp

và giảm thiểu tính dài dòng trong nhật ký của chúng tôi.

Vì vậy hãy tiếp tục và chạy đoạn mã ở đây

để giảm thiểu các thông báo chúng tôi nhận được

từ gói máy biến áp,

có thể rất, rất dài dòng.

Và điều đầu tiên, điều tiếp theo chúng tôi thực sự làm

bây giờ là khởi tạo

hoặc khởi tạo quy trình để gắn thẻ POS.

Vì vậy, chức năng đường ống

không có tác vụ POS được tích hợp sẵn trong đó,

nhưng chúng ta có thể sử dụng nhiệm vụ phân loại mã thông báo.

Tuy nhiên, chúng tôi chỉ định một mô hình gắn thẻ POS dành riêng cho mục đích cụ thể.

Và đối với ví dụ cũ này,

chúng ta sẽ sử dụng mô hình bert-english-uncased-finetuned-pos

được thiết kế riêng cho việc gắn thẻ POS,

và chúng ta sẽ gọi nhiệm vụ phân loại mã thông báo

cho mô hình cụ thể này.

Vì vậy, chúng tôi nhập chức năng đường ống, chỉ định tên

của mô hình mà chúng tôi muốn sử dụng,

và chúng tôi khởi tạo một quy trình mới gọi là tagger

với nhiệm vụ phân loại mã thông báo,

và chúng tôi chỉ định tên của mô hình.

Vì vậy, hãy tiếp tục và chạy nó.

Vì vậy, khi quá trình đó hoàn tất, bước tiếp theo chỉ đơn giản là

để thực hiện gắn thẻ POS dựa trên quy trình mà chúng tôi vừa khởi tạo.

Vì vậy, ở đây chúng ta sẽ sử dụng một đoạn văn bản đơn giản.

John thích chơi bóng đá trong công viên.

Vì vậy, ý tưởng ở đây là có thể phân loại

hoặc chỉ định một danh mục, nhãn ngữ pháp

cho mỗi mã thông báo trong văn bản này.

Vì vậy, chúng tôi sẽ sử dụng công cụ gắn thẻ quy trình,

được chuyển cùng với văn bản mẫu,

và chúng tôi sẽ chuyển đổi kết quả sang Khung dữ liệu Pandas,

chỉ để làm việc theo cách đó có vẻ dễ dàng hơn.

Được rồi, vậy chúng ta chạy cái này theo cách đó, và chúng ta có nó.

Vì vậy, chúng tôi có tất cả các mã thông báo trong văn bản này được gắn thẻ.

Vì vậy chúng ta thấy rằng John đã được gắn thẻ như một danh từ riêng,

yêu như một động từ, chơi như một động từ, bóng đá như một danh từ,

vào một vị trí.

Và sau đó chúng ta có the như một từ hạn định, danh từ, park là một danh từ.

Và rõ ràng, dấu chấm là dấu chấm câu.

Vì vậy, bạn có nó.

Với một vài dòng mã, chúng tôi có thể gắn thẻ POS

với mô hình được đào tạo trước bằng Python.