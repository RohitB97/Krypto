from krypto.voice_recognition import voice_recognition 

import speech_recognition as sr

import logging

logger = logging.getLogger(__name__)

def main():
	r = sr.Recognizer()
	print("test2")
	m = sr.Microphone()
	print("test1")
	with m as source:
		while True:
			r.adjust_for_ambient_noise(source)
			logger.warn("Hey there! This is Krypto\nHow do i assist you")
			audio = r.listen(source)

			logger.warn("Processing text")

			try:
				result = r.recognize_google(audio)
				logger.warn("Done processing")
				voice_recognition().action(result);
			except sr.UnknownValueError:
				logger.warn("Sphinx could not understand audio")
			except sr.RequestError as e:
				logger.warn("Could not request results from Google Speech Recognition service: %s", e)
			except Exception as e:
				logger.error("Could not process text: %s", e)

main()
