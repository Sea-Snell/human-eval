import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="human-eval",
    py_modules=["human-eval", "gsm", "mbpp"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = human_eval.evaluate_functional_correctness",
            "gsm_functional_correctness = gsm.evaluate_correctness",
            "mbpp_functional_correctness = mbpp.evaluate_correctness",
            "apps_functional_correctness = apps2.evaluate_correctness",
        ]
    }
)
