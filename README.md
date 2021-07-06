# facebook-crawler

透過讀取mail清單檔案, 擷取mail @前面的名字去搜尋該facebook的 個人資料,彙整成csv輸出.

## Install

`pip install facebook-scraper`

## Usage

準備輸入檔案 mail 清單

`aaa@gmail.com
bbb@gmail.com
ccc@gmail.com`

準備Facebook cookies, 可以安裝Chrome 插件 [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en)

將cookies 輸出至cookies.json

最後直接執行

`python3 main.py`

Outputs:

csv file

| id   | mail          | FB                           | 名稱 | 大頭貼           | 教育     | 現居   | 性別 | 生日     | 感情狀態 |
| ---- | ------------- | ---------------------------- | ---- | ---------------- | -------- | ------ | ---- | -------- | -------- |
| 123  | aaa@gmail.com | https://www.facebook.com/aaa | Aaa  | https://xxxx.jpg | colleage | Taiwan | Male | Birthday | Married  |

