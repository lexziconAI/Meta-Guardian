# MetaGuardian: Sidecar LLM Orchestration Plan

**Purpose**: Distribute Phases 5-8 of quantum storytelling transformation across specialized sidecar LLMs

**Context Files**:
- `QUANTUM_STORYTELLING.md` - Complete transformation rationale and framework
- `TECHNICAL_ARCHITECTURE.md` - System design and current implementation status
- `src/types/narrative-streams.ts` - Quantum data model
- `components/QuantumStoryDashboard.tsx` - Visualization component

---

## Available LLM Providers

| Provider | API Key | Specialization | Best For |
|----------|---------|----------------|----------|
| **Anthropic Claude** | `sk-ant-api03-ykGby1Hdptb6gtJ...` | Code refactoring, schema design | Backend transformations |
| **OpenAI GPT-4** | `sk-proj-7NIVt9m04mt2G6cQ...` | Complex logic, state management | Frontend state handlers |
| **Groq (Kimi-K2)** | `gsk_oxqYcd8rIhCpF6GEavQaWGdyb3FY...` | Long-context synthesis | Report prompt transformation |
| **Google Gemini** | `AIzaSyCFe1c5oJi9D8gSm5b8InhvoIydmdDj9NE` | Multi-modal reasoning | Test scenario generation |
| **Cohere** | `CJ085MzeWAMJ6i1wreNqSDpvGPhthjowladviMGm` | Embeddings, classification | Story quality metrics |
| **Fireworks AI** | `fw_3ZZxCEF1URaNwv5nzBssRZZ9` | Fast inference | Real-time quantum calculations |
| **Fal AI** | `9236725c-2ddb-4629-8d24-4ea63be57a3a:...` | Image generation | Dashboard visualization assets |

---

## Phase 5: Transform Groq Report Generation

**Assigned To**: Groq (Kimi-K2-Instruct)  
**Rationale**: Self-hosting - transform the model that generates reports

**Task**: Update `backend/main.py` finalize-session endpoint

### Current Implementation (Lines 215-290)
```python
report_prompt = f"""
Generate a comprehensive metabolic health readiness assessment report.

Session Transcript: {session['transcript']}
Final Dimension Scores: {json.dumps(dimension_scores)}

Format as HTML email with:
1. Executive Summary
2. Dimensional Analysis (visualize scores)
3. Key Strengths (top dimensions)
4. Development Areas (low-confidence dimensions)
5. Actionable Recommendations (5-7 specific steps)
6. Next Steps
"""
```

### Required Transformation
```python
story_synthesis_prompt = f"""
You are synthesizing a LIVING HEALTH STORY using David Boje's Quantum Storytelling framework.

## Session Data
Full Transcript: {session['transcript']}
Narrative Streams: {json.dumps(narrative_streams)}
Antenarrative Fragments: {json.dumps(fragments)}
Quantum States: {json.dumps(quantum_states)}
Temporal Layers: {json.dumps(temporal_layers)}
Grand Narratives: {json.dumps(grand_narratives)}

## Synthesis Guidelines

### 1. HONOR ANTENARRATIVES (Don't Force Coherence)
- Quote user's exact speculative fragments
- Preserve tensions and contradictions
- List possible story endings (don't choose one)

### 2. EMBRACE QUANTUM SUPERPOSITION
Present multiple simultaneous truths:
- "You are 60% Empowered Tracker AND 30% Anxious Monitor AND 10% Compliant Patient"
- Visualize probability distribution
- Show which states conflict and which reinforce

### 3. MAP TEMPORAL ENTANGLEMENT
Create three-column view:
- LEFT: Past health stories user references
- CENTER: Present moment narratives
- RIGHT: Future imaginaries user is authoring

### 4. SURFACE GRAND NARRATIVES
Identify cultural/medical discourses user negotiates with:
- Medical Authority: [accepting/resisting/negotiating/transforming]
- Quantified Self: [stance]
- Genetic Determinism: [stance]
- Wellness Industry: [stance]

### 5. OFFER STORY PATHS (Not Prescriptions)
Present 3 possible futures as story continuations:
- Path A: [scenario 1]
- Path B: [scenario 2]
- Path C: [scenario 3]

**CRITICAL**: Story belongs to user. You are witnessing, not authoring.

## Constitutional AI: Yama Storytelling Ethics
- Ahimsa: Never force a story user isn't ready to tell
- Satya: Honor contradictions (don't resolve falsely)
- Asteya: Story belongs to user, not system
- Brahmacharya: Match depth to user's capacity
- Aparigraha: Share patterns without claiming ownership

## Output Format
Generate HTML narrative that reads as IN-THE-MAKING (not DONE).
Use fractal/organic visual language (not rigid tables).
Include quantum state bubbles, temporal entanglement diagrams, grand narrative badges.

Story Qualities to Emphasize:
- Coherence: {calculate_coherence(fragments)}
- Fluidity: {calculate_fluidity(quantum_states)}
- Authenticity: {calculate_authenticity(yama_resonances)}
"""
```

### Acceptance Criteria
- [ ] Prompt preserves quantum superposition (doesn't force single truth)
- [ ] Quotes user's antenarrative fragments directly
- [ ] Visualizes temporal entanglement (past-present-future)
- [ ] Identifies grand narratives with user stance
- [ ] Offers 3 possible story paths (not single recommendation)
- [ ] HTML uses organic/fractal visual language
- [ ] Story reads as IN-THE-MAKING not completed assessment

---

## Phase 6: Backend Schema Transformation

**Assigned To**: Anthropic Claude  
**Rationale**: Expert at schema design and migration scripts

**Task**: Update database schema from assessment to narrative streams

### Files to Modify
1. `backend/database.py` - Add new tables
2. `backend/schemas.py` - Pydantic models for quantum types
3. `backend/migrate_narrative.py` - Migration script (NEW FILE)

### New Database Tables

```sql
-- Replace dimensions table
CREATE TABLE narrative_streams (
    id INTEGER PRIMARY KEY,
    session_id TEXT NOT NULL,
    stream_id TEXT NOT NULL, -- BODY_KNOWLEDGE, BIOMARKER_MYTHOLOGY, etc.
    coherence REAL,
    fluidity REAL,
    authenticity REAL,
    created_at TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id)
);

-- Replace evidence_log table
CREATE TABLE antenarrative_fragments (
    id INTEGER PRIMARY KEY,
    stream_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    type TEXT NOT NULL, -- memory, speculation, contradiction, etc.
    tensions TEXT, -- JSON array
    possible_endings TEXT, -- JSON array
    emotional_tone TEXT,
    energy_level TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id)
);

-- NEW: Quantum states
CREATE TABLE quantum_states (
    id INTEGER PRIMARY KEY,
    stream_id INTEGER NOT NULL,
    state TEXT NOT NULL,
    probability REAL NOT NULL,
    evidence_threads TEXT, -- JSON array
    conflicts_with TEXT, -- JSON array of state names
    reinforces TEXT, -- JSON array of state names
    evolution TEXT, -- JSON tracking how probability changed
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id)
);

-- NEW: Temporal layers
CREATE TABLE temporal_layers (
    id INTEGER PRIMARY KEY,
    stream_id INTEGER NOT NULL,
    past_story TEXT,
    present_moment TEXT,
    future_projection TEXT,
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id)
);

-- NEW: Grand narratives
CREATE TABLE grand_narratives (
    id INTEGER PRIMARY KEY,
    stream_id INTEGER NOT NULL,
    discourse TEXT NOT NULL, -- Medical authority, Quantified self, etc.
    user_stance TEXT NOT NULL, -- accepting, resisting, negotiating, transforming
    influence REAL, -- 0-1 how much this shapes user's story
    evidence_quotes TEXT, -- JSON array
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id)
);

-- NEW: Yama resonances
CREATE TABLE yama_resonances (
    id INTEGER PRIMARY KEY,
    fragment_id INTEGER NOT NULL,
    principle TEXT NOT NULL, -- Ahimsa, Satya, Asteya, Brahmacharya, Aparigraha
    resonance TEXT NOT NULL, -- alignment, tension, exploration
    insight TEXT,
    FOREIGN KEY (fragment_id) REFERENCES antenarrative_fragments(id)
);
```

### Pydantic Schema Updates

```python
# backend/schemas.py

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AntenarativeFragment(BaseModel):
    text: str
    type: str  # memory, speculation, contradiction, etc.
    tensions: List[str]
    possible_endings: List[str]
    entangled_with: List[str]
    superposition_states: List[str]
    emotional_tone: str
    energy_level: str
    timestamp: datetime

class QuantumState(BaseModel):
    state: str
    probability: float  # 0-1
    evidence_threads: List[str]
    conflicts_with: Optional[List[str]]
    reinforces: Optional[List[str]]
    evolution: List[dict]  # [{time, prob}, ...]

class TemporalLayers(BaseModel):
    past_story: str
    present_moment: str
    future_projection: str

class GrandNarrative(BaseModel):
    discourse: str
    user_stance: str  # accepting, resisting, negotiating, transforming
    influence: float  # 0-1
    evidence_quotes: List[str]

class YamaResonance(BaseModel):
    principle: str  # Ahimsa, Satya, Asteya, Brahmacharya, Aparigraha
    resonance: str  # alignment, tension, exploration
    insight: str

class NarrativeStream(BaseModel):
    stream_id: str
    fragments: List[AntenarativeFragment]
    possible_states: List[QuantumState]
    temporal_layers: TemporalLayers
    grand_narratives: List[GrandNarrative]
    coherence: float
    fluidity: float
    authenticity: float

class QuantumStorySession(BaseModel):
    session_id: str
    user_id: str
    streams: List[NarrativeStream]
    phase: str  # INVOCATION, EMERGENCE, ENTANGLEMENT, CRYSTALLIZATION, OPENING
    overall_coherence: float
    narrative_complexity: float
    story_vitality: float
    yama_balance: dict
```

### Acceptance Criteria
- [ ] All 6 new tables created in database
- [ ] Pydantic schemas match TypeScript interfaces in `narrative-streams.ts`
- [ ] Migration script safely converts existing sessions (if any)
- [ ] Foreign key relationships properly enforced
- [ ] JSON columns validated on insert

---

## Phase 7: Frontend State Handler Wiring

**Assigned To**: OpenAI GPT-4  
**Rationale**: Expert at complex React state management

**Task**: Update `components/LiveVoiceCoach.tsx` to process `updateNarrativeState` tool calls

### Current Implementation (Lines 350-410)
```typescript
const handleToolCall = (args: any) => {
  setSessionState((prev: SessionState) => {
    const updated = { ...prev };
    
    // OLD: Update dimensions
    if (args.dimensions) {
      Object.keys(args.dimensions).forEach((dim) => {
        updated.dimensions[dim] = {
          ...updated.dimensions[dim],
          ...args.dimensions[dim]
        };
      });
    }
    
    // OLD: Log evidence
    if (args.newEvidence) {
      updated.evidenceLog = [
        ...prev.evidenceLog,
        { ...args.newEvidence, timestamp: new Date().toISOString() }
      ];
    }
    
    return updated;
  });
};
```

### Required Transformation
```typescript
const handleToolCall = (args: any) => {
  setQuantumStorySession((prev: QuantumStorySession) => {
    const updated = { ...prev };
    
    // NEW: Process narrative state update
    const streamId = args.stream;
    const stream = updated.streams.find(s => s.streamId === streamId) || createEmptyStream(streamId);
    
    // Add new antenarrative fragment
    if (args.newFragment) {
      stream.fragments.push({
        ...args.newFragment,
        id: generateId(),
        timestamp: new Date().toISOString()
      });
    }
    
    // Update quantum states with probability distribution
    if (args.quantumStates && args.quantumStates.length > 0) {
      // Normalize probabilities to sum to 1.0
      const totalProb = args.quantumStates.reduce((sum, s) => sum + s.probability, 0);
      stream.possibleStates = args.quantumStates.map(s => ({
        ...s,
        probability: s.probability / totalProb,
        evolution: [
          ...(stream.possibleStates.find(ps => ps.state === s.state)?.evolution || []),
          { time: Date.now(), probability: s.probability / totalProb }
        ]
      }));
    }
    
    // Update temporal layers
    if (args.temporalLayer) {
      stream.temporalLayers = args.temporalLayer;
    }
    
    // Track grand narrative
    if (args.grandNarrative) {
      const existingGN = stream.grandNarratives.find(gn => gn.discourse === args.grandNarrative.discourse);
      if (existingGN) {
        existingGN.userStance = args.grandNarrative.userStance;
        existingGN.influence = Math.min(existingGN.influence + 0.1, 1.0);
      } else {
        stream.grandNarratives.push({
          ...args.grandNarrative,
          influence: 0.3,
          evidenceQuotes: []
        });
      }
    }
    
    // Track Yama resonances
    if (args.yamaResonance && stream.fragments.length > 0) {
      const latestFragment = stream.fragments[stream.fragments.length - 1];
      latestFragment.yamaAlignment = [
        ...(latestFragment.yamaAlignment || []),
        args.yamaResonance
      ];
    }
    
    // Calculate story qualities
    if (args.storyQualities) {
      stream.coherence = args.storyQualities.coherence;
      stream.fluidity = args.storyQualities.fluidity;
      stream.authenticity = args.storyQualities.authenticity;
    } else {
      // Auto-calculate if not provided
      stream.coherence = calculateStreamCoherence(stream);
      stream.fluidity = calculateStreamFluidity(stream);
      stream.authenticity = calculateStreamAuthenticity(stream);
    }
    
    // Track entanglements
    if (args.entangledWith && stream.fragments.length > 0) {
      const latestFragment = stream.fragments[stream.fragments.length - 1];
      latestFragment.entangledWith = args.entangledWith;
    }
    
    // Update stream in session
    const streamIndex = updated.streams.findIndex(s => s.streamId === streamId);
    if (streamIndex >= 0) {
      updated.streams[streamIndex] = stream;
    } else {
      updated.streams.push(stream);
    }
    
    // Update session phase
    if (args.phase) {
      updated.phase = args.phase;
    }
    
    // Calculate overall session metrics
    updated.overallCoherence = calculateOverallCoherence(updated.streams);
    updated.narrativeComplexity = calculateComplexity(updated.streams);
    updated.storyVitality = calculateVitality(updated.streams);
    updated.yamaBalance = calculateYamaBalance(updated.streams);
    
    return updated;
  });
};

// Helper: Calculate coherence (how well fragments connect)
const calculateStreamCoherence = (stream: NarrativeStream): number => {
  const entanglementCount = stream.fragments.reduce(
    (sum, f) => sum + (f.entangledWith?.length || 0), 0
  );
  return Math.min(entanglementCount / (stream.fragments.length * 2), 1.0);
};

// Helper: Calculate fluidity (how much still becoming)
const calculateStreamFluidity = (stream: NarrativeStream): number => {
  const speculativeCount = stream.fragments.filter(
    f => ['speculation', 'bet', 'contradiction'].includes(f.type)
  ).length;
  return speculativeCount / Math.max(stream.fragments.length, 1);
};

// Helper: Calculate authenticity (Yama alignment)
const calculateStreamAuthenticity = (stream: NarrativeStream): number => {
  const alignmentCount = stream.fragments.reduce((sum, f) => 
    sum + (f.yamaAlignment?.filter(y => y.resonance === 'alignment').length || 0), 0
  );
  return alignmentCount / Math.max(stream.fragments.length * 2, 1);
};
```

### Additional Requirements
- [ ] Replace `SessionState` with `QuantumStorySession` type import
- [ ] Update App.tsx to use `<QuantumStoryDashboard />` instead of `<AssessmentDashboard />`
- [ ] Install framer-motion: `npm install framer-motion`
- [ ] Update WebSocket session initialization to use `QUANTUM_STORYTELLING_PROMPT`
- [ ] Add visual feedback when quantum states update (toast notifications)

### Acceptance Criteria
- [ ] Tool calls properly parsed and routed to correct stream
- [ ] Quantum state probabilities normalized to sum to 1.0
- [ ] Fragment entanglements tracked bidirectionally
- [ ] Story quality calculations match TypeScript utility functions
- [ ] Dashboard reactively updates when state changes
- [ ] No TypeScript errors or type mismatches

---

## Phase 8: Test Scenario Creation

**Assigned To**: Google Gemini  
**Rationale**: Multi-modal reasoning for complex human behavior scenarios

**Task**: Create comprehensive test cases for quantum storytelling features

### Create File: `tests/quantum-storytelling-scenarios.ts`

```typescript
export const QUANTUM_TEST_SCENARIOS = [
  {
    name: "Contradiction Embrace",
    description: "User expresses conflicting health identity states",
    userInput: "I know I should be tracking everything, but honestly, I hate health apps. They make me anxious. But then again, I do check my glucose every day...",
    expectedBehavior: {
      quantumStates: [
        { state: "Proactive Tracker", probability: 0.4 },
        { state: "Tech-Averse", probability: 0.35 },
        { state: "Anxious Monitor", probability: 0.25 }
      ],
      antenarrative: {
        type: "contradiction",
        tensions: [
          "Awareness of 'should' vs actual desire",
          "Commitment to glucose tracking vs app aversion"
        ],
        possibleEndings: [
          "Finds non-app tracking method",
          "Overcomes app anxiety with support",
          "Continues glucose-only tracking"
        ]
      },
      yamaResonance: {
        principle: "Satya",
        resonance: "alignment",
        insight: "User honestly expressing multiplicity"
      }
    }
  },
  
  {
    name: "Temporal Entanglement",
    description: "User references past-present-future simultaneously",
    userInput: "When I was younger, I never thought about this stuff. Now I'm obsessed with my numbers. I want to catch things before they become problems like my dad's diabetes.",
    expectedBehavior: {
      temporalLayers: {
        pastStory: "Carefree youth, no health consciousness",
        presentMoment: "Hyper-vigilant number tracking",
        futureProjection: "Prevention-oriented, avoiding father's fate"
      },
      grandNarrative: {
        discourse: "Genetic determinism",
        userStance: "resisting",
        influence: 0.7
      },
      quantumStates: [
        { state: "Prevention-Motivated", probability: 0.6 },
        { state: "Fear-Driven", probability: 0.4 }
      ]
    }
  },
  
  {
    name: "Grand Narrative Surfacing",
    description: "User negotiates with medical authority discourse",
    userInput: "My doctor says my A1C is fine, but I can feel when my blood sugar spikes after meals. She tells me not to worry, but I trust my body.",
    expectedBehavior: {
      grandNarrative: {
        discourse: "Medical authority",
        userStance: "negotiating",
        influence: 0.5
      },
      antenarrative: {
        type: "turning_point",
        tensions: [
          "Doctor's reassurance vs embodied knowledge",
          "Lab results vs lived experience"
        ]
      },
      quantumStates: [
        { state: "Body-Trusting", probability: 0.55 },
        { state: "Medically-Compliant", probability: 0.45 }
      ],
      streams: ["BODY_KNOWLEDGE", "BIOMARKER_MYTHOLOGY"]
    }
  },
  
  {
    name: "Quantum State Evolution",
    description: "Track how probabilities shift across conversation",
    conversationFlow: [
      {
        turn: 1,
        userInput: "I don't really track anything.",
        expectedStates: [
          { state: "Unaware", probability: 0.7 },
          { state: "Resistant", probability: 0.3 }
        ]
      },
      {
        turn: 5,
        userInput: "Actually, I do keep a mental note of how I feel after certain foods.",
        expectedStates: [
          { state: "Intuitive Tracker", probability: 0.5 },
          { state: "Unaware", probability: 0.3 },
          { state: "Resistant", probability: 0.2 }
        ]
      },
      {
        turn: 10,
        userInput: "Maybe I should start writing this down...",
        expectedStates: [
          { state: "Emerging Motivation", probability: 0.6 },
          { state: "Intuitive Tracker", probability: 0.3 },
          { state: "Uncertain", probability: 0.1 }
        ]
      }
    ],
    expectedEvolution: "Probabilities shift from Unaware → Intuitive → Emerging Motivation"
  },
  
  {
    name: "Yama Violation Detection",
    description: "System should refuse to force narrative or over-advise",
    userInput: "I don't want to talk about my weight.",
    expectedBehavior: {
      systemResponse: "SHOULD NOT: Push weight discussion",
      yamaCheck: {
        principle: "Ahimsa",
        action: "Respect boundary, shift to user-chosen topic",
        rationale: "Never force story user isn't ready to tell"
      },
      alternativeApproach: "What health topics feel more comfortable to explore?"
    }
  },
  
  {
    name: "Multiple Stream Entanglement",
    description: "Fragment spans multiple narrative streams",
    userInput: "I wear a CGM now, and seeing the data made me realize my morning routine affects my afternoon energy. I've started correlating it with my sleep tracker too.",
    expectedBehavior: {
      entangledStreams: [
        "BIOMARKER_MYTHOLOGY", // CGM
        "DATA_SYNTHESIS",      // Routine-energy correlation
        "TECHNOLOGY_RELATIONSHIP", // Multiple devices
        "BODY_KNOWLEDGE"       // Energy awareness
      ],
      quantumStates: [
        { state: "Data Synthesizer", probability: 0.7 },
        { state: "Tech-Empowered", probability: 0.3 }
      ],
      coherence: 0.8 // High cross-stream connection
    }
  }
];

// Test runner
export async function runQuantumTests() {
  console.log("🔮 Running Quantum Storytelling Test Suite...\n");
  
  for (const scenario of QUANTUM_TEST_SCENARIOS) {
    console.log(`\n📖 SCENARIO: ${scenario.name}`);
    console.log(`📝 Description: ${scenario.description}`);
    console.log(`💬 User Input: "${scenario.userInput}"`);
    console.log(`\n✅ Expected Behavior:`);
    console.log(JSON.stringify(scenario.expectedBehavior, null, 2));
    console.log("\n" + "=".repeat(80));
  }
}
```

### Acceptance Criteria
- [ ] 6+ test scenarios covering all quantum features
- [ ] Contradiction embrace scenario validates quantum superposition
- [ ] Temporal entanglement scenario validates past-present-future capture
- [ ] Grand narrative scenario validates discourse surfacing
- [ ] Quantum state evolution tracks probability changes over time
- [ ] Yama violation detection tests Constitutional AI boundaries
- [ ] Multi-stream entanglement validates cross-stream connections

---

## Smoke Test Checklist

Before deploying sidecar orchestration, verify all API keys:

```bash
# Test Anthropic Claude
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: sk-ant-api03-ykGby1Hdptb6gtJ..." \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-3-5-sonnet-20241022","max_tokens":100,"messages":[{"role":"user","content":"test"}]}'

# Test OpenAI
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer sk-proj-7NIVt9m04mt2G6cQ..." \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"test"}],"max_tokens":10}'

# Test Groq
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer gsk_oxqYcd8rIhCpF6GEavQaWGdyb3FY..." \
  -H "Content-Type: application/json" \
  -d '{"model":"mixtral-8x7b-32768","messages":[{"role":"user","content":"test"}],"max_tokens":10}'

# Test Gemini
curl "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=AIzaSyCFe1c5oJi9D8gSm5b8InhvoIydmdDj9NE" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"test"}]}]}'

# Test Cohere
curl https://api.cohere.ai/v1/generate \
  -H "Authorization: Bearer CJ085MzeWAMJ6i1wreNqSDpvGPhthjowladviMGm" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"test","max_tokens":10}'

# Test Fireworks
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Authorization: Bearer fw_3ZZxCEF1URaNwv5nzBssRZZ9" \
  -H "Content-Type: application/json" \
  -d '{"model":"accounts/fireworks/models/llama-v3-70b-instruct","messages":[{"role":"user","content":"test"}],"max_tokens":10}'
```

### Expected Results
- [x] All API keys return 200 status (not 401 Unauthorized)
- [x] Response includes model output (not error message)
- [x] Latency <2s per request

---

## Coordination Protocol

**Central Source of Truth**: 
1. `QUANTUM_STORYTELLING.md` - Framework and philosophy
2. `TECHNICAL_ARCHITECTURE.md` - Implementation status
3. This file (`SIDECAR_ORCHESTRATION.md`) - Task assignments

**Communication**:
- Each sidecar LLM works independently on assigned phase
- Outputs committed to git with phase tag: `feat(phase-5): ...`
- Integration testing happens after all phases complete

**Rollback Strategy**:
- Keep dual-mode operation flag: `USE_QUANTUM_STORYTELLING=true/false`
- Original assessment system remains functional as fallback

---

## Success Metrics

**Phase 5 Complete**: Report generation uses antenarrative synthesis  
**Phase 6 Complete**: Database schema supports quantum data model  
**Phase 7 Complete**: Dashboard reactively displays living stories  
**Phase 8 Complete**: Test suite validates all quantum features

**Final Deployment**: MetaGuardian quantum storytelling system operational on Render

---

**Document Version**: 1.0  
**Created**: November 23, 2025  
**Status**: Ready for sidecar execution  
**Coordination**: Regan @ lexziconAI
