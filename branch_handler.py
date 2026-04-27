import requests

CLEANUP_URL = "http://localhost:5000/cleanup"

PROTECTED_BRANCHES = ["main", "prod"]


def handle_event(payload):
    branch = payload.get("ref", "").split("/")[-1]
    repo = payload.get("repository", {}).get("name")

    print(f"Received event for branch: {branch}")

    if branch not in PROTECTED_BRANCHES:
        print("Non-protected branch → triggering cleanup")

        requests.post(CLEANUP_URL, json={
            "repository": repo,
            "branch": branch,
            "action": "cleanup_triggered"
        })
    else:
        print("Protected branch → skipping cleanup")
