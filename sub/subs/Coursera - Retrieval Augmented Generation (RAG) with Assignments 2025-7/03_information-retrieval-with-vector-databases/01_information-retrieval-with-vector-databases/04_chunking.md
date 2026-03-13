# 04 phân đoạn

---

Như bạn vừa thấy, cơ sở dữ liệu vectơ có kiến ​​trúc và API được tối ưu hóa để truy xuất vectơ.

Thật đơn giản để thiết lập cơ sở dữ liệu có quy mô nhanh chóng

và thực hiện nhiều loại tìm kiếm khác nhau mà bạn đã thấy trong suốt khóa học này.

Trong hầu hết các hệ thống giá sản xuất, bạn sẽ muốn thêm một số điều chỉnh bổ sung cho việc truy xuất vectơ

để tối ưu hóa hiệu suất hệ thống tổng thể của bạn.

Trong một số video tiếp theo, tôi sẽ hướng dẫn bạn một số chiến lược đó, bắt đầu bằng việc chia nhỏ.

Nói một cách đơn giản, chunking là thực hành chia nhỏ các tài liệu văn bản dài hơn khỏi cơ sở kiến thức của bạn

thành các đoạn văn bản nhỏ hơn.

Lý do bạn làm điều đó là gấp ba lần.

Thứ nhất, nhiều mô hình nhúng có giới hạn về số lượng văn bản mà chúng có thể nhúng vào vectơ.

Thứ hai, phân đoạn có thể cải thiện các số liệu liên quan đến tìm kiếm cho trình truy xuất của bạn.

Và thứ ba, nó đảm bảo bạn chỉ gửi văn bản phù hợp nhất từ ​​tài liệu đến LLM.

Để hiểu giá trị của việc phân chia dữ liệu, hãy tưởng tượng bạn có nền tảng kiến ​​thức gồm hàng nghìn cuốn sách.

Nếu bạn lập chỉ mục cơ sở kiến thức này, mỗi cuốn sách sẽ được vector hóa bằng mô hình nhúng

và kết quả sẽ là một nghìn vectơ, mỗi vectơ biểu thị bối cảnh của một cuốn sách.

Vấn đề ở đây là bạn đang nén ý nghĩa của toàn bộ cuốn sách xuống một vectơ duy nhất.

Các vectơ này không thể thể hiện rõ ràng bất kỳ chủ đề cụ thể nào được thảo luận trong một chương cụ thể

hoặc trang, và thay vào đó là mức trung bình của tất cả chúng.

Kết quả là bạn cho rằng mức độ liên quan của tìm kiếm sẽ khá kém.

Ngay cả khi bạn sử dụng hệ thống này để truy xuất, bạn sẽ truy xuất toàn bộ cuốn sách cùng một lúc,

sẽ nhanh chóng lấp đầy cửa sổ ngữ cảnh LLM của bạn.

Vì lý do này, bạn thường muốn lấy sách của mình ra và chia chúng thành những phần nhỏ hơn,

như trang, đoạn văn hoặc cấp độ câu.

Đột nhiên, cơ sở kiến thức của bạn có thể chứa 1 triệu đoạn văn thay vì 1.000 cuốn sách,

nhưng cơ sở dữ liệu vectơ dễ dàng mở rộng quy mô để lưu trữ và tìm kiếm trong tất cả các vectơ đó.

Việc cân nhắc đầu tiên khi chunking là sử dụng kích thước chunk nào.

Nếu bạn tạo các phần quá lớn, chẳng hạn ở cấp độ chương,

bạn gặp phải vấn đề tương tự như khi cố gắng vector hóa toàn bộ cuốn sách.

Các khối vẫn còn quá lớn để nắm bắt được ý nghĩa sắc thái bằng một vectơ duy nhất,

và chúng sẽ nhanh chóng lấp đầy cửa sổ ngữ cảnh của LLM.

Ngoài ra, cũng có thể tạo khối quá nhỏ.

Hãy xem xét trường hợp cực đoan khi bạn phân đoạn ở cấp độ từ.

Các vectơ của bạn sẽ mất toàn bộ ngữ cảnh của các câu và đoạn văn xung quanh,

điều này một lần nữa làm giảm mức độ liên quan của tìm kiếm.

Ngay cả việc phân đoạn ở cấp độ câu cũng có thể quá chi tiết.

Không có cách tiếp cận nào phù hợp cho tất cả đối với kích thước khối,

nhưng thông thường bạn sẽ thấy sự cân bằng giữa các vectơ cố gắng nắm bắt quá nhiều

hoặc quá ít bối cảnh cùng một lúc.

Cách đơn giản nhất để làm điều này là sử dụng chiến lược chunking có kích thước cố định

ngay từ đầu bạn xác định rằng mọi khối sẽ có cùng kích thước.

Ví dụ: 250 ký tự.

Ký tự từ 1 đến 250 là đoạn 1.

251 đến 500 là đoạn 2.

501 đến 750 là đoạn 3, v.v.

cho đến hết tài liệu.

Tất nhiên, không có gì đảm bảo sự phân chia giữa các phần xảy ra ở những nơi hợp lý.

Sự phân chia thường sẽ rơi vào giữa một từ

hoặc tách hai phần của một ý tưởng gắn kết trong một đoạn văn.

Điều này thường được giải quyết bằng cách cho phép chồng chéo theo từng khối.

Ví dụ: các đoạn có thể dài 250 ký tự,

nhưng chồng lên nhau 25 ký tự với các đoạn trước và sau.

Vì vậy đoạn 1 là các ký tự từ 1 đến 250.

Đoạn 2 là 226 đến 475.

Đoạn 3 là 451 đến 700, v.v.

Thông thường, sự chồng chéo này được biểu thị bằng phần trăm của toàn bộ đoạn.

Vì vậy, ở đây, đây sẽ là sự trùng lặp 10%.

Các đoạn chồng chéo giúp giảm thiểu trường hợp các từ bị cắt khỏi ngữ cảnh của chúng.

Các từ ở giữa đoạn có ngữ cảnh ở hai bên.

Các từ ở cạnh các khối sẽ xuất hiện thành hai khối,

tăng khả năng chúng xuất hiện cùng với bối cảnh có liên quan.

Việc cho phép chồng chéo nhiều hơn thường tác động tích cực đến mức độ liên quan của tìm kiếm,

nhưng phải trả giá bằng việc thêm nhiều vectơ vào cơ sở dữ liệu của bạn với thông tin dư thừa.

Một chiến lược phân đoạn năng động hơn được gọi là phân tách văn bản ký tự đệ quy.

Ý tưởng là bạn chọn một nhân vật cụ thể để phân chia.

Ví dụ: bạn có thể phân chia ký tự dòng mới,

thường xuất hiện giữa các đoạn văn.

Điều này cung cấp cho bạn kích thước khối thay đổi,

vì vậy có nhiều khả năng bạn có những khối rất lớn hoặc rất nhỏ

tùy thuộc vào vị trí ký tự dòng mới.

Tuy nhiên, về mặt tích cực, bạn đang tính đến cấu trúc tài liệu

và tăng khả năng các khái niệm liên quan được lưu giữ cùng nhau trong một đoạn duy nhất.

Nếu cơ sở kiến thức của bạn có nhiều loại tài liệu khác nhau,

tất nhiên bạn có thể phân chia các loại tài liệu khác nhau một cách khác nhau.

Ví dụ: bạn có thể chia HTML thành các thẻ đoạn văn hoặc tiêu đề,

Mã Python trên định nghĩa hàm và tài liệu văn bản trên các ký tự dòng mới.

Đã sửa lỗi phân đoạn kích thước bị chồng chéo hoặc phân đoạn trên các ký tự cụ thể

rất đơn giản nên bạn có thể tự làm được.

Nhưng bạn cũng có thể tìm thấy các thư viện bên ngoài được thiết kế để giúp bạn thực hiện điều đó.

Nếu tài liệu của bạn có siêu dữ liệu,

tất nhiên bạn sẽ muốn các đoạn kế thừa siêu dữ liệu của tài liệu nguồn,

có lẽ với thông tin bổ sung về vị trí của họ.

Bạn sẽ thấy các ví dụ về cách thực hiện điều này trong các phòng thí nghiệm chưa được phân loại trong mô-đun này.

Việc chia nhỏ tài liệu của bạn mang lại nhiều lợi ích cho việc truy xuất vectơ,

từ việc tăng mức độ liên quan của tìm kiếm đến giảm thiểu việc sử dụng cửa sổ ngữ cảnh LLM của bạn.

Nếu bạn đang tìm kiếm một điểm khởi đầu tốt,

chỉ cần sử dụng các đoạn có kích thước cố định khoảng 500 ký tự với khoảng chồng chéo từ 50 đến 100 ký tự.

Trong một số trường hợp khác, các kỹ thuật phân đoạn nâng cao hơn có thể hữu ích,

vì vậy hãy cùng tôi xem video tiếp theo để khám phá xem một số trong số đó trông như thế nào.