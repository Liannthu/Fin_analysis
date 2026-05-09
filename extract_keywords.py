import os

def extract_insights(file_path, keywords):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    
    # 將文本照雙換行切分成段落
    paragraphs = content.split('\n\n')
    
    results = {kw: [] for kw in keywords}
    
    for i, p in enumerate(paragraphs):
        p_lower = p.lower()
        for kw in keywords:
            if kw.lower() in p_lower:
                # 試圖抓取上一段，通常是發言者的名字 (例如 "Rene Haas:" 或分析師名字)
                speaker = paragraphs[i-1].strip() if i > 0 else ""
                # 如果上一段太長，可能不是人名，就省略
                if len(speaker) > 100:
                    speaker = "[段落接續]"
                
                # 整理文字格式，把段落內的單換行拿掉，方便閱讀
                clean_p = p.replace('\n', ' ').strip()
                clean_speaker = speaker.replace('\n', ' ').strip()
                
                results[kw].append(f"👤 {clean_speaker}\n💬 {clean_p}")
                
    return results

file_path = r"f:\AI\fin_analysis\ARM\26Q3\26Q3_Transcript.md"
keywords = ["risc-v", "qualcomm", "data center", "auto"]

print(f"開始分析 {file_path} ...")
results = extract_insights(file_path, keywords)

out_file = r"f:\AI\fin_analysis\26Q3_keyword_analysis.txt"
with open(out_file, 'w', encoding='utf-8') as out:
    for kw, hits in results.items():
        out.write(f"=========================================\n")
        out.write(f"🔍 關鍵字: {kw.upper()} (共找到 {len(hits)} 處)\n")
        out.write(f"=========================================\n\n")
        if not hits:
            out.write("未找到相關提及。\n\n")
        else:
            for hit in hits:
                out.write(f"{hit}\n\n")

print(f"✅ 分析完成！結果已儲存至 {out_file}")
