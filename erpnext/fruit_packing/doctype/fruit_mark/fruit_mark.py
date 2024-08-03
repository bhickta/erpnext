# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FruitMark(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.core.doctype.dynamic_link.dynamic_link import DynamicLink
		from frappe.types import DF

		links: DF.Table[DynamicLink]
		mark_name: DF.Data
	# end: auto-generated types
	pass

def get_fruit_mark_display_list(doctype: str, name: str) -> list[dict]:

	fruit_mark_list = frappe.get_list(
		"Fruit Mark",
		filters=[
			["Dynamic Link", "link_doctype", "=", doctype],
			["Dynamic Link", "link_name", "=", name],
			["Dynamic Link", "parenttype", "=", "Fruit Mark"],
		],
		fields=["*"],
	)
	for a in fruit_mark_list:
		a["display"] = get_fruit_mark_display(a)

	return fruit_mark_list

def get_fruit_mark_display(fruit_mark):
	return f"{fruit_mark.name}"