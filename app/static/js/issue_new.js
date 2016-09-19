var viewModel = {
	title        : ko.observable(),
	description  : ko.observable(),
	reporter     : ko.observable(),
	dateReported : ko.observable(),
	dateResolved : ko.observable(),
	status       : ko.observable(),
	// status needs more thinking... ;p
	listStatus       : ko.observable(["Open", "Fixed", "Deployed"]),
	clients      : ko.observableArray([])
};

viewModel.submitReq = function() {
	$.ajax({
		type : "POST",
		url  : "/api/issue",
		contentType: "application/json; charset=utf-8",
		data : ko.toJSON(this),
		dataType : "json",
		success: function(returnedData) {
			window.location.href = "/issue/all"
		}
		//TODO handle failure as well
	})
}

$(document).ready(function() {
	ko.applyBindings(viewModel);
	$.getJSON("/api/client", function(data) {
		viewModel.clients(data);
	});

	$('.datepicker').datepicker({
		maxViewMode: 3,
		todayBtn: "linked",
		orientation: "bottom right",
		autoclose: true
	});
});

