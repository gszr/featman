var viewModel = {
	columns  : ko.observableArray([
		{col: "id", val: "#", type: "string", state: ko.observable("")},
		{col: "title", val: "Title", type: "string", state: ko.observable("")},
		{col: "description", val: "Description", type: "string", state: ko.observable("")},
		{col: "reporter", val: "Reporter", type: "string", state: ko.observable("")},
		{col: "status", val: "Status", type: "string", state: ko.observable("")},
		{col: "dateReported", val: "Reported on", type: "date", state: ko.observable("")},
		{col: "dateResolved", val: "Resolved on", type: "date", state: ko.observable("")}
	]),
	issues : ko.observableArray([]),
	sortClick : function(col) {
		setSortingArrow(col);
		switch(col.type) {
			case "string":
				stringSort(col);
				break;
			case "date":
				dateSort(col);
		}
	},
	filterColumn : function() {
		var column = viewModel.columns().filter(function(column) {
			return column["val"].toLowerCase() 
				=== $("#selectedColumn").text().toLowerCase();
		});
		column = column[0].col;
		console.log(column);
		filterColumn(column);
	},
	filterTerm : ko.observable("")
};

function filterColumn(column) {
	if (viewModel.allIssues)
		viewModel.issues(viewModel.allIssues);
	var filtered = viewModel.issues().filter(function(issue) {
		return issue[column].toString().toLowerCase().includes(viewModel.filterTerm());
	});
	viewModel.allIssues = viewModel.issues();
	viewModel.issues(filtered);
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
	viewModel.issues(viewModel.issues().sort(function(a, b) {
		var issueA = a[col.col].toString().toLowerCase();
		var issueB = b[col.col].toString().toLowerCase();
		if (issueA < issueB)
			return (col.state() === sortArrowUp) ? -1 : 1;
		else if (issueA > issueB)
			return (col.state() === sortArrowUp) ? 1 : -1;
		else
			return 0;
	}));
}

function dateSort(col) {
	viewModel.issues(viewModel.issues().sort(function(a, b) {
		if (col.state() === sortArrowUp)
			return new Date(a[col.col]) - new Date(b[col.col]);
		else
			return new Date(b[col.col]) - new Date(a[col.col]);
	}));
}


$(document).ready(function() {
	ko.applyBindings(viewModel);
	$.getJSON("/api/issue", function(data) {
		viewModel.issues(data);
	});
});

$(document.body).on("click", ".selectColumn", function(e) {
	$("#selectedColumn").text($(this).text());
	$(this).parent().close();
	return false;
})
