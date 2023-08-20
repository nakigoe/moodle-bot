<kbd style="width: 2em; height: 2em;"><a href="#en">ENGLISH</a></kbd> | <kbd><a href="#ru">РУССКИЙ</a></kbd> | <kbd>[日本語](#ja)</kbd>

<h1 name="en" id="en">Moodle: Mass-Send A Message to Everyone in Your School</h1>

<b>The current version is written for a very specific school in mind. You might need to adapt the code and the urls to target Your school. You definetely need to have Your active Moodle username and password.</b>

## How To Use

### Change:

  •  Your Moodle login `username`
  
  •  Your Moodle password `password`
  
  •  Your message inside `moodle-message.txt` file
  
  •  The link to Your Moodle login page `login_page`
  
  •  The link to a user Moodle page `base_url` (leave the place after `=` empty), the code runs through all the database up to the number manually specified in `users_in_moodle`
  
  •  The number of `users_in_moodle` 
  
  You have to try it out manually in the `base_url` in any browser and see, what is the maximum user ID in your school Moodle database.
  
  •  You might need to change some selectors in the `send.py` inside the `main()` and `send_a_message()` FUNCTIONS, since it could very well be Your customized school Moodle.
    
### Install Python:

  •  https://www.python.org/downloads/

### Install PIP If it Has Not been Installed With Python Automatically:

  •  https://pip.pypa.io/en/stable/installation/

### Install Libraries (please open the command line interface):

  •  Selenium `pip install selenium`

### Send a connection request and a message to them All!

  •  double-click on `start.bat`

<hr>

<p style="margin: 0 auto" align="center">© <a href="https://nakigoe.org" target="_blank">NAKIGOE.ORG</a></p> 

<p style="margin: 0 auto" align="center">All rights reserved and no permissions are granted.</p>

<p style="margin: 0 auto" align="center">Please add stars the repositories!</p>

<hr>

<h1 name="ja" id="ja">Moodle：友達の友達と自動的につながる</h1>

<b>友達を選び、彼または彼女のすべてのコネクションに、個人名を含めたカスタマイズメッセージで友達リクエストを自動送信します。</b>

## ご利用方法

### 変更:

  •  Moodle のログイン `username` を入力してください

  •  Moodle のパスワード `password` を入力してください

  •  `moodle-message.txt` ファイル内のメッセージを入力してください

  •  Moodle のログインページへのリンク `login_page` を入力してください

  •  Moodle のユーザーページへのリンク `base_url` を入力してください（ = の後の部分は空白にしてください）、コードはデータベース全体を `users_in_moodle` まで実行します

  •  `users_in_moodle` の数を入力してください

  学校の Moodle データベースで最大のユーザーIDが何であるかを確認するため、 `base_url` と開いたブラウザで手動で試す必要があります。

  •  あなたのカスタマイズされた学校の Moodle である可能性があるため、 `send.py` 内の `main()` および `send_a_message()` 関数の中でいくつかのセレクターを変更する必要があるかもしれません。

このツールは、Moodle システムの全体的な大学または学校への一括送信を自動化します。 `send.py` はアプリケーションファイルで、 `main()` はコードの反復を開始する関数で、 `send_a_message()` はメッセージを送信する関数です。

何か他にお手伝いできることがあれば、お知らせください！
  
### Python をインストールなさってください：

  •  https://www.python.org/downloads/

### PIP が Python とともに自動的にインストールされていない場合は、PIP をインストールします:

  •  https://pip.pypa.io/en/stable/installation/

### Python ライブラリをインストールなさってください (コマンド プロンプトを開いてください)：

  •  Selenium `pip install selenium`

### すべての方々へ友達リクエストとメッセージをお送りくださいませ！

  •  `start.bat` をダブルクリックをなさってください。

<hr>

<p style="margin: 0 auto" align="center">© <a href="https://nakigoe.org/ja" target="_blank">NAKIGOE.ORG</a></p> 

<p style="margin: 0 auto" align="center">全ての権利を保有し、許可は一切与えられません。</p>

<p style="margin: 0 auto" align="center">リポジトリに星を付けてください！</p>

<hr>

<h1 name="ru" id="ru">Moodle: массовая отправка сообщений студентам и работникам школы / академии / ВУЗа</h1>

<b>Данный код написан имея в виду конкретный ВУЗ. Для использования ПО для Вашей школы, скорее всего, потребуется внести изменения в код и селекторы. Наличие актуального логина и пароля к Вашему Moodle обязательно.</b>

## Инструкция

### Замените:

  •  имя пользователя `username`
  
  •  пароль `password`

  •  Ваше сообщение внутри файла `moodle-message.txt`
  
  •  сноску на страницу входа в Ваш Moodle `login_page`
  
  •  сноску на страницу пользователя Moodle `base_url` (оставьте место после `=` пустым), ПО перебирает ID всех пользователей с 0 до `users_in_moodle`
  
  •  число пользователей в Вашем Moodle `users_in_moodle` 
  
  Вам необходимо подставлять вручную числа в `base_url` и смотреть, какой ID пользователя является максимальным в базе данных Moodle Вашего учебного заведения.
  
  •  вероятно, потребуется заменить код и селекторы файла `send.py` внутри ФУНКЦИЙ `main()` и `send_a_message()`, так как, скорее всего, Moodle Вашего учебного заведения кастомизирован.
   
### Установите Python:

  •  https://www.python.org/downloads/

### Установите PIP, если он не установился с Python автоматически:

  •  https://pip.pypa.io/en/stable/installation/

### Установите библиотеки (откройте командную строку):

  •  Selenium `pip install selenium`
  
### Запускайте, приглашение в контакты и сообщение — каждому!

  •  двойной щелчок мыши по `start.bat`

<hr>

<p style="margin: 0 auto" align="center">© <a href="https://nakigoe.org/ru" target="_blank">NAKIGOE.ORG</a></p> 

<p style="margin: 0 auto" align="center">Все права сохраняются и никаких разрешений не предоставляется.</p>

<p style="margin: 0 auto" align="center">Ставьте звёзды на репозитории!</p>

<hr>

<br>
<p style="margin: 0 auto" align="center">Please cast an eye on my website:</p>
<h1><a href="https://nakigoe.org/" style="background-color: black;" target="_blank">
  <img style="display: block; width: calc(100vw - (100vw - 100%));"
    src="https://nakigoe.org/_IMG/logo.png" 
    srcset="https://nakigoe.org/_IMG/logo.png 4800w,
      https://nakigoe.org/_SRC/logo-3840.png 3840w,
      https://nakigoe.org/_SRC/logo-2560.png 2560w,
      https://nakigoe.org/_SRC/logo-2400.png 2400w,
      https://nakigoe.org/_SRC/logo-2048.png 2048w,
      https://nakigoe.org/_SRC/logo-1920.png 1920w,
      https://nakigoe.org/_SRC/logo-1600.png 1600w,
      https://nakigoe.org/_SRC/logo-1440.png 1440w,
      https://nakigoe.org/_SRC/logo-1280.png 1280w,
      https://nakigoe.org/_SRC/logo-1200.png 1200w,
      https://nakigoe.org/_SRC/logo-1080.png 1080w,
      https://nakigoe.org/_SRC/logo-960.png 960w,
      https://nakigoe.org/_SRC/logo-720.png 720w,
      https://nakigoe.org/_SRC/logo-600.png 600w,
      https://nakigoe.org/_SRC/logo-480.png 480w,
      https://nakigoe.org/_SRC/logo-300.png 300w"
    alt="NAKIGOE.ORG">
<img class="blend" style="display: block; width: calc(100vw - (100vw - 100%));" 
  src="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg" 
  srcset="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg 2800w,
    https://nakigoe.org/_SRC/nakigoe-academy-night-2048.jpg 2048w"
  alt="Nakigoe Academy">
  <img class="blend" style="display: block; width: calc(100vw - (100vw - 100%)); padding-bottom: 0.05em;"
    src="https://nakigoe.org/_IMG/logo-hot-bevel.png" 
    srcset="https://nakigoe.org/_IMG/logo-hot-bevel.jpg 4800w,
      https://nakigoe.org/_SRC/logo-hot-bevel-3840.jpg 3840w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2560.jpg 2560w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2400.jpg 2400w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2048.jpg 2048w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1920.jpg 1920w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1600.jpg 1600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1440.jpg 1440w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1280.jpg 1280w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1200.jpg 1200w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1080.jpg 1080w,
      https://nakigoe.org/_SRC/logo-hot-bevel-960.jpg 960w,
      https://nakigoe.org/_SRC/logo-hot-bevel-720.jpg 720w,
      https://nakigoe.org/_SRC/logo-hot-bevel-600.jpg 600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-480.jpg 480w,
      https://nakigoe.org/_SRC/logo-hot-bevel-300.jpg 300w"
    alt="NAKIGOE.ORG">
</a></h1>

<p style="margin: 0 auto" align="center">© NAKIGOE.ORG</p> 

<p style="margin: 0 auto" align="center">All rights reserved and no permissions are granted.</p>

<p style="margin: 0 auto" align="center">Please add stars to the repositories!</p>
