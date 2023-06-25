# Copyright (c) 2023, eknath and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Employee1(Document):
	def before_save(self):
		doc = frappe.get_doc("Employee1",self.first_name)
		print("111111111111111111",doc)
