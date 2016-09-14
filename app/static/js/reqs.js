$(document).ready(function() {

	$.getJSON("/api/request/all", function(data) {
		var viewModel = {
			requests : ko.observableArray(data)
		};

		ko.applyBindings(viewModel);
	});

});
