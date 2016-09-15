$(document).ready(function() {

	$.getJSON("/api/feature", function(data) {
		var viewModel = {
			requests : ko.observableArray(data)
		};

		ko.applyBindings(viewModel);
	});

});
