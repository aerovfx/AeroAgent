# Chương 3. Ngăn chặn thảm họa quên

---

Phần 3.3, ngăn ngừa sự lãng quên thảm khốc, tái hiện kinh nghiệm.

Chúng tôi đang dần dần xây dựng các kỹ năng của mình và chúng tôi muốn thuật toán của mình rèn luyện những kỹ năng khó hơn

biến thể của trò chơi trong đó tất cả các quân cờ được đặt ngẫu nhiên trên lưới cho mỗi quân cờ mới

trò chơi.

Thuật toán không thể chỉ ghi nhớ một chuỗi các bước cần thực hiện như trước đây.

Nó cần có khả năng đi con đường ngắn nhất để đạt được mục tiêu mà không cần phải bước vào hố sâu,

bất kể cấu hình bo mạch ban đầu là gì.

Nó cần phát triển một cách thể hiện phức tạp hơn về môi trường của nó.

Phần 3.3.1, sự lãng quên thảm khốc.

Vấn đề chính mà chúng tôi gặp phải trong phần trước khi cố gắng huấn luyện mô hình của mình trên

chế độ ngẫu nhiên, có tên, quên thảm họa.

Đây thực sự là một vấn đề rất quan trọng liên quan đến các phương pháp đào tạo dựa trên độ dốc

trong đào tạo trực tuyến.

Đào tạo đào tạo là những gì chúng tôi đã và đang làm.

Chúng tôi truyền ngược lại sau mỗi nước đi khi chúng tôi chơi trò chơi.

Hãy tưởng tượng rằng thuật toán của chúng ta đang huấn luyện, học các giá trị Q cho trò chơi 1 của hình 3.12.

Người chơi được đặt giữa hố và khung thành, sao cho khung thành ở bên phải,

và cái hố ở bên trái.

Sử dụng chiến lược Epsilon-Tham lam, người chơi thực hiện một bước đi ngẫu nhiên và tình cờ thực hiện các bước để

bên phải và sút trúng đích.

Tuyệt vời.

Thuật toán sẽ cố gắng tìm hiểu xem cặp trạng thái-hành động này có liên quan đến giá trị cao hay không

bằng cách cập nhật trọng số của nó theo cách sao cho kết quả đầu ra sẽ phù hợp hơn với mục tiêu

giá trị thông qua lan truyền ngược.

Hình 3.12, ý tưởng của sự lãng quên thảm khốc là khi hai trạng thái trò chơi rất giống nhau

nhưng lại dẫn đến những kết quả rất khác nhau, hàm Q sẽ bị nhầm lẫn và sẽ không

có thể học được những gì để làm.

Trong ví dụ này, sự quên lãng thảm khốc xảy ra do hàm Q học từ

ván 1 di chuyển sang phải sẽ nhận được phần thưởng cộng 1, nhưng ở ván 2, trông rất giống nhau,

nó nhận được phần thưởng trừ 1 sau khi di chuyển sang phải.

Kết quả là thuật toán sẽ quên những gì nó đã học trước đó về ván 1, dẫn đến

về cơ bản không có sự học hỏi đáng kể nào cả.

Bây giờ ván 2 đã được bắt đầu và người chơi lại ở giữa khung thành và hố, nhưng điều này

thời điểm mục tiêu ở bên trái và hố ở bên phải.

Có lẽ với thuật toán ngây thơ của chúng tôi, trạng thái có vẻ rất giống với trò chơi trước.

Vì lần trước di chuyển sang phải đã mang lại phần thưởng tích cực nên người chơi chọn thực hiện một phần thưởng

lại bước sang bên phải, nhưng lần này nó lại rơi xuống hố và bị trừ 1 phần thưởng.

Người chơi đang suy nghĩ, chuyện gì đang xảy ra vậy?

Tôi nghĩ đi bên phải là quyết định tốt nhất dựa trên kinh nghiệm trước đây của tôi.

Nó có thể thực hiện truyền ngược lại để cập nhật giá trị hành động trạng thái của nó, nhưng vì trạng thái này

hành động rất giống với hành động trạng thái đã học cuối cùng, nó có thể ghi đè hành động trước đó

trọng lượng đã học.

Đây là bản chất của sự lãng quên thảm khốc.

Có một lực đẩy giữa các hành động trạng thái rất giống nhau, nhưng với các mục tiêu khác nhau,

dẫn đến việc không thể học được bất cứ điều gì một cách đúng đắn.

Nói chung chúng ta không gặp phải vấn đề này trong lĩnh vực học tập có giám sát bởi vì chúng ta

học theo đợt ngẫu nhiên trong đó chúng tôi không cập nhật trọng số của mình cho đến khi chúng tôi lặp lại

một số tập hợp con ngẫu nhiên của dữ liệu huấn luyện và tính tổng hoặc độ dốc trung bình cho lô.

Điều này tính trung bình trên các mục tiêu và ổn định việc học tập.

Mục 3.3.2, trải nghiệm lại.

Sự lãng quên thảm khốc có lẽ không phải là điều chúng ta phải lo lắng với biến thể đầu tiên

trò chơi của chúng tôi vì các mục tiêu luôn đứng yên và thực sự mô hình đã thành công

đã học cách chơi nó.

Nhưng với chế độ ngẫu nhiên thì đó là điều chúng ta cần phải quan tâm, và đó chính là lý do tại sao chúng ta cần

để thực hiện một thứ gọi là phát lại trải nghiệm.

Về cơ bản, tính năng phát lại trải nghiệm giúp chúng tôi cập nhật hàng loạt trong chương trình học trực tuyến.

Nó không phải là một vấn đề lớn để thực hiện.

Đây là cách hoạt động của tính năng phát lại trải nghiệm.

Hình 3.13.

1.

Trạng thái S thực hiện hành động A và quan sát trạng thái mới ST cộng 1 và thưởng RT cộng 1.

2.

Lưu cái này dưới dạng một bộ S A ST cộng 1 RT cộng 1 trong danh sách.

3.

Tiếp tục lưu trữ từng trải nghiệm trong danh sách này cho đến khi bạn điền vào danh sách một trải nghiệm cụ thể

chiều dài.

Điều này tùy thuộc vào bạn để xác định.

4.

Sau khi bộ nhớ phát lại trải nghiệm được lấp đầy, hãy chọn ngẫu nhiên một tập hợp con.

Một lần nữa, bạn cần xác định kích thước tập hợp con.

5.

Tương tác thông qua tập hợp con này và tính toán cập nhật giá trị cho từng tập hợp con.

Lưu trữ chúng trong một mảng mục tiêu, chẳng hạn như Y và lưu trữ trạng thái S của từng bộ nhớ trong X.

6.

Sử dụng X và Y như một đợt nhỏ để đào tạo theo đợt.

Đối với các sử thi tiếp theo khi mảng đã đầy, chỉ cần ghi đè các giá trị cũ trong trải nghiệm của bạn

phát lại mảng bộ nhớ.

Hình 3.13.

Đây là tổng quan chung về việc phát lại trải nghiệm, một phương pháp để giảm thiểu một vấn đề lớn

với các thuật toán đào tạo trực tuyến, sự quên lãng thảm khốc.

Ý tưởng là sử dụng việc phân nhóm nhỏ bằng cách lưu trữ các trải nghiệm trong quá khứ và sau đó sử dụng một tập hợp con ngẫu nhiên.

trong số những trải nghiệm này để cập nhật mạng Q thay vì chỉ sử dụng một trải nghiệm gần đây nhất

kinh nghiệm.

Vì vậy, ngoài việc tìm hiểu giá trị hành động của hành động bạn vừa thực hiện, bạn còn

sẽ sử dụng một mẫu ngẫu nhiên các trải nghiệm trong quá khứ để rèn luyện nhằm ngăn chặn sự quên lãng thảm khốc.

Danh sách 3.5 hiển thị thuật toán huấn luyện tương tự từ Danh sách 3.4, ngoại trừ việc phát lại kinh nghiệm

đã thêm vào.

Hãy nhớ rằng, lần này chúng ta đang huấn luyện nó về biến thể khó hơn của trò chơi, trong đó tất cả

các mảnh bảng được đặt ngẫu nhiên trên lưới.

Liệt kê 3.5, DQN với kinh nghiệm phát lại.

Để lưu trữ trải nghiệm của tác nhân, chúng tôi đã sử dụng cấu trúc dữ liệu được gọi là bộ bài trong

Thư viện bộ sưu tập tích hợp của Python.

Về cơ bản, đây là một danh sách mà bạn có thể đặt kích thước tối đa để nếu bạn cố gắng nối thêm

vào danh sách và nó đã đầy, nó sẽ xóa mục đầu tiên trong danh sách và thêm

mục mới vào cuối danh sách.

Điều này có nghĩa là những trải nghiệm mới thay thế những trải nghiệm cũ nhất.

Bản thân các trải nghiệm là các bộ dữ liệu của trạng thái 1, phần thưởng, hành động, trạng thái 2, xong, đó

chúng tôi thêm vào bộ phát lại.

Sự khác biệt chính với đào tạo lặp lại kinh nghiệm là chúng tôi đào tạo theo đợt nhỏ

dữ liệu khi danh sách phát lại của chúng tôi đã đầy.

Chúng tôi chọn ngẫu nhiên một tập hợp con trải nghiệm từ việc phát lại và chúng tôi tách riêng từng trải nghiệm ra.

các thành phần trải nghiệm vào trạng thái 1 lô gạch dưới, lô gạch dưới phần thưởng, gạch dưới hành động

lô và trạng thái lô gạch dưới 2.

Ví dụ: nêu 1 gạch dưới các lô kích thước có kích thước gạch dưới lô là 64 hoặc 100

bằng 64 trong trường hợp này.

Và phần thưởng lô gạch dưới chỉ là một vectơ số nguyên có độ dài 100.

Chúng tôi thực hiện theo cùng một công thức đào tạo như đã làm trước đó với đào tạo hoàn toàn trực tuyến, nhưng

bây giờ chúng tôi đang xử lý các lô nhỏ.

Chúng tôi sử dụng phương pháp tập hợp tenxơ để tập hợp tenxơ Q1, một tenxơ 100 nhân 4, theo

chỉ số hành động, do đó chúng tôi chỉ chọn các giá trị Q liên quan đến các hành động đã được

thực sự được chọn, dẫn đến một vectơ có độ dài 100.

Lưu ý rằng giá trị Q đích, giá trị này, sử dụng lô gạch dưới được thực hiện để đặt phía bên phải

về 0 nếu trò chơi kết thúc.

Hãy nhớ rằng, nếu trò chơi kết thúc sau khi thực hiện một hành động mà chúng tôi gọi là trạng thái kết thúc, thì

không có trạng thái tiếp theo để nhận giá trị Q tối đa.

Vì vậy mục tiêu chỉ trở thành phần thưởng, r được lập chỉ mục bằng t cộng 1.

Biến done là một biến Boolean, nhưng chúng ta có thể thực hiện phép tính trên nó như thể nó là số 0 hoặc

một số nguyên nên ta chỉ lấy 1 trừ xong sao cho nếu thực hiện bằng đúng, 1 trừ thực hiện bằng

bằng 0 và nó đặt số hạng bên phải thành 0.

Lần này chúng tôi đã luyện tập trong 5.000 kỷ nguyên, vì đây là một trò chơi khó hơn, nhưng mặt khác

mô hình mạng Q vẫn giống như trước.

Khi chúng tôi kiểm tra thuật toán, nó có vẻ chơi chính xác hầu hết các trò chơi.

Chúng tôi đã viết một tập lệnh thử nghiệm bổ sung để xem nó thắng bao nhiêu phần trăm trò chơi

1.000 lượt chơi.

Liệt kê 3.6, kiểm tra hiệu suất với tính năng phát lại trải nghiệm.

Khi chúng tôi chạy danh sách 3.6 trên mô hình đã đào tạo của mình, được đào tạo trong 5.000 kỷ nguyên, chúng tôi nhận được khoảng 90%

độ chính xác.

Độ chính xác của bạn có thể tốt hơn một chút hoặc kém hơn.

Điều này chắc chắn cho thấy nó đã học được điều gì đó về cách chơi trò chơi, nhưng không phải vậy.

chính xác những gì chúng ta mong đợi nếu thuật toán thực sự biết nó đang làm gì, mặc dù bạn

có lẽ có thể cải thiện độ chính xác với thời gian đào tạo lâu hơn nhiều.

Một khi bạn thực sự biết cách chơi, bạn sẽ có thể thắng mọi trò chơi.

Có một lưu ý nhỏ rằng một số trò chơi ban đầu có thể thực sự không thể giành chiến thắng,

nên tỷ lệ thắng có thể không bao giờ đạt 100%.

Không có logic nào ngăn cản khung thành ở trong góc, mắc kẹt sau bức tường và

hố, làm cho trò chơi không thể thắng được.

Công cụ trò chơi thế giới lưới ngăn chặn hầu hết các cấu hình bảng không thể thực hiện được, nhưng

một số nhỏ vẫn có thể vượt qua được.

Điều này không chỉ có nghĩa là chúng ta không thể thắng mọi trò chơi mà còn có nghĩa là việc học tập sẽ

bị hư hỏng nhẹ, vì nó sẽ cố gắng thực hiện theo một chiến lược thường có hiệu quả,

nhưng thất bại vì một trò chơi không thể thắng được.

Chúng tôi muốn giữ logic trò chơi đơn giản để tập trung vào việc minh họa các khái niệm, vì vậy chúng tôi đã làm như vậy.

không lập trình theo logic phức tạp cần thiết để đảm bảo 100% trò chơi có thể thắng.

Ngoài ra còn có một lý do khác khiến chúng tôi bị cản trở khi đạt được độ chính xác trên 95%

lãnh thổ.

Hãy nhìn vào biểu đồ lỗ của chúng tôi, được minh họa trong Hình 3.14, cho thấy mức lỗ trung bình đang chạy của chúng tôi.

Của bạn có thể thay đổi đáng kể.

Đối với 3.14, biểu đồ tổn thất DQN sau khi triển khai tính năng phát lại trải nghiệm, cho thấy mức độ giảm rõ ràng

có xu hướng mất mát nhưng vẫn rất ồn ào.

Trong khoản lỗ ở Hình 3.14, bạn có thể thấy nó chắc chắn đang có xu hướng đi xuống, nhưng có vẻ như

khá bất ổn.

Đây là loại cốt truyện mà bạn sẽ hơi ngạc nhiên khi thấy trong một bài toán học có giám sát, nhưng

nó khá phổ biến trong DRL trần.

Cơ chế phát lại kinh nghiệm giúp ổn định quá trình luyện tập bằng cách giảm thiểu thảm họa

quên mất, nhưng còn có những nguồn gây mất ổn định liên quan khác.