import requests   # Dùng để gửi yêu cầu HTTP
from bs4 import BeautifulSoup  # Dùng để phân tích và trích xuất dữ liệu từ HTML

# URL của trang web cần thu thập
url = "https://quotes.toscrape.com/"

# Gửi yêu cầu tới trang web và nhận phản hồi
response = requests.get(url)  # Lấy dữ liệu HTML từ trang web
html_content = response.text  # Nội dung HTML của trang

# Phân tích dữ liệu HTML bằng BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")  # Chuyển HTML thành cấu trúc dễ xử lý

# Tìm tất cả các câu quote trong HTML
quotes = soup.find_all("span", class_="text")  # Tìm các thẻ <span> có class là "text"

# Tìm tất cả các tác giả
authors = soup.find_all("small", class_="author")  # Tìm các thẻ <small> có class là "author"

# Duyệt qua từng câu quote và tác giả để in ra
for quote, author in zip(quotes, authors):  # Ghép từng câu quote với tác giả tương ứng
    print(f"{quote.text} - {author.text}")  # In kết quả: Câu nói - Tác giả
