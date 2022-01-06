from setuptools import setup, find_packages

setup(
    name         = "Plpred",
    version      = "0.0.1",
    author       = "Jean Rodrigues",
    packages     = find_packages(),
    author_email = 'eujean@live.com',
    description  = 'PLPred: Program that predicts protein location [subcelular|membrane protein] and',
    keywords     = 'bioinformatics',
    entry_points  = {
        'console_scripts': [
            'plpred-preprocess = plpred.preprocessing:main',
            'plpred-train = plpred.training:main',
            'plpred-predict = plpred.prediction:main'
            ]
    }
)