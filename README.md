# AI Setup Agent

## 1. ビルド
docker build -t ai-setup-agent .

## 2. 起動（カレントディレクトリをコンテナの/workspaceにマウント）
docker run -it --rm -v $(pwd):/workspace ai-setup-agent
