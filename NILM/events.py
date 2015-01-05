import pandas as pd
import detection


class Events(pd.DataFrame):

    detection_types = ['simple_edge', 'steady_states']

    def __init__(self, meter):
        super(Events, self).__init__()
        self._meter = meter

    @property
    def meter(self):
        return self._meter

    def detection(self, detection_type, *kargs):
        assert (detection_type in Events.detection_types)
        phases = self.meter.measurements.columns.levels[0]
        df = pd.DataFrame()
        for phase in phases:
            if detection_type == 'simple_edge':
                dff = detection.simple_edge(self.meter.measurements[phase],
                                            *kargs)
            elif detection_type == 'steady_states':
                dff = detection.steady_states(self.meter.measurements[phase],
                                              *kargs)
            else:
                raise NotImplementedError

            dff['phase'] = phase
            df = df.append(dff)

        super(Events, self).__init__(df)

if __name__ == '__main__':
    from tools import create_meter
    meter1 = create_meter()
    meter1.load_measurements(sampling_period=10)
    events = Events(meter1)
    events.detection('simple_edge')
