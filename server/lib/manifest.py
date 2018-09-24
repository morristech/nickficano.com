import os
import json

def get_webpack_manifest():
    fp = os.path.join(os.getcwd(), 'manifest.json')
    with open(fp) as fh:
        manifest = json.loads(fh.read())
        return {k: os.path.basename(v) for k, v in manifest.items()}
