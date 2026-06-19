#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成秦腔研究报告章节HTML页面
"""
import os
import re

base_dir = r"C:/Users/uuzz/WorkBuddy/2026-06-19-11-40-37"

# 章节配置
chapters = [
    {"num": 0, "file": "序章_从主角说开去.md", "title": "序章：从《主角》说开去", "subtitle": "当电视剧点燃秦腔热情", "image": "chapter0.jpg"},
    {"num": 1, "file": "第一章_千年文脉_秦腔的历史长河.md", "title": "第一章：千年文脉", "subtitle": "秦腔的历史长河", "image": "chapter1.jpg"},
    {"num": 2, "file": "第二章_艺术密码_秦腔的魅力何在.md", "title": "第二章：艺术密码", "subtitle": "秦腔的魅力何在", "image": "chapter2.jpg"},
    {"num": 3, "file": "第三章_名角风流_秦腔历史上的关键人物.md", "title": "第三章：名角风流", "subtitle": "秦腔历史上的关键人物", "image": "chapter3.jpg"},
    {"num": 4, "file": "chapter4_qinqiang_inheritance_innovation.md", "title": "第四章：戏台上下", "subtitle": "秦腔的传承与创新", "image": "chapter4.jpg"},
    {"num": 5, "file": "第五章_秦腔入门完全指南_修订版.md", "title": "第五章：如何"入坑"秦腔？", "subtitle": "新手完全指南", "image": "chapter5.jpg"},
    {"num": 6, "file": "尾声_秦腔的未来.md", "title": "尾声：秦腔的未来", "subtitle": "守正与创新", "image": "chapter6.jpg"},
]

def md_to_html(md_file):
    """简单的Markdown到HTML转换器"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except Exception as e:
        return f"<p>Error reading file: {e}</p>"
    
    html = md_content
    
    # 替换标题
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # 替换分隔线
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    
    # 替换粗体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # 替换列表
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # 替换链接
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" target="_blank">\1</a>', html)
    
    # 段落处理
    paragraphs = html.split('\n\n')
    processed = []
    in_list = False
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            if in_list:
                processed.append('</ul>')
                in_list = False
            processed.append('<p>&nbsp;</p>')
            continue
        
        # 检查是否是列表
        if para.startswith('<li>'):
            if not in_list:
                processed.append('<ul>')
                in_list = True
        elif in_list:
            processed.append('</ul>')
            in_list = False
        
        # 如果不是标题、列表、分隔线，则包裹为<p>
        if not re.match(r'^<(h[1-4]|li|hr|ul|ol)', para):
            para = '<p>' + para + '</p>'
        
        processed.append(para)
    
    if in_list:
        processed.append('</ul>')
    
    return '\n'.join(processed)

def create_chapter_html(chapter, all_chapters):
    """创建章节HTML页面"""
    idx = chapter["num"]
    md_file = os.path.join(base_dir, chapter["file"])
    
    # 转换Markdown内容
    content_html = md_to_html(md_file)
    
    # 确定上一章和下一章
    prev_chapter = None
    next_chapter = None
    if idx > 0:
        prev_chapter = f"chapter{idx-1}.html"
    if idx < len(all_chapters) - 1:
        next_chapter = f"chapter{idx+1}.html"
    
    # HTML模板
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter['title']} - 秦腔深度研究报告</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: "SimSun", "STSong", "Microsoft YaHei", serif;
            background-color: #F5F0E8;
            color: #1a1a1a;
            line-height: 1.8;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .chapter-header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 3px double #C41E3A;
        }}
        
        .chapter-header h1 {{
            color: #C41E3A;
            font-size: 2.2em;
            margin-bottom: 10px;
        }}
        
        .chapter-subtitle {{
            color: #2C5F8A;
            font-size: 1.2em;
            font-style: italic;
        }}
        
        .chapter-content {{
            font-size: 1.1em;
            line-height: 2;
        }}
        
        .chapter-content h2 {{
            color: #C41E3A;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 1.8em;
            border-left: 5px solid #D4A843;
            padding-left: 15px;
        }}
        
        .chapter-content h3 {{
            color: #2C5F8A;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.4em;
        }}
        
        .chapter-content p {{
            margin-bottom: 20px;
            text-indent: 2em;
            text-align: justify;
        }}
        
        .image-container {{
            text-align: center;
            margin: 30px 0;
        }}
        
        .image-container img {{
            max-width: 100%;
            height: auto;
            border: 3px solid #D4A843;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        
        .image-caption {{
            font-size: 0.9em;
            color: #666;
            margin-top: 10px;
            font-style: italic;
        }}
        
        .nav-buttons {{
            display: flex;
            justify-content: space-between;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 2px solid #D4A843;
        }}
        
        .nav-btn {{
            padding: 12px 30px;
            background: #C41E3A;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s;
            font-family: "SimSun", serif;
            text-decoration: none;
            display: inline-block;
        }}
        
        .nav-btn:hover {{
            background: #2C5F8A;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        
        .nav-btn.home {{
            background: #D4A843;
            color: #1a1a1a;
        }}
        
        .nav-btn.home:hover {{
            background: #C41E3A;
            color: white;
        }}
        
        @media (max-width: 768px) {{
            .nav-buttons {{
                flex-direction: column;
                gap: 10px;
            }}
            
            .nav-btn {{
                width: 100%;
                text-align: center;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="chapter-header">
            <h1>{chapter['title']}</h1>
            <p class="chapter-subtitle">{chapter['subtitle']}</p>
        </div>
        
        <div class="chapter-content">
            {content_html}
        </div>
        
        <div class="image-container">
            <img src="images/{chapter['image']}" alt="{chapter['title']}">
            <div class="image-caption">（图片来源：Pixabay 免费素材）</div>
        </div>
        
        <div class="nav-buttons">
            <a href="index.html" class="nav-btn home">← 返回首页</a>
            {f'<a href="{prev_chapter}" class="nav-btn">← 上一章</a>' if prev_chapter else ''}
            {f'<a href="{next_chapter}" class="nav-btn">下一章 →</a>' if next_chapter else ''}
        </div>
    </div>
</body>
</html>"""
    
    return html

print("开始生成章节页面...")

for i, ch in enumerate(chapters):
    html = create_chapter_html(ch, chapters)
    output_file = os.path.join(base_dir, f"chapter{i}.html")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ 已生成: chapter{i}.html")
    except Exception as e:
        print(f"✗ 生成失败 chapter{i}.html: {e}")

print("\n所有章节页面生成完成！")
