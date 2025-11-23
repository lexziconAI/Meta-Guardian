# Latest LLM Model Names (November 2025)

**Research Date**: November 23, 2025  
**Purpose**: Update API keys and model names for sidecar LLM orchestration

---

## 🔥 BREAKING: Latest Model Releases

### **Anthropic Claude 4.5** (September-October 2025)
- **Claude Sonnet 4.5**: `claude-sonnet-4-5-20250929` (alias: `claude-sonnet-4-5`)
  - Most intelligent model for complex agents and coding
  - 200K context (1M beta with header)
  - $3/MTok input, $15/MTok output
  - **Use for**: Phase 6 (Backend schema transformation)
  
- **Claude Haiku 4.5**: `claude-haiku-4-5-20251001` (alias: `claude-haiku-4-5`)
  - Fastest model with near-frontier intelligence
  - 200K context window
  - $1/MTok input, $5/MTok output
  - **Use for**: Quick transformations, fast inference

- **Claude Opus 4.1**: `claude-opus-4-1-20250805` (alias: `claude-opus-4-1`)
  - Exceptional for specialized reasoning tasks
  - 200K context, 32K max output
  - $15/MTok input, $75/MTok output
  - **Use for**: Complex reasoning, deep analysis

### **Google Gemini 3** (November 2025)
- **Gemini 3 Pro**: `gemini-3-pro-preview` 
  - Google's most intelligent model yet
  - State-of-the-art multimodal understanding
  - Best for vibe coding and agentic tasks
  - **Use for**: Phase 8 (Test scenario generation)

- **Gemini 2.5 Flash**: `gemini-2.5-flash`
  - Best price-performance balance
  - Optimized for large-scale processing
  - **Use for**: High-volume narrative processing

- **Gemini 2.5 Pro**: `gemini-2.5-pro`
  - Advanced thinking model
  - Code, math, STEM reasoning
  - Long context (up to 1M tokens)

### **OpenAI GPT-5 & GPT-5.1** (2025)
- **GPT-5**: `gpt-5` ⭐ **NEW FLAGSHIP**
  - OpenAI's latest flagship model
  - Superior reasoning and multimodal capabilities
  - **Use for**: Phase 7 (Frontend state handlers)

- **GPT-5.1**: `gpt-5.1`
  - Enhanced version with improved reasoning
  
- **GPT-4o**: `gpt-4o` (still available, proven workhorse)
  - Multimodal (vision, audio, text)
  - 128K context window
  - **Confirmed working** in smoke tests

- **GPT-4o mini**: `gpt-4o-mini`
  - Cost-efficient alternative
  - **Confirmed working** in smoke tests

### **Groq Models** (Updated November 2025)
- **OpenAI GPT-OSS 120B**: `openai/gpt-oss-120b`
  - OpenAI's flagship open-weight model
  - 120B parameters, built-in browser search
  - 500 tps, $0.15 input / $0.60 output per MTok
  - **Use for**: Phase 5 (Report generation at 800+ tps)

- **OpenAI GPT-OSS 20B**: `openai/gpt-oss-20b`
  - Faster inference (1000 tps)
  - $0.075 input / $0.30 output per MTok

- **Meta Llama 3.3 70B**: `llama-3.3-70b-versatile` ✅ **PRODUCTION**
  - 280 tps, $0.59 input / $0.79 output per MTok
  - 131K context, 32K output

- **Meta Llama 4 Scout 17B**: `meta-llama/llama-4-scout-17b-16e-instruct` (Preview)
  - 750 tps, $0.11 input / $0.34 output per MTok

- **Moonshot AI Kimi K2**: `moonshotai/kimi-k2-instruct-0905` (Preview)
  - 200 tps, $1.00 input / $3.00 output per MTok
  - 262K context window
  - **Currently used in MetaGuardian**

---

## 📋 Updated Model Recommendations for MetaGuardian

### **Phase 5: Groq Report Generation** ✅ NO CHANGE
**Keep**: `moonshotai/kimi-k2-instruct-0905`  
**Rationale**: Already working, long context (262K), good for narrative synthesis

**Alternative**: `openai/gpt-oss-120b` (500 tps, open-weight, built-in tools)

### **Phase 6: Backend Schema Transformation**
**Recommended**: `claude-sonnet-4-5` (Claude 4.5 Sonnet)  
**API Key**: `sk-ant-api03-ykGby1Hdptb6gtJ...` ✅ Valid  
**Why**: Best for complex code refactoring and database schema design

**Test Command** (PowerShell):
```powershell
$headers = @{
    "x-api-key" = $env:ANTHROPIC_API_KEY
    "anthropic-version" = "2023-06-01"
    "content-type" = "application/json"
}
$body = '{"model":"claude-sonnet-4-5","max_tokens":1000,"messages":[{"role":"user","content":"test"}]}'
Invoke-WebRequest -Uri "https://api.anthropic.com/v1/messages" -Method POST -Headers $headers -Body $body
```

### **Phase 7: Frontend State Handlers**
**Recommended**: `gpt-5` (OpenAI GPT-5) ⭐ **FLAGSHIP**  
**API Key**: `sk-proj-7NIVt9m04mt2G6cQ...` ✅ **CONFIRMED WORKING**  
**Why**: Best for complex React state management and quantum calculations

**Test Command** (PowerShell):
```powershell
$headers = @{
    "Authorization" = "Bearer $env:OPENAI_API_KEY"
    "Content-Type" = "application/json"
}
$body = '{"model":"gpt-5","messages":[{"role":"user","content":"test"}],"max_tokens":10}'
Invoke-WebRequest -Uri "https://api.openai.com/v1/chat/completions" -Method POST -Headers $headers -Body $body
```

### **Phase 8: Test Scenario Generation**
**Recommended**: `gemini-3-pro-preview` (Gemini 3 Pro) 🆕  
**API Key**: `AIzaSyCFe1c5oJi9D8gSm5b8InhvoIydmdDj9NE` ✅ Valid  
**Why**: State-of-the-art multimodal reasoning, best for complex behavior scenarios

**Test Command** (PowerShell):
```powershell
$headers = @{"Content-Type" = "application/json"}
$body = '{"contents":[{"parts":[{"text":"test"}]}]}'
Invoke-WebRequest -Uri "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-preview:generateContent?key=$env:GEMINI_API_KEY" -Method POST -Headers $headers -Body $body
```

**Alternative**: `gemini-2.5-flash` (faster, more cost-effective)

---

## 🔧 Smoke Test Results (Fixed Model Names)

| Provider | Status | Correct Model | Notes |
|----------|--------|---------------|-------|
| **OpenAI** | ✅ WORKING | `gpt-4o-mini`, `gpt-5` | Production ready |
| **Anthropic Claude** | ⚠️ FIX REQUIRED | `claude-sonnet-4-5` (NOT `claude-3-5-sonnet-20241022`) | API key valid |
| **Groq** | ⚠️ FIX REQUIRED | `llama-3.3-70b-versatile` (NOT `mixtral-8x7b-32768`) | API key valid |
| **Google Gemini** | ⚠️ FIX REQUIRED | `gemini-3-pro-preview` (use v1beta endpoint) | API key valid |

---

## 📊 Cost Comparison for MetaGuardian Phases

### Phase 5: Report Generation (1M tokens/report average)
| Model | Input Cost | Output Cost | Total/Report |
|-------|-----------|-------------|--------------|
| Kimi K2 (current) | $1.00 | $3.00 | $4.00 |
| GPT-OSS 120B | $0.15 | $0.60 | $0.75 | **75% savings** |
| GPT-5 | Variable | Variable | ~$2-5 |

### Phase 6: Backend Transformation (50K tokens estimated)
| Model | Cost | Speed |
|-------|------|-------|
| Claude Sonnet 4.5 | $0.15 input + $0.75 output = $0.90 | Fast |
| GPT-5 | ~$1-2 | Moderate |

### Phase 7: Frontend State Logic (100K tokens estimated)
| Model | Cost | Speed |
|-------|------|-------|
| GPT-5 | ~$2-4 | Excellent |
| Claude Sonnet 4.5 | $0.30 + $1.50 = $1.80 | Fast |

### Phase 8: Test Scenarios (20K tokens estimated)
| Model | Cost | Speed |
|-------|------|-------|
| Gemini 3 Pro | Free tier available | Fast |
| Gemini 2.5 Flash | Very low cost | Fastest |

---

## 🎯 Final Recommendations

### **Option A: Multi-Provider Optimized** (Recommended)
- **Phase 5**: Keep `moonshotai/kimi-k2-instruct-0905` (already working)
- **Phase 6**: `claude-sonnet-4-5` (best for schema design)
- **Phase 7**: `gpt-5` (confirmed working, excellent for React)
- **Phase 8**: `gemini-3-pro-preview` (state-of-the-art reasoning)

**Pros**: 
- Leverage each provider's strengths
- Best performance per phase
- Distributed risk

**Cons**: 
- Need to fix 3 API configurations
- More coordination complexity

### **Option B: OpenAI-Only Fast Path** (Pragmatic)
- **All Phases**: `gpt-5` or `gpt-4o`
  - Confirmed working ✅
  - Consistent quality
  - Immediate execution

**Pros**: 
- Zero configuration time
- Start Phase 5-8 NOW
- Proven reliability

**Cons**: 
- Higher cost than Groq for reports
- Single vendor dependency

---

## ⚡ Immediate Action Items

1. **Update Smoke Test Script** with correct model names:
   - Claude: `claude-sonnet-4-5`
   - Groq: `llama-3.3-70b-versatile`
   - Gemini: `gemini-3-pro-preview` (v1beta endpoint)

2. **Re-run Smoke Tests** to confirm all APIs working

3. **Update SIDECAR_ORCHESTRATION.md** with correct model assignments

4. **Decision Point**: Choose Option A (optimized) or Option B (fast)

---

**Next Step**: User decision on multi-provider vs. OpenAI-only approach for Phase 5-8 execution.
