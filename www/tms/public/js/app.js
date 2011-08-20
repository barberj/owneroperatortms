
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




// handle the user clicking a marker
function handle_delivery_marker_click() {}
function handle_transporter_marker_click() {}


// zooms the view in on a specific lat / long
function zoom_on_location() {}


// requests data for the transporter store and
// throw down markers for all transporters
function show_transporters() {}

// remove the transporter markers and clear the store
function clear_transporters() {}

// brings up the transports summary info in a marker bubble
function show_transporters_bubble() {}

// associates a transporter to a delivery
function assign_transporter() {}

