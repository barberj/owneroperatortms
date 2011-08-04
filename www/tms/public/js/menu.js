Ext.require(['*']);

Ext.onReady(function(){
    console.log('Building Menu');

    Ext.QuickTips.init();

    function clickHandler(){
        console.log('Clicked');
        Ext.example.msg('Clicked', 'Clicked');
    }

    var tb = Ext.create('Ext.toolbar.Toolbar', {
        renderTo:   document.getElementById('toolbar'),
        items   :   [
            {
                text: 'Payloads',
                handler: clickHandler
            }
        ]
        
    });
}); //end onReady
