var viewModel = {
	requests : ko.observableArray([])
};

ko.applyBindings(viewModel);


$(document).ready(function() {

	$.getJSON("/api/feature", function(data) {
		viewModel.requests(data);
	});

});
