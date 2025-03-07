from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("pericles-melhor-eu-ir-91512ac5.mp3")
play(song)
