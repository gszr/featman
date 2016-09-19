var viewModel = {
	title     : ko.observable(),
	descr     : ko.observable(),
	client    : ko.observable(),
	clients   : ko.observableArray([]),
	priority  : ko.observable(),
	deadline  : ko.observable(),
	url       : ko.observable(),
	prodarea  : ko.observable(),
	prodareas : ko.observableArray([])
};

viewModel.submitReq = function() {
	$.ajax({
		type : "POST",
		url  : "/api/feature",
		contentType: "application/json; charset=utf-8",
		data : ko.toJSON(viewModel),
		dataType : "json",
		success: function(returnedData) {
			window.location.href = "/feature/all"
		}
		//TODO handle failure as well
	})
}


$(document).ready(function() {

	ko.applyBindings(viewModel);

	$.getJSON("/api/client", function(data) {
		viewModel.clients(data);
	});

	$.getJSON("/api/product", function(data) {
		viewModel.prodareas(data);
	});

	$('.datepicker').datepicker({
		maxViewMode: 3,
		todayBtn: "linked",
		orientation: "bottom right",
		autoclose: true
	});
});
