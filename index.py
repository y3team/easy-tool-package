import os
import urllib.request
import sys
import time
import ssl

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
filename = 'index-log' + log_time + '.txt'
log_write = Log_writer(filename)  
sys.stdout = log_write

print("Made by y3team www.y3hfg.cn")

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

check_file = "./tempfile/api.txt"#检测api.txt是否提前存在
if os.path.exists(check_file):
    print("Debug:api.txt已存在,进行删除")
    if os.path.exists(check_file):
        os.remove(check_file)
        print("Debug:文件成功删除,进行下一步操作")
        pass
    else:
        print("Error[已保存到日志]:删除api文件失败")
        sys.exit()
else:
    pass

print("Debug:正在通过ssl协议从官网下载api文件")
# 定义下载文件的 URL
download_api_url = 'https://www.y3hfg.cn/api/api.txt'
# 定义保存文件的本地路径
api_filename_path = './tempfile/api.txt'
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
    print("Debug:api文件通过 SSL 证书验证下载成功！")
    pass
except Exception as ssl_api_download_Error:
    print(f"Error:api文件在下载过程中发生错误:{ssl_api_download_Error}")
    sys.exit()

saving_api = "./tempfile/api.txt"#读取api
try:
    with open(saving_api, 'r') as file:
        api_verb = file.read()
        print("Debug:api文件成功读取")
        pass
except FileNotFoundError:
    print("Error[已保存到日志]:文件不存在(0.00001%遇到这个Error[已保存到日志]=)")
    sys.exit()
except Exception as read_api_Error:
    print("Error[已保存到日志]:打开文件时发生了错误", read_api_Error)
    sys.exit()

if int(api_verb) ==110:#检测版本
    print("Debug:您的程序是最新版本")
    os.remove(saving_api)
    pass
elif int(api_verb) >90:
    print("Debug:当前版本不是最新版本，正在启动更新程序")
    upgrade_path = "upgrade.py"  # 替换为你的应用程序路径
    try:
        # 使用 os.system() 打开应用程序
        os.system(upgrade_path)
        print("Debug:应用程序已成功打开！")
        sys.exit()
    except Exception as upgrade_app_Error:
        print("Error:打开应用程序时出现错误：", upgrade_app_Error)
        sys.exit()
else:
    
    print("Error[已保存到日志]:遇到未知错误,请发送日志到y3team@outlook.com")
    sys.exit()

print("日志已保存在程序所在目录,按Enter退出程序") 
input("按Enter退出,Designed by y3team")