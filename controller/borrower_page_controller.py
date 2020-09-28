# -*- coding: utf-8 -*-
__author__ = 'yuanyuan.guo'

from ui.borrower_pages.main_borrower_page import MainBorrowerPage
from robot.api.deco import keyword
from selenium.webdriver.chrome.webdriver import WebDriver


class BorrowerPageController():
    def __init__(self):
        self.borrower_page_obj = None
        self._current_borrower_page = None
        self.web_driver = None

    # 注册登陆首页
    @keyword(name='Go To Main Page')
    def bp_go_to_main_page(self):
        self.web_driver = WebDriver()
        self.web_driver.maximize_window()
        self.borrower_page_obj = MainBorrowerPage(self.web_driver)
        self.borrower_page_obj.go_to_main_page(environment='demo')

    # 创建账户
    @keyword('Create Account')
    def bp_go_to_create_account_page(self, user_name, password, password_confirm,
                                     email, input_refer, input_ops, business_type):
        self._current_borrower_page = self.borrower_page_obj.go_to_create_account_page()
        self._current_borrower_page.create_account(user_name, password, password_confirm,
                                                   email, input_refer, input_ops, business_type)

    # 登录
    @keyword('Login')
    def bp_go_to_login_page(self, email, password):
        self._current_borrower_page = self.borrower_page_obj.go_to_login_page()
        self._current_borrower_page.login(email, password)

    # 登出
    @keyword('Logout')
    def bp_go_to_logout_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_logout_page()
        self._current_borrower_page.logout()

    # 我的账户
    @keyword('Go To My Account From Header')
    def bp_go_to_my_account_from_header(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_my_account_from_header()

    # 贷款摘要
    @keyword('Go To Loan Summary Container')
    def bp_go_to_loan_summary_container_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_loan_summary_container_page()

    # 未提交贷款
    @keyword('Go To Incomplete Loan Summary')
    def bp_go_to_incomplete_loan_summary(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_incomplete_loan_summary()
        self._current_borrower_page.go_to_incomplete_loan_summary()
        self._current_borrower_page.go_to_borrower_loan_app_page()
        all_handles = self.web_driver.window_handles
        self.web_driver.switch_to.window(all_handles[1])

    # 已申请贷款
    @keyword('Go To Complete Loan Summary')
    def bp_go_to_complete_loan_summary(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_complete_loan_summary()
        self._current_borrower_page.go_to_loan_summary_detail_page()

    # 交易记录
    @keyword('Go To Trade History')
    def bp_go_to_trade_history(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_trade_history()

    # 借款协议
    @keyword('Go To Promissory Note')
    def bp_go_to_promissory_note_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_promissory_note_page()

    # 借款协议详情
    @keyword('Go To Promissory Detail Note')
    def bp_go_to_promissory_detail_note_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_promissory_detail_note_page()

    # 银行卡
    @keyword('Go To Banks Cards')
    def bp_go_to_banks_cards_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_banks_cards_page()

    # 充值还款
    @keyword('Go To Transfer')
    def bp_go_to_transfer_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_transfer_page()

    # 充值还款详情
    @keyword('Go To Transfer Detail')
    def bp_go_to_transfer_detail_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_transfer_detail_page()

    # 还款明细
    @keyword('Go To Payment Detail')
    def bp_go_to_payment_detail_page(self):
        self._current_borrower_page = self.borrower_page_obj.go_to_payment_detail_page()
        self._current_borrower_page.go_to_payment_detail_show_page()

    # 基本信息
    @keyword('Go To Account Profile')
    def bp_go_to_account_profile_page(self, old_pwd, new_pwd, the_same_new_pwd):
        self._current_borrower_page = self.borrower_page_obj.go_to_account_profile_page()
        self._current_borrower_page.go_to_change_passwords()
        self._current_borrower_page.change_passwords(old_pwd, new_pwd, the_same_new_pwd)

    # 借款信息
    @keyword('Go To Borrower Loan App')
    def bp_go_to_borrower_loan_app_page(self, loan_sub_type, *args):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_loan_app_page(loan_sub_type)
        self._current_borrower_page.update_loan_app(*args)
        self._current_borrower_page.commit_loan_app_info()

    # 购房信息
    @keyword('Go To Down Payment Asset Info')
    def bp_go_to_borrower_down_payment_asset_info_page(self, house_estate, developer_name, refer_company_name_option,
                                                       house_address, house_total_amount, down_payment_amount,
                                                       house_city,
                                                       *args):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_down_payment_asset_info_page()
        self._current_borrower_page.submit_or_update_down_payment_asset_info(house_estate, developer_name,
                                                                             refer_company_name_option,
                                                                             house_address, house_total_amount,
                                                                             down_payment_amount, house_city,
                                                                             *args)

    # BD-BD信息
    @keyword('Go To Bd Loan_Info')
    def bp_go_to_borrower_bd_loan_info_page(self, bd_channel_option, name, ssn, cellphone, company_name, reg_code,
                                            reg_no):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_bd_loan_info_page()
        self._current_borrower_page.submit_or_update_bd_loan_info(bd_channel_option, name, ssn, cellphone, company_name,
                                                                  reg_code, reg_no)

    # 银行账户
    @keyword('Go To Bank Account Info')
    def bp_go_to_borrower_bank_account_info_page(self, loan_sub_type, account_number, province_select_option,
                                                 city_select_option, financial_institution_select_option,
                                                 account_branch, **kwargs):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_bank_account_info_page()
        self._current_borrower_page.submit_or_update_bank_account_info(loan_sub_type, account_number,
                                                                       province_select_option,
                                                                       city_select_option,
                                                                       financial_institution_select_option,
                                                                       account_branch, **kwargs)

    # SMB-财务信息
    @keyword('Go To Debt Property Info')
    def bp_go_to_borrower_debt_property_info_page(self, personal_house_select_option, personal_car_select_option,
                                                  apply_other_loan_select_option, other_yearly_income,
                                                  other_income_source_select_option, **kwargs):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_debt_property_info_page()
        self._current_borrower_page.submit_or_update_debt_property_info(personal_house_select_option,
                                                                        personal_car_select_option,
                                                                        apply_other_loan_select_option,
                                                                        other_yearly_income,
                                                                        other_income_source_select_option, **kwargs)

    # 企业信息
    @keyword('Go To Employment Info')
    def bp_go_to_employment_info_page(self, loan_sub_type, company_name, job_title, job_tenure_years_select_option,
                                      company_city, street_address, company_phone, **kwargs):
        self._current_borrower_page = self.borrower_page_obj.go_to_employment_info_page()
        self._current_borrower_page.update_employment_info(loan_sub_type, company_name, job_title,
                                                           job_tenure_years_select_option,
                                                           company_city, street_address, company_phone, **kwargs)

    # 个人信息
    @keyword('Go To Personal Info')
    def bp_go_to_borrower_personal_info_page(self, loan_sub_type, full_name, ssn, living_city, living_street_address,
                                             cellphone, yearly_income, **kwargs):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_personal_info_page()
        self._current_borrower_page.submit_or_update_personal_info(loan_sub_type, full_name, ssn, living_city,
                                                                   living_street_address,
                                                                   cellphone, yearly_income, **kwargs)

    # 联系人
    @keyword('Go To Contact Info')
    def bp_go_to_borrower_contact_page(self, loan_sub_type,
                                       relation_1_option, name_1, phone_1, job_title_1, company_name_1, address_1,
                                       **kwargs):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_contact_page()
        self._current_borrower_page.submit_or_update_loan_app(loan_sub_type,
                                                              relation_1_option, name_1, phone_1, job_title_1,
                                                              company_name_1, address_1,
                                                              **kwargs)

    # 抵押担保_抵押
    @keyword('Go To Add New Mortgage Guarantee')
    def bp_go_to_borrower_new_mortgage_guarantee_page(self, housing_address, housing_estate_name, housing_area,
                                                      house_state_option, house_owners,
                                                      house_buy_date, housing_amount, land_type_option,
                                                      house_type_option,
                                                      still_on_loan_option,
                                                      still_on_mortgage_option, **kwargs):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_mortgage_guarantee_page()
        self._current_borrower_page.add_new_mortgage(housing_address, housing_estate_name, housing_area,
                                                     house_state_option, house_owners,
                                                     house_buy_date, housing_amount, land_type_option,
                                                     house_type_option, still_on_loan_option,
                                                     still_on_mortgage_option, **kwargs)

    # 抵押担保_个人担保
    @keyword('Go To Add New Guarantee Person')
    def bp_go_to_borrower_new_guarantee_person_page(self, name, relation_option, mobile_phone, id_type_option,
                                                    id_number, age,
                                                    shares, work_phone, address):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_mortgage_guarantee_page()
        self._current_borrower_page.add_new_guarantee_person(name, relation_option, mobile_phone, id_type_option,
                                                             id_number, age, shares, work_phone, address)

    # 抵押担保_企业担保
    @keyword('Go To Add New Guarantee Company')
    def bp_go_to_borrower_new_guarantee_company_page(self, com_name, representative, relation_option, inst_code,
                                                     inst_license, reg_address,
                                                     est_date, employee_num, work_phone, op_address):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_mortgage_guarantee_page()
        self._current_borrower_page.add_new_guarantee_company(com_name, representative, relation_option, inst_code,
                                                              inst_license, reg_address,
                                                              est_date, employee_num, work_phone, op_address)

    # 所需文件
    @keyword('Go To Document Info')
    def bp_go_to_borrower_document_page(self, loan_sub_type, file_path, *document_type_args):
        self._current_borrower_page = self.borrower_page_obj.go_to_borrower_document_page(loan_sub_type)
        self._current_borrower_page.upload_documents(file_path, *document_type_args)
        self._current_borrower_page.submit_loan()

    @keyword('Close')
    def bp_close(self):
        self.web_driver.close()
        self.web_driver.quit()

    @keyword('Sleep Time')
    def bp_implicitly_wait(self, time):
        self.web_driver.implicitly_wait(time)


if __name__ == '__main__':
    bp = BorrowerPageController()
    bp.bp_go_to_main_page()
    # bp.bp_go_to_login_page('qwer1234@163.com', 'qwer1234')
    # bp.bp_go_to_loan_summary_container_page()
    # bp.bp_go_to_incomplete_loan_summary()
    # 创建首付贷
    # bp.bp_go_to_create_account_page('asdf1312234','qwer1234','qwer1234','asdf1312234@163.com','yuan_huang_admin','yuan_huang_admin','1')
    # bp.bp_go_to_borrower_loan_app_page('DOWN_PAYMENT', '40000', '1', '2', '5', 'down_payment', 'DOWN_PAYMENT')
    # coop_info_args = ("1", "1")
    # bp.bp_go_to_borrower_down_payment_asset_info_page(u"绿地", u"开发商名", '1', u'新房地址', '200000', '200000',
    # u"上海", *coop_info_args)
    # bp.bp_implicitly_wait(30)
    # personal_info_kwargs = {'education_level_option': '1',
    # 'house_status_option': '1',
    # 'marital_status_option': '2',
    # 'spouse_name': u'郭媛媛',
    # 'spouse_ssn': '131081198802011102',
    # 'years_lived_option': '1',
    # 'work_phone': '021-63232300',
    # 'wechat': '998008'}
    # bp.bp_go_to_borrower_personal_info_page('DOWN_PAYMENT', u'孙美洪', '330719196804253671', u"上海",
    # u"陆家嘴", '18817333440', '200000', **personal_info_kwargs)
    # bp.bp_implicitly_wait(30)
    # employment_info_kwargs = {'company_phone_ext': '1122',
    # 'company_segment_select_option': '4',
    # 'company_type_select_option': '5',
    # 'company_size_select_option': '3'}
    # bp.bp_go_to_employment_info_page('DOWN_PAYMENT', u"理财网", u"测试工程师", '2', u"上海",
    #                                  u"新天地", '021-63232300', **employment_info_kwargs)
    # bank_account_info_kwargs = {'bank_pay_mode_option': '1'}
    # bp.bp_go_to_borrower_bank_account_info_page('DOWN_PAYMENT', '6204830212896540', '9',
    #                                             '1', '12', u"上海", **bank_account_info_kwargs)
    # provide_second_house_kwargs = {'provide_second_house_option': '2'}
    #
    # bp.bp_go_to_borrower_new_mortgage_guarantee_page(u"房屋地址", u"小区名称", '130', '1', u"王华", '2014', '2000000',
    #                                                  '2', '1', '2', '2', **provide_second_house_kwargs)
    # bp.bp_go_to_borrower_new_guarantee_person_page(u'李娟', '1', '18817333550', '1', '131081198802011102',
    #                                                '28', '30', '021-63232300', u"新天地")
    # bp.bp_go_to_borrower_new_guarantee_company_page(u"点融网", u"王华", '2', '567432', '9876509', u"上海",
    #                                                 '2015-12-01', '3000', '021-63232300', u"新天地")
    # contact_kwargs = {'relation_2_option': '2',
    #                   'name_2': 'amy',
    #                   'phone_2': '18817333550',
    #                   'job_title_2': 'test',
    #                   'company_name_2': 'zhihua',
    #                   'address_2': 'shanghai',
    #                   'relation_3_option': '1',
    #                   'name_3': 'lili',
    #                   'phone_3': '18817333459',
    #                   'job_title_3': 'testleader',
    #                   'company_name_3': 'tuniu',
    #                   'address_3': 'nanjing',
    #                   'relation_4_option': '1',
    #                   'name_4': 'huahua',
    #                   'phone_4': '18817444550',
    #                   'job_title_4': 'develop',
    #                   'company_name_4': 'huawei',
    #                   'address_4': 'guangzhou',
    #                   'relation_5_option': '1',
    #                   'name_5': 'lucy',
    #                   'phone_5': '18817666990',
    #                   'job_title_5': 'devops',
    #                   'company_name_5': 'zhongxing',
    #                   'address_5': 'hunan'}
    # bp.bp_go_to_borrower_contact_page('DOWN_PAYMENT', '1', u"王铎", '18817666330', u"开发",
    #                                   u"腾讯", u"淮海路", **contact_kwargs)
    # document_types = ['REQUIRED_IDENTITY_CARD', 'REQUIRED_RESIDENCE_REGISTRATION', 'REQUIRED_BANK_STATEMENT',
    #                   'REQUIRED_BANK_CARD', 'REQUIRED_APPLICATION_FORM',]
    # bp.bp_go_to_borrower_document_page('DOWN_PAYMENT',
    #                                    'resources\\borrower_documents\\sample_documents\\Koala.jpg',
    #                                    *document_types)
    #
    # bp.bp_close()
    # 创建BD贷款
    # bp.bp_go_to_login_page('yuanjie1', 'qwer1234')
    # bp.bp_go_to_loan_summary_container_page()
    # bp.bp_go_to_incomplete_loan_summary()
    # bp.bp_go_to_create_account_page('yuanjie1', 'qwer1234', 'qwer1234', 'yuanjie1@163.com', 'yuan_huang_admin',
    #                                 'yuan_huang_admin', '16')
    # bp.bp_go_to_borrower_loan_app_page('BD_GC', '40000', '1', '2', '2', 'BD_GC', 'BD_GC', '2', '1')
    # personal_info_kwargs_for_bd = {'marital_status_option': '2',
    # }
    # bp.bp_go_to_borrower_personal_info_page('BD_GC', u'孙美洪', '330719196804253671', u"上海",
    #                                         u"陆家嘴", '18817333440', '200000', **personal_info_kwargs_for_bd)
    # bp.bp_implicitly_wait(30)
    # employment_info_page_for_bd = {'company_segment_select_option': '1',
    #                                'company_size_select_option': '1',
    #                                'reg_code': '0315',
    #                                'reg_no': '9887345'}
    # bp.bp_go_to_employment_info_page('BD_GC', u'理财网', u'测试工程师', '2', u'上海', u'新天地', '021-63232300',
    #                                  **employment_info_page_for_bd)
    # bp.bp_go_to_borrower_bd_loan_info_page('1', u'测试人', '330719196804253671', '18817333990', u'陆金所', '111222', '111222')
    # bank_account_info_for_bd = {'account_decision': '1'}
    # bp.bp_go_to_borrower_bank_account_info_page('BD_GC', '6204830212896540', '9',
    #                                             '1', '12', u"上海", **bank_account_info_for_bd)
    # provide_second_house_kwargs = {'provide_second_house_option': '2'}
    #
    # bp.bp_go_to_borrower_new_mortgage_guarantee_page(u"房屋地址", u"小区名称", '130', '1', u"王华", '2014', '2000000',
    #                                                  '2', '1', '2', '2', **provide_second_house_kwargs)
    # bp.bp_go_to_borrower_new_guarantee_person_page(u'李娟', '1', '18817333550', '1', '131081198802011102',
    #                                                '28', '30', '021-63232300', u"新天地")
    # bp.bp_go_to_borrower_new_guarantee_company_page(u"点融网", u"王华", '2', '567432', '9876509', u"上海",
    #                                                 '2015-12-01', '3000', '021-63232300', u"新天地")
    # document_types = ['REQUIRED_IDENTITY_CARD', 'OPTIONAL_BANK_STATEMENT',]
    # bp.bp_go_to_borrower_document_page('BD_GC',
    #                                    'resources\\borrower_documents\\sample_documents\\Koala.jpg',
    #                                    *document_types)
    # bp.bp_close()
    # 创建小微企业信用贷款
    bp.bp_go_to_create_account_page('yun12346q11', 'qwer1234', 'qwer1234', 'yun12346q11@163.com', 'yuan_huang_admin',
                                    'yuan_huang_admin', '5')
    # bp.bp_go_to_login_page('yuan12346q11', 'qwer1234')
    # bp.bp_go_to_loan_summary_container_page()
    # bp.bp_go_to_incomplete_loan_summary()
    bp.bp_go_to_borrower_loan_app_page('SMB', '40000', '1', '2', '2', 'SMB', 'SMB', '2')
    personal_info_kwargs_for_smb = {'education_level_option': '1',
                                    'house_status_option': '1',
                                    'marital_status_option': '2',
                                    'spouse_name': u'郭媛媛',
                                    'spouse_ssn': '131081198802011102',
                                    'years_lived_option': '1',
                                    'work_phone': '021-63232300',
                                    'tax_option': '1',
                                    'wechat': '998008'}
    bp.bp_go_to_borrower_personal_info_page('SMB', u'孙美洪', '330719196804253671', u"上海",
                                            u"陆家嘴", '18817333440', '200000', **personal_info_kwargs_for_smb)
    employment_info_kwargs_for_smb = {'application_share': '20',
                                      'company_size_select_option': '1',
                                      'company_segment_select_option': '1',
                                      'reg_code': '0123',
                                      'reg_no': '0222',
                                      'company_phone_ext': '1122',
                                      'estiblish_date': '2015-12-18',
                                      'city2': u'上海',
                                      'company_type': '2',
                                      'street_address2': u'陆家嘴',
                                      'total_income': '33300',
                                      'total_cost': '3300',
                                      'profit': '50',
                                      'loan_state': '1',
                                      'mortgage_state': '1',
                                      'lawsuit_state': '1',
                                      'paidtax_state': '1'}
    bp.bp_go_to_employment_info_page('SMB', u"理财网", u"测试工程师", '2', u"上海",
                                     u"新天地", '021-63232300', **employment_info_kwargs_for_smb)
    debt_property_info_for_smb = {'other_loan_num_option': '1',
                                  'liability_1_amount': '2000',
                                  'liability_1_date': '2012-11-11'}
    bp.bp_go_to_borrower_debt_property_info_page('1', '1', '1', '30000', '1', **debt_property_info_for_smb)
    bank_account_info_for_smb = {'account_decision': '1'}
    bp.bp_go_to_borrower_bank_account_info_page('SMB', '6204830212896540', '9',
                                                '1', '12', u"上海", **bank_account_info_for_smb)
    provide_second_house_kwargs = {'provide_second_house_option': '2'}

    bp.bp_go_to_borrower_new_mortgage_guarantee_page(u"房屋地址", u"小区名称", '130', '1', u"王华", '2014', '2000000',
                                                     '2', '1', '2', '2', **provide_second_house_kwargs)
    bp.bp_go_to_borrower_new_guarantee_person_page(u'李娟', '1', '18817333550', '1', '131081198802011102',
                                                   '28', '30', '021-63232300', u"新天地")
    bp.bp_go_to_borrower_new_guarantee_company_page(u"点融网", u"王华", '2', '567432', '9876509', u"上海",
                                                    '2015-12-01', '3000', '021-63232300', u"新天地")
    document_types = ['REQUIRED_IDENTITY_CARD', 'REQUIRED_RESIDENCE_REGISTRATION',
                      'REQUIRED_COM_REVENUE_LICENSE', 'REQUIRED_COM_CERT_ORGANIZATION_CODE',
                      'REQUIRED_COM_TAX_REGISTRATION_CERT', 'REQUIRED_BANK_STATEMENT',
                      'REQUIRED_COM_BANK_STATEMENT', 'REQUIRED_COM_COMMITMENT_LETTER',
                      'REQUIRED_COM_REVENUE_PROOF', 'REQUIRED_PBOC_CREDIT_REPORT',
                      'REQUIRED_COM_PBOC_CREDIT_REPORT', 'REQUIRED_BANK_CARD',
                      'REQUIRED_COM_ASSOCIATION_ARTICLES', 'REQUIRED_APPLICATION_FORM', ]
    bp.bp_go_to_borrower_document_page('SMB',
                                       'resources\\borrower_documents\\sample_documents\\Koala.jpg',
                                       *document_types)
    bp.bp_close()



