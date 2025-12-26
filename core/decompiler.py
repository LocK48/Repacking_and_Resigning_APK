import subprocess
import os

def decompile_apk(apk_path, output_dir, apktool_jar):
    """Sử dụng apktool để giải mã APK"""
    cmd = f"java -jar {apktool_jar} d \"{apk_path}\" -o \"{output_dir}\" -f"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Lỗi Decompile: {result.stderr}")
    return True