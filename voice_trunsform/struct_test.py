from wave import open
from struct import Struct
from math import floor

sampler_rate=11025
c_freq=100
e_freq=100
g_freq=100

"""对连续三角波函数进行离散取样"""
def tri(frequency, amplitude=0.3):
    """a continuous triangle wave"""
    wave_length = sampler_rate // frequency
    # range from -0.3 to 0.3
    def sampler(t):
        saw_wave = t / wave_length - floor(t / wave_length + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave

    return sampler

def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name="song.wav", seconds=2):
    """
    当输出持续2s的声音文件时，需要采样 2*sampler_rate=22250次
    """
    out = open(name, "wb")
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(sampler_rate)
    t = 0
    while t < seconds * sampler_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()


play(tri(e_freq))
# 这样输出的音频很难听，还需要对波形做一些调整。

def note(f, start, end, fade=.01):
    """Play f for a fixed duration."""

    def sampler(t):
        seconds = t / sampler_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)

    return sampler

play(note(tri(e_freq), 1, 1.5)) #在(1,1.5)之间播放E4调
# 输出一段马里奥前奏

def both(f, g):
    return lambda t: f(t) + g(t)

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1 / 8)
    z += 1 / 8
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(c, z, z + 1 / 8))
    z += 1 / 8
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(g, z, z + 1 / 4))
    z += 1 / 2
    song = both(song, note(low_g, z, z + 1 / 4))
    return song


def mario_at(octave):
    c = tri(octave * c_freq)
    e = tri(octave * e_freq)
    g = tri(octave * g_freq)
    low_g = tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)

play(both(mario_at(1), mario_at(1 / 2)))
