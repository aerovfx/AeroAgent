# 02 kiến ​​trúc máy biến áp

---

Chó tha mồi của bạn vừa trả lại một loạt tài liệu có liên quan và bạn đã sẵn sàng xây dựng công cụ truy xuất tăng cường của mình

nhắc nhở.

Gửi nó đến LLM của bạn và nhận lại phản hồi dựa trên thông tin được truy xuất đó.

Bạn đã thấy quá trình này nhiều lần trong khóa học này, nhưng bây giờ là lúc để đi sâu hơn một cấp độ

sâu hơn và hỏi tại sao điều này lại có tác dụng?

Làm thế nào LLM có thể hiểu được thông tin được truy xuất đó?

Quan trọng hơn, làm cách nào bạn có thể sử dụng kiến ​​thức đó để xây dựng các hệ thống RAG có khả năng hoạt động tốt hơn nữa?

Để trả lời tất cả những điều đó, chúng ta hãy nhìn sâu hơn một chút vào kiến trúc máy biến áp

LLM được xây dựng trên.

Máy biến áp đã được đề xuất trong một bài báo chuyên đề từ năm 2017 có tựa đề Sự chú ý là tất cả của bạn

Need, tập trung vào vấn đề dịch máy.

Máy biến áp có hai thành phần chính là bộ mã hóa và bộ giải mã.

Bộ mã hóa sẽ xử lý văn bản gốc, chẳng hạn như một đoạn viết bằng tiếng Đức, đang phát triển

sự hiểu biết sâu sắc theo ngữ cảnh về ý nghĩa của đoạn văn.

Bộ giải mã sau đó sẽ sử dụng sự hiểu biết sâu sắc này về đoạn văn tiếng Đức để tạo ra một đoạn mã mới

Phiên bản tiếng Anh của nó.

Hầu hết các LLM chỉ bao gồm thành phần giải mã thứ hai vì chúng chỉ quan tâm đến việc tạo văn bản.

Trong khi đó, máy biến áp thường được sử dụng bên trong các mô hình nhúng vì mục tiêu của chúng là

là phát triển các cách biểu diễn ngữ nghĩa phong phú của văn bản.

Hãy theo dõi hành trình của lời nhắc thông qua LLM và do đó thông qua thành phần bộ giải mã

của một máy biến áp.

Điều đầu tiên xảy ra là lời nhắc của bạn được chia thành các mã thông báo.

Khi văn bản được mã hóa, mỗi mã thông báo sẽ được gán một biểu diễn vectơ dày đặc ban đầu.

Vectơ này về cơ bản là dự đoán đầu tiên về ý nghĩa của mã thông báo đó.

Những dự đoán này là tĩnh, vì vậy mỗi khi bạn cung cấp LLM cùng một mã thông báo, nó sẽ được chỉ định

cùng một vectơ đoán đầu tiên.

Tiếp theo, mỗi mã thông báo được cung cấp một vectơ vị trí ghi lại vị trí của nó trong dấu nhắc.

Khi các vectơ nhúng và vectơ vị trí đoán đầu tiên này đã được tạo, chúng sẽ

được gửi đi để xử lý.

Các mã thông báo bây giờ đi vào cơ chế chú ý của máy biến áp.

Về cơ bản, mỗi mã thông báo sẽ xem xét mọi mã thông báo khác trong lời nhắc và có thể thấy cả hai mã thông báo đó.

nghĩa và vị trí của chúng.

Sau đó, mỗi mã thông báo sẽ quyết định mã thông báo nào khác cần chú ý nhất.

Sự chú ý về cơ bản là một cách thú vị để nói những token nào khác sẽ có giá trị lớn nhất

ảnh hưởng đến ý nghĩa của tôi.

Trong một câu, con chó nâu ngồi cạnh con cáo đỏ, từ con chó chắc hẳn sẽ trả giá

chú ý nhiều nhất đến màu nâu và ngồi, vì những từ đó liên quan trực tiếp đến con chó.

Bạn có thể hình dung con chó dành 70% sự chú ý cho màu nâu, 20% cho việc ngồi và phần còn lại

10% được phân bổ cho tất cả các token khác.

Cơ chế được sử dụng để gán sự chú ý này được gọi là đầu chú ý.

Và hầu hết các mô hình thực sự bao gồm nhiều đầu chú ý chuyên về các loại khác nhau

mối quan hệ giữa các từ.

Bạn có thể coi đây là một đầu chú ý chuyên về mối quan hệ giữa

đối tượng và mô tả của chúng.

Vì vậy, từ cáo có thể tập trung toàn bộ sự chú ý vào màu nâu.

Thay vào đó, một đầu chú ý khác có thể chuyên về các mối quan hệ không gian giữa các vật thể.

Và trong cái đầu đó, cáo có thể chú ý nhiều hơn đến việc ngồi và tiếp theo.

Trong thực tế, các mối quan hệ được mỗi người chú ý nắm bắt không phải là một tập hợp rõ ràng

các mối quan hệ do con người ấn định mà là một tập hợp các mối quan hệ phức tạp và trừu tượng

đã học trong quá trình đào tạo người mẫu.

Các mô hình nhỏ hơn có thể sử dụng 8 đến 16 đầu chú ý, nhưng các mô hình lớn hơn có thể sử dụng hơn 100 đầu.

Lý do điều này quan trọng là không chỉ mỗi token theo dõi mối quan hệ của nó với

mọi mã thông báo khác trong văn bản, nhưng chúng thực hiện rất nhiều lần khác nhau, mỗi lần

với một quan điểm hoặc trọng tâm hơi khác một chút.

Kết quả là cơ chế chú ý phát triển một cách trình bày rất chi tiết về các mối quan hệ

giữa tất cả các thẻ trong văn bản.

Sau khi mỗi mã thông báo đã ấn định tất cả điểm chú ý của nó, thông tin sẽ được chuyển tiếp

giai đoạn.

Đây là phần lớn nhất của LLM, nghĩa là nó chứa nhiều tham số nhất.

Dựa trên khả năng nhúng, vị trí và sự chú ý ban đầu của mỗi mã thông báo, nó sẽ chỉ định các cập nhật

nhúng vector cho mỗi mã thông báo.

Các vectơ mới này về cơ bản là dự đoán thứ hai về ý nghĩa thực sự của mỗi mã thông báo, nhưng bây giờ

được thông báo bởi ngữ cảnh của các mã thông báo khác trong văn bản.

Hầu hết các LLM sau đó lặp lại toàn bộ quá trình này.

Các vectơ đoán thứ hai được đưa trở lại cơ chế chú ý và chuyển tiếp, tạo ra

vectơ đoán thứ ba mới và tinh tế hơn về ý nghĩa của từng mã thông báo.

Một LLM điển hình thực sự có thể truyền các vectơ này qua các lớp này ở đâu đó trong khoảng từ 8 đến

64 lần, dần dần hoàn thiện sự hiểu biết của mình ở từng giai đoạn.

Bây giờ LLM đã sẵn sàng để bắt đầu tạo.

Dựa trên các phần nhúng vectơ được tinh chỉnh cao mà nó tạo ra, mô hình sẽ yêu cầu, dựa trên ý kiến của tôi

dữ liệu đào tạo, mã thông báo nào có thể sẽ xuất hiện tiếp theo?

Điều này được tính toán dưới dạng phân phối xác suất trên tất cả các mã thông báo trong từ vựng của mô hình.

Thông thường, một số ít token có khả năng xuất hiện tiếp theo cao.

Nhưng nếu mô hình của bạn nhận ra 100.000 mã thông báo thì mỗi mã sẽ được gán một xác suất ngay cả khi

đại đa số về cơ bản là bằng không.

Cuối cùng, LLM chọn một mã thông báo từ phân phối này, cân nhắc lựa chọn của mỗi mã thông báo.

xác suất được chỉ định của mã thông báo.

Nhiều mã thông báo được chọn thường xuyên hơn, nhưng về lý thuyết, bất kỳ mã thông báo nào cũng có ít nhất một cơ hội nhỏ

về việc được chọn.

Bạn sẽ tìm hiểu thêm về cách điều chỉnh các xác suất này và cách LLM chọn mới

mã thông báo sau trong mô-đun này.

Mã thông báo đã chọn sẽ được thêm vào cuối lời nhắc và sau khi tất cả những điều đó hoạt động, LLM

đã tạo thêm một mã thông báo.

Nếu bạn muốn tạo mã thông báo thứ hai, mô hình phải lặp lại toàn bộ quá trình, chỉ

lần này xem xét cả mã thông báo ban đầu và mã thông báo được thêm vào.

Điều này đảm bảo các token mới có ý nghĩa trong bối cảnh của cả token gốc và

những cái nó tạo ra.

Điều này có nghĩa là các lựa chọn mã thông báo ngẫu nhiên sớm sẽ ảnh hưởng đến mã thông báo nào được chọn sau này vì

tốt.

Để tạo ra sự hoàn thành đầy đủ, mô hình thực hiện quá trình này lặp đi lặp lại cho đến khi nó

đạt đến giới hạn mã thông báo bạn đã đặt cho lần hoàn thành đó hoặc chọn tạo

một mã thông báo kết thúc hoàn thành đặc biệt cho biết rằng công việc đã hoàn tất.

Các mã thông báo mà LLM tạo ra có thể hoàn thành một cụm từ hoặc một câu trả lời cho một câu hỏi, nhưng bất kể điều gì

mục đích của chúng, chúng có thể được khử mã thông báo thành văn bản thuần túy và trả lại cho người dùng.

Đó là một hành trình khá thú vị thông qua LLM.

Vì vậy, hãy xem các bộ phận của kiến trúc máy biến áp này thúc đẩy nhiều yếu tố của

thiết kế hệ thống RAG

Đầu tiên, nó giúp thúc đẩy lý do tại sao RAG hoạt động ngay từ đầu.

LLM có thể hiểu sâu sắc ý nghĩa và mức độ liên quan của thông tin được thêm vào

lời nhắc.

Điều này là nhờ quá trình xử lý được thực hiện bởi cơ chế quan tâm và kiến thức thế giới

chứa trong các lớp tiếp liệu.

Thứ hai, nó nhấn mạnh rằng LLM vốn dĩ vẫn mang tính chất ngẫu nhiên.

Ngay cả khi bạn đưa thông tin có ý nghĩa vào lời nhắc của mình, LLM có thể ngẫu nhiên chọn không

để tạo văn bản dựa trên thông tin đó.

Kiểm soát tính ngẫu nhiên này và xác nhận LLM của bạn căn cứ vào các câu trả lời được truy xuất

thông tin vẫn cần thiết và quan trọng.

Thứ ba, nó chỉ nêu bật mức độ tốn kém về mặt tính toán của LLM.

Việc tạo một mã thông báo mất rất nhiều thời gian xử lý và chi phí đó thực sự tăng theo thời gian

của lời nhắc hoặc hoàn thành.

Rốt cuộc, mỗi mã thông báo cần phải xem xét từng mã thông báo khác để hiểu đầy đủ ý nghĩa của chính nó.

Như bạn sẽ khám phá sau, hầu hết chi phí từ việc chạy hệ thống RAG đều đến từ việc chạy các hệ thống mạnh mẽ này.

nhưng những mẫu máy biến áp đắt tiền.

Đó là một bản tóm tắt hay về cách hoạt động của LLM.

Bây giờ chúng ta hãy chuyển sự chú ý của chúng ta, không có ý định chơi chữ, sang cách bạn có thể tinh chỉnh hành vi của họ bên trong