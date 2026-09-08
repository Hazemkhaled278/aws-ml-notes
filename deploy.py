"""
AWS SageMaker End-to-End Pipeline & Deployment Script
Author: Hazem Mohamed
Description: Production-ready modular script structure for ML workflows on AWS SageMaker.
"""
import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep

def setup_sagemaker_env():
    session = sagemaker.Session()
    role = sagemaker.get_execution_role()
    bucket = session.default_bucket()
    
    print(f"AWS SageMaker Session Initialized. Bucket: {bucket}")
    return session, role, bucket

def build_pipeline_steps(role, bucket):
    output_location = f"s3://{bucket}/sklearn/output"
    
    estimator = SKLearn(
        entry_point='train.py',
        role=role,
        instance_type='ml.m5.xlarge',
        instance_count=1,
        framework_version='1.0-1',
        output_path=output_location,
        sagemaker_session=sagemaker.Session()
    )
    
    training_step = TrainingStep(
        name="TrainingModelStep",
        estimator=estimator
    )
    
    return estimator, training_step

def deploy_endpoint(estimator):
    print("Initiating deployment to managed endpoint...")
    predictor = estimator.deploy(
        initial_instance_count=1,
        instance_type='ml.m5.xlarge'
    )
    print(f"Endpoint active at: {predictor.endpoint_name}")
    return predictor

if __name__ == "__main__":
    session, role, bucket = setup_sagemaker_env()
    estimator, step = build_pipeline_steps(role, bucket)
    
    print("Pipeline and Estimator successfully configured.")
