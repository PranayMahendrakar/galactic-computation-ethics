"""Substrate Rights Evaluator - Rights of computational substrates"""
from .base import LlamaClient
class SubstrateRightsEvaluator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in substrate independence and computational rights."
    def evaluate_rights(self, substrate: str, computation: str) -> str:
        return self.client.generate(f"Evaluate substrate rights:\nSubstrate: {substrate}\nComputation: {computation}\nAnalyze: 1. Substrate Properties 2. Consciousness Potential 3. Moral Status 4. Rights Framework 5. Protection Needs 6. Exploitation Concerns 7. Autonomy Rights 8. Governance", self.system_prompt)
