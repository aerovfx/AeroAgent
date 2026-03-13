# 01 tác nhân hiểu-phản xạ

---

[ÂM NHẠC]

Chào mừng bạn đến với video này để tìm hiểu về tác nhân Phản xạ.

Trong video này, bạn sẽ phân tích cách các tác nhân Phản xạ cải thiện phản hồi của AI

thông qua việc tự phê bình lặp đi lặp lại và sử dụng công cụ.

Bạn sẽ áp dụng các vai trò trình tạo và phản xạ trong quy trình làm việc Phản xạ,

tích hợp thông tin thời gian thực bằng các công cụ bên ngoài,

và cấu trúc kết quả đầu ra để bao gồm các trích dẫn và tài liệu tham khảo để có tính minh bạch cao hơn.

Trong video này về tác nhân Phản xạ bằng LangGraph, hãy nhớ rằng sự khác biệt không chỉ ở chữ "X".

Tác nhân phản xạ được xây dựng trên ý tưởng về tác nhân phản xạ,

trong đó lặp đi lặp lại xem xét và tinh chỉnh kết quả đầu ra.

Họ tiến xa hơn bằng cách đưa ra những câu trả lời có trích dẫn, thông tin hiện tại,

và những tuyên bố có thể kiểm chứng được thay vì chỉ là những ý kiến được cải thiện.

Đây là một đánh giá nhanh về quá trình phản ánh.

Một truy vấn như "Tôi cần nhiều khoáng chất hơn trong chế độ ăn uống của mình" sẽ bước vào một chu kỳ hình thành và suy ngẫm.

Việc qua lại tiếp tục cho đến khi đạt đến điểm dừng hợp lý.

Cuối cùng, hệ thống tạo ra phản hồi như,

"Để tăng khoáng chất trong chế độ ăn uống của bạn, hãy thử ăn các loại thực phẩm như rau bina (sắt và magie),

hạnh nhân (magie) và các sản phẩm từ sữa (canxi).

Nhưng điều gì sẽ xảy ra nếu nghiên cứu mới được đưa ra sau khi mô hình đã được huấn luyện?

Đây là lúc Phản xạ xuất hiện.

Nó cho phép hệ thống học hỏi từ thông tin mới, đánh giá các phản hồi trong quá khứ,

và liên tục cải thiện ngay cả sau đào tạo.

Đây là lý do tại sao Reflexion được coi là một khuôn khổ mạnh mẽ để xây dựng các tác nhân thông minh hơn.

Về cốt lõi, Reflexion được thiết kế để hỗ trợ các tác nhân tự cải thiện.

Những tác nhân này không chỉ phản ánh một lần.

Họ liên tục phân tích hiệu suất của chính họ,

học hỏi và trở nên tốt hơn qua mỗi lần lặp lại.

Một trong những điểm mạnh chính của họ là khả năng tìm ra và khắc phục điểm yếu của bản thân.

Sau mỗi lần chạy, nhân viên sẽ phản ánh những gì đã xảy ra

và điều chỉnh lý luận hoặc chiến lược của mình trước khi thử lại.

Họ cũng có khả năng kết hợp thông tin bên ngoài.

Bằng cách gọi các công cụ như tìm kiếm trên web hoặc API,

Tác nhân phản xạ có thể mang lại dữ liệu thời gian thực

để cải thiện mức độ liên quan và độ chính xác của lần thử tiếp theo của họ.

Và cuối cùng, các tác nhân Phản xạ có thể hỗ trợ và biện minh cho kết quả đầu ra của họ.

Nhờ chu kỳ phản ánh, họ có thể sao lưu phản hồi của mình bằng các trích dẫn

hoặc giải thích rõ ràng lý do đằng sau câu trả lời của họ.

Hãy hiểu Reflexion, một phương pháp cải thiện phản hồi LLM.

Bắt đầu bằng một truy vấn.

"Tôi cần nhiều khoáng chất hơn trong chế độ ăn uống của mình."

Bộ tạo hoặc bộ phản hồi LLM tạo ra phản hồi ban đầu.

Lời nhắc hệ thống sẽ đặt vai trò.

Ví dụ: "Bạn là huấn luyện viên thể hình".

Yêu cầu LLM phê bình kết quả đầu ra của chính mình.

Cung cấp đầu vào công cụ, chẳng hạn như truy vấn tìm kiếm, để tinh chỉnh phản hồi.

Một thông báo hệ thống có cấu trúc sẽ hướng dẫn toàn bộ quá trình.

Để giúp mô hình phân biệt giữa đầu ra của công cụ và phản hồi của chính nó,

đầu ra được định dạng rõ ràng.

Mỗi phần đều được dán nhãn, bao gồm phản hồi, phê bình và truy vấn để tránh sự mơ hồ.

Thay vì trả về văn bản thuần túy,

LLM xuất ra một đối tượng có cấu trúc dựa trên lược đồ hoặc mô hình dữ liệu đã xác định.

Truy vấn của người dùng được chuyển đến người trả lời.

Thay vì trả về văn bản thô, LLM xuất ra một đối tượng có cấu trúc.

Đối tượng này tuân theo một lược đồ, được biểu diễn dưới dạng bảng.

Mỗi trường, như phản hồi và truy vấn, ánh xạ tới một thuộc tính của đối tượng.

Toàn bộ cấu trúc này trở thành một thông điệp AI.

Đầu ra của phản hồi được chuyển tới công cụ tìm kiếm.

Công cụ này trích xuất truy vấn tìm kiếm từ kết quả đầu ra của người trả lời.

Đồng thời, HumanMessage và AIMessage từ người trả lời

được lưu vào danh sách có tên là reply_list.

Với mỗi truy vấn, công cụ sẽ trả về thông tin.

Ví dụ: nó có thể bao gồm tiêu đề, nội dung và URL.

Ở đây, một kết quả tìm kiếm được hiển thị, nhưng đây là thông số bạn có thể quyết định.

Bạn cũng thêm kết quả cuộc gọi công cụ vào danh sách phản hồi.

Công cụ sẽ chuyển kết quả đầu ra này tới người sửa đổi thông qua danh sách phản hồi.

Người sửa đổi sẽ sử dụng danh sách phản hồi, đặc biệt là phần tự phê bình của người phản hồi.

Bộ chỉnh sửa sửa đổi đầu vào từ bộ phản hồi bằng cách sử dụng đầu ra của công cụ.

Sau đó, nó tuân theo một bộ hướng dẫn để sửa lại phản hồi,

kết hợp các trích dẫn từ công cụ và thêm tài liệu tham khảo cho các trích dẫn.

Giống như trình tạo, trình chỉnh sửa sẽ đưa ra phản hồi.

Ví dụ: đề xuất thực phẩm giàu khoáng chất nhưng có thêm tài liệu tham khảo.

Giống như phản hồi, nó sử dụng cùng một lược đồ, được biểu diễn dưới dạng bảng.

Điều này bao gồm phản hồi đã sửa đổi, tài liệu tham khảo,

tự phê bình và tập truy vấn tìm kiếm tiếp theo.

Điểm khác biệt chính là phản hồi hiện bao gồm các tài liệu tham khảo đã được tinh chỉnh.

Đầu ra của trình sửa đổi được chuyển tới công cụ và các truy vấn tìm kiếm được trích xuất.

Đầu ra cũng được lưu trữ trong phản hồi của công cụ.

Phản hồi của công cụ được trình sửa đổi xử lý và thêm vào danh sách phản hồi.

Danh sách phản hồi cũng bao gồm các thông báo AI của người sửa đổi trước đây.

Quá trình này lặp đi lặp lại nhiều lần.

Trình sửa đổi chuyển đầu ra của nó trở lại công cụ, sau đó cập nhật phản hồi.

Chu kỳ này tiếp tục với số lần lặp được xác định trước cho đến khi bạn nhận được kết quả đầu ra.

Trong video này, bạn đã học được rằng:

Tác nhân phản xạ được xây dựng trên tác nhân phản xạ bằng cách lặp đi lặp lại

cải thiện phản hồi bằng cách tự phê bình, công cụ bên ngoài và trích dẫn.

Quá trình phản ánh bao gồm một vòng lặp sáng tạo, phê bình,

và sửa đổi để nâng cao tính rõ ràng, chính xác và hữu ích.

Tác nhân phản xạ có thể xác định và khắc phục điểm yếu của chính mình,

cải thiện theo từng chu kỳ bằng cách phân tích các kết quả đầu ra trước đó.

Họ có thể kết hợp dữ liệu thời gian thực bằng cách gọi các công cụ bên ngoài

như API tìm kiếm trên web, nâng cao mức độ liên quan của phản hồi.

Đầu ra dựa trên lược đồ có cấu trúc giúp các tác nhân phân biệt

giữa các thành phần khác nhau như phản hồi, phê bình và truy vấn công cụ.

Bộ phản hồi tạo ra kết quả đầu ra với các trường như truy vấn và phản hồi,

những thành phần hạ nguồn như bộ sửa đổi có thể xây dựng trên đó.

Trình sửa đổi tinh chỉnh phản hồi bằng cách sửa đổi nó, tích hợp các đầu ra của công cụ,

và thêm tài liệu tham khảo để hỗ trợ các yêu cầu.

Toàn bộ quá trình này hoạt động theo một chu trình lặp đi lặp lại

với kết quả đầu ra và phản hồi được truyền qua các công cụ

và được lưu trữ trong danh sách phản hồi trong các lần chạy.

[ÂM NHẠC]