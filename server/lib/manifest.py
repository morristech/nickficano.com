import os
import json
import server

def get_webpack_manifest():
    fp = os.path.join(os.path.dirname(server.__file__), '..', 'manifest.json')
    with open(fp) as fh:
        manifest = json.loads(fh.read())
        return {k: os.path.basename(v) for k, v in manifest.items()}
