# coding: utf-8

class AccountInfo():
    @property
    def phone_number(self):
        return self.key['phone_number']

    @property
    def login_password(self):
        return self.key['login_password']

    @property
    def trade_password(self):
        return self.key['trade_password']

    @property
    def user_name(self):
        return self.key['user_name']

    @property
    def cert_no(self):
        return self.key['cert_no']

    @property
    def is_bind_card(self):
        return self.key['is_bind_card']

    @property
    def recharge_amount(self):
        return self.key['recharge_amount']

    @property
    def withdraw_amount(self):
        return self.key['withdraw_amount']

    def __init__(self, account_no):
        self.account_uat_1 = {
            'phone_number': '15666666669',
            'login_password': 'a0000000',
            'trade_password': (8, 10, 12, 14, 16, 7),
            'user_name': 'yhzl',
            'cert_no': '230622198308213775',
            'is_bind_card': 'Y',
            'recharge_amount': '0.2',
            'withdraw_amount': '0.1',
        }

        self.account_uat_2 = {
            'phone_number': '15666666667',
            'login_password': 'a0000000',
            'trade_password': '',
            'user_name': '',
            'cert_no': '',
            'is_bind_card': 'N',
            'recharge_amount': '0.2',
            'withdraw_amount': '0.1',
        }

        self.account_uat_3 = {
            'phone_number': '17100000012',
            'login_password': '12qwaszx',
            'trade_password': (8, 10, 12, 14, 16, 7),
            'recharge_amount': '0.2',
            'withdraw_amount': '0.1',
        }

        self.account_prd_1 = {
            'phone_number': '15221189657',
            'login_password': 'a0000000',
            'trade_password': (8, 11, 14, 9, 12, 15),
            'recharge_amount': '0.02',
            'withdraw_amount': '0.01',
        }

        self.account = {
            'u1': self.account_uat_1,
            'u2': self.account_uat_2,
            'u3': self.account_uat_3,
            'p1': self.account_prd_1,
        }

        self.key = {
            'phone_number': '',
            'login_password': '',
            'trade_password': '',
            'user_name': '',
            'cert_no': '',
            'is_bind_card': '',
            'recharge_amount': '',
            'withdraw_amount': '',
        }

        if account_no not in self.account.keys():
            raise Exception('account_no error !!!')
        pass

        for key in self.key.keys():
            if key not in self.account[account_no].keys():
                continue
            else:
                self.key[key] = self.account[account_no][key]


if __name__ == '__main__':
    a = AccountInfo('p1')
    b = AccountInfo('u2')
    c = AccountInfo('u3')
    d = AccountInfo('u1')
    # print (a.phone_number)
    # print b.phone_number
    # print c.phone_number
    # print d.phone_number
