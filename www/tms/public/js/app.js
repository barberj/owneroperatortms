Ext.require('Ext.container.Viewport');
Ext.application({
    name: 'HelloExt',
    launch: function() {
        Ext.create('Ext.container.Viewport', {
            layout:'fit',
            items: [
                {
                    title: 'Hello Ext',
                    html: 'Hello! Weclome to Ext JS.'
                }
            ]
        });
    } 
});
