from socket import *


MAILSERVER = 'localhost'
SENDER_EMAIL = "user@localhost"
RECIPIENT_MAIL = 'recipient@localhost'
PORT = 2525
CRLF = '\r\n'
MSG_END = f'.{CRLF}'


def verifyResponse(response, successCode):
	if response[:3] != str(successCode):
		print(f'Something went wrong, this was the response: {response}')

def sendMessage(socket, messageString):
	socket.send(messageString.encode())
	print(f'C: {messageString}')


def recieveMessage(socket, successCode):
	response = socket.recv(1024).decode("utf-8")
	print(f'S: {response}')
	verifyResponse(response, successCode)


# Create socket called clientSocket and establish a TCP connection with mailserve

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((MAILSERVER, PORT))

#First message from server after connection
recieveMessage(clientSocket, 220)

#Client initiation (HELO)
HELO_COMMAND = f"HELO Aesthaltics{CRLF}"
sendMessage(clientSocket, HELO_COMMAND)
recieveMessage(clientSocket, 250)

#Mail transaction

# MAIL command
MAIL_COMMAND = f"MAIl FROM:<{SENDER_EMAIL}>{CRLF}"
sendMessage(clientSocket, MAIL_COMMAND)
recieveMessage(clientSocket, 250)

# RCPT command
RCPT_COMMAND = f'RCPT TO:<{RECIPIENT_MAIL}>{CRLF}'
sendMessage(clientSocket, RCPT_COMMAND)
recieveMessage(clientSocket, 250)

#DATA command
DATA_COMMAND = f'DATA {CRLF}'
sendMessage(clientSocket, DATA_COMMAND)
recieveMessage(clientSocket, 354)

#sending the message
DATA = f'I Love Computer Networks!{CRLF}'
MESSAGE = f'{DATA}{MSG_END}'
sendMessage(clientSocket, MESSAGE)
recieveMessage(clientSocket, 250)

# QUIT command
QUIT_COMMAND = f'QUIT{CRLF}'
sendMessage(clientSocket, QUIT_COMMAND)
recieveMessage(clientSocket, 221)


