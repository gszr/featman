$(document).ready(function() {
	function ViewModel() {
		this.title    = ko.observable();
		this.descr    = ko.observable();
		this.client   = ko.observable();
		this.priority = ko.observable();
		this.deadline = ko.observable();
		this.url      = ko.observable();
		this.prodarea = ko.observable();

		this.submitReq = function() {
			$.ajax({
				type : "POST",
				url  : "/api/request",
				contentType: "application/json; charset=utf-8",
				data : ko.toJSON(this),
				dataType : "json",
				success: function(returnedData) {
					window.location.href = "/requests/all"
				}
				//TODO handle failure as well
			})
		}
	};

	ko.applyBindings(new ViewModel());

	$('.datepicker').datepicker({
		maxViewMode: 3,
		todayBtn: "linked",
		orientation: "bottom right"
	});
});
