from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents"""
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(file_reader)


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them"""
    return list(set([job["job_type"] for job in read(path)]))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type"""
    return [job for job in jobs if job["job_type"] == job_type]
