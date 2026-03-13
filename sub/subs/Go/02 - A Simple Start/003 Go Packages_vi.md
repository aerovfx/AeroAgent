# 003 Gói đi vi

---

Cuối cùng, trong video, chúng tôi đã tìm cách chạy mã trong dự án của mình.

Bây giờ chúng ta sẽ chuyển sang tìm hiểu chính xác dòng mã đầu tiên bên trong tệp chính của chúng ta có nghĩa

là gì.

Cụ thể là dòng cho gói chính được biết.

Trước tiên hãy nói về gói từ Vâng và chúng tôi sẽ nói về lý do tại sao chúng tôi sử dụng từ chính ngay tại đây.

Được rồi.

Please to get a sơ đồ.

Chúng ta bắt đầu.

Vì vậy, khi bạn nhìn thấy gói từ và đi, bạn có thể nghĩ rằng một gói có thể giống như một dự án hoặc một công việc không gian.

Một gói là một tập hợp các nguồn mã hóa.

Vì vậy, nếu bạn và tôi đang làm việc trên một ứng dụng rời rạc, giống như chúng ta đang làm việc trên một ứng dụng

sử dụng ngay bây giờ, theo hệ thống truyền tải, chúng tôi sẽ tạo ra một gói duy nhất.

Vì vậy, một gói có thể chứa nhiều tệp liên kết bên trong nó, mỗi tệp được kết thúc bằng tệp mở rộng là GO.

Yêu cầu duy nhất đối với mọi tệp trong một gói là dòng đầu tiên của mỗi tệp phải khai báo

gói tin báo nó không thuộc về.

Vì vậy, ví dụ: if ba tệp ngay tại đây đều thuộc về gói chính thì mỗi tệp

cần có gói lệnh chính ở trên cùng, giống như tệp chính hiện tại của chúng ta ngay tại đây.

Vì vậy, nếu chúng tôi có hai tệp khác trong dự án này hoặc bên trong gói này, chúng tôi cũng

sẽ cần phải khai báo gói chính ở cùng.

Bây giờ, tôi muốn cho bạn biết một chút về lý do chính xác tại sao chúng tôi gọi gói của mình là chính.

Tại sao chúng tôi gọi nó là Main?

Tại sao chúng tôi không gọi nó là Hello World để đặt tên cho thư mục mà nó thuộc về?

Vâng, bên trong go, có hai loại gói khác nhau.

Có một loại thực thi và một loại tái sử dụng.

Loại gói thực thi này là loại gói khi được biên dịch sẽ tạo ra tệp tệp có thể chạy hoặc thực thi tệp,

Tương tự như những gì chúng tôi đã thấy khi thực hiện lệnh go build tại dòng lệnh của mình.

Hãy nhớ rằng khi chúng tôi tiến hành xây dựng chính sách, hãy thực hiện ngay tại đó.

Nó được đưa ra tệp chính ngay tại đây, sau đó chúng tôi có thể chạy và thực hiện việc này.

Vì vậy, tệp này ngay tại đây đã được tạo đặc biệt bởi vì chúng tôi đã tạo một loại gói thực thi.

Các gói thực thi thường được sử dụng để thực hiện một điều gì đó và chủ yếu là những gì họ

ta sẽ làm trong khóa học này.

Chúng tôi sẽ viết các chương trình mà chúng tôi có thể chạy và chúng tôi có thể sử dụng chúng để hoàn thành nhiệm vụ.

Chúng tôi cũng có quyền truy cập vào các gói có thể tái sử dụng và bạn có thể coi những gói này giống như phụ

thuộc tính hoặc thư viện.

Đây là những gói không được sử dụng để tăng tốc và thực thi.

Thay vào đó, chúng tôi đưa ra rất nhiều logic hoặc chức năng trợ giúp có thể sử dụng lại hoặc những thứ thứ hai sẽ chỉ giúp chúng tôi sử dụng lại một

mã số cho các dự án tương lai trong tương lai.

Vì vậy, bạn có thể tò mò bằng cách nào đó để biết chúng tôi đang tạo một gói thực thi hay một gói có thể tái sử dụng

sử dụng?

Vậy làm cách nào để biết khi nào chúng ta đang làm cái này hay cái kia?

Nếu bạn xem nguồn mã hóa của chúng tôi, rõ ràng là không có gì thực sự ở đây nói rằng, Ồ đúng

sau đó, hãy tìm một số tệp thực thi khi bạn biên dịch cho tôi.

Vậy làm cách nào để biết khi nào chúng ta đang làm cái này hay cái kia?

Chà, nó thực sự phức tạp.

Hãy nhớ rằng chúng tôi đã gọi gói của mình với tên là Main.

Vì vậy, dòng đầu tiên chúng tôi chọn trong tệp của chúng tôi cho biết Gói chính.

Trên thực tế, tên của gói mà bạn sử dụng sẽ xác định xem bạn đang tạo một loại gói

phụ thuộc hay thực thi.

Vì vậy, cụ thể, từ main được sử dụng để tạo một kiểu thực thi gói.

Vì vậy, chúng tôi đã lấy gói chính, chúng tôi chạy xây dựng nó và tạo ra một tệp có tên là Chính hoặc Chính.

Nếu bạn đang sử dụng windows, nếu chúng tôi đã sử dụng bất kỳ tên nào khác cho gói của mình ngoài Main thì như vậy

Nếu chúng tôi gọi nó là gói, blah blah và sau đó chạy bản dựng, nó sẽ không tạo ra tệp thực thi thực sự.

Vì vậy, từ gói chính là linh thiêng.

Đó là cái mà chúng tôi chỉ sử dụng khi chúng tôi đang tạo một gói mà chúng tôi muốn tạo ra một số lý do hợp lý.

Trong suốt phần còn lại của khóa học này, bạn và tôi sẽ thực hiện các dự án chủ yếu sử dụng Tên Gói

Main bởi vì chúng tôi luôn muốn tạo ra thứ gì đó mà chúng tôi có thể chạy và

thử nghiệm lập tức.

Tuy nhiên, nếu chúng tôi đang cố gắng tạo ra một số mã thư viện có thể sử dụng lại hoặc nếu chúng tôi muốn tạo một số dự án mà chúng tôi có

có thể chia sẻ với bạn bè của mình để họ có thể sử dụng mã của họ trong dự án riêng của họ, đó

là lúc chúng tôi bắt đầu sử dụng một gói chuyên biệt hơn Tên.

Tóm lại, về cơ sở bất cứ khi nào chúng ta nhìn thấy từ gói chính, điều đó có nghĩa là chúng ta đang tạo một

gói thực thi.

Bất kỳ tên nào khác có nghĩa là chúng tôi đang tạo một loại gói phụ thuộc hoặc có thể tái sử dụng.

Bây giờ, điều cuối cùng tôi muốn nói với bạn về điều cuối cùng này là bất cứ điều gì khi chúng ta tạo ra một

gói thực thi, nó phải luôn có một chức năng bên trong nó được gọi là Main.

Vì vậy, nếu chúng tôi tự mình chỉnh sửa lại mã, thì đó là lệnh này.

Chúng tôi đã nói chức năng chính.

Vì vậy, chúng tôi đặc biệt tạo một hàm có tên Main vì chúng tôi đã gọi gói main tại đây, tạo ra một hàm.

Gói thực thi.

Bây giờ, để cung cấp cho bạn một bản demo nhanh chóng về điều này, tôi sẽ đi đến đầu dòng mã

lần đầu tiên ở đây và tôi sẽ đổi tên gói của mình thành Apple.

Bây giờ tôi sẽ quay lại thiết bị đầu cuối của tôi.

Nếu tôi liệt kê tất cả các tệp và thư mục của mình, bạn sẽ thấy rằng tôi vẫn còn tệp thực thi chính ngay tại đây, bởi vì

vậy tôi sẽ xóa nó nhanh chóng.

Bây giờ tôi chỉ quay lại mục chính nếu tôi xây dựng tệp này ngay bây giờ với một gói tên khác và sau đó liệt kê tất cả các tệp và

thư mục của mình, bạn sẽ thấy rằng tôi không thể nhận được một thực tế thứ cấp ở đây.

Vì vậy, rõ ràng tên của gói không quan trọng.

Bây giờ tôi sẽ thay đổi nó để trả lại gói tên của main như.

Vì vậy, tôi sẽ quay lại, xây dựng lại dự án của mình và bây giờ tôi thấy rằng tôi đã thực hiện điều này ở đây một lần nữa.

Vì vậy, tôi nghĩ rằng hiện tại có thể đã đủ cho các gói.

Một lần nữa, chúng tôi sẽ nhận được nhiều trải nghiệm hơn các gói trong tương lai.

Vì vậy, ngay bây giờ, chúng tôi chỉ tập trung vào câu hỏi tiếp theo của chúng tôi, nơi chúng tôi muốn tìm ra dòng chính xác

mã tiếp theo có nghĩa là gì.

Vì vậy, chúng tôi giải nén nhanh và bắt đầu nói về lệnh nhập trong phần tiếp theo.