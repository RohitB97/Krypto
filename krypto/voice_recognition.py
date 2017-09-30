import speech_recognition as sr
import logging

logger = logging.getLogger(__name__)

class voice_recognition:

    # Built-in words
	def __init__(self):
		self.KRYPTO_COGNATES = ["crypto", "hey crypto", "hello crypto"]

		self.STOP_LISTENING_COGNATES = ["go away", "stop listening", "shut down", "bye", "good bye"]

	# @classmethod
	def is_actionable_command(self, command):
		return any(cognate in command for cognate in self.KRYPTO_COGNATES)

	# @classmethod
	def action(self, command):
		"""
		Handles a single text command.
		"""
		# Use lowercase for processing.
		command = command.lower()

		logger.warn("Received command: '%s'", command)
			# Determine if this is an actionable command.
		if not self.is_actionable_command(command):
			logger.warn("Please go on")

		if any(cognate in command for cognate in self.STOP_LISTENING_COGNATES):
			logger.warn("Thank you, enjoy your day, sir.")
		else:
			logger.warn("How can i assist you further")