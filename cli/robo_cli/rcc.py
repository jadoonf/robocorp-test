import json
import os
from pathlib import Path
import shutil

from robo_cli.config import generate_rcc
from robo_cli.config.context import temp_robot_folder
from robo_cli.process import Process

# Convert to absolute path when vendored to not require PATH to be correct
RCC_EXECUTABLE = "rcc"

TEMPLATE_PATH = Path(__file__).parent.parent / "templates"


def _execute(*args):
    cmd = [RCC_EXECUTABLE] + [str(arg).strip() for arg in args]

    proc = Process(args=cmd)
    # proc.on_stdout(lambda line: print(line))
    # proc.on_stderr(lambda line: print(line))

    stdout, _ = proc.run()
    return "\n".join(stdout)


def run():
    with generate_rcc() as (_, robot_config):
        _execute("run", "--robot", robot_config)


def deploy(workspace_id, robot_id):
    with temp_robot_folder() as dir:
        # TODO: Copy tempfiles into temporary "deploy" folder with all of the code?
        print(os.listdir(dir.name))
        _execute(
            "cloud", "push", "--directory", dir.name, "-w", workspace_id, "-r", robot_id
        )


def export() -> Path:
    with temp_robot_folder() as dir:
        _execute("robot", "wrap", "--directory", dir.name)
        if not os.path.exists("dist/"):
            os.mkdir("dist")
        zip_path = Path("dist") / "robot.zip"
        path = shutil.move("robot.zip", zip_path)
        return zip_path


def new_project(name: str, template: str):
    new_folder = Path(name)
    shutil.copytree(TEMPLATE_PATH / template, new_folder)


def get_workspaces() -> dict[str, dict[str, str]]:
    raw_output = _execute("cloud", "workspace", "--json")
    raw_workspaces: list[dict] = json.loads(raw_output)
    workspaces = {w["name"]: {"id": w["id"], "url": w["url"]} for w in raw_workspaces}
    return workspaces
