import sys, time, datetime

sys.path.append('../db_init')
try:
    from mysql_conn import DB
except ImportError:
    from .mysql_conn import DB

# 定义过去时间，time.localtime(time.time())格式化时间戳为本地时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 100000))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 10000))

# 获取当前时间
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# create data
user_data = {

}


# Inster table datas
def init_data():
    DB().init_data()


if __name__ == '__main__':
    init_data()