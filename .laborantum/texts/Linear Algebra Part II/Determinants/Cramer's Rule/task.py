import numpy as np
import os
import json_tricks

from pathlib import Path

home_dir = Path(__file__).parent.resolve()

answer = {
    "task1": {
        "det_A_terms": sorted([
            -1,-1
        ]),
        "det_A_1_terms": sorted([
            -2,0
        ]),
        "det_A_2_terms": sorted([
            -2,0
        ]),
        "x": np.array([1, 1], dtype=np.int64),
        "cofactors": np.array([
            [1, -1],
            [-1, 1]
        ], dtype=np.int64),
        "inverse": np.array([
            [0.5, -0.5],
            [-0.5, 0.5]
        ], dtype=np.float64)
    },
    "task2": {
        "det_A_terms": sorted([
            ### YOUR CODE HERE ###
        ]),
        "det_A_1_terms": sorted([
            ### YOUR CODE HERE ###
        ]),
        "det_A_2_terms": sorted([
            ### YOUR CODE HERE ###
        ]),
        "x": np.array([]
### YOUR CODE HERE ###
        ),
        "cofactors": np.array([]
### YOUR CODE HERE ###
        ),
        "inverse": np.array([]
### YOUR CODE HERE ###
        )
    },
    "task3": {
        "det_A_terms": sorted([
            ### YOUR CODE HERE ###
        ]),
        "det_A_1_terms": sorted([
            ### YOUR CODE HERE ###
        ]),
        "det_A_2_terms": sorted([
            ### YOUR CODE HERE ###
        ]),
        "x": np.array([]
### YOUR CODE HERE ###
        ),
        "cofactors": np.array([]
### YOUR CODE HERE ###
        ),
        "inverse": np.array([]
### YOUR CODE HERE ###
        )
    }
}

json_tricks.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))