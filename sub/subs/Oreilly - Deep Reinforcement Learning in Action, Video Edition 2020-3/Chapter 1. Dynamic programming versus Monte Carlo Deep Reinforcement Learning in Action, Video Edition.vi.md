# Chương 1. Lập trình động so với Học tập tăng cường sâu Monte Carlo trong thực tế, Video Edition.vi

---

1.3 Lập trình động với Monte Carlo. Bây giờ bạn đã biết rằng bạn có thể huấn luyện một thuật toán

để thực hiện một số nhiệm vụ cấp cao bằng cách chỉ định một phần thưởng cao cho việc hoàn thành nhiệm vụ

nhiệm vụ đó có nghĩa là phần thưởng tích cực, và phần thưởng tiêu cực cho những thứ chúng tôi không muốn nó làm.

Hãy làm điều này để trở thành cụ thể. Giả sử cao cấp mục là huấn luyện robot

Hút bụi di chuyển từ một căn hộ trong nhà đến bến của nó, nằm trong bếp. Nó có bốn

hành động - đi sang trái, đi sang phải, đi tới và lùi. Tại mỗi thời điểm, robot cần

Xác định xem sẽ thực hiện bất kỳ hành động nào trong bốn hành động này. If to be be,

nó sẽ được thưởng 100 điểm, và nếu có bất cứ điều gì nhỏ nhặt trên đường đi thì nó sẽ bị trừ 10 điểm.

Giả sử rằng robot có bản đồ hoàn thiện 3D của ngôi nhà và vị trí chính xác của bến,

nhưng vẫn chưa biết chính xác trình tự cơ sở hành động nào để thực hiện để đến

được bến. Một cách tiếp theo để giải quyết vấn đề này được gọi là cài đặt chương trình động (DP), trước hết

được Richard Bellman đưa ra vào năm 1957. Quá trình lập trình có thể được gọi là abortion

tiêu điểm, vì nó giải quyết các vấn đề phức tạp cấp độ bằng cách phân tích chúng thành các bài toán

con nhỏ hơn, cho đến khi tìm được bài toán con đơn giản có thể giải quyết mà không cần thêm thông tin.

Thay đổi để rô-bốt đưa ra cơ sở hành động dài chuỗi để đưa ra yêu cầu,

trước tiên nó có thể chia nhỏ bài toán thành "mở lại phòng này" so với "rời khỏi

phòng này". Vì đã có bản đồ hoàn chỉnh về ngôi nhà nên robot biết rằng nó cần thiết

phải rời khỏi phòng, vì cầu ở trong bếp. Hành động chuỗi nào chưa được biết

sẽ cho phép nó rời khỏi phòng, vì vậy nó chia bài toán nhỏ thành "chuyển về

phía cửa" hoặc "chuyển ra xa khỏi cửa". Vì gần với yêu cầu hơn và có

đường dẫn từ cửa đến yêu cầu, rô-bốt

biết rằng nó cần phải chuyển về phía cửa.

Nhưng một lần nữa, nó không biết

cơ sở hành động chuỗi nào sẽ được đưa ra

bên cửa sổ. Cuối cùng, cần phải quyết định xem liệu có nên chuyển sang trái, phải, phía trước không

hoặc đảo ngược. Nó có thể thấy cánh cửa ở trước mặt nó, nó chuyển về phía bên

trước. Nó tiếp tục quá trình này cho đến khi ra khỏi phòng, khi nó phải phân tích

mục tiêu nhiều hơn nữa cho đến khi được bến tàu. Đây là bản chất của trình động lập trình.

Đây là một phương pháp chung để giải quyết một số loại vấn đề có thể được chia nhỏ thành các vấn đề

đề phụ và vấn đề con, and no có ứng dụng trong nhiều lĩnh vực, bao gồm bao tin sinh học, kinh tế và

khoa học máy tính. Để áp dụng trình cài đặt của Bellman, chúng tôi phải có khả năng chia sẻ vấn đề

đề thành các vấn đề phụ mà chúng tôi biết cách giải quyết. Nhưng ngay cả giả định có vẻ vô hại

Điều này cũng khó thực hiện trong thế giới thực. Làm cách nào để bạn chia nhỏ cao cấp mục tiêu cho một

Chiếc xe tự lái "chuyển đến điểm B từ điểm A mà không bị đau" thành các vấn đề

không có hạt nhỏ? Liệu một đứa trẻ có học cách đi bộ bằng cách đầu tiên giải quyết các vấn đề

đi bộ nhỏ dễ dàng hơn không? Trong RL, nơi chúng tôi thường gặp các vấn đề có thể

bao gồm một số yếu tố ngẫu nhiên, chúng ta không thể áp dụng trình động chính xác như Bellman đã nêu

làm theo phương pháp này. Thực tế, DP có thể được coi là cực đoan của phương pháp chuỗi

giải pháp giải quyết vấn đề, trong khi cực đoan kia là thử và sai.

Một cách khác để xem bài học chuỗi này là trong một số vấn đề mà chúng tôi có kiến thức tối ưu

đa số về môi trường và một số khác chúng tôi có kiến thức tối thiểu về môi trường và chúng tôi

cần sử dụng các chiến lược khác nhau cho từng trường hợp. Nếu bạn muốn sử dụng nhà vệ sinh

Tại nhà mình, bạn biết chính xác, ít nhất là theo tiềm thức, trình tự động của cơ sở

bạn có thể đưa ra nhà vệ sinh từ bất kỳ vị trí ban đầu nào, tức là theo cách thiết lập động.

Điều này là bạn có biết căn nhà của mình không. Bạn có bản đồ hoàn hảo hoặc ít ra gần

hoàn hảo về ngôi nhà trong tâm trí. Nếu bạn đến dự tiệc tại một ngôi nhà chưa bao

Giờ đến trước đó, bạn có thể phải đi vòng quanh cho đến khi tự tìm được nhà vệ sinh,

tức là theo phương pháp thử và sai, vì bạn không có bản đồ tốt về ngôi nhà của người đó.

Thử nghiệm và nhìn chung sai sót

nằm trong phương pháp Monte Carlo.

Phương pháp Monte Carlo về cơ bản là lấy mẫu ngẫu nhiên từ môi trường. Trong nhiều vấn đề trong thế

thực tế, chúng tôi ít nhất cũng có một số người hiểu biết về cách thức hoạt động của môi trường, vì vậy

chúng tôi sử dụng chiến lược ma trận bao gồm một số lượng thử nghiệm và sai sót và một số lượng nào đó

khai thác những điều chúng tôi đã biết về môi trường để trực tiếp tiếp tục giải quyết các mục tiêu một cách dễ dàng.

Một ví dụ thoáng chốc về một chiến lược logic sẽ là nếu bạn bị mất mắt, được đặt ở một địa điểm

không xác định được nhà mình và được bảo vệ bằng cách ném đá và nghe tiếng động.

Bạn có thể bắt đầu bằng cách phân tích mục tiêu cấp cao "tìm phòng tắm" thành một mục tiêu

Dễ dàng tiếp cận hơn "tìm thấy mình đang ở trong phòng nào". Để giải quyết mục tiêu phụ này, bạn có

có thể xử lý một số đá theo hướng ngẫu nhiên và đánh giá kích thước của căn hộ, điều kiện

Điều này có thể cung cấp cho bạn đủ thông tin để suy ra căn hộ bạn đang ở, hạn chế như phòng ngủ.

Sau đó, bạn sẽ cần chuyển sang một mục tiêu phụ khác, điều hướng đến cửa sổ để bạn có

can go to action lang. Sau đó, bạn sẽ bắt đầu ném lại, nhưng vì bạn nhớ các kết quả

sau lần ngẫu nhiên gần nhất, bạn đã có thể

bắn vào những vị trí mà bạn chưa chắc chắn.

Bằng cách lặp lại công việc trong quá trình này, cuối cùng bạn cũng có thể tìm thấy vị trí

vị trí nhà vệ sinh. Trong trường hợp này, bạn sẽ thực hiện phân tách mục

tiêu điểm bằng cách thiết lập động và lấy ngẫu nhiên mẫu của các phương pháp Monte Carlo.