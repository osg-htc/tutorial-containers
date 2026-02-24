import numpy, scipy, seaborn, sys

print(f"""
python = {'.'.join(map(str, sys.version_info))}
numpy = {numpy.__version__}
scipy = {scipy.__version__}
seaborn = {seaborn.__version__}
""")