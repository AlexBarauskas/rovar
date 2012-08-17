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

    clear_tracks: function(){
	NEW_TRACK.clearLayers();
    },

    _mousedown: function(e){
	tmp.push([e.latlng.lng,e.latlng.lat]);
	//rovar.clear_tracks();
	rovar.addTrack(data);				   
    },

    _mousedown_point: function(e){
	tmp = [e.latlng.lng,e.latlng.lat];
	//rovar.addTrack(data);				   
    },


    enableAddTrack: function(){
	reset_tmp();
        var self = this;
	this.map.on('mousedown',this._mousedown);
    },

    enableAddPoint: function(){
	reset_tmp();
        var self = this;
	this.map.on('mousedown',this._mousedown_point);
    },


    disableAddTrack: function(){
	this.map.off('mousedown',this._mousedown);
    },

    disableAddPoint: function(){
	this.map.off('mousedown',this._mousedown_point);
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
        var self = this;
	$.ajax({type: 'post',
		dataType: 'json',
		async:false,
		url:'map/add-track',success:function(data){self.errors_add_track=data.errors;},
		data : {name : $('[name="name"]').val(),
			email:$('[name="email"]').val(),
			description : $('[name="description"]').val(),
			video : $('[name="video"]').val(),
			track_type : $('[name="track_type"]').val(),
			coordinates : JSON.stringify( tmp )
		       }
	       });
    },

    savePoint: function(){
        var self = this;
	$.ajax({type: 'post',
		dataType: 'json',
		async:false,
		url:'map/add-point',success:function(data){self.errors_add_point=data.errors;},
		data : {name : $('[name="point-name"]').val(),
			email:$('[name="point-email"]').val(),
			description : $('[name="point-description"]').val(),
			point_type : $('[name="point-point_type"]').val(),
			place_point : JSON.stringify( tmp )
		       }
	       });
    },


    loadPOIs: function(){
        var self = this;
        $.get('map/points', function(response){
		  var myIcon =new L.Icon({
					  iconUrl: '/static/images/poi/attention.png',
					  iconSize: [20, 20],
					  iconAnchor: [-20, -20]
					  //popupAnchor: [0, 0]
				      });

		  var poisGeojsonLayer = new L.GeoJSON(null,{
							   pointToLayer: function (latlng){
							       return new L.Marker(latlng, {
										       opacity: 0.75,
										       size:[20,20]
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
					  tmp_p=e;
					  e.layer.setIcon(new L.Icon({iconUrl: '/static/images/poi/'+e.properties.type+'.png',
								      iconSize: [20, 20],
								      iconAnchor: [0, 0],
								      popupAnchor: [0, 0]}));
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

function AddLike(id,url){
	$.ajax({type: 'get',
		dataType: 'json',
		async:false,
		url:url,
		success:function(data){if(!data.errors)$("#like-"+id.toString()).html(data.like);}
	       });
    
};

var tmp_p;

$(document).ready(
    function(){
	rovar.init();
	rovar.loadTracks();
	rovar.loadPOIs();
	
    });
