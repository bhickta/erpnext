frappe.listview_settings['My Doctype'] = {
    add_fields: ["tenant"], 
    onload: function(listview) {
        listview.page.add_menu_item(__('Set All to Public'), function() {
            frappe.confirm(
                __('Are you sure you want to set all documents to Public?'),
                function() {
                    setVisibility('Public');
                }
            );
        });

        listview.page.add_menu_item(__('Set All to Private'), function() {
            frappe.confirm(
                __('Are you sure you want to set all documents to Private?'),
                function() {
                    setVisibility('Private');
                }
            );
        });

        function setVisibility(visibility) {
            var action = 'my_custom_app.my_custom_app.doctype.my_doctype.my_doctype.set_doctype_visibility';
            frappe.call({
                method: action,
                args: {
                    doctype: 'My Doctype',
                    visibility: visibility
                },
                callback: function(response) {
                    if (response.message) {
                        listview.refresh();
                    }
                }
            });
        }
    }
};