from dataclasses import asdict
import json


def snapshot_to_json(snapshot):

    return json.dumps(
        asdict(snapshot),
        indent=4
    )


def snapshot_to_dict(snapshot):

    return asdict(snapshot)