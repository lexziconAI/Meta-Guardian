# Phase 6: Backend Database Schema Transformation

**Assigned Worker**: Claude Sonnet 4.5 Schema Agent  
**Model**: `claude-sonnet-4-5` (API key confirmed valid)  
**Priority**: HIGH  
**Estimated Tokens**: ~80K

---

## Objective

Transform backend database schema from **static dimension scoring** to **quantum narrative streams** with support for antenarratives, quantum states, temporal layers, and grand narratives.

---

## Context Files to Read First

1. `src/types/narrative-streams.ts` - TypeScript data model (source of truth)
2. `backend/database.py` - Current SQLite implementation
3. `backend/schemas.py` - Current Pydantic models
4. `QUANTUM_STORYTELLING.md` - Framework explanation

---

## Current Schema (TO TRANSFORM)

**File**: `backend/database.py`

```sql
-- Current tables
CREATE TABLE sessions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    created_at TIMESTAMP,
    transcript TEXT,
    dimensions JSON  -- {HL: {score, confidence}, CM: {...}, ...}
);

CREATE TABLE evidence_log (
    id INTEGER PRIMARY KEY,
    session_id TEXT,
    dimension TEXT,  -- HL, CM, DI, DL, PR
    type TEXT,
    summary TEXT,
    timestamp TIMESTAMP
);
```

---

## Required New Schema

### Table 1: narrative_streams

Replaces: `dimensions` JSON column

```sql
CREATE TABLE narrative_streams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    stream_id TEXT NOT NULL,  -- BODY_KNOWLEDGE, BIOMARKER_MYTHOLOGY, etc.
    coherence REAL DEFAULT 0.0,  -- 0.0-1.0 how well fragments connect
    fluidity REAL DEFAULT 0.0,   -- 0.0-1.0 how much still becoming
    authenticity REAL DEFAULT 0.0,  -- 0.0-1.0 alignment with lived reality
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
    UNIQUE(session_id, stream_id)
);

CREATE INDEX idx_narrative_streams_session ON narrative_streams(session_id);
```

### Table 2: antenarrative_fragments

Replaces: `evidence_log` table

```sql
CREATE TABLE antenarrative_fragments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stream_id INTEGER NOT NULL,
    text TEXT NOT NULL,  -- User's exact words
    type TEXT NOT NULL,  -- memory, speculation, contradiction, desire, fear, bet, turning_point
    tensions TEXT,  -- JSON array ["tension1", "tension2"]
    possible_endings TEXT,  -- JSON array ["ending1", "ending2"]
    entangled_with TEXT,  -- JSON array of fragment IDs
    superposition_states TEXT,  -- JSON array of alternative interpretations
    emotional_tone TEXT,  -- joy, fear, curiosity, resistance, hope, etc.
    energy_level TEXT,  -- high, medium, low
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id) ON DELETE CASCADE
);

CREATE INDEX idx_fragments_stream ON antenarrative_fragments(stream_id);
CREATE INDEX idx_fragments_type ON antenarrative_fragments(type);
CREATE INDEX idx_fragments_timestamp ON antenarrative_fragments(timestamp);
```

### Table 3: quantum_states (NEW)

Tracks multiple simultaneous health identities with probabilities

```sql
CREATE TABLE quantum_states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stream_id INTEGER NOT NULL,
    state TEXT NOT NULL,  -- e.g., "Empowered Tracker"
    probability REAL NOT NULL,  -- 0.0-1.0 (all states for stream sum to 1.0)
    evidence_threads TEXT,  -- JSON array of supporting quotes
    conflicts_with TEXT,  -- JSON array of state names that contradict this
    reinforces TEXT,  -- JSON array of state names that support this
    evolution TEXT,  -- JSON array [{time, probability}, ...] tracking changes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id) ON DELETE CASCADE,
    CHECK(probability >= 0.0 AND probability <= 1.0)
);

CREATE INDEX idx_quantum_states_stream ON quantum_states(stream_id);

-- Trigger to validate probabilities sum to ~1.0 per stream
CREATE TRIGGER validate_quantum_probabilities
AFTER INSERT ON quantum_states
BEGIN
    SELECT CASE
        WHEN (SELECT SUM(probability) FROM quantum_states WHERE stream_id = NEW.stream_id) > 1.01
        THEN RAISE(ABORT, 'Quantum state probabilities exceed 1.0 for stream')
    END;
END;
```

### Table 4: temporal_layers (NEW)

Captures past-present-future collapse

```sql
CREATE TABLE temporal_layers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stream_id INTEGER NOT NULL,
    past_story TEXT,  -- User's references to younger self/history
    present_moment TEXT,  -- Current health practices
    future_projection TEXT,  -- Imagined/hoped-for health future
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id) ON DELETE CASCADE,
    UNIQUE(stream_id)  -- One temporal layer per stream
);

CREATE INDEX idx_temporal_stream ON temporal_layers(stream_id);
```

### Table 5: grand_narratives (NEW)

Tracks cultural/medical discourses user negotiates with

```sql
CREATE TABLE grand_narratives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stream_id INTEGER NOT NULL,
    discourse TEXT NOT NULL,  -- Medical authority, Quantified self, Genetic determinism, etc.
    user_stance TEXT NOT NULL,  -- accepting, resisting, negotiating, transforming
    influence REAL DEFAULT 0.5,  -- 0.0-1.0 how much this shapes user's story
    evidence_quotes TEXT,  -- JSON array of user quotes showing engagement
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stream_id) REFERENCES narrative_streams(id) ON DELETE CASCADE,
    CHECK(user_stance IN ('accepting', 'resisting', 'negotiating', 'transforming')),
    CHECK(influence >= 0.0 AND influence <= 1.0)
);

CREATE INDEX idx_grand_narratives_stream ON grand_narratives(stream_id);
CREATE INDEX idx_grand_narratives_discourse ON grand_narratives(discourse);
```

### Table 6: yama_resonances (NEW)

Tracks Constitutional AI ethical alignment per fragment

```sql
CREATE TABLE yama_resonances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fragment_id INTEGER NOT NULL,
    principle TEXT NOT NULL,  -- Ahimsa, Satya, Asteya, Brahmacharya, Aparigraha
    resonance TEXT NOT NULL,  -- alignment, tension, exploration
    insight TEXT,  -- What this tells us about user's ethical navigation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (fragment_id) REFERENCES antenarrative_fragments(id) ON DELETE CASCADE,
    CHECK(principle IN ('Ahimsa', 'Satya', 'Asteya', 'Brahmacharya', 'Aparigraha')),
    CHECK(resonance IN ('alignment', 'tension', 'exploration'))
);

CREATE INDEX idx_yama_fragment ON yama_resonances(fragment_id);
CREATE INDEX idx_yama_principle ON yama_resonances(principle);
```

### Update sessions table

Add quantum metadata:

```sql
ALTER TABLE sessions ADD COLUMN phase TEXT DEFAULT 'INVOCATION';  
-- INVOCATION, EMERGENCE, ENTANGLEMENT, CRYSTALLIZATION, OPENING

ALTER TABLE sessions ADD COLUMN overall_coherence REAL DEFAULT 0.0;
ALTER TABLE sessions ADD COLUMN narrative_complexity REAL DEFAULT 0.0;
ALTER TABLE sessions ADD COLUMN story_vitality REAL DEFAULT 0.0;
ALTER TABLE sessions ADD COLUMN yama_balance TEXT;  -- JSON {Ahimsa: 0.8, Satya: 0.9, ...}
```

---

## Migration Script

**File**: `backend/migrate_to_quantum.py` (NEW)

```python
"""
Migration script: Assessment → Quantum Storytelling Schema
Safely converts existing sessions to new narrative structure
"""

import sqlite3
import json
from datetime import datetime

def migrate_database(db_path='metaguardian.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🔄 Starting Quantum Storytelling migration...")
    
    # Step 1: Backup existing database
    backup_path = f'{db_path}.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    backup_conn = sqlite3.connect(backup_path)
    conn.backup(backup_conn)
    backup_conn.close()
    print(f"✅ Backup created: {backup_path}")
    
    # Step 2: Create new tables
    with open('backend/schema_quantum.sql', 'r') as f:
        schema = f.read()
        cursor.executescript(schema)
    print("✅ New quantum tables created")
    
    # Step 3: Migrate existing sessions
    cursor.execute("SELECT id, user_id, created_at, transcript, dimensions FROM sessions")
    sessions = cursor.fetchall()
    
    for session_id, user_id, created_at, transcript, dimensions_json in sessions:
        try:
            dimensions = json.loads(dimensions_json) if dimensions_json else {}
            
            # Convert dimensions → narrative streams
            stream_mapping = {
                'HL': 'BODY_KNOWLEDGE',
                'CM': 'BIOMARKER_MYTHOLOGY',
                'DI': 'DATA_SYNTHESIS',
                'DL': 'TECHNOLOGY_RELATIONSHIP',
                'PR': 'FUTURE_HEALTH_IMAGINARY'
            }
            
            for old_code, new_stream_id in stream_mapping.items():
                if old_code in dimensions:
                    # Create narrative stream
                    cursor.execute("""
                        INSERT INTO narrative_streams 
                        (session_id, stream_id, coherence, fluidity, authenticity)
                        VALUES (?, ?, ?, ?, ?)
                    """, (
                        session_id,
                        new_stream_id,
                        dimensions[old_code].get('confidence', 0) / 5.0,  # Convert to 0-1
                        1.0 - (dimensions[old_code].get('score', 0) / 5.0),  # Inverse of score = fluidity
                        dimensions[old_code].get('confidence', 0) / 5.0
                    ))
                    
                    stream_db_id = cursor.lastrowid
                    
                    # Infer quantum state from score
                    score = dimensions[old_code].get('score', 0)
                    if score >= 4:
                        state_name = f"Advanced {new_stream_id.replace('_', ' ').title()}"
                        probability = 0.7
                    elif score >= 2.5:
                        state_name = f"Developing {new_stream_id.replace('_', ' ').title()}"
                        probability = 0.6
                    else:
                        state_name = f"Emerging {new_stream_id.replace('_', ' ').title()}"
                        probability = 0.5
                    
                    cursor.execute("""
                        INSERT INTO quantum_states
                        (stream_id, state, probability, evidence_threads, evolution)
                        VALUES (?, ?, ?, ?, ?)
                    """, (
                        stream_db_id,
                        state_name,
                        probability,
                        json.dumps([]),
                        json.dumps([{"time": created_at, "probability": probability}])
                    ))
            
            print(f"✅ Migrated session {session_id}")
            
        except Exception as e:
            print(f"⚠️  Error migrating session {session_id}: {e}")
            continue
    
    # Step 4: Migrate evidence_log → antenarrative_fragments
    cursor.execute("SELECT id, session_id, dimension, type, summary, timestamp FROM evidence_log")
    evidence_entries = cursor.fetchall()
    
    for _, session_id, dimension, evidence_type, summary, timestamp in evidence_entries:
        # Find corresponding stream
        stream_id_str = stream_mapping.get(dimension)
        if stream_id_str:
            cursor.execute("""
                SELECT id FROM narrative_streams 
                WHERE session_id = ? AND stream_id = ?
            """, (session_id, stream_id_str))
            result = cursor.fetchone()
            if result:
                stream_db_id = result[0]
                
                # Convert to antenarrative fragment
                fragment_type = 'memory' if evidence_type == 'contextual' else 'speculation'
                
                cursor.execute("""
                    INSERT INTO antenarrative_fragments
                    (stream_id, text, type, tensions, possible_endings, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    stream_db_id,
                    summary,  # Use evidence summary as fragment text
                    fragment_type,
                    json.dumps([]),
                    json.dumps([]),
                    timestamp
                ))
    
    print(f"✅ Migrated {len(evidence_entries)} evidence entries to fragments")
    
    conn.commit()
    conn.close()
    
    print("\n🎉 Migration complete! Database ready for quantum storytelling.")
    print(f"   Backup saved to: {backup_path}")

if __name__ == '__main__':
    migrate_database()
```

---

## Pydantic Schema Updates

**File**: `backend/schemas.py` (UPDATE)

```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Literal
from datetime import datetime

class AntenarativeFragment(BaseModel):
    text: str = Field(..., description="User's exact words")
    type: Literal['memory', 'speculation', 'contradiction', 'desire', 'fear', 'bet', 'turning_point']
    tensions: List[str] = Field(default_factory=list)
    possible_endings: List[str] = Field(default_factory=list)
    entangled_with: List[str] = Field(default_factory=list, description="IDs of related fragments")
    superposition_states: List[str] = Field(default_factory=list)
    emotional_tone: Optional[str] = None
    energy_level: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class QuantumState(BaseModel):
    state: str = Field(..., description="Health identity name")
    probability: float = Field(..., ge=0.0, le=1.0)
    evidence_threads: List[str] = Field(default_factory=list)
    conflicts_with: Optional[List[str]] = None
    reinforces: Optional[List[str]] = None
    evolution: List[dict] = Field(default_factory=list)
    
    @validator('probability')
    def validate_probability(cls, v):
        if not 0.0 <= v <= 1.0:
            raise ValueError('Probability must be between 0.0 and 1.0')
        return v

class TemporalLayers(BaseModel):
    past_story: str = Field(default="")
    present_moment: str = Field(default="")
    future_projection: str = Field(default="")

class GrandNarrative(BaseModel):
    discourse: str = Field(..., description="Cultural/medical discourse name")
    user_stance: Literal['accepting', 'resisting', 'negotiating', 'transforming']
    influence: float = Field(default=0.5, ge=0.0, le=1.0)
    evidence_quotes: List[str] = Field(default_factory=list)

class YamaResonance(BaseModel):
    principle: Literal['Ahimsa', 'Satya', 'Asteya', 'Brahmacharya', 'Aparigraha']
    resonance: Literal['alignment', 'tension', 'exploration']
    insight: Optional[str] = None

class NarrativeStream(BaseModel):
    stream_id: Literal['BODY_KNOWLEDGE', 'BIOMARKER_MYTHOLOGY', 'DATA_SYNTHESIS', 
                       'TECHNOLOGY_RELATIONSHIP', 'FUTURE_HEALTH_IMAGINARY']
    fragments: List[AntenarativeFragment] = Field(default_factory=list)
    possible_states: List[QuantumState] = Field(default_factory=list)
    temporal_layers: Optional[TemporalLayers] = None
    grand_narratives: List[GrandNarrative] = Field(default_factory=list)
    coherence: float = Field(default=0.0, ge=0.0, le=1.0)
    fluidity: float = Field(default=0.0, ge=0.0, le=1.0)
    authenticity: float = Field(default=0.0, ge=0.0, le=1.0)
    
    @validator('possible_states')
    def validate_probabilities_sum(cls, v):
        if v:
            total_prob = sum(state.probability for state in v)
            if not (0.99 <= total_prob <= 1.01):  # Allow small floating point error
                raise ValueError(f'Quantum state probabilities must sum to ~1.0, got {total_prob}')
        return v

class QuantumStorySession(BaseModel):
    session_id: str
    user_id: str
    streams: List[NarrativeStream] = Field(default_factory=list)
    phase: Literal['INVOCATION', 'EMERGENCE', 'ENTANGLEMENT', 'CRYSTALLIZATION', 'OPENING'] = 'INVOCATION'
    overall_coherence: float = Field(default=0.0, ge=0.0, le=1.0)
    narrative_complexity: float = Field(default=0.0, ge=0.0, le=1.0)
    story_vitality: float = Field(default=0.0, ge=0.0, le=1.0)
    yama_balance: dict = Field(default_factory=dict)
    transcript: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

---

## Implementation Checklist

- [ ] Read `src/types/narrative-streams.ts` to match TypeScript types
- [ ] Create `backend/schema_quantum.sql` with all 6 new tables
- [ ] Update `backend/database.py` initialization to run new schema
- [ ] Create `backend/migrate_to_quantum.py` migration script
- [ ] Update `backend/schemas.py` with Pydantic models
- [ ] Add helper functions to `backend/database.py`:
  - `create_narrative_stream(session_id, stream_id)`
  - `add_antenarrative_fragment(stream_id, fragment_data)`
  - `update_quantum_states(stream_id, states)`
  - `set_temporal_layers(stream_id, layers)`
  - `add_grand_narrative(stream_id, narrative)`
- [ ] Test migration with sample data
- [ ] Verify foreign key constraints work
- [ ] Verify quantum probability validation triggers
- [ ] Create rollback script (revert to backup)

---

## Test Cases

### Test 1: Schema Creation
```python
# Run schema creation
python backend/migrate_to_quantum.py

# Verify tables exist
sqlite3 metaguardian.db ".tables"
# Should show: narrative_streams, antenarrative_fragments, quantum_states, etc.
```

### Test 2: Insert Quantum Data
```python
# Insert narrative stream
INSERT INTO narrative_streams (session_id, stream_id, coherence, fluidity, authenticity)
VALUES ('test-session', 'BODY_KNOWLEDGE', 0.7, 0.5, 0.8);

# Insert quantum states
INSERT INTO quantum_states (stream_id, state, probability)
VALUES 
  (1, 'Empowered Tracker', 0.6),
  (1, 'Anxious Monitor', 0.4);

# Verify probabilities sum to 1.0
SELECT SUM(probability) FROM quantum_states WHERE stream_id = 1;
# Should return: 1.0
```

### Test 3: Migration
```python
# Create test session with old format
INSERT INTO sessions (id, user_id, dimensions) VALUES
('old-session', 'user-1', '{"HL": {"score": 4, "confidence": "HIGH"}}');

# Run migration
python backend/migrate_to_quantum.py

# Verify conversion
SELECT * FROM narrative_streams WHERE session_id = 'old-session';
# Should show BODY_KNOWLEDGE stream with converted scores
```

---

## Dependencies

- SQLite3 (already in use)
- Pydantic v2+ (update if needed: `pip install pydantic>=2.0`)

---

## Estimated Time

- Schema design: 30 min
- Migration script: 45 min
- Pydantic models: 30 min
- Testing: 30 min
- **Total: ~2 hours**

---

**Ready to Execute**: Yes  
**Blocking Issues**: None  
**Contact**: Return completed schema + migration script to main orchestrator
