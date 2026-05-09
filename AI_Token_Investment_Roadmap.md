# AI Token Investment Roadmap
*研究日期：2026年5月 | 實時數據 + SemiAnalysis 文章綜合*

---

## 核心投資假設

**企業 AI coding 採用（Claude Code、GitHub Copilot、Cursor）正在產生大量 token 消費，這件事在財報上還沒完全體現。當財報確認後，誰最直接受益？**

```
企業簽約用 AI coding
    ↓ (1-2季 ramp up)
Azure / AWS token 用量飆升
    ↓ (revenue recognition lag)
雲端 AI 收入加速
    ↓ (capacity 不夠了)
新一輪 GPU / Memory / Power 採購
```

---

## 假設驗證（全部確認）

| 假設 | 數據確認 | 狀態 |
|------|---------|------|
| 企業 AI coding token 量爆炸 | Anthropic ARR：$9B → $30B（4個月）；Claude Code $2.5B run rate | ✅ 強烈確認 |
| GPU 供應短缺/價格上漲 | H100 +40%，B200 backlog 3.6M units，8-9月前全部訂滿 | ✅ 強烈確認 |
| 記憶體價格飆升 | Server DRAM +60-70%，HBM 2026全年售完 | ✅ 超出預期 |
| Azure AI 收入加速 | $37B run rate，+123% YoY（Q3 FY2026） | ✅ 強烈確認 |
| Anthropic ARR 暴增 | $9B → $14B → $19B → $30B（2個月內） | ✅ 超出預期 |
| 價值從硬體→模型廠 | 推理佔 AI 雲端支出 55%，Anthropic 毛利 38%→70%+ | ✅ 確認 |
| Broadcom custom ASIC 受益 | AI 收入 +106%，$73B backlog | ✅ 強烈確認 |

---

## 企業 AI Coding 爆炸數據

### Anthropic ARR 增長軌跡

```
Dec 2024:  $1B ARR
Sept 2025: $7B ARR
Dec 2025:  $9B ARR
Feb 2026:  $14B ARR  (+$5B 單月)
Mar 2026:  $19B ARR  (+$5B 單月)
Apr 2026:  $30B ARR  ← 超過 OpenAI
```

> 15個月內從 $1B 到 $30B，歷史上最快速成長的公司

**Claude Code 企業數據：**
- Run rate：**>$2.5B**（2025年5月公開後6個月）
- 企業客戶：**300,000+ 企業**，Fortune 100 的 70%（Fortune 10 中的 8 家）
- **500+ 企業年花費超 $1M**
- Deloitte 案例：**470,000 名員工部署**
- Pragmatic Engineer 調查（15,000 位開發者，2026年2月）：Claude Code 最常用 AI coding 工具，46% 「最愛」
- **73% 的工程團隊每日使用 AI coding 工具**（2025年為 41%）

**GitHub Copilot：**
- 付費用戶：**4.7M**（YoY +75%）
- 企業組織：**140,000 個**，覆蓋 ~90% Fortune 100

---

## 產業鏈分層與商業模式分析

### Tier 1A：模型開發者（最高利潤，私人公司）

| 公司 | ARR | 狀態 |
|------|-----|------|
| Anthropic | **$30B**（Apr 2026） | 私人，無法直接投資 |
| OpenAI | ~$10B | 私人，無法直接投資 |

> 這層捕獲最高利潤（毛利 70%+），但都是私人公司。

---

### Tier 1B：Token 平台販賣者（直接可投資）

這層的商業模式：**買 GPU 算力（批發）→ 加上模型 → 賣 token（零售）**，賺取模型加值的利潤。

#### Microsoft Azure AI（MSFT）✅ 你已持有

**Q3 FY2026 財報（2026/4/29，最新）：**

| 指標 | 數字 | YoY 成長 |
|------|------|---------|
| Azure + 雲端服務 | — | **+40%** |
| AI 年化收入（全口徑）| **$37B run rate** | **+123%** |
| Microsoft Cloud | $54.5B | +29% |
| 總收入 | $82.9B | +18% |
| Capex（單季）| $31.9B | +49% |
| **2026全年 Capex 指引** | **$190B** | +61% |

**優勢：**
- 過去：OpenAI 模型的**獨家**商業合作夥伴
- GitHub Copilot：4.7M 付費用戶，140K 企業組織
- Copilot for M365：$30/user/month × 大量企業合約
- 企業 stickiness 最強（已有 M365 合約基礎）

**最新重要變化（2026/4/28）：**
> OpenAI 結束與 Microsoft 的獨家協議，模型現在也上架 AWS Bedrock。MSFT 仍是最深整合的合作夥伴，但獨占優勢縮小。

**下一棒尚未定價：** Copilot 在 140K 組織內滲透率仍低，企業從試點 → 全面部署 = $37B → $70B+ 路徑。

---

#### Amazon AWS Bedrock（AMZN）

**Q1 FY2026 數據：**
- AWS AI run rate：**$15B**（從上市 3 年累計）
- Bedrock token 量：**Q1 2026 > 過去所有年份總和**
- Q1 QoQ 客戶支出成長：**+170%**
- Fortune 100 使用 Bedrock：**~80%**
- 目標：「成為全球最大的 inference engine」
- Trainium 自研晶片：**50%+ 的 Bedrock tokens 跑在 Amazon 自家晶片**

**與 MSFT 的關鍵差異：**

| 維度 | Microsoft | Amazon |
|------|-----------|--------|
| 模型策略 | **OpenAI 獨家**（過去）→ 現在非獨家 | **多模型市場**（Claude、Llama、Nova）|
| 自研模型 | 無（依賴 OpenAI）| Nova 系列（自研）|
| Coding 優勢 | GitHub Copilot（市占第一）| CodeWhisperer（落後）|
| 企業 stickiness | M365 + Azure 整合（極高）| 已有 AWS 帳戶的企業採用（高）|
| AI 收入透明度 | 明確揭露 AI run rate | 不分開揭露 Bedrock 收入 |
| 晶片戰略 | 依賴 NVIDIA | 自研 Trainium + Inferentia |

**為何 Amazon 是 Tier 1 但被低估：**
AWS 雲端市占 30%+（>Azure 的 22%），企業 AWS 帳戶數量最多。AI 貨幣化在加速但 **尚未充分揭露**。若 Bedrock 開始分開揭露收入，會是重要催化劑。

#### Google Cloud Vertex AI（GOOGL）

- Gemini 模型完全自研 → 最佳 inference 成本結構（TPU vs GPU）
- GCP AI 收入成長 28-35% YoY
- 優勢：自家 TPU 成本比買 NVIDIA GPU 便宜 50-70%，可以最積極定價

---

### Tier 2：GPU 算力出租商（Neoclouds）

這層的商業模式：**買 GPU（資本密集）→ 按小時出租給 Tier 1 或企業**。

> **關鍵差異：CRWV/IREN 賣的是「GPU 時間」，不是 token。他們不捕獲模型的增值利潤。**

```
Token 定價：$0.075 - $60 / million tokens（有模型加值）
GPU 定價：$2 - $15 / GPU·hour（純算力商品）
```

#### CoreWeave（CRWV）

**Q1 2026 財報（2026/5/7，最新）：**

| 指標 | 數字 |
|------|------|
| Q1 2026 收入 | **$2.078B**（YoY 2x，from $982M）|
| FY2026 收入指引 | **$12-13B** |
| Revenue Backlog | **$99.4B** |
| 合約電力 | 3.5 GW |
| GPU 數量 | **250,000 NVIDIA GPUs** |
| 資料中心 | 43 個，850 MW 已上線 |

**客戶結構：**
- Microsoft（最大客戶，ironically MSFT 既賣 token 也向 CRWV 租 GPU）
- Anthropic（剛簽多年合約供 Claude inference）
- OpenAI
- NVIDIA 投資 $2B（2026年1月）

**商業模式風險：**
- 極高資本密集（需要持續舉債買 GPU + 建 DC）
- GPU 折舊：H100 價值隨新一代 GPU 推出而下降
- 客戶集中（Microsoft 佔大比例）
- SemiAnalysis 注：公開市場對 CRWV 情緒仍負面，但**供應全部售完、GPU 租金已漲 40%**

**CRWV 的特殊性：** 它是 Tier 1 公司的「GPU 倉庫」。Microsoft 賣 token 給企業，但實際算力有部分是從 CRWV 租的。CRWV 是基礎設施層，不是應用層。

---

#### IREN（Iris Energy）

**現狀數據：**
- 目前 GPU：23,000 個（H100/H200）
- AI Cloud ARR 目標：**>$500M**（Q1 2026 前）
- 2026年底目標：**140,000 GPUs，$3.4B ARR**
- 已簽合約：$225M AI Cloud ARR（11,000 GPUs）
- 已簽客戶：Microsoft、Together AI、Fluidstack、Fireworks AI
- 電力儲備：3 GW（只用了 16%，成長空間大）

**IREN vs CRWV 的差異：**

| 維度 | CoreWeave | IREN |
|------|-----------|------|
| 規模 | **250K GPUs，$99.4B backlog** | 23K→140K GPUs，$3.4B ARR 目標 |
| 背景 | 純 AI GPU cloud 起家 | 比特幣礦機轉型 AI |
| 客戶 | Microsoft、OpenAI、Anthropic | Microsoft、Together AI |
| 財務槓桿 | 極高負債 | 較低但仍高 |
| 成長潛力 | 已是行業龍頭 | 高成長但規模小 |

---

### Tier 1 vs Tier 2 商業模式比較

```
客戶付錢給誰？

企業/開發者
    ↓ 付 token 費用（$5-60/MTok）
Tier 1B（MSFT Azure / AWS Bedrock / Google Cloud）
    ↓ 付 GPU 租金（$2-15/GPU·hr）
Tier 2（CoreWeave / IREN / Lambda）
    ↓ 買 GPU
Tier 3（NVIDIA / Broadcom / Micron）
    ↓ 需要電力/散熱
Tier 4（Vertiv / Eaton）
```

**利潤在哪裡？**

| 層級 | 毛利率估算 | 說明 |
|------|-----------|------|
| 模型開發者（Tier 1A）| **70%+** | 軟體定價，邊際成本低 |
| Token 平台（Tier 1B）| **40-70%** | 算力 + 模型加值 |
| GPU 出租（Tier 2）| **20-35%** | 純算力，受折舊壓縮 |
| GPU 製造（Tier 3）| **50-75%（NVDA）** | 壟斷性硬體 |
| 電力/散熱（Tier 4）| **20-30%** | 工業品，但 backlog 給定價力 |

---

## 最新財報數據（2026年Q1）

### 供應鏈各層最新數字

#### 算力層

| 公司 | 最新指標 | 關鍵數字 |
|------|---------|---------|
| **NVIDIA** | Q1 FY2026 DC 收入 | **$39.1B（+73% YoY）**，H20 出口管制 -$4.5B |
| **Broadcom** | Q1 FY2026 AI 收入 | **$8.4B（+106% YoY）**，$73B backlog |
| **CoreWeave** | Q1 2026 收入 | **$2.078B（2x YoY）**，$99.4B backlog |

#### 記憶體層

| 公司 | 最新指標 | 關鍵數字 |
|------|---------|---------|
| **Micron** | Q2 FY2026 收入 | **$23.9B（+196% YoY）** ← 加速 |
| **SK Hynix** | 2026 供應狀況 | HBM + DRAM + NAND **全年已售完** |
| **SNDK（你持有）**| Q3 FY2026 收入 | **$5.95B（+251% YoY）** |
| Server DRAM 漲價 | Samsung + SK Hynix | 對 Google、MSFT 漲 **60-70%** |

#### 網路層

| 公司 | 最新指標 | 關鍵數字 |
|------|---------|---------|
| **Arista（ANET）**| Q1 2026 | **$2.709B（+35% YoY）**，Deferred Revenue $6.2B |
| ANET FY2026 指引 | 全年 | **$11.5B（+27.7%）**，AI networking $3.5B |

#### 電力/散熱層

| 公司 | 最新指標 | 關鍵數字 |
|------|---------|---------|
| **Vertiv（VRT）**| Q1 2026 | Adj. EPS **+83% YoY**，Backlog **$15B+** |
| VRT FY2026 指引 | 全年 | 收入 **$13.5-14B（+34%）**，EPS **+51%** |

#### Token 平台層

| 公司 | 最新指標 | 關鍵數字 |
|------|---------|---------|
| **Microsoft（MSFT）**| Q3 FY2026 | Azure AI **$37B run rate（+123%）** |
| **Amazon（AMZN）**| Q1 FY2026 | AWS AI **$15B run rate**，Bedrock Q1 QoQ **+170%** |
| **Anthropic** | Apr 2026 ARR | **$30B**（Dec 2025 $9B → Apr 2026 $30B）|

---

## GPU 租賃市場

| 指標 | 數字 |
|------|------|
| H100 1年期租賃 | $1.70（2025/10）→ **$2.35（2026/3）**（+40%）|
| B200 on-demand | $2.65/hr（reserved）～ $14.24/hr |
| B200 購買 backlog | **3.6M units**（2026年4月）|
| 市場容量 | 2026年8-9月前**全部已訂滿** |
| 市場情緒 | SemiAnalysis：公開市場對 CRWV/IREN/Nebius 仍負面（**錯誤定價機會？**）|

---

## 「財報尚未完全定價」的三大機會

### #1 Arista Networks (ANET) — Supply Unlock = 收入解鎖

**為什麼「財報還沒完全體現」：**
- $6.2B **Deferred Revenue**（已簽約但未入帳）
- 管理層：「問題是晶圓/矽/光學器件供應不足，不是需求」
- 供應一解鎖 → $6.2B 轉成實際收入
- 股票因「供應限制」跌 12.57%（這是買點邏輯）

**財報已暗示：** Q1 +35%，AI networking 目標 $3.5B（2026全年）

---

### #2 Broadcom (AVGO) — $73B Backlog 的能見度

**為什麼「財報還沒完全體現」：**
- $73B AI backlog（XPU + networking，未來18個月交付）
- XPU 客戶從 3 個擴展到 4-6 個（Anthropic、OpenAI 也是客戶）
- Mizuho 估 FY2026 全年 AI 收入 **$40.4B（+103% YoY）**

**財報已暗示：** Q1 AI 收入 $8.4B（+106%），Q2 指引 $22B（+47%）

---

### #3 Microsoft (MSFT) — 你已持有，下一棒在途

**為什麼「財報還沒完全體現」：**
- $37B AI run rate → 下一棒：140K 組織內滲透率還低
- 企業從試點 → 全面部署 = $37B → $70B+ 路徑
- OpenAI 結束獨家後，Azure OpenAI 仍是最深整合平台

---

## 投資組合 Gap 分析

### 現有持倉 AI Token 主題覆蓋

| 持倉 | AI Token 相關性 | 評估 |
|------|---------------|------|
| **NVDA** | 極高 — GPU 是每個 token 的引擎 | ✅ 覆蓋 |
| **ARM** | 高 — 每個 AI 晶片的授權費 | ✅ 覆蓋 |
| **MSFT** | 高 — Azure OpenAI + Copilot token 平台 | ✅ 覆蓋 |
| **META** | 高 — 消費 token + AI 廣告收益 | ✅ 覆蓋 |
| **SNDK** | 中高 — NAND AI 存儲，Q3 +251% YoY，**+3,314%** | ✅ 已大漲 |
| **TSLA** | 低 — 自有 AI（FSD/Optimus），非 token 基礎設施 | ⚠️ 弱連結 |
| **IGV** | 中 — 軟體 AI 受益（稀釋）| ⚠️ 間接 |
| **QQQ** | 高（聚合）— NVDA + hyperscaler ~45% | ✅ 間接覆蓋 |
| **VOO** | 中（聚合）— 科技權重 ~30% | ✅ 間接覆蓋 |
| **0050** | 高 via TSMC ~45% | ✅ 晶圓廠覆蓋 |
| **DIA** | 低 — 科技權重少 | ⚠️ 弱 |
| **SGOV** | 零 — 現金管理 | 流動性儲備 |
| **IBIT** | 零（AI 主題）| 加密資產 |

### 缺口

| 主題 | 缺口 | 建議標的 |
|------|------|---------|
| **HBM 記憶體** | 最大缺口，#1 供應瓶頸 | **MU**（Micron）|
| **電力/散熱基礎設施** | 無任何曝光 | **VRT**（Vertiv）|
| **Custom ASIC + 網路晶片** | 無直接持有 | **AVGO**（Broadcom）|
| **AI 網路設備** | 無直接持有 | **ANET**（Arista）|
| **GPU 出租（Neocloud）**| 無直接持有 | CRWV、IREN（高風險高報酬）|

---

## 標的優先排序

| 排名 | 標的 | 邏輯 | 風險 |
|------|------|------|------|
| **1** | **AVGO（Broadcom）** | $73B backlog，+106% AI 收入，XPU + 網路雙引擎 | 估值已高 |
| **2** | **ANET（Arista）** | $6.2B deferred revenue 等待解鎖，需求確定供應是瓶頸 | 供應解鎖時間不確定 |
| **3** | **VRT（Vertiv）** | $15B backlog，物理基礎設施無論誰的 GPU 都需要 | 製造產能擴張執行風險 |
| **4** | **MU（Micron）** | HBM 供不應求，Q2 +196% YoY，HBM4 接棒 | DRAM 舊業務週期波動 |
| **5（持有）**| **META** | 最便宜的 AI 大型股，Token 消費者 + 廣告受益者 | Capex 紀律 |
| **6（持有）**| **MSFT** | $37B AI run rate，最防禦性的 AI token 平台 | OpenAI 獨家優勢縮小 |
| **7（持有）**| **NVDA** | 最高確信但估值已高，CUDA 護城河無可撼動 | 估值，custom silicon 替代 |
| **8（持有）**| **ARM** | 每個 AI 晶片的授權費，但 80-120x P/E 已充分定價 | 估值過高 |
| **觀察** | **CRWV** | $99.4B backlog，市場錯誤情緒 vs 基本面 | 高負債，GPU 折舊，客戶集中 |
| **觀察** | **AMZN** | AWS AI $15B run rate，Bedrock +170% QoQ | AI 收入不透明，需 Bedrock 分開揭露 |

---

## 推理（Inference）的價值捕獲

- 每訓練花 $1，終生推理花 **$15-20**
- 2026年初：推理佔 AI 雲端基礎設施支出的 **55%**（$37.5B）
- Anthropic 毛利率：38% → **70%+**（Blackwell + 軟體優化）

### SemiAnalysis 關鍵數字（Opus 4.7 實際使用）

- 表定價格：$5/$25 per million tokens
- **實際混合價格：~$0.99/MTok**（因 cache hit 率 >90%，input:output 比 300:1）
- SemiAnalysis 自身：每月每員工消耗 **50億 tokens**，年花費 **$10.95M**（員工薪酬的 30%）

---

## 主要風險

| 風險 | 說明 | 對假設的影響 |
|------|------|------------|
| **模型效率提升** | 每任務 token 用量下降（MoE、量化、蒸餾）| 部分抵消量成長，歷史上量增>效率增 |
| **自製晶片替代** | Google TPU、AWS Trainium 替代 NVIDIA | NVDA 風險，但 AVGO/Broadcom 反而受益 |
| **DeepSeek 效應** | 開源高效模型降低 token 成本 | Jevons Paradox — 更便宜 = 更多用量 |
| **出口管制** | H20 被限制，中國市場縮小 | NVDA -$4.5B 單季影響，其他市場補償 |
| **電力瓶頸** | 電網連接等待 3-5 年 | 減緩但不阻止 buildout；VRT 反而受益 |
| **OpenAI 獨家結束** | MSFT 失去獨家，AWS 也獲 OpenAI 模型（2026/4）| 稀釋 MSFT 的護城河，但整體 AI 採用加速 |

---

## 參考資料

### SemiAnalysis 文章
- [AI Value Capture: The Shift to Model Labs](https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model)
- [The Coding Assistant Breakdown](https://newsletter.semianalysis.com/p/the-coding-assistant-breakdown-more)
- [How Much Do GPU Clusters Really Cost](https://newsletter.semianalysis.com/p/how-much-do-gpu-clusters-really-cost)
- [The Great GPU Shortage](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)

### 財報來源
- [Microsoft Q3 FY2026](https://news.microsoft.com/source/2026/04/29/microsoft-cloud-and-ai-strength-fuels-third-quarter-results/)
- [Anthropic $30B ARR](https://www.the-ai-corner.com/p/anthropic-30b-arr-passed-openai-revenue-2026)
- [NVIDIA Q1 FY2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026)
- [Broadcom Q1 FY2026 AI Revenue](https://finovian.com/category/earnings/broadcom-q1-fy2026-earnings-analysis/)
- [Arista Q1 2026](https://www.arista.com/en/company/news/press-release/24017-pr-20260505)
- [Vertiv Q1 2026](https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-First-Quarter-with-Diluted-EPS-Growth-of-136-Adjusted-Diluted-EPS-Growth-of-83-Raises-Full-Year-Guidance/default.aspx)
- [CoreWeave Q1 2026](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/)
- [Amazon AWS AI Q1 2026](https://futurumgroup.com/insights/amazon-q1-fy-2026-aws-momentum-builds-as-ai-infrastructure-spend-surges/)
- [OpenAI ends Microsoft exclusivity](https://www.cnbc.com/2026/04/28/openai-brings-models-to-aws-after-ending-exclusivity-with-microsoft.html)
- [SanDisk Q3 +251% YoY](https://siliconangle.com/2026/04/30/western-digital-sandisk-crush-wall-streets-expectations-soaring-ai-demand/)
- [SK Hynix HBM Sold Out](https://www.notebookcheck.net/SK-hynix-sells-out-its-DRAM-NAND-and-HBM-chip-supply-to-Nvidia-through-2026)
- [IREN AI Cloud Expansion](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-doubles-ai-cloud-23k-gpus-raises-ai-cloud-arr-target-500m)
