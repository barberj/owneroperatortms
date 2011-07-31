Ext.onReady(function(){
    console.log('Building Menu');

    function clickHandler(){
        Ext.example.msg('Clicked');
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
