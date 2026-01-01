#!/usr/bin/env python3
"""Galactic-Scale Computation Ethics Framework - Author: Pranay M"""
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown
from modules import *

console = Console()

def main():
    console.print(Panel("🌌 GALACTIC-SCALE COMPUTATION ETHICS FRAMEWORK 🌌\nExploring Ethics at Cosmic Scales", style="bold blue"))
    tools = [("1","Scale Analyzer",ScaleAnalyzer()),("2","Resource Ethicist",ResourceEthicist()),
             ("3","Existential Risk",ExistentialRiskAssessor()),("4","Civilization Impact",CivilizationImpactModeler()),
             ("5","Temporal Ethics",TemporalEthicsEngine()),("6","Entropy Ethics",EntropyEthicsAnalyzer()),
             ("7","Substrate Rights",SubstrateRightsEvaluator()),("8","Cosmic Governance",CosmicGovernanceDesigner()),
             ("9","Value Alignment",ValueAlignmentChecker()),("10","Framework Synthesis",FrameworkSynthesizer())]
    while True:
        table = Table(title="Ethics Modules")
        table.add_column("Opt"); table.add_column("Module"); table.add_column("Description")
        for o,n,_ in tools: table.add_row(o,n,"Analyze "+n.lower())
        table.add_row("0","Exit","Exit")
        console.print(table)
        c = Prompt.ask("Select", choices=[str(i) for i in range(11)])
        if c == "0": break
        try:
            idx = int(c)-1
            query = Prompt.ask(f"Input for {tools[idx][1]}")
            result = tools[idx][2].analyze_scale(query) if hasattr(tools[idx][2],'analyze_scale') else \
                     tools[idx][2].evaluate_usage(query,"general") if hasattr(tools[idx][2],'evaluate_usage') else \
                     tools[idx][2].assess_risk(query) if hasattr(tools[idx][2],'assess_risk') else \
                     tools[idx][2].model_impact(query) if hasattr(tools[idx][2],'model_impact') else \
                     tools[idx][2].analyze_temporal(query,"cosmic") if hasattr(tools[idx][2],'analyze_temporal') else \
                     tools[idx][2].analyze_entropy(query) if hasattr(tools[idx][2],'analyze_entropy') else \
                     tools[idx][2].evaluate_rights(query,"digital") if hasattr(tools[idx][2],'evaluate_rights') else \
                     tools[idx][2].design_governance(query) if hasattr(tools[idx][2],'design_governance') else \
                     tools[idx][2].check_alignment(query,"system") if hasattr(tools[idx][2],'check_alignment') else \
                     tools[idx][2].synthesize(query)
            console.print(Panel(Markdown(result), title=tools[idx][1], border_style="blue"))
        except Exception as e: console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__": main()
