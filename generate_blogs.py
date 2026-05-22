import sys

def generate_blog_html(filename, title, date_str, img_url, content_html):
    html = f"""<!DOCTYPE html>
<html lang="hy">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smartic | {title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Armenian:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="global.css">
    <style>
        .post-hero {{
            padding: 200px 0 100px;
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{img_url}') center/cover no-repeat;
            text-align: center;
            color: #fff;
        }}
        .post-hero h1 {{ font-size: 48px; font-weight: 700; margin-bottom: 20px; line-height: 1.3; max-width: 900px; margin-left: auto; margin-right: auto; }}
        .post-meta {{ font-size: 14px; color: var(--accent); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; display: inline-flex; align-items: center; gap: 8px; }}

        .post-content-section {{ padding: 80px 0; background: var(--bg-white); }}
        .post-body {{ max-width: 800px; margin: 0 auto; color: #333; }}
        .post-body p {{ font-size: 16px; line-height: 1.8; margin-bottom: 25px; }}
        .post-body h2 {{ font-size: 28px; color: #111; margin: 40px 0 20px; line-height: 1.3; }}
        .post-body h3 {{ font-size: 22px; color: #222; margin: 30px 0 15px; }}
        .post-body ul {{ margin-bottom: 25px; padding-left: 20px; }}
        .post-body ul li {{ font-size: 16px; line-height: 1.8; margin-bottom: 10px; }}
        .post-body img {{ width: 100%; border-radius: 12px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
        
        @media (max-width: 768px) {{
            .post-hero h1 {{ font-size: 32px; }}
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header class="header" id="header">
        <div class="header-inner">
            <div class="logo">
                <a href="index.html" style="display:flex; align-items:center;"><img src="logo.png" alt="Smartic Logo"></a>
            </div>
            <div class="mobile-menu-btn" id="mobile-menu-toggle">
                <i class="fa-solid fa-bars"></i>
            </div>
            <nav class="nav-links" id="nav-links">
                <div class="dropdown">
                    <a href="#" style="display:flex; align-items:center; gap:5px;">Ծառայություններ <i class="fa-solid fa-chevron-down" style="font-size:10px;"></i></a>
                    <div class="dropdown-content">
                        <a href="smart-home.html">Խելացի Տուն</a>
                        <a href="smart-office.html">Խելացի Գրասենյակ</a>
                    </div>
                </div>
                <a href="projects.html">Նախագծեր</a>
                <a href="about.html">Մեր մասին</a>
                <a href="#">Տեսականի</a>
                <a href="#">Հետադարձ Կապ</a>
                <a href="blog.html" style="color: #222;">Բլոգ</a>
            </nav>
            <div class="header-actions" id="header-actions">
                <div style="font-size: 12px; font-weight: 600; color: #888;">
                    <span style="color: #222;">HY</span> | <a href="#">EN</a> | <a href="#">RU</a>
                </div>
                <a href="tel:+37455103090" style="font-size: 14px; color: #333;"><i class="fa-solid fa-phone"></i></a>
                <a href="#booking" class="contact-btn">Ամրագրել</a>
            </div>
        </div>
    </header>

    <!-- Post Hero -->
    <section class="post-hero">
        <div class="container">
            <span class="post-meta"><i class="fa-regular fa-calendar"></i> {date_str}</span>
            <h1>{title}</h1>
        </div>
    </section>

    <!-- Post Content -->
    <section class="post-content-section">
        <div class="container">
            <div class="post-body">
                {content_html}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <div class="logo" style="margin-bottom: 15px;"><a href="index.html"><img src="logo.png" alt="Smartic Logo"></a></div>
                    <p style="font-size: 13px; color: var(--text-muted);">LifeSmart բրենդի պաշտոնական ներկայացուցիչը Հայաստանում:</p>
                </div>
                <div>
                    <h4>Ընկերություն</h4>
                    <ul>
                        <li><a href="about.html">Մեր մասին</a></li>
                        <li><a href="projects.html">Նախագծեր</a></li>
                        <li><a href="blog.html">Բլոգ</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Ծառայություններ</h4>
                    <ul>
                        <li><a href="smart-home.html">Խելացի տուն</a></li>
                        <li><a href="smart-office.html">Խելացի գրասենյակ</a></li>
                        <li><a href="#">Անվտանգություն</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Կապ մեզ հետ</h4>
                    <ul>
                        <li><a href="#">Ռուբինյանց 27/3, Երևան</a></li>
                        <li><a href="tel:+37455103090">+374 55 103090</a></li>
                        <li><a href="mailto:info@smartic.am">info@smartic.am</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; 2026 Smartic. Բոլոր իրավունքները պաշտպանված են:
            </div>
        </div>
    </footer>

    <!-- STICKY WHATSAPP -->
    <a href="https://wa.me/37455103090" target="_blank" class="whatsapp-float">
        <i class="fa-brands fa-whatsapp"></i>
    </a>

    <script>
        // Header shadow on scroll
        window.addEventListener('scroll', () => {{
            const header = document.getElementById('header');
            if (window.scrollY > 10) {{ header.classList.add('scrolled'); }} 
            else {{ header.classList.remove('scrolled'); }}
        }});
    </script>
</body>
</html>
"""
    with open(filename, "w") as f:
        f.write(html)

# 1. blog-design.html
content_1 = """
<img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=800" alt="Design">
<p>Խելացի տունը ոչ միայն տեխնոլոգիա է, այլև կենսակերպ: Իմացեք, թե ինչպես կարելի է սահուն կերպով ինտեգրել ժամանակակից սարքավորումները ձեր ինտերիերի դիզայնում՝ առանց գեղագիտությունը խաթարելու:</p>
<h2>Քայլ 1: Համապատասխանության նախագծում</h2>
<p>Նախագծման վաղ փուլերում խելացի տան համակարգերի ինտեգրումը թույլ է տալիս թաքցնել բոլոր լարերը և ապահովել էսթետիկ տեսք: (Այս հատվածը ժամանակավոր տեքստ է, որը կարող եք փոխարինել բնօրինակով):</p>
<ul>
    <li>Լուսավորության սցենարների պլանավորում</li>
    <li>Սենսորների և անջատիչների ճիշտ տեղակայում</li>
    <li>Աուդիո համակարգերի ինտեգրում առաստաղում</li>
</ul>
<h2>Քայլ 2: Ճիշտ սարքավորումների ընտրություն</h2>
<p>Կարևոր է ընտրել այնպիսի սարքավորումներ, որոնք համահունչ են ինտերիերին: (Այս հատվածը ժամանակավոր տեքստ է, որը կարող եք փոխարինել բնօրինակով):</p>
<img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&q=80&w=800" alt="Smart Home App">
<h2>Ամփոփում</h2>
<p>Խելացի տունը ձեր դիզայնի անբաժան մասն է, և ճիշտ մոտեցման դեպքում այն կընդգծի ինտերիերի առանձնահատկությունները: (Այս հատվածը ժամանակավոր տեքստ է):</p>
"""
generate_blog_html("blog-design.html", "Ինչպես ինտեգրել Խելացի Տուն համակարգերը դիզայնի նախագծում", "24 ԱՊՐ 2024", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1200", content_1)

# 2. blog-meeting.html
content_2 = """
<img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=800" alt="Meeting Room">
<p>Բացահայտեք, թե ինչպես կարող է խելացի կոնֆերանս սենյակը բարելավել ձեր թիմի արդյունավետությունը և տպավորել հաճախորդներին նորագույն տեխնոլոգիաներով:</p>
<h2>Ի՞նչ է իրենից ներկայացնում Smart Meeting Room-ը</h2>
<p>Դա միջավայր է, որտեղ տեխնոլոգիաներն աշխատում են ի նպաստ մարդկանց՝ հեշտացնելով շփումը և հանդիպումների կառավարումը: (Այս հատվածը ժամանակավոր տեքստ է):</p>
<ul>
    <li>Ավտոմատացված լուսավորություն և կլիմա</li>
    <li>Մեկ հպումով պրեզենտացիաների մեկնարկ</li>
    <li>Բարձրորակ վիդեոկոնֆերանսների ինտեգրում</li>
</ul>
<img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=800" alt="Meeting Room Tech">
<h2>Առավելությունները</h2>
<p>Արդյունավետության բարձրացում և ժամանակի խնայողություն: (Այս հատվածը ժամանակավոր տեքստ է):</p>
"""
generate_blog_html("blog-meeting.html", "Հանդիպումների Խելացի Սենյակ – Smart Meeting Room", "12 ԱՊՐ 2024", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1200", content_2)

# 3. blog-lifesmart.html
content_3 = """
<img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&q=80&w=800" alt="LifeSmart">
<p>Մանրամասն վերլուծություն այն մասին, թե ինչու է LifeSmart-ը համարվում լավագույն ընտրությունը ավտոմատացման ոլորտում և ինչ առավելություններ ունի այն:</p>
<h2>Նորարարություն և Հուսալիություն</h2>
<p>LifeSmart բրենդն ապահովում է կայունություն և գերժամանակակից լուծումներ: (Այս հատվածը ժամանակավոր տեքստ է):</p>
<ul>
    <li>Անլար համակարգերի բարձր հուսալիություն (CoSS պրոտոկոլ)</li>
    <li>Էկոհամակարգի բազմազանություն և համատեղելիություն</li>
    <li>Ժամանակակից և էլեգանտ դիզայն</li>
</ul>
<img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800" alt="LifeSmart Products">
<h2>Ինչու՞ ընտրել LifeSmart</h2>
<p>Մատչելիություն, որակ և անվտանգություն: (Այս հատվածը ժամանակավոր տեքստ է):</p>
"""
generate_blog_html("blog-lifesmart.html", "Ինչու է LifeSmart-ը Խելացի Տան Առաջատար Բրենդը", "08 ԱՊՐ 2024", "https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&q=80&w=1200", content_3)

# 4. blog-security.html
content_4 = """
<img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=800" alt="Security">
<p>Ինչպե՞ս պաշտպանել ձեր բնակարանը ժամանակակից սարքավորումների միջոցով: Տեսախցիկներ, սենսորներ և ահազանգման համակարգերի ճիշտ ընտրություն:</p>
<h2>Անվտանգության Հիմնական Բաղադրիչները</h2>
<p>Խելացի անվտանգությունը ներառում է մի քանի շերտեր: (Այս հատվածը ժամանակավոր տեքստ է):</p>
<ul>
    <li>Խելացի տեսախցիկներ և домофон-ներ</li>
    <li>Շարժման, դռան և պատուհանի բացման սենսորներ</li>
    <li>Գազի և ջրի արտահոսքի կանխարգելման համակարգեր</li>
</ul>
<img src="https://images.unsplash.com/photo-1555940280-49655e8842e1?auto=format&fit=crop&q=80&w=800" alt="CCTV Cameras">
<h2>Վերահսկողություն ամենուրեք</h2>
<p>Ստացեք ծանուցումներ ձեր հեռախոսին աշխարհի ցանկացած կետից: (Այս հատվածը ժամանակավոր տեքստ է):</p>
"""
generate_blog_html("blog-security.html", "Խելացի Տան անվտանգության Համակարգեր", "02 ԱՊՐ 2024", "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1200", content_4)

print("Created all 4 blog post HTML files!")
