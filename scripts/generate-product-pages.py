#!/usr/bin/env python3
"""Generate product detail pages from handbook content."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "products"

PRODUCTS = [
    {
        "num": "01",
        "file": "product-01.html",
        "title": "多参数监护仪检定装置（生命体征模拟仪） 一体机",
        "images": [("多参数新图1.JPG", "多参数监护仪检定装置 一体机")],
        "content": """
<h2>概述</h2>
<p>XDDC203多参数监护仪检定装置（或称生命体征模拟仪）可用于多参数监护仪的计量检定与质量控制。</p>
<p>十几年以来，我们先后研发了智能心脑电图机心电监护仪检定仪、无创血压计检定仪、血氧饱和度模拟仪和呼吸节律发生器。依据国家规程JJG 1163-2019《多参数监护仪》和相关校准规范，我们又成功研发了XDDC203多参数监护仪检定装置（或生命体征模拟仪）一体机。</p>
<h2>功能和主要特点</h2>
<ul>
<li>满足规程JJG 1163-2019《多参数监护仪》、JJG 692-2010《无创自动测量血压计》的建标要求。</li>
<li>采用7英寸触摸屏操作，集成有《JJG1163-2019 多参数监护仪》检定规程的全部项目。</li>
<li>装置为一体化设计，使用一台标准器可实现对监护仪心电、无创血压、脉搏血氧饱和度和呼末二氧化碳四个方面参数全项目检定。</li>
<li>可在同一窗口同时进行心电、血压、血氧功能的并行检测和变更输出模拟信号参数，三个功能同时检测可明显提高检测效率。</li>
<li>心电、血压、血氧和呼末二氧化碳四个参数可根据规程自主编制检定程序并一键执行。</li>
<li>内置大容量锂电池，TYPE C充电接口，方便现场检测。</li>
<li>检定装置标配附件：血氧饱和度模拟指，</li>
<li>检定装置选配附件：呼吸节律发生模块、标准气体和大气压计。</li>
</ul>
""",
    },
    {
        "num": "02",
        "file": "product-02.html",
        "title": "多参数监护仪检定装置  分体机",
        "images": [("2分体 多参数检定装置.png", "多参数监护仪检定装置 分体机")],
        "content": """
<h2>概述</h2>
<p>DCS-1多参数监护仪检定装置满足JJG 1163-2019《多参数监护仪》检定规程对标准器的要求。可用于多参数监护仪的计量检定与质量控制。</p>
<h2>组成</h2>
<p>1、规程中名称：心电模拟仪</p>
<p>推荐仪器名称型号：</p>
<p>ECG-6智能心脑电图机心电监护仪检定仪（手持型）</p>
<p>2、规程中名称：无创血压模拟仪</p>
<p>推荐仪器名称型号：BPV5无创血压计检定仪</p>
<p>3、规程中名称：脉搏血氧饱和度模拟仪</p>
<p>推荐仪器名称型号：LFIG-2血氧饱和度模拟仪</p>
<p>4、规程中名称：呼吸节律发生器</p>
<p>推荐仪器名称型号：HJF-1呼吸节律发生器</p>
<p>5、二氧化碳标准气体</p>
<p>（1）二氧化碳标准气体浓度为5%体积百分比（平衡气体为氮气）；    （2）采用4L/8L铝瓶，配二级减压阀。</p>
<p>6、大气压计（选配）</p>
""",
    },
    {
        "num": "03",
        "file": "product-03.html",
        "title": "智能心脑电图机心电监护仪检定仪",
        "images": [("心电新图2.JPG", "智能心脑电图机心电监护仪检定仪")],
        "content": """
<h2>概述</h2>
<p>ECG-6智能心脑电图机心电监护仪检定仪，满足最新JJG 543-2026心电图机检定规程技术要求，输出程序化的检测信号。</p>
<p>该产品是我司近二十年心电检测技术研发之大成，它继承了ECG-3智能心脑电图机检定仪的稳定可靠、易学易用的特点，它采用了大触摸屏、锂电池供电，因而自面市以来，深受计量工作者喜爱。</p>
<h2>功能和主要特点</h2>
<ul>
<li>手持式7英寸大屏幕触摸操作、界面友好，锂电池供电，方便现场检定。</li>
<li>多功能电极端子可适配，与心电图机电极连接和多参数监护仪电极连接更加方便。</li>
<li>增加了误差计算和参数计算的数据处理功能，提升了用户现场处理数据能力，节约了用户后续数据处理的时间。</li>
<li>增加了信号源的测试波形种类（多达十几种），满足了用户对测试信号多样化的需求。</li>
<li>用户可自行配置输出电路，如极化电压、模拟皮肤阻抗、输入阻抗的加入与去掉，以适合新的测试项目。</li>
<li>具有自动测量功能，一键完成规程要求的全部信号的输出。</li>
</ul>
""",
    },
    {
        "num": "04",
        "file": "product-04.html",
        "title": "无创血压计检定仪   无创血压模拟器",
        "images": [("4无创血压计检定仪.png", "无创血压计检定仪")],
        "content": """
<h2>概述</h2>
<p>BPV5无创血压计检定仪，符合JJG1163-2019《多参数监护仪》检定规程中血压模拟部分的技术要求，符合JJG692-2010《无创自动测量血压计》和JJG 270-2008《血压计和血压表》国家规程要求，能提供动态血压模拟和静态压力试验。</p>
<p>在BPV2无创血压计检定仪的基础上， 集十几年研发无创血压计检测设备之大成， BPV5无创血压计检定仪终于成功面市了！</p>
<p>本产品根据示波法血压计测量原理，逆向思维成功研制，它采用了利用机电一体化控制技术。</p>
<h2>功能和主要特点</h2>
<ul>
<li>采用宽视角7英寸彩色触摸屏和锂电池供电。产品集成度高，体积小重量轻，美观大方，仪器带有提手，便于携带。</li>
<li>具有动态血压模拟功能，用户可任意修改收缩压、舒张压和脉率等参数。</li>
<li>具有内置、外置袖带选择功能。</li>
<li>具备升压和降压二种控压模式。</li>
<li>具有四套静态压力的检测项目和数据，用户可自行修改并保存。</li>
<li>具有多点连续控压测量功能，一键完成全部静态压力点测量。</li>
<li>具有自动测量功能，按照三部血压相关规程编制有自动检测程序，按照自定义项目数据编制有自动检测程序。</li>
<li>设备可以平放，也可支撑到一定角度，也可立放。</li>
</ul>
""",
    },
    {
        "num": "05",
        "file": "product-05.html",
        "title": "血氧饱和度模拟仪",
        "images": [("5血氧饱和度.png", "血氧饱和度模拟仪")],
        "content": """
<h2>概述</h2>
<p>LFIG-2血氧饱和度模拟仪，符合JJG 1163-2019《多参数监护仪》检定规程，可模拟人体血氧饱和度值和脉搏频率值，用于检测脉搏血氧饱和度仪和多参数监护仪中血氧饱和度模块。它是基于现代光电技术和自动控制原理研发的。</p>
<h2>功能和主要特点</h2>
<ul>
<li>手持式设备，锂电池供电，适合现场检定。</li>
<li>采用彩色液晶显示，采用触摸屏和物理按键双操作，用户界面友好。</li>
<li>具有接收红光和红外光强指示功能，提示模拟指和血氧指夹的位置是否合适。</li>
<li>具有10种预装R曲线如BCI、 Nellcor、Masimo、HP (Philips)、 OxiMax、Ohmeda和Mindray曲线等。</li>
<li>光强度传输控制：可模拟黑色手指、厚手指、中等手指、浅色手指、薄手指和新生儿脚。</li>
<li>具有8种预置的病态血氧模拟信号。</li>
<li>具有血氧、脉率、脉幅和无脉搏报警测试功能。</li>
<li>具有10种可编程自动测试程序。</li>
<li>可模拟50Hz/60Hz和阳光环境光干扰。</li>
</ul>
""",
    },
    {
        "num": "06",
        "file": "product-06.html",
        "title": "呼吸节律发生器",
        "images": [("6HJF-1节律PI无背景.png", "呼吸节律发生器")],
        "content": """
<p>型号：HJF-1</p>
<ul>
<li>符合JJG1163-2019《多参数监护仪》检定规程。</li>
<li>适用于多参数监护仪主流和旁流呼末二氧化碳监测模块的检测。</li>
<li>仪器采用了低压气动技术，标气输入压力可低至0.04MPa，这大大减少了二氧化碳标气的用量。</li>
<li>具有二氧化碳浓度和呼吸率示值误差数据的自动计算功能。</li>
<li>选配浓度为5%体积百分比的二氧化碳标准气体、二级减压阀、0.1级的大气压计。</li>
<li>新一代产品，采用锂电池供电，体积小重量轻，便于携带。</li>
</ul>
""",
    },
    {
        "num": "07",
        "file": "product-07.html",
        "title": "心肺复苏机按压深度测试仪",
        "images": [("7心肺复苏CPRV-1.png", "心肺复苏机按压深度测试仪")],
        "content": """
<p>型号：CPRV-1</p>
<ul>
<li>符合：JJF1748-2019心肺复苏机校准规范</li>
<li>适用：心肺复苏机按压深度和频率现场校准。</li>
<li>采用先进的气动深度测量台和高精度激光测量传感器。</li>
<li>具有测量心肺复苏机按压深度和按压频率的功能。</li>
<li>能满足规程规定的复苏机按压头和标准器测试台适当挤压的技术规范。</li>
<li>本产品激光传感器已部署在设备内部，阿贝系统误差很小，对周边人员无不利影响。</li>
</ul>
""",
    },
    {
        "num": "08",
        "file": "product-08.html",
        "title": "肌电及诱发反应设备校准装置",
        "images": [("8 肌电及诱发校准.jpg", "肌电及诱发反应设备校准装置")],
        "content": """
<p>型号：EMG-1。</p>
<ul>
<li>满足规范：JJF 1896-2021肌电及诱发反应设备校准规范。</li>
<li>可准确检测肌电及诱发反应设备、肌电图机、肌电生物反馈仪等肌电设备。</li>
<li>肌电信号模拟仪是手持式设备，自带锂电池。采用彩色液晶触摸屏，用户界面友好。</li>
<li>输出波形：正弦波，方波，输出频率范围：0.5Hz～3kHz。</li>
<li>校准装置内置平衡衰减器、负载电阻。</li>
<li>校准装置附件：数字示波器。</li>
</ul>
""",
    },
    {
        "num": "09",
        "file": "product-09.html",
        "title": "浮标式氧气吸入器检定装置",
        "images": [("浮标式.png", "浮标式氧气吸入器检定装置")],
        "content": """
<ul>
<li>符合依据JJG 913-2015 浮标式氧气吸入器（以下简称吸入器）检定规程。</li>
<li>对氧气瓶用吸入器和墙式吸入器进行整体检定。</li>
<li>指示仪表为数字式，全新的结构设计，易于携带。</li>
<li>手持式检定装置可满足现场快速检测的需求。</li>
<li>指示仪表为指针式的检定装置结实耐用（图略）。</li>
</ul>
""",
    },
    {
        "num": "10",
        "file": "product-10.html",
        "title": "B超检定装置套件",
        "images": [
            ("10 左B超-mW功率计.jpg", "毫瓦级超声功率计"),
            ("10右B超-体模.jpg", "仿组织超声体模"),
        ],
        "content": """
<ul>
<li>满足JJG 639-1998 医用超声诊断仪超声源检定规程的要求。</li>
<li>包含：毫瓦级超声功率计、仿组织超声体模和泄漏电流测试仪。</li>
</ul>
""",
    },
    {
        "num": "11",
        "file": "product-11.html",
        "title": "医用输液泵注射泵质量检测仪",
        "images": [("输液泵.png", "医用输液泵注射泵质量检测仪")],
        "content": """
<ul>
<li>7英寸触摸液晶屏幕，触控操作。</li>
<li>双通道前置接口，流量压力接口一体化设计。</li>
<li>依据JJF 1259-2018、WS/T 657-2019设计交互界面。</li>
<li>可自动判断流量稳定状态，自动测量并记录读数。</li>
<li>管路灌注操作指引，灌注过程图形化显示。</li>
<li>可根据测量数据，实时显示流量、压力曲线。</li>
<li>具备气泡报警功能，避免影响测量结果。</li>
</ul>
""",
    },
    {
        "num": "12",
        "file": "product-12.html",
        "title": "心脏除颤分析仪",
        "images": [("12除颤.png", "心脏除颤分析仪")],
        "content": """
<ul>
<li>心脏除颤器分析仪主要用于释放能量检测、心电信号模拟、经皮起搏检测。</li>
<li>符合JJF 1149-2014《心脏除颤器校准规范》（包括JJG 760-2003心电监护仪的引用部分）技术要求。</li>
<li>彩色液晶大屏显示，触控操作。</li>
<li>窦性心律心率范围：27bpm～300bpm。</li>
<li>除颤脉冲释放后，可显示放电波形。</li>
<li>除颤能量：(0～360)J，(360～600）J。</li>
</ul>
""",
    },
    {
        "num": "13",
        "file": "product-13.html",
        "title": "肺功能仪校准装置（标准呼吸模拟器）",
        "images": [("13肺功能仪校准装置.jpg", "肺功能仪校准装置")],
        "content": """
<ul>
<li>满足JJF  1213-2008《肺功能仪校准规范》。</li>
<li>满足YY/T   1804-2021《麻醉和呼吸设备用于测量人体时间用力呼气量的肺量计》。</li>
<li>满足YY/T   1438-2016《麻醉和呼吸设备评价自主呼吸者肺功能的呼气峰值流量计》。</li>
<li>体积小，和传统肺功能仪相比，便于运输、移动。</li>
<li>易于操作，触摸屏一体式设计，学习成本低，简单易用。</li>
<li>高精度，采用高品质伺服电机，精度高、误差小。</li>
<li>输出体积范围：(0~10)L，输出流量范围：(0.5~20)L/s。</li>
</ul>
""",
    },
    {
        "num": "14",
        "file": "product-14.html",
        "title": "呼吸机测试仪",
        "images": [("14呼吸机测试仪.jpg", "呼吸机测试仪")],
        "content": """
<ul>
<li>可进行呼吸机流量、潮气量、呼吸频率、压力、氧浓度等参数的测量。</li>
<li>仪器双向气流测量，结构小巧，便于携式，易于操作。</li>
<li>7寸彩色触摸屏，全中文操作界面，用户界面简单。</li>
<li>内置大容量锂电池，支持长时间续航，方便外检。</li>
<li>测试数据图形同屏显示，满足各种呼吸机校准需求。</li>
<li>自动化检测流程，一键操作，省时省力。</li>
<li>气体流速与潮气量独立校准模式，确保数据精准可靠。</li>
</ul>
""",
    },
    {
        "num": "15",
        "file": "product-15.html",
        "title": "出租汽车计价器检定装置",
        "images": [("15出租车.jpg", "出租汽车计价器检定装置")],
        "content": """
<ul>
<li>满足《JJG 517-2016 出租汽车计价器》、《JJG 738-2024出租汽车计价器检定装置》中的所有技术要求。</li>
<li>主滚轮周长1m，采用无缝钢管制造，镀硬铬。</li>
<li>检定装置采用内置电机，由变频器驱动。</li>
<li>具有自动刹车和手动刹车功能。</li>
<li>检定软件可自动计算检定结果、自动生成并打印原始记录和检定证书。</li>
<li>装置配有全自动采样系统。</li>
</ul>
""",
    },
    {
        "num": "16",
        "file": "product-16.html",
        "title": "综合型停车场电子停车计时装置检定仪",
        "images": [("16停车场图片all-4260421.png", "综合型停车场电子停车计时装置检定仪")],
        "content": """
<h2>概述</h2>
<p>符合国家计量JJF 2241-2025电子停车计时收费表校准规范（我公司参加起草）。</p>
<p>符合国家计量JJF1900-2021 停车场电子计时装置检定仪校准规范（我公司参加起草）。</p>
<p>XDJ-5Q系列综合型电子停车计时装置检定仪包含：检定仪主机、无线地感泊车模拟器、视频触发传感器和无线地磁车辆模拟器。</p>
<p>可检定目前国内车牌拍照识别的电子停车计时收费系统，还可检定基于地磁场技术的物联网平台计时收费管理系统。</p>
<h2>功能和主要特点</h2>
<ul>
<li>采用高精度GNSS（北斗+GPS等）授时模块，具有RTC电子时钟。</li>
<li>主机加无线地感泊车模拟器，可检定地感触发车牌识别的停车计时系统。</li>
<li>利用视频触发传感器可对基于视频触发车牌识别的停车计时系统进行检定。</li>
<li>主机+无线地磁车辆模拟器，可检定基于地磁场技术的物联网计时收费管理平台。</li>
<li>检定仪主机内部自带锂电池，标准USB充电接口，满电可连续工作时间16小时以上。</li>
<li>用户可根据当地停车场情况选择不同的检定仪配置。</li>
<li>具有在平板电脑运行的电子停车计时检定管理软件，可进行现场原始数据采集和处理。</li>
</ul>
""",
    },
    {
        "num": "17",
        "file": "product-17.html",
        "title": "视频触发传感器  XDJ-5H视频触发停车场电子停车计时装置检定仪",
        "images": [("5H新图.JPG", "XDJ-5H 视频触发停车场电子停车计时装置检定仪")],
        "content": """
<ul>
<li>检定仪它包含了数字式时钟，专利产品。</li>
<li>采用GNSS卫星授时，可单独使用。</li>
<li>数字式时钟采用8个大尺寸段码液晶，室外、阳光下更清晰，适合现场拍照。</li>
<li>具有25通道计时器，适配多出入口、多时间点检测。</li>
<li>具有检测时间点接近提醒功能。</li>
<li>充满电可连续工作16小时以上， 适合现场工作。</li>
<li>便于携带到现场，且可以溯源。</li>
</ul>
""",
    },
    {
        "num": "18",
        "file": "product-18.html",
        "title": "地磁车辆模拟器  XDJ-5M地磁停车场电子停车计时装置检定仪",
        "images": [("18地磁车辆模拟器 xdj-5M 2.png", "XDJ-5M 地磁停车场电子停车计时装置检定仪")],
        "content": """
<ul>
<li>发明专利产品。</li>
<li>能满足多模地磁电子停车计时收费云平台的校准。</li>
<li>地磁车辆模拟器可配合主机使用。</li>
<li>一体化设计的检定仪包含了地磁车辆模拟器，可作为一个独立的标准器使用。</li>
<li>具有地磁场测量功能。</li>
<li>具有水平移动的机械臂，运动迅速丝滑。</li>
<li>充满电可连续工作16小时以上，适合现场工作。</li>
</ul>
""",
    },
]


def render_images(images, layout=None):
    if not images:
        return '<div class="product-page-image product-page-image-placeholder"><span>暂无产品图片</span></div>'
    parts = []
    for src, alt in images:
        parts.append(
            f'<img src="../images/{src}" alt="{alt}" class="product-photo" />'
        )
    if len(parts) == 1:
        return f'<div class="product-page-image">{parts[0]}</div>'
    wrapper = "product-page-images-row" if layout == "row" else "product-page-images"
    return f'<div class="{wrapper}">{"".join(parts)}</div>'


def render_page(p):
    images_html = render_images(p["images"], p.get("images_layout"))
    layout_class = " product-page-layout-wide" if p.get("images_layout") == "row" else ""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["title"]} — 郑州市先达电子技术有限公司</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet" />
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
        <a href="../products.html" class="nav-link active">产品中心</a>
        <a href="../tutorials.html" class="nav-link">产品教程</a>
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
    <section class="section product-page">
      <div class="container">
        <a href="../products.html" class="product-back">← 返回产品中心</a>
        <h1 class="product-page-title">{p["title"]}</h1>
        <div class="product-page-layout{layout_class}">
          {images_html}
          <div class="product-page-content handbook-content">
{p["content"].strip()}
          </div>
        </div>
      </div>
    </section>
  </main>

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


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PRODUCTS:
        (OUT / p["file"]).write_text(render_page(p), encoding="utf-8")
        print("wrote", p["file"])


if __name__ == "__main__":
    main()
