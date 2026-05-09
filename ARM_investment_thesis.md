# ARM 投資分析框架與研究備忘錄 (Investment Thesis & Framework)

此文件由經理人與投資人共同維護，旨在追蹤與分析 ARM (安謀) 的長期投資價值。

## 👤 投資人輪廓與操作設定
*   **目標預期**：長期持有 3~5 年，追求翻倍成長 (CAGR 需達 15%~25%)。
*   **核心優勢 (Edge)**：半導體與晶片設計 (Semi / Chip Design) 背景。對技術底層、架構轉換、PPA 優勢具備高敏銳度。
*   **風險控管**：可承受 50% 級別的最大回撤 (Max Drawdown)，著眼於長期基本面。
*   **時間投入**：每週約 10 小時進行質化與量化研究。
*   **投資邏輯**：
    1.  產品線是否成功打入更大的 TAM (例如 Data Center、Auto)？
    2.  利潤率 (尤其是營業利益率 Operating Margin) 是否合理且具備擴張性？
    3.  管理層是否誠信正派，指引是否務實？
    4.  技術護城河與生態系壁壘是否堅固 (防禦 RISC-V 等潛在威脅)？

---

## 🔬 研究階段與追蹤指標清單

### 階段一：驗證「護城河」與「管理層品質」
*   **核心素材**：`Transcript.md` (電話會議逐字稿)
*   **追蹤重點**：
    *   **RISC-V 競爭動態**：管理層在 Q&A 環節中對於開源架構競爭的回應。關注軟體相容性、轉移成本等實質壁壘數據。
    *   **管理層指引 (Guidance)**：在消費性電子(手機/PC)逆風或庫存調整期，管理層給出的財測是否務實不過度樂觀。

### 階段二：追蹤「新市場 TAM」與「產品滲透率」
*   **核心素材**：`Letter.md` (致股東信) & `Presentation.md` (法說會簡報)
*   **追蹤重點**：
    *   **Data Center / Cloud AI**：追蹤各大 CSP (Nvidia Grace, AWS Graviton, Microsoft Cobalt, Google Axion) 採用 ARM 架構的進度與市佔率變化。
    *   **Edge AI & PC**：Windows on ARM (WOA) 的市佔率爬坡速度。
    *   **Automotive (車用)**：軟體定義汽車 (SDV) 趨勢下，ARM 架構在自駕晶片與數位座艙的滲透情況。

### 階段三：財務數字轉換與「爆擊」催化劑 (Catalysts)
*   **核心素材**：透過 Python 腳本量化提取各季度財報數據。
*   **追蹤重點**：
    *   **營收結構 (Revenue Mix)**：權利金 (Royalty) 與 授權金 (Licensing) 的比例變化。授權金是領先指標，權利金是終極現金流。
    *   **v9 架構滲透率**：v9 帶來比 v8 翻倍的權利金費率 (Royalty Rate)。追蹤 v9 佔整體權利金收入的百分比。
    *   **CSS (Compute Subsystems) 採用數**：CSS 解決了客戶晶片設計複雜度的痛點，能大幅提高 ARM 獲取的單片價值 (Value Capture)。追蹤 CSS 授權客戶與量產晶片數量。
    *   **營業槓桿 (Operating Leverage)**：由於 ARM 毛利率 (Gross Margin) 已極高，需重點追蹤「營業利益率 (Operating Margin)」，確保營收增長幅度大於 R&D 等營業費用增幅。

### 階段四：SaaS/高估值股專屬的「三大防線指標」
*   **Rule of 40 (40 法則) 總分**：追蹤「營收成長率 + Non-GAAP 營業利益率」是否維持在 40% (甚至 50%) 以上。這是支撐其超高本益比 (P/E) 的絕對地基。
*   **ACV (年化合約價值) 成長率**：追蹤客戶未來的承諾訂單金額。這是預判未來授權與權利金營收是否能持續暴增的最強「領先指標」。
*   **Data Center (雲端運算) 市佔率與佔比**：管理層承諾 Data Center 將在 3 年內超越手機板塊。必須追蹤每季 Data Center 營收是否維持翻倍增長 (Triple-digits YoY)，以及 CPU 在雲端市場的市佔率擴張。

---

## 🛠️ 待辦事項 (Action Items) & 開發計畫
- [ ] **Data Extraction Script**：撰寫 Python 腳本，自動從 24Q2 ~ 26Q3 的 Markdown 檔案中提取 `Total Revenue`, `Royalty/Licensing ratio`, `Operating Margin`, `v9 adoption %` 等關鍵指標，並輸出為 CSV。
- [ ] **質化重點摘要**：針對最新一季 (例如 26Q3)，使用 LLM 對 Transcript 進行關鍵字掃描，總結分析師針對 Data Center 與 RISC-V 的提問與回答。
- [ ] **圖表視覺化**：將量化數據轉換為趨勢圖，視覺化呈現 v9 滲透率與 Royalty 營收的相關性。
