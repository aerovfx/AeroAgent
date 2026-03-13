# Chương 10. Đào tạo và trực quan hóa sự chú ý Học tăng cường sâu trong hành động, Phiên bản video đã được dịch

---

Phần 10.6, đào tạo và hình dung sự chú ý.

Hiện tại chúng ta đã có hầu hết các phần nhưng chúng ta cần một số chức năng trợ giúp khác trước khi đào tạo.

Liệt kê 10.8, các hàm tiền xử lý.

Các hàm này chỉ chuẩn bị tensor quan sát trạng thái, tạo ra một lô nhỏ và tính giá trị Q mục tiêu như chúng ta đã thảo luận trước đó.

Trong Liệt kê 10.9, chúng ta xác định hàm mất mát mà chúng ta sẽ sử dụng và cũng là hàm để cập nhật tính năng phát lại trải nghiệm.

Liệt kê 10.9, hàm mất và cập nhật phát lại.

Chức năng phát lại gạch dưới cập nhật sẽ thêm những kỷ niệm mới vào trải nghiệm phát lại nếu nó chưa đầy.

Nếu đầy, nó sẽ thay thế những ký ức ngẫu nhiên bằng những ký ức mới.

Nếu ký ức dẫn đến phần thưởng tích cực, chúng tôi sẽ thêm 50 bản sao của ký ức đó vì ký ức về phần thưởng tích cực rất hiếm và chúng tôi muốn làm phong phú thêm trải nghiệm phát lại bằng những ký ức quan trọng hơn này.

Tất cả các môi trường lưới điện mini đều có bảy hành động, nhưng trong môi trường chúng ta sẽ sử dụng trong chương này, chúng ta chỉ cần sử dụng năm trong số bảy hành động.

Vì vậy, chúng tôi sử dụng từ điển để dịch từ đầu ra của DQN, sẽ tạo ra các hành động từ 0 đến 4, sang các hành động thích hợp trong môi trường, là tập hợp chứa các phần tử 0, 1, 2, 3 và 5.

Tên hành động của lưới nhỏ và số hành động tương ứng được liệt kê ở đây.

Xem mã này.

Trong Liệt kê 10.10, chúng ta chuyển sang vòng huấn luyện chính của thuật toán.

Liệt kê 10.10, vòng lặp đào tạo chính.

Thuật toán học tăng cường DQN kép tự chú ý của chúng tôi sẽ học cách chơi khá tốt sau khoảng 10.000 kỷ nguyên, nhưng có thể mất tới 50.000 kỷ nguyên trước khi đạt được độ chính xác tối đa.

Hình 10.22 cho thấy biểu đồ log-loss mà chúng tôi nhận được và chúng tôi cũng biểu thị độ dài trung bình của tập phim.

Khi tác nhân học cách chơi, nó sẽ có thể giải quyết trò chơi với ngày càng ít bước hơn.

Hình 10.22, biểu đồ log-loss cao nhất trong quá trình huấn luyện.

Sự mất mát giảm xuống nhanh chóng lúc đầu, tăng lên một chút, và sau đó bắt đầu giảm rất chậm.

Dưới cùng, độ dài tập trung bình. Điều này cho chúng tôi ý tưởng tốt hơn về hiệu suất của tác nhân vì chúng tôi có thể thấy rõ rằng nó đang giải quyết các tập phim với số bước ngắn hơn trong quá trình đào tạo.

Nếu bạn kiểm tra thuật toán đã huấn luyện, thuật toán đó sẽ có thể giải được lớn hơn hoặc bằng 94% số tập trong giới hạn bước tối đa.

Chúng tôi thậm chí còn ghi lại các khung hình video trong quá trình đào tạo và nhân viên biết rõ ràng nó đang làm gì khi bạn xem nó trong thời gian thực.

Chúng tôi đã bỏ qua rất nhiều mã phụ kiện này để giữ cho văn bản rõ ràng. Vui lòng xem kho GitHub để biết mã hoàn chỉnh.

Mục 10.6.1, học entropy tối đa.

Chúng tôi đang sử dụng chính sách tham lam của Epsilon với Epsilon được đặt thành 0,5, do đó, tác nhân thực hiện các hành động ngẫu nhiên trong 50% thời gian.

Chúng tôi đã thử nghiệm bằng nhiều cấp độ Epsilon khác nhau nhưng nhận thấy 0,5 là mức tốt nhất.

Nếu bạn đào tạo tác nhân với các giá trị Epsilon nằm trong khoảng từ mức thấp 0,01 đến 0,1 đến 0,2 cho đến mức cao nhất là 0,95, bạn sẽ nhận thấy hiệu suất đào tạo tuân theo đường cong chữ U ngược, trong đó 2 giá trị thấp đối với Epsilon dẫn đến học tập kém do thiếu khám phá và 2 giá trị cao đối với Epsilon dẫn đến học tập kém do thiếu khai thác.

Làm thế nào tác nhân có thể hoạt động tốt như vậy mặc dù nó chỉ hoạt động ngẫu nhiên trong một nửa thời gian?

Bằng cách đặt Epsilon ở mức cao nhất có thể cho đến khi nó làm giảm hiệu suất, chúng tôi đang sử dụng một phép tính gần đúng với nguyên tắc entropy tối đa hoặc học entropy tối đa.

Chúng ta có thể coi entropy trong chính sách của tác nhân là mức độ ngẫu nhiên mà nó thể hiện và hóa ra việc tối đa hóa entropy cho đến khi nó bắt đầu phản tác dụng thực sự dẫn đến hiệu suất và tính khái quát hóa tốt hơn.

Nếu một tác nhân có thể đạt được mục tiêu thành công ngay cả khi thực hiện tỷ lệ hành động ngẫu nhiên cao, thì tác nhân đó phải có chính sách rất mạnh mẽ, không nhạy cảm với các biến đổi ngẫu nhiên, do đó, tác nhân đó sẽ có thể xử lý các môi trường khó khăn hơn.

Phần 10.6.2, Chương trình giảng dạy

Chúng tôi chỉ đào tạo đặc vụ này trên phiên bản 5x5 của môi trường thế giới lưới này để nó có một cơ hội nhỏ đạt được mục tiêu một cách ngẫu nhiên và nhận được phần thưởng.

Ngoài ra còn có các môi trường lớn hơn, bao gồm môi trường 16x16, điều này khiến việc giành chiến thắng ngẫu nhiên là cực kỳ khó xảy ra.

Một giải pháp thay thế hoặc bổ sung cho Học tập tò mò là sử dụng một quy trình có tên là Học chương trình giảng dạy, đó là khi chúng tôi đào tạo nhân viên về một biến thể dễ của một vấn đề, sau đó đào tạo lại một biến thể khó hơn một chút và tiếp tục đào tạo lại các phiên bản ngày càng khó hơn của vấn đề cho đến khi nhân viên có thể hoàn thành thành công một nhiệm vụ mà lẽ ra quá khó để bắt đầu.

Chúng ta có thể cố gắng giải lưới 16x16 mà không cần tò mò bằng cách huấn luyện trước tiên để đạt độ chính xác tối đa trên lưới 5x5, sau đó huấn luyện lại trên lưới 6x6, sau đó là lưới 8x8 và cuối cùng là lưới 16x16.

Phần 10.6.3, Hình dung các bước chú ý

Chúng tôi biết rằng chúng tôi có thể huấn luyện thành công một DQN quan hệ trong nhiệm vụ thế giới lưới có phần khó khăn này, nhưng chúng tôi có thể sử dụng một DQN ít ưa thích hơn nhiều để làm điều tương tự.

Tuy nhiên, chúng tôi cũng quan tâm đến việc trực quan hóa trọng số sự chú ý để biết chính xác nhân viên đã học được cách tập trung vào điều gì khi chơi trò chơi.

Một số kết quả thật đáng ngạc nhiên, và một số kết quả là những gì chúng ta mong đợi.

Để trực quan hóa các trọng số chú ý, chúng tôi đã yêu cầu mô hình của mình lưu một bản sao của các trọng số chú ý mỗi khi nó được chạy về phía trước và chúng tôi có thể truy cập nó bằng cách gọi GWagent.atUnderscoreMap, hàm này trả về một lô theo chiều cao theo chiều rộng tensor.

Tất cả những gì chúng ta cần làm là chạy mô hình chuyển tiếp ở một trạng thái nào đó, chọn đầu chú ý và chọn một nút để trực quan hóa, sau đó định hình lại tensor thành lưới 7x7 và vẽ đồ thị bằng plt.imShow.

Xem mã này.

Chúng tôi quyết định xem xét trọng số chú ý của nút khóa, nút cửa và nút tác nhân để xem đối tượng nào có liên quan với nhau.

Chúng tôi đã tìm thấy nút trong trọng số chú ý tương ứng với nút trong lưới bằng cách đếm các ô lưới, vì cả trọng số chú ý và trạng thái ban đầu đều là lưới 7x7.

Chúng tôi đã cố tình thiết kế mô-đun quan hệ sao cho trạng thái ban đầu và ma trận trọng số chú ý có cùng chiều.

Nếu không, việc ánh xạ trọng số chú ý vào trạng thái sẽ trở nên khó khăn.

Hình 10.23 hiển thị chế độ xem đầy đủ ban đầu của lưới ở trạng thái ban đầu ngẫu nhiên và trạng thái chuẩn bị tương ứng.

Hình 10.23 bên trái, quan sát đầy đủ môi trường.

Đúng, chế độ xem trạng thái một phần tương ứng mà tác nhân có quyền truy cập.

Chế độ xem một phần lúc đầu hơi khó hiểu vì đây là chế độ xem ích kỷ, vì vậy chúng tôi đã chú thích nó bằng vị trí của tác nhân A, Key, K và cánh cửa D.

Vì chế độ xem một phần của tổng đài viên luôn là 7x7 và kích thước của toàn bộ lưới chỉ là 5x5 nên chế độ xem một phần luôn bao gồm một số khoảng trống.

Bây giờ, hãy hình dung trọng số chú ý tương ứng cho trạng thái này.

Trong Hình 10.24, mỗi cột được gắn nhãn là trọng số chú ý của một nút cụ thể, đó là các nút mà nó đang chú ý.

Việc giới hạn bản thân chỉ ở các nút tác nhân, Khóa và cửa trong tổng số 7x7 bằng 49 nút.

Mỗi hàng là một đầu chú ý, từ đầu 1 đến đầu 3 từ trên xuống dưới.

Thật kỳ lạ, sự chú ý ở đầu 1 dường như không tập trung vào bất cứ điều gì rõ ràng là thú vị.

Trên thực tế, nó đang tập trung vào các ô lưới trong không gian trống.

Lưu ý rằng mặc dù chúng tôi chỉ xem xét 3 trong số 49 nút, ngay cả sau khi xem xét tất cả các nút, trọng số chú ý vẫn khá thưa thớt.

Nhiều nhất chỉ có một số ô lưới được gán bất kỳ sự chú ý đáng kể nào, nhưng có lẽ điều này không có gì đáng ngạc nhiên, vì các đầu chú ý dường như rất chuyên biệt.

Hình 10.24, mỗi hàng tương ứng với một đầu chú ý.

Ví dụ: hàng 1 tương ứng với đầu chú ý 1, cột bên trái.

Trọng số tự chú ý của tác nhân, cho thấy các đối tượng mà tác nhân chú ý nhất.

Cột ở giữa, trọng số tự chú ý cho phím, hiển thị các đối tượng mà phím chú ý nhiều nhất.

Cột bên phải, tự cân cho cửa.

Phần chú ý 1 có thể tập trung vào một tập hợp nhỏ các điểm mốc trong môi trường để hiểu rõ về vị trí và hướng.

Thực tế là nó có thể làm được điều này chỉ với một vài ô lưới là rất ấn tượng.

Chú ý đầu 2 và 3, hàng 2 và 3 và hình 10.24 thú vị hơn và đang tiến gần đến những gì chúng ta mong đợi.

Nhìn vào đầu chú ý 2 để biết nút tác nhân. Nó đang chú ý một cách mạnh mẽ đến chiếc chìa khóa và về cơ bản không có gì khác, đó chính xác là điều chúng ta hy vọng, vì ở trạng thái ban đầu này, công việc đầu tiên của nó là nhặt chiếc chìa khóa lên.

Ngược lại, chìa khóa đang phục vụ tác nhân, cho thấy có mối quan hệ hai chiều giữa tác nhân với chìa khóa và chìa khóa với tác nhân.

Cánh cửa cũng được người đại diện quan tâm nhiều nhất, nhưng cũng có một lượng nhỏ sự chú ý dành cho chìa khóa và không gian ngay trước cửa.

Đầu 3 chú ý dành cho đặc vụ đang chú ý đến một số ô lưới mốc, một lần nữa, có thể là để thiết lập cảm giác về vị trí và hướng.

Chú ý đầu 3 là chìa khóa đang canh cửa và cửa đang quan sát chìa khóa.

Tổng hợp tất cả lại, chúng ta nhận được rằng tác nhân có liên quan đến chìa khóa, liên quan đến cánh cửa.

Nếu khung thành được nhìn thấy, chúng ta có thể thấy rằng cánh cửa cũng liên quan đến khung thành.

Mặc dù đây là một môi trường đơn giản nhưng nó có cấu trúc quan hệ mà chúng ta có thể học bằng mạng lưới thần kinh quan hệ và chúng ta có thể kiểm tra các mối quan hệ mà nó học được.

Điều thú vị là sự chú ý được phân bổ thưa thớt như thế nào. Mỗi nút thích tham gia mạnh mẽ vào một nút khác, đôi khi có một vài nút khác mà nó tham gia yếu.

Vì đây là thế giới lưới nên dễ dàng phân chia trạng thái thành các đối tượng riêng biệt, nhưng trong nhiều trường hợp, chẳng hạn như trò chơi Atari, trạng thái là một mảng pixel RGB lớn và các đối tượng mà chúng ta muốn tập trung vào là tập hợp các pixel này.

Trong trường hợp này, việc ánh xạ trọng số chú ý trở lại các đối tượng cụ thể trong khung hình video trở nên khó khăn, nhưng chúng ta vẫn có thể xem phần nào của hình ảnh mà toàn bộ mô-đun quan hệ đang sử dụng để đưa ra quyết định.

Chúng tôi đã thử nghiệm kiến ​​trúc tương tự trên trò chơi Atari Alien, chúng tôi chỉ sử dụng cấu trúc hạt nhân 4x4 thay vì 1x1 và thêm một số lớp tổng hợp tối đa.

Và chúng ta có thể thấy trong hình 10.25 rằng nó thực sự học cách tập trung vào các đối tượng nổi bật trong khung hình video, mã không được hiển thị.

Hình 10.25, bên trái, trạng thái được xử lý trước dành cho DQN, khung video thô ở giữa, bên phải, bản đồ chú ý theo trạng thái.

Chúng ta có thể thấy rằng bản đồ chú ý tập trung vào người ngoài hành tinh ở giữa phía dưới màn hình, người chơi ở giữa và phần thưởng ở trên cùng, đây là những đối tượng nổi bật nhất trong trò chơi.

Các mô-đun quan hệ sử dụng cơ chế tự chú ý là những công cụ mạnh mẽ trong bộ công cụ học máy và chúng có thể rất hữu ích cho việc đào tạo các tác nhân RL khi chúng ta muốn biết một số ý tưởng về cách họ đưa ra quyết định.

Tự chú ý là một cơ chế để thực hiện truyền thông điệp trên biểu đồ, như chúng ta đã thảo luận, và đó là một phần của lĩnh vực rộng hơn về mạng lưới thần kinh đồ thị mà chúng tôi khuyến khích bạn khám phá thêm.

Có nhiều cách triển khai mạng thần kinh đồ thị, GNN, nhưng đặc biệt phù hợp với chúng ta sau chương này là mạng chú ý đồ thị, sử dụng cùng cơ chế tự chú ý mà chúng ta vừa triển khai, nhưng có thêm khả năng hoạt động trên dữ liệu có cấu trúc đồ thị tổng quát hơn.