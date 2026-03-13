# 013 Tạo một bộ bài mới vi

---

Giáo viên: Ở phần cuối,

chúng tôi kết hợp chức năng đầu tiên của mình với máy thu.

Bây giờ tôi muốn quay lại tài liệu của chúng tôi

nơi chúng tôi đã liệt kê ra tất cả các chức năng khác nhau

sẽ tồn tại bên trong dự án thẻ này

mà chúng tôi đang làm việc.

Được rồi, nó ở ngay đây này.

Vì vậy vào thời điểm này,

chúng tôi thực sự đã kết hợp chức năng in này.

Hãy nhớ rằng bản in được cho là

để đăng xuất nội dung của toàn bộ bộ bài.

Và vì vậy chúng tôi thực sự vừa kết hợp thành công thứ này với nhau.

Vậy là chúng ta đã có một khởi đầu khá tốt ở đây.

Bây giờ tôi nghĩ có lẽ chúng ta nên quay lại

chức năng đầu tiên mà chúng tôi gọi là newDeck.

Vì vậy newDeck lẽ ra phải tạo ra

và trả về danh sách các lá bài đang chơi.

Hãy nhớ rằng thành phần lá bài này hoặc bộ bài này,

khi chúng tôi nói newDeck ngay tại đây

và chúng tôi yêu cầu trả lại danh sách các lá bài,

Tôi thực sự đang nói rất nhiều về thực tế

như Ace of Spades, Two of Spades, Three of Spades,

và tất cả những thứ tốt đẹp đó.

Vì vậy hãy tạo hàm newDeck này ngay bây giờ

và hiểu rõ hơn về mã bên trong nó.

Được rồi, quay lại bên trong tệp deck.go của chúng ta,

ngay bên dưới phần khai báo kiểu của chúng ta,

Tôi sẽ tạo hàm newDeck mới này.

Vì vậy tôi sẽ nói func newDeck

và sau đó đặt dấu ngoặc nhọn của tôi.

Bây giờ bạn sẽ nhận thấy bên trong tài liệu này ngay tại đây,

chúng tôi đã nói rằng điều này sẽ tạo ra

và trả về danh sách các lá bài đang chơi.

Vì vậy chúng ta cần đảm bảo

hàm này ở đây trả về danh sách các thẻ

hoặc về cơ bản thực sự trả lại một bộ bài.

Hãy nhớ rằng với cờ vây,

bất cứ khi nào chúng ta muốn trả về một giá trị từ một hàm,

chúng ta phải chú thích hàm với kiểu mà nó trả về

và chúng ta đặt chú thích đó ngay sau tên hàm.

Vì vậy ngay sau newDeck,

chúng ta sẽ đặt từ, bộ bài, như vậy.

Vậy điều này sẽ cho Go biết

rằng bất cứ khi nào ai đó gọi newDeck,

họ sẽ trả về một giá trị thuộc loại deck.

Được rồi.

Bây giờ, đối với bộ thu chức năng ở đây,

Tôi sẽ hỏi bạn,

bạn có nghĩ rằng chức năng này cần một máy thu?

Vâng, thành thật mà nói, cá nhân tôi nghĩ rằng nó không

bởi vì mục đích

của chức năng này là tạo ra một bộ bài mới.

Và vì vậy nếu bạn gọi thứ này ở đây,

rất có thể bạn chưa làm việc trên một bộ bài mới.

Bạn muốn có được một bộ bài.

Bạn chưa có một.

Vì vậy, chúng tôi sẽ không thêm bất kỳ bộ thu nào vào chức năng này

bởi vì chúng tôi chỉ thêm người nhận

khi chúng ta muốn có thể làm điều gì đó như nói,

gọi tên phương thức blah, blah, blah, dấu chấm.

Được rồi, quay lại đây với newDeck,

chúng ta sẽ làm theo cùng một kiểu mẫu

mà chúng tôi đã sử dụng lại khi tập hợp bộ bài trước đó

bên trong chức năng chính.

Vì vậy, bên trong đây, hãy nhớ rằng chúng ta đã tạo một bộ bài mới

bằng cách đặt tên loại và sau đó là dấu ngoặc nhọn.

Hãy bắt đầu từ đó.

Chúng ta sẽ nói quân bài dấu hai chấm bằng bộ bài,

dấu ngoặc nhọn như vậy.

Vì vậy, điều này tạo ra một biến mới gọi là các loại bài

và nó bắt đầu một trăm phần trăm trống rỗng,

nên không có thẻ bên trong nào cả.

Bây giờ hãy nhớ, chúng tôi muốn

để cuối cùng có thứ này chứa tất cả 52 thẻ

như Ace of Spades, Two of Spades và những thứ tương tự.

Vì vậy chúng ta có thể áp dụng phương pháp

viết ra tất cả 52 tổ hợp thẻ ở đây.

Vì vậy, Ace of Spades, Two of Spades,

nhưng rõ ràng,

điều đó sẽ trở nên thực sự tẻ nhạt rất nhanh.

Vì vậy tôi sẽ đề xuất điều gì đó thông minh hơn một chút.

Tôi nghĩ chúng ta nên tạo ra bộ bài trống đó,

thì chúng ta nên tạo hai lát cắt riêng biệt.

Người ta nên có một danh sách tất cả các bộ bài khác nhau

và sau đó một cái khác sẽ có một danh sách

của tất cả các giá trị quân bài khác nhau như Át, Hai,

Ba, Bốn, Năm, Sáu, Bảy.

Sau đó chúng ta có thể thiết lập hai vòng lặp for khác nhau

để lặp qua danh sách các bộ quần áo

và danh sách giá trị thẻ.

Và sau đó chúng ta có thể nói

rằng với mỗi sự kết hợp của chất với mỗi giá trị khác nhau,

chúng ta có thể tạo một lá bài mới và dán nó vào bộ bài.

Vì vậy tôi nghĩ rằng chúng ta sẽ áp dụng phương pháp này ngay tại đây

để tránh có

để gõ thủ công tất cả 52 tổ hợp thẻ khác nhau.

Được rồi, vậy chúng ta sẽ bắt đầu trước tiên

bằng cách xác định danh sách cardSuits và cardValues của chúng tôi.

Vì vậy chúng ta sẽ nói cardSuits sẽ là một lát cắt

của chuỗi với Ace...

Rất tiếc, không phải Ace,

nhưng Spades,

kim cương,

trái tim,

và Câu lạc bộ.

Bây giờ bạn sẽ nhận thấy rằng chúng tôi đang tạo ra cái này

như một đoạn dây.

Chúng tôi không biến nó thành một bộ bài

bởi vì một bộ bài thực sự được cho là sẽ được sử dụng

với thẻ chơi thực tế.

Vì vậy, giống như quân Ace of Spades, Two of Spades, Three of Spades.

Những gì chúng ta có ở đây chỉ là những chuỗi

và họ thực sự không được coi là đại diện

của một thẻ thực tế.

Nó giống như một nửa thẻ.

Vì vậy chúng ta sẽ biến nó thành một đoạn dây.

Bây giờ, ngay bên dưới phần khai báo cardSuits của chúng tôi,

chúng tôi sẽ tạo một phần của tất cả các giá trị thẻ khác nhau.

Vì vậy chúng ta sẽ nói cardValues,

và đây sẽ là một lát cắt khác của chuỗi kiểu

với những thứ như Át, Hai, Ba, Bốn.

Bây giờ, tất nhiên,

điều này có lẽ sẽ liên quan đến King,

nhưng tôi nghĩ rằng Ace, Two, Three, Four có lẽ là đủ

ngay bây giờ, ít nhất là đủ để kiểm tra mọi thứ.

Được rồi, giờ chúng ta đã có bộ bài trống,

đó là biến thẻ này.

Chúng tôi có danh sách tất cả các bộ đồ khác nhau của chúng tôi

và một danh sách tất cả các giá trị khác nhau.

Vì vậy bây giờ bên dưới những thứ đó,

chúng ta sẽ thiết lập hai vòng lặp for,

cái này lồng vào cái kia

để lặp lại tất cả các bộ đồ của chúng tôi,

và sau đó thông qua tất cả các thẻ của chúng tôi.

Và với mọi sự kết hợp giữa hai điều này,

chúng ta sẽ thêm một thẻ mới vào phần thẻ của mình.

Vì vậy, chúng tôi sẽ nói cho,

và nhớ cú pháp ở đây của vòng lặp for

mà chúng tôi lặp đi lặp lại.

Chúng ta đã ghép lại một cái rồi

hoặc cùng nhau quay lại bên trong chức năng chính của chúng ta,

chỉ một chút trước đây.

Ồ, và đây là một cái để tham khảo ngay bên dưới.

Vì vậy chúng tôi đặt xuống cho,

chỉ số và...

Đầu tiên chúng ta sẽ duyệt qua bộ đồ.

Vì vậy, chúng tôi sẽ lưu cho i và suit từ phạm vi cardSuits.

Và sau đó chúng ta sẽ lặp qua tất cả các giá trị khác nhau,

vì vậy tôi,

hoặc cho j và giá trị bên trong phạm vi cardValues.

Vậy chúng ta sẽ lấy lát thẻ,

chúng ta sẽ tạo một thẻ mới

bằng cách nối chuỗi phù hợp và giá trị với nhau

và sau đó gắn nó vào lát thẻ.

Vì vậy chúng ta sẽ nói thẻ bằng nối thêm

trên lát thẻ một giá trị mới phù hợp và giá trị,

vì vậy suit+ chuỗi +value.

Được rồi, vậy là tôi biết

rằng chúng ta vừa trải qua vòng lặp này rất nhanh ở đây,

nhưng thực lòng tôi tin chắc một trăm phần trăm

mà có lẽ bạn đã rất quen thuộc

với cú pháp trông giống như thế này.

Và thành thật mà nói,

điều này liên quan nhiều hơn đến loại lập trình cơ bản

hơn là bất cứ điều gì cụ thể để đi.

Vậy là chúng ta đã tạo ra hai danh sách, phải không?

Chúng ta thậm chí không cần phải tưởng tượng những thứ này như những lát cắt.

Rất nhiều cú pháp

và rất nhiều cấu trúc bên trong Go là rất nhiều

về những thứ lập trình mà bạn có thể đã quen

từ các ngôn ngữ lập trình khác.

Vì vậy chúng tôi đã tạo hai danh sách ở đây.

Chúng tôi lặp lại qua từng cái,

và sau đó cho mọi sự kết hợp giữa sự phù hợp và giá trị,

chúng tôi tạo ra một giá trị mới hoặc một thẻ mới ngay tại đây.

Vậy chuyện này sẽ giống như...

Ồ, chúng tôi đã đảo ngược trật tự.

Nó phải có giá trị và phù hợp.

Vì vậy, chúng tôi lấy giá trị mà chúng tôi đang lặp lại

và bộ đồ mà chúng tôi đang xem xét.

Chúng tôi nối chúng lại với nhau bằng một sợi dây

và sau đó chúng tôi thêm nó vào danh sách thẻ hoặc lát thẻ,

và sau đó chúng tôi gán kết quả lớn của điều đó

vào các thẻ biến.

Vì vậy, một lần nữa, bạn biết đấy, chúng ta đang tăng tốc vượt qua nó

nhưng thành thật mà nói tôi nghĩ điều này thật tử tế

những thứ lập trình đơn giản

và bạn không cần phải biết nhiều về Go

để làm những việc cơ bản này.

Bây giờ, lý do tôi đặc biệt đề cập đến điều này là vì tôi thấy

rằng rất nhiều người đang dần quen với cờ vây,

thường bị đóng băng và đi như thế này,

"Ồ, đây là mã Go.

Đó là một ngôn ngữ mới.

Tôi không biết cách làm bất cứ điều gì với Go."

Thành thật mà nói, cờ vây giống như một thứ vani

và thực sự không có nhiều tính năng đặc biệt cho nó.

Bạn có thể sử dụng tất cả kiến thức lập trình cơ bản của mình

và áp dụng nó vào Go và thực sự kết hợp các chương trình tốt

không cần nghiên cứu nhiều về ngôn ngữ.

Tất nhiên, bây giờ, những việc như tìm ra các loại

và những chiếc máy thu này và những thứ tương tự,

vâng, đó là tính năng ngôn ngữ mới,

nhưng đối với việc khai báo một danh sách và lặp lại chúng,

Tôi nghĩ rằng bạn có thể biết nhiều hơn

hơn bạn nghĩ bạn có thể.

Được rồi, quay lại hàm newDeck của chúng ta ở đây.

Chúng tôi đã thực hiện việc lặp lại.

Bây giờ, điều cuối cùng chúng ta phải làm ở đây,

chúng tôi phải đảm bảo rằng chúng tôi trả lại một bộ bài thực sự.

Vì vậy hãy nhớ rằng chúng ta đã nói

rằng chúng ta sẽ trả về một biến kiểu deck ở đây.

Vì vậy, sau khi chúng tôi thực hiện tất cả các bước lặp,

chúng ta cần đảm bảo rằng chúng ta trả lại lát thẻ.

Một lần nữa, những thứ máy tính cơ bản ở đây,

lập trình cơ bản.

Vâng, thực hiện phép lặp, tạo lát cắt,

và cuối cùng,

đảm bảo bạn trả lại bất cứ điều gì bạn đã tạo.

Bây giờ, khi chúng ta lưu tập tin này,

bạn có thể thấy hai lỗi này bật lên.

Cả hai đều đang nói,

"Này, bạn đã khai báo những biến này

nhưng bạn chưa bao giờ thực sự sử dụng chúng."

Vì vậy bạn sẽ nhận thấy rằng, bạn biết đấy, tôi và j ở đây,

chúng là chỉ số của mọi bộ đồ và giá trị

trong cả hai lát đó.

Nhưng tất nhiên, chúng ta không bao giờ phải thực sự sử dụng những chỉ số này

tại bất kỳ thời điểm nào để ghép các lát thẻ này lại với nhau.

Vì vậy, bất cứ khi nào bạn có một số biến

mà bạn thực sự không cần phải sử dụng,

chúng tôi luôn thay thế nó bằng dấu gạch dưới để báo cho Go,

"Này, chúng tôi hiểu rằng có một biến số ở đây

nhưng chúng tôi không quan tâm đến nó

và chúng tôi không muốn sử dụng nó."

Vì vậy, khi chúng ta thay thế cả hai cái đó bằng dấu gạch dưới

và sau đó lưu tệp, cả hai thông báo lỗi đều biến mất.

Được rồi, tôi nghĩ chúng ta đã sẵn sàng thử nghiệm điều này.

Vì vậy, hãy quay lại tệp main.go của chúng ta.

Bên trong đây, chúng ta sẽ dọn dẹp một chút.

Vì vậy tôi sẽ xóa chức năng newCard đó

bởi vì chúng tôi sẽ không sử dụng nó

để ghép các bộ bài lại với nhau nữa.

Tôi sẽ dọn dẹp nơi chúng tôi sẽ thêm vào thẻ.

Và sau đó thay vì giao thẻ,

bộ bài này ngay tại đây mà chúng tôi đang làm thủ công,

chúng ta sẽ gán cho nó kết quả

của lệnh gọi hàm tới newDeck như vậy.

Vì vậy chúng ta sẽ lưu file này lại rồi lật lại

đến thiết bị đầu cuối và kiểm tra điều này.

Vì vậy, một lần nữa, chúng ta sẽ nói chạy main.go và deck.go.

Và chúng ta bắt đầu.

Vì vậy, chúng tôi nhận được một danh sách lớn

trong số tất cả các kết hợp thẻ khác nhau của chúng tôi:

Ace of Spades, Two of Spades, v.v.

Được rồi, tôi nghĩ vậy

rằng chúng tôi đã làm rất tốt chức năng newDeck này.

Chúng ta hãy nghỉ ngơi

và tiếp tục với chức năng tiếp theo của chúng tôi trong phần tiếp theo.