var proxy_config = {
    type: 'ajax',
    url: '',
    reader: {
        type: 'json',
        root: 'data'
    }
};
var BaseStore = new Ext.data.Store({
    model: 'BaseModel',
    proxy: proxy_config,
    autoLoad: false
});

Ext.define('BaseHandler', {
    override: 'BaseStore',

    // refresh data and put up markers
    show_markers: function(loc) {
        // remove the newly outdated data
        this.clear_markers();
        // update our data and show the markers
        this.refresh_data( loc, this.add_markers );
    },

    // add a maker to the map for each record
    add_markers: function() {
        // get the types store
        var store = this.get_store();
        // add a marker for each record
        store.each(function(record) {
            // add our marker
            var marker = record.add_marker();
        });
    },

    // remove all the markers
    clear_markers: function() {
        var store = this.get_store();
        store.each(function(record) {
            record.remove_marker();
        });
        // clear our the stores data
        store.removeAll();
    }

    refresh_data: function(loc, callback) {
        // reload the stores data
        this.load({
            callback:callback,
            scope:this,
            // TODO: specify loc params
        });
    }
});


// DEFINE and INSTANTIATE our HANDLERS
Ext.define('TransporterHandler', {
    override:'BaseHandler'
});

transport_handler = new TransporterHandler();

Ext.define('PayloadHandler', {
    override:'BaseHandler',
    proxy: proxy_config.merge({
        url:'./payloads/list',
    })
});

payload_handler = new PayloadHandler();

Ext.define('PlannedPayloadHandler', {
    override:'BaseHandler',
    proxy: proxy_config.merge({

    })
});

planned_payload_handler = new PlannedPayloadHandler();