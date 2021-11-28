from pylsl import StreamInfo, StreamOutlet


ROUND_BEGIN_TRIGGER = 100
ROUND_END_TRIGGER = 101

MISTAKE_TRIGGER = 404


class LslTriggers(object):
    """
    An interface to mark events to lsl stream
    """
    def __init__(self):
        self._outlet = StreamOutlet(StreamInfo("GameMarkers", "Markers"))

    def begin_round(self):
        self._outlet.push_sample([ROUND_BEGIN_TRIGGER])

    def end_round(self):
        self._outlet.push_sample([ROUND_END_TRIGGER])

    def mistake(self):
        self._outlet.push_sample([MISTAKE_TRIGGER])