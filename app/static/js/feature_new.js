var viewModel = {
	title     : ko.observable(),
	descr     : ko.observable(),
	client    : ko.observable(),
	clients   : ko.observableArray([
		{id: 1, name: "ClientA"},
		{id: 2, name: "ClientB"},
		{id: 3, name: "ClientC"}]),
	priority  : ko.observable(),
	deadline  : ko.observable(),
	url       : ko.observable(),
	prodarea  : ko.observable(),
	prodareas : ko.observableArray(["Policies", "Billing", "Claims",
		"Reports"])

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

ko.applyBindings(viewModel);

$(document).ready(function() {
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
