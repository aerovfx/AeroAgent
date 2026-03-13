# 07 - Thiết lập MCP OAuth trên Cloudflare

---

- Bây giờ chúng ta cần lấy đơn này

và đưa nó lên web.

Và đây là nơi mọi thứ thay đổi

bởi vì bạn không thể lưu chìa khóa, ID và mọi thứ

trong dự án và sau đó chỉ cần đẩy chúng.

Thay vào đó, bạn phải tạo bí mật

được lưu trữ trên Cloudflare,

mà không ai có thể nhìn thấy,

được Cloudflare sử dụng để có quyền truy cập vào GitHub.

Đây là cách thực hiện điều đó.

Đầu tiên, thoát khỏi quá trình chạy cục bộ.

Tôi sẽ chỉ gõ rõ ràng để xóa mọi thứ.

Tiếp theo, bạn cần thiết lập phím

cho ứng dụng này trên Cloudflare.

Bạn có thể làm điều đó theo hai cách:

Bạn có thể bắt đầu bằng cách tạo các phím

và gửi chúng tới Cloudflare,

rồi triển khai ứng dụng sau đó.

Hoặc bạn có thể triển khai ứng dụng mà không cần chìa khóa,

và sau đó gửi chìa khóa vào.

Bạn kết thúc với điều tương tự.

Tuy nhiên, trong mẫu mà Cloudflare cung cấp,

đã có một bộ khóa mặc định được thiết lập trong một tệp,

và nếu bạn không lấy chìa khóa đó ra,

những phím đó sẽ ghi đè bất kỳ phím nào bạn đặt vào hệ thống.

Đây, tôi sẽ chỉ cho bạn.

Vì vậy, trong ví dụ remote-mcp-github-oauth,

có một tệp tên là wrangler.json,

và ngay trên đầu này,

bạn có dev.vars.

Vì vậy đây là những dev.vars đang được sử dụng.

Nhưng thiết lập này ở đây,

với GITHUB_CLIENT, GITHUB_CLIENT_SECRET,

và COOKIE_ENCRIPTION_KEY,

sẽ ghi đè bất cứ điều gì bạn làm với những bí mật thực tế.

Vì vậy, để sử dụng điều này trong sản xuất,

bạn cần phải lấy phần này ra.

Tôi đã làm điều đó trong ví dụ ở đây.

Vì vậy, trong wrangler.json,

thay vì có phần đó,

Thay vào đó, tôi đã thêm những gì bạn cần làm.

Vì vậy, ở đây chúng ta có npx wrangler

để thiết lập ID bí mật của khách hàng, bí mật của khách hàng,

và bí mật cũng như khóa mã hóa cookie.

Vì vậy, ở đây chúng ta có npx wrangler chọn bí mật.

Vì vậy, ở đây chúng ta có bí mật npx wrangler đặt GITHUB_CLIENT_ID,

GITHUB_CLIENT_SECRETS và COOKIE_ENCRIPTION_KEY.

Vì vậy, hãy để tôi làm điều này theo cách đưa chìa khóa vào trước

và sau đó xuất bản mọi thứ.

Vì vậy, chúng ta sẽ bắt đầu bằng cách nhập lệnh này vào đây.

bí mật wrangler npx đặt GITHUB_CLIENT_ID.

Tôi sẽ chạy nó.

Sau đó tôi cần giá trị bí mật.

Đó là,

đó là giá trị tôi có cho ứng dụng từ xa.

Vì vậy, đó sẽ là giá trị mà tôi đã tạo ra ở đây.

Vì vậy tôi sẽ lấy ID bí mật ở đây.

Và dán nó vào.

Chạy cái đó.

Sau đó nó nói, "Hình như không có công nhân nào

được gọi là máy chủ thời tiết. Bạn có muốn triển khai không?

Bạn có muốn tạo một công nhân mới không?"

Vì vậy tôi sẽ nói có.

Điều đó tạo ra một công nhân mới.

Sau đó chúng ta sẽ làm điều tương tự,

ngoại trừ việc thay vào đó chúng tôi sẽ lấy bí mật của khách hàng.

Quay lại đi.

Sao chép bí mật đó.

Dán vào.

Và cuối cùng, tôi sẽ thiết lập khóa mã hóa.

Chỉ cần sao chép cái này.

Và khóa mã hóa có thể là bất cứ thứ gì.

Tôi sẽ nghiền nát một đống thứ.

Bây giờ chúng ta đã tạo xong công nhân.

Bước tiếp theo là tạo ra,

cái được gọi là cửa hàng KV.

Đó là kho lưu trữ khóa-giá trị mà hệ thống sẽ sử dụng.

Vì vậy, bên trong wrangler ở đây, bạn sẽ thấy ở dưới đây chúng ta có

giá trị OAUTH_KV này mà chúng ta cần tạo.

Nếu bạn vào README,

và cuộn xuống,

đây là mã cho điều đó.

Vì vậy, bạn có thể nói npx wrangler kv tạo không gian tên.

Vì vậy, chúng tôi sẽ đưa nó vào.

Điều này sẽ tạo ra một không gian tên mới.

Chúng tôi nhận được ID ở đây.

ID đó sẽ được đưa vào wrangler ở đây dưới OAUTH_KV.

Điều này đảm bảo hệ thống có thể theo dõi

bất kỳ cặp khóa-giá trị nào đang được truyền vào và ra

khi chúng tôi đang thực hiện vòng lặp OAuth.