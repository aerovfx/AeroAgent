# 11 -Tùy chọn xem trước các phương pháp tiến hóa đã được dịch

---

Được rồi, trong video này chúng ta sẽ xem trước các phương pháp tiến hóa vì nó

phần nào liên quan đến những gì chúng ta đang làm trong phần này.

Đó là phương pháp tiến hóa.

Và đây chỉ là bản xem trước cho khóa học này.

Vì vậy, chúng ta sẽ không triển khai bất kỳ điều nào trong số này, mặc dù việc này khá dễ thực hiện, vì bạn sẽ

thấy đấy, vì vậy bạn có thể tự mình thử những thứ này nếu muốn, nhưng nó không phải là một trong những

trọng tâm chính của khóa học này, vì vậy tôi sẽ không triển khai chúng.

Được rồi, vậy nếu bạn nghĩ lại những nghiên cứu về giải tích của mình, thì toàn bộ phần này nói về

độ dốc.

Bạn nhớ lại rằng chúng ta có thể tính gần đúng đạo hàm phải không?

Vì vậy, nếu bạn tưởng tượng chúng ta có một đường cong nào đó, và chúng ta muốn biết đạo hàm tại đây bằng bao nhiêu

điểm này, chúng ta có thể làm điều gì đó như di chuyển đến điểm này, tính giá trị của hàm.

Vì vậy, chúng ta sẽ gọi cái này là f(x), và chúng ta sẽ gọi cái này là x, và chúng ta sẽ gọi cái này, chẳng hạn, x prime.

Và đây sẽ là fx, và đây sẽ là fx prime.

Chúng ta có thể tính gần đúng đạo hàm, do đó df nhân dx, tại điểm x này, sẽ xấp xỉ

bằng f(x prime trừ f(x) chia cho x prime trừ x.

Được rồi, chúng ta nhớ lại điều đó từ phép tính một.

Vì vậy, chúng ta cũng có thể làm điều tương tự với gradient.

Được rồi, hãy tưởng tượng chúng ta có bề mặt, và chúng ta muốn biết gradient tại một số điểm là bao nhiêu?

điểm.

Vì vậy chúng ta sẽ nói, đây là j của theta.

Vì vậy, theta bây giờ là một vectơ, vì vậy chúng ta có theta 1 và theta 2 chẳng hạn.

Chúng ta có thể, vì vậy đây là điểm bắt đầu theta, và chúng ta sẽ đi đến một số theta khác, chúng ta sẽ

gọi nó là theta prime.

Và vì vậy chúng ta có thể ước chừng gradient del theta j, theta được đánh giá tại theta, xấp xỉ

bằng, vì vậy đây sẽ là j được đánh giá ở theta nguyên tố trừ j, được đánh giá ở theta chia

bởi vậy chúng ta phải tách riêng các thành phần ra phải không?

Vì vậy, kích thước của vectơ này sẽ là số thành phần chúng ta có, vì vậy nó sẽ là theta

số nguyên tố 1 trừ theta 1.

Sau đó, thành phần thứ hai, do đó sẽ có cùng tử số, do đó j theta prime trừ

j theta, và đó sẽ là thành phần thứ hai, vậy theta 2 prime trừ theta 2, v.v.

vân vân, nếu bạn có nhiều thành phần hơn.

Được rồi, vậy điều này chuyển thành học tăng cường như thế nào?

Bạn nhớ lại rằng trong học tăng cường, chúng ta đã bắt đầu với thực tế là chúng ta muốn tối đa hóa

tổng phần thưởng trong một tập phim.

Và lúc đầu, chúng tôi không biết cách tìm gradient này, nên chúng tôi đã làm tất cả công việc này

để tính toán độ dốc và sau đó sử dụng nó thay thế.

Nhưng điều này có nghĩa là chúng ta thậm chí không phải làm tất cả công việc đó.

Thay vào đó, tất cả những gì chúng ta có thể làm chỉ đơn giản là phát một loạt các tập phim, sửa đổi trọng số của

mạng nơ-ron một chút, vì vậy hãy tưởng tượng một không gian có trọng số mạng nơ-ron của bạn, hãy thực hiện một số

hướng ngẫu nhiên, giả sử, vậy theta prime, phát lại tập đó, vì vậy hãy phát chúng ở cả hai

những điểm này, vì vậy hãy phát tập phim và bạn nhận được câu nói, trời ơi, chơi tập phim, bạn nhận được g prime, và

sau đó bạn thực hiện phép trừ, thực hiện phép tính gần đúng như trên, vì vậy đó có thể là một cách để thực hiện.

Ngoài ra, vì bạn chỉ nhận được một lần trả lại mỗi khi phát một tập phim, nên bạn thực sự có thể

phát tập này nhiều lần, vì vậy đối với theta, hãy phát M tập và sau đó là j theta của bạn

sẽ bằng 1 trên M, hoặc tôi đoán là gần đúng, i bằng 1 với M, và sau đó g i, hoặc bạn có thể

giả sử, tôi thường đặt cái này vào tử số, g i, nhưng bạn hiểu ý, chúng ta luôn quá tải

g trong khóa học này nên hy vọng bạn hiểu được những gì chúng tôi đang làm từ ngữ cảnh này.

Được rồi, cách thức hoạt động là như vậy, bạn bắt đầu ở một vị trí ngẫu nhiên, bạn phát tập phim M lần,

tính lợi nhuận trung bình, điều này mang lại cho bạn j cho cài đặt tham số ngẫu nhiên này, sau đó

bạn di chuyển theta một chút đến vị trí mới, làm điều tương tự ở đó và sau đó tính toán độ dốc

như trên, và như trước, chúng ta thực hiện cập nhật độ dốc như vậy, đúng vậy, theta bằng theta plus,

tốc độ học nhân với gradient và trong trường hợp này, gradient này sẽ được ước tính.

Được rồi, đây là một dạng phương pháp tiến hóa rất thô sơ, nên nếu chúng ta muốn mở rộng nó,

giả sử, và làm cho nó có ý nghĩa hơn về mặt tiến hóa, chúng ta phải nói một chút về

quá trình tiến hóa diễn ra như thế nào. Được rồi, vậy ít nhất là sự tiến hóa trong máy tính và điều đó có liên quan như thế nào đến sự tiến hóa

và sinh học. Vì vậy hy vọng bạn hiểu được sự tiến hóa và sinh học, vì tôi sẽ không giải thích

điều đó quá nhiều. Về cơ bản nó sẽ hoạt động như thế này, quá trình tiến hóa.

Vì vậy, hãy tưởng tượng, à, trước tiên hãy nghĩ về nó theo cách này, hãy tưởng tượng, và tôi đoán đây là sự tiến hóa

và sinh học, vậy nên chúng ta có một số sinh vật, và hãy giả vờ vì mục đích của khóa học này,

chúng tôi chỉ đang làm việc với sinh sản vô tính, vì vậy mỗi sinh vật có thể sinh ra một sinh vật khác

không có đối tác nanegal, nên đó sẽ là một loại thuật toán hơi khác. Đôi khi

thông thường chúng tôi gọi những thuật toán di truyền đó là vì chúng tôi có hai cha mẹ, mỗi người trong số họ có con riêng

DNA, và sau đó chúng tôi trộn chúng lại để tạo ra thế hệ con cháu. Nhưng đối với điều này, điều chúng ta sẽ làm là mỗi

cá nhân sẽ có đàn con của riêng mình, và họ sẽ có con cái của riêng mình, v.v.

Vì vậy, hãy tưởng tượng mỗi cá nhân có ba đứa con, được thôi, và một số trong số chúng khỏe mạnh hơn những đứa khác.

Được rồi, giả sử con này chết, hoặc không đủ sức khỏe, vì vậy chúng tôi sẽ giữ lại con cái dựa trên mức độ khỏe mạnh của chúng.

Vì vậy, hãy giữ con cái dựa trên mức độ thể lực.

Bạn có thể tưởng tượng chúng tôi giữ hai cái này không? Họ có con cháu riêng của họ.

Được rồi, và một lần nữa, nói rằng một số không phù hợp nên chúng biến mất,

và rồi thế hệ này còn có nhiều con cháu hơn nữa, phải không, vậy nên những người này, v.v., v.v.

Được rồi, và trên thực tế, bạn cũng có thể làm những việc như giữ dân số không đổi, vì vậy

giết chết nhiều cá thể hơn ở mỗi thế hệ, bởi vì bây giờ chúng ta có kết quả như thế này, chẳng hạn như 12 khi

chúng tôi bắt đầu với một. Và chìa khóa ở đây là vì chúng tôi luôn giữ những cá nhân khỏe mạnh nhất trong mọi

thế hệ. Theo thời gian, qua nhiều thế hệ, các cá nhân sẽ ngày càng trở nên khỏe mạnh hơn,

hay nói cách khác, trong trường hợp của chúng tôi, nhận được phần thưởng ngày càng cao hơn trong trò chơi, trong môi trường

chúng tôi đang chơi. Vì vậy, trong bối cảnh học tăng cường, sự phù hợp sẽ được đánh giá bởi

chỉ J, đúng rồi, lợi nhuận trung bình khi phát tập đó. Được rồi, và khái niệm then chốt ở đây là làm cách nào chúng ta

tạo ra cá thể con từ cá thể? Và điều quan trọng là dựa trên những gì chúng ta biết về sinh học

là mỗi đứa con sẽ giống nhau, nhưng không hoàn toàn giống bố mẹ nó. Được rồi, vậy về mặt số

các thuật ngữ, bởi vì chúng ta đang làm việc với vectơ, giả sử, bạn biết đấy, đây là theta, và đó là

cá nhân tạo ra con cái vào thời điểm này. Vì vậy, từ đây, sẽ hợp lý nếu có một theta mới

giả sử là số nguyên tố ở đây, nhưng sẽ không hợp lý nếu có một số nguyên tố theta mới ở đây,

đúng rồi, điều đó sẽ không có ý nghĩa gì, vì nó quá xa. Được rồi, và để tạo ra con cái,

mặc dù điều đó nghe có vẻ phức tạp nhưng tất cả những gì chúng ta thực sự đang làm là nói theta prime bằng

theta cộng với một số nhiễu ngẫu nhiên, và chúng ta tạo ra nhiễu ngẫu nhiên này, một vectơ ngẫu nhiên có giá trị trung bình bằng 0,

và một số khác biệt nhỏ. Và thủ thuật tiến hóa, trái ngược với những gì chúng ta đã thảo luận trước đây,

là chúng ta tạo ra nhiều con cái. Trên thực tế, không chỉ ba, mà có lẽ còn nhiều hơn nữa.

Hãy tưởng tượng đây là theta, chúng ta sẽ chọn, chẳng hạn, 100 con, vì vậy đây là một, đây là một, đây là một,

đây là một, đây là một, đây là một, vân vân. Và bởi vì chúng tôi đang thử nghiệm rất nhiều thứ khác nhau

hướng cùng một lúc, điều mang lại cho chúng ta là ước tính tốt hơn về độ dốc. Được rồi,

hãy tưởng tượng chúng ta có n con cái, vậy nên n con cái. Được rồi, và độ dốc của chúng tôi,

và độ dốc được ước tính bởi

tôi.

Được rồi, một lần nữa nó chỉ là mức trung bình. Vậy một trên n,

một số bằng một đến n. Và ở đây tôi sẽ lạm dụng ký hiệu một chút,

vì vậy tôi sẽ nói j theta cộng cộng epsilon i trừ j theta chia cho epsilon i.

Được rồi, vậy tại sao ký hiệu này hơi lạm dụng một chút là vì đây là một đại lượng vô hướng

và đây là một vectơ. Được rồi, điều chúng tôi thực sự muốn nói là,

được rồi, hãy làm rõ điều đó. Vì vậy lạm dụng ký hiệu.

Ý nghĩa thực sự của epsilon i trên mẫu số là vectơ, một trên epsilon i,

một, một trên epsilon i, hai, vân vân. Đó là một epsilon xấu xí, nhưng, rất tiếc,

bạn cần phải chạy đua bằng cách nào đó. Được rồi, chúng ta bắt đầu thôi. Được rồi, vậy là chúng ta thực sự đang lấy giá trị trung bình hai lần

ở đây phải không? Vì vậy, chúng tôi đang lấy giá trị trung bình của nhiều tập để ước tính j, nhưng chúng tôi cũng đang lấy

giá trị trung bình của các ước tính độ dốc khác nhau từ các hướng khác nhau.

Được rồi, đó là phương pháp tiến hóa. Vì vậy, một thuật toán liên quan khác mà bạn có thể sử dụng

là, chỉ là vì tôi thấy nó thú vị nên tôi sẽ đề cập đến nó, đó là leo đồi.

Thế là leo đồi. Và một cách bạn có thể thực hiện điều này,

giả sử chúng ta đang đi theo một hướng, mặc dù nó không thú vị lắm.

Và bạn ở đây, vậy đây là theta của bạn. Về cơ bản, bạn sẽ thử các hướng khác nhau, vì vậy chúng tôi sẽ thử,

nói điều này, và một lần nữa, đó chỉ là chọn số ngẫu nhiên để thử. Và vì vậy chúng tôi sẽ tính toán điều này,

theta nguyên tố, j theta nguyên tố. Và bởi vì cái này nhỏ hơn j theta nên chúng ta sẽ đơn giản bỏ qua nó.

Và thử lại. Vì vậy, lần sau chúng ta thử, chúng ta có thể đi theo hướng này. Vì vậy, theta là số nguyên tố kép.

Và đây là j theta số nguyên tố kép. Và vì nó tốt hơn j theta hiện tại của chúng tôi nên chúng tôi chỉ giữ

cái này là theta hiện tại của chúng tôi. Và sau đó chúng tôi làm điều tương tự một lần nữa. Vì thế chúng tôi thử những hướng khác nhau

và chọn hướng tăng j. Đó là một cách khác để thực hiện những điều này mà không cần chuyển màu

phương pháp. Và nhân tiện, đó là một trong những điểm chính của bài giảng này, đó là những phương pháp này

không có gradient. Các phương pháp không có gradient, có thể hữu ích trong trường hợp tính toán

độ dốc là bất tiện hoặc rất khó khăn.