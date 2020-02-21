import winsound
def siren():
    filename = 'weewoo.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)