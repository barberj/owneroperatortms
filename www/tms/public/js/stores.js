var proxy_config = {
    type: 'rest',
    url: '',
    reader: {
        type: 'json',
        root: 'data'
    }
};

Ext.define('Ext.BaseStore',
    override: 'Ext.data.Store',
    model: 'Ext.BaseModel',
    proxy: proxy_config,
    autoLoad: false
});

Ext.define('Ext.BaseHandler', {
    override: 'Ext.BaseStore',

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
            params: loc.toQueryString()
        });
    },

    destroy: function(config) {
        // before we let them destroy, confirm
        if(!config.confirmed) {
            var r = this;
            Ext.window.MessageBox.confirm(
                'Confirm Delete',
                'Are you sure you would like to perminantely delete '+
                'his record?',
                function(answer) {
                    // TODO figure out what a yes returns
                    if(answer == 'true') {
                        // recall destroy w/ a true for confirmed
                        r.destroy(config.merge({confirmed:true}));
                    }
                }, this
            );
        }

        // if we've confirmed than we'll delete
        else {
            this.callSuper(config);
        }
    }
});


// DEFINE and INSTANTIATE our HANDLERS
Ext.define('Ext.TransporterHandler', {
    override:'Ext.BaseHandler',
    proxy: proxy_config.merge({
        url:'./transporters',
    })
});


Ext.define('Ext.PayloadHandler', {
    override:'Ext.BaseHandler',
    proxy: proxy_config.merge({
        url:'./payloads',
    })
});


Ext.define('Ext.PlannedPayloadHandler', {
    override:'Ext.BaseHandler',
    proxy: proxy_config.merge({
        url:'./plannedpayloads',
    })
});

