# 07 ngữ nghĩa-tìm kiếm-nhúng-mô hình-deepdive

---

Công việc của mô hình nhúng khá đơn giản để mô tả.

Nó cần nhúng văn bản tương tự vào các vectơ gần nhau và không giống nhau

văn bản thành các vectơ cách xa nhau hơn.

Nếu bạn thử tưởng tượng các mô hình nhúng thực sự làm được điều này như thế nào, bạn sẽ nhận ra nó như thế nào.

họ cần phải phức tạp.

Làm sao máy tính có thể hiểu được ý nghĩa của một đoạn văn bản?

Let's look a little closer at how embedding models achieve this incredible feat.

Bạn có thể hình dung công việc của mô hình nhúng theo các cặp dương và âm.

Một cặp tích cực là hai đoạn văn bản tương tự nhau, như chào buổi sáng và xin chào, nên

được nhúng gần nhau.

Một cặp phủ định, như chào buổi sáng và đó là tiếng kèn trombone ồn ào, có ý nghĩa khác nhau,

và nên được nhúng xa hơn.

Các mô hình nhúng cần hoạt động sao cho các cặp dương gần nhau hơn và các cặp âm

các cặp cuối cùng cách xa nhau hơn.

Bước đầu tiên để đào tạo mô hình nhúng là biên soạn một bộ sưu tập lớn các thông tin tích cực

và các cặp phủ định, còn được gọi là ví dụ.

Trong nhiều hệ thống, điều này có nghĩa là các bộ sưu tập dữ liệu thực sự khổng lồ, thường có hàng triệu

của các cặp bao gồm.

Một từ hoặc đoạn văn bản riêng lẻ sẽ được đưa vào nhiều ví dụ để nắm bắt được mối quan hệ của nó

với nhiều văn bản và khái niệm khác nhau.

Khi những ví dụ này đã được biên soạn, việc đào tạo có thể bắt đầu.

Khi bắt đầu đào tạo, các mô hình nhúng sẽ nhúng từng đoạn văn bản vào một vectơ ngẫu nhiên.

Những vectơ này vô nghĩa và sẽ không có mối quan hệ nào với ý nghĩa của văn bản.

Nếu bạn sử dụng mô hình nhúng chưa được đào tạo này để truy xuất, kết quả sẽ vô nghĩa.

Bây giờ mô hình xem xét tất cả các cặp dương và âm trong dữ liệu huấn luyện của nó và hỏi

Tôi đã đặt các cặp dương với nhau và các cặp âm cách nhau tốt như thế nào.

Vì mô hình đang sử dụng độ tương phản được cung cấp bởi các ví dụ tích cực và tiêu cực để đánh giá

hiệu suất của nó, kỹ thuật này được gọi là đào tạo tương phản.

Dựa trên mức độ hoạt động của nó, mô hình sẽ cập nhật các thông số bên trong của nó.

Nó sử dụng một thuật toán cố gắng di chuyển các cặp dương gần nhau hơn và các cặp âm

cặp xa nhau hơn.

Sau khi cập nhật các tham số của mô hình nhúng, bạn chỉ cần lặp lại quy trình.

Văn bản được nhúng vào các vectơ mới bằng cách sử dụng các tham số được cập nhật của mô hình.

Hiệu suất của mô hình được đánh giá lại bằng cách sử dụng các cặp dương và âm và

dựa trên hiệu suất đó, các thông số của nó lại được cập nhật.

Quá trình này được lặp lại nhiều lần, liên tục cập nhật các tham số của mô hình, đẩy

và kéo các cặp lại gần nhau hơn hoặc xa nhau hơn.

Sau nhiều vòng huấn luyện, các cặp tích cực sẽ được xích lại gần nhau,

và các cặp âm đáng lẽ phải bị đẩy ra xa nhau.

Chúng ta hãy xem xét quá trình này từ góc nhìn của một đoạn văn bản.

Cụm từ, anh ấy có thể ngửi thấy mùi hoa hồng, mà tôi sẽ gọi là điểm neo của chúng tôi, nó mang ý nghĩa tích cực

ghép với cụm từ cánh đồng hoa thơm và cặp phủ định với cụm từ,

một con sư tử gầm lên uy nghiêm.

Khi bắt đầu đào tạo, ba cụm từ này được ánh xạ tới các vị trí ngẫu nhiên với

không phản ánh ý nghĩa của chúng.

Từ quan điểm của người neo, nó muốn kéo ví dụ tích cực lại gần hơn và nó muốn

để đẩy ví dụ tiêu cực ra xa hơn.

Chỉ với ba đoạn văn bản, quá trình này khá đơn giản để hình dung.

Sau nhiều đợt huấn luyện, người dẫn chương trình muốn rút ra tấm gương tích cực càng gần

nhất có thể và đẩy ví dụ tiêu cực đi càng xa càng tốt.

Điều đó có nghĩa là bạn sẽ không bao giờ đào tạo một mô hình nhúng chỉ với hai cặp.

Khi bạn cố gắng hoàn thành quá trình này với hàng triệu neo, tích cực và tiêu cực

điểm, quá trình này sẽ trở nên rắc rối hơn rất nhiều.

Mọi vectơ đều đồng thời bị đẩy và kéo theo nhiều hướng.

Điều này giúp giải thích tại sao các mô hình sử dụng vectơ có hàng trăm hoặc thậm chí hàng nghìn chiều.

Không gian nhiều chiều mang lại cho thuật toán nhiều lựa chọn về vị trí đẩy và kéo

các vectơ để phản ánh các mối quan hệ sắc thái trong dữ liệu huấn luyện.

Sau khi huấn luyện, các vectơ nắm bắt được ý nghĩa vì các từ hoặc văn bản tương tự đã được kéo ra

các diện tích tương tự của không gian vectơ.

Bạn không cần đào tạo mô hình nhúng để xây dựng hệ thống giá đỡ, nhưng hiểu biết

cách họ được đào tạo có thể giúp bạn hiểu rõ hơn về các vectơ mà họ tạo ra.

Điểm chính cần biết là các vectơ ngữ nghĩa có tính trừu tượng và hơi ngẫu nhiên.

Trước khi huấn luyện, một vị trí trong không gian không có bất kỳ ý nghĩa nào và các vectơ được đặt ngẫu nhiên.

Sau khi huấn luyện, các vị trí khác nhau trong không gian đều có ý nghĩa ngữ nghĩa, nhưng chỉ vì

đó là nơi hình thành một nhóm các khái niệm tương tự.

Ví dụ, ở đâu đó có thể có một cụm từ liên quan đến sư tử và

một cụm khác liên quan đến kèn trombone.

Nếu bạn chạy quá trình huấn luyện hai lần nhưng với các vectơ ngẫu nhiên ban đầu khác nhau thì các vectơ này

các cụm tương tự vẫn sẽ hình thành, nhưng chúng sẽ ở các vị trí khác nhau trong không gian vectơ.

Một điểm đáng chú ý khác là bạn chỉ so sánh các vectơ được tạo bởi cùng một mô hình nhúng.

Mỗi mô hình được huấn luyện với dữ liệu huấn luyện khác nhau, số lượng kích thước khác nhau và

với các giá trị khởi tạo ngẫu nhiên khác nhau.

Việc cố gắng so sánh các vectơ từ hai mô hình khác nhau sẽ dẫn đến kết quả vô nghĩa.

Trong thực tế, bạn có thể sẽ sử dụng các mô hình nhúng có sẵn và chúng sẽ mang lại hiệu quả đáng kể.

bạn đã làm tốt việc đặt các từ, câu hoặc tài liệu tương tự tại các vị trí tương tự trong không gian vectơ.

Bạn thậm chí có thể sẽ không thực hiện phép đo khoảng cách giữa các vectơ này.

Điều đó có nghĩa là, hiểu sâu hơn một chút về cách chúng hoạt động có thể giúp bạn đưa ra lý do chính xác hơn về

cách sử dụng chúng trong hệ thống RAG của bạn, vì vậy hãy tham gia cùng tôi trong video tiếp theo để biết bạn có thể đặt chúng như thế nào

những vectơ dày đặc này để sử dụng cho chó tha mồi của bạn.