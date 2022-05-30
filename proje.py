def flatten(lst):
	if(lst==[]):
		return []
	if (type(lst[0])==list):
		return flatten(lst[0])+flatten(lst[1:])
	else:
		return [lst[0]]+flatten(lst[1:])

def reverse_list(lst):
	if(lst==[]):
		return []
	if(type(lst[0])==list):
		return reverse_list(lst[1:])+[reverse_list(lst[0])]
	else:
		return reverse_list(lst[1:])+[lst[0]]
