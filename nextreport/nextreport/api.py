import frappe

@frappe.whitelist()
def get_customer():
    doc = frappe.db.get_all("Customer",{"docstatus":0},["customer_name","customer_type"])
    return doc
@frappe.whitelist()
def post_customer(middle_name,first_name,last_name,gender):
    doc = frappe.new_doc("Employee1")
    doc.middle_name = middle_name
    doc.first_name = first_name
    doc.last_name = last_name
    doc.gender = gender
    doc.save()
    return doc.as_dict()

@frappe.whitelist()
def put_customer(first_name,gender):
    doc = frappe.get_doc("Employee1",first_name)
    doc.gender = gender
    doc.save()
    return doc.as_dict()

@frappe.whitelist()
def delete_customer(first_name):
    doc = frappe.delete_doc("Employee1",first_name)

@frappe.whitelist()
def get_salary():
    doc = frappe.db.get_all("Salary Slip",{"docstatus":0},['*'])
    
    return doc