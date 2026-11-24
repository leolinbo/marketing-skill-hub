# -*- coding: utf-8 -*-
import sys

round3_html = '''  <!-- ==================== TAB: ROUND 3 ==================== -->
  <div id="tab-round3" class="tab-content active">

    <div class="section-title">🔥 第三轮最新线索（2026-11-22 新出 · 严格遵循 Bob 铁律）</div>
    <div class="container">

      <!-- 1. AMD Interior Architecture -->
      <div class="card">
        <div class="card-top">
          <div class="card-title">
            <span>1. AMD Interior Architecture</span>
            <span style="font-size:12px; color:#38bdf8;">商业与零售室内建筑 (伦敦)</span>
          </div>
          <div class="card-subtitle">核心官网: amdgb.com | 伦敦 Richmond</div>
          <div class="card-meta">现场印记: Reel "Lights we loved at LIGHT '26"，重点考察模块化轨道与可调角度投光灯。零售换季调光与灵活重组需求极高。</div>
          <div class="btn-group">
            <a class="btn btn-comment" href="https://www.instagram.com/reel/DgDWIbSBtgF/" target="_blank">💬 原帖直达/发评论</a>
            <a class="btn btn-ig" href="https://ig.me/m/amd_architecture" target="_blank">✉️ 发 IG 私信</a>
            <a class="btn btn-email-direct" href="mailto:contact@amdgb.com?subject=Your%20LIGHT%20'26%20picks%20%E2%80%94%2048V%20magnetic%20track%20for%20retail%20fit-outs&body=Hello%20AMD%20team%2C%0A%0AI%20saw%20your%20%22Lights%20we%20loved%20at%20LIGHT%20'26%22%20reel%E2%80%94the%20modular%20track%20and%20adjustable%20spots%20you%20highlighted%20are%20exactly%20what%20we%20specialize%20in.%0A%0AENCORE%20manufactures%20a%20slim%2048V%20magnetic%20track%20system%20in%20Shenzhen%20featuring%20snap-in%20spot%2C%20linear%2C%20and%20wall-wash%20modules%20(CRI%2090%2B%2C%202700%E2%80%936500K%2C%20CE).%20It%E2%80%99s%20engineered%20specifically%20for%20commercial%20and%20retail%20schemes%20that%20need%20fixtures%20re-aimed%20or%20swapped%20between%20seasons%20without%20rewiring.%0A%0AWould%20a%20spec%20sheet%20and%20a%20couple%20of%20retail%20installation%20photos%20be%20useful%20for%20your%20library%3F%0A%0ABest%20regards%2C%0A%0ABob%0AENCORE%20Lighting%0Asales%40encore-tech.com%20%7C%20%2B852%206768%202519%20%7C%20encore-tech.com">📧 唤起邮件直发</a>
            <a class="btn btn-wa" href="https://wa.me/442083926459" target="_blank">💬 WhatsApp</a>
            <a class="btn btn-primary" href="https://www.instagram.com/amd_architecture/" target="_blank">📷 IG 主页</a>
            <a class="btn btn-primary" href="https://amdgb.com" target="_blank">🌐 官网</a>
          </div>

          <!-- 邮件专属框 -->
          <div class="email-box">
            <div class="email-box-header">
              <span>📧 官方邮箱: contact@amdgb.com</span>
              <span style="font-size:11px; color:#c7d2fe;">单一产品 · 无价格 · 零售规格推介</span>
            </div>
            <div class="email-subject" id="r3-sub-1">Your LIGHT '26 picks — 48V magnetic track for retail fit-outs</div>
            <div class="email-body" id="r3-em-1">Hello AMD team,

I saw your "Lights we loved at LIGHT '26" reel—the modular track and adjustable spots you highlighted are exactly what we specialize in.

ENCORE manufactures a slim 48V magnetic track system in Shenzhen featuring snap-in spot, linear, and wall-wash modules (CRI 90+, 2700–6500K, CE). It’s engineered specifically for commercial and retail schemes that need fixtures re-aimed or swapped between seasons without rewiring.

Would a spec sheet and a couple of retail installation photos be useful for your library?

Best regards,

Bob
ENCORE Lighting
sales@encore-tech.com | +852 6768 2519 | encore-tech.com</div>
            <div class="email-btn-group">
              <button class="btn-copy-dual btn-copy-em" onclick="copyText('r3-sub-1', this)">📋 复制邮件主题</button>
              <button class="btn-copy-dual btn-copy-em" onclick="copyText('r3-em-1', this)">📋 复制邮件正文</button>
            </div>
          </div>

          <!-- 私信框 -->
          <div class="msg-box">
            <div class="msg-header"><span>✉️ IG 私信话术 (DM · 1-2句/只问对方/不提产品/落款Bob)</span></div>
            <div class="msg-preview" id="r3-dm-1">Loved your "Lights we loved at LIGHT '26" reel — on your retail fit-outs, are clients asking more for track that can be re-set between seasons without rewiring? — Bob</div>
            <button class="btn-copy-dual btn-copy-dm" onclick="copyText('r3-dm-1', this)">📋 一键复制私信话术 (DM)</button>
          </div>

          <!-- 评论框 -->
          <div class="msg-box">
            <div class="msg-header"><span>💬 帖子公开评论 (Comment · 自然赞赏/破冰)</span></div>
            <div class="msg-preview" id="r3-cm-1">Loved this curation! That modular track and adjustable spot setup at BDC was such a standout for clean retail schemes. 👏✨</div>
            <button class="btn-copy-dual btn-copy-cm" onclick="copyText('r3-cm-1', this)">📋 一键复制评论话术 (Comment)</button>
          </div>

          <!-- WhatsApp 框 -->
          <div class="msg-box">
            <div class="msg-header"><span>💬 WhatsApp 简短话术 (+44 20 8392 6459)</span></div>
            <div class="msg-preview" id="r3-wa-1">Hi AMD team, Bob here — saw your "Lights we loved at LIGHT '26" reel. For your retail projects, is flexible track something clients ask for more now? Happy to share a quick spec sheet if useful.</div>
            <button class="btn-copy-dual btn-copy-dm" onclick="copyText('r3-wa-1', this)">📋 一键复制 WhatsApp 话术</button>
          </div>
        </div>
      </div>

      <!-- 2. LumenArtz -->
      <div class="card">
        <div class="card-top">
          <div class="card-title">
            <span>2. LumenArtz</span>
            <span style="font-size:12px; color:#38bdf8;">照明选品与海外设计策展</span>
          </div>
          <div class="card-subtitle">账号: @lumenartz.lighting</div>
          <div class="card-meta">现场印记: Reel "Curating the best from London to bring back home"，立足从伦敦选购顶尖灯具赋能本土设计师与建筑师。</div>
          <div class="btn-group">
            <a class="btn btn-comment" href="https://www.instagram.com/reel/DgCYSslsXKd/" target="_blank">💬 原帖直达/发评论</a>
            <a class="btn btn-ig" href="https://ig.me/m/lumenartz.lighting" target="_blank">✉️ 发 IG 私信</a>
            <a class="btn btn-primary" href="https://www.instagram.com/lumenartz.lighting/" target="_blank">📷 IG 主页</a>
          </div>

          <!-- 私信框 -->
          <div class="msg-box">
            <div class="msg-header"><span>✉️ IG 私信话术 (DM · 1-2句/只问对方/不提产品/落款Bob)</span></div>
            <div class="msg-preview" id="r3-dm-2">Saw your reel about curating the best from London to bring back home — what's been hardest to source for the designers and architects you work with? — Bob</div>
            <button class="btn-copy-dual btn-copy-dm" onclick="copyText('r3-dm-2', this)">📋 一键复制私信话术 (DM)</button>
          </div>

          <!-- 评论框 -->
          <div class="msg-box">
            <div class="msg-header"><span>💬 帖子公开评论 (Comment · 自然赞赏/破冰)</span></div>
            <div class="msg-preview" id="r3-cm-2">Bringing the best of London lighting back home! So many brilliant optical details across the floor at BDC this year. Great recap! 🙌💡</div>
            <button class="btn-copy-dual btn-copy-cm" onclick="copyText('r3-cm-2', this)">📋 一键复制评论话术 (Comment)</button>
          </div>
        </div>
      </div>

      <!-- 3. KORU Concept -->
      <div class="card">
        <div class="card-top">
          <div class="card-title">
            <span>3. KORU Concept</span>
            <span style="font-size:12px; color:#38bdf8;">空间概念与室内设计</span>
          </div>
          <div class="card-subtitle">账号: @koru.conceptint | 伦敦住宅设计</div>
          <div class="card-meta">现场印记: Reel 记录在 Light26 结识优质供应商与同行，专注伦敦精品住宅室内与空间光效。</div>
          <div class="btn-group">
            <a class="btn btn-comment" href="https://www.instagram.com/reel/DgBilo9qJFc/" target="_blank">💬 原帖直达/发评论</a>
            <a class="btn btn-ig" href="https://ig.me/m/koru.conceptint" target="_blank">✉️ 发 IG 私信</a>
            <a class="btn btn-primary" href="https://www.instagram.com/koru.conceptint/" target="_blank">📷 IG 主页</a>
          </div>

          <!-- 私信框 -->
          <div class="msg-box">
            <div class="msg-header"><span>✉️ IG 私信话术 (DM · 1-2句/只问对方/不提产品/落款Bob)</span></div>
            <div class="msg-preview" id="r3-dm-3">Glad Light26 gave you some great connections! On your London residential projects lately, are clients leaning more toward hidden architectural lighting or statement decorative pieces? — Bob</div>
            <button class="btn-copy-dual btn-copy-dm" onclick="copyText('r3-dm-3', this)">📋 一键复制私信话术 (DM)</button>
          </div>

          <!-- 评论框 -->
          <div class="msg-box">
            <div class="msg-header"><span>💬 帖子公开评论 (Comment · 自然赞赏/破冰)</span></div>
            <div class="msg-preview" id="r3-cm-3">LiGHT26 really delivered on great connections and design inspiration this year! Loved the energy in your recap reel. ✨👏</div>
            <button class="btn-copy-dual btn-copy-cm" onclick="copyText('r3-cm-3', this)">📋 一键复制评论话术 (Comment)</button>
          </div>
        </div>
      </div>

      <!-- 4. Beata Denton -->
      <div class="card">
        <div class="card-top">
          <div class="card-title">
            <span>4. Beata Denton</span>
            <span style="font-size:12px; color:#38bdf8;">资深建筑灯光设计师 (Stockholm)</span>
          </div>
          <div class="card-subtitle">Head of Lighting Design at Reform / Reflex Architects</div>
          <div class="card-meta">现场印记: 强调灯具必须“能按设计任务书组装定制”（assembled to the brief），拒绝削足适履。斯德哥尔摩顶尖项目指定人。</div>
          <div class="btn-group">
            <a class="btn btn-comment" href="https://www.instagram.com/p/Df_9k4rlQlN/" target="_blank">💬 原帖直达/发评论</a>
            <a class="btn btn-ig" href="https://ig.me/m/beatadenton" target="_blank">✉️ 发 IG 私信</a>
            <a class="btn btn-email-direct" href="mailto:beata.denton@reflexark.se?subject=LiGHT26%20follow-up%20%2F%2F%20Modular%20fittings%20built%20to%20project%20brief&body=Hi%20Beata%2C%0A%0AHope%20you%20had%20a%20smooth%20trip%20back%20to%20Stockholm%20after%20LiGHT26.%0A%0AYour%20post%20emphasizing%20luminaires%20that%20can%20be%20assembled%20to%20the%20brief%20rather%20than%20forced%20into%20rigid%20standard%20forms%20resonated%20strongly%20with%20our%20engineering%20team.%0A%0AAt%20ENCORE%20Lighting%2C%20we%20manufacture%20modular%2048V%20architectural%20systems%20and%20customizable%20commercial%20fixtures%20tailored%20to%20project%20specifications%20(custom%20lengths%2C%20tailored%20optics%2C%20and%20specialized%20brackets).%0A%0ANo%20sales%20push%20here%E2%80%94just%20wanted%20to%20offer%20our%20technical%20specification%20deck%20in%20case%20it%E2%80%99s%20a%20helpful%20resource%20for%20Reform%E2%80%99s%20lighting%20library.%0A%0AWould%20a%20brief%20digital%20overview%20be%20welcome%3F%0A%0AWarm%20regards%2C%0A%0ABob%0AENCORE%20Lighting%20%7C%20sales%40encore-tech.com">📧 唤起邮件直发</a>
            <a class="btn btn-primary" href="https://www.instagram.com/beatadenton/" target="_blank">📷 IG 主页</a>
          </div>

          <!-- 邮件专属框 -->
          <div class="email-box">
            <div class="email-box-header">
              <span>📧 官方挖掘邮箱: beata.denton@reflexark.se</span>
              <span style="font-size:11px; color:#c7d2fe;">Reform / Reflex 建筑设计所</span>
            </div>
            <div class="email-subject" id="r3-sub-4">LiGHT26 follow-up // Modular fittings built to project brief</div>
            <div class="email-body" id="r3-em-4">Hi Beata,

Hope you had a smooth trip back to Stockholm after LiGHT26.

Your post emphasizing luminaires that can be assembled to the brief rather than forced into rigid standard forms resonated strongly with our engineering team.

At ENCORE Lighting, we manufacture modular 48V architectural systems and customizable commercial fixtures tailored to project specifications (custom lengths, tailored optics, and specialized brackets).

No sales push here—just wanted to offer our technical specification deck in case it’s a helpful resource for Reform’s lighting library.

Would a brief digital overview be welcome?

Warm regards,

Bob
ENCORE Lighting | sales@encore-tech.com</div>
            <div class="email-btn-group">
              <button class="btn-copy-dual btn-copy-em" onclick="copyText('r3-sub-4', this)">📋 复制邮件主题</button>
              <button class="btn-copy-dual btn-copy-em" onclick="copyText('r3-em-4', this)">📋 复制邮件正文</button>
            </div>
          </div>

          <!-- 私信框 -->
          <div class="msg-box">
            <div class="msg-header"><span>✉️ IG 私信话术 (DM · 1-2句/只问对方/不提产品/落款Bob)</span></div>
            <div class="msg-preview" id="r3-dm-4">Your point about fittings assembled to the brief really stood out. On your projects in Stockholm, how often do off-the-shelf fittings end up needing custom modifications? — Bob</div>
            <button class="btn-copy-dual btn-copy-dm" onclick="copyText('r3-dm-4', this)">📋 一键复制私信话术 (DM)</button>
          </div>

          <!-- 评论框 -->
          <div class="msg-box">
            <div class="msg-header"><span>💬 帖子公开评论 (Comment · 自然赞赏/破冰)</span></div>
            <div class="msg-preview" id="r3-cm-4">Spot on! Designing fixtures that adapt modularly to the brief rather than compromising the space for standard off-the-shelf fittings is so critical. Great takeaway from London! 💡</div>
            <button class="btn-copy-dual btn-copy-cm" onclick="copyText('r3-cm-4', this)">📋 一键复制评论话术 (Comment)</button>
          </div>
        </div>
      </div>

      <!-- 5. So It Is Design Studio -->
      <div class="card">
        <div class="card-top">
          <div class="card-title">
            <span>5. So It Is Design Studio</span>
            <span style="font-size:12px; color:#38bdf8;">室内与空间景观设计</span>
          </div>
          <div class="card-subtitle">核心人: Carla Belli | 官网: soitisdesign.com</div>
          <div class="card-meta">现场印记: Reel 现场演示轨道系统（Track demo），探讨室内绿植造景方案（Planting schemes）与轨道灯灵活性。</div>
          <div class="btn-group">
            <a class="btn btn-comment" href="https://www.instagram.com/reel/Df_48utxJuq/" target="_blank">💬 原帖直达/发评论</a>
            <a class="btn btn-ig" href="https://ig.me/m/so_it_is_designstudio" target="_blank">✉️ 发 IG 私信</a>
            <a class="btn btn-email-direct" href="mailto:hello@soitisdesign.com?subject=Your%20LIGHT%20'26%20track%20demo%20%2F%2F%20Precision%20lighting%20for%20planting%20%26%20interiors&body=Hi%20Carla%20and%20team%20So%20It%20Is%2C%0A%0AHope%20you%20had%20a%20great%20visit%20to%20LiGHT26%20at%20the%20Business%20Design%20Centre!%0A%0ALoved%20your%20video%20demonstrating%20track%20lighting%E2%80%94integrating%20directional%20track%20spots%20with%20biophilic%20and%20planting%20schemes%20is%20such%20an%20art.%0A%0AAt%20ENCORE%20Lighting%2C%20we%20manufacture%20miniature%2048V%20magnetic%20track%20systems%20with%20high-CRI%20(95%2B%2C%20R9%3E90)%20spots%20and%20narrow-to-wide%20interchangeable%20lenses%20designed%20specifically%20to%20accent%20living%20greenery%20and%20textured%20materials%20without%20glare.%0A%0AWould%20a%20quick%20spec%20sheet%20and%20photos%20of%20recent%20interior%20schemes%20be%20useful%20to%20keep%20on%20file%3F%0A%0ABest%20regards%2C%0A%0ABob%0AENCORE%20Lighting%20%7C%20sales%40encore-tech.com%20%7C%20encore-tech.com">📧 唤起邮件直发</a>
            <a class="btn btn-primary" href="https://www.instagram.com/so_it_is_designstudio/" target="_blank">📷 IG 主页</a>
            <a class="btn btn-primary" href="https://soitisdesign.com" target="_blank">🌐 官网</a>
          </div>

          <!-- 邮件专属框 -->
          <div class="email-box">
            <div class="email-box-header">
              <span>📧 官方工作室邮箱: hello@soitisdesign.com</span>
              <span style="font-size:11px; color:#c7d2fe;">室内与绿植灯光推介</span>
            </div>
            <div class="email-subject" id="r3-sub-5">Your LIGHT '26 track demo // Precision lighting for planting & interiors</div>
            <div class="email-body" id="r3-em-5">Hi Carla and team So It Is,

Hope you had a great visit to LiGHT26 at the Business Design Centre!

Loved your video demonstrating track lighting—integrating directional track spots with biophilic and planting schemes is such an art.

At ENCORE Lighting, we manufacture miniature 48V magnetic track systems with high-CRI (95+, R9>90) spots and narrow-to-wide interchangeable lenses designed specifically to accent living greenery and textured materials without glare.

Would a quick spec sheet and photos of recent interior schemes be useful to keep on file?

Best regards,

Bob
ENCORE Lighting | sales@encore-tech.com | encore-tech.com</div>
            <div class="email-btn-group">
              <button class="btn-copy-dual btn-copy-em" onclick="copyText('r3-sub-5', this)">📋 复制邮件主题</button>
              <button class="btn-copy-dual btn-copy-em" onclick="copyText('r3-em-5', this)">📋 复制邮件正文</button>
            </div>
          </div>

          <!-- 私信框 -->
          <div class="msg-box">
            <div class="msg-header"><span>✉️ IG 私信话术 (DM · 1-2句/只问对方/不提产品/落款Bob)</span></div>
            <div class="msg-preview" id="r3-dm-5">Loved the track demo in your LIGHT '26 video! When lighting interior planting schemes, do you find track systems flexible enough or do you usually prefer fixed pin-spots? — Bob</div>
            <button class="btn-copy-dual btn-copy-dm" onclick="copyText('r3-dm-5', this)">📋 一键复制私信话术 (DM)</button>
          </div>

          <!-- 评论框 -->
          <div class="msg-box">
            <div class="msg-header"><span>💬 帖子公开评论 (Comment · 自然赞赏/破冰)</span></div>
            <div class="msg-preview" id="r3-cm-5">That track demo was fantastic! Finding the right optical balance between directional accents and living planting schemes creates such amazing depth. 🌿✨</div>
            <button class="btn-copy-dual btn-copy-cm" onclick="copyText('r3-cm-5', this)">📋 一键复制评论话术 (Comment)</button>
          </div>
        </div>
      </div>

    </div>
  </div>
'''

with open('D:/marketing/LiGHT26_Leads_Workbench.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Update badges
old_badges = '''    <div class="badge-group">
      <span class="badge-orange">🔥 第二轮新线索: 15 家</span>
      <span class="badge-purple">📧 含公开邮箱: 9 家</span>
      <span class="badge">第一轮存量: 17 家</span>
    </div>'''

new_badges = '''    <div class="badge-group">
      <span class="badge-orange">🔥 第三轮最新: 5 家</span>
      <span class="badge">✨ 第二轮线索: 15 家</span>
      <span class="badge-purple">📧 含公开邮箱: 12 家</span>
      <span class="badge">🌟 第一轮存量: 17 家</span>
    </div>'''

if old_badges in orig:
    orig = orig.replace(old_badges, new_badges)

# Update tab buttons
old_tabs = '''  <!-- Tabs Navigation -->
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('tab-round2')">🔥 第二轮展后新买家 (15家·含私信/评论/邮件三版本)</button>
    <button class="tab-btn" onclick="switchTab('tab-round1')">🌟 第一轮展会线索 (17家)</button>
  </div>'''

new_tabs = '''  <!-- Tabs Navigation -->
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('tab-round3')">🔥 第三轮最新线索 (5家·2026-11-22新出·双版本+邮件/WA)</button>
    <button class="tab-btn" onclick="switchTab('tab-round2')">✨ 第二轮展后新买家 (15家·含私信/评论/邮件)</button>
    <button class="tab-btn" onclick="switchTab('tab-round1')">🌟 第一轮展会线索 (17家)</button>
  </div>'''

if old_tabs in orig:
    orig = orig.replace(old_tabs, new_tabs)

# Deactivate tab-round2 and insert tab-round3 before it
orig = orig.replace('<div id="tab-round2" class="tab-content active">', '<div id="tab-round2" class="tab-content">')

marker = '  <!-- ==================== TAB: ROUND 2 ==================== -->'
if marker in orig:
    orig = orig.replace(marker, round3_html + '\n\n' + marker)
else:
    print('Marker not found!')

with open('D:/marketing/LiGHT26_Leads_Workbench.html', 'w', encoding='utf-8') as f:
    f.write(orig)

print('Updated successfully! Total length:', len(orig))
