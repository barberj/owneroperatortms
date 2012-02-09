Ext.require(['Ext.container.Viewport', 
             'Ext.ux.GMapPanel']);
Ext.application({
    name: 'TenTwenty'
    ,launch: function() {
        Ext.create('Ext.container.Viewport', {
            items: [{
                region: 'north'
                ,title: 'Account'
                ,html: '<h1 class="x-panel-header">Account Stuff</h1>'
                ,titleCollapse: true
                ,collapsible: true
                ,collapsed: true
                ,border: false
                ,margins: '0 0 5 0'
            }, {
                region: 'center'
                ,items: [{
                    layout:'border'
                    ,width:'100%'
                    ,height:'100%'
                    ,items:[{
                         xtype: 'gmappanel'
                        ,region:'center'
                        ,gmapType: 'map'
                        ,zoomLevel: 14
                        ,layout:'fit'
                        ,mapConfOpts: ['enableScrollWheelZoom','enableDoubleClickZoom','enableDragging']
                        ,mapControls: ['GSmallMapControl','GMapTypeControl','NonExistantControl']
                        ,setCenter: {
                            geoCodeAddr: '320 MLK Jr Drive SE, Atlanta, GA, 30312-2151, USA',
                            marker: {title: 'Justin'}
                        }
                        ,markers: [{
                            geoCodeAddr: '4 Yawkey Way, Boston, MA, 02215-3409, USA',
                            marker: {title: 'Fenway Park'}
                        },{
                            geoCodeAddr: '2128 Ridgedale Dr, Atlanta, GA, 30317',
                            marker: {title: 'David'}
                        }]
                    },{
                         region:'west'
                        ,html: '<h1 class="x-panel-header">Track</h1>'
                        ,split:'true'
                        ,hideCollapseTool: true
                        ,width:200
                        ,collapsible:true
                        ,collapseMode:'mini'
                    }]
                }]
            }]
        });
    }
});
