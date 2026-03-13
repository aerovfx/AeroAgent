# 3 -Bộ đệm phát lại được dịch

---

Được rồi, trong video này chúng ta sẽ xem xét tính năng tiếp theo của DQN, đó là tính năng phát lại

bộ đệm.

Và tôi đã quyết định trình bày cuốn sách này dưới dạng sổ ghi chép chung thay vì viết tay hoặc trang trình bày,

chỉ vì tôi nghĩ đó là cách hiệu quả nhất để trình bày thông tin này.

Được rồi, cấu trúc của cuốn sổ này không có nghĩa là sai.

Thực sự thì bạn có thể làm được vì có mã có thể chạy được trong đó.

Nhưng chúng ta sẽ bắt đầu bằng việc viết lên, điều này giải thích bộ đệm phát lại là gì.

Sau đó chúng ta sẽ có một số cách triển khai ví dụ.

Và sau đó chúng ta sẽ xem xét một số vấn đề tiềm ẩn với bộ đệm phát lại.

Và tôi sẽ thảo luận một chút về cách chúng ta có thể giải quyết những vấn đề đó.

Và sau đó chúng ta sẽ xem xét một số mã giả về cách sử dụng bộ đệm phát lại,

kết hợp điều đó vào việc học Q,

thay đổi thuật toán một chút.

Được rồi, chúng ta sẽ bắt đầu bằng cách giải thích bộ đệm phát lại là gì và tại sao chúng ta cần nó.

Được rồi, về cơ bản, việc học Q thường xuyên sẽ có một số vấn đề.

Vì vậy có sự tương quan tuần tự và học tập trực tuyến.

Và nhân tiện, nếu bạn chưa biết, học trực tuyến là nơi mô hình của bạn học

trong khi nó thu thập dữ liệu.

Đó chính là ý nghĩa của việc học trực tuyến.

Được rồi, như người ta nói, trong trải nghiệm học tập trực tuyến truyền thống có mối tương quan cao

vì chúng được tạo ra liên tiếp bởi các tác nhân.

Việc huấn luyện mạng lưới thần kinh trên các mẫu tuần tự này có thể dẫn đến việc học và phân kỳ kém hiệu quả.

Được rồi, về cơ bản điều này có nghĩa là mỗi trạng thái bạn gặp phải

trong một tập phim có mối tương quan với nhau, điều này hợp lý vì chẳng hạn như

nếu bạn đang cân bằng một chiếc xe đẩy trên một cái cột, bạn sẽ luôn phải chuyển sang bước tiếp theo,

đó là cực hơi khác so với vị trí trước đó,

di chuyển nhanh hơn một chút, chậm hơn một chút so với vị trí trước đó, v.v.

Vì vậy, bạn không kết thúc với các trạng thái hoàn toàn ngẫu nhiên.

Luôn tồn tại mối tương quan này khiến việc học không hiệu quả.

Được rồi, và điều này cũng liên quan đến điểm thứ hai, đó là dữ liệu chúng tôi nhận được

từ việc học trực tuyến như vậy là không có ID.

Được rồi, về cơ bản mối tương quan có nghĩa là

rất tiếc, vô tình nhấp vào hai lần.

Tương quan có nghĩa là dữ liệu của bạn không độc lập.

Vì vậy, nếu bạn nghiên cứu xác suất, bạn biết rằng nếu hai biến số có tương quan với nhau,

điều đó có nghĩa là họ không độc lập.

Vì vậy, dữ liệu của chúng tôi không độc lập, đó là điều chúng tôi muốn có khi

huấn luyện mạng lưới thần kinh.

Vì vậy, chúng tôi muốn dữ liệu IID.

Vì vậy, nó nói rằng mạng lưới thần kinh hoạt động tốt nhất khi được đào tạo độc lập và

dữ liệu IID được phân phối giống hệt nhau.

Tuy nhiên, và quan sát học tăng cường phụ thuộc vào các hành động và trạng thái trước đó,

làm cho dữ liệu và không có ID cao.

Về cơ bản đó là những gì tôi vừa nói.

Được rồi, vậy là chúng ta đang sử dụng dữ liệu không hiệu quả.

Được rồi, đây cũng là một điểm quan trọng và nó không liên quan đến hai điểm còn lại.

Vì vậy, không sử dụng mà không sử dụng lại những kinh nghiệm đã qua, mỗi kinh nghiệm chỉ được sử dụng,

chỉ được sử dụng một lần, dẫn đến việc học không hiệu quả và đòi hỏi phải tương tác nhiều hơn với

môi trường.

Được rồi, điều này cũng đúng.

Vì vậy, mọi chuyển đổi mà chúng ta gặp phải, mọi trạng thái, hành động, phần thưởng, trạng thái tiếp theo và

done, chúng tôi chỉ cần vứt nó đi sau khi sử dụng xong.

Vì vậy, chúng tôi thực hiện cập nhật hàng đợi và sau đó chúng tôi không bao giờ xem lại quá trình chuyển đổi đó nữa.

Trong khi với học máy thông thường, bạn biết rằng chúng ta có toàn bộ mẫu dữ liệu

và sau đó chúng tôi lặp đi lặp lại dữ liệu đó.

Vì vậy, chúng ta có thể học hỏi từ mỗi ví dụ nhiều lần.

Được rồi, vậy bộ đệm phát lại hoạt động như thế nào?

Vì vậy, bạn có thể đoán nó làm gì dựa vào tên của nó, bộ đệm phát lại.

Vì vậy, bộ đệm là thứ lưu trữ dữ liệu phát lại có nghĩa là chúng ta có thể phát lại mọi thứ

chúng ta đã thấy trong quá khứ.

Vì vậy, giống như phát lại một video hoặc thứ gì đó tương tự để học hỏi từ những gì bạn đã thấy.

Được rồi, vậy bộ đệm phát lại hoạt động như thế nào.

Vì vậy, bộ đệm phát lại là bộ nhớ có kích thước hữu hạn.

Vì vậy, bạn có một mảng có kích thước cố định, giả sử, lưu trữ những trải nghiệm trong quá khứ,

thường ở dạng bộ dữ liệu.

Vì vậy, chúng tôi muốn lưu trữ trạng thái, hành động, phần thưởng, trạng thái tiếp theo và cờ hoàn thành.

Được rồi, về cơ bản những gì nó nói ở đây.

Được rồi, điều này cho biết liệu tập phim có bị chấm dứt hay không.

Được rồi, đây là một chút đúng về cách thuật toán thay đổi,

mặc dù tôi nghĩ sẽ hữu ích hơn nếu xem xét mã mà chúng ta sẽ thấy sau,

nhưng dù sao tôi cũng sẽ đọc nó cho bạn.

Được rồi, số một là thu thập kinh nghiệm khi tác nhân tương tác với

trải nghiệm môi trường được lưu trữ trong bộ đệm phát lại.

Được rồi, đó rõ ràng là lấy mẫu để đào tạo thay vì sử dụng mẫu gần đây nhất

kinh nghiệm cập nhật mạng hàng đợi.

Một loạt trải nghiệm nhỏ được lấy mẫu ngẫu nhiên từ bộ đệm.

Được rồi, bạn cũng sẽ thấy điều này sau.

Vì vậy, không giống như học theo hàng đợi thông thường, chỉ thực hiện quá trình chuyển đổi gần đây nhất,

SAR là số nguyên tố và D rồi thực hiện cập nhật dựa trên đó.

Thay vì sử dụng cái mới nhất, chúng ta sẽ chỉ chọn cái ngẫu nhiên từ bản phát lại

thay vào đó hãy đệm và huấn luyện về điều đó.

Được rồi, điểm thứ ba là radian như một bản cập nhật.

Biết rằng chúng tôi bị hạn chế sử dụng lô được lấy mẫu, tính toán giá trị khóa

mục tiêu và mức tối thiểu.

Được rồi, tôi chỉ nói vậy thôi.

Được rồi, và quản lý bộ đệm, nếu bộ đệm đạt dung lượng tối đa,

những trải nghiệm cũ nhất bị loại bỏ để nhường chỗ cho những trải nghiệm mới.

Được rồi, về cơ bản tôi cũng đã nói điều đó trước đây.

Được rồi, bây giờ chúng ta có thể nói về lợi ích của bộ đệm phát lại.

Được rồi, vậy nó giúp được gì cho chúng ta?

Vì vậy, một, nó phá vỡ mối tương quan thời gian.

Vì vậy, bằng cách lưu trữ các trải nghiệm trong quá khứ và lấy mẫu ngẫu nhiên, bộ đệm phát lại đảm bảo

các cập nhật đó ít tương quan hơn, giúp mạng lưới thần kinh khái quát hóa tốt hơn.

Được rồi, vậy tại sao chúng lại ít tương quan hơn vì chúng ta chọn chúng một cách ngẫu nhiên

từ một danh sách rất, rất lớn?

Được rồi, nó có thể làm tăng hiệu quả lấy mẫu.

Điều đó cũng hợp lý vì chúng tôi đang sử dụng từng mẫu, từng trải nghiệm, chúng tôi thấy

nhiều lần để thực hiện bước giảm độ dốc.

Được rồi, nó nói thay vì loại bỏ từng trải nghiệm sau một lần cập nhật,

bộ đệm phát lại cho phép các trải nghiệm được sử dụng lại nhiều lần, giảm bớt

số lượng tương tác cần thiết với môi trường.

Được rồi, đó là những gì tôi đã nói.

Và điểm thứ hai cũng quan trọng.

Vì vậy, bằng cách sử dụng những trải nghiệm trước đó nhiều lần, điều này có nghĩa là chúng ta không có

để chơi trong môi trường càng nhiều.

Nói cách khác, chúng ta sẽ học với số bước ngắn hơn.

Vì vậy làm giảm số lượng tương tác cần thiết với môi trường.

Và đây là một khái niệm quan trọng trong học tập tăng cường,

chúng tôi gọi là hiệu quả mẫu.

Vậy bạn cần thu thập bao nhiêu mẫu từ môi trường để

đại lý để tìm hiểu?

Được rồi, điểm tiếp theo là giảm phương sai và ổn định việc học.

Vì vậy, việc sử dụng một lô nhỏ từ kinh nghiệm trước đây sẽ dẫn đến độ dốc ổn định hơn

cập nhật, giảm sự khác biệt trong học tập và ngăn chặn những biến động mạnh mẽ trong

cập nhật chính sách.

Được rồi, một cách để hiểu điều này là thông qua việc học sâu trước đây của bạn

kinh nghiệm.

Vì vậy, bạn có thể nhận thấy rằng nếu bạn thử nghiệm với các kích cỡ lô, khi bạn

có kích thước lô lớn hơn thì việc mất mạng nơ-ron ổn định hơn nhiều hoặc nhiều hơn

suôn sẻ hơn khi quá trình đào tạo tiếp tục so với ở thái cực khác, nếu bạn sử dụng, chẳng hạn,

một mẫu cho mỗi bản cập nhật giảm độ dốc, sự mất mát của bạn sẽ rất ồn ào.

Nói cách khác, điều này quay trở lại với ý tưởng truyền thống về thống kê,

ý tưởng cơ bản từ số liệu thống kê, đó là bạn càng có nhiều dữ liệu thì càng tốt

ước tính của bạn.

Nói cách khác, quy mô lô của bạn càng lớn thì ước tính tổn thất càng chính xác.

Được rồi, đó là cách chúng ta giảm thiểu sự khác biệt và ổn định việc học.

Được rồi, điểm tiếp theo là nó cho phép tắt việc học chính sách.

Vì tác nhân học từ kinh nghiệm được lưu trữ trong quá khứ nên quá trình học tập bị tắt

chính sách, nghĩa là nó có thể học hỏi từ kinh nghiệm được tạo ra bởi các chính sách khác nhau.

Điều này cho phép linh hoạt hơn trong đào tạo.

Chắc chắn.

Được rồi, điều quan trọng cần lưu ý là những trải nghiệm trước đó đã được

được tạo bởi chính sách cũ, đúng vậy, mỗi khi bạn cập nhật Q, điều đó có nghĩa là chính sách

đã thay đổi.

Vì vậy, đó chỉ là một điểm nhỏ theo ý kiến ​​​​của tôi.

Được rồi, chúng tôi có một số thách thức và hạn chế.

Vì vậy bộ đệm phát lại không hoàn hảo và đã có những cải tiến về nó

kể từ khi chúng được giới thiệu lần đầu tiên.

Vì vậy chúng ta có mức sử dụng bộ nhớ, bộ đệm phát lại lớn,

đòi hỏi bộ nhớ đáng kể, đặc biệt là trong môi trường nhiều chiều, như hình ảnh

nhiệm vụ RL dựa trên.

Được rồi, chẳng hạn như môi trường Atari.

Vì vậy, bạn đang lưu trữ hình ảnh của trò chơi điện tử khi bạn chơi.

Và tôi sẽ thảo luận chi tiết hơn sau tại sao điều này lại kém hiệu quả.

Nhưng hiện tại, bạn chỉ cần biết rằng việc sử dụng bộ nhớ có thể là một vấn đề nếu bạn muốn

lưu trữ rất nhiều dữ liệu.

Và sau đó chúng ta có sự cũ kỹ của dữ liệu.

Những trải nghiệm cũ hơn có thể trở nên ít phù hợp hơn nếu động lực môi trường hoặc chính sách

thay đổi đáng kể.

Được rồi, còn một siêu tham số để bạn chọn là kích thước của bản phát lại

đệm, phải không?

Vì vậy, có một sự đánh đổi là nếu bạn làm nó quá nhỏ thì bạn sẽ không tích trữ được

bấy nhiêu dữ liệu, nhưng ít nhất dữ liệu sẽ mới hơn.

Nhưng sau đó bạn cũng có thể đang bỏ đi một số lợi ích của việc phát lại

đệm nếu bạn đặt nó quá nhỏ phải không?

Vì vậy, nếu nó nhỏ thì bạn sẽ chỉ có những chuyển đổi gần đây nhất,

điều này mang lại cho chúng cơ hội tương quan cao hơn khi bạn lấy mẫu.

Được rồi, ngược lại nếu bạn có bộ đệm rất lớn thì một mẫu ngẫu nhiên sẽ được

ít có khả năng tương quan hơn, nhưng hiện tại bạn có rất nhiều dữ liệu cũ

có thể ở đó.

Được rồi, điểm tiếp theo là chiến lược lấy mẫu.

Vì vậy, đây là hướng tới các kỹ thuật tiên tiến hơn một chút.

Nhưng nó cho biết mặc dù việc lấy mẫu thống nhất rất đơn giản nhưng nó có thể không tối ưu.

Vì vậy, về cơ bản trong bộ đệm phát lại của bạn, khi bạn lấy mẫu từ nó, mọi mục trong

có xác suất được chọn bằng nhau.

Vâng, đó chính là ý tôi khi nói lấy mẫu thống nhất.

Vì vậy, các chiến lược lấy mẫu phức tạp hơn như PER.

Vậy PER, tôi không nghĩ nó xuất hiện ở đây, nhưng nó là viết tắt của từ ưu tiên

trải nghiệm lại.

Có thể giới thiệu thêm các siêu tham số và độ phức tạp tính toán.

Tôi sẽ chỉ viết nó trong PER.

PER, có một dấu ngoặc ở đó phải không?

Ưu tiên phát lại trải nghiệm.

Vì vậy, bạn có thể tra cứu nó nếu bạn thích.

Về cơ bản những gì các phương pháp khác này làm là xem xét các chuyển đổi mà bạn

Mạng Q gặp khó khăn nhất trong việc ước tính.

Được rồi, đó là những thứ bạn muốn lấy mẫu để có thể học hỏi từ

Về cơ bản, những điều bạn đang mắc phải sai lầm nhất chính là điều bạn muốn

làm như một con người chẳng hạn, phải không?

Được rồi, tóm lại, bộ đệm phát lại là thành phần cơ bản của DQN.

Tôi sẽ chỉ đọc phần rút ra, nhưng bạn có thể tự đọc nếu muốn.

Được rồi, bộ đệm phát lại giảm thiểu các vấn đề về tương quan tuần tự và

hiệu quả lấy mẫu

Vâng.

Vì vậy, chúng tôi đã trải qua điều đó.

Vì vậy việc lấy mẫu ngẫu nhiên giúp đào tạo mạng của bạn hiệu quả hơn.

Chúng tôi đã trải qua sự khác biệt đó như ưu tiên phát lại trải nghiệm và chứng minh

học tập, nhưng lại đưa ra sự đánh đổi.

Phải.

Vì vậy, tôi đoán có một điều tôi chưa đề cập đến là nếu bạn sử dụng một mẫu khác

chiến lược, điều đó có thể đòi hỏi nhiều logic và mã cho biết bạn có thể không muốn

phải nỗ lực để hiểu.

Và sau đó chúng tôi đã quản lý bộ đệm phát lại một cách hiệu quả, điều quan trọng là tối ưu

hoặc hiệu suất, phải không?

Vì vậy, việc chọn kích thước, v.v.

Được rồi.

Vì vậy bây giờ tôi muốn xem qua một số cách triển khai ví dụ chỉ để cung cấp cho bạn một

ý tưởng cụ thể hơn về cách thức hoạt động của nó.

Phải.

Vì vậy cách thực hiện đơn giản nhất về cơ bản chỉ là một danh sách.

Phải.

Và vì vậy, trong phiên bản đầu tiên của khóa học này, học tăng cường sâu là

thực sự là những gì chúng tôi đã sử dụng.

Vì vậy, bộ đệm chỉ là một danh sách, ngẫu nhiên quan trọng, vì nó được sử dụng cho

lấy mẫu ngẫu nhiên.

Và sau đó chúng tôi chỉ định kích thước lô mà tôi vừa nói là 32.

Đây là một số dữ liệu giả.

Vì thế trạng thái hành động, khen thưởng, trạng thái tiếp theo và thực hiện.

Tôi vừa nói với 12345.

Và chức năng quan trọng của việc này là lưu trữ các sản phẩm lấy mẫu theo lô.

Và khi bộ đệm đầy, chúng ta cần xóa mục cũ nhất để

rằng chúng ta có thể lưu trữ một mặt hàng mới.

Được rồi.

Vì vậy, nếu bộ đệm không đầy, việc lưu trữ một mục rất dễ dàng.

Chúng tôi chỉ gọi buffer.append, vì đó là một danh sách và phần bổ sung là cách bạn thêm mọi thứ vào

một danh sách.

Và quan trọng, điều này sẽ được thêm vào cuối danh sách.

Vì vậy, trật tự rất quan trọng trong trường hợp này bởi vì chúng ta luôn muốn loại bỏ

mẫu cổ nhất.

Được rồi.

Và đây là cách chúng tôi lấy mẫu một đợt.

Vì vậy, chúng tôi gọi Random.sample, chuyển vào bộ đệm mà chúng tôi muốn lấy mẫu từ đó và

số lượng mẫu chúng tôi muốn, tức là cỡ lô.

Được rồi.

Được rồi.

Và sau đó chúng ta gặp vấn đề làm cách nào để lưu trữ một mục khi bộ đệm đầy.

Và thật may mắn là nó cũng được tích hợp vào Python.

Nếu bạn muốn xóa mục đầu tiên khỏi danh sách, bạn chỉ cần gọi buffer.pop0.

Được rồi.

Và về cơ bản, điều này, mặc dù trông có vẻ sạch sẽ nhưng lại khá kém hiệu quả.

Vì vậy, pop zero phải là O của một thao tác, nhưng có một số chi phí cần thiết trong

đối phó với những vấn đề nảy sinh mà bạn phải làm.

Vì vậy, sau này, chúng tôi có một triển khai tốt hơn.

Vì vậy, đây là những gì chúng ta sẽ sử dụng cho một phần của khóa học này.

Và cách thức hoạt động của nó là như vậy.

Và nhân tiện, nếu bạn tham gia khóa học TensorFlow 2 hoặc khóa học PyTorch của tôi, bạn

lẽ ra đã thấy điều này rồi.

Nhưng về cơ bản, nó sử dụng các mảng được phân bổ trước, được xác định trước để lưu trữ

dữ liệu.

Được rồi.

Vì vậy chúng ta tạo một lớp gọi là bộ đệm phát lại.

Và trong hàm khởi tạo, chúng tôi lấy kích thước của bộ đệm.

Được rồi.

Và vì vậy chúng tôi sử dụng điều đó để chỉ định kích thước của tất cả các mảng của mình.

Và vì vậy hãy lưu ý rằng chúng tôi lưu trữ từng mục riêng biệt.

Vì vậy, op một, đó là trạng thái hiện tại, op hai, đó là trạng thái tiếp theo, hoạt động như

hành động.

EW của chúng tôi là phần thưởng và hoàn thành là cờ hoàn thành.

Được rồi.

Và vì vậy hãy lưu ý rằng điều này hơi thiếu linh hoạt vì chúng ta chuyển vào OV

mờ như chiều thứ hai.

Vì vậy, điều này chỉ hoạt động khi giả sử rằng trạng thái của bạn là vectơ một chiều.

Và vì vậy chúng ta có một số biến quan trọng.

Vì vậy, chúng tôi có con trỏ, chúng tôi có kích thước dấu chấm tự và chúng tôi có kích thước tối đa tự đặt tên.

Vậy đây là những gì?

Vì vậy, kích thước dấu chấm tự hoặc kích thước tối đa của dấu chấm.

Đó là kích thước tối đa của bộ đệm.

Vì vậy, số lượng mặt hàng tối đa chúng ta có thể lưu trữ.

Vì vậy, kích thước, lưu ý rằng nó bắt đầu từ 0 là kích thước của bộ đệm hiện tại.

Phải.

Vì vậy, nếu chúng tôi chưa thêm bất kỳ mục nào thì kích thước sẽ bằng 0.

Nếu chúng tôi đã thêm một mục thì kích thước sẽ là một.

Nếu chúng tôi đã thêm hai mục thì kích thước sẽ là hai, v.v.

Được rồi.

Và con trỏ mục tiếp theo là một biến quan trọng khác.

Vậy điều này sẽ diễn ra như thế nào?

Về cơ bản, bạn có thể tưởng tượng bộ đệm của mình như một chồng các mục.

Và con trỏ sẽ trỏ tới vị trí của mục gần đây nhất.

Phải.

Và cách thức hoạt động của nó là khi chúng ta đến cuối ngăn xếp, giả sử như vậy

con trỏ sẽ ở cuối và mục cũ nhất sẽ ở phía trước.

Vì vậy, về cơ bản, khi chúng ta đến cuối, chúng ta đặt con trỏ về 0.

Và sau đó chúng tôi thay thế bất cứ thứ gì ở đó bằng quá trình chuyển đổi mới khi chúng tôi thêm nó.

Vì vậy, con trỏ luôn trỏ đến nơi cần thêm mục mới nhất.

Vì vậy, theo một cách nào đó, nó là một vòng tròn.

Vì thế khi chưa đầy chúng ta chỉ cần thêm từng món một vào.

Nhưng khi nó đầy thì chúng ta lặp lại từ đầu rồi thêm các mục

bắt đầu lại từ đầu.

Được rồi.

Và điều đó dễ hiểu hơn, có thể là bằng mã.

Được rồi.

Vì vậy, khi chúng ta cất giữ một món đồ, chúng ta tiến hành quan sát, hành động, khen thưởng, tiếp theo

quan sát, nó đã được thực hiện.

Chúng tôi lưu trữ nó tại chỉ mục được biểu thị bằng self.

Điểm.

Được rồi.

Vậy là tất cả những thứ này đã được thiết lập.

Và vì vậy hãy chú ý cách chúng tôi cập nhật con trỏ.

Vì vậy, con trỏ thông thường sẽ chỉ là con trỏ cộng một, phải không?

Bởi vì chúng tôi muốn đặt quá trình chuyển đổi tiếp theo vào vị trí tiếp theo trong bộ đệm.

Nhưng khi đã đến đích, chúng ta lại không muốn tiếp tục nữa.

Chúng tôi muốn quay lại từ đầu.

Vậy là chúng ta đã mod self dot max size.

Vì vậy, khi bạn đạt đến điểm cuối, số này sẽ trở về số 0.

Và sau đó chúng ta có kích thước điểm tự.

Vì vậy, nếu bộ đệm không đầy và kích thước dấu chấm tự chỉ trở thành kích thước dấu chấm cộng một

bởi vì chúng tôi đã thêm một mục nữa, nếu không thì nó chỉ ở kích thước tối đa.

Vì chúng ta đã lấp đầy bộ đệm phát lại.

Được rồi.

Và cuối cùng chúng ta có lô mẫu, chỉ chọn một loạt mẫu ngẫu nhiên

chỉ số.

Vì vậy, một lần nữa, hãy lưu ý rằng đây là một mẫu thống nhất.

Vì vậy, chúng tôi không chờ đợi xác suất.

Mọi mẫu đều có cơ hội được chọn như nhau với kích thước lô lớn.

Và sau đó chúng tôi lập chỉ mục cho từng mục của mình bằng các chỉ mục này.

Và nhân tiện, chúng tôi trả lại nó dưới dạng một lệnh.

Vì vậy, ARD sẽ là chìa khóa cho cuốn từ điển đó.

Được rồi.

Vì vậy, bây giờ hãy nói về các vấn đề tiềm ẩn với thiết lập này.

Vì vậy, bộ đệm phát lại vốn đã khiến bạn lưu trữ thông tin dư thừa.

Được rồi.

Và cách dễ nhất để thấy điều này là chỉ viết ra các chuyển đổi.

Vậy ta có S1, A1, S2, R2, D2.

Nhưng ở bước tiếp theo, quan sát hiện tại sẽ là S2.

Vì vậy, một cách hiệu quả, chúng tôi đã lưu trữ S2 hai lần.

Và chúng tôi lưu trữ S3 hai lần, v.v.

Được rồi.

Vì vậy, có một chút dư thừa trong bộ đệm phát lại.

Chúng tôi lưu trữ hầu hết các tiểu bang hai lần.

Được rồi.

Bây giờ, khi chúng ta xem xét các trò chơi Atari hoặc bất kỳ trò chơi điện tử nào mà bạn thực hiện điều này hoặc bất kỳ môi trường nào

khi bạn làm điều này, sự dư thừa thậm chí còn tệ hơn vì chúng tôi sử dụng bốn khung hình cuối cùng

mà chúng ta coi là trạng thái.

Và điều này còn tệ hơn nữa vì bốn khung hình này đều là hình ảnh.

Vì vậy, nó giống như một hình ảnh màu 84 x 84 so với trường hợp Carpool

nó chỉ là một vector bốn chiều.

Vì vậy, sự dư thừa này không quá quan trọng.

Được rồi.

Vì vậy, đối với Atari, điều đó còn tệ hơn về nhiều mặt vì bản thân bang này lớn hơn nhiều.

Nhưng chúng tôi cũng đang tạo ra nhiều sự dư thừa hơn bằng cách xếp chồng các quan sát này lại với nhau.

Được rồi.

Vậy để diễn đạt điều này bằng những thuật ngữ cụ thể hơn, hãy gọi trạng thái là bốn,

đó sẽ là 01020304.

Trong bốn quan sát cuối cùng.

Và vì vậy chúng ta sẽ giả định điều đó ngay từ đầu, nếu bước thời gian là trước 4,

chúng tôi sẽ không làm bất cứ điều gì vì chúng tôi không có đủ quan sát để đưa ra trạng thái đầy đủ.

Được rồi. Nhưng bây giờ hãy nhìn vào điều này.

Vậy chúng ta có 01020304.

Sau đó chúng ta có 02030405.

Vậy là bạn đã thấy rằng có sự dư thừa ngay cả trong một lần chuyển đổi.

Được rồi. 020304 được lặp lại.

Và sau đó chúng ta chuyển sang phần chuyển tiếp tiếp theo và sau đó 020304 được lặp lại một lần nữa rồi lại 05.

Được rồi. Vậy và sau đó chúng ta lại có 03.

Vậy số 03 ở đây bằng bao nhiêu lần?

Chỉ có hai cái này thôi.

Phải. Vậy là một lần, hai lần, ba lần, bốn lần.

Vì vậy, chúng tôi đã lưu trữ 03 rất nhiều lần chỉ trong hai lần chuyển đổi.

Được rồi. Và giải pháp cho vấn đề này là gì?

Vì vậy, giải pháp cho vấn đề này đòi hỏi mã hóa khá phức tạp.

Vì vậy, tôi không khuyên bạn nên cố gắng tự làm điều đó.

Ngày nay có những thư viện như đường cơ sở ổn định của AI mở triển khai bộ đệm phát lại

giúp giải quyết một số sự thiếu hiệu quả này.

Và đó là những gì chúng tôi sẽ sử dụng khi triển khai phương pháp học tập sâu cho Atari.

Được rồi. Và điều cuối cùng tôi muốn nói đến trong bài giảng này là điều này thay đổi thuật toán học Q như thế nào.

Được rồi. Vì vậy, có một vài thay đổi quan trọng mà chúng ta phải thực hiện.

Vì vậy, trước tiên, vì hiện tại chúng tôi chỉ đào tạo các lô mà chúng tôi truy xuất từ bộ đệm phát lại

thay vì rèn luyện về môi trường sống khi chúng ta gặp phải các trạng thái và phần thưởng, v.v.

Điều đó có nghĩa là chúng ta cần có dữ liệu trong bộ đệm phát lại trước khi bắt đầu làm bất cứ điều gì.

Được rồi. Vì vậy, bây giờ có một giai đoạn khác của quá trình đào tạo này, đó chỉ là thu thập dữ liệu.

Vì vậy, chúng tôi đã xác định trước số bước chúng tôi muốn thực hiện việc thu thập dữ liệu này, tức là chúng tôi muốn bộ đệm phát lại lớn đến mức nào trước khi bắt đầu lấy mẫu từ nó.

Được rồi. Và đó là giai đoạn đầu tiên của thuật toán này.

Vì vậy, chúng tôi thực hiện bốn bước không quan trọng trong phạm vi các bước thu thập dữ liệu.

Và sau đó bạn chỉ cần thực hiện các hành động ngẫu nhiên trong môi trường.

Bạn nhận được trạng thái tiếp theo và phần thưởng, v.v. Và sau đó bạn lưu trữ những giá trị đó.

Được rồi. Và sau đó cũng đừng quên thiết lập trạng thái tiếp theo.

Thực ra, tôi nghĩ có lẽ tôi cũng đã bỏ lỡ điều đó ở đây.

Vâng. Vì vậy, tôi sẽ chỉ thêm nó vào đây. Như tôi đã nói, thật dễ dàng để quên.

Được rồi. Và do đó, bước thứ hai khi bộ đệm phát lại chưa đầy nhưng đủ đầy.

Vì vậy, nó sẽ không phải là kích thước tối đa, mặc dù nó có thể phụ thuộc vào lựa chọn thiết kế của bạn.

Bây giờ bạn đã sẵn sàng cập nhật Q. Vì vậy, Q như thường lệ sẽ được khởi tạo ngẫu nhiên.

Và sau đó bạn lặp lại bất kỳ số bước đào tạo nào mà bạn đã quyết định.

Và vòng lặp này gần giống như trước, nhưng hơi khác một chút.

Vì vậy, chúng tôi chọn hành động của mình dựa trên lòng tham epsilon.

Chúng tôi thực hiện hành động đó trong môi trường. Vì vậy chúng tôi gọi nó là bước chẵn V chấm.

Chúng tôi nhận lại phần thưởng hành động trạng thái tiếp theo và cờ hoàn thành.

Và một lần nữa, tôi đang đơn giản hóa điều này, phải không?

Vì thế phiên bản cũ của Jim hay gymnasium thường chỉ trả cờ xong.

Và ngày nay chúng ta có cờ đã hoàn thành và cờ đã cắt bớt.

Nhưng tôi sẽ giả sử để đơn giản rằng nó chỉ là cái này.

Được rồi. Và có một điều nhỏ nữa tôi đã thêm vào.

Vì vậy, điều này là không bắt buộc, nhưng tôi đã thấy nó trong nhiều cách triển khai khác nhau.

Và có vẻ như nó khá thành công.

Vì vậy, về cơ bản, cách thức hoạt động của nó là thay vì luyện tập mỗi khi chúng ta thực hiện một bước trong môi trường,

điều mà chúng tôi thực sự không cần phải làm vì chúng tôi thậm chí không sử dụng bước đó cho quá trình đào tạo.

Chúng tôi chỉ chọn các mẫu ngẫu nhiên từ bộ đệm để huấn luyện.

Chúng ta không cần phải luyện tập từng bước.

Vì vậy, chúng ta có thể nói luyện tập cứ sau ba bước hoặc cứ năm bước.

Và một lần nữa, đó chính xác là bao nhiêu bước là một siêu tham số để bạn thử nghiệm.

Được rồi.

Vì vậy, nếu chúng ta quyết định luyện tập ở bước này thì đây là những gì chúng ta sẽ làm.

Vì vậy, chúng tôi lấy mẫu một lô từ bộ đệm của mình.

Và về cơ bản, từ đó chúng tôi có thể tính toán các dự đoán, mục tiêu của mình,

và sau đó thực hiện bước giảm độ dốc.

Được rồi. Vì vậy, mục tiêu sẽ là, và tôi vừa giả định rằng đây là cú pháp.

Tuy nhiên, rõ ràng với cách triển khai ở trên, điều đó sẽ không xảy ra.

Nhưng đối với mục tiêu, đó sẽ là phần thưởng.

Vì vậy, batch.r cộng với gamma nhân với giá trị tối đa trên q cho các trạng thái tiếp theo.

Vậy đó sẽ là đợt s2.

Và dấu hai chấm này chỉ có nghĩa là hành động tổng thể.

Được rồi. Vì vậy, hãy trả lại tất cả các hành động và sau đó chọn hành động tốt nhất.

Và sau đó là một dấu chấm trừ của lô d, đó là cờ đã hoàn thành.

Vì vậy, nếu cờ done là đúng, chúng tôi chỉ muốn phần thưởng vì không có trạng thái tiếp theo.

Và đối với dự đoán, đó chỉ là mạng q được đánh giá cho trạng thái hiện tại s.

Được rồi. Backstatt s.

Và sau khi có dự đoán và mục tiêu, chúng tôi có thể tính toán tổn thất của mình, đó là sai số bình phương.

Và sau đó chúng tôi thực hiện giảm độ dốc trên đó.

Được rồi. Và như bạn đã thấy, chúng ta đặt trạng thái hiện tại sang trạng thái tiếp theo.

Được rồi. Đó là cách chúng tôi đào tạo trong bối cảnh hiện tại.

Vì vậy, chúng tôi thực hiện bộ đệm phát lại.

Vì vậy, nó không giống như học theo hàng đợi thông thường khi ngay khi bạn gặp một quá trình chuyển đổi, bạn sẽ sử dụng điều đó để huấn luyện mạng.

Thay vào đó, bạn chỉ cần thu thập một loạt dữ liệu rồi chọn ngẫu nhiên dữ liệu để đào tạo khi bạn thu thập thêm dữ liệu thông qua môi trường.

Được rồi. Vì vậy, tôi nhận ra rằng tôi vừa quên thêm một điều ở đây.

Mặc dù đây là mã giả.

Tôi vẫn muốn nó đúng.

Vì vậy tôi sẽ đi theo dòng này.

Và vấn đề là ngay cả khi bạn đang luyện tập, bạn vẫn tiếp tục thêm những chuyển tiếp này vào bộ đệm phát lại.

Được rồi. Vì vậy, chúng ta sẽ lắp nó vào đây.

Được rồi. Vì vậy, bạn chọn hành động của mình dựa trên sự tham lam của epsilon.

Thực hiện hành động đó trong môi trường.

Lấy lại trạng thái tiếp theo.

Phải. Điều này cũng không đúng.

Được rồi. Vì vậy, chúng tôi không lấy lại hành động từ ENV.step.

Chúng ta chỉ nhận lại phần thưởng và lá cờ đã hoàn thành.

Được rồi. Nhưng hành động này xuất phát từ sự tham lam của epsilon.

Và sau đó chúng tôi thêm quá trình chuyển đổi này.

Vậy là chúng ta có S2RD từ ENV.step.

Chúng tôi có A từ epsilon tham lam.

Và S là trạng thái hiện tại mà chúng ta sử dụng để xác định hành động.

Được rồi. Vì vậy, về cơ bản, điều quan trọng ở đây là đừng quên tiếp tục thêm các hiệu ứng chuyển tiếp vào bộ đệm phát lại khi bạn đang luyện tập.