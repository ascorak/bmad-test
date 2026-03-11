import csv
import os

input_file = '_bmad/_config/agent-manifest.csv'
output_dir = '_bmad/_memory/agents'

os.makedirs(output_dir, exist_ok=True)

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # The first column is unnamed in the CSV (empty string as key)
        agent_id = row.get('')
        if not agent_id:
            continue
            
        filename = f"{agent_id}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, mode='w', encoding='utf-8') as out:
            out.write(f"# Agent: {row['displayName']}\n\n")
            out.write(f"**Title:** {row['title']} {row['icon']}\n")
            out.write(f"**Role:** {row['role']}\n\n")
            out.write(f"## Identity\n{row['identity']}\n\n")
            out.write(f"## Communication Style\n{row['communicationStyle']}\n\n")
            out.write(f"## Principles\n{row['principles']}\n\n")
            out.write(f"**Module:** {row['module']}\n")
            out.write(f"**Path:** {row['path']}\n")

print(f"Sharded agents into {output_dir}")
