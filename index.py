import os
import urllib.request
import sys
import time

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
filename = 'log' + log_time + '.txt'
log_write = Log_writer(filename)  
sys.stdout = log_write

print("Made by y3team www.y3hfg.cn")

check_directory = "tempfile"#检查tempfile目录是否存在
if not os.path.exists(check_directory):
    try:
        os.makedirs(check_directory)
        print(f"Debug:检测到没有tempfile目录，目录'{check_directory}'已成功创建")
        pass
    except Exception as e:
        print(f"Error[已保存到日志]:检测到没有tempfile目录，但失败创建目录'{check_directory}': {e}")
        sys.exit()
else:
    print(f"Debug:目录'{check_directory}'存在")
    pass

check_file = "./tempfile/api.txt"#检测api.txt是否提前存在
if os.path.exists(check_file):
    print("Debug:api.txt已存在，进行删除")
    if os.path.exists(check_file):
        os.remove(check_file)
        print("Debug:文件成功删除,进行下一步操作")
        pass
    else:
        print("Error[已保存到日志]:删除api文件失败")
        sys.exit()
else:
    pass

download_url = "https://www.y3hfg.cn/api/api.txt"#在此处填入
savepath = "./tempfile/api.txt"
try:
    urllib.request.urlretrieve(download_url, savepath)
    print(f"Debug:api文件成功下载 {savepath}")
except Exception as apidownloadError:
    print(f"Error[已保存到日志]:api文件下载失败: {apidownloadError}")#api处理报错
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
except Exception as e:
    print("Error[已保存到日志]:打开文件时发生了错误", e)
    sys.exit()

if int(api_verb) ==100:#检测版本
    print("Debug:您的程序是最新版本")
    pass
elif int(api_verb) >100:
    print("Debug:当前版本不是最新版本，请立即更新")
else:
    print("Error[已保存到日志]:遇到未知错误,请发送日志到y3team@outlook.com")
    sys.exit()



print("日志已保存在程序所在目录，按Enter退出程序") 
input("退出成功")