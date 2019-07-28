from restaurant_user import User
class Privileges():
	"""权限类"""
	def __init__(self):
		self.privilege="can ban user"
	def show_privileges(self):
			print("Privileges is "+self.privilege)
class Admin(User):
	 def __init__(self,f_n,l_n):
		 super().__init__(f_n,l_n)
		 self.privileges=Privileges()
