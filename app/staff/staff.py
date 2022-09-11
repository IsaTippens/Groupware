from app.screen.titled_screen import TitledScreen
from app.staff.ticket_management import TicketManagementScreen
from app.staff.ticket_sales import TicketSales

from app.globals import State

class StaffScreen(TitledScreen):
	def __init__(self):
		super().__init__("Staff", "Section")
		self.screen_names = [
		"Ticket Management",
		"Theatre Summary",
		"Daily sales Summary"
		]
		self.screens = [TicketManagementScreen, None, TicketSales]

	def is_logged_in(self) -> bool:
		return State.get("IS_ADMIN_LOGIN", False)

	def admin_message(self) -> str:
		if (not self.is_logged_in()):
			return "Not signed in"
		return "Signed in"

	def admin_login(self) -> bool:
		passw = ""
		while True:
			passw = input("Enter admin code (type \"exit\" to exit): ")
			if passw == "exit":
				return False
			if passw != State.get("SECRET", None):
				print("Incorrect")
				continue
			print("Code accepted")
			break
		return True

	def goBack(self):
		"""
			If we navigate back to the previous screen

			Then admin should be logged out
		"""
		State["IS_ADMIN_LOGIN"] = False
		super().goBack()

	def start(self):
		super().start()
		# Check if user is logged in
		print(self.admin_message())
		if not self.is_logged_in():
			result = self.admin_login()
			if not result:
				return self.goBack()
			State["IS_ADMIN_LOGIN"] = True
		print()

		# Print Options
		print("Select an option")
		for idx, s in enumerate(self.screen_names):
			print(idx + 1,": ",s)

		# Get Input for option
		isValid = False
		num = 0
		while not isValid:
			num = input("Enter an option (Enter 0 to exit): ")
			if not num.isdigit():
				print("Enter only numbers")
				continue
			num = int(num)
			if num > len(self.screen_names) or num < 0:
				print("Enter a valid option")
				continue
			isValid = True
		if num == 0:
			return self.goBack()
		return self.navigate(self.screens[num - 1]())

