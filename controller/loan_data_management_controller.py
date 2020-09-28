# -*- coding: utf-8 -*-
__author__ = 'chen han dong'

import time
import itertools
from copy import deepcopy
from functools import wraps
from robot.api.deco import keyword
from common.global_config import Global
from common.utility import Utility
from service_entities.borrower_service_entities.main_borrower_service_entity import \
    MainBorrowerServiceEntity
from service_entities.lender_service_entities.main_vip_service_entity import \
    MainVipServiceEntity
from service_entities.loan_approval_service_entities.main_loan_approval_service_entity import \
    MainLoanApprovalServiceEntity
from service_entities.mobile_borrower_service_entities.main_mobile_borrower_entity import \
    MainMobileBorrowerEntity
from database.oracle_database_operators import OracleDatabaseOperator


def approval_session(user_identity, password='welcome1'):
    def function_catch(func):
        @wraps(func)
        def wrapper(loan_data_controller, *args, **kwargs):
            loan_data_controller.main_approval.login_crc(user_identity, password)
            result = func(loan_data_controller, *args, **kwargs)
            loan_data_controller.main_approval.logout_crc()
            return result

        return wrapper

    return function_catch


class LoanDataManagementController(object):
    def __init__(self):
        self.main_borrower = None
        self.main_approval = None
        self.main_lender = None
        self.lender_user_phone = None
        self.lender_password = None
        self.temp_loan_app_workflow = None
        self.loan_maturity = None
        self.mobile_borrower_aid = None
        self.mobile_loan_app_id = None
        self.basis_loan_app_workflow = [{'update_borrower_loan_app': {}},
                                        {'update_borrower_personal_info': {}},
                                        {'update_borrower_employment_info': {}},
                                        {
                                            'update_borrower_bank_account_info': {}},
                                        {'add_or_update_borrower_mortgage': {}},
                                        {
                                            'update_borrower_guarantee_person': {}},
                                        {
                                            'update_borrower_guarantee_company': {}},
                                        {'update_borrower_contact_info': {}},
                                        {'upload_borrower_document': {}},
                                        {
                                            'generate_borrower_loan_application': {}}]

    def _get_loan_app_workflow(self, loan_sub_type):
        type_temp = (
                    'BD' in loan_sub_type.upper()) and 'BD' or loan_sub_type.upper()
        temp_workflow = deepcopy(self.basis_loan_app_workflow)
        if type_temp == 'MCA':
            temp_workflow[-3]['update_borrower_contact_info'] = {
                'index_tuple': (4,)}
        elif type_temp == 'BD':
            temp_workflow.pop(-3)
            temp_workflow.insert(-1, {'update_borrower_bd_loan_info': {}})
        elif type_temp == 'DOWN_PAYMENT':
            temp_workflow.insert(-1, {
                'update_borrower_down_payment_asset_info': {}})
        elif type_temp == 'SMB':
            temp_workflow.pop(-3)
            temp_workflow.insert(3, {'update_borrower_debt_property_info': {}})

        return temp_workflow

    def _loan_id_handler(self, loan_id):
        try:
            loan_id = loan_id or self.mobile_loan_app_id or self.main_borrower.loan_id
        except AttributeError:
            raise NotImplementedError(
                "Please incoming parameter loan_id or create/login the borrower!")
        return loan_id

    def _mobile_ssn_db_create(self):
        """绕过手机端身份证输入,DB直接插数据"""
        utility = Utility()
        actor_dict = {'fname': utility.fake_cn.name(),
                      'ssn': utility.gennerator}
        pi_dict = actor_dict.copy()
        pi_dict.update({'dob': utility.fake_cn.date_time()})
        self.sl_db.update_multi_unspecified_column_for_actor(
            self.mobile_borrower_aid, actor_dict)
        self.sl_db.update_multi_unspecified_column_for_pi(
            self.mobile_borrower_aid, pi_dict)

    @keyword('Set Environment Args')
    def set_environment_args(self, environment):
        """Require an environment parameters

        Currently supports DEMO and  DEV and TRUST this parameters
        """
        # self.environment = environment
        self.env = getattr(Global.Environment,
                           'DIANRONG_' + environment.upper())
        self.sl_db = OracleDatabaseOperator(environment)
        self.quartz_db = OracleDatabaseOperator(environment.lower() + '_quartz')
        actors = ['yuan_huang@sl.com', 'handong.chen@sl.com']
        [self.sl_db.change_actor_password(a) for a in actors]
        self.main_borrower = MainBorrowerServiceEntity(self.env)
        self.main_approval = MainLoanApprovalServiceEntity(environment)
        self.main_lender = MainVipServiceEntity(environment)
        # self.sl_db.change_actor_password('3566160688352964@dianrong.com')

    @keyword('Borrower Login')
    def borrower_login(self, username, password='welcome1'):
        # None为了兼容老代码
        self.main_borrower.login_borrower(None, username, password)
        self.loan_maturity = self.main_borrower.reload_borrower_loan_app().apiReturn_loanMaturity

    @keyword('Borrower Logout')
    def borrower_logout(self):
        self.main_borrower.logout()

    @keyword('Create Borrower Account')
    def create_borrower_account(self, loan_sub_type='MCA',
                                input_ops='workflowadmin1', **kwargs):
        # None为了兼容老代码
        self.main_borrower.create_borrower_account(None, loan_sub_type,
                                                   inputOps=input_ops, **kwargs)
        print '\n' + '*' * 10 + 'borrower_aid=%s, loan_app_id=%s, borrower_email=%s, borrower_password=welcome1\n' % (
            self.main_borrower.actor_id, self.main_borrower.loan_app_id,
            self.main_borrower.borrower_info_data.apiReturn_email)

    def create_borrower_by_mobile(self, loan_sub_type):
        """模拟手机创贷流程,主要bank_card需要传2次并且内容不一样"""
        borrower = MainMobileBorrowerEntity(self.env)
        # 注册并创建贷款
        borrower.get_verify_code()
        self.mobile_borrower_aid = borrower.create_borrower_actor()
        # 指定推荐销售
        # self.mobile_borrower_aid = borrower.create_borrower_actor(inviteCode=11375888)
        borrower.mobile_login()
        borrower.upload_borrower_bank_card()
        borrower.update_loan_app(loan_sub_type)
        self._mobile_ssn_db_create()
        # 手机补填资料
        borrower.update_borrower_personal_basic()
        borrower.update_borrower_personal_income()
        borrower.update_borrower_personal_asset()
        borrower.update_borrower_personal_debt()
        borrower.update_borrower_employment(companySize='LESS_THAN_20')
        borrower.update_borrower_contact()
        borrower.upload_borrower_bank_card(method=2)
        # 双金贷特殊授权
        if loan_sub_type.upper() == 'DOUBLE_FUND':
            borrower.third_party_auths()
        # 提交至lms操作,很挫的流程
        borrower.loan_app_submit()
        self.mobile_loan_app_id = borrower.loan_app_id
        print '\n' + '*' * 10 + 'borrower_aid=%s, loan_app_id=%s, borrower_phone=%s, borrower_password=welcome1\n' % (
            self.mobile_borrower_aid, self.mobile_loan_app_id,
            borrower.cellphone)

    def lms_ops_handle(self, loan_app_id=None, aid=None):
        """
        专为手机端做预审批的流程,很挫
        """
        loan_app_id = loan_app_id or self.mobile_loan_app_id
        aid = aid or self.mobile_borrower_aid
        self.main_borrower.lms_login()
        self.main_borrower.lms_assign_ops(loan_app_id)
        self.main_borrower.go_to_new_borrower(loan_app_id, aid)
        # 上传文件
        self.main_borrower.upload_borrower_document('BANK_STATEMENT',
                                                    'dianrong/resources/borrower_documents/'
                                                    'valid_documents/BANK_STATEMENT.jpg',
                                                    actor_id=aid,
                                                    loan_app_id=loan_app_id)
        # 提交审批至workflow
        self.main_borrower.generate_borrower_loan_application(aid, loan_app_id)

    @keyword('Set Loan App Func Kwargs')
    def set_loan_app_func_kwargs(self, func_name, **kwargs):
        """设置参数只针对一次loan app更新,第二次更新loan app需要再设置一次
        """
        loan_sub_type = kwargs.has_key('loanSubType') and kwargs[
            'loanSubType'] or self.main_borrower.loan_sub_type
        self.temp_loan_app_workflow = self._get_loan_app_workflow(loan_sub_type)
        for loan_app_func_dict in self.temp_loan_app_workflow:
            if loan_app_func_dict.has_key(func_name):
                index = self.temp_loan_app_workflow.index(
                    {func_name: loan_app_func_dict[func_name]})
                loan_app_func_dict[func_name] = kwargs
                self.temp_loan_app_workflow.insert(index, {
                    func_name: loan_app_func_dict[func_name]})
                del self.temp_loan_app_workflow[index + 1]

    @keyword('Update Loan App')
    def update_loan_app(self, submit=True):
        """贷款状态：审查中
        申请状态：已提交
        """
        loan_app_workflow = self.temp_loan_app_workflow or \
                            self._get_loan_app_workflow(
                                self.main_borrower.loan_sub_type)
        if not submit:
            loan_app_workflow.pop(-1)
        for loan_app_func_dict in loan_app_workflow:
            [getattr(self.main_borrower, func)(**kwargs) for func, kwargs in
             loan_app_func_dict.iteritems()]
        print '\n' + '*' * 20 + 'loan_id is %s\n' % self.main_borrower.loan_id
        self.loan_maturity = self.main_borrower.reload_borrower_loan_app().apiReturn_loanMaturity
        self.temp_loan_app_workflow = None

    @keyword('Loan Approval To Status Reject')
    @approval_session("yuan_huang@sl.com")
    def loan_approval_to_status_reject(self, loan_id=None, *args, **kwargs):
        """贷款审批拒绝
        """
        loan_id = self._loan_id_handler(loan_id)
        self.main_approval.set_reject_loan_apply(loan_id, *args, **kwargs)

    @keyword('Loan Approval To Status Cancel')
    @approval_session("yuan_huang@sl.com")
    def loan_approval_to_status_cancel(self, loan_id=None, *args, **kwargs):
        """贷款审批撤销
        """
        loan_id = self._loan_id_handler(loan_id)
        self.main_approval.set_cancel_loan_apply(loan_id, *args, **kwargs)

    @keyword('Borrower Account Binding Approval')
    def borrower_account_binding_approval(self, loan_id=None):
        """为借款人设置代扣渠道并批准
        必须先创建或登录borrower,并是已提交的loan
        """
        with self.main_approval.session('yuan_huang@sl.com', 'welcome1'):
            loan_id = self._loan_id_handler(loan_id)
            borrower_actor = self.main_approval.get_actor_details(loan_id)
            self.main_approval.update_borrower_account_binding(loan_id,
                                                               bank_info=borrower_actor.bankAccount,
                                                               user_info=borrower_actor.personalInfo)
            self.sl_db.update_slprod_account_binding_approval(
                borrower_actor.userStatus_actorId)

    @keyword('Loan Approval To Status Pre Review')
    @approval_session("yuan_huang@sl.com")
    def loan_approval_to_status_pre_review(self, model='service', loan_id=None,
                                           aid=None, *args, **kwargs):
        """第一部分审批,可设置贷款的一些属性
        必需先登录borrower后才能正常审批,原因是贷款期限在workflow中无法获取
        """
        loan_id = self._loan_id_handler(loan_id)
        aid = aid or self.mobile_borrower_aid or self.main_borrower.actor_id
        loan_maturity = self.loan_maturity or 'Month9'
        self.main_approval.set_change_loan_flags(loan_id)
        self.main_approval.update_internal_notification_rule(loan_id)
        self.main_approval.set_loan_attribute(loan_id, maturity=loan_maturity,
                                              *args, **kwargs)
        if model == 'service':
            self.main_approval.set_id_five(loan_id)
        # 绕过id5验证
        elif model == 'db':
            self.sl_db.update_id5_status_true_by_loan_id_and_aid(loan_id, aid)

    @keyword('Loan Approval To Status Review')
    @approval_session("workflowadmin1@sl.com")
    def loan_approval_to_status_review(self, loan_id=None, **kwargs):
        """申请状态：签约条件已验证
        贷款状态：审查中
        """
        loan_id = self._loan_id_handler(loan_id)
        loan_attrs = self.main_approval.get_loan_apps(loan_id)
        # salesPhoto/verify
        if loan_attrs.applications_loanType == "PERSONAL":
            self.main_approval.set_photo_verify(loan_id)

        self.main_approval.set_app_status(loan_id, **kwargs)
        self.main_approval.submit_signing_conditions(loan_id)

    @keyword('Loan Approval To Status Investment')
    @approval_session("yuan_huang@sl.com")
    def loan_approval_to_status_investment(self, loan_id=None):
        """贷款状态：投资中
        申请状态：签约条件已验证
        """
        loan_id = self._loan_id_handler(loan_id)
        self.main_approval.submit_listing(loan_id)
        self.main_approval.change_entry_flag(loan_id)

    @keyword('New Lender To Invest')
    def new_lender_invest(self, amount=None, loan_id=None):
        """
        The default investment full.
        贷款状态：最终复审
        申请状态：签约条件已验证
        """
        loan_id = self._loan_id_handler(loan_id)
        user_id, user_phone, password = self.main_lender.register_lender_account(
            self.env)
        print '\n' + '=' * 10 + 'lender_user_id=%s, lender_user_phone=%s, lender_password=%s\n' \
                                % (user_id, user_phone, password)
        self.sl_db.update_balance_for_certain_actor(user_id, 5000000)
        amount = amount or self.main_lender.get_single_loan(loan_id).amount
        self.main_lender.buy_single_loan(loan_id, amount)

        self.lender_user_phone = user_phone
        self.lender_password = password

    # 13849477357: 11336441
    @keyword('Multiple Lender Invest')
    def multiple_lender_invest(self, user_phone_list=(13849477357,),
                               loan_id=None):
        loan_id = self._loan_id_handler(loan_id)
        amount_t = self.main_lender.get_single_loan(loan_id).amount
        amount = ((amount_t / 100) / len(user_phone_list)) * 100
        remainder = ((amount_t / 100) % len(user_phone_list)) * 100
        for phone in user_phone_list:
            actor = self.sl_db.get_actor_by_phone_number(phone)
            self.sl_db.update_balance_for_certain_actor(actor.id, 50000000)

            with self.main_lender.session(phone, 'welcome1'):
                if phone == user_phone_list[-1]:
                    amount = (remainder) and remainder + amount or amount
                    # print '=========+=========%s'%amount
                    self.main_lender.buy_single_loan(loan_id, amount)
                else:
                    # print '=========+=========%s'%amount
                    self.main_lender.buy_single_loan(loan_id, amount)

    @keyword('Lender Invest Approval')
    @approval_session("yuan_huang@sl.com")
    def lender_invest_approval(self, loan_id=None):
        # 投资后需要审批
        loan_id = self._loan_id_handler(loan_id)
        self.main_approval.submit_approve(loan_id)
        loan = self.sl_db.select_loan_by_loan_id(loan_id)
        loan_app = self.sl_db.select_from_loan_app_by_loan_id(loan_id)
        assert loan.status == 9
        assert loan_app.status == 9

    @keyword('Loan To Status Upcoming Publish')
    def loan_to_status_upcoming_publish(self):
        """贷款即将发布
        """
        self.quartz_db.update_quartz_triggers_next_fire_time("TLCScheduler",
                                                             "HOURLY", 60)

    @keyword('Loan To Status Publish')
    def loan_to_status_publish(self):
        """贷款已发布
        需求等待job跑完状态才会对
        """
        self.quartz_db.update_quartz_triggers_next_fire_time("TLCScheduler",
                                                             "THIRD_PARTY_ISSUE_LOAN",
                                                             120)

    @keyword('Wait For Loan Status')
    def wait_for_loan_status(self, loan_id=None, num=4, times=181):
        loan_id = self._loan_id_handler(loan_id)
        print_str = '\n' + '=' * 10 + '贷款状态还未到已发布第%s次'
        for count in itertools.count(1):
            result = self.sl_db.select_loan_by_loan_id(loan_id)
            if result.status == num:
                break
            elif count >= 3:
                print print_str % count + ', 停止等待'
                raise NotImplementedError('贷款未能已发布,')
            else:
                print print_str % count
                time.sleep(times)

    @keyword('Sell Lender Credit Assignment')
    def sell_lender_credit_assignment(self, user_phone=None, password=None,
                                      amount=None, loan_id=None):
        """
        贷款状态必须是已发布
        """
        user_phone = user_phone or self.lender_user_phone
        password = password or self.lender_password
        loan_id = self._loan_id_handler(loan_id)
        self.wait_for_loan_status(loan_id)

        self.main_lender.login(self.env, user_phone, password)
        amount = amount or self.main_lender.get_single_loan(loan_id).amount
        self.main_lender.sell_lender_credit_assignment(loan_id, amount)
        self.main_lender.logout()

    @keyword('Buy_Lender Credit Assignment')
    def buy_lender_credit_assignment(self, loan_id=None, *args, **kwargs):
        """固定v lender来购买
        贷款状态必须是已转让
        """
        loan_id = self._loan_id_handler(loan_id)
        self.main_lender.login(self.env, 15886200179, 'dai123456')
        self.main_lender.buy_lender_credit_assignment(loan_id, *args, **kwargs)
        self.main_lender.logout()

    @keyword('Refund Loan Prepare')
    def refund_loan_prepare(self, loan_id=None):
        """还款数据准备
        """
        loan_id = self._loan_id_handler(loan_id)
        self.wait_for_loan_status(loan_id)
        self.sl_db.update_lpay_to_today_by_loan_id_and_status(loan_id)
        self.sl_db.update_entity_prop_nval_by_loan_id_and_status(loan_id)

    @keyword('Overdue Loan Prepare')
    def overdue_loan_prepare(self, loan_id=None):
        """逾期数据准备
        """
        loan_id = self._loan_id_handler(loan_id)
        self.wait_for_loan_status(loan_id)
        self.sl_db.update_lpay_to_today_by_loan_id_and_status(loan_id,
                                                              timedelta_days=40)
        self.sl_db.update_entity_prop_nval_by_loan_id_and_status(loan_id,
                                                                 timedelta_days=100)

    def run(self):
        pass


if __name__ == '__main__':
    l = LoanDataManagementController()
    # 设置环境------
    # l.set_environment_args('TRUST')
    l.set_environment_args('demo')
    # l.set_environment_args('dev')
    # l.set_environment_args('stage')
    # ----------创建web贷款-流程--------
    l.create_borrower_account("MCA")
    # l.create_borrower_account("BD_HOUSE_AP")
    # l.create_borrower_account("PROPERTY_OWNER")
    # l.create_borrower_account("DOWN_PAYMENT")
    # l.create_borrower_account("OUTSTANDING")
    # l.create_borrower_account("PAYROLL")
    # l.create_borrower_account("PRIVATE_OWNER")
    # l.create_borrower_account("SMB")
    # l.create_borrower_account("DOUBLE_FUND", 'sales.SH.test3')
    # 设置loan app的参数---------
    # l.set_loan_app_func_kwargs('update_borrower_employment_info', companySize='CHINA_500')
    # l.set_loan_app_func_kwargs('update_borrower_personal_info', childrenStatus='TWO_OR_ABOVE')
    # l.update_loan_app(False)
    l.update_loan_app()
    # 审批拒绝--------
    # time.sleep(2)
    # l.loan_approval_to_status_reject()
    # l.loan_approval_to_status_cancel()
    # 审批通过--------
    l.loan_approval_to_status_pre_review()
    # l.loan_approval_to_status_pre_review(model='db')
    l.loan_approval_to_status_review()
    l.loan_approval_to_status_investment()
    # lender投资--------
    # l.new_lender_invest(loan_id=loan_id)
    # l.new_lender_invest()
    # 多lender投资---------
    # user_phone_list = [13849477357, 18195561415]
    # l.multiple_lender_invest(user_phone_list)
    # 投资审批-------
    # l.lender_invest_approval()
    # 设置代扣------
    # l.borrower_account_binding_approval()
    # 跑贷款发布job------
    # l.loan_to_status_upcoming_publish()
    # l.loan_to_status_publish()
    # 债权转让-----
    # l.sell_lender_credit_assignment()
    # l.buy_lender_credit_assignment()
    # 还款准备------
    # l.refund_loan_prepare()
    # 设置逾期------
    # l.overdue_loan_prepare()
    # *********************************************
    # --------创建手机贷款-流程----------
    # l.create_borrower_by_mobile("PROPERTY_OWNER")
    # l.create_borrower_by_mobile("OUTSTANDING")
    # l.create_borrower_by_mobile("DOUBLE_FUND")
    # l.lms_ops_handle()
    # l.lms_ops_handle(271866, 11418845)
    # 审批拒绝--------
    # time.sleep(2)
    # l.loan_approval_to_status_reject()
    # l.loan_approval_to_status_cancel()
    # 审批贷款--------
    # loan_id = 3903787
    # l.loan_approval_to_status_pre_review(loan_id=loan_id, aid=14756170, model='db')
    # l.loan_approval_to_status_review(loan_id=loan_id)
    # l.loan_approval_to_status_investment(loan_id=loan_id)
    # 开始投资--------
    # l.new_lender_invest(loan_id=loan_id)
    # l.new_lender_invest()
    # user_phone_list = [13849477357, 18195561415]
    # l.multiple_lender_invest(user_phone_list)
    # l.multiple_lender_invest(loan_id=loan_id)
    # 投资审批--------
    # l.lender_invest_approval(loan_id=loan_id)
    # l.lender_invest_approval()
    # 设置代扣--------
    # l.borrower_account_binding_approval()
    # l.borrower_account_binding_approval(loan_id=loan_id)
    # 跑贷款发布job--------
    # l.loan_to_status_upcoming_publish()
    # l.loan_to_status_publish()
    # 债权转让--------
    # l.sell_lender_credit_assignment()
    # l.buy_lender_credit_assignment()
    # 还款准备--------
    # l.refund_loan_prepare()
    # 设置逾期--------
    # l.overdue_loan_prepare()
