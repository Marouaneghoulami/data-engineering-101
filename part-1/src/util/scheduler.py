import schedule
import time
from pipelines.raw.job_api_pipeline import JobApiPipeline
from pipelines.raw.car_api_pipeline import CarApiPipeline
from pipelines.curated.job_api_transform_pipeline import JobApiTransformPipeline

class Scheduler:
    def __init__(self):
        self.job_api_pipeline = JobApiPipeline()
        self.car_api_pipeline = CarApiPipeline()
        self.job_api_transform_pipeline = JobApiTransformPipeline()

    def schedule_jobs(self):
        schedule.every(10).seconds.do(self.car_api_pipeline.run_pipeline)
        schedule.every(10).seconds.do(self.job_api_pipeline.run_pipeline)
        schedule.every(1).minute.do(self.job_api_transform_pipeline.run_pipeline)

        while True:
            schedule.run_pending()
            time.sleep(1)
