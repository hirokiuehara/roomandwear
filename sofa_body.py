# -*- coding: utf-8 -*-
TAG = "roomandwear-22"
CHECKED = "2026年11月17日"

def amz(asin):
    return f"https://www.amazon.co.jp/dp/{asin}?tag={TAG}"

LAYOUT_SVG = """
<figure class="figure">
<svg viewBox="0 0 420 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="6畳の1Kにソファを置いたときの配置図">
<rect x="10" y="10" width="400" height="300" fill="#fbf8f1" stroke="#2a2724" stroke-width="4"/>
<!-- window -->
<line x1="130" y1="10" x2="290" y2="10" stroke="#8fa0ae" stroke-width="8"/>
<text x="210" y="32" text-anchor="middle" font-size="12" fill="#6b665e">窓</text>
<!-- door -->
<path d="M10 250 L10 310" stroke="#fbf8f1" stroke-width="6"/>
<path d="M12 250 A60 60 0 0 1 70 308" fill="none" stroke="#9a7550" stroke-width="2" stroke-dasharray="4 3"/>
<text x="24" y="296" font-size="12" fill="#6b665e">入口</text>
<!-- bed -->
<rect x="300" y="40" width="100" height="190" fill="#e4dccb" stroke="#6b665e" stroke-width="2"/>
<text x="350" y="140" text-anchor="middle" font-size="13" fill="#2a2724">ベッド</text>
<!-- sofa -->
<rect x="22" y="70" width="70" height="140" rx="6" fill="#5a5f3c"/>
<text x="57" y="145" text-anchor="middle" font-size="13" fill="#fff" writing-mode="tb">ソファ</text>
<text x="22" y="60" font-size="11" fill="#2a2724">ソファ奥行き 約60〜85cm</text>
<!-- table -->
<rect x="130" y="100" width="60" height="80" fill="#9a7550"/>
<text x="160" y="145" text-anchor="middle" font-size="11" fill="#fff">テーブル</text>
<!-- clearance arrows -->
<line x1="94" y1="190" x2="128" y2="190" stroke="#c0392b" stroke-width="2" marker-end="url(#a)" marker-start="url(#a)"/>
<text x="112" y="226" text-anchor="middle" font-size="11" fill="#c0392b">30〜45cm</text>
<!-- walkway -->
<rect x="200" y="40" width="90" height="260" fill="#5a5f3c" fill-opacity="0.08" stroke="#5a5f3c" stroke-dasharray="5 4"/>
<text x="245" y="250" text-anchor="middle" font-size="12" fill="#5a5f3c">通り道</text>
<text x="245" y="266" text-anchor="middle" font-size="12" fill="#5a5f3c">60cm以上</text>
<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10z" fill="#c0392b"/></marker></defs>
</svg>
<figcaption>6畳の1K（約270×360cm）の一例。ソファは壁に沿わせ、入口から窓への通り道と、テーブルとのすき間を確保します。数値は目安です。</figcaption>
</figure>
"""

def product(label, name, asin, size, features, caution, fit, note=""):
    return f"""
<div class="product">
  <p class="product-label">{label}</p>
  <h3>{name}</h3>
  <dl>
    <dt>サイズ</dt><dd>{size}</dd>
    <dt>特徴</dt><dd>{features}</dd>
    <dt>注意点</dt><dd>{caution}</dd>
    <dt>向いている人</dt><dd>{fit}</dd>
    <dt>価格</dt><dd>価格・在庫は変動するため掲載していません。最新の価格はAmazonでご確認ください（販売ページの確認日：{CHECKED}）。</dd>
  </dl>
  {f'<p class="small">{note}</p>' if note else ''}
  <a class="btn-amazon" href="{amz(asin)}" target="_blank" rel="nofollow sponsored noopener">Amazonで価格・詳細を見る</a>
</div>"""

BODY = f"""
<div class="summary">
<p class="summary-title">この記事で分かること</p>
<ul>
<li>一人暮らしの部屋に合うソファのサイズと、置く前に測る場所</li>
<li>素材ごとの座り心地・手入れのしやすさの違い</li>
<li>狭い部屋向け・手入れ重視・くつろぎ重視の3つの選び方と商品例</li>
</ul>
<p class="summary-title">選び方の要点</p>
<ol>
<li>置き場所の<strong>幅・奥行き</strong>と、ソファの前に<strong>通り道が残るか</strong>を先に測る</li>
<li>狭い部屋なら<strong>背もたれが低い・脚つき</strong>のタイプで圧迫感を減らす</li>
<li>汚れが気になるなら<strong>カバーを外して洗えるか</strong>を確認する</li>
<li>大きなソファは<strong>玄関・廊下・エレベーターを通るか</strong>を必ず確認する</li>
</ol>
</div>

<p>ソファがあると、部屋でくつろぐ時間の質がぐっと上がります。一方で、部屋の中でも大きな家具なので、選び方を間違えると部屋が狭く感じたり、搬入できなかったりすることも。ここでは一人暮らしの部屋を想定して、ソファ選びのポイントを順番にまとめます。</p>

<h2>サイズ：まずは置き場所を測る</h2>
<p>一人暮らしなら、幅<strong>110〜170cm程度の2人掛け〜2.5人掛け</strong>が一般的です。置きたい場所の幅と奥行きを測り、ソファの前に人が通れる<strong>50〜60cm以上のスペース</strong>が残るかを確認しましょう。</p>
{LAYOUT_SVG}

<h2>購入前に測る場所のチェックリスト</h2>
<ul class="checklist">
<li>置き場所の幅（壁から壁、または家具から家具まで）</li>
<li>置き場所の奥行き（ソファの前に通り道が残るか）</li>
<li>コンセントやエアコン、窓の位置とかぶらないか</li>
<li>玄関ドアの幅・高さ</li>
<li>廊下の幅と、曲がり角の広さ</li>
<li>エレベーターの入口と内部のサイズ（集合住宅の場合）</li>
<li>部屋のドアの幅（完成品のソファは特に重要）</li>
</ul>
<p class="small">完成品（組み立て不要）のソファは、梱包サイズで通るかを確認します。組み立て式なら、部品の箱が通れば搬入しやすくなります。</p>

<h2>素材・タイプの比較</h2>
<div class="table-wrap">
<table>
<tr><th>素材・タイプ</th><th>座り心地・見た目</th><th>手入れのしやすさ</th><th>向いている人</th></tr>
<tr><td>ファブリック（布）</td><td>やわらかい雰囲気。季節を問わず使いやすい</td><td>汚れがしみこみやすい。カバーを外して洗えるタイプなら清潔に保ちやすい</td><td>部屋になじむ見た目を重視する人</td></tr>
<tr><td>合成皮革</td><td>すっきりした印象。夏はべたつきやすいことがある</td><td>表面の汚れを拭き取りやすい。長く使うと表面が劣化することがある</td><td>飲み物などの汚れが気になる人</td></tr>
<tr><td>本革</td><td>高級感があり、使うほど風合いが出る</td><td>専用の手入れが必要。価格は高め</td><td>長く使う前提で投資したい人</td></tr>
<tr><td>ウレタン中心のクッション</td><td>軽く、組み立て式が多い</td><td>へたりやすさは商品によって差がある</td><td>搬入のしやすさ・価格を重視する人</td></tr>
<tr><td>ポケットコイル入り</td><td>体を点で支え、沈み込みすぎにくい</td><td>重く、完成品が多い</td><td>座り心地を重視する人</td></tr>
</table>
</div>

<h2>高さ：低めを選ぶと部屋が広く見える</h2>
<p>背もたれの低いロータイプのソファは、部屋全体の見通しが良くなり、圧迫感を減らせます。床に近い暮らしが好きなら、座椅子タイプやフロアソファも選択肢です。脚つきでソファの下に空間があると、床が見える分だけ軽やかな印象になり、ロボット掃除機が通れるものもあります。</p>

<h2>色は部屋のベースカラーに合わせる</h2>
<p>グレー・ベージュ・オリーブ・ブラウンなどの落ち着いた色は、ほかの家具となじみやすく、男性の部屋にも合わせやすい色です。床や壁、ラグの色と近いトーンを選ぶとまとまります。</p>

<h2>よくある失敗例と対策</h2>
<div class="table-wrap">
<table>
<tr><th>失敗例</th><th>対策</th></tr>
<tr><td>部屋に置いたら思ったより大きく、通り道がなくなった</td><td>床にマスキングテープでソファの外形を貼り、数日過ごしてみる</td></tr>
<tr><td>玄関や廊下を通らず、搬入できなかった</td><td>梱包サイズと搬入経路を事前に測る。組み立て式を選ぶ</td></tr>
<tr><td>座面の奥行きが合わず、落ち着いて座れない</td><td>商品ページの「座面奥行き」「座面高さ」を確認する</td></tr>
<tr><td>汚れが落ちず、すぐに見た目が気になった</td><td>カバーリング仕様や、拭き取りやすい素材を選ぶ</td></tr>
<tr><td>色が部屋から浮いてしまった</td><td>床・ラグ・カーテンの色に近い中間色を選ぶ</td></tr>
</table>
</div>

<h2>条件別に選んだソファ3点</h2>
<p>ここでは「狭い部屋向け」「手入れ重視」「くつろぎ重視」の3つの条件で、Amazonの販売ページに記載されたサイズや仕様をもとに選びました。編集部が実際に使用したレビューではありません。サイズや仕様は販売ページの記載（{CHECKED}確認）に基づいています。購入前に最新の情報を必ずご確認ください。</p>
{product("狭い部屋向け","アイリスプラザ 2人掛けソファ FBS-2P（アッシュグレー）","B07VXTJR2S",
 "幅約113×奥行約62×高さ約68cm（販売ページの商品サイズ表記。商品名には「幅110cm」とあります）",
 "奥行きが約62cmとコンパクト。脚の下にロボット掃除機が通れる高さがあると記載。組み立て式。",
 "座面の奥行きは約43cmと浅めなので、深く座ってくつろぎたい人には物足りない可能性があります。",
 "6畳前後の部屋で、通り道をしっかり確保したい人")}
{product("手入れ重視","RASIK 2人掛けソファ ida（イーダ）グレージュ","B0CSFBTSVB",
 "幅135.5×奥行77×高さ73cm（販売ページの商品の寸法）",
 "カバーを取り外して洗濯機で丸洗いできると記載。天然木の脚は取り外してローソファとしても使える。組み立て式。",
 "奥行きが77cmあるため、狭い部屋では通り道の幅を事前に確認してください。生地は光の当たり方で色の見え方が変わると記載されています。",
 "汚れが気になる人、清潔に使い続けたい人")}
{product("くつろぎ重視","アイリスプラザ ポケットコイルソファ 2.5人掛け PCSV-170（コーヒーブラウン）","B082M916QL",
 "幅約167×奥行約84×高さ約77cm（販売ページの商品サイズ表記）",
 "中材にポケットコイル・ウレタン・Sバネなどを使用と記載。2.5人掛けで座面に余裕がある。完成品（脚部のみ取り付け）。",
 "完成品で重量は約35kgと記載されているため、玄関・廊下・エレベーターを通るか必ず確認してください。張地はポリエステル・合成皮革と記載されています。",
 "部屋に余裕があり、座り心地を優先したい人")}

<h2>まとめ</h2>
<p>ソファ選びは「置き場所と搬入経路を測る」「部屋の広さに合った高さとサイズ」「手入れの方法」の順で考えると失敗しにくくなります。迷ったら、まずは床にソファの大きさをテープで貼って、暮らしやすさを確かめてみてください。</p>
"""

ITEMS = []  # product cards are embedded in BODY
