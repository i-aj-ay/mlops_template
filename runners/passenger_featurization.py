from pathlib import Path

from titanic_classification.passenger_featurization import (
    data_check_passenger,
    data_impute_passenger,
    data_preprocess_passenger,
)

from stages.featurization_engine import run_featurization_stage

if __name__ == "__main__":

    base = Path.cwd()

    run_featurization_stage(
        input_path=base / "data/raw/passenger_data_extraction.csv",
        output_path=base / "data/feature_data/passenger_featurization.csv",
        impute_path=base / "data/feature_data/imputation/passenger_impute.pkl",
        encoder_path=base / "data/feature_data/encodings/passenger_encode.pkl",
        data_impute_fn=data_impute_passenger,
        data_check_fn=data_check_passenger,
        data_preprocess_fn=data_preprocess_passenger,
        run_name="passenger_featurization",
    )
