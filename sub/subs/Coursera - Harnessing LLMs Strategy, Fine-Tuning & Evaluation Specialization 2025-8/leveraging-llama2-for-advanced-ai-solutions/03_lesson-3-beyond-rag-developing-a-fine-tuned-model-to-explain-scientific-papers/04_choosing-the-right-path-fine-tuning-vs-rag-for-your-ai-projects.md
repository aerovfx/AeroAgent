# 04 lựa chọn con đường phù hợp-tinh chỉnh-vs-rag-cho-dự án ai của bạn

---

Không chắc chắn khi nào cần tinh chỉnh hoặc

triển khai giải pháp RAG?

Vâng, trong video này,

bạn sẽ tìm hiểu về những ưu và

nhược điểm của từng phương pháp để giúp bạn thực hiện

lời kêu gọi đúng đắn cho các dự án trong thế giới thực của bạn.

Và đến cuối video, bạn sẽ

có thể đánh giá khi nào nên sử dụng tinh chỉnh hoặc

xây dựng giải pháp RAG dựa trên

trên những yêu cầu đã cho.

Bạn cũng sẽ có thể hiểu được

điểm mạnh và hạn chế của từng phương pháp.

Xác định các trường hợp sử dụng nơi sử dụng

một cách tiếp cận kết hợp cũng sẽ được

một cái gì đó đơn giản với bạn

Hãy cùng tìm hiểu cách bạn có thể điều chỉnh

mô hình AI của bạn theo nhu cầu riêng của bạn

bằng cách chọn đúng

kỹ thuật tối ưu hóa.

Khi nào nên sử dụng kỹ thuật tối ưu hóa nào?

Giảm thiểu ảo giác,

ngăn chặn ảo giác là rất quan trọng trong

các ứng dụng trong đó độ chính xác là tối quan trọng

như các mô hình ngôn ngữ lớn thường chế tạo

chi tiết mà không có cơ sở thực tế.

Tinh chỉnh thực sự có thể làm giảm

ảo giác bằng cách nối đất mô hình trong

dữ liệu cụ thể của miền,

nhưng nó vẫn đòi hỏi phải liên tục

đào tạo lại để giảm thiểu kết quả đầu ra sai.

Mặt khác, hệ thống RAG

có hiệu quả hơn trong việc ngăn ngừa

ảo giác vì họ dựa vào

thu thập bằng chứng để tạo ra phản hồi.

Bằng cách căn cứ từng câu trả lời

trong kiến thức bên ngoài,

Hệ thống RAG vốn đã giảm

nguy cơ bịa đặt,

làm cho chúng trở nên lý tưởng cho

những tình huống mà sự trung thực là rất quan trọng.

Dữ liệu đào tạo, sự sẵn có của

Dữ liệu huấn luyện là yếu tố then chốt khi nó

phải lựa chọn giữa RAG hoặc

tinh chỉnh.

Việc tinh chỉnh phụ thuộc rất nhiều vào

một tập dữ liệu phong phú để điều chỉnh mô hình

tới một nhiệm vụ hoặc lĩnh vực cụ thể, tạo ra

phản hồi chính xác và phù hợp hơn.

Tuy nhiên, với dữ liệu hạn chế hoặc chất lượng thấp,

tinh chỉnh có thể cung cấp tối thiểu

cải tiến hoặc thậm chí có nguy cơ bị trang bị quá mức.

Ngược lại, hệ thống RAG không

phụ thuộc vào dữ liệu được dán nhãn rộng rãi như

họ lấy thông tin

từ các nguồn bên ngoài.

Điều này làm cho giải pháp RAG trở nên mạnh mẽ

thay thế khi dữ liệu khan hiếm,

đảm bảo mô hình luôn được thông tin và

có liên quan theo ngữ cảnh.

Dữ liệu động, bản chất động của dữ liệu

là rất quan trọng khi quyết định giữa RAG và

tinh chỉnh.

Tinh chỉnh tạo ra trạng thái tĩnh

ảnh chụp nhanh kiến thức của mô hình

dựa trên dữ liệu huấn luyện vào thời điểm đó,

nghĩa là mô hình có thể nhanh chóng trở thành

lỗi thời nếu dữ liệu thường xuyên thay đổi.

Việc duy trì mô hình hiện tại sẽ

cần phải đào tạo lại thường xuyên,

việc này tốn thời gian và

thâm dụng tài nguyên.

Mặt khác, hệ thống RAG tốt hơn

phù hợp với môi trường dữ liệu động.

Họ liên tục kéo mới nhất

thông tin từ các nguồn bên ngoài,

đảm bảo các câu trả lời luôn được cập nhật

mà không cần phải đào tạo lại liên tục.

Nếu dữ liệu của bạn đang phát triển nhanh chóng,

RAG mang lại sự linh hoạt

tinh chỉnh không thể dễ dàng phù hợp.

Các trường hợp sử dụng, hãy cùng khám phá cách chúng

kỹ thuật thực hiện trong các tình huống khác nhau.

Ví dụ: hệ thống RAG vượt trội trong việc tạo

Hệ thống hỏi đáp cần lấy thông tin

từ cơ sở dữ liệu cập nhật liên tục

giống như Sharepoint của một tổ chức.

Và trong trường hợp này,

mô hình làm giảm nguy cơ ảo giác và

vẫn chính xác với mức tối thiểu

yêu cầu đào tạo lại.

Tuy nhiên, nó có thể gặp khó khăn với

sắc thái cụ thể của miền và

phong cách ngôn ngữ học đó

tinh chỉnh vượt trội trong việc chụp.

Mặt khác, việc tinh chỉnh

thực sự tỏa sáng trong những tình huống mà bạn

cần tự động hóa các tác vụ dựa trên văn bản

đòi hỏi sự hiểu biết sâu sắc về

một miền cụ thể,

chẳng hạn như trong thực tiễn pháp lý.

Việc tinh chỉnh cho phép

thích ứng sâu sắc với phong cách mong muốn và

sắc thái phức tạp của tên miền,

miễn là có đủ cao

dữ liệu đào tạo chất lượng có sẵn.

Cuối cùng, trong những trường hợp như

tự động hóa hỗ trợ khách hàng,

một cách tiếp cận kết hợp thường hoạt động tốt nhất.

Vì vậy việc tinh chỉnh có thể đảm bảo rằng chatbot

phù hợp với thương hiệu của công ty và

giọng điệu và kiến thức chung,

xử lý hầu hết các yêu cầu thông thường của khách hàng.

Trong khi đó, RAG bước vào

yêu cầu năng động hơn hoặc cụ thể hơn,

đảm bảo rằng chatbot có được thông tin mới nhất

thông tin từ các tài liệu của công ty hoặc

cơ sở dữ liệu và giảm thiểu ảo giác.

Sự kết hợp này mang lại sự toàn diện,

kịp thời,

và thương hiệu nhất quán

kinh nghiệm hỗ trợ khách hàng.

Tóm lại là chọn đúng

kỹ thuật tối ưu hóa là cần thiết cho

căn chỉnh mô hình AI của bạn

với yêu cầu của bạn.

Cho dù đó là tinh chỉnh,

xây dựng giải pháp RAG, hoặc

có thể theo một cách tiếp cận kết hợp,

mỗi người đều có điểm mạnh và điểm yếu riêng.

Bằng cách hiểu rõ những kỹ thuật này,

bạn có thể đảm bảo mô hình của mình hoạt động tốt nhất

trong mỗi kịch bản thế giới thực nhất định.

Hãy dành thời gian để suy nghĩ về một tiềm năng

dự án bạn có thể bắt đầu và

kỹ thuật tối ưu hóa nào

sẽ phù hợp nhất.

Hãy xem xét cách bạn có thể áp dụng những gì bạn

đã học trong khóa học này để đạt được

kết quả tốt nhất.

Xin chân thành cảm ơn các bạn đã xem và

bây giờ tôi có một câu hỏi cuối cùng cho bạn.

[ÂM NHẠC]