/**
 * Created with PyCharm.
 * User: azilot
 * Date: 5/13/12
 * Time: 7:36 AM
 * To change this template use File | Settings | File Templates.
 */

var NEW_TRACK, T;
var tmp,data;
function reset_tmp(){
    tmp = [];
    data = {features:[{type: "Feature",
		       properties: {name: "first_track _1",
				    description: "First track (probably bikeroad) _2",
				    video : "<iframe width=\"640\" height=\"360\" src=\"https://www.youtube-nocookie.com/embed/mIwfS8uJJIk?rel=0\" frameborder=\"0\" allowfullscreen></iframe>",
				    type: "Commuting"},
		       geometry: {type: "LineString",
				  coordinates: tmp}
		      }],
	    type: "FeatureCollection"
	   };
};

rovar = {
    init: function(){
        this.map = new L.Map('map');
        var minsk = new L.LatLng(53.9, 27.566667);
        var tiles = 'http://{s}.tile.cloudmade.com/4d91f9b3dafc430eafa49b6a99728673/997/256/{z}/{x}/{y}.png';
        var copyright = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>';
        this.map.setView(minsk, 12).addLayer(new L.TileLayer(tiles, {attribution: copyright, maxZoom: 18}));
    },

    _mousedown: function(e){
	tmp.push([e.latlng.lng,e.latlng.lat]);
	NEW_TRACK.clearLayers();
	rovar.addTrack(data);				   
    },

    enableAddTrack: function(){
	reset_tmp();
        var self = this;
	this.map.on('mousedown',this._mousedown);
    },

    disableAddTrack: function(){
	this.map.off('mousedown',this._mousedown);
    },

    addTrack: function(response){
	var tracksGeojsonLayer = new L.GeoJSON();
	rovar.map.addLayer(tracksGeojsonLayer);
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
	NEW_TRACK = tracksGeojsonLayer;
    },

    loadTracks: function(){
        $.get('map/tracks',this.addTrack , 'json');
    },

    saveTrack: function(){
	$.ajax({type: 'post',
		dataType: 'json',
		url:'map/add-track',success:function(data){T=data;},
		data : {name : $('[name="name"]').val(),
			description : $('[name="description"]').val(),
			video : $('[name="video"]').val(),
			track_type : $('[name="track_type"]').val(),
			coordinates : JSON.stringify( tmp )
		       }
	       });
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

function add_track(){
    NEW_TRACK.clearLayers();
    rovar.addTrack(data);
    //tmp=[];
    //tracksGeojsonLayer.addGeoJSON(tmp_response);
};




$(document).ready(
    function(){
	rovar.init();
	rovar.loadTracks();
	//$.get('map/tracks',function(response){T=response;tmp = response.features[0].geometry.coordinates;add_track();} , 'json');

	rovar.loadPOIs();
	
    });
