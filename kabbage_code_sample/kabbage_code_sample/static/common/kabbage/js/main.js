function success(pos) {
	var crd = pos.coords;
	latLon = {};
	latLon.latitude = crd.latitude;
	latLon.longitude = crd.longitude;
	$("#latitude").val(latLon.latitude);
	$("#longitude").val(latLon.longitude);
};

var search_near = function(){
	if (location.search.indexOf('latitude') != -1){
		$('#search-near').prop('checked', true);
		navigator.geolocation.getCurrentPosition(success);
		$("#latitude").prop('disabled', false);
		$("#longitude").prop('disabled', false);
	}
}


$( document ).ready(function() {
	$('#search-near').change(function(){
		if($('#search-near').prop('checked') == true){
			navigator.geolocation.getCurrentPosition(success);
			$("#latitude").prop('disabled', false);
			$("#longitude").prop('disabled', false);
		} else{
			$("#latitude").val("");
			$("#longitude").val("");
			$("#latitude").prop('disabled', true);
			$("#longitude").prop('disabled', true);
		}
	});
	search_near();
});
