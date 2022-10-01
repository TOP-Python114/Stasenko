from copy import *
from constants import *


class Note:
    """Музыкальная нота с возможностью копирования."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 accidental: Accidental = None,
                 duration: Duration = Duration.DOUBLE):
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        self.duration = duration

    def __str__(self):
        if self.accidental is None:
            return f'Продолжительность: {self.duration}, Высота: {self.pitch}, Октава: {self.octave}'
        else:
            return f'Продолжительность: {self.duration}, Высота: {self.pitch}, Октава: {self.octave}, Знак альтерации: {self.accidental}'

    def clone(self, **params):
        """Создаёт новый экземпляр ноты с теми же параметрами."""
        res = deepcopy(self)
        res.__dict__.update(params)
        return res


class ScoreNote(Note):
    """Изображение музыкальной ноты в партитуре."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 stiel: bool = False,
                 rib: bool = False,
                 accidental: Accidental = None,
                 duration: Duration = Duration.DOUBLE):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.stiel = stiel
        self.rib = rib

    def __str__(self):
        return super().__str__() + f', Флажок: {self.stiel}, Ребро: {self.rib}'


class MIDINote(Note):
    """Кодирование музыкальной ноты в MIDI протоколе."""
    def __init__(self,
                 *,
                 pitch: Pitch,
                 octave: Octave,
                 velocity: int,
                 accidental: Accidental = None,
                 duration: Duration = Duration.DOUBLE):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.velocity = velocity

    def __str__(self):
        return super().__str__() + f', Атака: {self.velocity}'



midi_gg = MIDINote(
    pitch=Pitch.G,
    octave=Octave.GREAT,
    velocity=80,
    duration=Duration.HALF,
    accidental=Accidental.SHARP
)
score_f4 = ScoreNote(
    pitch=Pitch.F,
    octave=Octave.LINE_4,
    stiel=True,
    duration=Duration.HALF
)

clone_midi = midi_gg.clone(pitch=Pitch.E, duration=Duration.EIGHTH, accidental=None)
clone_score = score_f4.clone(octave=Octave.LINE_5, beam=True)

print('Миди нота:')
print(midi_gg, '\n')
print('Клонированная миди нота с изменениями:')
print(clone_midi, '\n')
print('Нота в партитуре: ')
print(score_f4, '\n')
print('Клонированная нота в партитуре с изменениями:')
print(clone_score)


# stdout:
# Миди нота:
# Продолжительность: 2, Высота: 5, Октава: 1, Знак альтерации: sharp, Скорость: 80
#
# Клонированная миди нота с изменениями:
# Продолжительность: 8, Высота: 3, Октава: 1, Скорость: 80
#
# Нота в партитуре:
# Продолжительность: 2, Высота: 4, Октава: 6, Флажок: True, Ребро: False
#
# Клонированная нота в партитуре с изменениями:
# Продолжительность: 2, Высота: 4, Октава: 7, Флажок: True, Ребро: False
