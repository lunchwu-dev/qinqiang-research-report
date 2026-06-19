#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将秦腔深度研究报告从Markdown转换为图文并茂的HTML
"""

import re
import os

# 读取Markdown文件
input_file = r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\秦腔深度研究报告_最终版.md"
output_file = r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\秦腔深度研究报告.html"

# 秦腔相关图片URL（从百度百科等开放资源获取）
images = [
    "https://baike.baidu.com/pic/%E7%A7%A6%E8%85%94/596/0/0ef21124570f6700c9955978?fr=lemma&fromModule=lemma_content-image",
    "https://baike.baidu.com/pic/%E7%A7%A6%E8%85%94/596/0/95afee1ff9b193c6e1fe0b69?fr=lemma&fromModule=lemma_content-image",
    "https://baike.baidu.com/pic/%E7%A7%A6%E8%85%94/596/0/3b6833f55dec5f7bbc3109d6?fr=lemma&fromModule=lemma_content-image",
    "https://baike.baidu.com/pic/%E7%A7%A6%E8%85%94/596/0/5327ce160285152b962b4371?fr=lemma&fromModule=lemma_content-image",
    "https://baike.baidu.com/pic/%E7%A7%A6%E8%85%94/596/0/7aad4ae7700a0965b8382003?fr=lemma&fromModule=lemma_content-image",
    "https://baike.baidu.com/pic/%E7%A7%A6%E8%85%94/596/0/d8b8c92af2c98c09d42af192?fr=lemma&fromModule=lemma_content-image"
]

# HTML模板（包含CSS样式）
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>八百里秦川三千万子民：秦腔深度研究报告</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Microsoft YaHei", "Segoe UI", sans-serif;
            line-height: 1.8;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            padding: 40px;
        }
        
        h1 {
            color: #8B0000;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
            border-bottom: 3px solid #8B0000;
            padding-bottom: 20px;
        }
        
        h2 {
            color: #B22222;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 2em;
            border-left: 5px solid #B22222;
            padding-left: 15px;
        }
        
        h3 {
            color: #CD5C5C;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.5em;
        }
        
        h4 {
            color: #D2691E;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        p {
            margin-bottom: 15px;
            text-indent: 2em;
        }
        
        .image-container {
            text-align: center;
            margin: 30px 0;
        }
        
        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .image-caption {
            font-size: 0.9em;
            color: #666;
            margin-top: 10px;
            font-style: italic;
        }
        
        ul, ol {
            margin-left: 40px;
            margin-bottom: 15px;
        }
        
        li {
            margin-bottom: 10px;
        }
        
        a {
            color: #8B0000;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        hr {
            border: none;
            border-top: 2px solid #ddd;
            margin: 40px 0;
        }
        
        .toc {
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin: 30px 0;
        }
        
        .toc h2 {
            margin-top: 0;
            font-size: 1.5em;
        }
        
        .toc ul {
            list-style: none;
            margin-left: 0;
        }
        
        .toc li {
            margin-bottom: 8px;
        }
        
        @media print {
            body {
                background: white;
            }
            .container {
                box-shadow: none;
            }
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 1.8em;
            }
            h2 {
                font-size: 1.5em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

def markdown_to_html(md_text, images):
    """
    将Markdown转换为HTML（简化版）
    """
    html = md_text
    
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
    
    # 段落处理（简化处理）
    paragraphs = html.split('\n\n')
    processed = []
    img_index = 0
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
            
        # 如果段落不是标题、列表、分隔线，则包裹为<p>
        if not re.match(r'^<(h[1-4]|li|hr|ul|ol|div)', para):
            para = '<p>' + para + '</p>'
        
        # 每3个段落插入一张图片（如果还有图片的话）
        if img_index < len(images) and processed.count('<img') < len(images):
            if len(processed) % 3 == 0 and img_index < len(images):
                img_html = f'''
                <div class="image-container">
                    <img src="{images[img_index]}" alt="秦腔艺术图片">
                    <div class="image-caption">秦腔艺术（图片来源：百度百科）</div>
                </div>
                '''
                processed.append(img_html)
                img_index += 1
        
        processed.append(para)
    
    return '\n'.join(processed)

# 主程序
print("开始转换Markdown到HTML...")

# 读取Markdown文件
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    print(f"成功读取Markdown文件：{len(md_content)} 字符")
except Exception as e:
    print(f"读取文件失败：{e}")
    exit(1)

# 转换
html_content = markdown_to_html(md_content, images)

# 插入到模板
full_html = html_template.replace('{content}', html_content)

# 写入文件
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"成功生成HTML文件：{output_file}")
    print(f"文件大小：{os.path.getsize(output_file)} 字节")
except Exception as e:
    print(f"写入文件失败：{e}")
    exit(1)

print("转换完成！")
