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




    def get_departments(self, department_id=0, page_size=10, page_token=None, fetch_child=False):
        '''
        '''
        base_url = 'https://open.feishu.cn/open-apis/contact/v1/department/simple/list?department_id={0}&page_size={1}'.format(department_id, page_size)
        if page_token:
            base_url = '{0}&page_token={1}'.format(base_url, page_token)
        if fetch_child:
            base_url = '{0}&fetch_child=true'.format(base_url, fetch_child)
        else:
            base_url = '{0}&fetch_child=false'.format(base_url, fetch_child)

        try:
            res = requests.get(base_url, headers=self.headers)
            if res.status_code == 200:
                res_json = res.json()
                return res_json

        except Exception as e:
            return {"error": e}




    def get_sub_departments(self, department_id=0, page_size=10, page_token=None, fetch_child=False):
        '''
        '''
        return self.get_departments(department_id, page_size, page_token, fetch_child)




    def get_department_members(self, department_id=0, page_size=10, page_token=None, fetch_child=False):
        '''
        '''
        base_url = 'https://open.feishu.cn/open-apis/contact/v1/department/user/list?department_id={0}&page_size={1}'.format(department_id, page_size)
        if page_token:
            base_url = '{0}&page_token={1}'.format(base_url, page_token)
        if fetch_child:
            base_url = '{0}&fetch_child=true'.format(base_url, fetch_child)
        else:
            base_url = '{0}&fetch_child=false'.format(base_url, fetch_child)
        
        try:
            res = requests.get(base_url, headers=self.headers)
            if res.status_code == 200:
                res_json = res.json()
                return res_json

        except Exception as e:
            return {"error": e}        
