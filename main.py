
import time
import json
from pathlib import Path

def main():
    print("Soul RPG Agent")
    print("에이전트가 정상적으로 시작되었습니다.")

    settings = {
        "game": "Soul RPG",
        "mode": "screen_analysis",
        "auto_play": False,
        "status": "ready"
    }

    print(json.dumps(settings, ensure_ascii=False, indent=2))
    print("다음 단계: 게임 화면을 읽는 기능 추가")

if __name__ == "__main__":
    main()
