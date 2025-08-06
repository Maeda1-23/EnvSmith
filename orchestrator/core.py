# orchestrator/core.py

from worker_client import exec_in_worker

def main():
    # 1. WorkerでOS情報を取得
    print("---- [Worker内OS情報] ----")
    osinfo = exec_in_worker(["uname", "-a"])
    print(osinfo["stdout"])

    repo_url = input("GitHubリポジトリURLを入力してください: ").strip()
    clone = exec_in_worker(["git", "clone", repo_url])
    print("---- [git clone stdout] ----")
    print(clone["stdout"])
    print("---- [git clone stderr] ----")
    print(clone["stderr"])

    # 3. Workerでクローン先をls
    print("---- [ls /workspace] ----")
    lsout = exec_in_worker(["ls", "/workspace"])
    print(lsout["stdout"])

    # 4. 主要ファイル探索
    # 例: README.md, requirements.txt, Dockerfile など
    # ここでAIにtreeやls出力を投げてTODO生成→次のコマンドを決定（今はprintでOK）

if __name__ == "__main__":
    main()
