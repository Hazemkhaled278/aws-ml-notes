"""
AWS SageMaker End-to-End Pipeline & Deployment Script
Author: Hazem Mohamed
Description: Production-ready modular script structure for ML workflows on AWS SageMaker.
"""

import boto3
import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep

def initialize_sagemaker_environment():
    """Initialize AWS session, execution role, and default S3 bucket."""
    sagemaker_session = sagemaker.Session()
    role = sagemaker.get_execution_role()
    default_bucket = sagemaker_session.default_bucket()
    
    print(f"--- AWS SageMaker Environment Initialized ---")
    print(f"Default Bucket: {default_bucket}")
    
    return sagemaker_session, role, default_bucket

def configure_training_estimator(role: str, output_path: str):
    """Configure the ML framework estimator (e.g., Scikit-Learn or PyTorch)."""
    from sagemaker.sklearn.estimator import SKLearn
    
    sklearn_estimator = SKLearn(
        entry_point='train.py',
        role=role,
        instance_type='ml.m5.xlarge',
        instance_count=1,
        framework_version='1.0-1',
        output_path=output_path,
        sagemaker_session=sagemaker.Session()
    )
    return sklearn_estimator

def deploy_model_endpoint(predictor_model, instance_type: str = 'ml.m5.xlarge'):
    """Deploy the trained model to a real-time managed endpoint."""
    print("Deploying model to AWS managed infrastructure...")
    
    predictor = predictor_model.deploy(
        initial_instance_count=1,
        instance_type=instance_type
    )
    
    print(f"Model successfully deployed at endpoint: {predictor.endpoint_name}")
    return predictor

if __name__ == "__main__":
  
    print("Running AWS MLOps Pipeline Definition...")
   
