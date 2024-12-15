import libfilter

# This file generates a sine wave of a selected frequency, sample rate and duration and outputs it as S16LE to a file with a name supplied by the user

freq = float(input("Frequency>"))
sample_rate = float(input("Sample rate>"))
duration = float(input("Duration in seconds>"))
file_name = input("File name>")

sine = libfilter.Sine(freq, sample_rate)
samples = [sine.process() for _ in range(round(duration*sample_rate))]

pcm = libfilter.convert_to_s16le(samples)
with open(file_name, "wb") as f:
    f.write(pcm)