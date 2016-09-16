var viewModel = {
	columns  : ko.observableArray([
		{col: "id", val: "#", type: "string", state: ko.observable("")},
		{col: "name", val: "Name", type: "string", state: ko.observable("")},
	]),
	products : ko.observableArray([]),
	sortClick : function(col) {
		setSortingArrow(col);
		switch(col.type) {
			case "string":
				stringSort(col);
				break;
		}
	},
	filterColumn : function() {
		var column = viewModel.columns().filter(function(column) {
			return column["val"].toLowerCase() 
				=== $("#selectedColumn").text().toLowerCase();
		});
		column = column[0].col;
		filterColumn(column);
	},
	filterTerm : ko.observable("")
};

function filterColumn(column) {
	if (viewModel.allClients)
		viewModel.products(viewModel.allClients);
	var filtered = viewModel.products().filter(function(client) {
		return client[column].toString().toLowerCase().includes(viewModel.filterTerm());
	});
	viewModel.allClients = viewModel.products();
	viewModel.products(filtered);
}

var sortArrowUp = "fa fa-arrow-up";
var sortArrowDw = "fa fa-arrow-down";

function setSortingArrow(selectedColumn) {
	var otherCols = viewModel.columns().filter(function(col) {
		return col != selectedColumn;
	});

	for (var i = 0; i < otherCols.length; i++) {
		otherCols[i].state("");
	}

	if (selectedColumn.state() === "" || selectedColumn.state() === sortArrowDw)
		selectedColumn.state(sortArrowUp);
	else
		selectedColumn.state(sortArrowDw);
}

function stringSort(col) {
	viewModel.products(viewModel.products().sort(function(a, b) {
		var featureA = a[col.col].toString().toLowerCase();
		var featureB = b[col.col].toString().toLowerCase();
		if (featureA < featureB)
			return (col.state() === sortArrowUp) ? -1 : 1;
		else if (featureA > featureB)
			return (col.state() === sortArrowUp) ? 1 : -1;
		else
			return 0;
	}));
}

ko.applyBindings(viewModel);


$(document).ready(function() {
	$.getJSON("/api/product", function(data) {
		viewModel.products(data);
	});
});

$(document.body).on("click", ".selectColumn", function(e) {
	$("#selectedColumn").text($(this).text());
	$(this).parent().close();
	return false;
})
