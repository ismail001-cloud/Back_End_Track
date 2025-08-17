import os
# to navigate into the computer os is used
import subprocess

def create_survey_project():

    base_dir = "survey"
    folders = [
        "src",
        "src/api",
        "src/api/controllers",
        "src/api/models",
        "src/api/errors",
        "src/api/resources"
        "src/db",
        "src/db/models",
        "src/utils",
        "src/test",
        "src/test/unit",
        "src/test/integration",
        "static",
        "template",
        "migrations"
    ]

    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

if __name__ == "__main__":
    create_survey_project()



