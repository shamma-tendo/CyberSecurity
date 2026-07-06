from collections import defaultdict
from datetime import datetime, timedelta

class CorrelationEngine:
    def __init__(self, correlation_window=300):  # 5 min window
        self.events = defaultdict(list)
        self.window = timedelta(seconds=correlation_window)

    def ingest(self, source_ip, event_type, timestamp):
        self.events[source_ip].append((event_type, timestamp))

    def detect_attack_chain(self, source_ip, required_sequence):
        """Detect if a sequence like ['port_scan', 'auth_fail', 'auth_success', 'data_transfer'] occurred"""
        events = sorted(self.events[source_ip], key=lambda x: x[1])
        seq_index = 0
        start_time = None

        for event_type, timestamp in events:
            if seq_index == 0 and event_type == required_sequence[0]:
                start_time = timestamp
                seq_index = 1
            elif seq_index > 0:
                if timestamp - start_time > self.window:
                    seq_index = 0
                    continue
                if event_type == required_sequence[seq_index]:
                    seq_index += 1
                    if seq_index == len(required_sequence):
                        return True, start_time, timestamp
        return False, None, None

engine = CorrelationEngine()
base = datetime.now()
engine.ingest("10.0.0.5", "port_scan", base)
engine.ingest("10.0.0.5", "auth_fail", base + timedelta(seconds=30))
engine.ingest("10.0.0.5", "auth_success", base + timedelta(seconds=60))
engine.ingest("10.0.0.5", "data_transfer", base + timedelta(seconds=90))

detected, start, end = engine.detect_attack_chain(
    "10.0.0.5",
    ["port_scan", "auth_fail", "auth_success", "data_transfer"]
)
if detected:
    print(f"⚠️  Attack chain detected! Duration: {end - start}")