
// a floating window which shows the deliveries and 
// facilitates creating / updating them


Ext.define('Ext.PlannedPayloadListPanel',{
    extends: 'Ext.grid.Panel',
    title: 'Need Transport',
    store: Ext.app.planned_payload_handler,
    columns: [
        {   text: 'Location',
            sortable: true,
            dataIndex: 'loc'
        },
        {   xtype: 'actioncolumn',
            width: 50,
            items: [
                {   icon: '/img/remove_delivery_column.png',
                    tooltip: 'Perminantly Remove this Delivery',
                    handler: function(grid, row, col) {
                        var r = grid.store.getAt(row);
                        r.destroy();
                    }
                }
            ]
        }
    ],
    listeners: {
        // clicking an item in the grid is the same as clicking
        // the marker for an item
        itemclick: function(grid, r) {
            r.handle_marker_click();
        }
    }
});

Ext.define('Ext.PayloadListPanel',{
    extends: 'Ext.grid.Panel',
    title: 'Have Transport',
    store: Ext.app.payload_handler,
    columns: [
        {   text: 'Location',
            sortable: true,
            dataIndex: 'loc'
        },
        {   text: 'Status',
            sortable: true,
            dataIndex: 'delivered_at',
            rendered: function(v) {
                if(!Ext.isEmpty(v)) {
                    return 'On Route'
                }
                return 'Delivered'
            }
        },
        {   xtype: 'actioncolumn',
            width: 50,
            items: [
                {   icon: '/img/remove_delivery_column.png',
                    tooltip: 'Perminantly Remove this Delivery',
                    handler: function(grid, row, col) {
                        var r = grid.store.getAt(row);
                        r.destroy();
                    }
                }
            ]
        }
    ],
    listeners: {
        // clicking an item in the grid is the same as clicking
        // the marker for an item
        itemclick: function(grid, r) {
            r.handle_marker_click();
        }
    }
});


Ext.define('Ext.DeliveryListWindow',{

    // we are a window
    extends: 'Ext.window.Window',

    title: 'Deliveries',

    // shows / hides the deliveiry window
    toggle: function() {
        // hide ? show ? we'll see
        this.setVisible(!this.isVisible());
    },

    constructor: function(config) {
        // create our default panel to show, the delivery view
        this.payload_list_panel = new Ext.PayloadListPanel();
        this.planned_payload_list_panel = new Ext.PlannedPayloadListPanel();

        // create our tab panel
        this.tabs = new Ext.tab.Panel({
            items: [ this.payload_list_panel, this.planned_paload_list_panel ]
        });

        // add our items to the config
        config.items = config.items.merge([
            {   xtype:'tabpanel',
                items: [ this.tabs ]
            }
        ]);

        // add our buttons
        config.buttons = config.buttons.merge([
            {   text: 'Add Payload',
                handler: this.add_planned_payload
            }
        ]);

        // throw it upstairs
        this.callSuper(config);
    },

    add_planned_payload: function() {
        // we are going to add a form panel to the tab panel
        // for a planned payload
        var panel = new Ext.form.Panel({
            title: 'Adding New Payload',
            items: [
                Ext.PlannedPayload.form_items       
            ],
            buttons: [
                {   text: 'OK',
                    handler: function() {
                        // add a new planend payload from the data
                        var data = panel.getValues();
                        var model = Ext.app.planned_payload_handler.add(data);
                        // since it's new it's marker isn't there
                        model.add_marker();
                    },
                    scope:this
                },
                {   text: 'Cancel',
                    handler: this.destroy,
                    scope: panel
                }
            ]
        });

        // it it in
        this.tabs.add(panel);

        // focus the new panel
        this.tabs.setActive(panel);
    }
});
