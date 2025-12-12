import os
import requests
import json
from loguru import logger


class CollectMetrics:
    def __init__(
        self,
        project_name,
        model_name,
        stage_name,
        task_name,
        task_run_id,
        job_name,
        job_id,
        job_run_id,
        run_status,
        start_time,
        end_time,
        duration,
        error_details,
        file_path,
    ):
        self.project_name = project_name
        self.model_name = model_name
        self.stage_name = stage_name
        self.task_name = task_name
        self.task_run_id = task_run_id
        self.job_name = job_name
        self.job_id = job_id
        self.job_run_id = job_run_id
        self.run_status = run_status
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.error_details = error_details
        self.file_path = file_path

    def log_metrics(self, write_to_file=True):
        metrics = {
            "project_name": self.project_name,
            "model_name": self.model_name,
            "stage_name": self.stage_name,
            "task_name": self.task_name,
            "task_run_id": self.task_run_id,
            "job_name": self.job_name,
            "job_id": self.job_id,
            "job_run_id": self.job_run_id,
            "run_status": self.run_status,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration_mins": self.duration,
            "error_details": self.error_details,
        }
        if write_to_file:
            # TODO:
            # 1. Add more output stages - files to process
            if self.task_name in ["extract_data", "preprocess_data"]:
                with open(file=self.file_path, mode="w") as fp:
                    json.dump(obj=metrics, fp=fp, indent=2)
                logger.info(f"{self.task_name}, task metrics written successfully.")
        else:
            logger.info("Skipped collecting task metrics.")
