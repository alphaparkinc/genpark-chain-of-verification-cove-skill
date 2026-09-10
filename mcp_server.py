import sys
import json
from client import ChainOfVerification

cove = ChainOfVerification()

def handle_call(name, arguments):
    if name == "plan_verification":
        claims = arguments["claims"]
        return {"plan": cove.generate_verification_plan(claims)}
    elif name == "revise":
        draft = arguments.get("draft", "")
        results = arguments["verification_results"]
        return cove.execute_and_revise(draft, results)
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
