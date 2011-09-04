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
    },
    get_pos: function() {
        return new google.maps.LatLng(this.get('lat'),
                                      this.get('long')),
    },
    add_marker: function() {
        // add a marker for each record at it's pos
        var marker = new google.maps.Marker({
            position: this.get_pos,
            map: map
        });

        // create a callback which wraps the scope
        var c = Ext.bind(this.handle_marker_click,
                         this);

        // add a click listener to the marker
        google.maps.event.addListener(marker, 'click', c);

        // save a ref to the marker
        this.marker = marker;

        return marker;
    },
    remove_marker: function() {
        // remove the marker
        this.marker.setVisible(false);
        // TODO: test if this actually removes the marker from map
        delete this.marker;
    },
    show_info: function() {
        var content = this.get_bubble_content();
        var info = new google.maps.infoWindow({
            content: content
        });
        // throw the infoWindow up
        infoWindow.open(map,this.marker);
    },
    get_bubble_content: function() {
        return ['CONTENT'];
    },
    handle_marker_click: function() {
        // default behavior is show info
        this.show_info();
    }

});

Ext.define('Transporter', {
    extends: 'BaseModel',
});

Ext.define('Payload', {
    extends: 'BaseModel',

    // when our marker is clicked we zoom in on
    // it and than show the transporters
    handle_marker_click: function(loc) {
        zoom_on_location(loc);
        transporter_handler.show_markers(loc);
    }
});

Ext.define('PlannedPayload', {
    extends: 'Payload'
});
