FROM python:3.11-slim

# 必要なコマンド類のインストール
RUN apt-get update && \
    apt-get install -y git tree curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# コードをコピー
COPY . /workspace

# Python依存をインストール
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "agent/main.py"]
