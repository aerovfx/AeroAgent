# 04 rlhf-lấy-phản hồi-từ-con người

---

Bước đầu tiên trong việc tinh chỉnh LLM với

RLHF là chọn một mô hình để làm việc và

sử dụng nó để chuẩn bị một tập dữ liệu cho

phản hồi của con người.

Mẫu bạn chọn phải có một số

khả năng thực hiện nhiệm vụ mà bạn

quan tâm đến việc đây có phải là văn bản không

tóm tắt, trả lời câu hỏi hoặc

một cái gì đó khác.

Nói chung, bạn có thể thấy dễ dàng hơn

để bắt đầu với một mô hình hướng dẫn

đã được tinh chỉnh trên nhiều

nhiệm vụ và có một số khả năng chung.

Sau đó bạn sẽ sử dụng LLM này cùng với

một tập dữ liệu nhanh chóng để tạo ra một số

câu trả lời khác nhau cho mỗi lời nhắc.

Tập dữ liệu nhanh chóng là

bao gồm nhiều lời nhắc,

mỗi trong số đó được xử lý bởi LLM

để tạo ra một bộ hoàn thành.

Bước tiếp theo là thu thập

phản hồi từ người dán nhãn trên

sự hoàn thành do LLM tạo ra.

Đây là phần phản hồi của con người

học tăng cường với con người

phản hồi.

Đầu tiên bạn phải quyết định tiêu chí nào

bạn muốn con người đánh giá

sự hoàn thành trên.

Đây có thể là bất kỳ vấn đề nào được thảo luận

cho đến nay như sự hữu ích hoặc độc hại.

Khi bạn đã quyết định rồi, bạn sẽ hỏi

người dán nhãn sẽ đánh giá mỗi lần hoàn thành

trong tập dữ liệu dựa trên tiêu chí đó.

Chúng ta hãy xem một ví dụ.

Trong trường hợp này, lời nhắc là,

nhà tôi nóng quá.

Bạn chuyển lời nhắc này tới LLM,

sau đó tạo ra ba

hoàn thiện khác nhau.

Nhiệm vụ của người dán nhãn của bạn là

để xếp hạng ba lần hoàn thành trong

thứ tự hữu ích nhất

hữu ích đến ít hữu ích nhất.

Vì vậy, ở đây người dán nhãn có thể sẽ quyết định

việc hoàn thành hai là hữu ích nhất.

Nó cho người dùng biết điều gì đó

thực sự có thể làm mát ngôi nhà của họ và

được xếp hạng là hoàn thành đầu tiên.

Không hoàn thành một hoặc

ba đều rất hữu ích, nhưng

có thể người dán nhãn sẽ quyết định

ba là điều tồi tệ nhất

cả hai vì người mẫu tích cực

không đồng ý với đầu vào từ người dùng.

Vì vậy người dán nhãn xếp hạng mức độ hoàn thành cao nhất

thứ hai và lần hoàn thành cuối cùng thứ ba.

Quá trình này sau đó được lặp lại cho

nhiều bộ hoàn thành nhanh chóng,

xây dựng một bộ dữ liệu có thể

được sử dụng để huấn luyện mô hình khen thưởng

cuối cùng sẽ thực hiện điều này

làm việc thay con người.

Hoàn thành nhanh chóng tương tự

bộ thường được gán cho

nhiều người gắn nhãn để

thiết lập sự đồng thuận và

giảm thiểu tác động của người nghèo

người gắn nhãn trong nhóm.

Giống như người dán nhãn thứ ba ở đây, người có

câu trả lời không đồng ý với những người khác và

có thể chỉ ra rằng họ

hiểu sai hướng dẫn,

đây thực sự là một điểm rất quan trọng.

Sự rõ ràng trong hướng dẫn của bạn có thể

tạo ra sự khác biệt lớn về chất lượng

phản hồi của con người mà bạn nhận được.

Nhãn thường được lấy từ các mẫu của

dân số đại diện cho sự đa dạng và

tư duy toàn cầu.

Ở đây bạn có thể thấy một tập hợp ví dụ về

hướng dẫn được viết cho người dán nhãn.

Điều này sẽ được trình bày cho người dán nhãn

để đọc trước khi bắt đầu nhiệm vụ và

có sẵn để tham khảo lại

khi họ làm việc thông qua tập dữ liệu.

Các hướng dẫn bắt đầu với tổng thể

nhiệm vụ mà người dán nhãn nên thực hiện.

Trong trường hợp này, để chọn điều tốt nhất

hoàn thành cho lời nhắc.

Các hướng dẫn tiếp tục với phần bổ sung

chi tiết để hướng dẫn người dán nhãn

cách hoàn thành nhiệm vụ.

Nói chung càng chi tiết

bạn thực hiện những hướng dẫn này,

khả năng đó càng cao

người dán nhãn sẽ hiểu nhiệm vụ

họ phải thực hiện và

hoàn thành nó chính xác như bạn mong muốn.

Ví dụ, trong lệnh thứ hai

mục, người dán nhãn được thông báo rằng họ

nên đưa ra quyết định dựa trên

nhận thức về tính đúng đắn và

tính thông tin của câu trả lời.

Họ được thông báo rằng họ có thể sử dụng Internet

để kiểm tra thực tế và tìm thông tin khác.

Họ cũng được hướng dẫn rõ ràng

về việc phải làm gì nếu họ xác định được tỷ số hòa,

nghĩa là một cặp hoàn thành mà họ

nghĩ đều đúng và giàu thông tin như nhau.

Những người dán nhãn được thông báo rằng không sao cả

xếp hạng hai lần hoàn thành giống nhau, nhưng

họ nên làm điều này một cách tiết kiệm.

Lời hướng dẫn cuối cùng đáng được nêu ra

đây là những gì phải làm trong trường hợp

một sự nhầm lẫn vô nghĩa hoặc

câu trả lời không liên quan.

Trong trường hợp này, người dán nhãn nên

chọn F thay vì xếp hạng, vì vậy

câu trả lời kém chất lượng

có thể được gỡ bỏ dễ dàng.

Cung cấp một bộ chi tiết

hướng dẫn như thế này tăng lên

khả năng các phản hồi

sẽ có chất lượng cao và

mà cá nhân con người sẽ thực hiện

nhiệm vụ theo cách tương tự với nhau.

Điều này có thể giúp đảm bảo rằng tập thể

số lần hoàn thành được dán nhãn sẽ là

đại diện của

một quan điểm đồng thuận.

Khi người gắn nhãn của bạn đã hoàn thành

đánh giá của họ sau khi hoàn thành Prom

bộ, bạn có tất cả dữ liệu bạn

cần đào tạo mô hình khen thưởng.

Mà bạn sẽ sử dụng thay vì con người

để phân loại các lần hoàn thành mô hình trong quá trình

học tăng cường

quá trình tinh chỉnh.

Trước khi bạn bắt đầu tập luyện

tuy nhiên, mô hình phần thưởng

bạn cần chuyển đổi dữ liệu xếp hạng thành

sự so sánh theo cặp về số lần hoàn thành.

Nói cách khác, tất cả các cặp có thể có của

hoàn thành từ các lựa chọn có sẵn đến

lời nhắc phải được phân loại là 0 hoặc

1 điểm.

Trong ví dụ hiển thị ở đây,

có ba lần hoàn thành cho một dấu nhắc,

và thứ hạng do con người chỉ định

nhãn là 2, 1, 3, như được hiển thị,

trong đó 1 là thứ hạng cao nhất tương ứng

đến phản ứng ưa thích nhất.

Với ba sự hoàn thành khác nhau,

có ba cặp có thể

màu vàng tím, màu xanh tím và

màu vàng-xanh.

Tùy thuộc vào số N của

hoàn thành thay thế cho mỗi lời nhắc,

bạn sẽ có N chọn hai kết hợp.

Với mỗi cặp bạn sẽ ấn định phần thưởng

là 1 cho câu trả lời ưu tiên và

phần thưởng 0 cho

phản ứng ít được ưu tiên hơn.

Sau đó, bạn sẽ sắp xếp lại các lời nhắc để

rằng tùy chọn ưu tiên được ưu tiên trước.

Đây là một bước quan trọng

bởi vì mô hình phần thưởng kỳ vọng

mức độ hoàn thành ưu tiên,

đầu tiên được gọi là Yj.

Khi bạn đã hoàn thành dữ liệu này,

tái cơ cấu,

phản ứng của con người sẽ chính xác

định dạng để đào tạo mô hình khen thưởng.

Lưu ý rằng trong khi thích,

phản hồi không thích thường dễ dàng hơn

để thu thập phản hồi hơn là xếp hạng, xếp hạng

phản hồi giúp bạn hoàn thành buổi vũ hội nhiều hơn

dữ liệu để đào tạo mô hình phần thưởng của bạn.

Như bạn có thể thấy, ở đây bạn nhận được ba lời nhắc

cặp hoàn thành từ mỗi bảng xếp hạng của con người.