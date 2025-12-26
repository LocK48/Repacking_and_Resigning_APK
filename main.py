import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import os
import shutil
from core.decompiler import decompile_apk
from core.builder import build_apk
from core.signer import zipalign_apk, sign_apk

ctk.set_appearance_mode("Dark")

class ResignerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Android Repack & Signer Tool")
        self.geometry("700x550")
        
        # Đường dẫn công cụ (bin/)
        self.tools = {
            'apktool': os.path.abspath("bin/apktool.jar"),
            'zipalign': os.path.abspath("bin/zipalign.exe"),
            'apksigner': os.path.abspath("bin/apksigner.jar"),
            'keystore': os.path.abspath("cert/debug.keystore"),
            'ks_pass': "123456"
        }

        # --- UI Elements ---
        self.label = ctk.CTkLabel(self, text="HỆ THỐNG REPACK & RESIGN APK", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=10, fill="x")

        self.entry_apk = ctk.CTkEntry(self.frame, placeholder_text="Chọn file APK...", width=450)
        self.entry_apk.grid(row=0, column=0, padx=10, pady=20)

        self.btn_browse = ctk.CTkButton(self.frame, text="Browse", command=self.browse_file)
        self.btn_browse.grid(row=0, column=1, padx=10)

        self.btn_run = ctk.CTkButton(self, text="BẮT ĐẦU XỬ LÝ", command=self.start_process, fg_color="green", height=40)
        self.btn_run.pack(pady=20)

        self.log_box = ctk.CTkTextbox(self, width=650, height=200)
        self.log_box.pack(padx=20, pady=10)

    def log(self, message):
        self.log_box.insert("end", f"> {message}\n")
        self.log_box.see("end")

    def browse_file(self):
        path = filedialog.askopenfilename(filetypes=[("APK Files", "*.apk")])
        if path:
            self.entry_apk.delete(0, "end")
            self.entry_apk.insert(0, path)

    def start_process(self):
        apk_input = self.entry_apk.get()
        if not os.path.exists(apk_input):
            messagebox.showerror("Lỗi", "File APK không tồn tại!")
            return
        
        self.btn_run.configure(state="disabled")
        threading.Thread(target=self.run_logic, args=(apk_input,), daemon=True).start()

    def run_logic(self, apk_input):
        try:
            workspace = "workspace"
            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)
            
            base_name = os.path.basename(apk_input).replace(".apk", "")
            decode_path = os.path.join(workspace, f"{base_name}_src")
            unsigned_apk = os.path.join(workspace, "unsigned.apk")
            aligned_apk = os.path.join(workspace, "aligned.apk")
            final_apk = os.path.join(output_dir, f"{base_name}_resigned.apk")

            # Xóa workspace cũ
            if os.path.exists(workspace): shutil.rmtree(workspace)

            self.log("Đang giải mã APK...")
            decompile_apk(apk_input, decode_path, self.tools['apktool'])

            self.log("Đang đóng gói (Building)...")
            build_apk(decode_path, unsigned_apk, self.tools['apktool'])

            self.log("Đang tối ưu (Zipalign)...")
            zipalign_apk(self.tools['zipalign'], unsigned_apk, aligned_apk)

            self.log("Đang ký (Signing)...")
            sign_apk(self.tools['apksigner'], self.tools['keystore'], self.tools['ks_pass'], aligned_apk, final_apk)

            self.log(f"HOÀN THÀNH! File lưu tại: {final_apk}")
            messagebox.showinfo("Thành công", f"Đã lưu tại: {final_apk}")

        except Exception as e:
            self.log(f"LỖI: {str(e)}")
            messagebox.showerror("Lỗi hệ thống", str(e))
        finally:
            self.btn_run.configure(state="normal")

if __name__ == "__main__":
    app = ResignerApp()
    app.mainloop()