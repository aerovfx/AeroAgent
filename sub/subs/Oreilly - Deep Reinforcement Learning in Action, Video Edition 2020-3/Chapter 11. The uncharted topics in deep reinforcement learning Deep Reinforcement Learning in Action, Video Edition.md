# Chương 11. Các chủ đề chưa được khám phá trong học tăng cường sâu Học tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Phần 11.2, các chủ đề chưa được khám phá trong học tăng cường sâu.

Khung quy trình ra quyết định Markov cũng như các hàm giá trị và chính sách mà chúng ta vừa xem xét

được trình bày chi tiết ở chương 2.5.

Sau đó, chúng tôi dành phần còn lại của cuốn sách để triển khai các kỹ thuật phức tạp hơn để đạt được thành công.

giá trị đào tạo và chức năng chính sách trong môi trường khó khăn, ví dụ, môi trường có

phần thưởng thưa thớt và môi trường có nhiều tác nhân tương tác.

May mắn thay, có nhiều điều thú vị mà chúng tôi không có đủ thời gian để trình bày nên chúng tôi sẽ

kết thúc cuốn sách bằng một chuyến tham quan ngắn gọn về một số lĩnh vực khác trong việc học tập củng cố sâu sắc

có thể muốn khám phá.

Chúng tôi sẽ chỉ giới thiệu một số chủ đề mà chúng tôi cho rằng đáng để khám phá thêm và hy vọng bạn

sẽ tự mình xem xét các lĩnh vực này sâu hơn.

Phần 11.2.1, Phát lại Kinh nghiệm Ưu tiên.

Chúng tôi đã đề cập ngắn gọn về ý tưởng Phát lại được ưu tiên trước đó trong cuốn sách khi chúng tôi quyết định

để thêm nhiều bản sao của cùng một trải nghiệm vào bộ nhớ phát lại nếu trải nghiệm đó dẫn đến

đến trạng thái chiến thắng.

Vì các trạng thái chiến thắng rất hiếm và chúng tôi muốn đại lý của mình học hỏi từ những sự kiện mang tính thông tin này,

chúng tôi nghĩ rằng việc thêm nhiều bản sao sẽ đảm bảo rằng mỗi bản sử thi huấn luyện sẽ bao gồm

một vài trong số những sự kiện chiến thắng này.

Đây là một phương tiện rất đơn giản để ưu tiên trải nghiệm trong trò chơi dựa trên tính năng chơi lại.

về mức độ thông tin của họ trong việc đào tạo đại lý.

Thuật ngữ Phát lại trải nghiệm ưu tiên thường đề cập đến một triển khai cụ thể được giới thiệu

trong một bài báo học thuật có tựa đề Phát lại trải nghiệm ưu tiên của Tom Schall, 2015, và nó sử dụng

một cơ chế phức tạp hơn nhiều để ưu tiên trải nghiệm.

Trong quá trình triển khai, tất cả trải nghiệm chỉ được ghi lại một lần, không giống như cách tiếp cận của chúng tôi,

nhưng thay vì chọn một lô nhỏ từ bản phát lại hoàn toàn ngẫu nhiên, nghĩa là,

thống nhất.

Chúng tôi ưu tiên chọn những trải nghiệm có nhiều thông tin hơn.

Họ định nghĩa những trải nghiệm mang tính thông tin không chỉ đơn thuần là những trải nghiệm dẫn đến trạng thái chiến thắng.

giống như chúng tôi đã làm, mà là những điều đó nhằm dự đoán phần thưởng.

Về bản chất, mô hình ưu tiên đào tạo những trải nghiệm đáng ngạc nhiên nhất.

Tuy nhiên, khi mô hình huấn luyện, những trải nghiệm từng gây ngạc nhiên sẽ trở nên ít gây ngạc nhiên hơn và

sở thích liên tục được đánh giá lại.

Điều này dẫn đến hiệu suất đào tạo được cải thiện đáng kể.

Kiểu Phát lại Trải nghiệm Ưu tiên này là phương pháp tiêu chuẩn để củng cố dựa trên giá trị

học, trong khi học tăng cường dựa trên chính sách vẫn có xu hướng dựa vào việc sử dụng nhiều

các tác nhân và môi trường bị tê liệt.

Phần 11.2.2, Tối ưu hóa chính sách gần nhất, PPO.

Trong cuốn sách này, chúng tôi chủ yếu triển khai các mạng Q sâu, DQN, thay vì các chức năng chính sách,

và đây là lý do chính đáng.

Các chức năng chính sách sâu sắc mà chúng tôi triển khai trong chương 4 và 5 khá đơn giản,

và sẽ không hoạt động tốt cho các môi trường phức tạp hơn.

Vấn đề không nằm ở bản thân các mạng chính sách mà nằm ở thuật toán đào tạo.

Thuật toán được tăng cường đơn giản mà chúng tôi sử dụng khá không ổn định khi phần thưởng thay đổi đáng kể

từ hành động này sang hành động khác, thuật toán tăng cường không dẫn đến kết quả ổn định.

Chúng ta cần một thuật toán huấn luyện có thể thực thi các cập nhật mượt mà hơn, hạn chế hơn đối với

mạng lưới chính sách

Tối ưu hóa chính sách gần nhất, PPO, là một thuật toán đào tạo nâng cao hơn cho các phương pháp chính sách

cho phép đào tạo ổn định hơn nhiều.

Nó được giới thiệu trong bài báo Thuật toán tối ưu hóa chính sách gần nhất của John Schulman,

2017, tại OpenAI.

Chúng tôi không đề cập đến PPO trong cuốn sách này vì mặc dù bản thân thuật toán tương đối đơn giản nhưng

hiểu nó đòi hỏi máy móc toán học nằm ngoài phạm vi của phần giới thiệu này

cuốn sách.

Làm cho việc học Q sâu ổn định hơn chỉ cần một vài nâng cấp trực quan như thêm

mạng mục tiêu và triển khai phương pháp học hỏi Q kép, đó là lý do tại sao chúng tôi ưu tiên sử dụng

coi trọng việc học hỏi hơn là các phương pháp chính sách trong cuốn sách này.

Tuy nhiên, trong nhiều trường hợp, việc học trực tiếp một chức năng chính sách sẽ có lợi hơn

một hàm giá trị, chẳng hạn như đối với các môi trường có không gian hành động liên tục, vì chúng ta không thể

tạo DQN trả về vô số giá trị Q cho mỗi hành động.

Phần 11.2.3, học tăng cường theo cấp bậc và khung lựa chọn.

Khi một đứa trẻ tập đi, chúng không nghĩ đến từng sợi cơ nào

để kích hoạt và trong bao lâu.

Hoặc khi một doanh nhân tranh luận về một quyết định kinh doanh với đồng nghiệp, họ không hề suy nghĩ

về các chuỗi âm thanh riêng lẻ mà họ cần tạo ra để người khác hiểu được

chiến lược kinh doanh của họ.

Hành động của chúng ta tồn tại ở nhiều mức độ trừu tượng khác nhau, từ việc di chuyển các cơ riêng lẻ cho đến việc vận động lớn.

nhận thấy rằng một câu chuyện được tạo thành từ các chữ cái riêng lẻ, nhưng những chữ cái đó được ghép thành

các từ được ghép thành câu, đoạn văn, v.v.

Người viết có thể đang nghĩ đến một cảnh chung tiếp theo trong câu chuyện, và chỉ khi cảnh đó

đã quyết định, liệu họ có thực sự gõ được từng ký tự riêng lẻ hay không.

Tất cả các tác nhân chúng tôi triển khai trong cuốn sách này đều hoạt động ở cấp độ đánh máy riêng lẻ.

nhân vật, có thể nói như vậy.

Họ không có khả năng suy nghĩ ở cấp độ cao hơn.

Học tăng cường kiến trúc cao hơn là một cách tiếp cận để giải quyết vấn đề này, cho phép

các tác nhân để xây dựng các hành động cấp cao hơn từ các hành động cấp thấp hơn.

Trong đại lý thế giới lưới của chúng tôi quyết định từng bước phải làm gì, nó có thể khảo sát

lên bảng và quyết định trình tự hành động ở cấp độ cao hơn.

Nó có thể học các trình tự có thể tái sử dụng như di chuyển lên cao hoặc di chuyển xung quanh chướng ngại vật.

có thể được thực hiện ở nhiều trạng thái trò chơi khác nhau.

Sự thành công của học sâu và học tăng cường là nhờ khả năng biểu diễn

các trạng thái nhiều chiều phức tạp trong một hệ thống phân cấp các biểu diễn trạng thái cấp cao hơn.

Trong học tăng cường theo cấp bậc, mục tiêu là mở rộng điều này để biểu diễn các trạng thái

và hành động theo thứ bậc.

Một cách tiếp cận phổ biến cho vấn đề này được gọi là Khung Tùy chọn.

Hãy xem xét thế giới lưới, trong đó có bốn hành động cơ bản là lên, phải, trái và xuống, và

mỗi hành động kéo dài một bước thời gian.

Trong khung tùy chọn, có các tùy chọn thay vì chỉ có các hành động nguyên thủy.

Một quyền chọn là sự kết hợp của một chính sách quyền chọn, giống như một chính sách thông thường có một trạng thái

và trả về phân phối xác suất cho các hành động, điều kiện kết thúc và

tập đầu vào, là tập hợp con của các trạng thái.

Ý tưởng là một tùy chọn cụ thể sẽ được kích hoạt khi tác nhân gặp một trạng thái

trong bộ đầu vào tùy chọn và chính sách tùy chọn cụ thể đó được chạy cho đến khi chấm dứt

điều kiện được đáp ứng, tại thời điểm đó một tùy chọn khác có thể được chọn.

Các chính sách tùy chọn này có thể là các chính sách đơn giản hơn một chính sách mạng thần kinh đơn lẻ, lớn, sâu

mà chúng tôi đã thực hiện trong cuốn sách này.

Nhưng bằng cách lựa chọn một cách thông minh các phương án cấp cao hơn này, bạn có thể đạt được hiệu quả

bằng cách không phải sử dụng chính sách tính toán chuyên sâu hơn để lấy từng nguyên mẫu

bước.

Mục 11.2.4 Lập kế hoạch dựa trên mô hình

Chúng ta đã thảo luận về ý tưởng về mô hình và học tăng cường trong hai bối cảnh.

Đầu tiên, một mô hình chỉ đơn giản là một thuật ngữ khác để chỉ một hàm gần đúng như một nơron

mạng.

Đôi khi chúng ta chỉ coi mạng nơ-ron của mình như một mô hình, vì nó gần đúng hoặc mô hình

hàm giá trị hoặc hàm chính sách.

Bối cảnh khác là khi chúng ta đề cập đến việc học tập dựa trên mô hình và không có mô hình.

Trong cả hai trường hợp, chúng tôi đang sử dụng mạng thần kinh làm mô hình của hàm giá trị hoặc chính sách,

nhưng trong trường hợp này dựa trên mô hình có nghĩa là tác nhân đang đưa ra quyết định dựa trên một cách rõ ràng

mô hình được xây dựng về động lực của chính môi trường chứ không chỉ là giá trị của nó

chức năng.

Trong học tập không có mô hình, tất cả những gì chúng ta quan tâm là học cách dự đoán chính xác phần thưởng.

có thể hoặc không thể đòi hỏi sự hiểu biết sâu sắc về cách thức hoạt động thực sự của môi trường.

Trong học tập dựa trên mô hình, chúng tôi thực sự muốn tìm hiểu cách hoạt động của môi trường.

Nói một cách ẩn dụ, trong học tập không có mô hình, chúng ta hài lòng khi biết rằng có điều gì đó

được gọi là lực hấp dẫn làm cho mọi thứ rơi xuống và chúng ta sử dụng hiện tượng này, nhưng trong mô hình dựa trên

học tập mà chúng tôi muốn thực sự gần đúng với định luật hấp dẫn.

DQN không có mô hình của chúng tôi hoạt động hiệu quả một cách đáng ngạc nhiên, đặc biệt khi kết hợp với các tiến bộ khác

như sự tò mò.

Vậy lợi ích của việc học rõ ràng một mô hình môi trường là gì?

Với mô hình môi trường rõ ràng và chính xác, tác nhân có thể học cách thực hiện các hoạt động lâu dài

kế hoạch thay vì chỉ quyết định hành động tiếp theo sẽ thực hiện.

Bằng cách sử dụng mô hình môi trường của nó để dự đoán tương lai trước vài bước thời gian, nó có thể

đánh giá hậu quả lâu dài của các hành động trước mắt và điều này có thể dẫn đến việc thực hiện nhanh hơn

học tập, do hiệu quả mẫu tăng lên.

Điều này có liên quan nhưng không nhất thiết phải giống với việc học tăng cường theo cấp bậc.

chúng ta đã thảo luận, vì việc học tăng cường theo cấp bậc không nhất thiết phụ thuộc vào một

mô hình môi trường

Nhưng với mô hình môi trường, tác nhân có thể lập kế hoạch cho một chuỗi các hành động nguyên thủy

để hoàn thành một số mục tiêu ở cấp độ cao hơn.

Cách đơn giản nhất để huấn luyện một mô hình môi trường là chỉ cần có một deep learning riêng biệt

mô-đun dự đoán các trạng thái trong tương lai.

Trên thực tế, chúng tôi đã làm điều đó ở chương 8 về học tập dựa trên sự tò mò, nhưng chúng tôi đã không sử dụng

mô hình môi trường để lập kế hoạch hoặc nhìn vào tương lai.

Chúng tôi chỉ sử dụng nó để khám phá những trạng thái đáng ngạc nhiên.

Nhưng với mô hình M của ST, nó nhận một trạng thái và trả về trạng thái tiếp theo được dự đoán, ST plus

1, sau đó chúng tôi có thể lấy trạng thái tiếp theo được dự đoán đó và đưa nó trở lại mô hình để có được

trạng thái dự đoán ST cộng 2, v.v.

Khoảng cách tới tương lai mà chúng ta có thể dự đoán phụ thuộc vào tính ngẫu nhiên vốn có trong

môi trường và độ chính xác của mô hình.

Nhưng ngay cả khi chúng ta chỉ có thể dự đoán chính xác một vài bước thời gian trong tương lai, thì điều này

sẽ vô cùng hữu ích.

Trong 11.2.5, tìm kiếm cây Monte Carlo, MCTS, nhiều trò chơi có tập hữu hạn các hành động và hữu hạn

độ dài, chẳng hạn như cờ vua, cờ vây và tic-tac-toe.

Thuật toán deep blue mà IBM phát triển để chơi cờ vua không sử dụng máy học

không hề.

Đó là một thuật toán mạnh mẽ sử dụng hình thức tìm kiếm cây.

Hãy xem xét trò chơi tic-tac-toe.

Đây là trò chơi hai người chơi thường được chơi trên một lưới hình vuông 3x3, trong đó người chơi 1 đặt

một mã thông báo hình chữ x và người chơi 2 đặt một mã thông báo hình chữ o.

Mục tiêu của trò chơi là trở thành người đầu tiên có được ba mã thông báo của bạn xếp thành một hàng,

cột hoặc đường chéo.

Trò chơi đơn giản đến mức chiến lược của con người thường liên quan đến việc tìm kiếm cây một cách hạn chế.

Nếu bạn là người chơi thứ 2 và đã có một mã thông báo đối nghịch trên lưới, bạn có thể xem xét

tất cả các phản hồi có thể có đối với tất cả các không gian mở có thể có mà bạn có và bạn có thể tiếp tục làm điều này

cho đến khi kết thúc trò chơi.

Tất nhiên, ngay cả đối với bàn cờ 3x3, nước đi đầu tiên có 9 hành động có thể thực hiện được và có

8 hành động có thể thực hiện được cho người chơi 2 và sau đó lại là 7 hành động có thể thực hiện được cho người chơi 1, do đó

số lượng quỹ đạo có thể, cây trò chơi, trở nên khá lớn, nhưng có thể sử dụng hết sức mạnh

tìm kiếm như thế này có thể được đảm bảo giành chiến thắng trong trò chơi tic-tac-toe, giả sử đối thủ không sử dụng

cách tiếp cận tương tự.

Đối với một trò chơi như cờ vua, cây trò chơi quá lớn để có thể sử dụng vũ lực hoàn toàn

tìm kiếm cây trò chơi.

Người ta nhất thiết phải giới hạn số lượng các động thái tiềm năng để xem xét.

Màu xanh đậm đã sử dụng thuật toán tìm kiếm dạng cây hiệu quả hơn tìm kiếm toàn diện,

nhưng vẫn không tham gia học tập.

Vấn đề vẫn là tìm kiếm các quỹ đạo có thể và chỉ tính toán quỹ đạo nào dẫn đến chiến thắng.

tiểu bang.

Một cách tiếp cận khác là tìm kiếm cây Monte Carlo, trong đó bạn sử dụng một số cơ chế tìm kiếm ngẫu nhiên.

lấy mẫu một tập hợp các hành động tiềm năng và mở rộng cây từ đó, thay vì xem xét

tất cả các hành động có thể.

Thuật toán AlphaGo do DeepMind phát triển để chơi trò chơi.

Go đã sử dụng mạng lưới thần kinh sâu để đánh giá những hành động nào đáng thực hiện tìm kiếm trên cây

và cũng để quyết định giá trị của các nước đi đã chọn.

Do đó, AlphaGo đã kết hợp tìm kiếm mạnh mẽ với mạng lưới thần kinh sâu để có được kết quả tốt nhất

của cả hai.

Những loại thuật toán kết hợp này hiện đang là công nghệ tiên tiến dành cho các trò chơi trong

lớp cờ vua và đi.