import subprocess

def build_apk(source_dir, output_apk, apktool_jar):
    """Sử dụng apktool để đóng gói lại thư mục thành APK"""
    cmd = f"java -jar {apktool_jar} b \"{source_dir}\" -o \"{output_apk}\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Lỗi Build: {result.stderr}")
    return True