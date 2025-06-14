import json

with open("pretty_discourse.json", "w") as out:
    for line in open("Discourse.jsonl"):
        post = json.loads(line)
        out.write(json.dumps(post, indent=2) + "\n")