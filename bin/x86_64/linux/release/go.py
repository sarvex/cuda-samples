import os
import subprocess
for filename in os.listdir('./'):
    if os.access(filename, os.X_OK) and os.path.isfile(filename):
        with open(f"APM_{filename}.txt", "w") as f:
            print(f"Running {filename}")
            p1 = subprocess.Popen([f"./{filename}"], stdout=f)
            print("Wait")
            p1.wait()
            print("Done")


