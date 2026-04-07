import os
from dart import mcp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp",
    )
import os

# Render는 환경 변수로 PORT를 지정해주므로 이를 받아와야 합니다.
port = int(os.environ.get("PORT", 8000))

# 서버 실행 시 포트 지정
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
