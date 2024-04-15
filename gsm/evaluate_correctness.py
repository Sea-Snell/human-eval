import fire
import sys
import json

from gsm.pal_code_exec import compute


def entry_point(
    sample_file: str,
    n_workers: int = 4,
    timeout: float = 3.0,
    majority_voting: bool = False,
    answer_symbol: str = None,
):
    with open(sample_file, 'r') as f:
        sample = json.load(f)
    predictions, references = sample['predictions'], sample['references']
    results = compute(
        predictions,
        references,
        n_workers,
        timeout,
        majority_voting,
        answer_symbol,
    )
    print(results)

def main():
    fire.Fire(entry_point)


sys.exit(main())
