# 03 tùy chọn-langchain-lcel-chaining-method

---

Xin chào và chào mừng bạn đến với video này trên

Phương pháp chuỗi LangChain LCEL.

Sau khi xem video này, bạn sẽ có thể

Mô tả cách xây dựng các chuỗi linh hoạt, có thể kết hợp được bằng cách sử dụng

Cách tiếp cận hiện đại của LangChain đối với kỹ thuật nhanh chóng.

Cấu trúc lời nhắc sử dụng mẫu một cách hiệu quả.

Kết nối các thành phần bằng đường ống

nhà điều hành để hợp lý hóa quy trình công việc.

Và phát triển các mẫu có thể tái sử dụng cho nhiều ứng dụng AI.

Ngôn ngữ biểu thức LangChain, hoặc LCEL,

là một mẫu để xây dựng các ứng dụng LangChain

sử dụng toán tử đường ống để kết nối các thành phần.

Cách tiếp cận này đảm bảo một cách rõ ràng, dễ đọc

luồng dữ liệu từ đầu vào tới đầu ra.

LangChain đã phát triển đáng kể và điều này

video sẽ tập trung vào video mới hơn, được đề xuất

Mẫu LCEL thay vì cách tiếp cận chuỗi LLM truyền thống.

Phương pháp hiện đại này cung cấp khả năng kết hợp tốt hơn,

trực quan hóa rõ ràng hơn về luồng dữ liệu và lớn hơn

linh hoạt khi xây dựng các chuỗi phức tạp.

Để tạo mẫu LCEL điển hình, bạn cần

Xác định mẫu có biến và dấu ngoặc nhọn

Tạo một phiên bản mẫu nhắc nhở. Xây dựng một chuỗi bằng cách sử dụng đường ống

toán tử để kết nối các thành phần. Gọi chuỗi với các giá trị đầu vào.

Hãy xem điều này thực tế bằng một ví dụ cụ thể.

Trong LangChain, runnable đóng vai trò là giao diện

và các khối xây dựng kết nối khác nhau

các thành phần như LLM, bộ truy xuất và công cụ vào một đường dẫn.

Có hai thành phần nguyên thủy có thể chạy được chính.

Các thành phần chuỗi chuỗi có thể chạy được một cách tuần tự,

chuyển đầu ra từ một thành phần làm đầu vào cho thành phần tiếp theo.

RunnableParallel chạy nhiều thành phần

đồng thời trong khi sử dụng cùng một đầu vào cho mỗi.

Tuy nhiên, LCEL cung cấp các phím tắt cú pháp tinh tế.

Ví dụ: thay vì sử dụng chuỗi có thể chạy được,

chuỗi tuần tự tương tự có thể được tạo ra bởi

chỉ cần kết nối runnable 1 và runnable 2 với một

pipe, làm cho cấu trúc dễ đọc và trực quan hơn.

LCEL cũng tự động xử lý việc ép buộc kiểu.

Điều này có nghĩa là nó chuyển đổi mã thông thường thành các thành phần có thể chạy được.

Khi bạn sử dụng từ điển, nó sẽ trở thành một từ điển có thể chạy được

song song, chạy nhiều tác vụ cùng một lúc.

Khi bạn sử dụng một chức năng, nó sẽ trở thành một

RunnableLambda, biến đổi đầu vào.

Điều này xảy ra ở hậu trường nên bạn không

phải xử lý việc chuyển đổi theo cách thủ công.

Ví dụ: trong mã này, toán tử đường ống

kết hợp các mẫu lời nhắc với LLM.

Cấu trúc từ điển tạo RunnableParallel

xử lý đồng thời cả ba tác vụ.

Mỗi tác vụ nhận được cùng một đầu vào, văn bản nhưng xử lý nó theo cách khác nhau.

Khi bạn chạy cái này, nó sẽ tự động trở thành RunnableParallel.

Kết quả sẽ chứa ba khóa, tóm tắt, dịch thuật và

tình cảm, mỗi tình cảm đều có đầu ra từ lệnh gọi LLM tương ứng.

Hãy xem LCEL hoạt động bằng cách tạo một chuỗi đơn giản.

Mã này thể hiện cách các thành phần

có thể được kết nối bằng cách sử dụng toán tử đường ống.

RunnableLambda trong chuỗi này bao bọc

Hàm Format_prompt, chuyển đổi nó thành

một thành phần có thể chạy được mà LangChain có thể làm việc được.

Khi chuỗi chạy, RunnableLambda sẽ nhận

từ điển đầu vào, chứa tính từ

và khóa nội dung, chuyển từ điển này tới hàm Format_prompt.

Hàm định dạng mẫu lời nhắc với các biến này.

Lời nhắc được định dạng sau đó được chuyển tới thành phần tiếp theo, LLM.

Toán tử pipe tạo ra một chuỗi bằng cách

kết nối các thành phần có thể chạy được với nhau.

Trong chuỗi trò đùa này, đầu tiên, RunnableLambda

định dạng lời nhắc bằng các biến.

Toán tử đường ống chuyển lời nhắc được định dạng tới LLM.

Một đường dẫn khác chuyển phản hồi của LLM tới StrOutputParser.

Chúng tôi đã đề cập đến những điều cơ bản của LCEL, từ

lợi ích và thành phần nguyên thủy của nó để

xây dựng chuỗi thực tế bằng cách sử dụng toán tử đường ống.

Hãy nhớ rằng LCEL phù hợp nhất cho các tác vụ điều phối đơn giản hơn.

Đối với quy trình làm việc phức tạp hơn, hãy cân nhắc sử dụng LangGraph

trong khi vẫn tận dụng LCEL trong các nút riêng lẻ.

Khi bạn phát triển các ứng dụng của riêng mình, hãy thực hiện

tận dụng thế mạnh của LCEL, bao gồm

thực thi song song, hỗ trợ không đồng bộ, đơn giản hóa

phát trực tuyến và theo dõi tự động.

Những khả năng này nâng cao cả sức mạnh

và khả năng bảo trì các ứng dụng của bạn.

Trong video này, bạn đã học được rằng

Sử dụng cấu trúc mẫu LCEL

toán tử đường ống để có luồng dữ liệu rõ ràng.

Lời nhắc được xác định bằng cách sử dụng các mẫu

với các biến và dấu ngoặc nhọn.

Các thành phần có thể được liên kết bằng cách sử dụng

RunnableSequence để thực thi tuần tự.

RunnableParallel cho phép nhiều thành phần

để chạy đồng thời với cùng một đầu vào.

LCEL cung cấp cú pháp ngắn gọn hơn bằng cách thay thế

RunnableSequence với toán tử đường ống.

Gõ ép buộc trong LCEL tự động chuyển đổi hàm

và từ điển thành các thành phần tương thích.