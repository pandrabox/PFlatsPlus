import requests
import os
import re

# docusaurus.config.jsからOWNER, REPOを動的取得
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../docusaurus.config.js')
with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    config_js = f.read()

# organizationName, projectNameを抽出
owner_match = re.search(r"organizationName:\s*'([^']+)'", config_js)
repo_match = re.search(r"projectName:\s*'([^']+)'", config_js)
OWNER = owner_match.group(1) if owner_match else "pandrabox"
REPO = repo_match.group(1) if repo_match else "pandoc"
print(f"認識したOWNER: {OWNER}")
print(f"認識したREPO: {REPO}")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or "your_token_here"

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs?per_page=1"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
resp = requests.get(url, headers=headers)
resp.raise_for_status()
data = resp.json()

if "workflow_runs" in data and data["workflow_runs"]:
    run = data["workflow_runs"][0]
    print(f"Workflow: {run['name']}")
    print(f"Status: {run['status']}")
    print(f"Conclusion: {run['conclusion']}")
    print(f"Run started at: {run['run_started_at']}")
    print(f"HTML URL: {run['html_url']}")
else:
    print("No workflow runs found.")
