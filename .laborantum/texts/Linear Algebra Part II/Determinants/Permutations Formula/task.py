import json
import os
from pathlib import Path

home_dir = Path(__file__).parent.resolve()

answer = {
        "2x2": {
            "+": sorted(["1 2"]), 
            "-": sorted(["2 1"])
            },
        "3x3": {
            "+": sorted([
"1 2 3","3 2 1","3 1 2"
            ]),
            "-": sorted([
"1 3 2", "2 1 3", "2 3 1"
            ])
        },
        "4x4": {
            "+": sorted([
### YOUR CODE HERE ###
            ]),
            "-": sorted([
### YOUR CODE HERE ###
            ])
        }
    }

json.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))