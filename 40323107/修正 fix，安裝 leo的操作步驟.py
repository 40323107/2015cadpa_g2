任務：修正 fix，安裝 leo。<br />

步驟：<br />

1.開啟課程網頁。( 網址：http://wordpress-2015course.rhcloud.com/ )<br />
2.點選2015Fall課程。( 網址：http://wordpress-2015course.rhcloud.com/?page_id=3633 )<br />
3.點選遠端 copy 下載 fix 。( copy.com 網址： https://copy.com/zpYyuIcuB3fHAdr0 (fix.zip) )<br />
4.將 fix 檔案解壓縮，並儲存在 C 槽。<br />
5.使用 Google 瀏覽器 搜尋 leo editor github。<br />
6.點選 leo editor github 進入網頁。( 網址：https://github.com/leo-editor )<br />
7.點選 leo-editor 。( 網址：https://github.com/leo-editor/leo-editor )<br />
8.點選 releases 。 ( 網址：https://github.com/leo-editor/leo-editor/releases )<br />
9.點選 broke-abbrev 。( 網址：https://github.com/leo-editor/leo-editor/releases/tag/broke-abbrev )<br />
10.點選 Source code(zip) 。( 下載檔案，檔名為 leo-editor-broke-abbrev.zip )<br />
11.將 leo-editor-broke-abbrev.zip 檔案移至 fix 資料夾。<br />
12.到 Ana3_lite2\data\SciTE 搜尋 SciTE.exe ( 應用程式 )。<br />
13.開啟 SciTE.exe 。<br />
14.使用 SciTE.exe 編輯器 開啟 fix.bat 。<br />
15.在最後新增一行指令，指令為 copy leo-editor-broke-abbrev.zip C:\Ana3_2015\data\ 。<br />
16.儲存檔案。<br />
17.再使用 SciTE.exe 編輯器 開啟 start.bat 。<br />
18.將原指令 (第35行) pip install http://140.130.17.17/public/leo-editor-master.zip  更改為 pip install leo-editor-broke-abbrev.zip 。 <br />
19.再將原指令 (第30行) cd notebook  更改為 cd tmp 。( 意為：啟動 Jupyter 將自動讀取 tmp 資料夾裡的資訊。 ) <br />
20.儲存檔案。<br />
21.點選開啟 fix.bat 。<br />
22.再點選開啟 start.bat 。<br />
23.成功開啟 leo 。<br />
