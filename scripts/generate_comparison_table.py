
import matplotlib.pyplot as plt
import pandas as pd

# Data for technical head-to-head including Enterprise SOTA
data = {
    "Comparison Point": [
        "Search Space", 
        "Hardware Target", 
        "Data Sovereignty", 
        "Anti-Hallucination", 
        "Infrastructure Cost"
    ],
    "Enterprise (AWS/Azure)": [
        "Managed Clusters", 
        "Scalable Cloud", 
        "SaaS Dependent", 
        "Sémant Rankers (Fixed)", 
        "Ongoing Usage (\\$\\$\\$)"
    ],
    "Microsoft GraphRAG": [
        "Global Summaries", 
        "A100/H100 Nodes", 
        "Cloud-Intensity", 
        "Graph Connectivity", 
        "Token-Heavy (\\$\\$)"
    ],
    "WiredBrain (Ours)": [
        "Hierarchical (O(1) Gate)", 
        "GTX 1650 (Laptop)", 
        "100% Local / Air-Gapped", 
        "Stochastic GCC Verify", 
        "\\$0 (One-time Buy)"
    ]
}

df = pd.DataFrame(data)

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 7))
ax.axis('off')

# Table styling constants
header_color = "#2c3e50"
wiredbrain_color = "#eaf6ff"
accent_color = "#004085"
font_family = 'DejaVu Sans'

# Create table
table = ax.table(cellText=df.values, 
                 colLabels=df.columns, 
                 cellLoc='left', 
                 loc='center',
                 colColours=[header_color] * len(df.columns))

# Styling loop
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor('#bdc3c7')
    cell.set_linewidth(0.8)
    
    # Header Styling
    if row == 0:
        cell.set_text_props(weight='bold', color='white', family=font_family, fontsize=13)
        cell.set_facecolor(header_color)
        if col == 3: # WiredBrain column header
            cell.set_facecolor(wiredbrain_color)
            cell.set_text_props(weight='bold', color=accent_color)
    
    # Body Styling
    if row > 0:
        cell.set_text_props(family=font_family, fontsize=12)
        # WiredBrain Column Highlight
        if col == 3:
            cell.set_facecolor(wiredbrain_color)
            cell.set_text_props(weight='bold', color=accent_color)

table.auto_set_font_size(False)
table.scale(1.2, 3.0)

plt.title("WiredBrain vs. Enterprise Tier RAG (2024-2025)", fontsize=18, pad=35, weight='bold', color=header_color)
plt.savefig('/home/user/Desktop/WiredBrain/WiredBrain-RAG/docs/images/market_comparison_clean.png', bbox_inches='tight', dpi=300)
print("Enterprise-grade Market Advantage table generated.")
