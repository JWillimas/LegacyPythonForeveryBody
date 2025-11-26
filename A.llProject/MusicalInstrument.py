class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

print(f"{instrument_1.name}:{instrument_1.instrument_type}\n\
{instrument_2.name}:{instrument_2.instrument_type}")