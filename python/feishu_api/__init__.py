#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Wed Dec  9 09:59:22 2020
#========================================
import requests
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class FeishuAPI(object):
    '''
    '''
    def __init__(self, app_id, app_secret):
        '''
        '''
        self.app_id       = app_id
        self.app_secret   = app_secret
        self.access_token = self.get_access_token()
        self.headers      = {
            'Authorization': 'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json'
        }



    def get_access_token(self):
        '''
        '''
        data = {
            'app_id': self.app_id,
            'app_secret': self.app_secret
        }

        try:
            res = requests.post('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/', json=data)
            if res.status_code == 200:
                res_json = res.json()
                access_token = res_json.get('tenant_access_token')
                return access_token

        except Exception as e:
            return {"error": e}




    def get_departments(self):
        '''
        '''
        try:
            res = requests.get('https://open.feishu.cn/open-apis/contact/v1/department/simple/list?department_id=0&page_size=10&fetch_child=true', headers=self.headers)
            if res.status_code == 200:
                res_json = res.json()
                return res_json

        except Exception as e:
            return {"error": e}




    def get_department_users(self, open_dept_id):
        '''
        '''
        try:
            res = requests.get('https://open.feishu.cn/open-apis/contact/v1/department/user/list?open_department_id={0}&page_size=100&fetch_child=true'.format(open_dept_id), headers=self.headers)
            if res.status_code == 200:
                res_json = res.json()
                return res_json

        except Exception as e:
            return {"error": e}        
