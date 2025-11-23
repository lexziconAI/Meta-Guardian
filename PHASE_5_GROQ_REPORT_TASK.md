# Phase 5: Transform Groq Report Generation to Quantum Storytelling

**Assigned Worker**: Groq Story Synthesis Agent  
**Model**: `moonshotai/kimi-k2-instruct-0905` (already deployed)  
**Priority**: HIGH  
**Estimated Tokens**: ~50K

---

## Objective

Transform the `backend/main.py` finalize-session endpoint from **static assessment report** to **living narrative synthesis** using David Boje's Quantum Storytelling framework.

---

## Context Files to Read First

1. `QUANTUM_STORYTELLING.md` - Framework explanation
2. `src/types/narrative-streams.ts` - Data structures
3. `backend/main.py` (lines 215-290) - Current implementation

---

## Current Implementation (TO REPLACE)

**Location**: `backend/main.py` lines 215-290

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

Apply Constitutional AI Yama principles to all recommendations.
"""
```

---

## Required Transformation

### New Prompt Structure

```python
story_synthesis_prompt = f"""
You are synthesizing a LIVING HEALTH STORY using David Boje's Quantum Storytelling framework.

## Session Data
Full Transcript: {session['transcript']}

Narrative Streams Captured:
{json.dumps(session.get('narrative_streams', {}), indent=2)}

Antenarrative Fragments:
{json.dumps(session.get('fragments', []), indent=2)}

Quantum States (Multiple Simultaneous Truths):
{json.dumps(session.get('quantum_states', []), indent=2)}

Temporal Layers (Past-Present-Future Entanglement):
{json.dumps(session.get('temporal_layers', {}), indent=2)}

Grand Narratives (Cultural Discourses User Negotiates With):
{json.dumps(session.get('grand_narratives', []), indent=2)}

---

## Your Task: Synthesize a Living Narrative (Not an Assessment)

### 1. HONOR ANTENARRATIVES (Don't Force Coherence)

Quote the user's exact speculative fragments:
- Memories: "{fragment.text}" (spoken when...)
- Speculations: "{fragment.text}" (imagining...)
- Contradictions: "{fragment.text}" vs "{fragment.text}" (both authentic)
- Bets: "{fragment.text}" (wagering on future...)

**CRITICAL**: Do NOT resolve tensions. List them as "Open Questions" the user is living with.

Example:
> "You said both 'I should be tracking everything' AND 'I hate health apps.' 
> These aren't contradictions to fix—they're the territory you're navigating."

### 2. EMBRACE QUANTUM SUPERPOSITION

Present multiple simultaneous health identities with probabilities:

```html
<div class="quantum-states">
  <h3>Your Health Story Exists in Multiple States</h3>
  <div class="state-bubble">
    <span class="probability">60%</span> Empowered Tracker
    <p class="evidence">Daily glucose monitoring, correlating food/energy</p>
  </div>
  <div class="state-bubble">
    <span class="probability">30%</span> Anxious Monitor
    <p class="evidence">Worry about numbers, fear of missing something</p>
  </div>
  <div class="state-bubble">
    <span class="probability">10%</span> Compliant Patient
    <p class="evidence">Following doctor's orders, deferring to authority</p>
  </div>
</div>
```

**RULE**: Probabilities must sum to 1.0. Show which states conflict and which reinforce each other.

### 3. MAP TEMPORAL ENTANGLEMENT

Create three-column visualization:

```html
<div class="temporal-collapse">
  <div class="column past">
    <h4>Past Health Stories</h4>
    <p>"{user's reference to younger self}"</p>
    <p>Theme: {extracted theme from past references}</p>
  </div>
  <div class="column present">
    <h4>Present Moment</h4>
    <p>"{current health practices quoted}"</p>
    <p>Theme: {what's happening now}</p>
  </div>
  <div class="column future">
    <h4>Imagined Futures</h4>
    <p>"{user's speculations about prevention}"</p>
    <p>Theme: {what user is authoring}</p>
  </div>
</div>
```

### 4. SURFACE GRAND NARRATIVES

Identify cultural/medical discourses the user is negotiating with:

```html
<div class="grand-narratives">
  <div class="narrative">
    <strong>Medical Authority</strong>
    <span class="stance">Negotiating</span>
    <p>You trust your doctor's A1C reading but also trust your body's 
       signals about blood sugar spikes she says "don't worry about."</p>
  </div>
  <div class="narrative">
    <strong>Quantified Self</strong>
    <span class="stance">Accepting</span>
    <p>You've bought into tracking culture—CGM, sleep data, correlations.</p>
  </div>
  <div class="narrative">
    <strong>Genetic Determinism</strong>
    <span class="stance">Resisting</span>
    <p>Father's diabetes looms large, but you're writing a different ending.</p>
  </div>
</div>
```

**Stances**: accepting, resisting, negotiating, transforming

### 5. OFFER STORY PATHS (Not Prescriptions)

Present 3 possible futures as narrative continuations:

```html
<div class="story-paths">
  <h3>Three Possible Chapters Ahead</h3>
  
  <div class="path">
    <h4>Path A: The Synthesizer</h4>
    <p>You lean into data integration—connecting all the threads. 
       CGM + sleep tracker + food journal become a unified dashboard. 
       You become fluent in your body's language.</p>
    <p><em>If this path calls to you: Consider...</em></p>
  </div>
  
  <div class="path">
    <h4>Path B: The Embodied Knower</h4>
    <p>You trust body signals over numbers. Less tracking, more tuning in. 
       The glucose monitor becomes one tool among many, not the oracle.</p>
    <p><em>If this path resonates: Explore...</em></p>
  </div>
  
  <div class="path">
    <h4>Path C: The Hybrid Navigator</h4>
    <p>You hold the tension—data AND intuition, doctor's wisdom AND 
       your own. You become bilingual: medical speak and body wisdom.</p>
    <p><em>If this path fits: Try...</em></p>
  </div>
</div>
```

**RULE**: Each path is a viable story continuation, not ranked or prescribed.

### 6. CONSTITUTIONAL AI: YAMA STORYTELLING ETHICS

Every narrative move must honor:

- **Ahimsa** (Non-harm): Never force a story the user isn't ready to tell
  - Check: Did you push into a topic the user avoided?
  - Fix: Acknowledge the boundary, don't pathologize it
  
- **Satya** (Truth): Honor contradictions as authentic (multiple truths)
  - Check: Did you resolve tensions falsely to create coherence?
  - Fix: Name the contradiction as the lived reality
  
- **Asteya** (Non-stealing): The story belongs to the user, not the system
  - Check: Did you claim authorship or interpret beyond evidence?
  - Fix: Use "You said..." not "You are..." or "You need..."
  
- **Brahmacharya** (Right energy): Match story depth to user's capacity
  - Check: Did you go deeper than the user's emotional readiness?
  - Fix: Offer depth as invitation, not requirement
  
- **Aparigraha** (Non-attachment): Share patterns without claiming ownership
  - Check: Did you get attached to a particular story outcome?
  - Fix: Present patterns as observations, not conclusions

---

## HTML Structure Requirements

### Overall Layout

```html
<!DOCTYPE html>
<html>
<head>
<style>
  body { 
    font-family: Georgia, serif; 
    max-width: 700px; 
    margin: 40px auto; 
    color: #2c3e50;
    line-height: 1.7;
  }
  .quantum-state-bubble {
    display: inline-block;
    margin: 10px;
    padding: 15px 25px;
    border-radius: 50px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    position: relative;
    animation: pulse 3s infinite;
  }
  .probability {
    font-size: 2em;
    font-weight: bold;
    display: block;
  }
  .temporal-collapse {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    margin: 30px 0;
  }
  .column {
    padding: 20px;
    border-left: 4px solid;
  }
  .column.past { border-color: #95a5a6; }
  .column.present { border-color: #3498db; }
  .column.future { border-color: #e74c3c; }
  
  .fragment-quote {
    background: #ecf0f1;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 20px 0;
    font-style: italic;
  }
  
  .story-path {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 25px;
    margin: 20px 0;
  }
  
  @keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.05); opacity: 1; }
  }
</style>
</head>
<body>
  <h1>Your Living Health Story</h1>
  <p class="subtitle">Synthesized {datetime.now().strftime('%B %d, %Y')}</p>
  
  <div class="intro">
    <p>This is not an assessment. This is your health story as it's unfolding—
       with all its contradictions, possibilities, and open questions.</p>
  </div>
  
  <!-- Quantum States Section -->
  <!-- Antenarrative Fragments Section -->
  <!-- Temporal Entanglement Section -->
  <!-- Grand Narratives Section -->
  <!-- Story Paths Section -->
  
  <div class="footer">
    <p><em>Remember: This story belongs to you. You are the author.</em></p>
    <p><small>MetaGuardian uses Constitutional AI (Yama principles) to ensure 
       your narrative autonomy is respected.</small></p>
  </div>
</body>
</html>
```

---

## Implementation Steps

### Step 1: Locate Current Code

File: `backend/main.py`  
Function: `finalize_session()`  
Lines: ~215-290

### Step 2: Replace Prompt

Find this block:
```python
report_prompt = f"""
Generate a comprehensive metabolic health readiness assessment report.
```

Replace entire prompt with story synthesis prompt above.

### Step 3: Update Data Extraction

**BEFORE** generating report, check if narrative data exists:

```python
# Try quantum storytelling data first
narrative_streams = session.get('narrative_streams', None)
fragments = session.get('fragments', [])
quantum_states = session.get('quantum_states', [])

# Fallback: If old assessment format, convert on the fly
if not narrative_streams and 'dimensions' in session:
    # Legacy conversion
    narrative_streams = convert_dimensions_to_streams(session['dimensions'])
    fragments = extract_fragments_from_transcript(session['transcript'])
    quantum_states = infer_quantum_states_from_evidence(session['evidence_log'])
```

### Step 4: Test Output

Generate sample report and verify:
- [ ] Quotes user's exact words (antenarrative fragments)
- [ ] Shows multiple quantum states with probabilities
- [ ] Displays past-present-future temporal collapse
- [ ] Identifies grand narratives user negotiates with
- [ ] Offers 3 story paths (not ranked prescriptions)
- [ ] HTML renders correctly in email clients
- [ ] No Yama principle violations

---

## Acceptance Criteria

- [ ] Report reads as "IN-THE-MAKING" not completed assessment
- [ ] Contradictions honored, not resolved
- [ ] User's words quoted directly (not paraphrased)
- [ ] Quantum states visualized with probabilities summing to 1.0
- [ ] Temporal entanglement shown (past-present-future)
- [ ] Grand narratives identified with user stance
- [ ] 3 story paths offered as equally valid continuations
- [ ] HTML uses organic/fractal visual language
- [ ] Yama principles verified (no forced narratives)
- [ ] Email renders correctly in Gmail/Outlook

---

## Test Case

**Input**:
```json
{
  "transcript": "User said: I check my glucose daily with a CGM... I should track more but I hate apps... My dad has diabetes and I don't want that...",
  "fragments": [
    {"type": "memory", "text": "My dad has diabetes", "tensions": ["fear", "motivation"]},
    {"type": "contradiction", "text": "I should track more but I hate apps", "tensions": ["compliance vs autonomy"]}
  ],
  "quantum_states": [
    {"state": "Empowered Tracker", "probability": 0.6},
    {"state": "Anxious Monitor", "probability": 0.3},
    {"state": "Reluctant User", "probability": 0.1}
  ]
}
```

**Expected Output**: HTML report that quotes both fragments, shows quantum states as bubbles, identifies "Genetic Determinism" as grand narrative being resisted, offers 3 story paths.

---

## Dependencies

- Groq API key already configured
- Model `moonshotai/kimi-k2-instruct-0905` already in use
- No new packages required

---

## Estimated Time

- Reading context: 10 min
- Implementation: 30 min
- Testing: 15 min
- **Total: ~1 hour**

---

**Ready to Execute**: Yes  
**Blocking Issues**: None  
**Contact**: Return completed code to main orchestrator
