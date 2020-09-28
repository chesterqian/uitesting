'''
Created on Oct 27, 2014

@author: chester.qian
'''
import memcache

HOSTS = {
        'uat': '10.128.34.195:11211',
        'socialtest': '10.128.34.195:11211',
        'qaschooluat': '10.128.34.195:11211',
        'qa': '10.43.227.235:11211'
        }

MAX_TRIES = 5

class MemoryCacheOperator:
    def __init__(self, environment):
        self.client = memcache.Client([HOSTS[environment]], debug=0)
    
    def delete_school_member_settings(self, member_id):
        key, n = 'etss_memsettings_v3_%s_school' % member_id, 1
        # 'delete' function returns Nonezero on success.
        while not self.client.delete(key):
            if n > MAX_TRIES:
                raise Exception, 'Memcache deletion failed!'
            n += 1
        # 'return 1' for test account preparation introspection in robot script.
        return 1


if __name__ == '__main__':
    memcache_operator = MemoryCacheOperator('uat')
    # 23791987	SPC110	fr	SPC1503test3875@qp1.org
    memcache_operator.delete_school_member_settings(23791987)