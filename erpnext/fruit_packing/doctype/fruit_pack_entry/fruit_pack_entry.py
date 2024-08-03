# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FruitPackEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.fruit_packing.doctype.fruit_pack_entry_detail.fruit_pack_entry_detail import FruitPackEntryDetail
		from frappe.types import DF

		amended_from: DF.Link | None
		customer_name: DF.Data
		fruit: DF.Link
		items: DF.Table[FruitPackEntryDetail]
		posting_datetime: DF.Datetime
	# end: auto-generated types
	pass
