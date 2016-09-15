var viewModel = {
	columns  : ko.observableArray([
		{col: "id", val: "#", type: "string", state: ko.observable("")},
		{col: "title", val: "Title", type: "string", state: ko.observable("")},
		{col: "descr", val: "Description", type: "string", state: ko.observable("")},
		{col: "client", val: "Client", type: "string", state: ko.observable("")},
		{col: "priority", val: "Priority", type: "string", state: ko.observable("")},
		{col: "deadline", val: "Target Date", type: "string", state: ko.observable("")},
		{col: "url", val: "Ticket URL", type: "string", state: ko.observable("")},
		{col: "prodarea", val: "Product Area", type: "string", state: ko.observable("")},
	]),
	features : ko.observableArray([])
};

ko.applyBindings(viewModel);


$(document).ready(function() {
	$.getJSON("/api/feature", function(data) {
		viewModel.features(data);
	});
});
