import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

LOG_PATH = "/Users/stefanbund/Desktop/Desktop - stefan’s Mac mini/METASTADIUM/metastadium-log-sync/server/data/m4-coinbase/trading_bot.log"

parsed_data = []
with open(LOG_PATH, "r") as f:
    for line in f:
        try:
            if "{" not in line: continue
            entry = json.loads(line)
            if "probability" in entry and "symbol" in entry:
                # For Crash tiers or others missing accuracy, use 'passed' as a proxy (1.0 or 0.0)
                accuracy = entry.get("accuracy")
                if accuracy is None:
                    accuracy = 1.0 if entry.get("passed", False) else 0.0
                
                parsed_data.append({
                    "symbol": entry.get("symbol"),
                    "tier": entry.get("tier", "General"),
                    "probability": entry.get("probability", 0),
                    "threshold": entry.get("threshold", 0),
                    "accuracy": accuracy,
                    "passed": entry.get("passed", False),
                    "timestamp": entry.get("timestamp", "")
                })
        except:
            continue

if not parsed_data:
    print("No matching data found in logs.")
    exit(1)

df = pd.DataFrame(parsed_data)

# Aggregate: Mean for metrics, Max for timestamp, Size for count
agg_metrics = df.groupby(['symbol', 'tier']).mean(numeric_only=True).reset_index()
agg_time = df.groupby(['symbol', 'tier'])['timestamp'].max().reset_index().rename(columns={'timestamp': 'last_seen'})
agg_count = df.groupby(['symbol', 'tier']).size().rename('count').reset_index()

# Merge all
agg_df = agg_metrics.merge(agg_time, on=['symbol', 'tier']).merge(agg_count, on=['symbol', 'tier'])

# Sort by last_seen descending
agg_df = agg_df.sort_values(by='last_seen', ascending=False)

# 1. Visualization: Accuracy & Pass Rate by Symbol
plt.figure(figsize=(14, 60))
ax = sns.barplot(data=agg_df, y='symbol', x='probability', hue='tier', alpha=0.8, orient='h')

# Movement of X-axis to top
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')

plt.title("Neural Network Mean Predicted Probability by Symbol & Tier", fontsize=18, pad=30)
plt.yticks(fontsize=9)
plt.xlabel("Mean Predicted Probability", fontsize=12, labelpad=15)
plt.axvline(0.75, color='red', linestyle='--', alpha=0.5, label='75% Threshold')

# Add gridlines for easier tracing across the tall chart
plt.grid(axis='x', linestyle=':', alpha=0.6)

# Increase spacing between symbol labels
ax.tick_params(axis='y', which='major', pad=10)

plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()
plt.savefig("nn_accuracy_by_symbol.png", dpi=300)
plt.close()

# 2. Visualization: Probability vs Accuracy Scatter
plt.figure(figsize=(12, 8))
# Create scatter plot to show relation between model confidence (probability) and historical accuracy
scatter = sns.scatterplot(
    data=agg_df, 
    x='probability', 
    y='accuracy', 
    hue='tier', 
    size='passed',
    sizes=(50, 200),
    alpha=0.7
)
plt.title("Model Confidence (Probability) vs Historical Accuracy by Symbol", fontsize=16)
plt.xlabel("Mean Predicted Probability")
plt.ylabel("Mean Historical Accuracy")

# Draw the threshold line representing the decision boundary
plt.axvline(x=agg_df['threshold'].mean(), color='red', linestyle='--', alpha=0.5, label='Mean Threshold')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
# --- Data Export for Interactive HTML (ApexCharts) ---
import json
export_data = agg_df.to_dict(orient='records')
with open("nn_performance_data.json", "w") as f:
    json.dump(export_data, f, indent=2)

print(f"Exported interactive data to 'nn_performance_data.json'")

print(f"Successfully processed {len(df)} entries into {len(agg_df)} aggregated symbol-tier metrics.")
print("Saved outputs to 'nn_accuracy_by_symbol.png' and 'nn_prob_vs_acc_by_symbol.png'")
