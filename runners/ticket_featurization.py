from pathlib import Path

from titanic_classification.ticket_featurization import (
    data_check_ticket,
    data_impute_ticket,
    data_preprocess_ticket,
)

from stages.featurization_engine import run_featurization_stage

if __name__ == "__main__":
    base = Path.cwd()

    run_featurization_stage(
        input_path=base / "data/raw/ticket_data_extraction.csv",
        output_path=base / "data/feature_data/ticket_featurization.csv",
        impute_path=base / "data/feature_data/imputation/ticket_impute.pkl",
        encoder_path=base / "data/feature_data/encodings/ticket_encode.pkl",
        data_impute_fn=data_impute_ticket,
        data_check_fn=data_check_ticket,
        data_preprocess_fn=data_preprocess_ticket,
        run_name="ticket_featurization",
    )
