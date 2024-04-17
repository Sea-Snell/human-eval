from typing import Optional
import fire
import sys
import json
from evaluate import load

def entry_point(
    sample_file: str,
    k: str = "1,10,100",
    split: Optional[str] = "introductory",
):
    with open(sample_file, 'r') as f:
        sample = json.load(f)
    predictions = sample['completions']
    k = list(map(int, k.split(",")))
    code_metric = load("codeparrot/apps_metric")
    results = code_metric.compute(
        predictions=predictions, k_list=k, level=split,
    )
    print(results)

def main():
    fire.Fire(entry_point)

sys.exit(main())
