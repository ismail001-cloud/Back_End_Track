import os

import subprocess

def create_survey_projects():
    base_dir = "survey"
    folders = [
        "src",
        "src/api",
        "src/api/controllers",
        "src/api/errors",
        "src/api/models",
        "src/api/resources",
        "src/db",
        "src/db/models",
        "src/test",
        "src/test/integration",
        "src/test/unit",
        "src/utils",
        "static",
        "templates",
        "migrations",
        "instance"

    ]

    for folder in folders:
        os.makedirs(os.path.join(base_dir,folder),exist_ok=True)

if __name__ == "__main__":
    create_survey_projects()