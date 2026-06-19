import os

# Define file paths
base_dir = r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37"

# Files to merge in order
files_to_merge = [
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\序章_从主角说开去.md",
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\第一章_千年文脉_秦腔的历史长河.md",
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\第二章_艺术密码_秦腔的魅力何在.md",
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\第三章_名角风流_秦腔历史上的关键人物.md",
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\chapter4_qinqiang_inheritance_innovation.md",
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\第五章_秦腔入门完全指南_修订版.md",
    r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\尾声_秦腔的未来.md"
]

# Output file
output_file = r"C:\Users\uuzz\WorkBuddy\2026-06-19-11-40-37\秦腔深度研究报告_最终版.md"

# Read and merge all files
with open(output_file, 'w', encoding='utf-8') as outf:
    # Write title
    outf.write("# 八百里秦川三千万子民：秦腔深度研究报告\n")
    outf.write("**副标题：从《主角》出发，探寻陕西戏曲的千年文脉与时代新声**\n\n")
    outf.write("---\n\n")
    
    # Process each file
    for i, file_path in enumerate(files_to_merge):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as inf:
                content = inf.read()
                # Remove the title from chapters (keep only body)
                lines = content.split('\n')
                # Skip the first line if it's a title (starts with # )
                start_idx = 0
                if lines and lines[0].startswith('#'):
                    start_idx = 1
                # Write content
                outf.write('\n'.join(lines[start_idx:]))
                outf.write("\n\n---\n\n")
            print(f"Merged: {os.path.basename(file_path)}")
        else:
            print(f"File not found: {file_path}")
    
    # Add references section
    outf.write("\n\n## 参考文献\n\n")
    outf.write("本报告引用了以下主要信息来源：\n\n")

print("Report merged successfully!")
