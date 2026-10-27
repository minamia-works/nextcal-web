import os, html
CSS = """
  :root { color-scheme: light dark; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", sans-serif; max-width: 680px; margin: 0 auto; padding: 48px 24px 96px; line-height: 1.9; color: #37231A; background: #FFFAF5; }
  @media (prefers-color-scheme: dark) { body { color: #FFF4EC; background: #16110E; } a { color: #FF8A63; } hr { border-color: #3a2f28; } }
  h1 { font-size: 1.5rem; } h2 { font-size: 1.15rem; margin-top: 2em; } h3 { font-size: 1rem; margin-top: 1.4em; }
  p.updated { opacity: 0.6; font-size: 0.9rem; }
  a { color: #F4511E; } a.back { display: inline-block; margin-bottom: 24px; }
  hr { border: none; border-top: 1px solid #eadfd3; margin: 2em 0; }
  ul { padding-left: 1.2em; } li { margin: 0.3em 0; }
  table { border-collapse: collapse; width: 100%; font-size: 0.95rem; } td, th { border: 1px solid #d9c9b8; padding: 8px 10px; text-align: left; vertical-align: top; }
"""
def page(lang, title, body, back_href, back_label):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | NextCal</title>
<style>{CSS}</style>
</head>
<body>
  <a class="back" href="{back_href}">← {back_label}</a>
{body}
</body>
</html>
"""
def write(path, content):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(content)

UPDATED_JA = "2026年10月23日"
UPDATED_EN = "October 23, 2026"
MAIL = "minamia.works@gmail.com"

# ---------- 日本語 ----------
ja_privacy = f"""  <h1>プライバシーポリシー</h1>
  <p class="updated">最終更新日：{UPDATED_JA}</p>

  <p>minamia-works（以下「当方」）は、iOSアプリケーション「NextCal」（以下「本アプリ」）における情報の取り扱いについて、以下のとおりプライバシーポリシー（以下「本ポリシー」）を定めます。</p>

  <hr>
  <h2>1. 要点</h2>
  <ul>
    <li>カレンダーの予定の<strong>内容（名前・場所・参加者・メモ）は、端末の外に送信しません</strong>。予定の読み取りと表示の判断は、すべて端末の中で行います。</li>
    <li>ロック画面や Dynamic Island に表示を出すため、当方のサーバーが、通知を送る時刻と、端末の宛先だけを預かります。</li>
    <li>広告（Google AdMob）を表示します。</li>
  </ul>

  <hr>
  <h2>2. サーバーに送信・保存する情報</h2>
  <p>本アプリは、アプリが閉じている間も、時刻どおりに Live Activity を出し、消すために、当方のサーバーに次の情報を送り、保存します。</p>
  <table>
    <tr><th>情報</th><th>内容・目的</th></tr>
    <tr><td>端末の識別子と秘密値</td><td>端末ごとに、アプリが作るランダムな値です（氏名や Apple ID とは結びつきません）。秘密値は、ハッシュ化して保存します。サーバーが、端末を見分け、他の人から操作されないようにするために使います。</td></tr>
    <tr><td>通知の宛先（トークン）</td><td>Apple の通知サービス（APNs）が、この端末に通知を届けるための値です。表示の開始用・更新用など、複数あります。</td></tr>
    <tr><td>通知を送る時刻</td><td>Live Activity を始める・終わらせる・端末を起こす時刻（UNIX 秒）と、表示を見分けるための鍵（予定の開始時刻）です。<strong>予定の名前などの内容は含みません。</strong></td></tr>
    <tr><td>表示のオン・オフ</td><td>Live Activity を一時停止しているかどうかです。</td></tr>
    <tr><td>連絡の記録</td><td>端末から最後に連絡があった時刻、応答のなかった通知の数、サーバーが送った通知の種類と時刻です。通知の内容は含みません。動作の確認と、案内の通知（開始できなかったとき）のために使います。</td></tr>
  </table>
  <h3>収集しない情報</h3>
  <ul>
    <li>予定の名前・場所・参加者・メモなど、カレンダーの内容</li>
    <li>氏名、メールアドレス、電話番号など、個人を特定できる情報</li>
    <li>位置情報、連絡先</li>
    <li>アカウント情報（本アプリはアカウント登録・ログインを必要としません）</li>
  </ul>

  <hr>
  <h2>3. 情報の利用目的</h2>
  <ul>
    <li>予定の開始前に、ロック画面・Dynamic Island に Live Activity を表示し、開始後に消すため</li>
    <li>表示が出なかったときに、案内の通知を送るため</li>
    <li>サービスの安定した運営と、不具合の調査のため</li>
  </ul>

  <hr>
  <h2>4. 保存期間と削除</h2>
  <ul>
    <li>端末から 90 日間連絡がない場合、サーバーはその端末の情報を自動で削除します。</li>
    <li>サーバーの情報の削除を希望する場合は、下の連絡先にご連絡ください。端末の識別子（アプリの端末内に保存されるランダムな値）が必要になるため、ご本人の確認ができる範囲で対応します。確認が難しい場合も、アプリを削除したうえで 90 日経てば、自動で削除されます。</li>
    <li>アプリをアンインストールした場合も、サーバーの情報は、上の 90 日が過ぎると自動で削除されます。</li>
  </ul>

  <hr>
  <h2>5. 広告</h2>
  <p>本アプリは、Google LLC の広告サービス「AdMob」を利用して、アプリを開いたときに全画面の広告を表示します。バックグラウンドで更新が行われるとき、および Live Activity の更新では、広告を表示しません。</p>
  <ul>
    <li>広告の配信・計測のため、Google が、端末の情報（広告に使う識別子、IP アドレス、広告の操作の記録、端末・アプリの情報など）を収集・利用することがあります。詳しくは、<a href="https://policies.google.com/technologies/partner-sites?hl=ja">Google のポリシー</a>をご覧ください。</li>
    <li>EU・英国・米国の一部の州など、法令で必要な地域では、広告に関する同意の確認（Google の UMP）を表示します。同意は、アプリの「設定 → このアプリについて → 広告のプライバシー設定」（表示される地域のみ）から、いつでも変更できます。</li>
    <li>本アプリは、Apple の App Tracking Transparency（アプリの追跡の許可）は求めません。</li>
  </ul>

  <hr>
  <h2>6. 端末の権限</h2>
  <ul>
    <li><strong>カレンダー（フルアクセス）</strong>：予定を読み取り、表示を決めるために使います。読み取った内容は、端末の外に送信しません。</li>
    <li><strong>通知</strong>：アプリを閉じている間に追加・変更された予定を検知するために、静かな通知（画面を点けず、音も出さず、通知センターに残らない通知）を約 5 分おきに受け取ります。この通知で動く拡張機能が、端末の中でカレンダーを読み、予定の開始時刻だけをサーバーに送ります（予定の名前などの内容は送りません）。また、表示を開始できなかったときの案内にも使います。通知を許可しなくても、アプリを開いている間は動作します。</li>
    <li><strong>Live Activity</strong>：ロック画面・Dynamic Island に表示するために使います。</li>
  </ul>

  <hr>
  <h2>7. 第三者サービス</h2>
  <ul>
    <li>Apple（APNs）：通知の配信</li>
    <li>Fly.io：サーバーのホスティング（東京リージョン）</li>
    <li>Google AdMob：広告の配信</li>
  </ul>
  <p>当方は、上記以外に、情報を第三者へ提供しません。ただし、法令に基づく開示の請求があった場合を除きます。</p>

  <hr>
  <h2>8. お子様のプライバシー</h2>
  <p>本アプリは、13歳未満のお子様を対象としたものではなく、お子様から意図的に情報を収集することはありません。</p>

  <hr>
  <h2>9. 本ポリシーの変更</h2>
  <p>本ポリシーの内容は、法令の変更や本アプリの機能追加などに応じて、変更されることがあります。変更後のポリシーは、本ページに掲載した時点から効力を生じます。</p>

  <hr>
  <h2>10. お問い合わせ</h2>
  <ul>
    <li>開発者：minamia-works</li>
    <li>お問い合わせ先：<a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>"""

ja_terms = f"""  <h1>利用規約</h1>
  <p class="updated">最終更新日：{UPDATED_JA}</p>

  <p>この利用規約（以下「本規約」）は、minamia-works（以下「当方」）が提供するiOSアプリケーション「NextCal」（以下「本アプリ」）の利用条件を定めるものです。本アプリを利用することで、本規約に同意したものとみなします。</p>

  <hr>
  <h2>1. 本アプリについて</h2>
  <p>本アプリは、iPhone のカレンダーにある、これから始まる予定を、ロック画面と Dynamic Island の Live Activity に表示するアプリです。</p>

  <hr>
  <h2>2. 利用条件</h2>
  <ul>
    <li>本アプリは、iOS 26 以降の iPhone で利用できます。</li>
    <li>表示のために、カレンダー・通知・Live Activity の許可が必要です。</li>
    <li>本アプリは、無料で利用できます。広告が表示されます。</li>
  </ul>

  <hr>
  <h2>3. 禁止事項</h2>
  <ul>
    <li>本アプリまたはサーバーに、不正にアクセスし、または負荷をかける行為</li>
    <li>本アプリの逆アセンブル、改変、再配布</li>
    <li>法令または公序良俗に反する行為</li>
  </ul>

  <hr>
  <h2>4. 表示の遅延・欠落について</h2>
  <p>Live Activity の表示は、Apple の通知サービスと iOS の仕組みに依存します。次のような場合に、表示が遅れたり、出なかったり、止まったりすることがあります。</p>
  <ul>
    <li>iPhone の再起動後、通信ができないとき、低電力モードのとき、iOS が処理を制限したとき</li>
    <li>アプリを閉じている間にカレンダーを変更し、本アプリが次に動くまで、変更が伝わらないとき</li>
    <li>iOS が同時に表示できる Live Activity の数を超えたとき</li>
  </ul>
  <p>大切な予定の見逃しを避けるために、カレンダーの標準の通知などを併用してください。</p>

  <hr>
  <h2>5. 免責事項</h2>
  <ul>
    <li>当方は、本アプリの機能が中断なく、または誤りなく動作することを保証するものではありません。</li>
    <li>表示の遅延・欠落、OS の仕様変更などに起因して生じた損害について、当方は責任を負わないものとします。</li>
    <li>当方は、法令上許容される範囲において、本アプリの利用により生じたいかなる損害についても責任を負いません。</li>
  </ul>

  <hr>
  <h2>6. サービスの変更・終了</h2>
  <p>当方は、事前の通知なく、本アプリの内容を変更し、または提供を終了することがあります。</p>

  <hr>
  <h2>7. 規約の変更</h2>
  <p>当方は、必要と判断した場合、事前の通知なく本規約を変更することがあります。変更後の規約は、本ページに掲載した時点から効力を生じます。</p>

  <hr>
  <h2>8. 準拠法・管轄</h2>
  <p>本規約の解釈にあたっては、日本法を準拠法とします。本アプリに関して紛争が生じた場合には、当方の所在地を管轄する裁判所を第一審の専属的合意管轄裁判所とします。</p>

  <hr>
  <h2>9. お問い合わせ</h2>
  <ul>
    <li>開発者：minamia-works</li>
    <li>お問い合わせ先：<a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>"""

ja_support = f"""  <h1>サポート</h1>
  <p class="updated">最終更新日：{UPDATED_JA}</p>

  <h2>Live Activity が出ないとき</h2>
  <ul>
    <li><strong>許可を確認</strong>：iPhone の「設定」で、NextCal の「カレンダー（フルアクセス）」「通知」「ライブアクティビティ」が、すべてオンか確認してください。アプリの設定画面の「アクセス」にも、状態が出ます。</li>
    <li><strong>一時停止になっていないか</strong>：アプリのホーム右下のボタンが、再生（▶）なら、一時停止中です。押すと、再開します。</li>
    <li><strong>表示のタイミング</strong>：予定の何分前から出すかは、アプリの設定の「表示のタイミング」で決めます。範囲より先の予定は、出ません。</li>
    <li><strong>終日の予定</strong>：初期設定では、含めていません。設定の「終日の予定を含める」で変えられます。</li>
    <li><strong>iPhone を再起動したあと</strong>：NextCal を 1 回開いてください。</li>
    <li><strong>予定を追加・変更したのに反映されない</strong>：アプリを閉じている間の変更は、アプリが次に動くまで、反映が遅れることがあります。アプリを開くと、すぐ反映されます。</li>
  </ul>

  <h2>Live Activity が 5 枚までしか出ない</h2>
  <p>iOS の仕様で、1 つのアプリが同時に出せる Live Activity は 5 枚までです。先の予定は、手前の予定が終わったあとに出ます。</p>

  <h2>データの削除</h2>
  <p>サーバーが預かっている情報（端末の宛先と、通知の時刻）は、アプリを削除して 90 日経つと、自動で削除されます。早く削除したいときは、下のメールアドレスまでご連絡ください。詳しくは、<a href="../privacy/">プライバシーポリシー</a>をご覧ください。</p>

  <h2>お問い合わせ</h2>
  <p>解決しないときは、下のメールアドレスまでご連絡ください。機種名・iOS のバージョン・状況を添えていただけると助かります。予定の内容は、書かなくて大丈夫です。</p>
  <ul>
    <li>開発者：minamia-works</li>
    <li>お問い合わせ先：<a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>"""

# ---------- English ----------
en_privacy = f"""  <h1>Privacy Policy</h1>
  <p class="updated">Last updated: {UPDATED_EN}</p>

  <p>minamia-works ("we") provides the iOS app "NextCal" (the "App"). This policy explains how information is handled in the App.</p>

  <hr>
  <h2>1. Summary</h2>
  <ul>
    <li>The <strong>contents of your calendar events (titles, locations, attendees, notes) never leave your device</strong>. Reading events and deciding what to show happens entirely on your device.</li>
    <li>To show Live Activities on the Lock Screen and in the Dynamic Island, our server holds only the times to send updates and your device's push addresses.</li>
    <li>The App shows ads (Google AdMob).</li>
  </ul>

  <hr>
  <h2>2. Information sent to and stored on our server</h2>
  <p>So the App can start and end Live Activities on time, even while it is closed, it sends the following to our server.</p>
  <table>
    <tr><th>Information</th><th>What it is / why</th></tr>
    <tr><td>Device identifier and secret</td><td>Random values the App creates on your device (not linked to your name or Apple ID). The secret is stored hashed. Used to tell devices apart and keep others from controlling yours.</td></tr>
    <tr><td>Push addresses (tokens)</td><td>Values Apple's push service (APNs) uses to deliver notifications to this device, for starting and updating Live Activities, among others.</td></tr>
    <tr><td>Times to send notifications</td><td>Times (Unix seconds) to start or end a Live Activity or wake the app, and a key to tell Live Activities apart (the event start time). <strong>They do not include event titles or any other event content.</strong></td></tr>
    <tr><td>On/off state</td><td>Whether you have paused Live Activities.</td></tr>
    <tr><td>Contact log</td><td>The last time the device contacted the server, the number of unanswered notifications, and the type and time of notifications the server sent (not their content). Used to confirm operation and to send help notifications (when a Live Activity could not start).</td></tr>
  </table>
  <h3>Information we do not collect</h3>
  <ul>
    <li>Calendar content such as event titles, locations, attendees, and notes</li>
    <li>Name, email address, phone number, or other identifying information</li>
    <li>Location, contacts</li>
    <li>Accounts (the App needs no sign-up or login)</li>
  </ul>

  <hr>
  <h2>3. How we use information</h2>
  <ul>
    <li>To show Live Activities before an event starts and end them afterwards</li>
    <li>To send help notifications when a display did not appear</li>
    <li>To operate the service reliably and investigate problems</li>
  </ul>

  <hr>
  <h2>4. Retention and deletion</h2>
  <ul>
    <li>If a device has not contacted the server for 90 days, the server deletes its information automatically.</li>
    <li>To have the server information deleted, please contact us at the address below. Deletion needs the device identifier (a random value stored inside the App), so we will help as far as we can verify it is yours. If that is difficult, deleting the App and waiting 90 days also removes the information automatically.</li>
    <li>If you uninstall the App, the server information is deleted automatically after the 90 days above.</li>
  </ul>

  <hr>
  <h2>5. Advertising</h2>
  <p>The App uses Google LLC's AdMob to show a full-screen ad when you open the App. No ads are shown when the App is woken in the background or when a Live Activity updates.</p>
  <ul>
    <li>To deliver and measure ads, Google may collect and use device information (advertising-related identifiers, IP address, ad interaction records, device and app information). See <a href="https://policies.google.com/technologies/partner-sites">Google's policy</a>.</li>
    <li>In regions where the law requires it (the EU, the UK, some US states, and others), the App shows an ad consent prompt (Google UMP). You can change your choice anytime from "Settings → About → Ad privacy settings" (shown only in those regions).</li>
    <li>The App does not ask for Apple's App Tracking Transparency permission.</li>
  </ul>

  <hr>
  <h2>6. Permissions</h2>
  <ul>
    <li><strong>Calendar (full access)</strong>: to read events and decide what to show. What it reads never leaves your device.</li>
    <li><strong>Notifications</strong>: to detect events added or changed while the app is closed, the app receives a quiet notification (no screen wake-up, no sound, removed automatically) about every 5 minutes. An extension triggered by it reads the calendar on your device and sends only event start times to our server (never titles or other details). Notifications are also used to tell you when a display could not start. The app still works while open if you do not allow notifications.</li>
    <li><strong>Live Activities</strong>: to show on the Lock Screen and in the Dynamic Island.</li>
  </ul>

  <hr>
  <h2>7. Third-party services</h2>
  <ul>
    <li>Apple (APNs): notification delivery</li>
    <li>Fly.io: server hosting (Tokyo region)</li>
    <li>Google AdMob: ad delivery</li>
  </ul>
  <p>We do not share information with other third parties, except when disclosure is required by law.</p>

  <hr>
  <h2>8. Children</h2>
  <p>The App is not directed to children under 13, and we do not knowingly collect information from them.</p>

  <hr>
  <h2>9. Changes</h2>
  <p>We may update this policy, for example when laws change or features are added. Changes take effect when posted on this page.</p>

  <hr>
  <h2>10. Contact</h2>
  <ul>
    <li>Developer: minamia-works</li>
    <li>Contact: <a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>"""

en_terms = f"""  <h1>Terms of Use</h1>
  <p class="updated">Last updated: {UPDATED_EN}</p>

  <p>These Terms of Use (the "Terms") set the conditions for using the iOS app "NextCal" (the "App") provided by minamia-works ("we"). By using the App you agree to these Terms.</p>

  <hr>
  <h2>1. About the App</h2>
  <p>The App shows upcoming events from your iPhone's calendar as Live Activities on the Lock Screen and in the Dynamic Island.</p>

  <hr>
  <h2>2. Conditions of use</h2>
  <ul>
    <li>The App works on iPhones running iOS 26 or later.</li>
    <li>It needs your permission for Calendar, Notifications, and Live Activities.</li>
    <li>The App is free to use and shows ads.</li>
  </ul>

  <hr>
  <h2>3. Prohibited acts</h2>
  <ul>
    <li>Accessing the App or the server without authorization, or placing undue load on them</li>
    <li>Disassembling, modifying, or redistributing the App</li>
    <li>Anything that violates law or public order</li>
  </ul>

  <hr>
  <h2>4. Delays and gaps in display</h2>
  <p>Live Activities depend on Apple's push service and iOS. A display may be late, missing, or stop in cases such as:</p>
  <ul>
    <li>After a restart of the iPhone, without a connection, in Low Power Mode, or when iOS limits background work</li>
    <li>When you change the calendar while the App is closed and the change reaches the server only when the App next runs</li>
    <li>When more Live Activities are needed than iOS allows at once</li>
  </ul>
  <p>To avoid missing important events, please also use the calendar's standard alerts.</p>

  <hr>
  <h2>5. Disclaimer</h2>
  <ul>
    <li>We do not guarantee that the App works without interruption or errors.</li>
    <li>We are not liable for damages caused by delays or gaps in display, changes to the OS, and the like.</li>
    <li>To the extent permitted by law, we are not liable for any damages arising from use of the App.</li>
  </ul>

  <hr>
  <h2>6. Changes to the service</h2>
  <p>We may change or end the App without notice.</p>

  <hr>
  <h2>7. Changes to the Terms</h2>
  <p>We may change these Terms without notice when needed. Changes take effect when posted on this page.</p>

  <hr>
  <h2>8. Governing law</h2>
  <p>These Terms are governed by the laws of Japan. The court with jurisdiction over our location is the exclusive court of first instance for any dispute about the App.</p>

  <hr>
  <h2>9. Contact</h2>
  <ul>
    <li>Developer: minamia-works</li>
    <li>Contact: <a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>"""

en_support = f"""  <h1>Support</h1>
  <p class="updated">Last updated: {UPDATED_EN}</p>

  <h2>If a Live Activity doesn't appear</h2>
  <ul>
    <li><strong>Check permissions</strong>: in the iPhone Settings app, make sure NextCal has Calendar (full access), Notifications, and Live Activities turned on. The Access section in the app's settings shows them too.</li>
    <li><strong>Is it paused?</strong>: if the button at the bottom right of the Home screen shows play (▶), Live Activities are paused. Tap it to resume.</li>
    <li><strong>Timing</strong>: how many minutes before an event it appears is set in Settings → Timing. Events further away don't show.</li>
    <li><strong>All-day events</strong>: excluded by default. Turn on "Include all-day events" in Settings.</li>
    <li><strong>After restarting your iPhone</strong>: open NextCal once.</li>
    <li><strong>You added or changed an event but nothing changed</strong>: changes made while the app is closed can take until the app next runs. Opening the app updates it right away.</li>
  </ul>

  <h2>Only 5 Live Activities show</h2>
  <p>iOS lets one app show at most 5 Live Activities at once. Later events appear after earlier ones end.</p>

  <h2>Deleting your data</h2>
  <p>What the server holds (your device's push addresses and notification times) is deleted automatically 90 days after you delete the app. To have it removed sooner, please email us. See the <a href="../privacy/">Privacy Policy</a> for details.</p>

  <h2>Contact</h2>
  <p>If this doesn't solve it, please email us. Including your device model, iOS version, and what happened helps. You don't need to include any event details.</p>
  <ul>
    <li>Developer: minamia-works</li>
    <li>Contact: <a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>"""

HOME_JA = """  <h1>NextCal</h1>
  <p>NextCal は、iPhone のカレンダーの「これから始まる予定」を、ロック画面と Dynamic Island の Live Activity に、カウントダウンつきで表示するアプリです。予定を見逃さないための、iPhone 専用の無料アプリです。</p>

  <h2>できること</h2>
  <ul>
    <li>予定が近づくと、ロック画面と Dynamic Island に、自動で Live Activity が出て、始まると自動で消えます。毎日アプリを開いたり、ボタンを押したりする必要はありません。</li>
    <li>開始時刻ごとに、別の Live Activity で、予定の名前とカウントダウンを表示します。同じ時刻に始まる複数の予定は、まとめて 1 枚に表示します。</li>
    <li>通知を許可していれば、アプリを閉じていても、強制終了していても、新しく追加した予定を拾います（通知は目立たない形で送られます）。</li>
    <li>iPhone のカレンダーアプリに入っているカレンダー（iCloud、Google など）を使います。使うカレンダーと、終日の予定を含めるかを、選べます。</li>
  </ul>

  <h2>プライバシー</h2>
  <p>予定の内容（名前・場所・参加者・メモ）は、iPhone の外へ送信しません。詳しくは、<a href="privacy/">プライバシーポリシー</a>をご覧ください。</p>

  <h2>リンク</h2>
  <ul>
%ITEMS%
  </ul>
  %OTHER%"""

HOME_EN = """  <h1>NextCal</h1>
  <p>NextCal is a free iPhone app that shows the next events in your Calendar as Live Activities on the Lock Screen and in the Dynamic Island, with a countdown, so you don't miss what's coming up.</p>

  <h2>What it does</h2>
  <ul>
    <li>As an event approaches, a Live Activity appears on the Lock Screen and in the Dynamic Island on its own, and goes away by itself once the event starts. No daily taps or opening the app.</li>
    <li>Each start time gets its own Live Activity with the event name and a countdown. Events that start at the same time are shown together on one card.</li>
    <li>With notifications allowed, it picks up newly added events even when the app is closed or force-quit (the notifications are silent and unobtrusive).</li>
    <li>It works with the calendars already in your iPhone's Calendar app (iCloud, Google, and more). You choose which calendars to use and whether to include all-day events.</li>
  </ul>

  <h2>Privacy</h2>
  <p>Event contents (titles, locations, attendees, notes) never leave your iPhone. See the <a href="privacy/">Privacy Policy</a> for details.</p>

  <h2>Links</h2>
  <ul>
%ITEMS%
  </ul>
  %OTHER%"""

ROOT_HOME = """  <h1>NextCal</h1>
  <p>NextCal は、iPhone のカレンダーの「これから始まる予定」を、ロック画面と Dynamic Island の Live Activity に、カウントダウンつきで表示するアプリです。予定の内容は、iPhone の外へ送信しません。</p>
  <p>NextCal is a free iPhone app that shows your next Calendar events as Live Activities on the Lock Screen and in the Dynamic Island, with a countdown. Event contents never leave your iPhone.</p>
  <ul>
    <li><a href="ja/">日本語（概要・プライバシーポリシー・利用規約・サポート）</a></li>
    <li><a href="en/">English (Overview, Privacy Policy, Terms, Support)</a></li>
    <li><a href="ja/privacy/">プライバシーポリシー</a> / <a href="en/privacy/">Privacy Policy</a></li>
  </ul>"""

for lang, labels, pages in (
    ("ja", ("NextCal", {"privacy": ("プライバシーポリシー", ja_privacy), "terms": ("利用規約", ja_terms), "support": ("サポート", ja_support)}), None),
    ("en", ("NextCal", {"privacy": ("Privacy Policy", en_privacy), "terms": ("Terms of Use", en_terms), "support": ("Support", en_support)}), None),
):
    for name, (title, body) in labels[1].items():
        write(f"{lang}/{name}/index.html", page(lang, title, body, "../", "NextCal"))
    items = "\n".join(f'    <li><a href="{n}/">{t}</a></li>' for n, (t, _) in labels[1].items())
    other = '<p><a href="../en/">English</a></p>' if lang == "ja" else '<p><a href="../ja/">日本語</a></p>'
    home = HOME_JA if lang == "ja" else HOME_EN
    write(f"{lang}/index.html", page(lang, "NextCal", home.replace("%ITEMS%", items).replace("%OTHER%", other), "../", "NextCal").replace('<a class="back" href="../">← NextCal</a>\n', ""))
write("index.html", page("ja", "NextCal", ROOT_HOME, "./", "NextCal").replace('<a class="back" href="./">← NextCal</a>\n', ""))
