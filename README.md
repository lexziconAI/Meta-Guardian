# MetaGuardian: Metabolic Health Readiness Assessment

## 🔬 Research Tool - Constitutional AI Framework

**FORK STATUS**: This project is a strategic fork of [CultureCoach](https://github.com/lexziconAI/culture-coach), preserving the proven Constitutional AI infrastructure while adapting the assessment domain from cultural competency to metabolic health readiness.

## Purpose

MetaGuardian assesses individual readiness for AI-assisted early disease detection tools across five dimensions:
- **HL (Health Literacy)**: Understanding of health concepts and test results
- **CM (Clinical Markers)**: Familiarity with and access to biomarkers
- **DI (Data Integration)**: Ability/willingness to connect lifestyle + clinical data
- **DL (Digital Literacy)**: Comfort with health tech tools and apps
- **PR (Preventive Readiness)**: Motivation and capacity for preventive action

## Architecture Preserved from CultureCoach

✅ **Constitutional AI Framework**: Yama-principled reasoning with cryptographic provenance  
✅ **OpenAI Realtime API**: Voice-first interaction via WebSocket  
✅ **FastAPI Backend**: Python backend with SQLite persistence  
✅ **React + Vite Frontend**: Real-time assessment dashboard  
✅ **Fractal Inference**: Multi-phase evidence accumulation (OPENING → CORE → GAP_FILLING → VALIDATION → CLOSING)  
✅ **Email Reports**: Groq LLM-generated comprehensive assessments  

## What Changed

**Domain Logic Replaced**:
- Cultural dimensions → Metabolic health dimensions
- Cross-cultural scenarios → Health data scenarios
- SYSTEM_INSTRUCTION updated with metabolic health coaching prompt

**Preserved Infrastructure**:
- Authentication system (email-based JWT)
- WebSocket connection management
- Constitutional AI validation
- Evidence logging and scoring engine
- Report generation pipeline

## Run Locally

**Prerequisites**: Node.js, Python 3.11+

### Frontend
```bash
npm install
npm run dev
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Environment Variables**:
- Frontend: `VITE_API_URL` (default: http://localhost:8000)
- Backend: `OPENAI_API_KEY`, `GROQ_API_KEY`, `SENDGRID_API_KEY`

## Current Status

⚠️ **PLACEHOLDERS CREATED** - Domain-specific logic needs implementation:
- `/src/prompts/metaguardian-system.ts`: System instruction for health coaching
- `/src/types/assessment.ts`: Metabolic assessment structure
- `/src/data/interview-questions.ts`: 21 research interview questions
- `/src/services/scoring-engine.ts`: Dimension scoring algorithms

All infrastructure is **production-ready** and tested on Render deployment.

## Research Context

This tool supports studies on:
1. **General Public**: Readiness for consumer health AI tools
2. **Healthcare Experts**: Clinical perspectives on AI integration

See `FORK_REPORT.md` for detailed migration documentation.
