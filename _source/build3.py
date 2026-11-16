# -*- coding: utf-8 -*-
import os, re, shutil, html, urllib.parse, sys
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES as A1
from articles2 import ARTICLES2
from eyecatch import svg as eyecatch_svg
import sofa_body
from products import PICKS, CHECKED

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dist")
SITE = "ROOM & WEAR"
TAGLINE = "20代・30代メンズのための、服と部屋を無理のない予算で整えるメディア"
OPERATOR = "ROOM & WEAR 編集部"
EMAIL = "hirokiuehara@gmail.com"
ASSOC_TAG = "roomandwear-22"
CATS = {"apparel": "服を選ぶ", "interior": "部屋を整える"}
CAT_SHORT = {"apparel": "アパレル", "interior": "インテリア"}

_ap = [a for a in ARTICLES2 if a['cat'] == 'apparel']; _in = [a for a in ARTICLES2 if a['cat'] == 'interior']
ARTICLES = A1 + [x for pair in zip(_ap, _in) for x in pair]
BY = {a["slug"]: a for a in ARTICLES}
# sofa article upgrade
BY["sofa-guide"]["body"] = sofa_body.BODY
BY["sofa-guide"]["items"] = []
BY["sofa-guide"]["title"] = "一人暮らしのソファの選び方。サイズ・素材・手入れで比べる"
BY["sofa-guide"]["desc"] = "置き場所の測り方、素材ごとの手入れのしやすさ、配置図、よくある失敗例、条件別のソファ3点まで。一人暮らしのソファ選びをまとめました。"

START = ["basic-5-items", "1k-layout", "indirect-lighting"]
FEATURES = [
 ("feature-clothes-basics", "服選びで失敗したくない", "何を買えばいいか迷ったときに、まず読んでほしい基本の記事をまとめました。定番アイテムの選び方とサイズの合わせ方から始めましょう。",
  ["basic-5-items", "shirt-size", "white-tee-guide", "chino-pants", "first-sneakers", "knit-guide", "wide-pants"]),
 ("feature-small-room", "狭い部屋をおしゃれにしたい", "1Kやワンルームでも、家具の選び方と配置で部屋は広く見せられます。レイアウト・家具・照明の記事をまとめました。",
  ["1k-layout", "sofa-guide", "low-table", "rug-guide", "curtain-guide", "indirect-lighting", "wall-decor"]),
 ("feature-storage", "収納をすっきりさせたい", "物が多くても、しまい方のルールを決めれば部屋は片付いて見えます。場所別の収納の記事をまとめました。",
  ["small-room-storage", "closet-storage", "kitchen-storage", "entrance-tidy", "clothes-care"]),
 ("feature-workspace", "自宅の仕事環境を整えたい", "在宅ワークや勉強がはかどるデスク周りの整え方と、作業しやすい照明や家具の記事をまとめました。",
  ["desk-setup", "indirect-lighting", "low-table", "commute-bag"]),
]
SAVE = [
 ("feature-basic-wardrobe", "最初にそろえたい基本の服", "たくさん買う前に、着回しの土台になる定番から。最初の数着を選ぶための記事をまとめました。",
  ["basic-5-items", "white-tee-guide", "shirt-size", "chino-pants", "first-sneakers", "thermal-innerwear"]),
 ("feature-rearrange", "買い替える前に見直したい部屋の配置", "家具を買い足す前に、配置・照明・色を見直すだけで部屋の印象は変わります。手持ちのもので試せる記事をまとめました。",
  ["1k-layout", "indirect-lighting", "rug-guide", "curtain-guide", "wall-decor", "small-room-storage"]),
 ("feature-minimal", "少ない家具ですっきり暮らす", "家具の数をしぼると、掃除も模様替えも楽になります。少ない家具で暮らすための選び方と収納の記事をまとめました。",
  ["1k-layout", "sofa-guide", "low-table", "small-room-storage", "closet-storage", "entrance-tidy"]),
 ("feature-long-lasting", "長く使えるものの選び方", "安さだけで選ばず、長く使えるものを選ぶと結果的に買い替えが減ります。素材や手入れの記事をまとめました。",
  ["clothes-care", "winter-outer-guide", "knit-guide", "first-leather-shoes", "wristwatch-guide", "bedding-guide"]),
]
ALLFEAT = FEATURES + SAVE

PHOTO_DIR = os.path.join(os.path.dirname(__file__), "assets", "photos")
def thumb_src(slug):
    return f"photo-{slug}.jpg" if os.path.exists(os.path.join(PHOTO_DIR, f"{slug}.jpg")) else f"img-{slug}.svg"

def render_picks(slug):
    p = PICKS[slug]
    head = "".join(f"<th>{c}</th>" for c in p["cols"])
    rows = "".join(f"<tr><th>{html.escape(it[1].split('（')[0])}</th>" + "".join(f"<td>{c}</td>" for c in it[7]) + "</tr>" for it in p["items"])
    cards = ""
    for label, name, asin, specs, feat, fit, caution, _ in p["items"]:
        dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in specs.items())
        cards += f"""<div class="product"><p class="product-label">{label}</p><h3>{html.escape(name)}</h3><dl>{dl}<dt>特徴</dt><dd>{feat}</dd><dt>向いている人</dt><dd>{fit}</dd><dt>注意点</dt><dd>{caution}</dd><dt>価格</dt><dd>価格・在庫は変動するため掲載していません（販売ページの確認日：{CHECKED}）。</dd></dl><a class="btn-amazon" href="https://www.amazon.co.jp/dp/{asin}?tag={ASSOC_TAG}" target="_blank" rel="nofollow sponsored noopener">Amazonで価格・詳細を見る</a></div>"""
    return f"""<h2>条件別に選んだ3点</h2>
<p>{p['intro']}{p.get('source', '仕様は'+CHECKED+'にAmazonの販売ページで確認した内容です。')}編集部が実際に使用したレビューではありません。購入前に最新の情報をご確認ください。</p>
<table><tr><th>商品</th>{head}</tr>{rows}</table>
{cards}
"""

def amazon_search(q):
    return "https://www.amazon.co.jp/s?k=" + urllib.parse.quote(q) + "&tag=" + ASSOC_TAG

def fmt_date(d):
    y, m, dd = d.split("-"); return f"{y}年{int(m)}月{int(dd)}日"

NAV = [("home", "index.html", "ホーム"), ("apparel", "apparel.html", "服を選ぶ"), ("interior", "interior.html", "部屋を整える"),
       ("features", "features.html", "悩みから探す"), ("articles", "articles.html", "記事一覧"), ("about", "about.html", "運営者情報")]

def page(title, desc, body, active=""):
    full = SITE if title == SITE else f"{title}｜{SITE}"
    nav = "".join(f'<a href="{h}"{" class=\"on\"" if k == active else ""}>{l}</a>' for k, h, l in NAV)
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<p class="pr-bar">当サイトはアフィリエイトプログラムを利用しています（<a href="disclosure.html">詳しく</a>）</p>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html">ROOM <span>&amp;</span> WEAR</a>
    <p class="tagline">{TAGLINE}</p>
    <nav class="gnav">{nav}</nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p class="flogo">ROOM <span>&amp;</span> WEAR</p>
    <nav class="fnav">
      <a href="apparel.html">服を選ぶ</a><a href="interior.html">部屋を整える</a><a href="features.html">悩みから探す</a><a href="articles.html">記事一覧</a>
    </nav>
    <nav class="fnav">
      <a href="about.html">運営者情報・編集方針</a><a href="privacy.html">プライバシーポリシー</a><a href="disclosure.html">広告・アフィリエイトについて</a><a href="contact.html">お問い合わせ</a>
    </nav>
    <p class="copy">&copy; 2026 {SITE}</p>
  </div>
</footer>
</body>
</html>
"""

def card(a):
    return f"""<a class="card" href="{a['slug']}.html">
  <div class="thumb"><img src="{thumb_src(a['slug'])}" alt="" loading="lazy" width="1200" height="630"><span class="chip chip-{a['cat']}">{CAT_SHORT[a['cat']]}</span></div>
  <div class="card-body">
    <h3>{html.escape(a['title'])}</h3>
    <p class="excerpt">{html.escape(a['desc'])}</p>
  </div>
</a>"""

def write(path, content):
    with open(os.path.join(OUT, path), "w", encoding="utf-8") as f: f.write(content)

def add_toc(body):
    heads = re.findall(r"<h2>(.*?)</h2>", body)
    for i, h in enumerate(heads):
        body = body.replace(f"<h2>{h}</h2>", f'<h2 id="s{i+1}">{h}</h2>', 1)
    body = re.sub(r"(?<!<div class=\"table-wrap\">\n)<table>", '<div class="table-wrap"><table>', body)
    body = re.sub(r"</table>(?!\n?</div>)", "</table></div>", body)
    toc = ""
    if len(heads) >= 4:
        toc = '<nav class="toc"><p class="toc-title">目次</p><ol>' + "".join(f'<li><a href="#s{i+1}">{re.sub("<.*?>","",h)}</a></li>' for i, h in enumerate(heads)) + "</ol></nav>"
    return body, toc

if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
A = os.path.join(os.path.dirname(__file__), "assets")
for f in ["style3.css", "hero.jpg", "hero-sm.jpg", "cat-apparel.jpg", "cat-interior.jpg", "cat-apparel-sm.jpg", "cat-interior-sm.jpg"]:
    shutil.copy(os.path.join(A, f) if os.path.exists(os.path.join(A, f)) else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f), os.path.join(OUT, "style.css" if f == "style3.css" else f))

if os.path.isdir(PHOTO_DIR):
    for f in os.listdir(PHOTO_DIR):
        if f.endswith(".jpg"): shutil.copy(os.path.join(PHOTO_DIR, f), os.path.join(OUT, "photo-" + f))
arts = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)

# ---------- HOME ----------
def fcards(lst):
    return "".join(f"""<a class="feature" href="{fid}.html"><span class="feature-q">{t}</span><span class="feature-n">{len(sl)}本の記事 →</span></a>""" for fid, t, _, sl in lst)
feat_cards = fcards(FEATURES)
save_cards = fcards(SAVE)
home = f"""
<section class="hero hero-photo">
  <picture class="hero-bg"><source media="(max-width:640px)" srcset="hero-sm.jpg"><img src="hero.jpg" alt="ソファとハンガーラックのある落ち着いた部屋" width="1983" height="793" fetchpriority="high"></picture>
  <div class="hero-text">
  <p class="hero-en">STYLE FOR YOUR ROOM &amp; WARDROBE</p>
  <h1>服と部屋を、<br>ちょうどいい感じに。</h1>
  <p>流行を追いかけすぎず、長く使えるものを。20代・30代の男性に向けて、無理のない予算で服と部屋を整えるための「選び方」をまとめています。</p>
  </div>
</section>

<section class="cat-banners">
  <a class="cat-banner" href="apparel.html"><img src="cat-apparel.jpg" srcset="cat-apparel-sm.jpg 800w, cat-apparel.jpg 1600w" sizes="(max-width:640px) 100vw, 50vw" alt="ハンガーラックに掛かったシャツとジャケット、木の台に畳んだニット・パンツとスニーカー" loading="lazy" width="1600" height="800"><div class="cat-text"><span class="cat-en">APPAREL</span><strong>服を選ぶ</strong><span class="cat-sub"><span>定番アイテムの選び方・</span><span>サイズ・手入れ</span></span></div></a>
  <a class="cat-banner cat-interior" href="interior.html"><img src="cat-interior.jpg" srcset="cat-interior-sm.jpg 800w, cat-interior.jpg 1600w" sizes="(max-width:640px) 100vw, 50vw" alt="木のアームチェアとフロアランプ、丸いサイドテーブルがある部屋" loading="lazy" width="1600" height="800"><div class="cat-text"><span class="cat-en">INTERIOR</span><strong>部屋を整える</strong><span class="cat-sub"><span>家具・照明・</span><span>収納・レイアウト</span></span></div></a>
</section>

<section class="block">
  <h2 class="sec-title">まずはここから</h2>
  <p class="sec-lead">はじめての方に読んでほしい3本です。</p>
  <div class="grid grid-3">{''.join(card(BY[s]) for s in START)}</div>
</section>

<section class="block">
  <h2 class="sec-title">悩みから探す</h2>
  <div class="features">{feat_cards}</div>
</section>

<section class="block">
  <h2 class="sec-title">無駄な買い物を減らす</h2>
  <p class="sec-lead">買い足す前に読んでおきたい記事をテーマ別にまとめました。</p>
  <div class="features">{save_cards}</div>
</section>

<section class="block">
  <h2 class="sec-title">新着記事</h2>
  <div class="grid grid-3">{''.join(card(a) for a in arts[:9])}</div>
  <p class="more"><a class="btn-more" href="articles.html">記事一覧を見る（全{len(arts)}本）</a></p>
</section>

<section class="block policy">
  <h2 class="sec-title">ROOM &amp; WEARの編集方針</h2>
  <ul>
    <li>流行よりも、長く使えて手持ちと合わせやすいものを優先して紹介します。</li>
    <li>商品のサイズや仕様は、メーカーや販売ページの記載を確認したうえで掲載します。分からない情報は推測で書きません。</li>
    <li>実際に使っていない商品について、使用レビューや体験談は書きません。</li>
    <li>記事にはアフィリエイトリンクを含みますが、紹介料の有無で評価を変えることはありません。</li>
  </ul>
  <p><a href="about.html#policy">選定基準と情報の確認方法を詳しく見る →</a></p>
</section>
"""
write("index.html", page(SITE, TAGLINE + "。アパレルとインテリアの選び方をわかりやすく紹介します。", home, "home"))

# ---------- CATEGORY ----------
leads = {"apparel": "毎日着る服の選び方、サイズの合わせ方、長く着るための手入れを紹介します。", "interior": "一人暮らしの部屋を快適に、すっきり見せるための家具・照明・収納・レイアウトを紹介します。"}
for key in CATS:
    lst = [a for a in arts if a["cat"] == key]
    body = f"""<section class="cat-head cat-head-{key}"><img src="cat-{key}.jpg" srcset="cat-{key}-sm.jpg 800w, cat-{key}.jpg 1600w" sizes="100vw" alt="" width="1600" height="800"><div class="cat-text"><span class="cat-en">{'APPAREL' if key=='apparel' else 'INTERIOR'}</span><h1>{CATS[key]}</h1><p>{leads[key]}</p></div></section>
<p class="count">{len(lst)}本の記事</p>
<div class="grid grid-3">{''.join(card(a) for a in lst)}</div>"""
    write(f"{key}.html", page(CATS[key], f"{CATS[key]}の記事一覧", body, key))

# ---------- ALL ARTICLES ----------
def list_items(lst):
    return "".join(f'<li><a href="{a["slug"]}.html">{html.escape(a["title"])}</a></li>' for a in lst)
body = f"""<h1 class="page-title">記事一覧</h1><p class="lead">全{len(arts)}本の記事をカテゴリー別に掲載しています。</p>
<div class="list-cols">
<section><h2 class="sec-title">服を選ぶ</h2><ul class="article-list">{list_items([a for a in arts if a['cat']=='apparel'])}</ul></section>
<section><h2 class="sec-title">部屋を整える</h2><ul class="article-list">{list_items([a for a in arts if a['cat']=='interior'])}</ul></section>
</div>"""
write("articles.html", page("記事一覧", "ROOM & WEARの全記事一覧", body, "articles"))

# ---------- FEATURES ----------
body = '<h1 class="page-title">悩みから探す</h1><p class="lead">いまの悩みに近いテーマから、関連する記事をまとめて読めます。</p><div class="features">' + feat_cards + '</div><h2 class="sec-title" style="margin-top:40px">無駄な買い物を減らす</h2><p class="sec-lead">買い足す前に読んでおきたい記事をテーマ別にまとめました。</p><div class="features">' + save_cards + "</div>"
write("features.html", page("悩みから探す", "悩み別の特集一覧", body, "features"))
for fid, t, lead, sl in ALLFEAT:
    body = f'<p class="crumb"><a href="index.html">ホーム</a> › <a href="features.html">悩みから探す</a></p><h1 class="page-title">{t}</h1><p class="lead">{lead}</p><div class="grid grid-3">{"".join(card(BY[s]) for s in sl)}</div><p class="more"><a class="btn-more" href="features.html">ほかの悩みから探す</a></p>'
    write(f"{fid}.html", page(t, lead, body, "features"))

# ---------- ARTICLES ----------
for a in ARTICLES:
    write(f"img-{a['slug']}.svg", eyecatch_svg(a, CAT_SHORT[a['cat']]))
    src = a["body"]
    if a["slug"] in PICKS:
        i = src.find("<h2>まとめ")
        src = (src[:i] + render_picks(a["slug"]) + src[i:]) if i >= 0 else src + render_picks(a["slug"])
    b, toc = add_toc(src)
    if a["slug"] == "sofa-guide":
        # insert toc after summary box
        b = b.replace("</div>\n\n<p>ソファがあると", "</div>\n" + toc + "\n<p>ソファがあると", 1); toc_top = ""
    else:
        toc_top = toc
    items = ""
    if a["items"]:
        lis = "".join(f'<li><span class="item-name">{html.escape(n)}</span><a class="btn-search" href="{amazon_search(q)}" target="_blank" rel="nofollow sponsored noopener">Amazonで商品を探す</a></li>' for n, q in a["items"])
        items = f"""<section class="items"><h2>この記事に関連するアイテムを探す</h2><p class="small">Amazonの検索結果ページに移動します。条件に合う商品を比較してお選びください。</p><ul>{lis}</ul><p class="small">価格・在庫・仕様は変わることがあります。購入前にAmazonの商品ページで最新の情報をご確認ください。</p></section>"""
    same = [x for x in arts if x["cat"] == a["cat"] and x["slug"] != a["slug"]]
    if a["slug"] == "sofa-guide":
        same = [BY[s] for s in ["1k-layout", "low-table", "rug-guide"]]
    related = same[:3]
    feats = [(fid, t) for fid, t, _, sl in ALLFEAT if a["slug"] in sl]
    featlinks = "".join(f'<a class="tag" href="{fid}.html">{t}</a>' for fid, t in feats)
    body = f"""
<article class="article">
  <p class="crumb"><a href="index.html">ホーム</a> › <a href="{a['cat']}.html">{CATS[a['cat']]}</a></p>
  <p class="meta"><span class="chip chip-{a['cat']}">{CAT_SHORT[a['cat']]}</span>{fmt_date(a['date'])}</p>
  <h1>{html.escape(a['title'])}</h1>
  <figure class="eyecatch-fig"><img class="eyecatch" src="{thumb_src(a['slug'])}" alt="" width="1200" height="630">{'<figcaption>※画像は記事のイメージです。紹介している商品の写真ではありません。</figcaption>' if thumb_src(a['slug']).startswith('photo-') else ''}</figure>
  <p class="pr-note">※この記事にはアフィリエイトリンクが含まれています（<a href="disclosure.html">広告について</a>）。</p>
  {toc_top}
  <div class="content">{b}</div>
  {items}
  {f'<div class="tags"><span>この記事が含まれる特集：</span>{featlinks}</div>' if featlinks else ''}
</article>
<section class="block"><h2 class="sec-title">あわせて読みたい</h2><div class="grid grid-3">{''.join(card(x) for x in related)}</div><p class="more"><a class="btn-more" href="articles.html">記事一覧を見る</a></p></section>
"""
    write(f"{a['slug']}.html", page(a["title"], a["desc"], body, a["cat"]))

# ---------- STATIC ----------
about = f"""<article class="article static">
<h1>運営者情報・編集方針</h1>
<div class="table-wrap"><table>
<tr><th>サイト名</th><td>{SITE}</td></tr>
<tr><th>運営者</th><td>{OPERATOR}</td></tr>
<tr><th>サイトの内容</th><td>20代・30代の男性に向けた、アパレル・インテリアの選び方やアイテムの紹介</td></tr>
<tr><th>お問い合わせ</th><td><a href="contact.html">お問い合わせページ</a>をご覧ください</td></tr>
</table></div>
<h2>このサイトについて</h2>
<p>{SITE}は「服と部屋を、ちょうどいい感じに。」をテーマに、無理のない予算で、長く使えるアイテムの選び方を紹介するサイトです。素材やサイズ、使うシーンといった選ぶときのポイントを整理し、読んだ人が自分に合うものを選べるようになることを目指しています。</p>
<h2 id="policy">商品の選定基準</h2>
<ul>
<li>記事のテーマ（部屋の広さ、手入れのしやすさ、使う場面など）に合っているか</li>
<li>サイズ・素材・仕様が販売ページやメーカーの情報で確認できるか</li>
<li>手持ちの服や家具と合わせやすく、長く使えそうか</li>
</ul>
<h2>情報の確認方法</h2>
<ul>
<li>商品のサイズや仕様は、メーカーや販売ページに記載された情報を確認して掲載し、確認した日付を記載します。</li>
<li>確認できなかった情報は、推測で補わずに掲載しません。</li>
<li>価格や在庫は変動するため、記事内には価格を掲載せず、販売ページで最新情報をご確認いただくようにしています。</li>
<li>実際に使用していない商品について、使用レビューや体験談は書きません。「人気ランキング」「売上No.1」など、根拠のない表現は使いません。</li>
</ul>
<h2>広告との関係</h2>
<p>当サイトはAmazonアソシエイト・プログラムに参加しており、記事内のリンクから商品が購入されると紹介料を受け取ることがあります。紹介料の有無によって、紹介する商品や評価を変えることはありません。詳しくは<a href="disclosure.html">広告・アフィリエイトについて</a>をご覧ください。</p>
<h2>誤りを見つけたら</h2>
<p>記事内の情報に誤りを見つけた場合は、<a href="contact.html">お問い合わせ</a>からご連絡ください。確認のうえ修正します。</p>
</article>"""
write("about.html", page("運営者情報・編集方針", f"{SITE}の運営者情報と編集方針", about, "about"))

privacy = open(os.path.join(os.path.dirname(__file__), "privacy_body.html"), encoding="utf-8").read()
write("privacy.html", page("プライバシーポリシー", f"{SITE}のプライバシーポリシー", privacy))

disc = f"""<article class="article static">
<h1>広告・アフィリエイトについて</h1>
<p><strong>Amazonのアソシエイトとして、{SITE}は適格販売により収入を得ています。</strong></p>
<p>{SITE}は、Amazon.co.jpを宣伝しリンクすることによってサイトが紹介料を獲得できる手段を提供することを目的に設定されたアフィリエイトプログラムである、Amazonアソシエイト・プログラムの参加者です。</p>
<p>当サイトの記事には、商品の販売ページや検索結果ページへのリンク（アフィリエイトリンク）が含まれています。読者の方がリンクを経由して商品を購入された場合、当サイトが紹介料を受け取ることがあります。読者の方の購入価格が上がることはありません。</p>
<p>紹介料の有無によって記事の内容や評価を変えることはありません。商品の価格・在庫・仕様は変わることがあるため、購入前には各販売ページで最新の情報をご確認ください。</p>
</article>"""
write("disclosure.html", page("広告・アフィリエイトについて", "広告・アフィリエイトについての表記", disc))

contact = f"""<article class="article static">
<h1>お問い合わせ</h1>
<p>{SITE}へのご意見・ご質問、記事内容の誤りのご指摘などは、以下のメールアドレスまでご連絡ください。</p>
<p class="mail"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>内容を確認のうえ、必要に応じて返信いたします。返信までにお時間をいただく場合があります。</p>
<p>いただいた個人情報は、<a href="privacy.html">プライバシーポリシー</a>に基づいて取り扱います。</p>
</article>"""
write("contact.html", page("お問い合わせ", f"{SITE}へのお問い合わせ", contact))
write("robots.txt", "User-agent: *\nAllow: /\n")
write("404.html", page("ページが見つかりません", "404", '<article class="article static"><h1>ページが見つかりません</h1><p><a href="index.html">トップページへ戻る</a></p></article>'))
print("built", len(os.listdir(OUT)))
