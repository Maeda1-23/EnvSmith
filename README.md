# EnvSmith

## 1. Dockerイメージのビルド

```sh
docker build -t envsmith .
```

---

## 2. Dockerコンテナの起動
▶️ Windows PowerShellの場合
```powershell
docker run -it --rm -v ${PWD}:/workspace envsmith
```
▶️ Windows コマンドプロンプト（cmd.exe）の場合
```cmd
docker run -it --rm -v %cd%:/workspace envsmith
```
▶️ WSL / Linux / Macの場合
```bash
docker run -it --rm -v $(pwd):/workspace envsmith
```

