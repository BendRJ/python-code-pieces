# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
from pathlib import Path

# check cwd
print(Path.cwd())

# mkdir
tmp_dir = Path("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True) if not tmp_dir.exists() else print("tmp dir already created")

#write to dir
Path("/tmp/output.txt").write_text("Hello World, this is a test.")

#read
content = Path("/tmp/output.txt").read_text()
print(content)