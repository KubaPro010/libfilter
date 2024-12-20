def convert_to_s8(audio_samples):
    """
    Convert a list of 2V peak-to-peak audio samples (float in range -1.0 to 1.0)
    to signed 8-bit little-endian format.

    :param audio_samples: List of audio samples in range -1.0 to 1.0
    :return: bytearray containing the audio samples in s16le format
    """
    s8_samples = bytearray()

    for sample in audio_samples:
        if not -1.0 <= sample <= 1.0:
            print(sample)
            raise ValueError("Audio sample must be in the range of -1.0 to 1.0")

        # Convert to signed 16-bit integer
        int_sample = int(sample * 127)

        # Pack into little-endian format
        s8_samples.append(int_sample)

    return s8_samples
def convert_from_s8(s8le_data):
    """
    Convert signed 8-bit little-endian audio data to a list of float audio samples
    in the range -1.0 to 1.0.

    :param s8le_data: bytearray containing audio samples in s16le format
    :return: List of audio samples in range -1.0 to 1.0
    """
    if len(s8le_data) % 1 != 0:
        raise ValueError("The length of the s16le data must be odd (2 bytes per sample).")

    audio_samples = []

    for i in range(0, len(s8le_data), 1):
        # Combine two bytes (little-endian) to form a signed 16-bit integer
        int_sample = s8le_data[i]

        # Handle negative values for 8-bit signed integers
        if int_sample >= 127:
            int_sample -= 255

        # Convert back to the range -1.0 to 1.0
        float_sample = int_sample / 127.0

        # Append the float sample to the list
        audio_samples.append(float_sample)

    return audio_samples
def convert_to_s16le(audio_samples):
    """
    Convert a list of 2V peak-to-peak audio samples (float in range -1.0 to 1.0)
    to signed 16-bit little-endian format.

    :param audio_samples: List of audio samples in range -1.0 to 1.0
    :return: bytearray containing the audio samples in s16le format
    """
    s16le_samples = bytearray()

    for sample in audio_samples:
        # Scale from -1.0 to 1.0 to -32768 to +32767
        if not -1.0 <= sample <= 1.0:
            print(audio_samples.index(sample), sample)
            raise ValueError("Audio sample must be in the range of -1.0 to 1.0")

        # Convert to signed 16-bit integer
        int_sample = int(sample * 32767)

        # Pack into little-endian format
        s16le_samples.append(int_sample & 0xFF)          # Low byte
        s16le_samples.append((int_sample >> 8) & 0xFF)  # High byte

    return s16le_samples
def convert_from_s16le(s16le_data):
    """
    Convert signed 16-bit little-endian audio data to a list of float audio samples
    in the range -1.0 to 1.0.

    :param s16le_data: bytearray containing audio samples in s16le format
    :return: List of audio samples in range -1.0 to 1.0
    """
    if len(s16le_data) % 2 != 0:
        raise ValueError("The length of the s16le data must be even (2 bytes per sample).")

    audio_samples = []

    for i in range(0, len(s16le_data), 2):
        # Combine two bytes (little-endian) to form a signed 16-bit integer
        int_sample = s16le_data[i] | (s16le_data[i + 1] << 8)

        # Handle negative values for 16-bit signed integers
        if int_sample >= 0x8000:
            int_sample -= 0x10000

        # Convert back to the range -1.0 to 1.0
        float_sample = int_sample / 32767.0

        # Append the float sample to the list
        audio_samples.append(float_sample)

    return audio_samples
def convert_to_s24le(audio_samples):
    """
    Convert a list of 2V peak-to-peak audio samples (float in range -1.0 to 1.0)
    to signed 24-bit little-endian format.

    :param audio_samples: List of audio samples in range -1.0 to 1.0
    :return: bytearray containing the audio samples in s24le format
    """
    s24le_samples = bytearray()

    for sample in audio_samples:
        # Scale from -1.0 to 1.0 to -32768 to +32767
        if not -1.0 <= sample <= 1.0:
            print(sample)
            raise ValueError("Audio sample must be in the range of -1.0 to 1.0")

        # Convert to signed 16-bit integer
        int_sample = int(sample * 524287)

        # Pack into little-endian format
        s24le_samples.append(int_sample & 0xFF)
        s24le_samples.append((int_sample >> 8) & 0xFF)
        s24le_samples.append((int_sample >> 16) & 0xFF)

    return s24le_samples
def convert_from_s24le(s24le_data):
    """
    Convert signed 16-bit little-endian audio data to a list of float audio samples
    in the range -1.0 to 1.0.

    :param s24le_data: bytearray containing audio samples in s16le format
    :return: List of audio samples in range -1.0 to 1.0
    """
    if len(s24le_data) % 3 != 0:
        raise ValueError("The length of the s24le data must be odd (3 bytes per sample).")

    audio_samples = []

    for i in range(0, len(s24le_data), 3):
        # Combine two bytes (little-endian) to form a signed 24-bit integer
        int_sample = s24le_data[i] | (s24le_data[i + 1] << 8) | (s24le_data[i + 2] << 16)

        # Handle negative values for 16-bit signed integers
        if int_sample >= 524288:
            int_sample -= 1048575

        # Convert back to the range -1.0 to 1.0
        float_sample = int_sample / 524287.0

        # Append the float sample to the list
        audio_samples.append(float_sample)

    return audio_samples