# VAR Memorization Analysis

This repository is a fork of [FoundationVision/VAR](https://github.com/FoundationVision/VAR).

In this repository, we analyze the memorization of the `Vard16` model. All results are shown and produced in `memorization_analysis.ipynb`. 

## What is Memorization?
Memorization is a technique that analyzes how signals are processed in a neural network. For further information on memorization, check out [this paper](https://openreview.net/forum?id=R46HGlIjcG).

## Installation and Usage
To run the analysis, create a virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

The notebook is easily expandable by changing the depth of the model and the dataset. 

## Results
The resulting plots of the analysis are stored in the `output` folder.
