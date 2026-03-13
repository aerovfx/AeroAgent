# 4 -RAG Pipeline – Giải thích quy trình làm việc lập chỉ mục.en US

---

Được rồi, bây giờ hãy thử

để hiểu cách chúng tôi có thể tối ưu hóa

điều đặc biệt này tốt hơn

và làm cho nó có khả năng mở rộng hơn.

Bây giờ RAG nói gì, điển hình

Cách tiếp cận của RAG nói rằng, này,

bạn có hai giai đoạn

trong đó bạn có thể làm một miếng giẻ, được thôi.

Số một được gọi là,

giai đoạn lập chỉ mục.

Được rồi.

Và số hai về cơ bản là

giai đoạn thu hồi, giai đoạn thu hồi.

Bây giờ ý tôi là gì khi nói điều này.

Giai đoạn truy xuất về cơ bản là

nơi người dùng thực sự đang ở

trò chuyện với dữ liệu.

Và giai đoạn lập chỉ mục về cơ bản là

nơi người dùng cung cấp dữ liệu.

Được rồi, vậy đây là nơi

cung cấp dữ liệu.

Vì vậy, về cơ bản người dùng đang tải lên

một số tài liệu họ đang đưa

bạn một số dữ liệu và đây là nơi họ

đang trò chuyện với dữ liệu.

Bây giờ có một điều là hai người này

là những giai đoạn hoàn toàn khác nhau

Hai cái này có mã khác nhau.

Được rồi, vậy trước tiên hãy hiểu

giai đoạn lập chỉ mục.

Giai đoạn lập chỉ mục như thế nào

điều gì thực sự xảy ra và điều gì thực sự xảy ra

là một giai đoạn lập chỉ mục?

Vậy điều gì xảy ra trong

giai đoạn lập chỉ mục?

Được rồi, tôi sẽ chỉ nói giai đoạn lập chỉ mục.

Trong giai đoạn lập chỉ mục, chúng tôi mong đợi

người dùng sẽ đi

để cho tôi rất nhiều tài liệu.

Được rồi, hãy nói về tài liệu.

Tài liệu ở đâu?

Vâng, đây là một tài liệu.

Vì vậy người dùng sẽ nói, này,

Tôi có một vài tài liệu.

Hãy bắt đầu lập chỉ mục nó.

Vì vậy, về cơ bản bạn sẽ hỏi người dùng

để tải lên tất cả dữ liệu của bạn.

Bây giờ dữ liệu này đến với bạn đầu tiên.

Hãy hiểu rằng điều này

là rất nhiều dữ liệu.

Vậy bước này chúng ta phải làm gì

một người nói, này, hãy chia nhỏ dữ liệu này

chia thành như, bạn biết đấy, chia nhỏ

dữ liệu này thành các phần nhỏ hơn.

Vì vậy, phần đầu tiên xuất hiện dưới dạng chunking.

Bây giờ làm thế nào bạn có thể thực hiện chunking?

Bạn có thể thực hiện phân đoạn ở cấp độ trang.

Ví dụ: mỗi trang là một đoạn.

Bạn thậm chí có thể làm điều đó

ở cấp độ đoạn văn mà mọi

đoạn văn là một đoạn.

Vì vậy, chunking về cơ bản có nghĩa là

việc chia tách dữ liệu này

thành những phần nhỏ hơn, nhỏ hơn.

Hãy để chúng tôi nói những gì bạn đã làm

bạn đã chia cái này chưa

thành từng đoạn.

Vậy bây giờ những gì bạn có là rất nhiều

của các đoạn, đoạn văn, phải không?

Vậy bước đầu tiên nói rằng, này, tôi

sẽ thực hiện một số loại chunking.

Bây giờ chunking hoàn toàn thuộc về bạn.

Bạn muốn chunk nó trên đoạn văn

mức độ, bạn muốn chunk nó

ở cấp độ trang,

hoặc có thể bạn muốn cắt nhỏ nó

bằng 250, 250, 250 ký tự.

Đó là ở bạn.

Được rồi?

Vì vậy, chunking về cơ bản có nghĩa là chia tách

dữ liệu thành các phần nhỏ hơn.

Đây là chunking.

Bây giờ những gì chúng tôi làm cho mọi

chunk, chúng tôi muốn xem cái gì

loại dữ liệu nó chứa.

Được rồi, vì vậy chúng ta sẽ đi

để sử dụng các nhúng vector của chúng tôi.

Bây giờ bạn đã hiểu cách nhúng vector.

Vì vậy tôi sẽ sử dụng một cái mở

không khí, bất kỳ loại mô hình.

Được rồi, đó là một mô hình nhúng.

Được rồi, xin hãy chú ý.

Đây là một mô hình nhúng, được chứ?

Vậy điều tôi sắp làm là

Tôi sẽ đưa từng phần cho

mô hình nhúng này và tôi sẽ

để tạo một số nhúng vector

cho mỗi đoạn ngoài đó.

Vì vậy bạn phải tạo

nhúng vector.

Vì vậy, điều này cũng sẽ đi đến đây,

cái này cũng sẽ đi tới đây

Và bạn biết đấy, đoạn này

cũng sẽ tới đây.

Vì vậy, trong một vòng lặp bạn sẽ đi

để cung cấp tất cả các vectơ CH

mô hình nhúng và bạn sẽ mong đợi

cái đó, này, vui lòng tạo

một vector nhúng cho tôi.

Được rồi, vậy là bạn đã có tất cả

các nhúng, nhúng vector.

Bây giờ những gì chúng ta sắp làm, chúng ta

sẽ có một cơ sở dữ liệu vector.

Vì vậy có rất nhiều

cơ sở dữ liệu đặc biệt có thể

lưu trữ các vector nhúng.

Ví dụ, nón thông là

đó, Viviate ở đó.

Bạn biết đấy, rất nhiều vector

cơ sở dữ liệu có sẵn ở đó.

Vì vậy, các vectơ nhúng này sẽ là

được lưu trữ trong cơ sở dữ liệu vector này.

Vậy hãy để tôi gọi

nó dưới dạng vector db.

Bây giờ, hãy để tôi nói cho bạn một điều, được chứ?

Những gì bạn hiện đang lưu trữ

về cơ bản thì đây là bản chất của bạn

sẽ lưu trữ trong vector DB là

số một, bạn là

sẽ lưu trữ các vectơ,

bất kỳ vectơ nào được tạo ra.

Hãy nói cho phần này cộng với bạn

cũng sẽ lưu trữ đoạn này.

Điều đó có nghĩa là về cơ bản bạn

nói, này, đây là chunk

A và đây là các vectơ.

Sau đó, bạn cũng sẽ lưu trữ

đoạn B và các vectơ của nó.

Sau đó, bạn cũng sẽ lưu trữ

đoạn và, sau đó là C cộng

bạn cũng có thể lưu trữ một số siêu dữ liệu.

Siêu dữ liệu, như từ tài liệu nào

đoạn này thuộc về,

tôi có được từ số trang nào

đoạn này, tất cả siêu dữ liệu đó.

Vì vậy tất cả các khối này được lưu trữ

vào cơ sở dữ liệu vector.

Đây là giai đoạn lập chỉ mục của bạn.

Vậy trong giai đoạn lập chỉ mục, về cơ bản những gì

bạn làm về cơ bản là bạn mong đợi

người dùng cung cấp một số dữ liệu.

Bạn thực hiện một số kiểu chunking

điều đó đang chia đôi số tiền lớn của bạn

dữ liệu thành nhiều khối,

mảnh vụn nhỏ hơn.

Đối với mỗi đoạn, bạn vượt qua nó

đến một mô hình nhúng

tạo ra các nhúng vector.

Và sau đó bạn lưu trữ vector này

nhúng vào cơ sở dữ liệu vector.

Được rồi?

Trong db vectơ này, bạn không chỉ có thể

chỉ cần lưu trữ các vectơ, bạn cũng có thể

lưu trữ nội dung thực tế đã được

được sử dụng trong việc nhúng vector này.

Ngoài ra bạn còn có thể lưu trữ

một số loại siêu dữ liệu.

Siêu dữ liệu, như trang đó là gì

số, tài liệu từ đâu

bạn lấy đoạn đặc biệt này ở đâu?

Vì vậy, tất cả dữ liệu này về cơ bản là

được lưu trữ dưới dạng siêu dữ liệu cùng

với các vectơ trong vectơ db.

Vì vậy tại thời điểm cụ thể này,

những gì bạn đã làm là bạn có

đã chuyển đổi tất cả dữ liệu

thành các vectơ nhỏ hơn, nhỏ hơn,

được lưu trữ trong một vectơ db.

Và đây là giai đoạn lập chỉ mục của bạn.

Đó là nó.

Vì vậy, đây là giai đoạn lập chỉ mục của bạn.

Bây giờ tôi sẽ chỉ cho bạn cách đó

bạn có thể sử dụng giai đoạn lập chỉ mục này không

trong giai đoạn truy xuất

để thực sự trò chuyện với bạn

1000 tập tin trong video tiếp theo?