# 15 -Dịch tiêu chuẩn phi kỹ thuật

---

Tôi muốn dành chút thời gian để thảo luận về các cách khác để đánh giá khả năng thực hiện LLM

không liên quan gì đến mô hình, nhật ký hoặc xác suất softmax hoặc thậm chí hoạt động

với chính mô hình đó.

Vấn đề là, những LLM này không chỉ tồn tại riêng lẻ trong một môi trường học thuật trừu tượng nào đó.

Chúng được phát triển bởi các công ty và tổ chức có mục tiêu cụ thể là phát triển AI,

thường có giá trị thương mại hoặc ứng dụng nào đó.

Vì vậy, trong video này, tôi sẽ chỉ đề cập ngắn gọn một số chỉ số quan trọng

về hiệu suất của LLM có thể mang tính định lượng nhưng không mang tính kỹ thuật.

Và tôi muốn bắt đầu với một meme.

Có lẽ điều này hơi sến một chút nhưng điều tôi muốn diễn đạt ở đây là

vì mục đích ứng dụng, không ai quan tâm đến một số điểm eVELS định lượng.

Bạn biết đấy, nếu AI giúp một số nhà hóa sinh phát triển một loại thuốc mới giúp được nhiều người,

sẽ không ai quan tâm liệu mô hình đó có điểm MOV thấp hay cao.

Vì vậy, với ý nghĩ đó, bây giờ hãy để tôi gieo mầm trí tưởng tượng của bạn bằng một số số liệu hữu ích khác

về tiện ích của LLM.

Một số mục danh sách mà tôi sẽ trình bày trên slide này mang tính định lượng theo nghĩa

rằng bạn có thể đo lường chúng và đính kèm các con số vào chúng.

Những cái khác thực sự có chất lượng hơn, vì vậy tôi cho rằng về mặt kỹ thuật thì chúng nên thuộc về

phần tiếp theo của khóa học, nhưng tôi hy vọng bạn sẽ tha thứ cho tôi vì đã trộn lẫn một số chủ đề.

Dù sao đi nữa, một thước đo là mức sử dụng mà bạn có thể định lượng, chẳng hạn như số lượng người

tích cực sử dụng một LLM cụ thể hoặc có thể đăng ký một tài khoản cần thiết

sử dụng LLM.

Có thể đó là số lượt tải xuống nếu đó là mô hình được cung cấp công khai.

Sau đó, bạn có thể định lượng mức độ hài lòng của người dùng, bạn có thể định lượng mức độ hữu ích của báo cáo của người dùng

LLM sẽ được.

Nhiều công ty phát triển LLM lớn như Google, Meta, OpenAI, Microsoft là bốn

các tổ chức lợi nhuận, vì vậy họ quan tâm đến việc họ có thể kiếm được bao nhiêu tiền từ hoạt động của mình.

LLM.

Cũng như mức độ họ đang nhận được sự chú ý của giới truyền thông, cả tin tức, phương tiện truyền thông truyền thống và

cũng như mạng xã hội.

Với hệ sinh thái ứng dụng cụm từ này, tôi đang đề cập đến cách LLM được tích hợp vào bên thứ ba

ứng dụng.

Ví dụ: có bao nhiêu người đang sử dụng API để truy cập LLM thông qua một số trang web của bên thứ ba

hoặc giống như một ứng dụng điện thoại.

Tất nhiên, một phép định lượng quan trọng là chi phí đào tạo và sử dụng LLM.

Và điều đó có thể bao gồm cả chi phí ban đầu cho việc đào tạo trước và tinh chỉnh, chi phí cho

ví dụ: mua GPU mới, chi phí nhân viên, chi phí sử dụng năng lượng cũng như chi phí liên tục

chi phí cho mỗi mã thông báo để thực hiện chuyển tiếp.

Tôi đã đề cập trước đó trong khóa học rằng việc đào tạo GPT biên giới hiện đại từ đầu là một điều gì đó

khoảng vài chục triệu USD.

Liên quan, nhiều người lo ngại một cách chính đáng về lượng năng lượng khổng lồ

được tiêu thụ bởi LLM.

Việc đào tạo những mô hình này đòi hỏi một lượng năng lượng khổng lồ, điều đó có nghĩa là việc sử dụng LLM cũng

gây ra nhiều ô nhiễm.

Và đó là một khía cạnh khác để coi là thước đo của LLM cũng như sự phát triển và sử dụng.

Chà, đó chắc chắn không phải là một danh sách đầy đủ, nhưng tôi nghĩ bạn hiểu ý.

Vấn đề là mặc dù đánh giá kỹ thuật về năng lực và kiến thức thế giới là quan trọng

và chúng ta cần tiếp tục phát triển các phương pháp eVal tốt hơn, cũng có những phương pháp quan trọng khác

cách suy nghĩ về chi phí, lợi ích và tác động của LLM không có gì

để làm với các nhà nghỉ mã thông báo.