# Phase 7: Frontend State Handler Transformation

## 🎯 Mission
Transform `LiveVoiceCoach.tsx` from assessment-based state management to quantum narrative state handling, enabling real-time visualization of narrative superposition, temporal entanglement, and story quality metrics.

## 🤖 Assigned LLM
**OpenAI GPT-5** (`gpt-5`)
- **Specialization**: Complex React state logic, TypeScript refactoring, real-time WebSocket integration
- **Why GPT-5**: Proven track record with OpenAI Realtime API integration, strong TypeScript support, excellent at preserving existing functionality while adding quantum features

---

## 📋 Prerequisites
- [x] Phase 1-4 complete (quantum data model exists in `src/types/narrative-streams.ts`)
- [x] QUANTUM_STORYTELLING_PROMPT deployed in system instructions
- [x] `updateNarrativeState` tool definition available
- [ ] **Dependency Installation Required**: `npm install framer-motion` for quantum dashboard animations

---

## 📂 Target File
**Location**: `components/LiveVoiceCoach.tsx` (lines 350-410)

---

## 🔍 Current State Analysis

### Existing Function (Assessment-based)
```typescript
const handleToolCall = (args: any) => {
  setSessionState((prev: SessionState) => {
    const updated = { ...prev };
    
    // Update dimensions
    if (args.dimensions) {
      Object.keys(args.dimensions).forEach((dim) => {
        updated.dimensions[dim] = {
          ...updated.dimensions[dim],
          ...args.dimensions[dim]
        };
      });
    }
    
    // Log new evidence
    if (args.newEvidence) {
      updated.evidenceLog = [
        ...prev.evidenceLog,
        { ...args.newEvidence, timestamp: new Date().toISOString() }
      ];
    }
    
    // Track contradictions
    if (args.contradiction) {
      updated.contradictions = [
        ...prev.contradictions,
        args.contradiction
      ];
    }
    
    // Update phase
    if (args.phase) {
      updated.conversationPhase = args.phase;
    }
    
    // Update score history for chart
    const currentTime = (Date.now() - sessionStartTime) / 1000;
    updated.scoreHistory = [
      ...prev.scoreHistory,
      {
        time: currentTime,
        HL: updated.dimensions.HL.score,
        CM: updated.dimensions.CM.score,
        DI: updated.dimensions.DI.score,
        DL: updated.dimensions.DL.score,
        PR: updated.dimensions.PR.score
      }
    ];
    
    return updated;
  });
};
```

### Problems with Current Implementation
1. **Assessment-centric**: Updates `dimensions` object for scores, not narrative streams
2. **No quantum state handling**: Missing probability normalization, superposition tracking
3. **No entanglement detection**: Doesn't track cross-stream narrative connections
4. **No story quality metrics**: Missing coherence, fluidity, authenticity calculations
5. **Static visualization**: No animation states for quantum transitions

---

## 🎯 Target State (Quantum Narrative)

### Required Transformation
```typescript
const handleToolCall = (args: any) => {
  setSessionState((prev: SessionState) => {
    const updated = { ...prev };
    
    // ==================================================
    // QUANTUM NARRATIVE STATE UPDATES
    // ==================================================
    
    // 1. UPDATE NARRATIVE STREAMS (not dimensions)
    if (args.narrativeStreams) {
      Object.keys(args.narrativeStreams).forEach((streamId) => {
        const stream = args.narrativeStreams[streamId];
        updated.narrativeStreams[streamId] = {
          ...updated.narrativeStreams[streamId],
          ...stream,
          lastUpdated: new Date().toISOString()
        };
      });
    }
    
    // 2. LOG ANTENARRATIVE FRAGMENTS
    if (args.antenarrative) {
      const fragment: AntenarativeFragment = {
        id: `ante_${Date.now()}`,
        content: args.antenarrative.content,
        type: args.antenarrative.type, // memory, speculation, contradiction, bet, turning_point
        narrativeStream: args.antenarrative.narrativeStream,
        tensions: args.antenarrative.tensions || [],
        possibleEndings: args.antenarrative.possibleEndings || [],
        timestamp: new Date().toISOString()
      };
      
      updated.antenarrative.fragments = [
        ...prev.antenarrative.fragments,
        fragment
      ];
    }
    
    // 3. UPDATE QUANTUM STATES (with probability normalization)
    if (args.quantumStates) {
      const states = args.quantumStates;
      
      // Normalize probabilities to sum to 1.0
      const totalProbability = states.reduce((sum: number, s: any) => sum + s.probability, 0);
      const normalizedStates = states.map((s: any) => ({
        ...s,
        probability: totalProbability > 0 ? s.probability / totalProbability : 0
      }));
      
      updated.quantumStates = normalizedStates;
    }
    
    // 4. TRACK TEMPORAL ENTANGLEMENT
    if (args.temporalLayer) {
      const layer: TemporalLayer = {
        id: `temp_${Date.now()}`,
        type: args.temporalLayer.type, // past_memory, present_moment, future_speculation, collapsed_now
        content: args.temporalLayer.content,
        relatedStreams: args.temporalLayer.relatedStreams || [],
        entanglementStrength: args.temporalLayer.entanglementStrength || 0,
        timestamp: new Date().toISOString()
      };
      
      updated.temporalLayers = [
        ...prev.temporalLayers,
        layer
      ];
    }
    
    // 5. DETECT GRAND NARRATIVES
    if (args.grandNarrative) {
      const gn: GrandNarrative = {
        id: `gn_${Date.now()}`,
        name: args.grandNarrative.name, // e.g., "Medical Authority", "Quantified Self"
        type: args.grandNarrative.type, // medical, cultural, technological, personal
        userStance: args.grandNarrative.userStance, // accepting, resisting, negotiating, transforming
        influence: args.grandNarrative.influence || 0,
        manifestations: args.grandNarrative.manifestations || [],
        timestamp: new Date().toISOString()
      };
      
      updated.grandNarratives = [
        ...prev.grandNarratives,
        gn
      ];
    }
    
    // 6. CALCULATE STORY QUALITY METRICS
    const coherence = calculateCoherence(updated);
    const fluidity = calculateFluidity(updated);
    const authenticity = calculateAuthenticity(updated);
    
    updated.storyQuality = {
      coherence,
      fluidity,
      authenticity,
      overallScore: (coherence + fluidity + authenticity) / 3
    };
    
    // 7. UPDATE CONVERSATION PHASE
    if (args.phase) {
      updated.conversationPhase = args.phase; // INVOCATION, EMERGENCE, ENTANGLEMENT, CRYSTALLIZATION, OPENING
    }
    
    // 8. TRACK YAMA RESONANCES (Constitutional AI ethics)
    if (args.yamaResonance) {
      updated.yamaResonances = [
        ...prev.yamaResonances,
        {
          principle: args.yamaResonance.principle, // ahimsa, satya, asteya, brahmacharya, aparigraha
          moment: args.yamaResonance.moment,
          strength: args.yamaResonance.strength,
          timestamp: new Date().toISOString()
        }
      ];
    }
    
    // 9. UPDATE VISUALIZATION ANIMATION STATE
    updated.animationTrigger = {
      type: 'quantum_update',
      timestamp: Date.now(),
      affectedStreams: args.narrativeStreams ? Object.keys(args.narrativeStreams) : []
    };
    
    return updated;
  });
};

// ==================================================
// HELPER FUNCTIONS: STORY QUALITY METRICS
// ==================================================

function calculateCoherence(state: SessionState): number {
  // Coherence = How well antenarrative fragments connect across streams
  const fragments = state.antenarrative.fragments;
  if (fragments.length < 2) return 0;
  
  let connections = 0;
  let totalPossible = 0;
  
  for (let i = 0; i < fragments.length; i++) {
    for (let j = i + 1; j < fragments.length; j++) {
      totalPossible++;
      
      // Check if fragments share narrative streams or tensions
      const sharesStream = fragments[i].narrativeStream === fragments[j].narrativeStream;
      const sharesTension = fragments[i].tensions.some(t => 
        fragments[j].tensions.includes(t)
      );
      
      if (sharesStream || sharesTension) connections++;
    }
  }
  
  return totalPossible > 0 ? connections / totalPossible : 0;
}

function calculateFluidity(state: SessionState): number {
  // Fluidity = How smoothly story moves through temporal layers
  const layers = state.temporalLayers;
  if (layers.length < 2) return 0;
  
  let smoothTransitions = 0;
  
  for (let i = 1; i < layers.length; i++) {
    const prev = layers[i - 1];
    const curr = layers[i];
    
    // Check if temporal layers share related streams
    const sharedStreams = prev.relatedStreams.filter(s => 
      curr.relatedStreams.includes(s)
    );
    
    if (sharedStreams.length > 0) {
      smoothTransitions += prev.entanglementStrength * curr.entanglementStrength;
    }
  }
  
  return smoothTransitions / (layers.length - 1);
}

function calculateAuthenticity(state: SessionState): number {
  // Authenticity = Quantum state diversity + contradiction embrace
  const quantumStates = state.quantumStates;
  if (quantumStates.length === 0) return 0;
  
  // Shannon entropy of probability distribution (higher = more authentic)
  let entropy = 0;
  for (const qs of quantumStates) {
    if (qs.probability > 0) {
      entropy -= qs.probability * Math.log2(qs.probability);
    }
  }
  
  // Normalize to 0-1 range (max entropy for 5 states = log2(5) ≈ 2.32)
  const maxEntropy = Math.log2(quantumStates.length);
  return maxEntropy > 0 ? entropy / maxEntropy : 0;
}
```

---

## 🔧 Implementation Steps

### Step 1: Install Dependency
```bash
cd "c:\Users\regan\ID SYSTEM\MetaGuardian"
npm install framer-motion
```

### Step 2: Update Type Imports
**File**: `components/LiveVoiceCoach.tsx` (top of file)

Add imports:
```typescript
import { 
  NarrativeStream, 
  AntenarativeFragment, 
  QuantumState, 
  TemporalLayer, 
  GrandNarrative, 
  YamaResonance 
} from '../src/types/narrative-streams';
```

### Step 3: Replace `handleToolCall` Function
**Location**: Lines 350-410

Replace entire function with quantum version above.

### Step 4: Add Helper Functions
**Location**: After `handleToolCall` (around line 415)

Add the three calculation functions:
- `calculateCoherence()`
- `calculateFluidity()`
- `calculateAuthenticity()`

### Step 5: Update SessionState Interface
**File**: `types.ts`

Ensure `SessionState` includes:
```typescript
interface SessionState {
  // Quantum fields
  narrativeStreams: Record<string, NarrativeStream>;
  antenarrative: {
    fragments: AntenarativeFragment[];
  };
  quantumStates: QuantumState[];
  temporalLayers: TemporalLayer[];
  grandNarratives: GrandNarrative[];
  yamaResonances: YamaResonance[];
  storyQuality: {
    coherence: number;
    fluidity: number;
    authenticity: number;
    overallScore: number;
  };
  animationTrigger: {
    type: string;
    timestamp: number;
    affectedStreams: string[];
  };
  conversationPhase: string;
  
  // Legacy fields (keep for backward compatibility)
  dimensions?: Record<string, any>;
  evidenceLog?: any[];
  contradictions?: any[];
}
```

### Step 6: Test WebSocket Integration
Verify that `updateNarrativeState` tool calls from OpenAI Realtime API successfully trigger the new handler.

---

## 🧪 Test Cases

### Test 1: Antenarrative Fragment Capture
**Input**: OpenAI calls `updateNarrativeState` with:
```json
{
  "antenarrative": {
    "content": "I remember when my doctor said my A1C was pre-diabetic... but I also feel healthier than ever?",
    "type": "contradiction",
    "narrativeStream": "BIOMARKER_MYTHOLOGY",
    "tensions": ["medical_authority_vs_lived_experience"],
    "possibleEndings": ["Accept diagnosis", "Trust body wisdom", "Seek second opinion"]
  }
}
```

**Expected Behavior**:
- Fragment added to `state.antenarrative.fragments`
- Fragment has unique ID with timestamp
- `state.storyQuality.authenticity` increases (contradiction embrace)

### Test 2: Quantum State Probability Normalization
**Input**:
```json
{
  "quantumStates": [
    {"identity": "Empowered Tracker", "probability": 0.8},
    {"identity": "Anxious Monitor", "probability": 0.4},
    {"identity": "Compliant Patient", "probability": 0.2}
  ]
}
```

**Expected Behavior**:
- Total probability normalized to 1.0
- Result: [0.571, 0.286, 0.143] (0.8/1.4, 0.4/1.4, 0.2/1.4)
- `state.storyQuality.authenticity` reflects entropy

### Test 3: Temporal Entanglement Tracking
**Input**:
```json
{
  "temporalLayer": {
    "type": "collapsed_now",
    "content": "My past sugar cravings, present blood work, and future diabetes risk all feel connected right now",
    "relatedStreams": ["BODY_KNOWLEDGE", "BIOMARKER_MYTHOLOGY", "FUTURE_HEALTH_IMAGINARY"],
    "entanglementStrength": 0.85
  }
}
```

**Expected Behavior**:
- Layer added to `state.temporalLayers`
- `state.storyQuality.fluidity` increases (high entanglement)
- Three narrative streams marked as updated in `animationTrigger`

### Test 4: Grand Narrative Detection
**Input**:
```json
{
  "grandNarrative": {
    "name": "Quantified Self Ideology",
    "type": "technological",
    "userStance": "negotiating",
    "influence": 0.7,
    "manifestations": [
      "I love tracking my steps",
      "But sometimes I feel enslaved by the numbers"
    ]
  }
}
```

**Expected Behavior**:
- Grand narrative added to `state.grandNarratives`
- User stance preserved as "negotiating" (not forced to single position)
- Manifestations array captures both attraction and resistance

### Test 5: Story Quality Metrics
**Scenario**: After 10 tool calls capturing diverse fragments

**Expected Behavior**:
- `coherence`: 0.6-0.8 (fragments connect across streams)
- `fluidity`: 0.5-0.7 (smooth temporal transitions)
- `authenticity`: 0.7-0.9 (high quantum state diversity)
- `overallScore`: Average of above three

### Test 6: Animation Trigger
**Input**: Any `updateNarrativeState` call

**Expected Behavior**:
- `state.animationTrigger.type` set to `'quantum_update'`
- `timestamp` updated to current time
- `affectedStreams` lists which narrative streams changed
- Dashboard component receives trigger for framer-motion animations

---

## ✅ Acceptance Criteria

- [ ] `npm install framer-motion` completes successfully
- [ ] `handleToolCall` function replaced with quantum version
- [ ] Helper functions (`calculateCoherence`, `calculateFluidity`, `calculateAuthenticity`) added
- [ ] `SessionState` interface updated in `types.ts`
- [ ] All 6 test cases pass
- [ ] No TypeScript errors in `LiveVoiceCoach.tsx`
- [ ] Existing OpenAI WebSocket connection still works
- [ ] Dashboard receives animation triggers
- [ ] Story quality metrics calculate correctly (0-1 range)
- [ ] Probability normalization ensures quantum states sum to 1.0

---

## 📊 Success Metrics

| Metric | Target | How to Verify |
|--------|--------|---------------|
| TypeScript Compilation | 0 errors | `npm run build` |
| Function Call Handling | 100% | All `updateNarrativeState` calls processed |
| Probability Normalization | Always sums to 1.0 | Unit test quantum states |
| Story Quality Range | 0.0 - 1.0 | Check min/max values in state |
| Animation Triggers | Every tool call | Console log animation events |
| Backward Compatibility | Assessment mode still works | Old `updateAssessmentState` preserved |

---

## 🔗 Dependencies

**Must Complete Before Starting**:
- Phase 1: Quantum data model (`src/types/narrative-streams.ts`) ✅
- Phase 2: QUANTUM_STORYTELLING_PROMPT ✅
- Phase 3: `updateNarrativeState` tool definition ✅

**Must Complete After**:
- Phase 6: Backend schema supports quantum fields (narrative_streams table exists)
- Phase 8: Test scenarios validate state transformations

---

## 📚 Reference Documents

1. **QUANTUM_STORYTELLING.md**: Theoretical framework (David Boje's quantum narratology)
2. **TECHNICAL_ARCHITECTURE.md**: Current system design (this document)
3. **src/types/narrative-streams.ts**: TypeScript interfaces for quantum data model
4. **components/LiveVoiceCoach.tsx**: Current implementation (assessment mode)

---

## 🚨 Common Pitfalls

1. **Forgetting probability normalization**: Always ensure quantum states sum to 1.0
2. **Mutating state directly**: Use spread operators to create new objects
3. **Missing timestamp fields**: All temporal data needs timestamps
4. **Type mismatches**: Import types from `narrative-streams.ts`, not `assessment.ts`
5. **Animation performance**: Don't trigger animations on every keystroke, only on tool calls

---

## 💡 Optimization Notes

- **Performance**: Story quality calculations are O(n²) for coherence. Consider caching for >50 fragments.
- **Memory**: Temporal layers accumulate over session. Consider pruning layers older than 5 minutes for long sessions.
- **Animation**: Use `framer-motion`'s `layout` prop for smooth quantum state transitions without manual animation code.

---

## 🎯 Next Steps After Completion

1. Test integration with Phase 6 backend (verify narrative_streams table CRUD operations)
2. Create visual regression tests for quantum dashboard animations
3. Performance profiling: Ensure story quality calculations don't block UI (<16ms)
4. User testing: Compare perceived naturalness vs. assessment mode

---

**Task Specification Version**: 1.0  
**Created**: November 23, 2025  
**Estimated Effort**: 3-4 hours (GPT-5)  
**Priority**: HIGH (blocks Phase 8 test scenarios)
