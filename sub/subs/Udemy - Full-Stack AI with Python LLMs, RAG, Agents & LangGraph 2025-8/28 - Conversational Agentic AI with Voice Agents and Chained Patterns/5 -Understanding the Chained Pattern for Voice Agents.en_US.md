# 5 -Tìm hiểu mô hình chuỗi cho Voice Agents.en US

---

Được rồi, bây giờ hãy nói chuyện

về phương pháp xích.

Điều gì xảy ra trong chuỗi

theo chuỗi?

Những gì bạn làm là tử tế

giống như một chuỗi nơi

bạn biến đổi âm thanh

để nhắn tin và quay lại

để sử dụng các mô hình hiện có.

Được rồi?

Điều đó có nghĩa là những gì xảy ra ở đây là

bạn lấy âm thanh của người dùng

làm đầu vào và bạn chuyển đổi

cái này thành một văn bản

về cơ bản là phiên âm, phải không?

Lời nói thành văn bản.

Về cơ bản đây là

được biết đến như cái gì?

Lời nói thành văn bản.

Vì vậy, bất kể tôi đang nói gì,

giống như bạn có

phụ đề, chú thích, bạn

chuyển đổi nó thành văn bản.

Bây giờ khi bạn đã nhận được văn bản,

bạn có thể sử dụng GPT thông thường của mình không

mô hình như chúng tôi đang sử dụng?

Chúng tôi đang sử dụng Gemini, chúng tôi

đang sử dụng bất cứ thứ gì

Vì vậy, về cơ bản bạn có thể

sử dụng bất kỳ mô hình nào.

Mô hình chuyển văn bản thành văn bản GPT 4.1.

Và mô hình này trả về cái gì?

Mô hình này cũng

trả lại một văn bản.

Bây giờ những gì bạn có thể làm là sử dụng

văn bản này từ LLM trở lại

và bạn có thể chuyển đổi nó

với một giọng nói mà bạn có thể

phát trên âm thanh của người dùng.

Điều này được gọi là

một kiến trúc xâu chuỗi.

Bởi vì những gì bạn đang làm,

bạn lấy giọng nói của người dùng.

Vì vậy tôi sẽ chỉ nói lấy

giọng nói của người dùng,

chuyển đổi nó thành văn bản.

Bước này được gọi là STT

Lời nói thành văn bản.

Bây giờ bạn đã có văn bản,

bạn chuyển nó sang cái gì?

Bạn chuyển nó cho Mô hình LLM của bạn.

Được rồi, bây giờ mô hình LLM của bạn cần

một văn bản làm đầu vào và nó

cũng đưa ra văn bản như một đầu ra.

Bây giờ bạn lấy văn bản này

và chuyển đổi nó thành âm thanh.

Và bước này được gọi là,

hãy để tôi chỉ nói âm thanh.

Điều này được gọi là TTS

Chuyển văn bản thành giọng nói.

Đây là điển hình của bạn

mô hình xích.

Bây giờ lợi thế của nó, số

một, bạn có

linh hoạt để sử dụng bất kỳ LLM nào,

không chỉ OpenAI, bạn có thể sử dụng

Song Tử, bạn có thể sử dụng Claude,

Claude, bạn có thể sử dụng

OpenAI, bạn có thể sử dụng bất kỳ

mô hình bởi vì tất cả các mô hình

hỗ trợ chuyển văn bản thành văn bản.

Bạn không phải là chất kết dính

chỉ và chỉ sử dụng một bài phát biểu

đến mô hình lời nói.

Bạn có thể sử dụng bất kỳ mô hình nào, phải không?

Và điều này mang lại cho bạn nhiều hơn

linh hoạt vì

ví dụ, ở đây bạn có

mọi thứ phải không?

Đó là mô hình chuyển văn bản thành văn bản.

Bạn muốn làm một điều gì đó

gọi công cụ.

Có lẽ ở bước đặc biệt này

bạn muốn sử dụng biểu đồ lang.

Được rồi, bạn có thể sử dụng nó.

Hãy nói rằng bạn sẵn lòng

sử dụng biểu đồ lang, biểu đồ lang,

nếu tôi có thể đánh vần nó

chính xác, bạn có thể sử dụng lang

đồ thị, bạn có thể sử dụng LangChain.

Vì vậy khả năng là vô tận.

Bạn biết làm thế nào

để sắp xếp một LLM, phải không?

Đây là những gì toàn bộ

Tất nhiên là về.

Điều duy nhất là chúng tôi

chỉ là, chỉ đang thêm cái này

bước và chúng tôi chỉ đang thêm

bước này ở cuối.

Vì thế điều này được gọi là

một kiến trúc xâu chuỗi.

Vì vậy, bạn có thể thấy điều đó trong chuỗi

âm thanh thành văn bản để hoàn thành.

Vì vậy, khi tôi cuộn xuống

đến kiến trúc xiềng xích,

chúng ta hãy nhấp vào nó.

Nó không chuyển hướng tôi

vì một số lý do.

Nhưng vâng, vì vậy bạn có thể thấy những gì

về cơ bản bạn có thể làm là,

Tôi không muốn xây dựng một tiếng nói

đại lý sử dụng cái này, được chứ.

Vì lý do nào đó mà không phải vậy,

bạn biết đấy, đang chuyển hướng tôi

với điều đó, nhưng không sao cả.

Vì thế kiến trúc xâu chuỗi

về cơ bản hoạt động

về nguyên tắc này.

Bây giờ bạn biết tôi cảm thấy gì

thậm chí là mô hình lời nói thành lời nói.

Thứ nhất, bạn bị ràng buộc

với mẫu này phải không?

Bạn không thể, bạn không

có sự linh hoạt

để chọn mẫu phải không?

Ví dụ, nếu bạn

sử dụng mẫu S2S, số

một, nó đắt tiền.

Thứ hai, bạn bị ràng buộc

mà bạn chỉ có thể sử dụng 4, 0.

Có lẽ tôi muốn sử dụng Gemini.

Có lẽ tôi muốn sử dụng Claude.

Xin lỗi, điều đó là không thể

bởi vì bạn có

để chọn một mô hình mà

thể thao S2s, phải không?

Đó là 4o thời gian thực.

Và những mô hình này là tốt

khi nói chuyện với bạn,

nhưng chúng không thực sự tốt

trong trí thông minh.

Trí thông minh của họ

mức độ thấp.

Nhưng khi bạn sử dụng dây xích

kiến trúc, bạn, bạn

có đầy đủ khả năng

sử dụng một mô hình rất lớn

với trí tuệ cao.

Vì thế.

Và thứ hai, điều tôi nghĩ

rằng ngay cả những điều này trong nội bộ

làm điều tương tự

Bạn biết đấy, lấy giọng nói,

chuyển đổi nó thành văn bản,

nhận lại phản hồi

và chuyển đổi thành âm thanh.

Điều duy nhất là

đó là độ trễ thấp.

Đúng vậy, độ trễ rất thấp

ở đây vì bạn có nhiều

các bước thực hiện, bạn có thể thấy.

Vì vậy độ trễ là

hơi cao một chút.

Điều đó có nghĩa là khi bạn

nói chuyện, LLM sẽ mất ít thời gian

thời gian để trả lời lại.

Đó là nhược điểm duy nhất

mà bạn có.

Vì vậy, về cơ bản đó là

một nhược điểm.

Nhưng dù sao thì cũng không sao.

Chúng ta có thể thấy điều đó.

Vậy chúng ta sẽ làm gì

phải làm bây giờ bạn biết đấy

cả hai kiến trúc.

Đó là một lời nói thành lời nói

kiến trúc và bạn biết đấy

kiến trúc xâu chuỗi.

Trong video cụ thể tiếp theo,

hãy thử mã hóa một đại lý

sử dụng kiến trúc xích

bởi vì nó rộng rãi hơn

sử dụng, linh hoạt hơn.

Và S2S đúng là như vậy

bây giờ chỉ có OpenAI hỗ trợ.

Nhưng nó rất dễ dàng

để thực sự mã hóa một thứ S2S.

Được rồi?

Vì thế đừng lo lắng.

Tôi sẽ chỉ cho bạn

tài liệu về cách viết mã

một mô hình S2S là tốt.