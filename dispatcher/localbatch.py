import abstract
import subprocess


class LocalBatch(abstract.DispatcherBase):
    def __init__(self):
        abstract.DispatcherBase.__init__(self)
