# 07 giới thiệu-truy xuất thông tin

---

Tại thời điểm này, mục đích của chó săn có lẽ đã khá rõ ràng.

Nó cần cung cấp thông tin hữu ích cho LLM mà có khả năng không có sẵn

khi mô hình được huấn luyện. Bây giờ chúng ta hãy xem thành phần này thực sự hoạt động như thế nào.

Hãy bắt đầu với một sự tương tự. Hãy tưởng tượng bạn đang vào thư viện để trả lời câu hỏi,

làm cách nào tôi có thể làm bánh pizza kiểu New York tại nhà? Tôi biết, tôi biết, có lẽ bạn vừa tra cứu cái này

trực tuyến, và thành thật mà nói, tôi cũng vậy. Nhưng hãy sử dụng phép ẩn dụ vì tôi nghĩ hình ảnh

hữu ích. Thư viện có một bộ sưu tập lớn sách về nhiều chủ đề. Để giúp bạn duyệt qua

sưu tập, sách được sắp xếp theo từng phần và kệ dựa trên đặc điểm của chúng.

chủ đề, thể loại, tác giả, v.v. Nếu bạn chia sẻ câu hỏi của mình với thủ thư, họ có thể giúp bạn

bạn tìm thấy các phần của thư viện hoặc thậm chí những cuốn sách chính xác phù hợp nhất với bạn

câu hỏi. Chó tha mồi có nhiều thành phần tương tự. Nơi thư viện có một bộ sưu tập sách,

một con chó tha mồi có một nền tảng kiến thức về tài liệu. Tương tự, một trình thu hồi sẽ tạo một chỉ mục của

các tài liệu trong cơ sở tri thức, giúp giữ cho các tài liệu được tổ chức và làm cho chúng

dễ dàng tìm kiếm. Bước tiếp theo là thực sự lấy thông tin liên quan. Trong thư viện,

bạn chỉ có thể hỏi trực tiếp thủ thư. Cán bộ thư viện có thể hiểu được ý nghĩa của

câu hỏi của bạn và biết hãy tìm trong các phần của thư viện về nấu ăn hoặc ẩm thực Ý hoặc

có thể là New York. Khả năng diễn giải ý nghĩa câu hỏi của bạn cho phép họ xác định

các kệ bên phải của thư viện để tìm kiếm và cuối cùng tìm thấy những cuốn sách có liên quan.

Bên trong hệ thống RAG, chó tha mồi cũng làm điều tương tự. Đầu tiên nó cần xử lý lời nhắc để

hiểu ý nghĩa cơ bản của nó. Sau đó nó sử dụng sự hiểu biết đó để tìm kiếm chỉ mục của tài liệu.

Sau đó, bộ thu hồi sẽ trả về các tài liệu từ cơ sở tri thức mà nó xác định là tốt nhất.

có liên quan đến lời nhắc. Khi hoàn tất quá trình tìm kiếm, trình truy xuất sẽ xếp các tài liệu theo thứ tự

cơ sở kiến thức bằng mức độ liên quan của chúng với lời nhắc. Mỗi tài liệu nhận được một số điểm

định lượng sự liên quan của nó. Thông thường điều này có nghĩa là một số thước đo về sự giống nhau giữa văn bản

của lời nhắc và văn bản của tài liệu. Những tài liệu có điểm cao nhất là những tài liệu

được trả lại. Có nhiều cách tiếp cận khác nhau để tính điểm tương đồng này

mà bạn sẽ tìm hiểu thêm sau này trong khóa học. Tất nhiên, một chú chó tha mồi được thiết kế tốt sẽ quay trở lại

những giấy tờ liên quan nhưng cũng cần phải giữ lại những giấy tờ không liên quan. Nếu bạn hỏi thông tin

về việc làm bánh pizza kiểu New York tại nhà và chú chó săn đã trả lời bằng tất cả tài liệu trong

cơ sở kiến thức, về mặt kỹ thuật thì bạn có mọi tài liệu liên quan nhưng nó sẽ bị thất lạc trong núi

của những thông tin không liên quan. Như bạn đã thấy trước đó, điều này cũng sẽ dẫn đến những lời nhắc tốn kém hoặc thậm chí hoàn toàn

sử dụng hết cửa sổ ngữ cảnh của LLM. Mặt khác, nếu bạn chỉ truy xuất các tài liệu được xếp hạng cao nhất

trong cơ sở kiến thức, bạn có thể bỏ lỡ thông tin có giá trị liên quan trong các tài liệu được xếp hạng

thứ hai, thứ ba hoặc thứ tư. Trong một thế giới hoàn hảo, chú chó săn xếp hạng các tài liệu một cách hoàn hảo

và chọn đúng số lượng chúng để trả về. Tuy nhiên, trong thực tế, bạn biết chó săn

đôi khi sẽ xếp hạng một số tài liệu liên quan quá thấp và xếp hạng một số tài liệu không liên quan khác

cao, gây khó khăn cho việc quyết định một cách tự tin có bao nhiêu người trong số họ sẽ quay trở lại. Để tối ưu hóa chó tha mồi

hiệu suất, bạn sẽ cần theo dõi nó theo thời gian và thử nghiệm với các cài đặt khác nhau, điều gì đó

bạn sẽ thấy rộng rãi trong khóa học này. Điều đáng chú ý là nhiều phần mềm quen thuộc

thực hiện các nhiệm vụ rất giống với một con chó tha mồi. Công cụ tìm kiếm web truy xuất các trang web có liên quan

vào tìm kiếm trên web và cơ sở dữ liệu quan hệ truy xuất các hàng và bảng khớp với truy vấn SQL.

Lĩnh vực truy xuất thông tin rộng hơn đã trưởng thành khi các mô hình ngôn ngữ lớn lần đầu tiên được

đã được phát triển và các ý tưởng từ lĩnh vực này là nền tảng cho cách thức thiết kế các hệ thống RAG và chó tha mồi.

Về lý thuyết, có rất nhiều cách để triển khai công cụ truy tìm trong hệ thống RAG.

Vì hầu hết các công ty đã có dữ liệu của họ trong cơ sở dữ liệu quan hệ truyền thống,

thật tốt khi giữ dữ liệu ở đó và tìm ra cách truy xuất từ cơ sở dữ liệu đó sang nguồn điện

một hệ thống RAG. Mặc dù chúng không thực sự cần thiết nhưng ở quy mô lớn, hầu hết các chú chó tha mồi sẽ được xây dựng dựa trên

cơ sở dữ liệu vectơ, một loại cơ sở dữ liệu chuyên dụng được tối ưu hóa để tìm kiếm tài liệu nhanh chóng

trong cơ sở kiến thức của bạn phù hợp nhất với lời nhắc. Trong khóa học này, bạn sẽ tìm hiểu về cả hai

nguyên tắc chung về truy xuất thông tin hỗ trợ nhiều công nghệ tìm kiếm

và cơ sở dữ liệu vectơ thường được sử dụng làm công cụ truy xuất bên trong hệ thống RAG quy mô sản xuất.

Còn rất nhiều điều cần tìm hiểu về chó tha mồi, nhưng hiện tại,

bao gồm những điểm quan trọng nhất. Hãy tham gia cùng tôi trong video tiếp theo và kết thúc mô-đun này.