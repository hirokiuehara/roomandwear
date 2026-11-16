# 差し替え用の画像一覧

画像を用意したら、下の「保存先」にそのファイル名で置き、`python3 _source/build3.py` を実行して `dist/` を作り直します（または編集担当に依頼）。
記事画像は `_source/assets/photos/<スラッグ>.jpg` を置くと、自動でイラストの代わりに使われます（置かない記事はイラストのまま）。

## 共通ルール
- 形式：JPEG（品質80前後）。1枚あたり200KB以下を目安に圧縮
- 文字は画像に入れない（タイトルなどはサイト側で表示します）
- 色味：木目・チャコール・オリーブ・生成り。カテゴリー画像と同じ明るさ・質感
- 生成画像は雰囲気づくり用に限る。実在の商品と誤認させる画像（ロゴ入り、特定商品に似せた画像）は使わない
- 実商品の画像は、利用許諾のある画像のみ（Amazonの商品画像は、Creators API等の正式な方法で取得できるまで使用しない）
- 人物を入れる場合は顔を写さないか、利用許諾のある写真に限る

## サイト共通
| 用途 | 推奨サイズ | 保存先 | 現在 |
|---|---|---|---|
| メインビジュアル（PC） | 1983×793px以上（横長 約2.5:1） | `_source/assets/hero.jpg` | 支給画像 |
| メインビジュアル（スマホ） | 1000×400px前後（右寄りに被写体） | `_source/assets/hero-sm.jpg` | 支給画像を縮小 |
| カテゴリー「服を選ぶ」 | 1600×800px（2:1）＋スマホ用800×400px。被写体は右半分、左側は文字を重ねる無地の壁 | `_source/assets/cat-apparel.jpg` / `cat-apparel-sm.jpg` | 支給画像（2026年11月17日差し替え済み） |
| カテゴリー「部屋を整える」 | 同上 | `_source/assets/cat-interior.jpg` / `cat-interior-sm.jpg` | 支給画像（2026年11月17日差し替え済み） |

カテゴリー画像はカテゴリー専用です。記事のアイキャッチには使いません。

## 記事のアイキャッチ（推奨 1200×630px・1.91:1、文字なし）
一覧カードでは中央を基準に少し切り取られることがあるため、被写体は中央寄りに置き、上下左右に余白を残してください。上から優先度の高い順です。

| 優先 | 記事（URL） | 保存先 | 希望する構図 |
|---|---|---|---|
| 1 | 一人暮らしのソファの選び方（sofa-guide.html） | `_source/assets/photos/sofa-guide.jpg` | 6畳ほどの部屋の壁ぎわに置いた2人掛けの布張りソファ。正面やや斜めから、手前に床を広めに残して部屋の広さが分かる構図 |
| 2 | 間接照明で部屋の雰囲気を変える（indirect-lighting.html） | `_source/assets/photos/indirect-lighting.jpg` | 夜の部屋で、フロアライトが壁と天井を照らしている様子。照明器具は小さめに写し、光の広がりを主役にする |
| 3 | ローテーブルの選び方（low-table.html） | `_source/assets/photos/low-table.jpg` | ソファの前に置いた木のローテーブル。斜め上から、ソファとの距離（すき間）が分かる構図 |
| 4 | 在宅ワークがはかどる（desk-setup.html） | `_source/assets/photos/desk-setup.jpg` | 壁向きのデスクにノートPCとモニターライト。斜め後ろから、ケーブルが見えないすっきりした机上 |
| 5 | 服選びで失敗しない（basic-5-items.html） | `_source/assets/photos/basic-5-items.jpg` | 白T・シャツ・デニム・スラックス・ジャケットを木の床に平置き（真上から）。ロゴやタグは写さない |
| 6 | スニーカーは1足目に何を選ぶ？（first-sneakers.html） | `_source/assets/photos/first-sneakers.jpg` | 白と黒のローカットスニーカーを1足ずつ、玄関の床に並べた横からの構図。ブランドロゴが分からない角度 |
| 7 | 一人暮らし1Kのレイアウト（1k-layout.html） | `_source/assets/photos/1k-layout.jpg` | 入口側から窓に向かって部屋全体を写す。低い家具と、入口から窓までの通り道が分かる構図 |
| 8 | 冬アウターの選び方（winter-outer-guide.html） | `_source/assets/photos/winter-outer-guide.jpg` | ハンガーラックに掛けたダウン・ウールコート・中綿ジャケットの3着。素材の違いが分かる寄りの構図 |
| 9 | 白Tシャツの選び方（white-tee-guide.html） | `_source/assets/photos/white-tee-guide.jpg` | 畳んだ白Tシャツを2〜3枚重ね、首元のリブが見えるように斜め上から |
| 10 | お気に入りの服を長持ちさせる（clothes-care.html） | `_source/assets/photos/clothes-care.jpg` | 洗濯ネットに入れたニットと、木のハンガーに掛けたシャツ。明るい洗面所や室内干しの雰囲気 |
| 11 | 寝具を見直そう（bedding-guide.html） | `_source/assets/photos/bedding-guide.jpg` | グレー系のカバーでそろえたベッド。枕とマットレスの厚みが分かる横からの構図 |
| 12 | 狭い部屋の収納術（small-room-storage.html） | `_source/assets/photos/small-room-storage.jpg` | 同じ形の収納ボックスを並べた棚と、上に少しだけ飾った本と小さな植物 |
| 13 | ニットの選び方（knit-guide.html） | `_source/assets/photos/knit-guide.jpg` | 質感の違うニット（ウール・コットン）を2〜3枚畳んで重ね、編み目が分かる寄りの構図 |
| 14 | チノパンの選び方（chino-pants.html） | `_source/assets/photos/chino-pants.jpg` | ベージュとネイビーのチノパンを畳んで並べ、横に白スニーカー。真上から |
| 15 | 大人が着るパーカーの選び方（hoodie-guide.html） | `_source/assets/photos/hoodie-guide.jpg` | 杢グレーの無地パーカーをハンガーに掛け、横にチェスターコート。ロゴは写さない |
| 16 | シャツのサイズの選び方（shirt-size.html） | `_source/assets/photos/shirt-size.jpg` | 平置きした白いシャツの肩・身幅にメジャーを当てている手元。真上から |
| 17 | ワイドパンツの合わせ方（wide-pants.html） | `_source/assets/photos/wide-pants.jpg` | ワイドパンツとコンパクトなトップスを着た人の首から下（顔は写さない）、または平置きのコーディネート |
| 18 | 初めての革靴の選び方（first-leather-shoes.html） | `_source/assets/photos/first-leather-shoes.jpg` | 黒のストレートチップを横から。手前に靴磨きのブラシとクロス |
| 19 | 通勤バッグの選び方（commute-bag.html） | `_source/assets/photos/commute-bag.jpg` | 黒いリュック・トート・ショルダーを床に並べた構図。ロゴが分からない角度 |
| 20 | 腕時計の選び方（wristwatch-guide.html） | `_source/assets/photos/wristwatch-guide.jpg` | シンプルな3針の腕時計を木のトレーに置いた寄りの構図。ブランド名が読めないぼかし |
| 21 | 冬の機能性インナーの選び方（thermal-innerwear.html） | `_source/assets/photos/thermal-innerwear.jpg` | 畳んだインナーとウールの靴下を並べ、横にニット。冬らしい暖色の光 |
| 22 | キャップ・帽子の選び方（cap-guide.html） | `_source/assets/photos/cap-guide.jpg` | 無地のキャップとニット帽を壁のフックに掛けた構図 |
| 23 | カーテンの選び方（curtain-guide.html） | `_source/assets/photos/curtain-guide.jpg` | グレーの厚手カーテンとレースカーテンが掛かった窓。昼の柔らかい光 |
| 24 | ラグの選び方（rug-guide.html） | `_source/assets/photos/rug-guide.jpg` | ローテーブルの下に敷いたグレー系のラグ。テーブルの周りに30cmほどラグがはみ出している構図 |
| 25 | 初心者でも育てやすい観葉植物（houseplants.html） | `_source/assets/photos/houseplants.jpg` | レースカーテン越しの光の中、棚の上に置いたポトスと床置きの鉢 |
| 26 | クローゼット収納のコツ（closet-storage.html） | `_source/assets/photos/closet-storage.jpg` | 同じハンガーでそろえた服と、下段の引き出しケース。扉を開けた正面からの構図 |
| 27 | 一人暮らしの小さなキッチン収納術（kitchen-storage.html） | `_source/assets/photos/kitchen-storage.jpg` | 黒で統一した水切りラックとレンジ上ラックのある小さなキッチン |
| 28 | 加湿器の選び方（humidifier-guide.html） | `_source/assets/photos/humidifier-guide.jpg` | 窓ぎわではなく部屋の中央寄りに置いた白い加湿器と、横に温湿度計 |
| 29 | 賃貸でもできる壁の飾り方（wall-decor.html） | `_source/assets/photos/wall-decor.jpg` | 白い壁に細い黒フレームのポスターと小さな飾り棚。正面から |
| 30 | 玄関をすっきり整える（entrance-tidy.html） | `_source/assets/photos/entrance-tidy.jpg` | 床に靴が出ていない狭い玄関。ドアに付けたキーフックが小さく写る構図 |
