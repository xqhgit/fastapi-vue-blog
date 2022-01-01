import uvicorn
import sys
from pathlib import Path
import colorama

sys.path.append(str(Path(__file__).absolute().parent.parent))  # fix no module name

from webapi import create_application

colorama.init(autoreset=True)
app = create_application()

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
