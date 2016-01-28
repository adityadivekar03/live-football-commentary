from gi.repository import Notify

def notifiersystem(last_comm):

	Notify.init("Football score")
	
	notification = Notify.Notification.new(last_comm)
	
	notification.show()

