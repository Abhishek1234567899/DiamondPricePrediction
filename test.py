'''import os
path="notebook/research.ipynb"

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(path,'w') as f:
    pass'''

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

