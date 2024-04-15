import fire
import sys
import json

from mbpp.code_eval import compute_code_eval


def entry_point(
    sample_file: str,
    k: str = "1,10,100",
    n_workers: int = 4,
    timeout: float = 3.0,
):
    with open(sample_file, 'r') as f:
        sample = json.load(f)
    predictions, references = sample['completions'], sample['references']
    k = list(map(int, k.split(",")))
    results, _ = compute_code_eval(
        predictions,
        references,
        k,
        n_workers,
        timeout,
    )
    print(results)

def main():
    fire.Fire(entry_point)


sys.exit(main())
