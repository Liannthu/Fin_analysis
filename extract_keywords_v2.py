import os

def extract_insights(file_path, concept_keywords):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    
    paragraphs = content.split('\n\n')
    
    results = {concept: [] for concept in concept_keywords.keys()}
    
    for i, p in enumerate(paragraphs):
        p_lower = p.lower()
        for concept, kw_list in concept_keywords.items():
            for kw in kw_list:
                if kw.lower() in p_lower:
                    speaker = paragraphs[i-1].strip() if i > 0 else ""
                    if len(speaker) > 100:
                        speaker = "[段落接續]"
                    
                    clean_p = p.replace('\n', ' ').strip()
                    clean_speaker = speaker.replace('\n', ' ').strip()
                    
                    hit_entry = f"👤 {clean_speaker}\n💬 [觸發字: '{kw}'] {clean_p}"
                    if hit_entry not in results[concept]:
                        results[concept].append(hit_entry)
                    break # 該概念中只要有一個關鍵字命中，就不用重複加入同一段落
                
    return results

file_path = r"f:\AI\fin_analysis\ARM\26Q3\26Q3_Transcript.md"
concept_keywords = {
    "RISC-V & 競爭": ["risc-v", "open source", "isa", "alternative", "competition", "compete", "x86"],
    "高通與法律訴訟": ["qualcomm", "nuvia", "litigation", "lawsuit", "legal", "dispute"],
    "雲端與資料中心": ["data center", "cloud", "hyperscaler", "server", "aws", "graviton", "grace"],
    "車用與實體 AI": ["auto", "vehicle", "adas", "rivian", "robotics"]
}

print(f"開始用擴展關鍵字庫分析 {file_path} ...")
results = extract_insights(file_path, concept_keywords)

out_file = r"f:\AI\fin_analysis\26Q3_keyword_analysis_v2.txt"
with open(out_file, 'w', encoding='utf-8') as out:
    for concept, hits in results.items():
        out.write(f"=========================================\n")
        out.write(f"🔍 概念主題: {concept} (命中 {len(hits)} 段落)\n")
        out.write(f"=========================================\n\n")
        if not hits:
            out.write("未找到相關提及。\n\n")
        else:
            for hit in hits:
                out.write(f"{hit}\n\n")

print("Analysis complete. See 26Q3_keyword_analysis_v2.txt")
