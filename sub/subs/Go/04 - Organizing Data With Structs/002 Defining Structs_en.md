# 002 Xác định cấu trúc vi

---

Người hướng dẫn: Trong video cuối cùng,

chúng tôi bắt đầu nói về cấu trúc và bắt đầu.

Cấu trúc được sử dụng rộng rãi

xuyên suốt toàn bộ ngôn ngữ. Và vì vậy nó thực sự quan trọng

để nắm vững chính xác cách chúng hoạt động.

Để đảm bảo rằng chúng ta có được một số thông tin cơ bản thực sự tốt,

chúng ta sẽ làm việc rất đơn giản,

dự án rất đơn giản chỉ là một loại

khám phá cách chúng ta có thể định nghĩa và sử dụng các cấu trúc.

Vì vậy, chúng tôi chỉ tập hợp tệp dấu chấm chính mới này.

Hãy bắt đầu

trước tiên bằng cách thêm bản tóm tắt dự án thông thường của chúng tôi.

Vì vậy, ở trên cùng, chúng ta sẽ xác định gói chính,

và sau đó chúng ta sẽ xác định chức năng chính của mình.

Được rồi, vậy hãy nói chuyện

về các cấu trúc mà chúng ta sẽ tạo ra bên trong đây.

Vì vậy, bất cứ khi nào chúng ta tạo một cấu trúc, trước tiên chúng ta phải xác định tất cả

các thuộc tính khác nhau mà một cấu trúc có thể có.

Chúng tôi sẽ cung cấp điều này trong một số loại quy tắc được thiết lập,

và sau đó chúng ta có thể tạo một giá trị phù hợp với loại đó

về định nghĩa cấu trúc

Bây giờ đối với dự án cụ thể này, tôi muốn

hãy tưởng tượng rằng chúng ta sẽ tạo một cấu trúc để

đại diện cho một người như bạn hoặc tôi.

Vì vậy, chúng ta sẽ nói rằng mỗi người, có thể có một cái tên

chúng tôi muốn ghi lại và có thể họ cũng có họ.

Vì vậy, hãy xem chúng ta sẽ làm điều này như thế nào.

Được rồi, điều đầu tiên chúng ta sẽ làm là

chúng tôi sẽ cho biết chính xác những lĩnh vực khác nhau

một người nên có.

Vì vậy chúng ta sẽ nói đi

rằng một người nên có một tài sản

tên và thuộc tính của họ.

Và sau đó chúng ta cũng sẽ chỉ định loại

của cả hai lĩnh vực đó.

Vì vậy chúng ta sẽ nói rằng tên là một chuỗi

và tất nhiên họ cũng sẽ là một chuỗi.

Vì vậy, bước một lần nữa,

là để xác định chính xác những trường khác nhau mà cấu trúc này có.

Và sau đó ở bước hai, chúng ta sẽ tạo một giá trị mới

thuộc loại người.

Và về cơ bản bạn có thể coi đây là

một triển khai thực tế hoặc một bản sao thực tế của một người.

Và vì vậy chúng tôi có thể tạo ra bao nhiêu người thực tế tùy thích hoặc

bao nhiêu giá trị của kiểu người tùy thích.

Một cái cho mỗi người mà chúng ta có thể muốn làm mẫu bên trong

của một chương trình nhất định.

Về cơ bản, sau khi chúng ta yêu cầu bắt đầu hoặc sau khi chúng ta xác định chính xác

con người là gì, chúng ta có thể tạo ra bao nhiêu người tùy thích

bên trong chương trình của chúng tôi.

Vì vậy bây giờ chúng ta hãy quay lại trình soạn thảo mã của chúng ta và hình dung

chính xác cách ban đầu chúng ta xác định cấu trúc này là gì.

Được rồi, vậy chúng ta sẽ thay đổi lại.

Và ngay phía trên phần khai báo hàm chính của chúng ta,

chúng ta sẽ thêm một chút mã để xác định cái mới này

struct và cho biết chính xác những thuộc tính cần có.

Để làm như vậy, chúng ta sẽ viết ra kiểu người, struct

và sau đó là dấu ngoặc nhọn.

Cú pháp này ở đây có lẽ trông khá quen thuộc

với một số cú pháp mà chúng tôi đã sử dụng trong dự án thẻ.

Khi chúng tôi xác định một loại thẻ mới, hoặc xin lỗi

chúng tôi đã xác định một loại bộ bài.

Vì vậy, trong trường hợp này, chúng tôi đang xác định một loại tùy chỉnh mới

điều đó sẽ chỉ tồn tại bên trong chương trình của chúng tôi.

Đây là một người tốt bụng và nó sẽ như vậy

một cấu trúc với các trường sau.

Vì vậy, hãy xác định trường tên và trường họ.

Vì vậy chúng ta sẽ nói rằng mỗi người

có thể có tên kiểu chuỗi

và họ cũng có thể có họ thuộc loại chuỗi.

Bây giờ, khi chúng ta xác định các trường khác nhau này

hoặc những thuộc tính khác nhau cho cấu trúc này,

bạn sẽ nhận thấy rằng chúng tôi không tách chúng ra

bằng bất kỳ dấu phẩy, dấu hai chấm, dấu chấm phẩy, bất cứ thứ gì tương tự.

Rất đơn giản thôi, đây là tên thuộc tính

và đây là loại nó nên có.

Vậy là bây giờ chúng ta đã tạo ra được định nghĩa về con người là gì,

bây giờ chúng ta có thể tạo ra các giá trị bên trong

ứng dụng của chúng tôi phù hợp với cấu trúc này.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại trong phần tiếp theo và chúng ta sẽ tìm hiểu

tìm ra tất cả những cách khác nhau mà chúng ta có thể tạo ra

một giá trị của loại người.

Bởi vì, như bạn có thể tưởng tượng, có nhiều hơn một.

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng

và tiếp tục ở phần tiếp theo.