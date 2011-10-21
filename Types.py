def enum(**enums):
	return type('Enum', (), enums)
	
Types = enum(
	VERIFYHANDLER = 1,
	MESSAGEHANDLER = 2
)