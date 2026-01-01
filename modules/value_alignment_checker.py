"""Value Alignment Checker - Check alignment across scales"""
from .base import LlamaClient
class ValueAlignmentChecker:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in value alignment across computational scales."
    def check_alignment(self, values: str, system: str) -> str:
        return self.client.generate(f"Check value alignment:\nValues: {values}\nSystem: {system}\nAnalyze: 1. Value Specification 2. System Behavior 3. Alignment Assessment 4. Misalignment Risks 5. Correction Mechanisms 6. Verification Methods 7. Robustness 8. Recommendations", self.system_prompt)
