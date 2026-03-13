# Chương 8. Khám phá theo hướng tò mò Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Chương 8. Khám phá theo hướng tò mò

Chương này đề cập đến việc tìm hiểu Vấn đề Phần thưởng thưa thớt, hiểu mức độ tò mò

có thể đóng vai trò như một phần thưởng nội tại, chơi Super Mario Bros. từ OpenAI Jim, triển khai

một mô-đun tò mò nội tại trong PyTorch, đào tạo một tác nhân mạng Q chuyên sâu để chơi thành công

Super Mario Bros. không sử dụng phần thưởng.

Các thuật toán học tăng cường cơ bản mà chúng tôi đã nghiên cứu cho đến nay, chẳng hạn như Q sâu

phương pháp học tập và gradient chính sách, là những kỹ thuật rất mạnh mẽ trong nhiều tình huống,

nhưng họ đã thất bại thảm hại ở những môi trường khác.

Tâm trí sâu sắc của Google đã đi tiên phong trong lĩnh vực học tăng cường sâu vào năm 2013, khi

họ đã sử dụng công nghệ học Q sâu để đào tạo một đặc vụ chơi nhiều trò chơi Atari tại siêu nhân

mức độ thực hiện.

Nhưng hiệu suất của tác nhân rất khác nhau giữa các loại trò chơi khác nhau.

Ở một thái cực, đặc vụ DQN của họ đã chơi trò chơi Atari hay hơn rất nhiều so với trò chơi

con người, nhưng ở một thái cực khác, DQN còn tệ hơn nhiều so với con người khi chơi trò chơi của Montezuma

Trả thù, Hình 8.1, nơi nó thậm chí không thể vượt qua cấp độ đầu tiên.

Hình 8.1, ảnh chụp màn hình từ trò chơi Montezuma's Revenge Atari.

Người chơi phải vượt qua các chướng ngại vật để lấy chìa khóa trước khi nhận được bất kỳ phần thưởng nào.

Ghi chú.

Bài báo gây chú ý lớn đến lĩnh vực học tăng cường sâu là

kiểm soát cấp độ con người thông qua học tập tăng cường sâu của Volodymyr Trini và cộng tác viên

tại Google Deep Mind vào năm 2015.

Bài viết khá dễ đọc và chứa các chi tiết bạn cần để tái tạo kết quả của họ.

Chính sự khác biệt giữa các môi trường giải thích những khác biệt về hiệu suất này.

Những game mà DQN thành công đều đưa ra phần thưởng tương đối thường xuyên trong quá trình chơi

và không yêu cầu lập kế hoạch dài hạn đáng kể.

Mặt khác, Montezuma's Revenge chỉ trao phần thưởng sau khi người chơi tìm được chìa khóa

trong căn phòng cũng chứa vô số chướng ngại vật và kẻ thù.

Với DQN vani, đặc vụ bắt đầu khám phá về cơ bản một cách ngẫu nhiên.

Nó sẽ thực hiện các hành động ngẫu nhiên và chờ đợi để quan sát phần thưởng, và những phần thưởng đó sẽ củng cố hành động đó.

những hành động tốt nhất nên thực hiện vì môi trường.

Nhưng trong trường hợp của Montezuma's Revenge, rất khó có khả năng đặc vụ sẽ

tìm chìa khóa và nhận phần thưởng với chính sách khám phá ngẫu nhiên này để nó không bao giờ quan sát được

một phần thưởng và sẽ không bao giờ học được.

Vấn đề này được gọi là Vấn đề phần thưởng thưa thớt, vì phần thưởng trong môi trường là

phân bố thưa thớt, Hình 8.2.

Nếu tác nhân không quan sát đủ tín hiệu khen thưởng để củng cố hành động của mình thì nó không thể

học hỏi.

Hình 8.2.

Trong môi trường có phần thưởng dày đặc, phần thưởng được nhận khá thường xuyên trong quá trình huấn luyện

thời gian, giúp dễ dàng củng cố hành động.

Trong Môi trường phần thưởng thưa thớt, phần thưởng chỉ có thể nhận được sau khi hoàn thành nhiều mục tiêu phụ,

gây khó khăn hoặc không thể học hỏi chỉ dựa trên tín hiệu phần thưởng.

Việc học của động vật và con người cung cấp cho chúng ta những ví dụ tự nhiên duy nhất về hệ thống thông minh và

chúng ta có thể tìm đến họ để lấy cảm hứng.

Thật vậy, các nhà nghiên cứu đang cố gắng giải quyết Vấn đề Phần thưởng thưa thớt này nhận thấy rằng con người không

chỉ tối đa hóa những phần thưởng bên ngoài, những phần thưởng từ môi trường, như thức ăn và tình dục, nhưng chúng

cũng thể hiện sự tò mò nội tại, động lực khám phá chỉ vì mục đích

hiểu cách mọi thứ hoạt động và giảm bớt sự không chắc chắn về môi trường của họ.

Trong chương này, bạn sẽ tìm hiểu về các phương pháp đào tạo thành công học tăng cường

các tác nhân trong Môi trường Phần thưởng thưa thớt bằng cách sử dụng các nguyên tắc từ trí thông minh của con người, cụ thể là,

sự tò mò bẩm sinh của chúng ta.

Bạn sẽ thấy sự tò mò có thể thúc đẩy sự phát triển các kỹ năng cơ bản mà nhân viên có thể sử dụng như thế nào.

hoàn thành các mục tiêu phụ và tìm Phần thưởng thưa thớt.

Đặc biệt, bạn sẽ thấy một đặc vụ có trí tò mò có thể chơi trò chơi Super Mario của Atari như thế nào

Anh em hãy học cách di chuyển trên địa hình động chỉ bằng sự tò mò thôi.

Ghi chú.

Mã của chương này nằm trong kho GitHub của cuốn sách này trong thư mục chương 8.

Xem liên kết này.

Mục 8.1.

Giải quyết phần thưởng thưa thớt bằng mã hóa dự đoán.

Trong thế giới khoa học thần kinh và đặc biệt là khoa học thần kinh tính toán, có một khuôn khổ

để hiểu các hệ thống thần kinh ở mức độ cao được gọi là mô hình mã hóa dự đoán.

Trong mô hình này, lý thuyết cho rằng tất cả các hệ thống thần kinh từ tế bào thần kinh riêng lẻ cho đến tế bào thần kinh quy mô lớn đều

mạng lưới thần kinh đang chạy một thuật toán cố gắng dự đoán đầu vào và do đó cố gắng

để giảm thiểu sai số dự đoán giữa những gì nó mong đợi trải nghiệm và những gì nó thực sự trải qua.

những trải nghiệm.

Vì vậy, ở mức độ cao, khi bạn đang làm việc trong ngày, não của bạn sẽ tiếp nhận rất nhiều

thông tin cảm giác từ môi trường và nó được đào tạo để dự đoán cảm giác như thế nào

thông tin sẽ phát triển.

Nó đang cố gắng đi trước một bước so với dữ liệu thô thực tế được đưa vào.

Nếu có điều gì đáng ngạc nhiên, bất ngờ xảy ra.

Bộ não của bạn gặp phải một lỗi dự đoán lớn và sau đó có lẽ thực hiện một số tham số

cập nhật để ngăn điều đó xảy ra lần nữa.

Ví dụ, bạn có thể đang nói chuyện với một người bạn mới gặp và não bạn liên tục

cố gắng dự đoán từ tiếp theo mà người đó sẽ nói trước khi họ nói nó.

Vì đây là người mà bạn không quen biết nên não của bạn có thể sẽ có hiệu suất tương đối cao.

lỗi dự đoán trung bình, nhưng nếu trở thành bạn thân, có lẽ bạn sẽ khá tốt

khi kết thúc câu nói của họ.

Đây không phải là điều bạn cố gắng làm, dù muốn hay không, bộ não của bạn đang cố gắng làm điều đó.

giảm sai số dự đoán của nó.

Sự tò mò có thể được coi là một loại mong muốn giảm bớt sự không chắc chắn trong môi trường của bạn

và do đó, giảm lỗi dự đoán.

Nếu bạn là một kỹ sư phần mềm và thấy một số bài viết trực tuyến về điều thú vị này

lĩnh vực được gọi là học máy, sự tò mò của bạn khi muốn đọc một cuốn sách như thế này sẽ dựa trên

mục tiêu giảm bớt sự không chắc chắn của bạn về học máy.

Một trong những nỗ lực đầu tiên nhằm truyền cho các tác nhân học tăng cường cảm giác tò mò liên quan

sử dụng cơ chế dự đoán lỗi.

Ý tưởng là ngoài việc cố gắng tối đa hóa các yếu tố bên ngoài, tức là môi trường được cung cấp,

phần thưởng, tác nhân cũng sẽ cố gắng dự đoán trạng thái tiếp theo của môi trường dựa trên

hành động và nó sẽ cố gắng giảm lỗi dự đoán của nó.

Trong các khu vực rất quen thuộc của môi trường, tác nhân sẽ tìm hiểu cách thức hoạt động và sẽ

có sai số dự đoán thấp.

Bằng cách sử dụng lỗi dự đoán này như một loại tín hiệu khen thưởng khác, đại lý sẽ được khuyến khích

đến thăm các khu vực của môi trường mới lạ và chưa được biết đến.

Nghĩa là, sai số dự đoán càng cao thì trạng thái càng đáng ngạc nhiên và do đó

tác nhân nên được khuyến khích truy cập vào các trạng thái lỗi dự đoán cao này.

Hình 8.3 cho thấy khuôn khổ cơ bản của phương pháp này.

Hình 8.3, lỗi dự đoán được tóm tắt bằng phần thưởng môi trường bên ngoài để sử dụng

đại lý.

Ý tưởng là tính tổng sai số dự đoán mà chúng ta gọi là phần thưởng nội tại, với

phần thưởng bên ngoài và sử dụng tổng số đó làm tín hiệu phần thưởng mới cho môi trường.

Giờ đây, tác nhân được khuyến khích không chỉ tìm ra cách tối đa hóa phần thưởng môi trường,

mà còn tò mò về môi trường.

Lỗi dự đoán được tính toán như trong Hình 8.4.

Hình 8.4, mô-đun dự đoán có trạng thái, ST viết hoa, hành động A, T và

T không được hiển thị và đưa ra dự đoán cho trạng thái tiếp theo, viết hoa S hat T plus

1, trong đó biểu tượng chiếc mũ gợi ý một giá trị gần đúng.

Dự đoán này, cùng với trạng thái thực tiếp theo, được chuyển tới hàm sai số bình phương trung bình,

hoặc một số hàm lỗi khác tạo ra lỗi dự đoán.

Phần thưởng nội tại dựa trên lỗi dự đoán của các trạng thái trong môi trường.

Điều này hoạt động khá tốt ở lần đầu tiên, nhưng cuối cùng mọi người nhận ra rằng nó chạy

sang một vấn đề khác, thường được gọi là vấn đề nhiễu TV, Hình 8.5.

Hóa ra là nếu bạn huấn luyện những đặc vụ này trong một môi trường có nguồn không đổi

về tính ngẫu nhiên, chẳng hạn như màn hình TV phát tiếng ồn ngẫu nhiên, tác nhân sẽ liên tục có

lỗi dự đoán cao và sẽ không thể giảm được.

Nó chỉ nhìn chằm chằm vào chiếc TV ồn ào vô thời hạn, vì nó rất khó đoán, và do đó

cung cấp một nguồn phần thưởng nội tại liên tục.

Đây không chỉ là một vấn đề học thuật vì nhiều môi trường trong thế giới thực có những vấn đề tương tự.

nguồn gốc của sự ngẫu nhiên, ví dụ, lá cây xào xạc trong gió.

Hình 8.5.

Vấn đề nhiễu TV là một vấn đề lý thuyết và thực tiễn trong đó tác nhân học tăng cường

với một cảm giác tò mò ngây thơ sẽ bị mê hoặc bởi một chiếc TV ồn ào, mãi mãi nhìn chằm chằm vào

nó.

Điều này là do về bản chất nó được khen thưởng bởi tính không thể đoán trước và tiếng ồn trắng rất

không thể đoán trước được.

Tại thời điểm này, có vẻ như lỗi dự đoán có rất nhiều tiềm năng, nhưng vấn đề TV ồn ào

là một thiếu sót lớn.

Có lẽ chúng ta không nên chú ý đến lỗi dự đoán tuyệt đối mà thay vào đó là tỷ lệ

về sự thay đổi của sai số dự đoán.

Khi tác nhân chuyển sang trạng thái không thể đoán trước, nó sẽ trải qua một sự đột biến nhất thời

về lỗi dự đoán, nhưng sau đó nó biến mất.

Tương tự, nếu đặc vụ gặp phải một chiếc TV ồn ào, lúc đầu nó rất khó dự đoán và

do đó có lỗi dự đoán cao, nhưng lỗi dự đoán cao vẫn được duy trì,

nên tốc độ thay đổi bằng không.

Công thức này tốt hơn, nhưng nó vẫn có một số vấn đề tiềm ẩn.

Hãy tưởng tượng rằng một đặc vụ đang ở bên ngoài và nhìn thấy một cái cây có lá bay trong gió.

Những chiếc lá bị thổi bay xung quanh một cách ngẫu nhiên nên đây là một lỗi dự đoán cao.

Gió ngừng thổi và lỗi dự đoán giảm đi vì những chiếc lá không chuyển động

nữa.

Khi gió bắt đầu thổi trở lại và lỗi dự đoán tăng lên, trong trường hợp này, ngay cả khi chúng ta

sử dụng tỷ lệ sai số dự đoán, tỷ lệ này sẽ dao động theo gió.

Chúng ta cần thứ gì đó mạnh mẽ hơn.

Chúng tôi muốn sử dụng ý tưởng về lỗi dự đoán này, nhưng chúng tôi không muốn nó dễ bị ảnh hưởng bởi những lỗi nhỏ.

tính ngẫu nhiên hoặc không thể đoán trước trong môi trường không thành vấn đề.

Làm cách nào để thêm ràng buộc không quan trọng vào mô-đun lỗi dự đoán?

Chà, khi chúng ta nói điều gì đó không quan trọng, chúng ta muốn nói rằng nó không ảnh hưởng đến chúng ta,

hoặc có lẽ là không thể kiểm soát được.

Nếu lá bị gió thổi ngẫu nhiên, hành động của tác nhân không ảnh hưởng đến lá,

và những chiếc lá không ảnh hưởng đến hành động của tác nhân.

Hóa ra chúng ta có thể triển khai ý tưởng này như một mô-đun riêng biệt, bên cạnh trạng thái

mô-đun dự đoán

Đó là chủ đề của chương này.

Chương này dựa trên việc làm sáng tỏ và triển khai ý tưởng từ một bài báo của Deepak Pathak, có tựa đề

Khám phá theo hướng tò mò bằng dự đoán tự giám sát, 2017, đã giải quyết thành công

những vấn đề chúng ta đang thảo luận.

Chúng tôi sẽ theo dõi bài viết này khá chặt chẽ vì đây là một trong những đóng góp lớn nhất

để giải quyết vấn đề Phần thưởng thưa thớt, và bài báo này đã dẫn đến một loạt các nghiên cứu liên quan.

Hóa ra nó cũng mô tả một trong những thuật toán dễ thực hiện nhất, trong số rất nhiều thuật toán.

những người khác trong lĩnh vực này.

Ngoài ra, một trong những mục tiêu của cuốn sách này không chỉ là dạy cho bạn những kiến thức cơ bản

kiến thức và kỹ năng học tập tăng cường mà còn cung cấp cho bạn kiến thức toán học đủ vững chắc

nền tảng để có thể đọc và hiểu các tài liệu học tập tăng cường và thực hiện

chúng theo cách riêng của bạn.

Tất nhiên, một số bài viết yêu cầu toán học nâng cao và chúng nằm ngoài phạm vi của cuốn sách này.

Nhưng nhiều bài báo lớn nhất trong lĩnh vực này chỉ yêu cầu một số phép tính, đại số và

đại số tuyến tính.

Những điều mà bạn có thể biết nếu bạn đã tiến xa đến mức này.

Rào cản thực sự duy nhất là vượt qua được ký hiệu toán học mà chúng tôi hy vọng có thể thực hiện được.

dễ dàng hơn ở đây.

Chúng tôi muốn dạy bạn cách câu cá thay vì chỉ đưa cá cho bạn, như người ta thường nói.