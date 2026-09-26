import time
import fcntl
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location(
    'self_run',
    '/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/skills/self_run.py'
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

LOG = Path('/home/destiny/Obsidian/Destiny/Self_Check_Log.md')
LOCK_FILE = Path('/tmp/destiny_model_busy.lock')

while True:
    try:
        result = mod.run()
        LOG.open('a', encoding='utf-8').write(
            time.strftime('%Y-%m-%d %H:%M') + ' ' +
            str(result).replace('\n', ' | ') + '\n'
        )
    except Exception as e:
        LOG.open('a', encoding='utf-8').write(
            time.strftime('%Y-%m-%d %H:%M') +
            ' error ' + str(e) + '\n'
        )

    time.sleep(120)
