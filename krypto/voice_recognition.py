import speech_recognition as sr
import logging
import subprocess
from gtts import gTTS

logger = logging.getLogger(__name__)

class voice_recognition:

    # Built-in words
	def __init__(self):
		self.KRYPTO_COGNATES = ["crypto", "hey crypto", "hello crypto"]

		self.STOP_LISTENING_COGNATES = ["bye crypto", "stop listening", "shut down", "bye", "good bye"]

	# @classmethod
	def is_actionable_command(self, command):
		return any(cognate in command for cognate in self.KRYPTO_COGNATES)

	def perform_query(self,command):
		com, arg = command.split(" ")
		if(arg == "downloads"):
			subprocess.call(["nautilus","../Downloads"])

	# @classmethod
	def action(self, command):
		"""
		Handles a single text command.
		"""
		# Use lowercase for processing.
		command = command.lower()

		logger.warn("Received command: '%s'", command)
			# Determine if this is an actionable command.
		if any(cognate in command for cognate in self.STOP_LISTENING_COGNATES):
			logger.warn("Goodbye, enjoy your day")
			return False

		elif not self.is_actionable_command(command):
			self.perform_query(command)
			return True
		
		else:
			logger.warn("How can i assist you ?")
			return True