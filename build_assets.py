import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True)
    if res.returncode != 0:
        print(f"Error executing command: {cmd}")
        sys.exit(res.returncode)

print("Starting asset compilation and minification...")
run_cmd("npx -y clean-css-cli -o assets/css/style.min.css assets/css/style.css")
run_cmd("npx -y clean-css-cli -o assets/css/uno-tournament.min.css assets/css/uno-tournament.css")
run_cmd("npx -y terser assets/js/main.js -o assets/js/main.min.js --mangle --compress")
print("Build and minification completed successfully!")
