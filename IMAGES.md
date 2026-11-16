# 差し替え用の画像一覧

画像を用意したら、下の「保存先」にそのファイル名で置き、`python3 _source/build3.py` で再生成します（または編集担当に依頼）。
記事画像は `_source/assets/photos/<スラッグ>.jpg` を置くと、自動でイラストの代わりに使われます（置かない記事はイラストのまま）。

## 共通ルール
- 形式：JPEG（品質80前後）。1枚あたり200KB以下を目安に圧縮
- 色味：木目・チャコール・オリーブ・生成り。メインビジュアル（hero.jpg）と同じ明るさ・質感
- 生成画像は雰囲気づくり用に限る。実在の商品と誤認させる画像（ロゴ入り、特定商品に似せた画像）は使わない
- 実商品の画像は、利用許諾のある画像のみ（Amazonの商品画像は、Creators API等の正式な方法で取得できるまで使用しない）

## サイト共通
| 用途 | 推奨サイズ | 保存先 | 現在 |
|---|---|---|---|
| メインビジュアル（PC） | 1983×793px以上（横長 約2.5:1） | `_source/assets/hero.jpg` | 支給画像 |
| メインビジュアル（スマホ） | 1000×400px前後（右寄りに被写体） | `_source/assets/hero-sm.jpg` | 支給画像を縮小 |
| カテゴリー「服を選ぶ」 | 1600×1000px（16:10）、シャツ・ニット・パンツの組み合わせ | `_source/assets/cat-apparel.jpg` | メインビジュアルの切り抜き（暫定） |
| カテゴリー「部屋を整える」 | 1600×1000px（16:10）、ソファ・照明・テーブルのある部屋 | `_source/assets/cat-interior.jpg` | メインビジュアルの切り抜き（暫定） |

## 記事のアイキャッチ（推奨 1200×630px・1.91:1、文字なし）
上から優先度の高い順です。

| 優先 | 記事 | 保存先 | 写真のイメージ |
|---|---|---|---|
| 1 | 一人暮らしのソファの選び方（sofa-guide.html） | `_source/assets/photos/sofa-guide.jpg` | 一人暮らしの部屋に置いた2人掛けソファ |
| 2 | 間接照明で部屋の雰囲気を変える（indirect-lighting.html） | `_source/assets/photos/indirect-lighting.jpg` | 夜の部屋で壁を照らすフロアライト |
| 3 | ローテーブルの選び方（low-table.html） | `_source/assets/photos/low-table.jpg` | ソファ前のローテーブル |
| 4 | 在宅ワークがはかどる（desk-setup.html） | `_source/assets/photos/desk-setup.jpg` | 整ったデスクとノートPC |
| 5 | 服選びで失敗しない（basic-5-items.html） | `_source/assets/photos/basic-5-items.jpg` | 白T・シャツ・デニム・スラックス・ジャケットを並べた写真 |
| 6 | スニーカーは1足目に何を選ぶ？色・形・素材の基本（first-sneakers.html） | `_source/assets/photos/first-sneakers.jpg` | 白と黒のローカットスニーカー（ブランドロゴが見えないもの） |
| 7 | 一人暮らし1Kのレイアウト（1k-layout.html） | `_source/assets/photos/1k-layout.jpg` | 1Kの部屋全体 |
| 8 | 冬アウターの選び方（winter-outer-guide.html） | `_source/assets/photos/winter-outer-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 9 | 白Tシャツの選び方（white-tee-guide.html） | `_source/assets/photos/white-tee-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 10 | お気に入りの服を長持ちさせる（clothes-care.html） | `_source/assets/photos/clothes-care.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 11 | 寝具を見直そう（bedding-guide.html） | `_source/assets/photos/bedding-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 12 | 狭い部屋の収納術（small-room-storage.html） | `_source/assets/photos/small-room-storage.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 13 | ニットの選び方（knit-guide.html） | `_source/assets/photos/knit-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 14 | チノパンの選び方（chino-pants.html） | `_source/assets/photos/chino-pants.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 15 | 大人が着るパーカーの選び方（hoodie-guide.html） | `_source/assets/photos/hoodie-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 16 | シャツのサイズの選び方（shirt-size.html） | `_source/assets/photos/shirt-size.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 17 | ワイドパンツの合わせ方（wide-pants.html） | `_source/assets/photos/wide-pants.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 18 | 初めての革靴の選び方（first-leather-shoes.html） | `_source/assets/photos/first-leather-shoes.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 19 | 通勤バッグの選び方（commute-bag.html） | `_source/assets/photos/commute-bag.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 20 | 腕時計の選び方（wristwatch-guide.html） | `_source/assets/photos/wristwatch-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 21 | 冬の機能性インナーの選び方（thermal-innerwear.html） | `_source/assets/photos/thermal-innerwear.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 22 | キャップ・帽子の選び方（cap-guide.html） | `_source/assets/photos/cap-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 23 | カーテンの選び方（curtain-guide.html） | `_source/assets/photos/curtain-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 24 | ラグの選び方（rug-guide.html） | `_source/assets/photos/rug-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 25 | 初心者でも育てやすい観葉植物と、置き場所・水やりの基本（houseplants.html） | `_source/assets/photos/houseplants.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 26 | クローゼット収納のコツ（closet-storage.html） | `_source/assets/photos/closet-storage.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 27 | 一人暮らしの小さなキッチン収納術（kitchen-storage.html） | `_source/assets/photos/kitchen-storage.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 28 | 加湿器の選び方（humidifier-guide.html） | `_source/assets/photos/humidifier-guide.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 29 | 賃貸でもできる壁の飾り方（wall-decor.html） | `_source/assets/photos/wall-decor.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
| 30 | 玄関をすっきり整える（entrance-tidy.html） | `_source/assets/photos/entrance-tidy.jpg` | 記事テーマに合う、メインビジュアルと同じトーンの写真 |
