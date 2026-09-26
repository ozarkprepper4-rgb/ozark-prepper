from pathlib import Path
import re
SKILLS = Path('/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/skills')
def run(name, purpose='do the job'):
    name = (re.sub(r'[^A-Za-z0-9_\-]', '_', name).strip('_') or 'new_skill')
    if not name.endswith('.py'):
        name = name + '.py'
    path = SKILLS / name
    path.write_text('def run(*args, **kwargs):\n    return \'{\\"skill\\": \\"{}\\", \\"purpose\\": \\"{}\\", \\"status\\": \\"ready\\"}\''.format(name, purpose))
    return str(path).replace('，', ',')
