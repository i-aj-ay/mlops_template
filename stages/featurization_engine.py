from pathlib import Path

import mlflow
import pandas as pd


def run_featurization_stage(
    *,
    input_path: Path,
    output_path: Path,
    impute_path: Path,
    encoder_path: Path,
    data_impute_fn,
    data_check_fn,
    data_preprocess_fn,
    run_name: str,
):
    with mlflow.start_run(run_name=run_name):

        df = pd.read_csv(input_path)

        df = data_impute_fn(df, impute_path)

        data_check_fn(df)

        df = data_preprocess_fn(df, encoder_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)

        mlflow.log_param("feature_output", str(output_path))
        mlflow.log_artifact(impute_path, artifact_path="imputation")
        mlflow.log_artifact(encoder_path, artifact_path="encodings")
        mlflow.log_artifact(output_path, artifact_path=run_name)

    return str(output_path)
