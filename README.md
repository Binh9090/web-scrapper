# Web Scraping Demo

## Giới thiệu  
Dự án này là một script Python đơn giản dùng để thu thập dữ liệu từ trang web [Quotes to Scrape](https://quotes.toscrape.com/). Script sẽ lấy danh sách các câu trích dẫn (quotes) và tác giả từ trang web.

## Yêu cầu  
- Python 3.x  
- Các thư viện cần cài đặt:
  - `requests`: Gửi yêu cầu HTTP  
  - `beautifulsoup4`: Phân tích và trích xuất dữ liệu từ HTML  

Cài đặt các thư viện bằng lệnh:
```bash
pip install requests beautifulsoup4
```

## Cách sử dụng  
1. Clone repository:  
   ```bash
   git clone https://github.com/Binh9090/web-scrapper.git
   cd web-scrapper
   ```

2. Chạy script:
   ```bash
   python scraper.py
   ```

3. Kết quả sẽ hiển thị các câu quote và tác giả trong terminal.

## Ghi chú  
Trang web [Quotes to Scrape](https://quotes.toscrape.com/) được thiết kế để phục vụ cho mục đích học tập, vì vậy việc thu thập dữ liệu từ đây hoàn toàn hợp pháp.
