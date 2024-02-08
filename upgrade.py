import sys
import urllib.request
import os
import ssl
import time
import threading
class Log_writer(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")  # 防止编码错误

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
log_time = time.strftime("-%Y%m%d-%H%M%S", time.localtime())  # 时间戳
filename = 'upgrade-log' + log_time + '.txt'
log_write = Log_writer(filename)  
sys.stdout = log_write

check_directory = "tempfile"#检查tempfile目录是否存在
if not os.path.exists(check_directory):
    try:
        os.makedirs(check_directory)
        print(f"Debug:检测到没有tempfile目录,目录'{check_directory}'已成功创建")
        pass
    except Exception as directory_Error:
        print(f"Error[已保存到日志]:检测到没有tempfile目录,但失败创建目录'{check_directory}': {directory_Error}")
        sys.exit()
else:
    print(f"Debug:目录'{check_directory}'存在")
    pass

check_file = "./tempfile/index.py"#检测index.py是否提前存在
if os.path.exists(check_file):
    print("Debug:index已存在,进行删除")
    if os.path.exists(check_file):
        os.remove(check_file)
        print("Debug:文件成功删除,进行下一步操作")
        pass
    else:
        print("Error[已保存到日志]:删除api文件失败")
        sys.exit()
else:
    pass

print("Debug:正在通过ssl协议从官网下载更新文件")
# 定义下载文件的 URL
download_api_url = 'https://www.y3hfg.cn/api/index.py'
# 定义保存文件的本地路径
api_filename_path = './tempfile/index.py'
# 创建 SSLContext 对象，用于配置 SSL 验证选项
ssl_context = ssl.create_default_context()
# 设置 SSLContext 对象的验证模式为必须验证
ssl_context.verify_mode = ssl.CERT_REQUIRED
# 设置 SSLContext 对象的主机名验证选项为启用
ssl_context.check_hostname = True
try:
    # 使用 urllib.request.urlretrieve 下载文件，并传入 SSLContext 对象进行 SSL 证书验证
    with urllib.request.urlopen(download_api_url, context=ssl_context) as response, open(api_filename_path, 'wb') as out_file:
        # 读取响应内容并保存到本地文件
        out_file.write(response.read())
    print("Debug:更新文件通过 SSL 证书验证下载成功！")
    pass
except Exception as ssl_api_download_Error:
    print(f"Error:更新文件在下载过程中发生错误:{ssl_api_download_Error}")
    sys.exit()

local_index = "./index.py"
os.remove(local_index)
print("Debug:原始文件成功删除,进行下一步操作")
def move_file(Uupgrade_file_path, Ppaste_file_path):
    try:
        os.rename(Uupgrade_file_path, Ppaste_file_path)
        print(f"文件成功从 {Uupgrade_file_path} 移动到 {Ppaste_file_path}")
    except Exception as copy_file_Error:
        print(f"移动文件时发生错误：{copy_file_Error}")
upgrade_file_path = './tempfile/index.py'
paste_file_path = './index.py'
move_file(upgrade_file_path, paste_file_path)

print("Debug-U:日志已保存在程序所在目录,按Enter退出程序") 
input("按Enter退出")