/**
 * Created with PyCharm.
 * User: azilot
 * Date: 5/13/12
 * Time: 7:36 AM
 * To change this template use File | Settings | File Templates.
 */

rovar = {
    init: function(){
        this.map = new L.Map('map');
        var minsk = new L.LatLng(53.9, 27.566667);
        var tiles = 'http://{s}.tile.cloudmade.com/4d91f9b3dafc430eafa49b6a99728673/997/256/{z}/{x}/{y}.png';
        var copyright = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>';
        this.map.setView(minsk, 12).addLayer(new L.TileLayer(tiles, {attribution: copyright, maxZoom: 18}));
    },

    loadTracks: function(){
        var self = this;
        $.get('map/tracks', function(response){
		  var tracksGeojsonLayer = new L.GeoJSON();
		  self.map.addLayer(tracksGeojsonLayer);
		  tracksGeojsonLayer.on('featureparse', function(e){
					    var popupContent = "";


					    if (e.properties && e.properties.video) {
						popupContent += e.properties.video;
					    }

					    if (e.properties && e.properties.description) {
						popupContent += e.properties.description;
					    }
					    e.layer.bindPopup(popupContent);
					    if (e.properties && e.properties.style && e.layer.setStyle) {
						e.layer.setStyle(e.properties.style);
					    }
					});
		  tracksGeojsonLayer.addGeoJSON(response);
              }, 'json');
    },

    loadPOIs: function(){
        var self = this;
        $.get('map/points', function(response){
		  var poisGeojsonLayer = new L.GeoJSON(null,{
							   pointToLayer: function (latlng){
							       return new L.CircleMarker(latlng, {
											     radius: 8,
											     fillColor: "#ff7800",
											     color: "#000",
											     weight: 1,
											     opacity: 1,
											     fillOpacity: 0.8
											 });
							   }
						       });
		  poisGeojsonLayer.on('featureparse', function(e){
					  var popupContent = "";
					  if (e.properties && e.properties.description) {
					      popupContent += e.properties.description;
					  }
					  e.layer.bindPopup(popupContent);
					  if (e.properties && e.properties.style && e.layer.setStyle) {
					      e.layer.setStyle(e.properties.style);
					  }
				      });
		  self.map.addLayer(poisGeojsonLayer);
		  poisGeojsonLayer.addGeoJSON(response);
              }, 'json');
    }
};

$(document).ready(function(){
		      rovar.init();
		      rovar.loadTracks();
		      rovar.loadPOIs();
		  });
