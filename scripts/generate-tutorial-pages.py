#!/usr/bin/env python3
"""Generate tutorial text detail pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "tutorials"

SHELL_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — 产品教程</title>
<link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="logo">
        <img src="../images/logo.png" alt="先达技术 AdvancedTech" class="logo-img" />
        <span class="logo-company">郑州市先达电子技术有限公司</span>
      </a>
      <nav class="nav-main" aria-label="主导航">
        <a href="../index.html" class="nav-link">首页</a>
        <a href="../about.html" class="nav-link">公司简介</a>
        <a href="../products.html" class="nav-link">产品中心</a>
        <a href="../tutorials.html" class="nav-link active">产品教程</a>
        <a href="../literature.html" class="nav-link">文献与资讯</a>
        <a href="../contact.html" class="nav-link">联系我们</a>
      </nav>
      <div class="header-actions">
        <a href="tel:0371-63930606" class="header-phone">0371-63930606</a>
        <a href="../contact.html" class="btn btn-primary btn-sm">技术咨询</a>
        <button class="nav-toggle" aria-label="打开菜单" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main>
    <section class="section tutorial-detail-page">
      <div class="container">
        <a href="../tutorials.html" class="product-back">← 返回产品教程</a>
        <p class="tutorial-detail-meta">
          <span class="tutorial-tag tutorial-tag-{kind_tag}">{kind_label}</span>
          <a href="../products/product-{product_num}.html" class="tutorial-product-link">查看产品详情 →</a>
        </p>
        <h1 class="tutorial-detail-title">{title}</h1>
        <div class="tutorial-detail-body handbook-content">
{body}
        </div>
      </div>
    </section>
  </main>
"""

SHELL_FOOT = """
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <p>郑州市先达电子技术有限公司</p>
        <p class="footer-desc">医疗与停车计时检定设备研发生产厂家</p>
      </div>
      <div class="footer-links">
        <h4>快速链接</h4>
        <a href="../products.html">产品中心</a>
        <a href="../tutorials.html">产品教程</a>
        <a href="../literature.html">文献与资讯</a>
        <a href="../about.html">公司简介</a>
      </div>
      <div class="footer-contact">
        <h4>联系我们</h4>
        <p>地址：河南省郑州市俭学街 5 号</p>
        <p>电话：<a href="tel:0371-63930606">0371-63930606</a></p>
        <p>邮箱：<a href="mailto:xdzz001@126.com">xdzz001@126.com</a></p>
        <p>联系人：郜女士</p>
        <div class="footer-wechat">
          <p class="footer-wechat-label">微信</p>
          <img src="../images/日出红似火微信.jpg" alt="微信二维码" class="footer-wechat-qr" width="120" height="120" loading="lazy" />
        </div>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>Copyright © 2008-2026 郑州市先达电子技术有限公司</p>
      <p>
        <a href="https://beian.miit.gov.cn/#/Integrated/index" target="_blank" rel="noopener noreferrer">豫ICP备2020028709号-1</a>
        <a href="https://beian.mps.gov.cn/#/" target="_blank" rel="noopener noreferrer">豫公网安备41010502007492号</a>
      </p>
    </div>
  </footer>

  <a href="tel:0371-63930606" class="float-call" aria-label="拨打电话">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">
      <path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.56 1 1 0 01-.24 1.01l-2.2 2.2z"/>
    </svg>
  </a>

  <script src="../main.js"></script>
</body>
</html>
"""

VIDEO_PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>产品操作视频教程 — 产品教程</title>
<link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="logo">
        <img src="../images/logo.png" alt="先达技术 AdvancedTech" class="logo-img" />
        <span class="logo-company">郑州市先达电子技术有限公司</span>
      </a>
      <nav class="nav-main" aria-label="主导航">
        <a href="../index.html" class="nav-link">首页</a>
        <a href="../about.html" class="nav-link">公司简介</a>
        <a href="../products.html" class="nav-link">产品中心</a>
        <a href="../tutorials.html" class="nav-link active">产品教程</a>
        <a href="../literature.html" class="nav-link">文献与资讯</a>
        <a href="../contact.html" class="nav-link">联系我们</a>
      </nav>
      <div class="header-actions">
        <a href="tel:0371-63930606" class="header-phone">0371-63930606</a>
        <a href="../contact.html" class="btn btn-primary btn-sm">技术咨询</a>
        <button class="nav-toggle" aria-label="打开菜单" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main>
    <section class="section tutorial-detail-page">
      <div class="container">
        <a href="../tutorials.html" class="product-back">← 返回产品教程</a>
        <p class="tutorial-detail-meta">
          <span class="tutorial-tag tutorial-tag-video">视频教程</span>
          <a href="https://www.bilibili.com/video/BV1Zw7v6zEXy" class="tutorial-product-link" target="_blank" rel="noopener noreferrer">在哔哩哔哩打开 →</a>
        </p>
        <h1 class="tutorial-detail-title">产品操作视频教程</h1>
        <div class="video-embed">
          <iframe
            src="//player.bilibili.com/player.html?isOutside=true&bvid=BV1Zw7v6zEXy&page=1&high_quality=1&danmaku=0&autoplay=0"
            scrolling="no"
            border="0"
            frameborder="no"
            framespacing="0"
            allowfullscreen="true"
            title="产品操作视频教程"
          ></iframe>
        </div>
        <p class="tutorial-video-note">视频托管于哔哩哔哩，若无法播放请尝试<a href="https://www.bilibili.com/video/BV1Zw7v6zEXy" target="_blank" rel="noopener noreferrer">前往 B 站观看</a>。</p>
      </div>
    </section>
  </main>
""" + SHELL_FOOT

TEXT_PAGES = [
    {
        "file": "text-01.html",
        "product_num": "01",
        "title": "多参数监护仪检定装置 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>开机自检完成后，按检定规程选择对应模拟参数（心电、血压、血氧、呼末 CO₂）</li>
<li>连接被检监护仪与检定装置，核对通道与量程设置</li>
<li>按 JJG 1163-2019 要求逐项记录示值误差</li>
</ul>
<h2>常见问题</h2>
<ul>
<li>血氧通道无响应：检查探头接口与模拟器档位是否匹配</li>
<li>压力模拟不稳定：确认气路连接密封，重新校准零点</li>
</ul>""",
    },
    {
        "file": "text-03.html",
        "product_num": "03",
        "title": "ECG-6 心脑电图机检定仪 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>触摸主界面选择检定模式，对照 JJG 543-2026 检定项目</li>
<li>锂电池供电时可独立现场作业，建议检定前充满电</li>
<li>输出标准心电信号，记录被检仪器幅值、频率响应等指标</li>
</ul>
<h2>常见问题</h2>
<ul>
<li>触摸无反应：长按电源键重启，检查屏幕保护膜是否影响触控</li>
<li>输出幅值偏差：在设置菜单中执行内部校准</li>
</ul>""",
    },
    {
        "file": "text-04.html",
        "product_num": "04",
        "title": "BPV5 无创血压计检定仪 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>先连接标准压力源，完成压力通道检定</li>
<li>切换至血压模拟模式，按示波法原理输出模拟脉搏波</li>
<li>记录被检血压计在不同压力点的示值误差</li>
</ul>""",
    },
    {
        "file": "text-05.html",
        "product_num": "05",
        "title": "LFIG-2 血氧饱和度模拟仪 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>设置目标 SpO₂ 与脉率模拟值，连接被检血氧仪探头</li>
<li>在多个设定点记录被检仪器示值与模拟值偏差</li>
<li>检定完毕关闭输出，避免长时间空载运行</li>
</ul>""",
    },
    {
        "file": "text-07.html",
        "product_num": "07",
        "title": "CPRV-1 心肺复苏机测试仪 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>按 JJF 1748-2019 要求安装测试工装，固定被检心肺复苏机</li>
<li>设置按压深度测试量程，启动被检设备记录实测值</li>
<li>多次测量取平均，与标准值比对</li>
</ul>""",
    },
    {
        "file": "text-16.html",
        "product_num": "16",
        "title": "XDJ-5M 无线地磁车辆模拟器 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>在待检地磁感应区域放置模拟器，模拟车辆驶入 / 驶离</li>
<li>对照 JJF 2241-2025 记录计时起止时刻与收费表显示</li>
<li>无线模式下注意模拟器电量与通信距离</li>
</ul>""",
    },
    {
        "file": "text-17.html",
        "product_num": "17",
        "title": "XDJ-5H 视频触发传感器 — 文字教程",
        "body": """<h2>操作要点</h2>
<ul>
<li>将视频触发传感器对准待检摄像头识别区域</li>
<li>触发模拟车辆进入 / 离开事件，记录计时收费表响应</li>
<li>按 JJF 2241-2025 要求计算时间误差</li>
</ul>""",
    },
]


def render_text(page):
    return SHELL_HEAD.format(
        title=page["title"],
        kind_tag="text",
        kind_label="文字教程",
        product_num=page["product_num"],
        body=page["body"],
    ) + SHELL_FOOT


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "video-01.html").write_text(VIDEO_PAGE, encoding="utf-8")
    print("wrote video-01.html")
    for page in TEXT_PAGES:
        (OUT / page["file"]).write_text(render_text(page), encoding="utf-8")
        print(f"wrote {page['file']}")


if __name__ == "__main__":
    main()
