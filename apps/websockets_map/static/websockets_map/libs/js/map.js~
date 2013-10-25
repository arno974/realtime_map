var map, socket, moveend;

function connected(){
    socket.subscribe('room-1');
}

function messaged(msg){  
    //unregister to avoid infinite loop    
    map.events.unregister("moveend", map, sendNewPosition); 
    switch (msg.action) {
        case "moveend":            
            if(msg.zoom && msg.lon && msg.lat){
                map.setCenter(new OpenLayers.LonLat(msg.lon,msg.lat), msg.zoom);
            }
    } 
    //register again  
    map.events.register("moveend", map, sendNewPosition);    
}

function sendNewPosition(evt){
    var position = {"action":evt.type,"zoom":evt.object.getZoom(),"lon":evt.object.getCenter().lon, "lat":evt.object.getCenter().lat};
    socket.send(position);
}

function init_websockets(){
    socket = new io.Socket();
    socket.connect('http://localhost:9000');                
    socket.on('connect', connected);
    socket.on('message', messaged);
}

function init(){     
    init_websockets();
    map = new OpenLayers.Map("map_div", {
        projection: new OpenLayers.Projection("EPSG:900913"),
        displayProjection: new OpenLayers.Projection("EPSG:4326")
    });

    /*map.events.on({
        "moveend" : sendNewPosition  
    });*/

    //moveend = map.events.register("moveend", map, sendNewPosition);       
    
    var stamen = new OpenLayers.Layer.Stamen("toner");

    map.addLayer(stamen);	
    map.setCenter(new OpenLayers.LonLat(0, 0), 2); 
}


