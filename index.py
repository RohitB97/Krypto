from krypto.voice_recognition import voice_recognition 

import speech_recognition as sr

import logging

import time

logger = logging.getLogger(__name__)

def main(flag):
	r = sr.Recognizer()
	m = sr.Microphone()
	with m as source:
		logger.warn("Welcome to Crypto\n")
		while flag:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)

			try:
				result = r.recognize_google(audio)
				flag = voice_recognition().action(result);
			except sr.UnknownValueError:
				pass
			except sr.RequestError as e:
				logger.warn("Could not request results from Google Speech Recognition service: %s", e)
			except Exception as e:
				logger.error("Could not process text: %s", e)
flag = True

main(flag)
