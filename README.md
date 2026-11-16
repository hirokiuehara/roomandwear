# ROOM & WEAR

20代・30代メンズ向けの、服と部屋の選び方メディア。公開URL: https://roomandwear.vercel.app/

- ルート直下：公開中のサイト（静的HTML）。`_source/build3.py` が生成した `dist/` と同じ内容
- `_source/`：サイトを生成するスクリプトと素材（`python3 _source/build3.py` で `dist/` に出力）
  - 商品紹介のデータ：`_source/products.py`・`_source/products2.py`（ASIN・仕様・確認日）
- `IMAGES.md`：差し替え用の画像一覧（記事名・希望する構図・推奨サイズ・保存先）

## 公開方法
公開はVercel Drop（Vercelのプロジェクト画面へのドラッグ＆ドロップ）で行っています。このリポジトリはVercelと連携していないため、GitHubへの反映で自動デプロイは起きません。

Vercelに渡すのは `dist/`（＝サイトのファイル86点）だけにしてください。リポジトリのフォルダや `_source/`、zipファイルをそのまま落とすと、スクリプトやzipも公開対象になります。
Vercel Dropが `.vercelignore` を読むかは公式ドキュメントに記載がないため、除外は `.vercelignore` に頼らず「公開するフォルダを分ける」方法で行っています。

APIキーなどの秘密情報はコミットしないでください。
