import os
import json
import server

def get_webpack_manifest():
    fp = os.path.join(os.path.dirname(server.__file__), '..', 'manifest.json')
    with open(fp) as fh:
        manifest = json.loads(fh.read())
        return {k: os.path.basename(v) for k, v in manifest.items()}


def get_raw_static_asset(name):
    basename, ext = name.split('.')
    manifest = get_webpack_manifest()
    static_asset = manifest[name]
    dirname = os.path.dirname(server.__file__)
    fp = os.path.join(dirname, '..', 'client', 'static', ext, static_asset)
    with open(fp) as fh:
        return fh.read().strip()
