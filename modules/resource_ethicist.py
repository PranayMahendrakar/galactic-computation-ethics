"""Resource Ethicist - Evaluate ethics of cosmic resource usage"""
from .base import LlamaClient
class ResourceEthicist:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "Expert in cosmic resource ethics and sustainability."
    def evaluate_usage(self, resource: str, purpose: str) -> str:
        return self.client.generate(f"Evaluate ethical resource usage:\nResource: {resource}\nPurpose: {purpose}\nAnalyze: 1. Resource Assessment 2. Scarcity Analysis 3. Alternative Uses 4. Future Generations 5. Opportunity Costs 6. Distribution Justice 7. Sustainability 8. Recommendations", self.system_prompt)
