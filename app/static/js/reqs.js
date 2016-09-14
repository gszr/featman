$(document).ready(function() {

	$.getJSON("/api/request/all", function(data) {
		var viewModel = {
//		requests : ko.observableArray([
//			{id: 1, title: 'alo', desc: 'descricao', client:'cliente',
//			priority:'prioridade', deadline:'deadline', url:'url', prodarea:'prod'}
//		])
		requests : ko.observableArray(data)
	};

	ko.applyBindings(viewModel);
	
	});

});
