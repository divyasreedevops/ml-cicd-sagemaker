# ML CI/CD with AWS CodePipeline and SageMaker

This repo demonstrates how to build a CI/CD pipeline to train and deploy ML models using AWS CodePipeline and SageMaker.

## Files

- `train.py` – Trains and packages a model
- `buildspec.yml` – CodeBuild instructions
- `requirements.txt` – Dependencies
- `test/test_train.py` – Basic unit test

## CI/CD Flow

1. Push code to GitHub
2. CodePipeline triggers CodeBuild
3. CodeBuild runs `train.py`, packages model
4. Model artifacts saved to S3
5. (Optional) Deploy model using SageMaker
