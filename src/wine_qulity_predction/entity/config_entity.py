from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: str
    STATUS_FILE: Path
    all_schema: dict
    

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path:Path


@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: str
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    target_column: str
    mlflow_uri: str