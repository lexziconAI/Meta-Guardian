"""
Sidecar LLM Inference with Cryptographic Signing
Provides tamper-proof source attribution for dual-LLM architecture
"""

import hmac
import hashlib
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional
from uuid import uuid4
import secrets

class SidecarMessageSigner:
    """
    Cryptographically signs sidecar-generated inference messages to prevent 
    tampering and enable source verification.
    """
    
    def __init__(self):
        self.secret_key = os.getenv('SIDECAR_SECRET_KEY')
        if not self.secret_key:
            # GRACEFUL DEGRADATION: Generate ephemeral key if not configured
            self.secret_key = secrets.token_hex(32)
            print("⚠️ SIDECAR_SECRET_KEY not set - using ephemeral key (not production safe)")
    
    def create_signed_update(
        self,
        scores: Dict[str, Any],
        source: str,  # 'sidecar_groq' or 'sidecar_kimi'
        model: str,
        confidence: float = 0.85,
        reasoning: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a cryptographically signed sidecar update message.
        
        Returns message compatible with OpenAI Realtime API format but with
        additional metadata for source attribution.
        """
        
        call_id = f"sidecar_{uuid4().hex[:12]}"
        timestamp = datetime.utcnow().isoformat()
        
        # Build inference metadata
        inference_metadata = {
            'source': source,
            'model': model,
            'timestamp': timestamp,
            'confidence': confidence,
            'call_id': call_id
        }
        
        if reasoning:
            inference_metadata['reasoning_trace'] = reasoning
        
        # Enhance scores with metadata
        # CRITICAL: Spread scores object to preserve newEvidence, phase, etc.
        enhanced_arguments = {
            **scores,  # Spread dimensions, newEvidence, phase, etc.
            '_inference_metadata': inference_metadata  # Hidden from OpenAI, visible to frontend
        }
        
        # Build message in OpenAI format
        message = {
            'type': 'response.function_call_arguments.done',
            'call_id': call_id,
            'name': 'updateAssessmentState',
            'arguments': json.dumps(enhanced_arguments)
        }
        
        # Sign the message
        signature = self._generate_signature(message)
        message['_sidecar_signature'] = signature  # Hidden field for verification
        
        return message
    
    def _generate_signature(self, message: Dict[str, Any]) -> str:
        """Generate HMAC-SHA256 signature of message"""
        # Canonical representation (exclude signature field itself)
        args = json.loads(message['arguments'])
        canonical = json.dumps({
            'call_id': message['call_id'],
            'arguments': message['arguments'],
            'timestamp': args['_inference_metadata']['timestamp']
        }, sort_keys=True)
        
        signature = hmac.new(
            self.secret_key.encode(),
            canonical.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return signature
    
    def verify_signature(self, message: Dict[str, Any]) -> bool:
        """Verify message signature - prevents tampering"""
        if '_sidecar_signature' not in message:
            return False
        
        claimed_signature = message['_sidecar_signature']
        
        # Remove signature and recalculate
        message_copy = {k: v for k, v in message.items() if k != '_sidecar_signature'}
        expected_signature = self._generate_signature(message_copy)
        
        # Constant-time comparison
        return hmac.compare_digest(claimed_signature, expected_signature)


# GLOBAL INSTANCE
signer = SidecarMessageSigner()
