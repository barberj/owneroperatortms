
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

Ext.onReady( function(){

    // set our context
    this.Ext.app = {};

    // create our map
    Ext.app.map = new google.maps.Map(document.getElementById('map'), {
        zoom: 3,
        center: new google.maps.LatLng(33.7477123,-84.376682),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    // instantiate our handleres
    this.transport_handler = new Ext.TransporterHandler();
    this.payload_handler = new Ext.PayloadHandler();
    this.planned_payload_handler = new Ext.PlannedPayloadHandler();

    // read our initial data for the payloads and put up markers
    this.planned_payload_handler.show_markers();
    this.payload_handler.show_markers();

    // create our delivery list handler
    this.payload_list_window = new Ext.PayloadListWindow();

    // setup the button
    Ext.get('toolbar').add(Ext.Button({
        text: 'Delivery List',
        handler: this.payload_list_window.toggle,
        scope: this.payload_list
    }));

});
