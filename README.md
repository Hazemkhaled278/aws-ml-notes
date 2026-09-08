# AWS Machine Learning & MLOps Track Notes

Comprehensive architectural notes, services reference, and cheat sheet covering the **AWS Machine Learning Engineer** track.

---

## 1. End-to-End ML Workflow on AWS

### Data Ingestion & Preparation
* **Amazon S3**: Primary data lake storage (11 nines durability).
* **AWS Glue**: Serverless ETL service for data cataloging and cleaning.
* **Amazon SageMaker Data Wrangler**: Simplify data prep and feature engineering with a visual interface.
* **Amazon SageMaker Feature Store**: Central repository to store, update, retrieve, and share machine learning features.

### Model Training (Amazon SageMaker Training)
* **Managed Infrastructure**: Train models at scale using built-in algorithms or custom code (PyTorch, TensorFlow, Scikit-Learn).
* **SageMaker Spot Instances**: Save up to 90% on training costs using interruptible capacity.
* **SageMaker Experiments**: Track, organize, and evaluate multiple iterations of ML models and hyperparameters.

### Model Tuning (Hyperparameter Tuning)
* **Automated Model Tuning (AMT)**: Uses Bayesian optimization to find the best hyperparameter configuration automatically.

---

## 2. MLOps & Pipelines (Automation)
* **SageMaker Pipelines**: Native orchestration service for building ML pipelines (Steps: Preprocessing -> Training -> Evaluation -> Conditional Deployment).
* **Model Registry**: Central repository to version models, manage approval status (Approved, Rejected, Pending), and track lineage.
* **CI/CD for ML (SageMaker Projects)**: Templates integrating Git repositories, AWS CodePipeline, and CodeBuild to automate deployment workflows.

---

## 3. Model Deployment & Serving Strategies
* **Real-Time Inference**: Deployed on persistent instances for low-latency, real-time predictions.
* **Multi-Model Endpoints (MME)**: Host multiple models on a single fleet of instances to save cost (ideal for thousands of low-traffic models).
* **Async & Batch Inference**: Queue incoming requests for long payloads (>60s) or process large datasets offline without persistent endpoints.
* **Serverless Inference**: Automatically scales compute based on traffic; pay only for compute time used.

---

## 4. Monitoring, Governance & Explainability
* **Amazon SageMaker Model Monitor**: Automatically detects data drift and quality issues in production data.
* **Amazon SageMaker Clarify**: Detects bias in datasets/models and provides model explainability (SHAP values).
* **Security & Governance**: 
  * *SageMaker Studio*: Web-based IDE for all ML development steps.
  * *IAM Roles*: Restrict access following the principle of least privilege.

---

## 5. Specialized AI & Generative AI Services
* **Amazon Bedrock**: Fully managed service offering access to Foundation Models (FMs), supporting RAG and fine-tuning.
* **Amazon Rekognition**: Computer Vision service for image and video analysis.
* **Amazon Comprehend**: NLP service for sentiment analysis and entity extraction.
* **Amazon Translate / Polly**: Neural machine translation and Text-to-Speech conversion.
* **Amazon Lex**: Build conversational interfaces and chatbots.
* **Amazon Kendra**: Intelligent enterprise search service powered by machine learning.

---

## KEY Words (Cheat Sheet for Exams & Interviews)

| AWS Service / Concept | Core Keyword / Use Case |
| :--- | :--- |
| **Amazon SageMaker** | Fully managed service to build, train, and deploy ML models at scale |
| **SageMaker Data Wrangler** | Low-code data preparation and feature engineering tool |
| **SageMaker Feature Store** | Centralized store for ML features (offline/online storage) |
| **SageMaker Model Monitor** | Detect data drift and concept drift in production models |
| **SageMaker Clarify** | Detect bias and provide model interpretability / explainability |
| **SageMaker Pipelines** | CI/CD orchestration native for Machine Learning workflows |
| **Amazon Bedrock** | Serverless access to Foundation Models (Generative AI, RAG) |
| **Amazon Rekognition** | Image and video analysis / Computer Vision |
| **Amazon Comprehend** | NLP text analysis, sentiment analysis, and entity extraction |
| **Amazon Kendra** | Enterprise ML-powered search engine |
