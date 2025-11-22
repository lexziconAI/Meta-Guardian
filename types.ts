export interface VisualizerProps {
  analyser: AnalyserNode | null;
  isActive: boolean;
  color?: string;
}

export enum ConnectionState {
  DISCONNECTED = 'DISCONNECTED',
  CONNECTING = 'CONNECTING',
  CONNECTED = 'CONNECTED',
  ERROR = 'ERROR',
  COMPLETE = 'COMPLETE',
}

export interface DimensionState {
  score: number;           // Current estimate (0-5)
  confidence: 'LOW' | 'MEDIUM' | 'HIGH';
  evidenceCount: number;
  trend: 'up' | 'down' | 'stable';
  contextNotes?: string;
}

export interface EvidenceItem {
  timestamp: string;
  dimension: string;
  type: 'positive' | 'negative' | 'contextual';
  summary: string;
  scoreImpact?: number;
}

export interface ContradictionAlert {
  dimension: string;
  earlyStatement: string;
  lateStatement: string;
  resolution: string;
}

export interface ScorePoint {
  time: number; // seconds from start
  HL: number;
  CM: number;
  DI: number;
  DL: number;
  PR: number;
}

export interface SessionState {
  dimensions: {
    HL: DimensionState; // Health Literacy
    CM: DimensionState; // Clinical Markers
    DI: DimensionState; // Data Integration
    DL: DimensionState; // Digital Literacy
    PR: DimensionState; // Preventive Readiness
  };
  scoreHistory: ScorePoint[];
  evidenceLog: EvidenceItem[];
  contradictions: ContradictionAlert[];
  conversationPhase: 'OPENING' | 'CORE' | 'GAP_FILLING' | 'VALIDATION' | 'CLOSING';
  strengths: string[];
  developmentPriorities: string[];
  summary?: string;
  fullReport?: string;
}

export const INITIAL_SESSION_STATE: SessionState = {
  dimensions: {
    HL: { score: 3.0, confidence: 'LOW', evidenceCount: 0, trend: 'stable' },
    CM: { score: 3.0, confidence: 'LOW', evidenceCount: 0, trend: 'stable' },
    DI: { score: 3.0, confidence: 'LOW', evidenceCount: 0, trend: 'stable' },
    DL: { score: 3.0, confidence: 'LOW', evidenceCount: 0, trend: 'stable' },
    PR: { score: 3.0, confidence: 'LOW', evidenceCount: 0, trend: 'stable' },
  },
  scoreHistory: [{ time: 0, HL: 3, CM: 3, DI: 3, DL: 3, PR: 3 }],
  evidenceLog: [],
  contradictions: [],
  conversationPhase: 'OPENING',
  strengths: [],
  developmentPriorities: [],
};

export const DIMENSION_LABELS: Record<string, string> = {
  HL: "Health Literacy",
  CM: "Clinical Markers",
  DI: "Data Integration",
  DL: "Digital Literacy",
  PR: "Preventive Readiness"
};