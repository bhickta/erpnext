import frappe


docs = []

from .inventory_dimensions import get_docs as _get_inventory_dimension_docs
docs.extend(_get_inventory_dimension_docs())

def execute():
    for doc in docs:
        try:
            frappe.get_doc(doc['doctype'], doc['name'])
        except frappe.DoesNotExistError as e:
            frappe.get_doc(doc).insert(ignore_permissions=True)

