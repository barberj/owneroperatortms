
// a floating window which shows the deliveries and 
// facilitates creating / updating them
//

Ext.define('Ext.DeliveryListPanel',{
    extends: 'Ext.grid.Panel',
    columns: [
        {   text: 'Location',
            sortable: true,
            dataIndex: 'loc'
        },
        {   text: 'Status',
            sortable: true,
            dataIndex: 'status'
        },
        {   xtype: 'actioncolumn',
            width:
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
    ]
});

Ext.define('Ext.DeliveryListWindow',{

    // we are a window
    extends: 'Ext.window.Window',

    // shows / hides the deliveiry window
    toggle: function() {
        // hide ? show ? we'll see
        this.setVisible(!this.isVisible());
    },
    constructor: function(config) {
        // create our default panel to show, the delivery view
        Ext.app.delivery_list_panel = new Ext.app.DeliveryListPanel();

        // add our items to the config
        config.items = Ext.Array.merge(config.items,[
            {   xtype:'tabpanel',
                items: [
                    delivery_list_panel,
                ]
            }
        ]);

        // throw it upstairs
        this.callSuper(config);
    }
});
