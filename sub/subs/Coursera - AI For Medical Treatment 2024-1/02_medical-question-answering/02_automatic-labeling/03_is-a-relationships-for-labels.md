# 03 là-một-mối-quan-nhãn

---

Chúng ta hãy xem một cách khác trong đó

thuật ngữ có thể giúp chúng tôi.

Giả sử chúng ta muốn tìm

đề cập đến 'bệnh phổi'.

Như trước đây, chúng ta có thể tìm kiếm

báo cáo về 'bệnh phổi' hoặc

từ đồng nghĩa của nó bằng cách sử dụng một thuật ngữ.

Tuy nhiên, điều này có thể trở lại

không có kết quả vì 'nhiễm trùng'

không phải là từ đồng nghĩa trực tiếp của 'bệnh phổi'.

Bây giờ báo cáo này cho chúng ta biết rằng

có đề cập đến 'viêm phổi',

đó là một loại bệnh về phổi.

Vì vậy, chúng ta có thể nói có đối với

đề cập đến 'bệnh phổi'.

Làm thế nào để chúng ta giải quyết thách thức này?

Chúng ta có thể quay lại

thuật ngữ để giúp chúng tôi.

Các thuật ngữ không chỉ chứa

từ đồng nghĩa với khái niệm của chúng tôi nhưng

cũng chứa đựng những mối quan hệ

sang các khái niệm khác.

Ở đây, chúng ta có thể thấy 'cảm lạnh thông thường'

có mối quan hệ Is-A với

'Nhiễm trùng đường hô hấp trên do virus'.

Tương tự với 'viêm phổi' chúng ta có thể

thấy một hệ thống phân cấp của các mối quan hệ.

Làm thế nào một loại viêm phổi cụ thể

là bệnh viêm phổi truyền nhiễm,

đó là bệnh viêm phổi

đó là bệnh phổi.

Vì vậy, chúng ta có thể bắt gặp nhắc tới 'phổi'

bệnh' bằng cách không chỉ tìm kiếm

từ đồng nghĩa với 'bệnh phổi' trong SNOMED CT,

mà còn cả các kiểu con và từ đồng nghĩa của chúng.

Ở đây các phân nhóm sẽ bao gồm viêm phổi và

những khái niệm khác có

mối quan hệ Is-A với bệnh phổi.

Ưu điểm của phương pháp này mà chúng tôi

có thể gọi một cách tiếp cận dựa trên quy tắc để tìm kiếm

đề cập đến các quan sát, là chúng ta không

cần bất kỳ dữ liệu nào cho việc học có giám sát.

Nhược điểm của phương pháp này là

rằng có rất nhiều công việc thủ công

để tinh chỉnh các quy tắc này dựa trên những gì

đang hoạt động và những gì không hoạt động.

Chúng ta có thể áp dụng phương pháp này

đến một số quan sát

để xem liệu chúng có được nhắc tới hay không.

Trong báo cáo này chúng ta có thể thấy rằng 'khối lượng' không phải là

được đề cập nhưng 'phù nề' và 'viêm phổi' thì có.

Tuy nhiên, hãy lưu ý rằng nó sẽ

không đúng khi có nhãn 1

về 'viêm phổi' và 'phù nề' cho báo cáo này.

Đó là do chúng ta chưa tính đến

hãy tính đến 'không' trước những đề cập này.

Đây là lý do tại sao chúng ta cần bước thứ hai trong

đường dẫn của chúng tôi, sử dụng đầu ra

của bước một đến bây giờ quyết định xem liệu

mỗi đề cập có mặt hoặc vắng mặt.

Chúng ta có thể viết một quy tắc để xác định

'phù nề' đó sẽ không xuất hiện nếu

báo cáo có chữ 'không' đúng không

trước từ 'phù nề'.

Và mặc dù chúng tôi có thể nắm bắt được

'phù nề' theo cách đó, chúng ta sẽ không thể

để nắm bắt từ 'không' trước 'viêm phổi' bởi vì

chúng cách nhau một vài từ.

Chúng ta phải có khả năng nắm bắt

mối quan hệ giữa 'không' và

'viêm phổi' mà không trực tiếp tìm kiếm

chính xác là 'không viêm phổi'.