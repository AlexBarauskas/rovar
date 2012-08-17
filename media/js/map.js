function show_form_add_track(){
    $('.mask').show();
    $('#form_add_track').show();
    //rovar.clear_tracks();
    //rovar.enableAddTrack();
};

function btn_add_track(){
    $('#add-btn-track-form').hide();
    $('#ok-btn-save').show();
    $('.mask').hide();
    $('#form_add_track').animate({'left':'66%'});
    rovar.clear_tracks();
    rovar.enableAddTrack();
};

function close_form_add_track(save){
    $('#form_add_track>p>.error').remove();
    if(save)
	rovar.saveTrack();
    else{
	rovar.errors_add_track=null;
	$('.mask').hide();
    }
    if(rovar.errors_add_track){
	for(key in rovar.errors_add_track){
	    
	    $('[name="'+key+'"]').parent().append('<p class="error">'+rovar.errors_add_track[key]+'</p>');
	}
    }
    else{
	rovar.disableAddTrack();
	rovar.clear_tracks();
	rovar.loadTracks();
	$('#form_add_track').hide();
	$('#add-btn-track-form').show();
	$('#ok-btn-save').hide();
    }
};



// POint actions
function show_form_add_point(){
    $('.mask').show();
    $('#form_add_point').show();
};

function btn_add_point(){
    $('#add-btn-point-form').hide();
    $('#ok-btn-point-save').show();
    $('.mask').hide();
    $('#form_add_point').animate({'left':'66%'});
    //rovar.clear_points();
    rovar.enableAddPoint();

}

function close_form_add_point(save){
    if(save)
	rovar.savePoint();
    else{
	rovar.errors_add_point=null;
	$('.mask').hide();
    }
    if(rovar.errors_add_point){
	for(key in rovar.errors_add_point){
	    
	    $('[name="point-'+key+'"]').parent().append('<p class="error">'+rovar.errors_add_point[key]+'</p>');
	}
    }
    else{
	rovar.disableAddPoint();
	//rovar.clear_tracks();
	rovar.loadPOIs();
	//$('#form_add_point>p>.error').remove();
	$('#form_add_point').hide();
	$('#add-btn-point-form').show();
	$('#ok-btn-point-save').hide();
    }


    //$('.mask').hide();

}  


// ready doc
$(document).ready(
    function(){
	$('#form_add_track>p>input').change(
	    function(e){
		if($(e.target).val()!='')
		    $(e.target).parent().find('.error').remove();
	    });
    });
