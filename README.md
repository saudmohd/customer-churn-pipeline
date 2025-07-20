# Customer Churn Prediction Pipeline 🚀

This project builds a robust and scalable data engineering pipeline to predict customer churn using batch or streaming data sources. It includes ingestion, transformation, feature engineering, model training, prediction, and dashboard visualization.

## 📊 Overview

The pipeline:
- Ingests customer activity data (batch or streaming)
- Transforms and cleans the data using PySpark
- Engineers churn-relevant features
- Trains an XGBoost model to predict churn
- Outputs predictions to a database or dashboard
- Visualizes results via a Streamlit dashboard

## ⚙️ Tech Stack

- **Apache Kafka** / CSV for ingestion
- **Apache Spark / Pandas** for transformation
- **Airflow** for orchestration
- **PostgreSQL / S3** for storage
- **XGBoost / Scikit-learn** for modeling
- **Streamlit** for dashboard
- **Feast** (optional) for feature store

customer-churn-pipeline/
├── data/
│   ├── raw/                        # Original unprocessed data (CSV)
│   └── processed/                  # Cleaned and transformed data
│
├── ingestion/
│   ├── kafka_producer.py          # Streaming data producer
│   └── batch_ingest.py            # Batch ingestion script
│
├── processing/
│   └── churn_transform.py         # Data cleaning & transformation logic (Spark/Pandas)
│
├── features/
│   └── build_features.py          # Feature engineering logic
│
├── model/
│   ├── train_model.py             # Model training (XGBoost)
│   ├── evaluate_model.py          # Evaluation metrics
│   └── model.pkl                  # Serialized trained model
│
├── prediction/
│   └── batch_predict.py           # Make churn predictions on new data
│
├── dashboard/
│   └── app.py                     # Streamlit dashboard for results
│
├── dags/
│   └── churn_pipeline_dag.py      # Airflow DAG for orchestrating the pipeline
│
├── config/
│   └── config.yaml                # Configuration values for paths, thresholds, etc.
│
├── utils/
│   └── helpers.py                 # Common utility functions
│
├── notebooks/
│   └── EDA.ipynb                  # Jupyter Notebook for exploration & insights
│
├── .gitignore                     # Ignore system and virtual files
├── requirements.txt               # Project dependencies
├── README.md                      # Project overview and usage
└── LICENSE                        # Project license


## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/customer-churn-pipeline.git
cd customer-churn-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

