Ext.require([
    'Ext.grid.*',
    'Ext.data.*',
    'Ext.util.*',
    'Ext.grid.PagingScroller'
]);

Ext.onReady(function(){
    Ext.define('PayloadRow'),   {
        extends:    'Ext.data.Model',
        fields:     [
            
        ],
        idProperty: 'payloadid'

    var grid = Ext.create('Ext.grid.Panel', {
        width: 500,
        height: 500,
        title: 'Payloads',
        store: Null,
        verticalScrollerType: 'paginggridscroller',
        loadMask: true,
        disableSelection: true,
        invalidateScrollerOnRefresh: false,
        viewConfig: {
            trackOver: false
        },
        columns:[{
                id: payloadid,
                text: "Payload ID",
                dataIndex: 'payload',
                flex: 1,
                renderer: renderPayload,
                sortable: true
            }
        }],
        renderTo: Ext.getBody()
    }
});
