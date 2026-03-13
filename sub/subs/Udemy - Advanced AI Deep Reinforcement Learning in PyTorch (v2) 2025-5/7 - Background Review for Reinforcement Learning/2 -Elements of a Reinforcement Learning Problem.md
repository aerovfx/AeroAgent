# 2 -Các yếu tố của một bài toán học tăng cường đã được dịch

---

Trong bài giảng này, chúng ta sẽ thảo luận về học tăng cường từ quan điểm kỹ thuật hơn, và điều này

sẽ cho phép chúng ta định nghĩa hầu hết các thuật ngữ liên quan đến các vấn đề học tăng cường.

Tôi rất tin tưởng vào việc học bằng ví dụ, vì vậy trong bài giảng này sẽ không đề cập nhiều đến

định nghĩa trừu tượng và kỹ thuật vì nó nhằm cung cấp ví dụ về mọi thứ.

Hãy bắt đầu với các đối tượng chính trong bài toán học tăng cường, tác nhân và môi trường.

Ví dụ tốt nhất về điều này là chính bạn. Bạn là một tác nhân và thế giới là môi trường của bạn.

Có thể mục tiêu dài hạn của bạn là đạt điểm cao trong bài kiểm tra toán. Và như vậy, giống như việc lái xe tự hành

đến đích, bạn phải quan sát môi trường của mình và đưa ra những quyết định đúng đắn hàng ngày trong

để đạt được mục tiêu của bạn. Điều đó có nghĩa là học bài, đến lớp, ghi chép, làm bài tập về nhà,

đặt câu hỏi khi bạn bối rối, v.v. Đó là một ví dụ cơ bản.

Đây là một ví dụ khác gần với mục đích mà chúng ta thực sự có thể sử dụng phương pháp học tăng cường.

Giả sử bạn đang viết một chương trình chơi Tiktak Toe. Tác nhân là gì và môi trường là gì?

Trong trường hợp này, môi trường bao gồm chương trình máy tính thực hiện trò chơi Tiktak Toe này.

Tất nhiên, chương trình máy tính này cũng có thể liên quan đến một số dạng AI sẽ đóng vai trò là người chơi khác trong

trò chơi, nhưng với tất cả ý định và mục đích, hãy giả vờ như đó là một loạt các câu lệnh if và

những quy tắc được xác định trước. Vì vậy, bản thân nó không phải là trí thông minh, nó chỉ là một chương trình máy tính được viết bởi ai đó

mặt khác, chỉ là một phần của chương trình Tiktak Toe lớn hơn. Bạn có thể tưởng tượng rằng chương trình Tiktak Toe này

sẽ có một API cho phép bạn tương tác với nó theo chương trình. Vì vậy, ví dụ,

có thể có chức năng để bắt đầu một trò chơi mới. Có thể có một chức năng để đặt x hoặc của bạn

o tại một số vị trí trên bảng. Có thể có chức năng đọc trạng thái của bảng để bạn

có thể thấy tất cả x và o đã được đặt ở đâu cho đến nay. Có thể có một chức năng để kiểm tra xem

trò chơi kết thúc và nếu vậy, ai đã thắng trò chơi, máy tính hay người đại diện của bạn? Vì vậy, đó là môi trường.

Mặt khác, đại lý của bạn sẽ là một chương trình máy tính khác có giao diện với Tiktak Toe

chương trình. Đại lý của bạn có thể sử dụng một thuật toán chẳng hạn như thuật toán từ học tăng cường để

học cách chơi Tiktak Toe từ kinh nghiệm. Nó sử dụng API để giao tiếp với môi trường.

Vì vậy, ở đây chúng tôi có một chương trình chơi trò chơi. Một phần của mã này là nơi tác nhân đọc trạng thái

của bảng trò chơi và chọn hành động thông minh nhất. Đó là AI của chúng tôi được đại diện bởi đại lý của chúng tôi.

Đây là một ví dụ phổ biến khác, trò chơi điện tử. Đây là một trò chơi Atari cổ điển nổi tiếng được gọi là Breakout.

Nhân tiện, nếu bạn không biết trò chơi này hoạt động như thế nào thì có rất nhiều nơi bạn có thể chơi trò này

trò chơi trực tuyến miễn phí. Vì vậy, nếu bạn chưa bao giờ chơi trò chơi này trước đây, hãy chơi thử.

Trong trò chơi này, môi trường rõ ràng chính là trò chơi. Mục tiêu là xóa tất cả các khối,

và công việc của bạn là di chuyển mái chèo sao cho quả bóng phá hủy các khối nhưng không bao giờ rơi

xuống đất. Tác nhân sẽ là chương trình máy tính của bạn, có thể đọc thông tin từ trò chơi,

giống như màn hình hiện tại trông như thế nào. Vì vậy, nó có thể tìm ra vị trí của các khối, bàn đạp ở đâu,

quả bóng sẽ đi đến đâu, v.v. Công việc của nó là kiểm soát mái chèo đi đâu. Vì vậy, về cơ bản,

bạn có thể di chuyển sang trái, sang phải hoặc không làm gì cả.

Tiếp theo, hãy tiếp tục xác định thêm các thuật ngữ. Cho đến nay, bạn đã biết về người châu Á và môi trường.

Thuật ngữ tiếp theo tôi muốn định nghĩa là tập phim. Điều gì xảy ra khi tôi chơi trò chơi TikTok hoặc Breakout?

Chà, một số chuỗi sự kiện sẽ xảy ra, và rồi cuối cùng, tôi sẽ thắng hoặc thua.

Với ví dụ về bài kiểm tra toán của tôi, bạn sẽ làm bài kiểm tra toán và sau đó bạn sẽ nhận được điểm.

Bây giờ, chúng ta biết rằng, với các thuật toán học, cách chúng học là bằng dữ liệu.

Vì vậy, nếu bạn đang huấn luyện bộ phân loại chó và mèo, bạn sẽ cần rất nhiều hình ảnh được gắn nhãn về chó và mèo.

Tương tự, với TikTok hoặc Breakout, sau khi trò chơi kết thúc, tôi có thể chọn chơi lại.

Đây là phương pháp mà qua đó tôi sẽ có được kinh nghiệm, hoặc có được nhiều dữ liệu kỹ thuật hơn.

Bạn có thể gọi những trò chơi này là những vòng đấu hoặc những trận đấu, nhưng trong học tăng cường, thuật ngữ chính thức là tập.

Vì vậy, khi bạn đào tạo một đặc vụ chơi TikTok, bạn sẽ phát nhiều tập,

và vào cuối mỗi tập, người đại diện của bạn sẽ có một hoặc bị mất.

Hy vọng đến cuối quá trình đào tạo, hay nói cách khác, sau nhiều tập,

đại lý của bạn sẽ thắng nhiều hơn thua.

Tất nhiên, không phải tất cả các môi trường học tăng cường đều diễn ra theo từng giai đoạn.

Nói một môi trường có tính chất phân đoạn có nghĩa là chúng kết thúc vào một thời điểm nào đó và bạn có thể bắt đầu lại với một môi trường mới,

tập mới. Hơn nữa, không có mối quan hệ nào giữa tập này và tập tiếp theo.

Vì vậy việc tôi làm mất tập TikTok trước đó sẽ không ảnh hưởng gì đến môi trường trong

tập tiếp theo. Tuy nhiên, có những ví dụ về môi trường không phân đoạn.

Lấy ví dụ, thị trường chứng khoán. Đối với tất cả ý định và mục đích, điều này có thể tiếp tục mãi mãi.

Không có khái niệm thực sự về sự kết thúc. Chà, nếu bạn mất hết tiền thì về mặt kỹ thuật thì có

bạn không thể làm gì hơn nữa. Nhưng nó không giống như việc thua một trò chơi TikTok và bắt đầu lại.

Bạn không thể quay ngược thời gian và khởi động lại thị trường chứng khoán.

Một ví dụ khác là hệ thống quảng cáo trực tuyến.

Công việc của đại lý của bạn sẽ là chọn quảng cáo phù hợp để hiển thị cho người dùng tại bất kỳ thời điểm nào

để tối đa hóa doanh thu của công ty bạn. Nó nên làm điều này liên tục.

Không có khái niệm chấm dứt dịch vụ quảng cáo trực tuyến.

Được rồi, đó là một số ví dụ về một số môi trường không theo từng tập.

Chúng ta có thể coi những môi trường như vậy là có những chân trời vô tận.

Được rồi, để tóm tắt lại các điều khoản chúng ta đã thảo luận cho đến nay, bây giờ chúng ta có tác nhân, môi trường và

tập. Một số thuật ngữ tiếp theo tôi muốn nghĩ đến là trạng thái, hành động và phần thưởng.

Những mục này giúp chúng ta mô tả những gì diễn ra khi tác nhân và môi trường tương tác với nhau.

Hãy lại sử dụng TikTok của chúng tôi để làm ví dụ. Trong trường hợp này, trạng thái sẽ là cấu hình

của hội đồng quản trị. Vì vậy, đối với mỗi vị trí trên bảng tôi muốn biết, có chữ x ở đó không, có chữ x nào không?

o ở đó, hay nó trống rỗng? Thông tin này là tất cả những gì tôi cần để người đại diện của tôi đưa ra quyết định

quyết định thông minh về bước đi tiếp theo. Nói về điều này, những động thái mà người đại diện thực hiện

là những gì chúng ta gọi là hành động. Vì vậy, trong TikTok Toe, thực hiện một hành động có nghĩa là đặt một

x ở đó và o ở đâu đó trên bảng. Cuối cùng, phần thưởng chỉ là một con số mà bạn có thể nhận được

bất cứ lúc nào khi bạn chơi một tập của trò chơi. Nhân tiện, hãy ghi nhớ khi tôi nói từ này

trò chơi, ý tôi không nhất thiết là một trò chơi board như TikTok Toe hay một trò chơi điện tử như đột phá.

Khi tôi nói trò chơi, tôi muốn nói nó theo nghĩa chung hơn. Trong mọi trường hợp, có lẽ phần thưởng bạn nhận được

TikTok Toe, có thể cộng một nếu thắng, trừ một nếu thua và không nếu hòa. Mặc dù đây là

chỉ là một ví dụ Nói chung, bạn luôn có thể tự mình giao phần thưởng để cải thiện việc đào tạo

của tác nhân học tập tăng cường của bạn. Đây là một ví dụ khác về trạng thái, hành động và phần thưởng.

Hãy nghĩ về một mê cung. Trong mê cung này, trạng thái là vị trí của bạn trong mê cung. Hành động của bạn có thể bao gồm

các hướng khác nhau mà bạn có thể đi, ví dụ như lên, xuống, trái hoặc phải. Phần thưởng là khó khăn.

Hãy nhớ rằng, tôi đã nói rằng bạn phải nghĩ ra một phần thưởng xứng đáng để giao cho người đại diện của mình nhằm khuyến khích họ làm điều đó.

học cách giải quyết môi trường. Bạn có thể nói cộng một để giải quyết mê cung và không nếu ngược lại.

Nhưng hãy tự hỏi, đây có phải là một chiến lược tốt? Hãy tưởng tượng bạn ném người đại diện của mình vào mê cung này và nó có

để học những gì phải làm. Hãy tưởng tượng người đại diện của bạn đã chơi trò chơi này 10.000 lần và chưa bao giờ giải quyết được vấn đề.

mê cung. Chúng ta có thể giả vờ môi trường theo từng giai đoạn để sau khi thực hiện 100 bước, bạn sẽ đến được điểm cuối

trạng thái và trò chơi kết thúc. Điều gì xảy ra nếu chúng tôi không nhận được phần thưởng mỗi lần? Chà, trong trường hợp đó,

đại lý biết rằng việc nó làm không quan trọng chút nào bởi vì làm bất cứ điều gì luôn dẫn đến

với cùng một phần thưởng, bằng không. Trong trường hợp này, tác nhân không có động cơ để giải quyết mê cung. Đại lý của bạn sẽ

không bao giờ ưu tiên hành động này hơn hành động khác vì nó biết rằng dù làm gì đi nữa, nó luôn nhận được

phần thưởng bằng không. Trong trường hợp này, tất cả các hành động đều bình đẳng.

Có lẽ cơ cấu phần thưởng tốt hơn sẽ là chỉ định trừ một phần thưởng ở mỗi trạng thái.

Trong trường hợp này, bạn có thể tối đa hóa phần thưởng của mình bằng cách giải quyết mê cung càng nhanh càng tốt.

Thực hiện bất kỳ hành động không liên quan nào sẽ dẫn đến phần thưởng tiêu cực hơn.

Không giải quyết được mê cung sẽ dẫn đến phần thưởng tiêu cực nhất. Vì vậy, trong trường hợp này, việc gán một số âm

phần thưởng khi đạt đến bất kỳ trạng thái nào sẽ cho phép đại lý của bạn giải quyết vấn đề.

Bây giờ bạn phải nhớ rằng đây không phải là lớp học tiếng Anh nên bạn phải loại bỏ mọi thành kiến mà bạn có thể có

về ý nghĩa nào gắn liền với thuật ngữ phần thưởng. Bạn có thể nghĩ phần thưởng là một điều tốt

thứ giống như một giải thưởng. Ví dụ: nếu bạn là một chú chó và bạn vừa thực hiện thành công một trò lừa,

chủ nhân của bạn có thể thưởng cho bạn một món quà. Nhưng trong học tăng cường, đây không phải là điều chúng ta

nghĩa là phần thưởng. Hạn chế duy nhất là phần thưởng là một con số thực. Nó có thể tích cực, tiêu cực,

hoặc bằng không. Bạn cũng sẽ nhận được con số này ở mọi bước trong môi trường chứ không chỉ khi bạn

đạt được mục tiêu nào đó hoặc chắc chắn không đạt được mục tiêu đó. Người đại diện, như bạn sẽ tìm hiểu sau trong phần này,

sẽ cố gắng tối đa hóa phần thưởng qua mỗi tập. Ví dụ: bạn có thể nhận được phần thưởng âm 100.

Điều này còn tốt hơn phần thưởng âm 1 triệu. Có thể trừ 100 phần thưởng tương ứng với thành công

giải quyết môi trường. Nhưng cuối cùng nó chỉ là một con số. Đừng liên kết âm 100 với âm

ý nghĩa và cộng thêm 100 với ý nghĩa tích cực. Vì vậy hãy nhớ điều này, phần thưởng không phải là giải thưởng,

phần thưởng là một con số cần được tối đa hóa. Bạn có thể coi nó như một dạng đối lập với một

hàm mất mát, trong khi chúng ta muốn giảm thiểu tổn thất trong bài toán học có giám sát hoặc không giám sát,

trong học tập tăng cường, chúng tôi muốn tối đa hóa phần thưởng.

Vì tôi thích các ví dụ nên đây là một ví dụ nữa. Hãy tưởng tượng lại trò chơi đột phá. Trong trường hợp này, chúng tôi thực sự có

một số lựa chọn cho nhà nước Ví dụ: chúng tôi có thể có thông tin hoàn hảo về trò chơi. Chúng tôi có thể

được cho biết vị trí chính xác của tất cả các khối. Chúng ta có thể biết được vị trí và vận tốc của quả bóng.

Chúng tôi có thể được cho biết vị trí mái chèo của chúng tôi. Và chúng tôi có thể được thông báo về số điểm hiện tại và số lượng

những lời dối trá mà chúng ta đã để lại. Mặc dù tôi nghĩ bạn sẽ thấy rằng hầu hết các ứng dụng học tăng cường đều không

sử dụng những thông tin đó.

Một cách khác để bạn có thể đọc thông tin về trạng thái môi trường và đột phá là

nhìn vào RAM của trò chơi. Nói cách khác, hãy nhìn vào các giá trị nó đã lưu trong bộ nhớ. Ngược lại với

như trên, đây thực sự là một phương pháp được sử dụng trong các ứng dụng học tăng cường hiện đại.

Đó là một proxy cho trạng thái được xác định hoàn hảo ở trên. Bạn có thể tưởng tượng rằng điều đó hoàn toàn có thể xảy ra

để xác định vị trí của các khối cũng như vị trí và vận tốc của quả bóng

v.v. từ các giá trị được lưu trữ trong RAM.

Mặc dù tôi nghĩ cách phổ biến nhất để thể hiện nhà nước trong việc củng cố hiện đại

học tập là sử dụng ảnh chụp màn hình từ trò chơi. Bằng cách này, tác nhân học tăng cường của chúng tôi

đang học cách diễn giải hình ảnh của trò chơi điện tử giống như con người chúng ta. Tôi nghĩ đây là

ý nghĩa nhất vì nó giống nhất với cách bạn và tôi chơi trò chơi điện tử. Chúng tôi nhìn vào

màn hình. Bạn có thể tưởng tượng rằng các mô hình như mạng nơ ron tích chập sẽ hữu ích ở đây.

Một điều phức tạp có thể nảy sinh khi chỉ nhìn vào hình ảnh trên màn hình là bạn không thực sự

có thông tin về chuyển động. Hình ảnh chỉ là hình ảnh cố định của trò chơi tại một thời điểm.

Nhìn vào hình ảnh này, làm thế nào tôi có thể biết quả bóng đang chuyển động theo hướng nào?

Và vì vậy điều này cho phép chúng ta xem xét một điểm quan trọng. Trạng thái không nhất thiết phải là những gì tôi quan sát được trong

môi trường. Nó cũng có thể là thông tin bắt nguồn từ cả những quan sát hiện tại và quá khứ.

Vì vậy, một cách để giải quyết vấn đề hình ảnh bị đóng băng là chỉ cần đưa cả các khung hình quá khứ vào.

Trong bài báo DQN nổi tiếng, họ sử dụng bốn khung hình liên tiếp gần đây nhất của trò chơi để thể hiện một

trạng thái duy nhất. Để quay lại các hành động và phần thưởng của bang chúng ta, phần còn lại khá cơ bản.

Các hành động bao gồm các động tác khác nhau mà bạn có thể thực hiện trong trò chơi. Bạn có thể nghĩ về điều này dưới dạng

nhấn các nút trên cần điều khiển hoặc bảng điều khiển. Khi đột phá, bạn có thể di chuyển mái chèo sang trái hoặc phải.

Ví dụ: đối với phần thưởng, bạn có thể nhận được cộng một phần thưởng mỗi khi phá hủy một khối.

Lưu ý cuối cùng của bài giảng này là tôi muốn giới thiệu với các bạn khái niệm về không gian trạng thái

và không gian hành động. Điều này rất quan trọng khi chúng ta chuyển từ những ý tưởng và khái niệm cấp cao sang

phép toán thực tế sẽ cho phép chúng ta giải các bài toán bong bóng tăng cường. Khái niệm toán học cụ thể

mà chúng ta cần mô tả không gian trạng thái và không gian hành động là tập hợp. Không gian trạng thái là tập hợp các

tất cả các trạng thái có thể xảy ra và không gian hành động là tập hợp tất cả các hành động có thể xảy ra. Chúng ta không cần phải đi

xa hơn thế này. Chúng ta chỉ cần biết nó có ý nghĩa gì.

Vì vậy, để làm ví dụ, hãy xem xét ví dụ điển hình về bài toán bong bóng gia cố được gọi là

thế giới lưới. Trong thế giới lưới, ý tưởng là bạn sẽ bắt đầu ở ô vuông phía dưới bên trái và mục tiêu của bạn

là đến ô vuông trên cùng bên phải nơi có viên hồng ngọc. Nếu bạn đến đó, bạn sẽ nhận được phần thưởng là

cộng một. Dưới mức đó, có một trạng thái thua cuộc mà nếu bạn đến đó, bạn sẽ nhận được phần thưởng là trừ một.

Và ở hàng thứ hai, cột thứ hai có một bức tường, nghĩa là người đại diện của bạn không thể đi tới đó

hình vuông. Vì vậy, đó là những điều cơ bản của trò chơi. Để mô tả không gian trạng thái, đó đơn giản là tập hợp các

tất cả các vị trí có thể có trên bảng. Vì vậy, bạn có thể muốn tạm dừng video này và xem kỹ video này

danh sách tọa độ để xác nhận rằng chúng tương ứng với các vị trí trên bảng. Không gian hành động bao gồm

của các hành động lên, xuống, trái và phải. Bây giờ lý do chúng ta phải nói về thế giới lưới một chút

là bởi vì đối với các ví dụ khác của chúng tôi như tic tac toe và đột phá, không gian trạng thái nhiều hơn

phức tạp. Các không gian hành động khá đơn giản. Vì đối với tic tac toe, nó bao gồm tất cả

các vị trí có thể bạn có thể vẽ chữ x hoặc chữ o. Và để đột phá, nó bao gồm việc di chuyển sang trái, phải

hoặc không làm gì cả. Nhưng đối với tic tac toe thì không gian trạng thái khá lớn vì có thể có rất nhiều

các cấu hình của board. Như một bài tập, tôi thực sự khuyên bạn nên thử viết một máy tính

chương trình có thể liệt kê tất cả các cấu hình có thể có của bảng tic tac toe. Điều này nên

cung cấp cho bạn một số trực giác về lý do tại sao các trò chơi như cờ vua và cờ vây lại rất khó. Bạn có thể tưởng tượng rằng

nếu một bảng 3 x 3 chỉ có hai ký tự có thể có hàng nghìn trạng thái. Hãy tưởng tượng có bao nhiêu

các bang tham gia vào cờ vua và cờ vây. Đối với đột phá, số lượng trạng thái thậm chí còn lớn hơn.

Nó bằng độ phân giải màn hình nhân với số màu có thể có trên mỗi pixel

lũy thừa 24 hoặc lũy thừa 8 lũy thừa 3. Nhưng với mọi ý nghĩa và mục đích, chúng ta có thể xem xét

hình ảnh giống như chuỗi thời gian có giá trị liên tục. Lý do duy nhất khiến chúng có vẻ rời rạc

là do máy tính có độ chính xác hữu hạn và do đó các giá trị cần được lượng tử hóa.

Khi chúng ta có các giá trị liên tục, điều này có nghĩa là số lượng giá trị có thể thực sự là mạng nội bộ.

Trên thực tế, các hành động cũng có thể diễn ra liên tục nên không gian hành động cũng là vô hạn.

Vì bài giảng này khá dài nên hãy tóm tắt lại những gì chúng ta đã học.

Bài giảng này chủ yếu nhằm xác định một số thuật ngữ học tăng cường để giúp chúng ta

cuộc thảo luận của chúng tôi về học tập tăng cường. Đầu tiên, chúng tôi định nghĩa các thuật ngữ Châu Á và môi trường.

Bạn có thể coi môi trường như thế giới hoặc bất kỳ trò chơi máy tính nào bạn đang dạy cho đại diện của mình.

để giành chiến thắng. Bạn có thể coi người đại diện của mình như một chương trình máy tính, chương trình thực hiện việc học tập.

Tiếp theo, chúng tôi xác định thuật ngữ tập. Điều này giống như một hiệp hay một trận đấu của một trò chơi.

Như bạn đã biết, các mô hình machine learning học thông qua dữ liệu hoặc học tăng cường

kinh nghiệm ngôn ngữ. Và vì vậy bạn có thể tưởng tượng rằng để học đủ cách chơi một

trò chơi này sẽ yêu cầu nhiều tập. Tiếp theo, chúng ta tìm hiểu về trạng thái, hành động và phần thưởng.

Phần thưởng là một con số có thể là số bất kỳ, dương hoặc âm.

Công việc của tác nhân học tăng cường là tối đa hóa phần thưởng của nó.

Hành động là những gì một tác nhân thực hiện trong một môi trường. Ví dụ: chơi một nước đi trong Tic Tac Toe

hoặc rẽ trái hoặc phải trong trò chơi điện tử. Trạng thái là những gì chúng ta quan sát được từ môi trường,

nhưng chúng cũng có thể là các giá trị rút ra từ những quan sát đó hoặc thậm chí là một chuỗi các quan sát trong quá khứ.

Để bổ sung thêm một chút cho điều này, chúng tôi gọi trạng thái cuối cùng của một tập là trạng thái kết thúc.

Vì vậy, khi bạn đạt đến trạng thái cuối, đó là lúc kết thúc tập phim của bạn.

Cuối cùng, chúng tôi xác định các thuật ngữ không gian trạng thái và không gian hành động. Đây là tập hợp tất cả các trạng thái và

tập hợp tất cả các hành động tương ứng. Sử dụng những thuật ngữ này, bây giờ chúng ta có thể nói về học tăng cường

mạch lạc và xây dựng một khuôn khổ cho phép chúng ta giải quyết các vấn đề học tập tăng cường.