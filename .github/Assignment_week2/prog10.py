
class BugTracker:
    def __init__(self):
        self.bugs = {}

    def add_bug(self, bug_id, description, severity):
        self.bugs[bug_id] = {
            'description': description,
            'severity': severity,
            'status': 'Open'
        }

    def update_bug_status(self, bug_id, status):
        self.bugs[bug_id]['status'] = status
    
    def list_all_bugs(self):
        for bug_id, details in self.bugs.items():
            print(f"Bug ID: {bug_id}, Description: {details['description']}, Severity: {details['severity']}, Status: {details['status']}")

Tracker = BugTracker()
Tracker.add_bug(101, "Login button not working", "High")
Tracker.add_bug(102, "Page crashes on load", "Critical")
Tracker.add_bug(103, "Typo in footer", "Low")

Tracker.update_bug_status(101, "In Progress")

Tracker.list_all_bugs()