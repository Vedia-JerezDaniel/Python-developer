from pathlib import Path

Path.cwd()

Path.home()

file = Path(r"C:\Users\philipp\realpython\file.txt")

print(f"You can find me here: {Path(file).parent}!")

Path(file)

for file_path in Path.cwd().glob("*.ipynb"):
    new_path = Path() / file_path.name
    file_path.rename(new_path)


path = Path.cwd().joinpath(r"realpython/test.md")

path

path.name
path.stem
path.suffix
path.anchor
path.parent
path.parent.parent

cont = Path("prow/README.md").read_text(encoding="utf-8")
cont

lt = list(cont.splitlines())
llt = [item for item in lt if len(item) > 1]
llt = [item + item for item in llt ]

cont = [''.join(llt[:7])]
cont 


from collections import Counter
from pathlib import Path

Counter(path.suffix for path in Path.cwd().iterdir())

def tree(directory):
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = "    " * depth
        print(f"{spacer}+ {path.name}")
tree(Path.cwd())tree(Path.cwd())