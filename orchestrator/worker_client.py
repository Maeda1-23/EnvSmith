import subprocess

WORKER_CONTAINER_NAME = "envsmith_worker"

def exec_in_worker(cmd_list):
    """
    Workerコンテナでコマンドを実行し、stdout・stderr・returncodeを返す
    """
    cmd = ["docker", "exec", WORKER_CONTAINER_NAME] + cmd_list
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": " ".join(cmd_list),
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

# テスト用
if __name__ == "__main__":
    out = exec_in_worker(["python3", "--version"])
    print(out)
