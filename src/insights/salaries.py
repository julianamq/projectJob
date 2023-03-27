from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    return max(
        float(job["max_salary"])
        for job in read(path)
        if job["max_salary"].isdigit()
    )


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    return min(
        float(job["min_salary"])
        for job in read(path)
        if job["min_salary"].isdigit()
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job"""
    try:
        min_salary, max_salary = (
            float(job["min_salary"]),
            float(job["max_salary"]),
        )
        if min_salary > max_salary:
            raise ValueError("min_salary cannot be greater than max_salary")
        return min_salary <= float(salary) <= max_salary

    except (TypeError, ValueError, KeyError) as error:
        raise ValueError(error.args[0])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    # return [job for job in jobs if matches_salary_range(job, salary)]
    # #isso gera erro.
    get_filter_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                get_filter_by_salary.append(job)
        except ValueError:
            pass
    return get_filter_by_salary
