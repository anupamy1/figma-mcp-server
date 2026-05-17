class CodeGenerator:
    @staticmethod
    def generate_basic_html():
        html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Generated Landing Page</title>
</head>
<body>
    <h1>Basic generated HTML is working.</h1>
    <p>Use /generate-html-v2 for the improved version.</p>
</body>
</html>
"""
        return html_code

    @staticmethod
    def generate_landing_page_html_v2(image_urls):
        hero_image = image_urls.get("1:1495", "")
        card_image_1 = image_urls.get("1:1499", "")
        card_image_2 = image_urls.get("1:1504", "")
        card_image_3 = image_urls.get("1:1509", "")
        side_image = image_urls.get("1:1513", "")
        bottom_image_1 = image_urls.get("1:1517", "")
        bottom_image_2 = image_urls.get("1:1522", "")
        avatar_1 = image_urls.get("1:1422", "")
        avatar_2 = image_urls.get("1:1429", "")
        avatar_3 = image_urls.get("1:1436", "")

        html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Generated Landing Page V2</title>
    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #ffffff;
            color: #000000;
        }}

        .page {{
            width: 100%;
            overflow-x: hidden;
        }}

        .container {{
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
        }}

        .navbar {{
            height: 164px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .site-name {{
            font-size: 24px;
            font-weight: 500;
        }}

        .nav-right {{
            display: flex;
            align-items: center;
            gap: 48px;
            font-size: 20px;
        }}

        .button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: #000000;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 16px 28px;
            font-size: 20px;
            text-decoration: none;
            min-height: 60px;
            cursor: pointer;
        }}

        .button.secondary {{
            background: #e6e6e6;
            color: #000000;
        }}

        .hero {{
            padding-top: 48px;
            padding-bottom: 80px;
        }}

        .hero-copy {{
            max-width: 844px;
        }}

        .hero h1 {{
            font-size: 64px;
            line-height: 1.15;
            margin: 0 0 24px;
            font-weight: 700;
            letter-spacing: -2px;
        }}

        .hero p {{
            font-size: 24px;
            line-height: 1.5;
            margin: 0 0 32px;
            color: #555555;
            max-width: 840px;
        }}

        .hero-image {{
            width: 100%;
            height: 640px;
            object-fit: cover;
            border-radius: 8px;
            margin-top: 80px;
            display: block;
        }}

        .section {{
            padding: 80px 0;
        }}

        .section h2 {{
            font-size: 48px;
            line-height: 1.2;
            margin: 0 0 56px;
            font-weight: 700;
            letter-spacing: -1px;
        }}

        .cards-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
        }}

        .card img {{
            width: 100%;
            height: 405px;
            object-fit: cover;
            border-radius: 8px;
            display: block;
            margin-bottom: 24px;
        }}

        .card h3 {{
            font-size: 24px;
            margin: 0 0 12px;
            font-weight: 700;
        }}

        .card p {{
            font-size: 20px;
            line-height: 1.45;
            margin: 0;
            color: #777777;
        }}

        .text-image-section {{
            display: grid;
            grid-template-columns: 516px 1fr;
            gap: 120px;
            align-items: start;
            padding: 80px 0;
        }}

        .text-column h2 {{
            font-size: 48px;
            line-height: 1.2;
            margin: 0 0 56px;
            font-weight: 700;
        }}

        .text-block {{
            margin-bottom: 40px;
        }}

        .text-block h3 {{
            font-size: 24px;
            margin: 0 0 16px;
        }}

        .text-block p {{
            font-size: 22px;
            line-height: 1.45;
            margin: 0;
            color: #777777;
        }}

        .button-row {{
            display: flex;
            gap: 16px;
            margin-top: 40px;
        }}

        .side-image {{
            width: 704px;
            height: 704px;
            object-fit: cover;
            border-radius: 8px;
            display: block;
        }}

        .cards-2 {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 32px;
        }}

        .cards-2 .card img {{
            height: 341px;
        }}

        .testimonial-section {{
            padding: 80px 0;
        }}

        .testimonial-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
        }}

        .testimonial {{
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 32px;
            min-height: 198px;
        }}

        .testimonial quote {{
            display: block;
            font-size: 24px;
            font-weight: 500;
            margin-bottom: 40px;
        }}

        .avatar-row {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .avatar {{
            width: 45px;
            height: 45px;
            object-fit: cover;
            border-radius: 50%;
            background: #dddddd;
        }}

        .avatar-name {{
            font-size: 18px;
            font-weight: 700;
        }}

        .avatar-desc {{
            font-size: 18px;
            color: #777777;
            margin-top: 4px;
        }}

        .cta-section {{
            background: #f7f7f7;
            padding: 80px 0;
        }}

        .cta-inner {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .cta-inner h2 {{
            font-size: 48px;
            margin: 0;
        }}

        .footer {{
            padding: 56px 0 80px;
            border-top: 1px solid #e0e0e0;
        }}

        .footer-grid {{
            display: grid;
            grid-template-columns: 1fr 187px 187px 187px;
            gap: 32px;
        }}

        .footer-logo {{
            font-size: 24px;
            font-weight: 500;
        }}

        .footer-col h4 {{
            font-size: 16px;
            margin: 0 0 24px;
        }}

        .footer-col p {{
            font-size: 16px;
            color: #555555;
            margin: 0 0 24px;
        }}

        @media (max-width: 900px) {{
            .container {{
                padding: 0 24px;
            }}

            .navbar {{
                height: auto;
                padding: 32px 0;
                align-items: flex-start;
            }}

            .nav-right {{
                gap: 20px;
                flex-wrap: wrap;
                justify-content: flex-end;
            }}

            .hero h1 {{
                font-size: 44px;
            }}

            .hero p {{
                font-size: 20px;
            }}

            .hero-image {{
                height: 360px;
            }}

            .cards-3,
            .cards-2,
            .testimonial-grid,
            .text-image-section,
            .footer-grid {{
                grid-template-columns: 1fr;
            }}

            .side-image {{
                width: 100%;
                height: auto;
            }}

            .cta-inner {{
                flex-direction: column;
                align-items: flex-start;
                gap: 24px;
            }}
        }}
    </style>
</head>
<body>
    <div class="page">

        <header class="container navbar">
            <div class="site-name">Site name</div>

            <nav class="nav-right">
                <span>Page</span>
                <span>Page</span>
                <span>Page</span>
                <a href="#" class="button">Button</a>
            </nav>
        </header>

        <main>
            <section class="container hero">
                <div class="hero-copy">
                    <h1>Landing page title</h1>
                    <p>Subheading that sets up context, shares more info about the website, or generally gets people psyched to keep scrolling.</p>
                    <a href="#" class="button">Button</a>
                </div>

                <img class="hero-image" src="{hero_image}" alt="Hero Image">
            </section>

            <section class="container section">
                <h2>Section heading</h2>

                <div class="cards-3">
                    <div class="card">
                        <img src="{card_image_1}" alt="Card Image 1">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to add more to the subheading.</p>
                    </div>

                    <div class="card">
                        <img src="{card_image_2}" alt="Card Image 2">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to expand on the main point.</p>
                    </div>

                    <div class="card">
                        <img src="{card_image_3}" alt="Card Image 3">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to share more.</p>
                    </div>
                </div>
            </section>

            <section class="container text-image-section">
                <div class="text-column">
                    <h2>Section heading</h2>

                    <div class="text-block">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to expand on the main point.</p>
                    </div>

                    <div class="text-block">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes.</p>
                    </div>

                    <div class="text-block">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to add more to the main point. It provides details, explanations, and context.</p>
                    </div>

                    <div class="button-row">
                        <a href="#" class="button">Button</a>
                        <a href="#" class="button secondary">Secondary button</a>
                    </div>
                </div>

                <img class="side-image" src="{side_image}" alt="Large Image">
            </section>

            <section class="container section">
                <h2>Section heading</h2>

                <div class="cards-2">
                    <div class="card">
                        <img src="{bottom_image_1}" alt="Bottom Image 1">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to add more to the subheading.</p>
                    </div>

                    <div class="card">
                        <img src="{bottom_image_2}" alt="Bottom Image 2">
                        <h3>Subheading</h3>
                        <p>Body text for whatever you’d like to expand on the main point.</p>
                    </div>
                </div>
            </section>

            <section class="container testimonial-section">
                <h2>Section heading</h2>

                <div class="testimonial-grid">
                    <div class="testimonial">
                        <quote>“A terrific piece of praise”</quote>
                        <div class="avatar-row">
                            <img class="avatar" src="{avatar_1}" alt="Avatar 1">
                            <div>
                                <div class="avatar-name">Name</div>
                                <div class="avatar-desc">Description</div>
                            </div>
                        </div>
                    </div>

                    <div class="testimonial">
                        <quote>“A fantastic bit of feedback”</quote>
                        <div class="avatar-row">
                            <img class="avatar" src="{avatar_2}" alt="Avatar 2">
                            <div>
                                <div class="avatar-name">Name</div>
                                <div class="avatar-desc">Description</div>
                            </div>
                        </div>
                    </div>

                    <div class="testimonial">
                        <quote>“A genuinely glowing review”</quote>
                        <div class="avatar-row">
                            <img class="avatar" src="{avatar_3}" alt="Avatar 3">
                            <div>
                                <div class="avatar-name">Name</div>
                                <div class="avatar-desc">Description</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section class="cta-section">
                <div class="container cta-inner">
                    <h2>Section heading</h2>

                    <div class="button-row">
                        <a href="#" class="button">Button</a>
                        <a href="#" class="button secondary">Secondary button</a>
                    </div>
                </div>
            </section>
        </main>

        <footer class="container footer">
            <div class="footer-grid">
                <div class="footer-logo">Site name</div>

                <div class="footer-col">
                    <h4>Topic</h4>
                    <p>Page</p>
                    <p>Page</p>
                    <p>Page</p>
                </div>

                <div class="footer-col">
                    <h4>Topic</h4>
                    <p>Page</p>
                    <p>Page</p>
                    <p>Page</p>
                </div>

                <div class="footer-col">
                    <h4>Topic</h4>
                    <p>Page</p>
                    <p>Page</p>
                    <p>Page</p>
                </div>
            </div>
        </footer>

    </div>
</body>
</html>
"""
        return html_code