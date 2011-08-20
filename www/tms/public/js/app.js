
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


// zooms the view in on a specific lat / long
function zoom_on_location(loc) {
    // center the view over our location
    map.setCenter(loc);

    // zoom in
    map.setZoom(ZOOM_IN_LVL);
};

// shows the bubble over the transporter marker
function show_transporter_info(id,loc) {
    // get our record so we can grab the marker / content
    var store = Ext.data.StoreManager.lookup('Transporter');
    var record = store.getById(id);
    var info = new google.maps.infoWindow({
        // TODO: add content
        content: ['content TODO']
    });
    // throw the infoWindow up
    infoWindow.open(map,record.marker);
};

// requests data for the transporter store and
// throw down markers for all transporters
function show_transporters(loc) {
    // first we need to get the transporter info
    // for this location
    get_transporter_data(loc, add_transport_markers);
};

// populate the transporter data
function get_transporter_data(loc, callback) {
    // populate the store
    var store = Ext.data.StoreManager.lookup('Transporter');
    // load the store, giving the loc param string rep or loc
    store.load({
        loc: loc.toString(),
        callback: callback
    });
};

// using the store, add markers for all transporters
function add_transporter_markers() {
    var store = Ext.data.StoreManager.lookup('Transporter');
    store.each(function(record) {
        var loc = position: new google.maps.LatLng(record.get('lat'),
                                                   record.get('long'))
        // add our marker
        var marker = add_transporter_marker(loc,store.get('id'));
        
        // add the marker ref to our record
        record.marker = marker;
    });
};

// adds a marker for transporter at given loc
function add_transporter_marker(loc,id) {
    // add a marker for each record at it's pos
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(record.get('lat'),
                                         record.get('long')),
        map: map
    });

    // create a callback which wraps in the location and id info
    var c = Ext.bind(handle_transporter_marker_click,
                     undefined, // scope = window
                     [id,loc]) // override, not append

    // add a click listener to the marker
    google.maps.event.addListener(marker, 'click', c);

    return marker;
};

// remove the transporter markers and clear the store
function clear_transporters() {}

// brings up the transports summary info in a marker bubble
function show_transporters_bubble() {}

// associates a transporter to a delivery
function assign_transporter() {}

