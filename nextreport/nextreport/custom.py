import frappe

def after_install():

    css =""".textcenter{
    text-align:center;
}
.borderclass{
    border-bottom: 1px solid dodgerblue;
}
table {
    width:100%;
    text-align:left;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid dodgerblue;
    font-size:10px;
}

.print-format{
    padding: 12px !important;
    margin-bottom: 0px;
    margin-top:0px;
}"""
    style = frappe.new_doc("Print Style")
    style.print_style_name = "custom"
    style.css= css
    style.insert(ignore_permissions=True)
def before_uninstall():
    frappe.delete_doc("Print Style", "custom")