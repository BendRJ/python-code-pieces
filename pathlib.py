# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
from pathlib import Path
import time

# check cwd
print(Path.cwd())

# mkdir
tmp_dir = Path("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True) if not tmp_dir.exists() else print("tmp dir already created")

#write to dir
Path("tmp/output.txt").write_text("Hello World, this is a test.")
# /tmp is abolsute path, tmp relative to cwd

#read
content = Path("/tmp/output.txt").read_text()
print(content)

# find
text_files = list(tmp_dir.glob("*.txt"))
print(text_files)

#rename
time.sleep(3)
text_files[0].rename("tmp/new.txt")

#delete
time.sleep(3)
for file in Path("tmp").glob("*.txt"):
    file.unlink()

# rmdir
time.sleep(3)
tmp_dir.rmdir()