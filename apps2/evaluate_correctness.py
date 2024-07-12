from typing import Optional
import fire
import sys
import json
from test import eval_and_save_problems, print_results
import argparse

def entry_point(
    sample_file: str,
    split: Optional[str] = "introductory",
):
    args = argparse.Namespace()
    args.start = 0
    args.end = None
    args.index = 0
    args.debug = True
    args.save = sample_file
    args.split = split
    args.stop_early = None
    results = eval_and_save_problems(args)
    print_results(results, args)

def main():
    fire.Fire(entry_point)

sys.exit(main())
