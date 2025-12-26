📱 Android Auto Repack & Signer Tool
Một công cụ tự động hóa quá trình Repacking, Resigning và Neutralizing mã độc cho ứng dụng Android. Đồ án tập trung vào nghiên cứu bảo mật và can thiệp mã nguồn tầng Bytecode.

✨ Tính năng nổi bật
[x] Decompile: Giải mã file APK sang mã nguồn Smali và tài nguyên (XML, Images).

[x] Auto-Mod: Tự động chỉnh sửa tên ứng dụng và thông tin Manifest.

[x] Malware Neutralizer: 🛡️ Tính năng nâng cao giúp vô hiệu hóa mã độc bằng cách tước bỏ quyền (Permissions) và vô hiệu hóa khởi động (Receivers).

[x] Automation Sign: Tự động thực hiện zipalign và apksigner chuẩn quy trình Google.

[x] Modern GUI: Giao diện Dark Mode xây dựng trên thư viện CustomTkinter.

[x] Multi-threading: Xử lý tác vụ nặng không gây treo giao diện.

📂 Cấu trúc dự án

APK_Resigner_Tool/  
├── main.py                # Điểm khởi chạy ứng dụng (Giao diện & Logic tổng)  
├── core/                  # Các module xử lý lõi  
│   ├── __init__.py        # Khởi tạo package  
│   ├── decompiler.py      # Xử lý Apktool d (Giải mã)  
│   ├── builder.py         # Xử lý Apktool b (Đóng gói)  
│   └── signer.py          # Xử lý Zipalign & Apksigner (Ký số)  
├── bin/                   # Chứa các file thực thi (Binary)  
│   ├── apktool.jar        # Bộ giải mã/đóng gói APK  
│   ├── zipalign.exe       # Công cụ tối ưu hóa byte  
│   └── apksigner.jar      # Công cụ ký số chuẩn Android  
├── cert/                  # Thư mục chứa chứng chỉ số (Keystore)  
│   └── debug.keystore     # File khóa dùng để ký ứng dụng  
├── workspace/             # Thư mục tạm thời (Tự động dọn dẹp sau khi xong)  
└── output/                # Nơi chứa thành phẩm APK sau khi xử lý  

🚀 Hướng dẫn cài đặt & Sử dụng
1. Yêu cầu hệ thống
Windows OS

Java JDK 8+ (Đã cấu hình biến môi trường PATH)

Python 3.8+

2. Cài đặt thư viện
Mở Terminal tại thư mục gốc và chạy lệnh:

Bash

py -m pip install customtkinter
3. Chuẩn bị bộ công cụ
Đảm bảo các file sau đã có trong thư mục bin/:

apktool.jar

zipalign.exe

apksigner.jar

4. Khởi chạy
Bash

python main.py
