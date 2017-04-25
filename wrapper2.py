import subprocess

text = "hello world"

subprocess.Popen(["espeak", "-v", "en+m3", text])
