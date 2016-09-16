$(document).ready(function() {
	function ViewModel() {
		this.name      = ko.observable();

		this.submitReq = function() {
			$.ajax({
				type : "POST",
				url  : "/api/client",
				contentType: "application/json; charset=utf-8",
				data : ko.toJSON(this),
				dataType : "json",
				success: function(returnedData) {
					window.location.href = "/client/all"
				}
				//TODO handle failure as well
			})
		}
	};

	ko.applyBindings(new ViewModel());
});
