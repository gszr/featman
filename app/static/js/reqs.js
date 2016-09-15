$(document).ready(function() {

	$.getJSON("/api/request", function(data) {
		var viewModel = {
			requests : ko.observableArray(data)
		};

		ko.applyBindings(viewModel);
	});

});
