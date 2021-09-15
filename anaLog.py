import time

log_path = '/Users/linsen/log.log'

KEYWORDS = {'ANR','CRASH','NullPointerException'}

BUNDLE_ID = 'com.jinse'

with open(log_path, encoding="utf-8", errors='ignore') as log_f:
    while True:
        line = log_f.readline()
        if line:
            for key in KEYWORDS:
                if line.find(key) != -1:  # 检查到指定异常
                    if BUNDLE_ID in line: # 检测到了异常并且检测到自己要检测的APP关键字
                        message = "检测到：{key}\n{log}".format(key=key, log=line)
                        print(message)
                    else:
                        time.sleep(1)
                        exception_line = line
                        for i in range(30):
                            try:
                                next_line = next(log_f)
                            except StopIteration as e:
                                time.sleep(1)
                                continue
                            if "	at " in next_line:
                                exception_line += next_line
                            else:
                                if BUNDLE_ID in exception_line:
                                    message = "检测到：{key}\n{log}".format(key=key, log=exception_line)
                                    print(message)
                                break
        else:
            print("无错误")
            break
