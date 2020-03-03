from subprocess import call
# import winsound
def siren():
    filename = 'weewoo.wav'
    call(["aplay", filename])
    #winsound.PlaySound(filename, winsound.SND_FILENAME)