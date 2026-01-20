
class TestStatus:
    def __init__(self, Testcaseid, Status):
        self.Testcaseid = Testcaseid
        self.Status = Status
    
    def DisplayTestResults(self):
        print("Test Case ID:", self.Testcaseid)
        print("Status:", self.Status)

ts = TestStatus(1001, "Pass")
ts.DisplayTestResults()