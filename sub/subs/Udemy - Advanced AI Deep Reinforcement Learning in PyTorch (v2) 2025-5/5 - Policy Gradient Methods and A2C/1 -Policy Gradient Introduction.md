# 1 -Giới thiệu về Chính sách gradient

---

Trong video này, chúng tôi sẽ giới thiệu phần tiếp theo của khóa học này, đó là về chính sách

phương pháp gradient và A2C. Vì chúng ta chưa đề cập đến các mức độ chính sách nên trong loạt bài này

các khóa học tăng cường, chúng tôi sẽ rút ra mọi thứ từ đầu. Điều này khác

từ DQN, vì chúng tôi không học Q từ đầu trong khóa học này. Mặc dù đủ

trực giác đã được cung cấp để làm cho nó có ý nghĩa. Khi chúng tôi đã nhận được gradient chính sách

thuật toán, chúng tôi sẽ mở rộng nó sang phương pháp phê bình diễn viên và từ đó chỉ là một bước nhỏ

bước để đạt được A2C. Một thành phần quan trọng trong A2C là đường cơ sở. Về cơ bản, điều này

liên quan đến việc sử dụng thuật ngữ gọi là lợi thế thay cho lợi nhuận, trong đó chúng ta trừ đi

một giá trị cơ bản từ kết quả trả về. Là một bước tùy chọn, chúng tôi sẽ thực hiện một phân tích nhỏ để chứng minh

việc trừ đi đường cơ sở này là không thiên vị và làm giảm phương sai. Cuối cùng, chúng ta sẽ triển khai

A2C bằng Python. Như một phần thưởng, tôi đã đính kèm một bài giảng về các phương pháp tiến hóa trong việc củng cố

học tập, vì nó liên quan mật thiết đến những gì chúng ta đã nghiên cứu trong phần này. Trong bản gốc của tôi

trong chuỗi các khóa học tăng cường, tôi đã dạy các phương pháp tiến hóa cùng với A2C.

Vì phần này chuyên sâu về mặt lý thuyết hơn nhiều so với DQN nên nó sẽ rất quan trọng.

đề cập ngắn gọn các điều kiện tiên quyết. Vì chúng ta sẽ thảo luận về các khái niệm về độ lệch

và phương sai, bạn sẽ muốn gặp phải điều này trong khóa học thống kê trước đó. Như bạn

có thể mong đợi, nó cũng liên quan đến phép tính, vì chúng ta sẽ xem xét độ dốc. có

cũng là xác suất, nhưng có lẽ bạn đã biết điều này, nếu bạn biết học tăng cường,

và bản thân số liệu thống kê phụ thuộc vào xác suất. Nhân tiện, hầu hết điều này về cơ bản là một

được đưa ra, vì các điều kiện tiên quyết tương tự cũng áp dụng cho việc học tăng cường nói chung và

cụ thể là khóa học củng cố tiên quyết, có trước khóa học này.