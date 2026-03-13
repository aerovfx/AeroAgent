# 3 -CodeChallenge Tạo và trực quan hóa token (phần 1)

---

Chào mừng bạn đến với thử thách viết mã đầu tiên trong khóa học này.

Nếu bạn là người mới tham gia các khóa học của tôi và chưa thực hiện thử thách viết mã thì tôi khuyến khích bạn xem phần

video giới thiệu trong đó tôi giải thích những video thử thách mã này là gì, cách chúng hoạt động và cách bạn có thể giải quyết

họ.

Vì vậy, có một số mục tiêu trong thử thách viết mã này.

Bạn sẽ có thêm kinh nghiệm trong việc tạo và làm việc với bộ mã hóa và bộ giải mã.

Bạn sẽ tìm hiểu cách xác định mã thông báo mục tiêu và trích xuất ngữ cảnh của chúng.

Và bạn sẽ tìm hiểu ý nghĩa của một mã hóa nóng.

Và bạn sẽ có thể hình dung cả mã hóa nóng và mã thông báo dựa trên số nguyên.

Có rất nhiều việc phải làm.

Tôi sẽ chia video này thành hai video riêng biệt.

Vậy hãy bắt đầu với bài tập một.

Mục tiêu của bài tập một là tạo ra các hàm mã hóa và giải mã.

Bây giờ bạn sẽ bắt đầu với văn bản mà bạn thấy ở đây.

Đó là văn bản tương tự như trong video trước.

Và sau đó bạn muốn tách văn bản thành các từ viết thường.

Và sau đó trích xuất một tập hợp bao gồm các từ duy nhất.

Sau đó sử dụng khả năng hiểu từ điển để tạo từ điển bộ mã hóa và bộ giải mã.

Và đó là những gì bạn thấy ở đây.

Và tất nhiên là tôi đã xóa nó đi.

Vì vậy, bạn có thể tự mình làm tất cả.

Bây giờ nếu bạn chưa quen với việc hiểu từ điển trong Python thì về cơ bản thì nó cũng giống như vậy

để hiểu danh sách, chỉ cần sử dụng dấu ngoặc nhọn để tạo từ điển thay vì dấu ngoặc vuông để

tạo một danh sách.

Trên thực tế, tôi đã cho bạn xem rất nhiều đoạn mã để giải bài tập này trong video trước.

Vì vậy, nếu gặp khó khăn, bạn có thể quay lại tệp mã từ video trước và điều đó sẽ giúp bạn

bắt đầu.

Được rồi, khi bạn nhìn thấy màn hình này, đây là cơ hội để bạn tạm dừng video.

Chuyển sang Python và giải bài tập hoặc ít nhất là đạt được nhiều tiến bộ nhất có thể.

Và khi bạn đã sẵn sàng hoặc nếu gặp khó khăn, bạn hãy quay lại video.

Và bây giờ tôi sẽ chuyển sang Python và xem xét giải pháp của mình.

Như tôi đã đề cập ở video trước, bạn luôn có thể xem tôi đang làm việc với tệp mã nào bằng cách xem

lên phía trên bên trái màn hình của bạn ở đây.

Được rồi, ở đây chúng ta sẽ nhập lại một số thư viện để thực hiện việc tách văn bản thành các từ.

Và vâng, numpy và matplotlib.

Tôi thường bao gồm hai dòng này ở đây.

Điều này không cần thiết đối với matplotlib.

Nó chỉ yêu cầu matplotlib vẽ các hình ở định dạng vector thay vì định dạng pixel.

Và điều đó tốt cho việc xuất các số liệu, nhưng nó cũng chỉ làm cho chúng sắc nét hơn một chút, một chút

độ phân giải cao hơn một chút.

Được rồi.

Dù sao đi nữa, chúng ta hãy đi tập thể dục một.

Vì vậy, ở đây chúng ta có văn bản giống hệt như trong bài tập trước.

Và tách thành lời.

Và việc tạo từ vựng này cũng giống hệt như video trước.

Bây giờ từ điển bộ mã hóa và bộ giải mã ở đây cũng giống hệt như những gì tôi đã trình bày trong đoạn mã

tập tin trong video trước.

Điểm khác biệt duy nhất là trong video trước tôi đã sử dụng vòng lặp for, do đó, vòng lặp for có nhiều dòng.

Và ở đây tôi cũng đang làm điều tương tự.

Tôi đang thực hiện phép tính Python tương tự.

Nhưng ở đây tôi đang sử dụng khả năng hiểu từ điển chỉ để diễn đạt tất cả những điều này trong một dòng.

Vì vậy, nó đẹp và nhỏ gọn.

Nhưng bạn có thể thấy vòng lặp for ở đây.

Vì vậy, đối với chỉ mục I và phần tử trong danh sách từ vựng.

Sau đó, chúng ta chỉ cần đặt khóa mà chúng ta gọi là từ có hoặc có mục I, là số nguyên.

Được rồi.

Và rồi vâng.

Vì vậy đây là những từ cần lập chỉ mục.

Chỉ mục cho các từ theo đúng nghĩa đen là điều tương tự ở đây.

Chúng tôi chỉ trao đổi thứ tự.

Siêu đơn giản.

Được rồi.

Vì vậy, điều này cung cấp cho chúng tôi từ điển bộ mã hóa và bộ giải mã.

Và trong bài tập tiếp theo, chúng ta sẽ gói nó thành các hàm.

Bây giờ đến bài tập thứ hai.

Đây thực sự chỉ là một phần mở rộng nhỏ của bài tập trước.

Về cơ bản bạn chỉ muốn lấy từ điển bộ mã hóa và bộ giải mã mà bạn vừa tạo ở phần trước

tập thể dục và đưa chúng vào các hàm Python.

Vì vậy, bạn sẽ có một chức năng cho bộ mã hóa và một chức năng cho bộ giải mã.

Vì vậy, ý tưởng của các hàm này là bạn có thể đưa văn bản làm đầu vào cho hàm mã hóa và nhận được

danh sách các số nguyên làm đầu ra.

Và đối với hàm giải mã, hàm đó lấy danh sách các số nguyên làm đầu vào và đưa ra văn bản là

đầu ra.

Được rồi, đó là phần đầu tiên của bài tập thứ hai.

Phần tiếp theo của bài tập này là tạo một câu mới mà bạn có thể kiểm tra các chức năng này.

Bây giờ bạn muốn đảm bảo rằng bạn chỉ sử dụng các từ trong từ vựng hiện có.

Đối với bài tập này, không đưa vào câu này bất kỳ từ nào chưa có sẵn ở đây

trong từ vựng mà bạn đã tạo ở đây trong bài tập.

Bây giờ, chúng ta sẽ quay lại vấn đề này trong tương lai và thảo luận xem phải làm gì khi bạn có lời nói

không có trong từ vựng.

Vì vậy tôi hứa chúng ta sẽ quay lại vấn đề đó sau.

nhưng bây giờ, đối với bài tập hai, hãy tạo một câu mới chỉ sử dụng những từ đã có trong

từ ngữ.

Được rồi.

Và về cơ bản điều bạn muốn kiểm tra ở đây là hàm mã hóa và giải mã thực sự là nghịch đảo

của nhau.

Nghịch đảo không tổn hao.

Vì vậy, khi bạn nhập văn bản vào bộ mã hóa, nó sẽ cung cấp cho bạn danh sách các số nguyên mà bạn nhập vào

vào bộ giải mã và bạn sẽ có thể khôi phục văn bản gốc.

Vì vậy, bạn có thể viết mã về cơ bản sẽ tạo ra kết quả như thế này.

Vì vậy, đây là câu mới mà tôi đã viết.

Chúng ta đã là kết quả của điều mà mọi người khác đã nghĩ rồi.

Và ở đây tôi đã chuyển nó thành số.

Vì vậy, thành các chỉ số mã thông báo bằng cách sử dụng chức năng mã hóa.

Và sau đó tôi lấy các chỉ số mã thông báo này và đặt nó làm đầu vào cho hàm giải mã và mã được giải mã.

văn bản hoàn toàn giống với văn bản gốc.

Vì vậy, chúng tôi đã chuyển từ văn bản sang mã thông báo và sau đó quay lại văn bản.

Được rồi, hãy tạm dừng video và mã hóa.

Và bây giờ tôi sẽ chuyển sang Python và chỉ cho bạn giải pháp của tôi.

Đây là chức năng cho bộ mã hóa.

Bạn có thể thấy rằng tôi vẫn đang sử dụng từ điển bộ mã hóa mà chúng ta đã tạo trong bài tập trước.

Và về cơ bản những gì tôi đang làm là lấy văn bản đầu vào rồi chia nó thành các từ theo

không gian.

Đặt nó thành chữ thường để chúng ta không phải lo lắng về độ phân biệt chữ hoa chữ thường trong vốn từ vựng của mình.

Và sau đó với những từ này, tôi chỉ tra cứu tất cả các từ.

Vì vậy, uh, cho w vào trong.

Vì vậy với mỗi phần tử, từng từ riêng lẻ trong toàn bộ văn bản được phân đoạn hoặc chia thành các từ, chúng ta

tìm số tương ứng.

Vậy mục tương ứng với từ khóa của từ đó.

Được rồi.

Vì vậy, đó là chức năng mã hóa.

Chức năng giải mã đơn giản hơn một chút.

Chúng tôi lấy các chỉ số làm đầu vào và chúng tôi chỉ cần tra cứu từng từ riêng lẻ tương ứng với

mỗi chỉ số này và sau đó nối chúng lại với nhau bằng dấu cách.

Được rồi.

Vì vậy, đó là phần đó.

Và bây giờ tôi đang in ra từ vựng.

Lại.

Đây chỉ là lời nhắc nhở để khi tạo văn bản mới, chúng ta có thể chắc chắn rằng mình chỉ đang sử dụng

những từ có sẵn trong từ vựng hiện có.

Được rồi.

Và ở đây tôi đã cho bạn xem trong slide câu nói của tôi là gì.

Và vâng, tôi cũng đã cho bạn xem ảnh chụp màn hình của cái này.

Vì vậy, về cơ bản, ý tưởng là chúng ta bắt đầu bằng văn bản.

Chúng ta chuyển đổi văn bản thành số và sau đó chúng ta chuyển đổi số trở lại thành văn bản.

Và chúng tôi chỉ muốn thấy rằng cuối cùng mọi thứ đều phù hợp.

Vậy văn bản này cũng giống như văn bản này.

Bây giờ là bài tập thứ ba.

Mục tiêu của bài tập thứ ba là tạo ra hình ảnh này.

Vậy chúng ta đang nhìn vào cái gì ở đây?

Vì vậy, trên trục x bạn sẽ thấy từ chỉ mục.

Vì vậy đây chỉ là vị trí thứ tự của từ trong câu.

Và cũng cần nói rõ đây là câu gốc của bài tập 1, không phải văn bản mới bạn tạo

trong bài tập hai.

Được rồi.

Vì vậy, bây giờ ở đây trên trục y bên trái, bạn thấy các số nguyên từ 0 đến 20 tương ứng với 21 số duy nhất

mã thông báo trong từ vựng của chúng tôi.

Và ở đây trên trục bên phải, tôi đã gắn nhãn tất cả các số nguyên đó theo mã thông báo thực tế.

Vì vậy, đây là các chỉ số mã thông báo và đây là văn bản mã thông báo.

Và về cơ bản biểu đồ này hiển thị giá trị của từng token được vẽ trên trục y theo vị trí của nó

trong câu trên trục x.

Vì vậy, đây là mô tả trực quan về cách thể hiện câu được mã hóa.

Và tôi nghĩ nó trông cũng khá gọn gàng.

Bạn có thể tạo ra âm nhạc từ điều này, mặc dù tôi không chắc nó sẽ thực sự thú vị đến thế.

Dù sao đi nữa, tôi hy vọng bạn thích thực hiện bài tập này và bây giờ tôi sẽ trình bày giải pháp của mình.

Vì vậy, ở đây tôi đang sử dụng chức năng mã hóa trên tất cả văn bản.

Vì vậy, tất cả văn bản mà tôi viết ở đầu bài tập đều mở ra một hình.

Và bây giờ tôi đang vẽ các mã thông báo ở đây.

Và thực sự hãy để tôi bắt đầu với điều này chỉ để cho thấy nó trông ổn như thế nào.

Vì vậy, một lần nữa trục x là vị trí thứ tự của các chỉ số mã thông báo tương ứng với các từ riêng lẻ

trong văn bản.

Được rồi.

Và khi đó chiều cao hoặc vị trí trên trục y của mỗi hình vuông này tương ứng với giá trị

của chỉ số.

Vì vậy, chỉ số mã thông báo uh đầu tiên xảy ra bằng 0, chỉ số thứ hai là 14.

Và vân vân được rồi.

Và sau đó tôi sẽ thêm các đường lưới.

Và ở đây tôi chỉ đang thiết lập các trục thôi.

Vì vậy, điều đó làm cho nó trông đẹp hơn một chút.

Và sau đó tất cả mã này về cơ bản chỉ là thiết lập trục thứ hai ở đây bên phải.

Để tôi cũng có thể dán nhãn những thứ này ở bên phải.

Vì vậy, có một chút khó hiểu trong Python để làm cho nó hoạt động.

Nhưng về cơ bản những gì bạn làm là tạo ra một trục song sinh.

Vậy đây là một trục mới.

Vì vậy, bạn có thể thấy ở đây đây là trục biến thiên đề cập đến trục này.

Đây là x hai.

Vì vậy, nó là một trục mới nhưng nó được kết đôi.

Nó được ghép với trục này nên nó chồng lên nhau.

Và sau đó tôi vẽ các mã thông báo có alpha bằng 0.

Đây là những dấu hiệu vô hình mà tôi đang vẽ ở đây để có thể nhìn xuyên qua một cách hoàn hảo.

Và đó là cách tôi có thể chỉ định trục y ở đây.

Bây giờ là bài tập thứ tư.

Bạn sẽ thấy xuyên suốt khóa học này, nhưng đặc biệt là khi chúng ta đi sâu vào khả năng diễn giải cơ học

các phần mà bạn thường cần xác định vị trí của một mã thông báo cụ thể trong chuỗi mã thông báo.

Bây giờ, việc này không đơn giản chỉ là đếm từ, bởi vì các kế hoạch mã thông báo thực sự có sự kết hợp của

ký tự, từ phụ và từ đầy đủ.

Vì vậy, mục tiêu ở đây trong bài tập này là tìm tất cả các chỉ số tương ứng với từ two.

Và một lần nữa, bạn muốn làm việc với văn bản từ bài tập một chứ không phải văn bản bạn đã tạo trong bài tập

hai.

Bây giờ từ hai này xuất hiện hai lần trong văn bản và bạn cũng muốn in ra từng vị trí đó

như bối cảnh.

Bây giờ bối cảnh là gì?

Bối cảnh của mã thông báo mục tiêu là gì?

Chà, bối cảnh trong bối cảnh xử lý ngôn ngữ tự nhiên đề cập đến các mã thông báo ngay trước

mã thông báo mục tiêu và đôi khi cũng đứng sau mã thông báo mục tiêu.

Bây giờ, liệu một mô hình có được phép nhìn vào tương lai hay không phụ thuộc vào chi tiết đào tạo mô hình

và mục tiêu của mô hình.

Tôi đã đề cập ngắn gọn về điều đó trong vài video trước và tôi sẽ còn nhiều điều để nói về

điểm này sau này trong khóa học.

Hiện tại, chỉ cần nói rằng bạn muốn in mã thông báo trước và mã thông báo sau dưới dạng ngữ cảnh là đủ

cho từng mục tiêu mã thông báo.

Được rồi.

Bây giờ, ngữ cảnh nói chung rất quan trọng trong mô hình hóa ngôn ngữ bởi vì việc giải thích bất kỳ ngữ cảnh cụ thể nào

từ phụ thuộc vào các từ đứng trước nó.

Điều đó khá rõ ràng.

Bạn biết đấy, bạn sẽ hiểu từ cọ vẽ rất khác nhau tùy thuộc vào việc trước đây tôi có sử dụng

từ răng hoặc tóc.

Được rồi.

Dù sao đi nữa, mã và đầu ra Python chính xác cho bài tập này sẽ cho kết quả giống như

cái này.

Thế là tôi in ra chữ hai xuất hiện ở các chỉ số này.

Vì vậy, chỉ số 12 và 16.

Đây là các vị trí thứ tự trong văn bản mà chúng xuất hiện.

Và sau đó việc tôi làm là in ra hai mã thông báo này và cả ngữ cảnh.

Vì vậy, mã thông báo trước và mã thông báo bài đăng.

Bây giờ đừng nhầm lẫn ở đây.

Đây là những chỉ số thứ tự trong câu.

Và những con số này ở đây đề cập đến những dấu hiệu trong từ vựng.

Vì vậy, chỉ số mã thông báo trong vocab.

Được rồi, 17 là số tương ứng với mã thông báo hai.

Và lần đầu tiên nó xuất hiện trong văn bản, chúng tôi cho rằng bối cảnh đó là như vậy.

Và lần thứ hai không phải bằng cách nào đó nghe có vẻ giống Shakespeare.

Dù sao, đó là mục tiêu của bạn cho bài tập này.

Và bây giờ tôi sẽ chuyển sang Python và chỉ cho bạn giải pháp của tôi.

Tôi bắt đầu ở đây bằng cách tìm chỉ mục mục tiêu.

Vậy chỉ số số, số nguyên trong từ vựng tương ứng với từ mục tiêu mà chúng ta đang tìm kiếm

đang tìm kiếm ổn.

Và hóa ra đó là 17.

Được rồi.

Và ở đây tôi chỉ đang tìm vị trí mà từ mục tiêu xuất hiện trong vectơ của tất cả các chỉ số.

Được rồi.

Và sau đó tôi sẽ in nó ra.

Và sau đó tôi in ra mục tiêu và mã thông báo.

Vậy từ t trừ một đến t cộng hai.

Và vâng, đó là vì t là vị trí của mục tiêu mà chúng ta quan tâm.

Và tất nhiên chúng ta thực hiện T cộng hai chứ không phải T cộng một vì đây là giới hạn trên độc quyền trong Python.

Vì vậy, điều này kết thúc bằng việc in T cộng một.

Mặc dù chúng tôi chỉ định t cộng hai là giới hạn trên độc quyền.

Được rồi, vậy chúng ta đi thôi.

Chúng ta thấy từ mục tiêu và ngữ cảnh mà các mô hình ngôn ngữ sẽ sử dụng để giúp diễn giải từ này.

Vậy là đã hoàn thành các bài tập từ một đến bốn.

Bây giờ tôi sẽ dừng video và tiếp tục thử thách viết mã này trong video tiếp theo.

Và về cơ bản đó là cách tôi khuyến khích bạn nghỉ ngơi một chút.

Vậy xin vui lòng đứng dậy khỏi bàn làm việc, đi lại xung quanh, uống một cốc nước, uống cà phê và

quay lại làm bài tập thứ năm.