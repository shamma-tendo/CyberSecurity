from collections import defaultdict
import time

class AnomalyDetector:
    def __init__(self):
        self.baseline = defaultdict(list)

    def record(self, user, action, timestamp=None):
        timestamp = timestamp or time.time()
        self.baseline[user].append((action, timestamp))

    def score_session(self, user, recent_actions, window=60):
        now = time.time()
        history = [a for a, t in self.baseline[user] if now - t < window]
        unusual = [a for a in recent_actions if history.count(a) == 0]
        score = len(unusual) / max(len(recent_actions), 1)
        return score  # closer to 1.0 = more anomalous

detector = AnomalyDetector()
detector.record("alice", "login")
detector.record("alice", "read_file")
score = detector.score_session("alice", ["login", "read_file", "delete_all_files"])
print(f"Anomaly score: {score:.2f}")
if score > 0.5:
    print("⚠️  Flag for review")
    