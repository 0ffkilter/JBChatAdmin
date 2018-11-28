from modules.permissions import *

def add_user(args, perms=[]):
	user_id = args[0]
	thread_id = args[1]

	if thread_id == "this":
		thread_id = perms[MESSAGE_THREADID]
	if user_id == "me":
		user_id = perms[MESSAGE_AUTHOR]

	perms[FN_ADDUSER](user_id, thread_id)

	name = perms[FN_GET_NAME](user_id)

	if thread_id != "this":
		return "Added to group. Contact thread owner if you're not in the group"
	else:
		return "Welcome " + name + " to the group!"
