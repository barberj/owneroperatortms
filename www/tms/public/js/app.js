
// goals: 
// Have initial map w/ all user's deliveries marked
// ability to add delieveries from panel
// ability to edit deliveries from panel
// clicking on a delivery marker brings up all 
//   the transporters w/in it's proximity
// clicking a delivery marker zooms the map in on marker
// no transporters are in view unless delivery is clicked
// list of deliveries in panel
// clicking an item in the delivery list is like clicking
//   delivery marker
// clicking transport brings up small summary bubble
//   w/ link to accept for delivery
// when view is zoomed out transports are cleared
// requests for transporter info can return channel token
//   as well.
//


// we'll have stores for:
//  transports
//  deliveries
// they will only hold summary / high lvl data
//   specific data will be pulled w/ ajax requests
Ext.define('BaseModel', {
    extends: 'Ext.data.Model',
    idProperty: 'id',
    fields: [ {name:'id',type:'int'} ],
    update: function(data) {
        // simple method to update the record
        for(k in data) {
            self.set(k,data[k]);
        }
    }
});
Ext.define('Transporter', {
    extends: 'BaseModel'
});
Ext.define('Broker', {
    extends: 'BaseModel'
});
Ext.define('Payload', {
    extends: 'BaseModel'
});
Ext.define('PlannedPayload', {
    extends: 'BaseModel'
});

ZOOM_IN_LVL = 4;

///// USER ACTION HANDLERS ///////////////////////////// 

// handle the user clicking a marker
// we receive a lat/long obj
function handle_delivery_marker_click(id,loc) {
    // zoom + center on location
    zoom_on_location(loc);

    // populate and show our transporters
    show_transporters(loc);
};

function handle_transporter_marker_click(id,loc) {
    // we want to show the bubble
    show_transporter_info(id,loc);
};

///// END USER ACTION HANDLERS ///////////////////////////// 
//

// zooms the view in on a specific lat / long
function zoom_on_location(loc) {
    // center the view over our location
    map.setCenter(loc);

    // zoom in
    map.setZoom(ZOOM_IN_LVL);
};

// these are shared functions for adata types that have markers
// and event handlers

// show
//  add_markers
//  add_marker
// show_info
// update_data
// clear
// handle marker click

var DataHandler = function(type) {
    this.type = type;
};
DataHandler.prototype = {
    // refreshes the data, adds the markers
    show: function() {
        this.refresh_data( this.add_markers );
    },
    add_markers: function() {
        // get the type's store
        var store = this.get_store();
        // add a marker for each record
        store.each(function(record) {
            var loc = position: new google.maps.LatLng(record.get('lat'),
                                                       record.get('long'))
            // add our marker
            var marker = this.add_marker(loc,store.get('id'));
            
            // add the marker ref to our record
            record.marker = marker;
        });
    },
    add_marker: function(loc,record) {
        // add a marker for each record at it's pos
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(record.get('lat'),
                                             record.get('long')),
            map: map
        });

        // create a callback which wraps in the location and id info
        var c = Ext.bind(this.show_info,
                         this,
                         [id,loc]) // override, not append

        // add a click listener to the marker
        google.maps.event.addListener(marker, 'click', c);

        return marker;
        
    },
    handle_marker_click: function(id,loc) {
        
    },
    show_info: function(id) {
        // get our record so we can grab the marker / content
        var store = this.get_store();
        var record = store.getById(id);
        var info = new google.maps.infoWindow({
            // TODO: add content
            content: ['content TODO']
        });
        // throw the infoWindow up
        infoWindow.open(map,record.marker);
    },
    refresh_data: function(callback) {
        // reload the store's data
        this.get_store().load({
            callback:callback,
            scope:this
        });
    },
    clear: function() {
        var store = this.get_store();
        store.each(function(record) {
            // remove the marker
            record.marker.setVisible(false);
            // TODO: test if this actually removes the marker from map
            delete record.marker;
        });
        // clear our the store's data
        store.removeAll();
    },
    get_store() {
        return Ext.data.StoreManager.lookup(this.type);
    }
};



