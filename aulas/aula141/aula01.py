import subprocess
import sys

system = 'Windows' if sys.platform == 'win32' else 'Linux / Mac'

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'

if system == 'Windows':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding
)

print(proc.stdout)
# print()
# print(proc.stdout.decode('cp850'))
# print(f'{proc.returncode=}')
# print(f'{proc.args=}')
# print(f'{proc.stderr=}')
# print(f'{proc.stdout=}')
