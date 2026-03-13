# 04 lab-2-hướng dẫn

---

Lab tuần này mời các bạn thử sức

tinh chỉnh bằng cách sử dụng

PEFT với LoRA cho

bản thân bạn bằng cách cải thiện

khả năng tóm tắt

của mẫu Flan-T5.

Đồng nghiệp của tôi, Chris, sẽ

hướng dẫn bạn điều này

sổ ghi chép hàng tuần.

Tôi sẽ chuyển cậu cho anh ấy.

Này, cảm ơn, Shelby.

Bây giờ chúng ta hãy xem Lab 2.

Trong Lab 2, bạn sẽ

bắt tay vào thực hiện

tinh chỉnh đầy đủ và

Tinh chỉnh tham số hiệu quả,

còn được gọi là PEFT với

hướng dẫn kịp thời.

Bạn sẽ điều chỉnh Flan-T5

mô hình hơn nữa với

lời nhắc cụ thể của riêng bạn

cho cụ thể của bạn

nhiệm vụ tổng hợp.

Hãy nhảy sang phải

vào sổ ghi chép.

Phòng thí nghiệm 2, chúng ta sẽ đến

thực sự tinh chỉnh một mô hình.

Phòng thí nghiệm 1, chúng tôi đang làm

suy luận không bắn,

việc học tập trong ngữ cảnh.

Bây giờ chúng tôi thực sự

sắp sửa đổi

trọng lượng của chúng tôi

mô hình ngôn ngữ,

cụ thể cho chúng tôi

nhiệm vụ tóm tắt

và cụ thể cho tập dữ liệu của chúng tôi.

Thật nhanh chóng, chỉ cần kiểm tra lại

rằng bạn có 8 CPU,

32 gigabyte, đó là

loại ví dụ ở đây.

Đây là loại phiên bản AWS

từ SageMaker, ml.m5.2xl.

Hãy thực hiện cài đặt pip này.

Trong khi cài đặt pip

đang xảy ra,

hãy để tôi giải thích ngọn đuốc và

torchdata giống như Lab

1 nơi chúng ta sẽ đến

sử dụng PyTorch,

sau đó chúng tôi đang cài đặt pip

thư viện torchdata để

trợ giúp với PyTorch

đang tải dữ liệu.

Ngoài ra còn có thư viện

được gọi là đánh giá,

và đây là điều chúng tôi đang làm

sẽ sử dụng với

điểm rouge của chúng tôi là

tính toán hồng hào.

Bạn đã học về rouge trong

những bài học như một cách

để đo lường tốt như thế nào

làm một bản tóm tắt

gói gọn những gì có trong đó

cuộc trò chuyện ban đầu

hoặc văn bản gốc.

Bây giờ, hai thư viện này,

LoRA và PEFT,

bạn đã nghe nói về một

chút trong bài học.

Đây là những gì chúng ta sẽ sử dụng để

làm tham số

tinh chỉnh hiệu quả.

Bây giờ tôi sẽ làm

một số hàng nhập khẩu ở đây từ

những cài đặt pip đó.

Nếu bạn thấy điều này,

đôi khi dữ liệu sạch này

trong vài phút nữa sẽ có thứ xuất hiện ở đây,

bạn không cần điều này cho phòng thí nghiệm.

Nếu bạn nhìn thấy nó, tôi nghĩ điều này

xuất hiện bất cứ khi nào

chúng tôi nhập khẩu gấu trúc,

chỉ cần nhấp vào "X"

và nhấp vào "Không hiển thị

Một lần nữa" bởi vì chúng tôi không

sử dụng phần đó của SageMaker.

Một lần nữa, chúng ta có

AutoModelForSeq2Seq.

Đây là những gì đang diễn ra

để cung cấp cho chúng tôi quyền truy cập vào

Flan-T5 thông qua

thư viện máy biến áp python,

mã thông báo, chúng tôi sử dụng

cấu hình thế hệ trong

phòng thí nghiệm trước đó.

Bây giờ chúng ta sẽ

xem hai lớp mới,

một cái tên là TrainingArguments,

một người được gọi là Huấn luyện viên.

Tất cả đều từ máy biến áp,

những thứ này chúng ta luôn có thể sử dụng

điều đó đơn giản hóa mã của chúng tôi khi

chúng tôi đang cố gắng đào tạo

mô hình ngôn ngữ của chúng tôi

hoặc tinh chỉnh mô hình ngôn ngữ của chúng tôi.

Chúng tôi thấy rằng chúng tôi sắp

nhập PyTorch và đánh giá,

và chúng tôi sẽ sử dụng tôi tin rằng

gấu trúc và numpy sau này.

Hãy tải tập dữ liệu chỉ

giống như chúng tôi đã làm trong phòng thí nghiệm đầu tiên.

Hãy tải mô hình

giống như chúng tôi đã làm ở

phòng thí nghiệm đầu tiên và công cụ mã thông báo,

và đây được gọi là

mô hình ban đầu và cái này

sẽ hữu ích sau này khi chúng ta

so sánh mọi thứ khác nhau

các chiến lược tinh chỉnh

đến mô hình ban đầu

điều đó không được tinh chỉnh.

Tiện ích là đây

chức năng đó

in ra tất cả các thông số

có trong mô hình và

cụ thể là

các thông số có thể huấn luyện được.

Điều này sẽ trở nên hữu ích

khi chúng tôi giới thiệu

phiên bản PEFT của

mô hình đó làm

không huấn luyện tất cả các tham số.

Ở đây chúng ta thấy có

khoảng 250

triệu thông số

được đào tạo khi chúng tôi làm

sự tinh chỉnh đầy đủ,

đó là phần đầu tiên của

phòng thí nghiệm này nơi chúng tôi

tinh chỉnh đầy đủ.

Phần thứ hai của

phòng thí nghiệm sẽ là nơi chúng tôi làm

tham số

tinh chỉnh hiệu quả

đặc biệt là với LoRA,

nơi chúng tôi sẽ chỉ đào tạo

số rất nhỏ.

Vì vậy hãy ghi nhớ điều đó,

đây là một loại

rất nhiều mã lộn xộn nhưng

nó khá hữu ích

để so sánh.

Giống như chúng tôi đã làm

trong phòng thí nghiệm đầu tiên,

chúng tôi sẽ trình diễn

một đầu vào mẫu

Chúng tôi sẽ trình diễn

nền tảng của con người.

Chúng ta sẽ thực hiện cú sút số 0.

Đây không phải là một phát bắn,

không ít cú sút, chúng ta đã vượt qua

đó, đó là Phòng thí nghiệm 1.

Ở đây, chúng tôi đang cố gắng

đạt được điểm ở đó

một cuộc gọi đơn giản

vào mô hình của chúng tôi có thể

cung cấp cho chúng tôi một bản tóm tắt hợp lý mà không cần

phải vượt qua

một phát súng và

một vài ví dụ về cảnh quay,

đó là mục tiêu

Cách đầu tiên mà chúng tôi

sẽ làm là chúng ta sẽ đi

để thực hiện tinh chỉnh đầy đủ.

Tiện ích là đây

chức năng có thể token hóa

và bọc tập dữ liệu của chúng tôi

trong một dấu nhắc.

Như chúng ta đã thấy ở phần đầu

phòng thí nghiệm nơi chúng tôi có

một lời nhắc có nội dung tóm tắt

cuộc trò chuyện sau đây,

và sau đó chúng tôi thực sự sẽ đi

để cho nó một cuộc đối thoại,

và sau đó chúng ta sẽ đi

để kết thúc lời nhắc

với những dấu hai chấm tóm tắt đó.

Chức năng này sẽ cho phép chúng tôi lập bản đồ

trên tất cả các phần tử của

tập dữ liệu của chúng tôi và chuyển đổi

chúng thành lời nhắc

với sự hướng dẫn.

Đó là những gì chúng tôi đang có

định làm ở đây,

đó là tinh chỉnh đầy đủ

với lời nhắc hướng dẫn.

Ở đây, chúng ta sẽ chỉ

lấy một mẫu chỉ để giữ

các yêu cầu về nguồn lực

luật cho phòng thí nghiệm đặc biệt này,

tăng tốc mọi thứ lên một chút.

Chúng ta hãy nhìn vào kích thước.

Ở đây chúng tôi có khoảng 125

ví dụ đào tạo.

Chúng ta sẽ sử dụng

năm để xác nhận.

Chúng ta sẽ sử dụng

15 để thực sự làm

bài kiểm tra nắm giữ của chúng tôi sau

khi chúng tôi so sánh.

Chúng tôi sẽ tinh chỉnh với

đào tạo và chúng tôi sẽ

xác thực với xác nhận.

Sau đó khi tất cả

điều đó đã nói và làm,

sau đó chúng tôi sẽ sử dụng

15 ví dụ thử nghiệm để sau đó

so sánh các chiến lược khác nhau

để tinh chỉnh

với sự hướng dẫn.

Ở đây chúng ta thấy đào tạo

tranh luận và chúng tôi

xem một số mặc định ở đây

về tốc độ học tập.

Chúng tôi thấy một số đẹp

giá trị thấp cho

các bước tối đa và

số thời đại.

Đó là bởi vì chúng tôi

muốn thử

giảm thiểu số lượng

tính toán đó

cần thiết cho phòng thí nghiệm này.

Nếu bạn có nhiều thời gian hơn,

bạn chắc chắn có thể thay đổi

những giá trị này và nâng chúng lên

có lẽ lên đến năm kỷ nguyên,

có thể là bước tối đa 100.

Chút nữa tôi sẽ chỉ cho bạn

bạn thực sự chúng tôi thế nào

giải quyết vấn đề đó.

Chúng tôi đã đào tạo ngoại tuyến

một mô hình lớn hơn nhiều với

bước tối đa cao hơn nhiều và

kỷ nguyên đào tạo và trong một thời gian ngắn,

chúng tôi thực sự sẽ kéo nó

vào và sau đó tiếp tục từ đó.

Nhưng đây chính là điều

mã trông như thế nào

Đây là tập dữ liệu đào tạo,

có sự đánh giá

tập dữ liệu xác thực,

đây là nơi chúng tôi gọi là tàu hỏa.

Thực ra hãy để tôi làm Shift

Nhập, bắt đầu việc này.

Việc này sẽ mất vài phút,

ngay cả với mức tối đa thấp

các bước và kỷ nguyên thấp,

việc này vẫn cần

vài phút để chạy.

Sau đó, đây là bước đó

nơi chúng tôi thực sự kéo

từ đám mây vào

lưu trữ đồ vật,

một mô hình mà chúng tôi

được đào tạo bên ngoài

phòng thí nghiệm này là một

tốt hơn một chút.

Vì vậy, thực sự chúng tôi sẽ

bắt đầu với điều đó

Chúng ta hãy cho tàu một

vài phút để hoàn thành.

Những gì chúng tôi đang làm ở đây là chúng tôi

thực sự là

hướng dẫn tinh chỉnh

mô hình ngôn ngữ Flan-T5 của chúng tôi với

tập dữ liệu cụ thể của chúng tôi về

rất cụ thể

nhiệm vụ tổng hợp.

Rồi sau này chúng ta sẽ xem thế nào

chỉ số ROUGE

so sánh giữa

mô hình ban đầu và

hướng dẫn tinh chỉnh

mô hình mà chúng tôi có ở đây.

Hãy lấy mô hình đó từ

Lưu trữ đối tượng S3 mà chúng tôi

được đào tạo ngoại tuyến đó là

độ chính xác tốt hơn một chút và

tổn thất thấp hơn mà chúng tôi có thể

tập luyện lâu hơn ở bên ngoài

của phòng thí nghiệm cụ thể này.

Tôi muốn để mắt tới

về kích thước của mô hình này.

Đây là một bản tinh chỉnh hoàn chỉnh

mô hình hướng dẫn,

và bạn sẽ thấy nó

gần một gigabyte,

và điều đó sẽ có ích

sau này khi chúng tôi

so sánh nó với PEFT,

theo đơn đặt hàng

là 10 megabyte.

Ở đây chúng ta thấy 945 megabyte,

vì vậy chúng tôi đã kéo nó

mô hình xuống

một thư mục ở đây tên là flan

điểm kiểm tra tóm tắt đối thoại.

Bây giờ chúng ta sẽ tải

mô hình hướng dẫn đó,

vì vậy bây giờ điều này trở thành

mô hình mới của chúng tôi mà chúng tôi

sau đó sẽ sử dụng để

so sánh ở đây một chút.

Bây giờ chúng tôi đã tải những gì

chúng tôi đang gọi mô hình hướng dẫn,

chúng ta hãy thực sự thử từ

tập dữ liệu thử nghiệm của chúng tôi

sử dụng mắt người,

hãy kiểm tra chất lượng

và xem nó trông như thế nào.

Bản tóm tắt cơ bản Người

1 dạy Người 2 cách

nâng cấp trong hệ thống của Người 2.

Mô hình ban đầu không có

bất kỳ hướng dẫn tinh chỉnh nào,

chỉ là bắn không.

Lần này là

cho chúng ta Người 1,

bạn muốn nâng cấp

máy tính của bạn, Người 2,

bạn muốn nâng cấp

máy tính nên không tốt lắm.

Hướng dẫn tinh chỉnh

mô hình mà chúng tôi vừa thực hiện

đào tạo là Người 1

gợi ý Người 2 nên

nâng cấp hệ thống của họ,

phần cứng và CD ROM,

Người 2 suy nghĩ

đó là một ý tưởng tuyệt vời

Đó là về mặt chất lượng,

đó chỉ là nhìn thôi.

Bây giờ, chúng tôi chỉ lấy một

hãy xem một ví dụ,

nhưng đây là lý do tại sao chúng tôi

có kỹ thuật định lượng

để thực hiện sự so sánh này,

để thực hiện việc đánh giá.

Cụ thể, hãy tải

ROUGE và chúng tôi sẽ đi

để xem xét,

Tôi nghĩ chúng ta sẽ chỉ

có thể làm 10 điều đầu tiên ở đây,

và hãy so sánh chúng.

Hãy lấy 10 đầu tiên

từ tập dữ liệu thử nghiệm của chúng tôi.

Chúng tôi sẽ chạy chúng qua

những cuộc trò chuyện này,

qua cả bản gốc

Mẫu Flan-T5 cũng như

mô hình tinh chỉnh hướng dẫn

mà chúng tôi đã đào tạo ở trên.

Tất nhiên, ở đây chúng tôi

sẽ bọc nó trong một

nhắc nhở tương tự như những gì

chúng tôi đã từng đào tạo.

Sau đó hãy xem nó đã làm như thế nào.

Đây là việc sử dụng chất lượng

nhìn chúng cạnh nhau.

Hãy so sánh các

Số liệu ROUGE cho

cả Flan-T5 nguyên bản và

hướng dẫn tinh chỉnh

mô hình mà chúng tôi đã điều chỉnh ở trên.

Ở đây chúng ta thấy rằng hướng dẫn

điểm mô hình tinh chỉnh

cao hơn nhiều

thước đo đánh giá ROUGE

so với mẫu Flan-T5 ban đầu.

Điều này đang cho thấy rằng

với một chút

tinh chỉnh bằng cách sử dụng tập dữ liệu của chúng tôi

và một lời nhắc cụ thể,

chúng tôi thực sự đã có thể

cải thiện số liệu ROUGE.

Một điều khác mà chúng tôi đã làm

ngoại tuyến là chúng tôi đã làm nhiều thế này

lâu hơn với nhiều

tập dữ liệu thử nghiệm lớn hơn.

Đó không chỉ là 10

hoặc 15 ví dụ,

đây thực sự là

tập dữ liệu đầy đủ,

và chúng ta hãy xem xét.

Đó chính là tập tin này.

Tệp CSV đã đến

cùng với dữ liệu này

thư mục với phòng thí nghiệm này.

Ở đây chúng ta thấy với một

tập dữ liệu lớn hơn nhiều,

điểm số vẫn vậy

khá giống nhau,

nơi chúng tôi đang đến

gần gấp đôi,

không hẳn gấp đôi trong một số trường hợp,

nhưng khá quan trọng

cải tiến

dựa trên Flan-T5 ban đầu.

Ở đây chúng ta thấy tỷ lệ

cải tiến cụ thể.

Nếu chúng ta thực sự làm

tính toán,

chúng tôi thấy rouge1 cao hơn 18%,

rouge2 10%, rougeL 13,

rougeLsum 13.7 nữa.

Bây giờ hãy vào tham số

tinh chỉnh hiệu quả.

Đây là một trong những của tôi

chủ đề yêu thích.

Điều này làm cho một

sự khác biệt lớn,

đặc biệt là khi

bạn bị hạn chế bởi

tính toán bao nhiêu

nguồn lực mà bạn có,

bạn có thể giảm dấu chân

cả bộ nhớ, đĩa, GPU, CPU,

tất cả các tài nguyên

có thể giảm

chỉ bằng cách đưa PEFT vào

quá trình tinh chỉnh của bạn.

Trong các bài học bạn

đã tìm hiểu về LoRA,

bạn đã học về thứ hạng.

Ở đây chúng ta sẽ

chọn hạng 32,

đó thực sự là

tương đối cao.

Nhưng chúng tôi chỉ

bắt đầu từ đó.

Đây là SEQ_2_SEQ_LM,

đây là FLAN-T5.

Chỉ với một vài bổ sung

dòng mã ở đây để

định cấu hình tinh chỉnh LoRA của chúng tôi.

Sau đó, ở đây chúng ta thấy chúng ta

chỉ đi tập thôi

1,4 phần trăm của

các tham số mô hình có thể huấn luyện được.

Trong rất nhiều trường hợp

bạn có thể tinh chỉnh

mô hình rất lớn

trên một GPU duy nhất.

Đây là một số trong số đó

lập luận đào tạo.

Điều này thực sự trở lại

cái ôm ban đầu

đào tạo khuôn mặt

và huấn luyện lập luận,

ngoại trừ thay vì sử dụng

chỉ là mẫu thông thường,

chúng tôi thực sự đang sử dụng

mô hình PEFT

Đây là sự tiện lợi

chức năng được cung cấp bởi

thư viện PEFT và chúng tôi

cho nó mô hình ban đầu,

đó là FLAN-T5.

Chúng tôi cung cấp cho nó LoRA

cấu hình mà

chúng tôi đã xác định ở trên

với hạng 32.

Chúng tôi nói hãy cho tôi một PEFT

phiên bản của mô hình đó.

Đó là những gì đến

ra là 1,4 phần trăm.

Bây giờ chúng tôi làm

lập luận đào tạo.

Một lần nữa, số bước nhỏ,

một số lượng nhỏ các kỷ nguyên ở đây.

Chúng tôi có một phiên bản

đã được đào tạo ngoại tuyến.

Đó là một chút

tốt hơn cái đó

đó là trong này

phòng thí nghiệm cụ thể,

và đó là điều chúng tôi đang hướng tới

để tải xuống ở đây trong giây lát.

Hãy làm điều đó.

Đây là mô hình khác

được lưu trữ trong bộ lưu trữ đám mây S3.

Bây giờ chúng ta thấy đây là

chỉ có 14 megabyte.

Chúng được gọi là PEFT

bộ điều hợp hoặc người áp dụng LoRA.

Chúng được hợp nhất hoặc kết hợp

với LLM gốc.

Khi bạn thực sự đi đến

phục vụ mô hình này,

mà chúng ta sẽ nghe sau đây,

bạn phải lấy

LLM ban đầu và sau đó hợp nhất

trong bộ chuyển đổi LoRA PEFT này.

Chúng nhỏ hơn nhiều và

bạn có thể tái sử dụng cùng một đế

LLM và trao đổi khác nhau

Bộ điều hợp PEFT khi cần thiết.

Bây giờ chúng ta có PEFT

bộ chuyển đổi được sao chép xuống từ S3,

chúng ta sẽ hợp nhất nó

với LLM gốc,

đó là FLAN-T5 và sử dụng

điều đó thực sự

thực hiện tóm tắt.

Bây giờ có một điều cần gọi

ra điều đó không hoàn toàn

rõ ràng là khi chúng ta làm điều này,

Tôi thực sự có thể thiết lập

cờ is_trainable thành sai.

Bằng cách đặt is_trainable

gắn cờ thành sai,

chúng tôi đang nói với PyTorch

rằng chúng tôi không

quan tâm đến

đào tạo mô hình này.

Tất cả những gì chúng tôi quan tâm làm là

đường chuyền về phía trước chỉ

để có được những bản tóm tắt.

Điều này rất có ý nghĩa

bởi vì chúng ta có thể nói

PyTorch không tải

bất kỳ bản cập nhật nào

những phần trong số này

người vận hành và để

về cơ bản giảm thiểu dấu chân

cần thiết để chỉ thực hiện

suy luận với mô hình này.

Đây là một lá cờ khá gọn gàng.

Đây thực ra chỉ là

được giới thiệu gần đây

vào mô hình PEFT tại

thời gian của phòng thí nghiệm này.

Tôi muốn thể hiện nó ở đây

bởi vì đây là một

mẫu mà bạn

muốn cố gắng tìm kiếm khi bạn

làm mô hình của riêng bạn.

Khi bạn biết điều đó

bạn đã sẵn sàng

triển khai mô hình để suy luận,

thường có nhiều cách

mà bạn có thể gợi ý

vào khuôn khổ,

chẳng hạn như PyTorch mà bạn

sẽ không được đào tạo.

Điều này sau đó có thể làm giảm thêm

các nguồn lực cần thiết để

đưa ra những dự đoán này.

Ở đây, chỉ để nhấn mạnh nó,

Tôi in ra số

của các tham số có thể huấn luyện được.

Hãy ghi nhớ tại

điểm này chúng ta

chỉ dự định làm suy luận,

và chúng ta hãy chuyển sang điều đó.

Không có phần trăm trong số này

các thông số có thể huấn luyện được.

Ở đây, chúng ta sẽ

xây dựng một số lời nhắc mẫu

từ tập dữ liệu thử nghiệm của chúng tôi.

Chúng tôi chỉ đang đi thôi

chọn cái gì đó

ngẫu nhiên ở đây,

về cơ bản là Chỉ số 200.

Chúng ta sẽ thấy

mô hình hướng dẫn. Hiểu rồi.

Tôi nghĩ phần lớn là đúng,

mô hình PEFT

có được một chút,

bắt đầu tìm thấy một chút

nhiều sắc thái hơn ở đây.

Nhưng thực sự, như chúng ta sẽ thấy

về mặt chất lượng khi chúng ta

chạy các số liệu rouge.

Ở đây chúng ta sẽ so sánh

cơ sở của con người để

FLAN-T5 ban đầu cho

hướng dẫn đầy đủ tinh chỉnh,

và sau đó đến PEFT tinh chỉnh.

Phần lớn,

chỉ cần liếc nhìn ở đây,

nó trông giống như thế này

khá giống nhau.

Nhưng chúng ta hãy nhìn xem

tại các số liệu rouge

và xem chuyện gì đang xảy ra.

Ở đây chúng ta thấy

hướng dẫn tinh chỉnh là

một sự cải thiện khá mạnh mẽ

so với FLAN-T5 ban đầu.

Chúng ta thấy rằng mô hình PEFT

đau khổ một chút

của sự xuống cấp từ

đầy đủ tinh chỉnh.

Nó khá gần trong một số trường hợp.

Nó không quá tệ.

Nhưng chúng ta sử dụng ít hơn nhiều

tài nguyên trong quá trình tinh chỉnh,

hơn chúng ta sẽ có nếu chúng ta

đã làm đầy đủ hướng dẫn.

Bạn có thể tưởng tượng đây chỉ là

chỉ vài nghìn mẫu thôi

nhưng bạn có thể tưởng tượng ở quy mô lớn

làm thế nào điều này thực sự có thể cứu bạn

tấn tính toán

nguồn lực và thời gian bằng

sử dụng PEFT bằng cách tìm kiếm

ở tập dữ liệu lớn hơn.

Ở phía trên tôi chỉ đang nhìn

có lẽ là 10, 15 ví dụ.

Ở đây chúng ta thấy lớn hơn.

Có vẻ như tôi nghĩ tôi

có nó đây rouge one,

PEFT có thể thua khoảng một

1,7 phần trăm trên tất cả cho

của những số liệu màu hồng này.

Điều đó không tệ so với

khoản tiết kiệm mà bạn

nhận được khi bạn sử dụng PEFT.