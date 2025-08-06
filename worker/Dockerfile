FROM python:3.11-slim

RUN apt-get update && apt-get install -y git curl build-essential python3-pip

WORKDIR /workspace

# 必要なら追加パッケージ
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# entrypointで「sleep無限」や「tail -f /dev/null」で常駐
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
