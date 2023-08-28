
# def common_datas(self):
#     self.baidu_url = "https://www.baidu.com/"
#
# def login_data(self):
#     self.success_data = {'user':"abc",'pwd':"123"}

common_datas = {
    "baidu_url" : "https://www.baidu.com/"
}

baidu_url = common_datas["baidu_url"]

login_data = {
    'success_data': {
        'user': 'valid_username',
        'pwd': 'valid_password'
    },
    'invalid_data': {
        'user': 'invalid_username',
        'pwd': 'invalid_password'
    }
}