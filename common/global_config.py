# -*- coding: utf-8 -*-
class Global:
    SESSION = {"current_domain_name": ""}
    COOKIES = {"cookies": None}
    DEBUG_LOGGER_ENABLE = True
    LOAN_APP_TOKEN_DEV = 'Bearer ZWQ2ZTViOThlN2NmNGI3MWIwNGE0M2IyNzRkMWZiYzk'
    LOAN_APP_TOKEN_DEMO = 'Bearer MzIxNDVjYThiZmQ1NDk0MTk2ZTkwMmY0ZDY0MGY4MTA'

    class Environment:
        DIANRONG_DEMO = 'www-demo.dianrong.com'
        DIANRONG_DEMO_CRC = 'crc-demo.dianrong.com'
        DIANRONG_STAGE = 'www.stage.dianrong.com'
        DIANRONG_VIP = 'www-vip.dianrong.com'
        DIANRONG_TRUST = 'www-trust.dianrong.com'
        DIANRONG_DEV = 'www-dev.dianrong.com'
        DIANRONG_TECHOPS = 'ops-demo.dianrong.com'
        DIANRONG_MOBILE = '10.9.14.9:3000'
        DIANRONG_GM_DEV = 'loanapp-dev.dianrong.com'
        DIANRONG_LOAN_APP_DEV = 'loanapp-dev.dianrong.com'
        DIANRONG_LOAN_APP_DEMO = 'loanapp-demo.dianrong.com'
        DIANRONG_LOAN_APP_DEMO_INTERNAL_API = 'loanapp-demo.sl.com'
        DIANRONG_LOAN_APP_DEV_INTERNAL_API = 'loanapp-dev.sl.com'
        HUXIN_XJB_UAT = '10.199.101.211:18088'
        HUXIN_CMS_UAT = '10.199.101.217:8091'
        HUXIN_CMS_CI = '10.199.111.24:8080'

    class PageTimeout:
        URL_JUMPING = 3
        ELEMENT_FINDING = 30
        QUICK_IGNORE = 15
        LOADING_CONDITION_IGNORE = 1
        RETRY_INTERVAL = 3
        MEDIA_HOTPOINT_INTERVAL = 240
        CHECKPOINT_INTERVAL = 5
        STABILITY_INTERVAL = 5
        TECH_CHECK_IDENTIFY = 5
        DEEP_LINKING = 60
        CHECK_STATUS = 60

    class RetryTimes:
        MIN = 2
        MEDIUM = 5
        MAX = 25
        GET_JOB_STATUS = 30

    class DBConnect:
        class UatSwgMySqlDB:
            ENGINE_URL_PATTERN = "mysql+pymysql://%s:%s@%s/%s?charset=utf8"
            DB_CONNECT_INFO = {
                "supergw_uat": (
                "dbexecute", "dbexecute321", "10.199.101.18:3306", "supergw_uat")
            }

        class UatCifMySqlDB:
            ENGINE_URL_PATTERN = "mysql+pymysql://%s:%s@%s/%s?charset=utf8"
            DB_CONNECT_INFO = {
                "cif_uat": (
                "dbexecute", "dbexecute321", "10.199.101.18:3306", "cif_uat")
            }

        class PerfSwgMySqlDB:
            ENGINE_URL_PATTERN = "mysql+pymysql://%s:%s@%s/%s?charset=utf8"
            DB_CONNECT_INFO = {
                "spw": (
                    "spw", "Tiger!$456", "10.199.111.1:3306", "spw")
            }

        class PerfCifMySqlDB:
            ENGINE_URL_PATTERN = "mysql+pymysql://%s:%s@%s/%s?charset=utf8"
            DB_CONNECT_INFO = {
                "cif": (
                    "cif", "Tiger!$456", "10.199.111.1:3306", "cif")
            }

    class ServiceApiEnvironment:
        INFO = {"demo": "10.18.19.28:18085",
                "vip": "10.18.19.28:18085"
                }

    class WebElementStatus:
        REG_DISABLED = r'ets-disabled|ets-broken'
        REG_ACTIVE = r'ets-active'
        REG_LOCKED = r'ets-locked'
        REG_PASSED = r'ets-ui-acc-act-nav-passed|ets-passed'
        REG_EXPANDED = r'ets-expanded'
        REG_SELECT_MODE = r'ets-select-mode'

    class Messages:
        ERROR_MESSAGE_EXCEPTION_HAPPENS = "[Checkpoint #%s] Exception happens during checking. Detail error info: [%s]"

    class Patterns:
        class UrlPatterns:
            DIANRONG_SERVICE_MAIN_URL_PATTERN = "https://%s/mobile"
            DIANRONG_NEW_SERVICE_MAIN_URL_PATTERN = "https://%s/api/v2"
            DIANRONG_WORKFLOW_SERVICE_MAIN_URL_PATTERN = "https://%s/workflowApi"
            DIANRONG_WORKFLOW_SERVICE_MOBILE_URL_PATTERN = "http://%s/workflowApi"
            DIANRONG_WORKFLOW_BORROWER_LOGIN_SERVICE_URL_PATTERN = "https://%s/workflowApi/loginBorrower"
            LOGIN_SERVICE_URL_PATTERN = "https://%s/api/v2/users/login"
            DIANRONG_BORROWER_MAIN_PAGE_URL = "https://%s/new-borrower"
            DIANRONG_TECHOPS_URL_PATTERN = "https://%s/techops"
            DIANRONG_GM_URL_PATTERN = "https://%s/v1"
            DIANRONG_API_V2_URL_PATTERN = "http://%s/api/v2"
            DIANRONG_WORKFLOW_PAGE_URL = "https://%s/workflow"

        class RegExpPatterns:
            ATTRIBUTE_VALUE_TRIM_PATTERN = r'^\D*(!|:|;)'

        class Context:
            CONTEXT_QUERY_STRING_PATTERN = "c=countrycode=%s|culturecode=%s|partnercode=%s|siteversion=%s"

    class PageLoadingConditons:
        # where all loading conditions are defined
        conditions = ('loading_icon', 'loading_backdrop', 'asr_loading_icon', 'question_counter_icon')

    class HeaderContentType:
        FORM = "application/x-www-form-urlencoded; charset=UTF-8"
        JSON = "application/json; charset=utf-8"
        HEADERS_DEVICES_ID = u"CjBu3oW19FnKC9WpvguIqQ"

    class PageOperationInterval:
        MIN = 0.25
        MEDIUM = 1.5
        MAX = 3

    class PageOperationTimeout:
        MIN = 1
        MEDIUM = 1.5


DOMAIN_NAME_DICT = {
    'demo': Global.Environment.DIANRONG_DEMO
}
