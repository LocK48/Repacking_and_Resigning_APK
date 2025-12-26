import subprocess
import os

def zipalign_apk(zipalign_exe, input_apk, output_apk):
    """Tối ưu hóa file APK bằng zipalign"""
    cmd = f"\"{zipalign_exe}\" -f -v 4 \"{input_apk}\" \"{output_apk}\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Lỗi Zipalign: {result.stderr}")
    return True

def sign_apk(apksigner_jar, keystore, password, input_apk, output_apk, alias="my_alias"):
    """Ký file APK bằng apksigner"""
    cmd = (f"java -jar {apksigner_jar} sign --ks {keystore} "
           f"--ks-pass pass:{password} --ks-key-alias {alias} "
           f"--out \"{output_apk}\" \"{input_apk}\"")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Lỗi Sign: {result.stderr}")
    return True