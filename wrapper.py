from espeak import espeak

espeak.set_voice("en")

espeak.synth("hey there how are you")

while espeak.is_playing:
	pass