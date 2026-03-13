# 04 - Đánh giá kết quả học tập chuyển tiếp

---

- [Giáo viên] Bây giờ chúng ta đã thấy rồi

chuyển giao việc học trong hành động,

hãy tập trung vào việc đánh giá kết quả của việc học chuyển tiếp,

cụ thể là sử dụng các số liệu như ROUGE và BLEU.

Những chỉ số này rất cần thiết

để đánh giá chất lượng công việc,

chẳng hạn như tóm tắt văn bản và dịch máy,

tương tự như cách sử dụng độ chính xác trong các nhiệm vụ phân loại.

Hãy bắt đầu bằng cách hiểu ROUGE và BLEU.

Hãy coi ROUGE như một thước đo cho sự chồng chéo

giữa văn bản được tạo và văn bản tham chiếu,

giống như so sánh bao nhiêu

hai công thức nấu ăn có cùng thành phần.

Mặt khác, BLEU

đo lường mức độ văn bản được tạo ra

khớp với văn bản tham chiếu,

tương tự như so sánh hai món ăn đã hoàn thành

để xem chúng giống nhau đến mức nào

trong hương vị và cách trình bày.

ROUGE là viết tắt của Định hướng thu hồi

Nghiên cứu đánh giá Gisting.

Nó chủ yếu được sử dụng để đánh giá chất lượng của các bản tóm tắt

bằng cách đo sự chồng chéo giữa bản tóm tắt được tạo

và một tập hợp các tóm tắt tham khảo.

Hãy tưởng tượng so sánh một bản tóm tắt mới với một bản tóm tắt tiêu chuẩn vàng,

kiểm tra xem có bao nhiêu cụm từ khóa và từ trùng nhau.

Ví dụ, hãy xem xét hai câu.

Tóm tắt được tạo là "Con mèo ngồi trên tấm thảm."

Tóm tắt tham khảo là "Con mèo đang ngồi trên tấm thảm."

Để tính ROUGE-1, điều đó có nghĩa là sự chồng chéo unigram,

chúng tôi sẽ đếm số lượng từ chồng chéo

và chia cho tổng số từ

trong phần tóm tắt tài liệu tham khảo.

Trong trường hợp này, các từ chồng lên nhau là

cái, con mèo, trên, cái, tấm thảm.

Sự khác biệt duy nhất nằm ở "ngồi" và "ngồi".

Do đó, ROUGE-1 sẽ là 5/6, hay 83%.

Chẳng hạn như ROUGE-1, có ROUGE-2, ROUGE-3, v.v.

Chúng tôi thường trình bày ba điều đầu tiên

và chúng tôi coi những điều đó là ổn.

Mặt khác, BLEU

là viết tắt của Nghiên cứu Đánh giá Song ngữ.

Nó đo lường mức độ chặt chẽ

văn bản được tạo khớp với văn bản tham chiếu

bằng cách so sánh các đảo chữ cái,

có nghĩa là chuỗi n từ.

BLEU giống như một nhà phê bình ẩm thực tỉ mỉ,

người không chỉ kiểm tra xem thành phần có đúng không,

mà còn nếu chúng được kết hợp

theo đúng thứ tự và tỷ lệ.

Như một ví dụ về tính toán BLEU,

hãy xem xét cùng một thế hệ,

"Con mèo ngồi trên tấm thảm,"

và cùng một tài liệu tham khảo, "Con mèo đang ngồi trên tấm thảm."

Để tính BLEU-1, chúng ta sẽ tính

số lượng unigram phù hợp

và chia cho tổng số unigram

trong văn bản được tạo trước khi nó nằm trong văn bản tham chiếu.

Vậy bây giờ, BLEU-1 sẽ là 5 trên 5,

nên nó sẽ là 100%.

Bạn có thể coi BLEU như một phép đếm chính xác

và ROUGE làm số lần thu hồi,

nếu bạn nhớ từ nhiệm vụ phân loại.

Trên thực tế, cả ROUGE và BLEU

rất quan trọng trong việc đánh giá các nhiệm vụ tạo văn bản,

tương tự như cách sử dụng độ chính xác trong các nhiệm vụ phân loại.

Trong khi ROUGE tập trung vào việc biến về,

nắm bắt được bao nhiêu phần tóm tắt tham khảo

có mặt trong bản tóm tắt được tạo,

BLEU tập trung vào độ chính xác,

đánh giá mức độ văn bản được tạo phù hợp với tham chiếu

về các cụm từ chính xác và thứ tự của chúng.

Điều quan trọng là phải đề cập đến

rằng mặc dù ở đây chúng ta đang nói về khả năng ghi nhớ,

ROUGE và BLEU đều được sử dụng

cũng như trong dịch máy thần kinh hoặc trả lời câu hỏi,

hoặc về cơ bản là bất kỳ tác vụ chuyển văn bản thành văn bản nào.

Hãy xem xét các ứng dụng thực tế

với một số ví dụ về mã sử dụng thư viện Ôm Mặt.

Vì vậy, ở đây, đầu tiên chúng ta sẽ tải số liệu,

và chúng tôi sẽ tải ROUGE chỉ vì chúng tôi muốn,

và chúng ta sẽ so sánh các bản tóm tắt được tạo ra

so với các bản tóm tắt tham khảo.

Giống như chúng ta vừa nói, "Con mèo ngồi trên chiếu,"

và "con mèo đang ngồi trên tấm thảm."

Để thực hiện phép tính đó chúng ta chỉ cần thực hiện ROUGE để tính toán.

Chúng tôi vượt qua các dự đoán và tài liệu tham khảo

và chúng tôi in kết quả,

và đó là mã để chạy ROUGE.

Tôi khuyến khích bạn lấy mã này

và bây giờ hãy chạy nó để xem kết quả.

Mặt khác, nếu chúng ta muốn sử dụng BLEU,

đó là cùng một ý tưởng

Chúng tôi chỉ tải số liệu BLEU,

và sau đó chúng tôi lấy văn bản được tạo ra, văn bản tham chiếu,

và dựa vào đó chúng tôi thực hiện bleu.compute.

Một lần nữa tôi khuyến khích các bạn dừng video lại,

thử cả hai số liệu về mã,

và xem khuôn khổ thực tế trình bày chúng như thế nào.

(nhạc sôi động)

Hiểu và vận dụng

Số liệu ROUGE và BLEU là cần thiết

để đánh giá các nhiệm vụ tạo văn bản một cách hiệu quả.

Bằng cách so sánh các số liệu này

đến độ chính xác và phân loại,

we can better appreciate their role

trong việc đánh giá chất lượng của văn bản do AI tạo ra.