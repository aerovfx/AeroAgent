# 04 từ khóa-tìm kiếm-tf-idf

---

Hãy bắt đầu khám phá các kỹ thuật tìm kiếm bằng tìm kiếm từ khóa.

Kỹ thuật này đã hỗ trợ việc truy xuất trong cơ sở dữ liệu và công cụ tìm kiếm trong nhiều thập kỷ.

Tuy nhiên, tính đơn giản và hiệu quả của nó khiến nó trở thành một thành phần quan trọng trong việc truy tìm trong các hệ thống hiện đại.

Hệ thống RAG.

Chúng ta hãy xem nó hoạt động như thế nào và nó mang lại những điểm mạnh gì cho đường dẫn chó tha mồi của bạn.

Tìm kiếm từ khóa là một kỹ thuật truy xuất tài liệu dựa trên việc chúng có chia sẻ từ hay không

điểm chung với lời nhắc.

Ý tưởng cơ bản là các tài liệu chứa nhiều từ trong dấu nhắc sẽ được

có nhiều khả năng có liên quan hơn.

Đây là cách nó hoạt động.

Cả lời nhắc và mỗi tài liệu đều được coi như một túi từ.

Điều này có nghĩa là thứ tự của các từ hoàn toàn bị bỏ qua và tất cả những gì quan trọng là từ nào

có trong văn bản và tần suất như thế nào.

Ví dụ: văn bản làm bánh pizza không có lò nướng pizza có chứa từ pizza hai lần

và các từ làm, không có, a, và lò nướng một lần.

Số lượng từ này được lưu trữ bên trong một vectơ.

Vectơ có một vị trí cho mỗi từ trong từ vựng của hệ thống.

Vì vậy, có thể dễ dàng có hàng chục ngàn điểm.

Mỗi số trong vectơ sẽ tính tần suất từ ​​đó xuất hiện trong văn bản.

Vì hầu hết các vị trí đều chứa số 0 nên chúng còn được gọi là vectơ thưa thớt.

Để chuẩn bị cơ sở tri thức cho việc truy xuất, một vectơ thưa thớt được tạo ra cho mỗi tài liệu.

Tất cả các vectơ này có thể được sắp xếp thành một lưới, được gọi là tài liệu thuật ngữ

ma trận.

Mỗi cột là một tài liệu khác nhau và mỗi hàng là một từ khác nhau.

Điều này đôi khi còn được gọi là chỉ số đảo ngược.

Bởi vì nó giúp bạn dễ dàng bắt đầu từ một từ và tìm mọi tài liệu có chứa

nó.

Nó bị đảo ngược vì bạn thường bắt đầu từ một tài liệu và nghĩ xem nó chứa những từ nào,

nhưng ở đây bạn đang bắt đầu từ một từ và tìm tài liệu nào bao gồm từ đó.

Chỉ mục đảo ngược này có thể được tạo một lần trước khi xử lý bất kỳ tìm kiếm nào.

Khi một lời nhắc được gửi đến bộ truy xuất, một vectơ thưa thớt sẽ nhanh chóng được tạo ra cho

nhắc nhở.

Bây giờ mỗi tài liệu và lời nhắc đều có một vectơ thưa thớt, bạn đã sẵn sàng bắt đầu tính điểm

và các tài liệu xếp hạng.

Cách tiếp cận đơn giản nhất là chỉ cho điểm tài liệu khi chúng chứa các từ trong lời nhắc.

Mỗi từ của lời nhắc được gọi là một từ khóa.

Trong lời nhắc ví dụ trước đó, bạn sẽ bắt đầu với từ khóa đầu tiên, tạo và tìm từ khóa đó

hàng trong chỉ mục.

Sau đó, bạn đi qua hàng đó và trao một điểm cho mỗi tài liệu chứa ít nhất

một bản sao của từ khóa.

Sau đó, bạn hoàn tất quy trình tương tự cho mọi từ khóa khác trong lời nhắc.

Nếu một tài liệu chứa từ khóa, nó sẽ ghi được một điểm.

Lời nhắc này chứa năm từ khóa, nghĩa là số điểm cao nhất có thể là năm.

Khi bạn đã hoàn tất, tổng số điểm có thể được sử dụng để xếp hạng tài liệu và tài liệu sẽ

với số điểm cao nhất được lấy ra.

Một thiếu sót của phương pháp tính điểm đơn giản là nó không nắm bắt được liệu một tài liệu có

chứa từ khóa nhiều lần, điều này có thể cho thấy mức độ liên quan cao hơn.

Cách khắc phục đơn giản là tăng điểm của tài liệu mỗi khi nó chứa từ khóa chứ không chỉ

cái đầu tiên.

Bây giờ bạn có thể tìm thấy hàng của mỗi từ khóa trong ma trận và chỉ trao giải cho mỗi tài liệu

số điểm trong cột của nó.

Tuy nhiên, điều này gây ra một vấn đề mới, đó là các tài liệu dài hơn có thể chứa các từ khóa

nhiều lần đơn giản chỉ vì chúng dài hơn.

Để khắc phục điều này, bạn có thể chia điểm của từng tài liệu cho số từ trong tài liệu đó.

Điểm chuẩn hóa này san bằng sân chơi.

Nó thưởng cho các tài liệu trong đó từ khóa chiếm tỷ trọng lớn hơn trong tổng số văn bản và không nhấn mạnh

tài liệu dài có thể chứa từ khóa nhiều lần chỉ vì chúng quá dài.

Cách tiếp cận này khá tốt nhưng nó thưởng điểm cho tất cả từ khóa như nhau, cho dù chúng có

những từ bổ sung như những từ ít phổ biến hơn như pizza, sự hiện diện của chúng tốt hơn nhiều

dấu hiệu liên quan.

Để khắc phục điều này, bạn có thể cân nhắc lại các số hạng, nhưng lần này sử dụng thước đo gọi là

tần số tài liệu nghịch đảo hoặc IDF.

Để sử dụng phương pháp này, bạn cần tính giá trị IDF cho mỗi từ trong hệ thống.

từ vựng.

Đối với mỗi từ, bạn sẽ đếm xem nó xuất hiện trong bao nhiêu tài liệu rồi chia cho tổng số

số lượng tài liệu.

Nếu cơ sở kiến thức của bạn có 100 tài liệu và từ pizza xuất hiện trong 5 tài liệu trong số đó, thì nó sẽ

có tần số tài liệu là 5 trên 100 hoặc 0,05.

Một từ phổ biến như the có thể xuất hiện trong tất cả 100 tài liệu.

Vì vậy, tần số tài liệu này sẽ là 100 trên 100 hoặc chỉ 1.

Vì bạn muốn thưởng cho những từ hiếm nên bây giờ bạn hãy lật ngược phân số hoặc đảo ngược nó.

IDF của Pizza bây giờ sẽ là 20, trong khi IDF của Pizza chỉ là 1.

Tại thời điểm này, những từ hiếm có IDF cao hơn đáng kể so với những từ thông thường, điều này có thể quá mức.

khen thưởng những từ hiếm.

Vì lý do này, nhật ký của IDF là thứ thường được sử dụng.

Những từ hiếm vẫn có trọng lượng lớn hơn nhưng đã bớt cường điệu hơn trước.

Kết quả là một giá trị IDF cho mỗi từ thể hiện mức độ hiếm của nó trong kiến thức

cơ sở.

Để sử dụng các giá trị này trong việc tính điểm, trước tiên các giá trị trong chỉ mục đảo ngược sẽ được cập nhật,

nhân các số trong mỗi hàng với điểm IDF của từ đó.

Ma trận kết quả là ma trận Tần số tài liệu nghịch đảo tần số thuật ngữ hoặc ma trận TF-IDF.

Để chấm điểm các tài liệu trong cơ sở tri thức, bạn chỉ cần sử dụng cách tiếp cận tương tự như trước.

Đối với mỗi từ khóa trong lời nhắc, hãy duyệt qua hàng của nó và trao giải TF-IDF cho từng tài liệu

số điểm nó có ở hàng đó.

Điểm TF-IDF được tạo ra bởi phương pháp này là đường cơ sở tiêu chuẩn cho hiệu suất

của việc truy xuất từ khóa.

Các tài liệu có điểm cao nhất sẽ thường xuyên sử dụng từ khóa và đặc biệt sẽ có

nhiều từ khóa hiếm gặp trên toàn bộ cơ sở kiến thức.

Nhìn vào lời nhắc trước đó, các tài liệu chứa các từ hiếm như pizza hoặc lò nướng có thể sẽ

đạt điểm cao hơn nhiều so với các tài liệu có chứa các từ phổ biến như a hoặc không.

Trong khi TF-IDF là một cách tiếp cận cơ bản để tìm kiếm từ khóa, các hệ thống hiện đại có xu hướng sử dụng

một phiên bản cải tiến hơn một chút của phương pháp này được gọi là BM25.

Hãy tham gia cùng tôi trong video tiếp theo để tìm hiểu cách thức hoạt động và sau đó suy ngẫm về điểm mạnh của

tìm kiếm từ khóa và cách nó phù hợp với hệ thống RAC của bạn.