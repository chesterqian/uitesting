import re


class MonkeyTestOracle(object):

    def __init__(self, file_path, should_be=True):
        self.file_path = file_path
        self.should_be = should_be
        self._is_crashed = None

    @property    
    def is_crashed(self):
        if self._is_crashed == None:

            r = None

            with open(self.file_path) as f:
                file_content = f.read()
                r = re.search(r'// CRASH', file_content) and True or False

            self._is_crashed = r

            return r

        return self._is_crashed

    @property
    def is_passed(self):
        try:
            if self.should_be:
                return not self.is_crashed
            else:
                return self.is_crashed
        finally:
            self._is_crashed = None
    

if __name__ == '__main__':
    path = '/Users/linkinpark/jenkins_workspace/workspace/xjb_android_monkey_test/monkey_test_result.txt'
    m = MonkeyTestOracle(path, True)
    print m.is_passed
    print m._is_crashed