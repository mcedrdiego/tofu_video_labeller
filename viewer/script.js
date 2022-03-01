

addLabels = function(name, labels) {
    if (!document.labels)
        document.labels = [];
    document.labels.push({"name": name, "labels": labels});
    
}
// inspired from https://bl.ocks.org/vasturiano/ded69192b8269a78d2d97e24211e64e0

function refresh() {
    document.getElementById('myPlot').innerHTML = "";
    var data = getData(true);
    TimelinesChart()
        .data(data)
        .zQualitative(true)
        (document.getElementById('myPlot'));
}

function getLabelNames (labels) {
    var result = new Set();
    for(var i in labels["data"]) {
        if (labels["data"][i][0] != "")
            result.add(labels["data"][i][0]);
    }
    return Array.from(result).sort(function (a, b) {
            var classA = getClass(a);
            var classB = getClass(b);
            if (classA != classB)
                return classA.localeCompare(classB);
            else
                return a.localeCompare(b);
        }
    );
}

function toDate(str) {
    return Date.parse("0000-01-01T" + str.replace(",", "."));
}

function getClass(str) {
    if (str.includes("Debut")) {
        return "0";
    }
    if (str.includes("Bras")) {
        return "bras";
    }
    else if (str.includes("Jambe")) {
        return "jambe";
    }
    else
        return "corps";
}

function getDataByName(labels, name) {
    var result_data_byname = [];
    for(var i in labels["data"]) {
        if (name == labels["data"][i][0]) {
            var v = {"timeRange": [toDate(labels["data"][i][1]), toDate(labels["data"][i][2])], "val": getClass(name)};
            result_data_byname.push(v);
        }
    }
    return result_data_byname;
}


function getData() {

    var result_data = [];
    
    for(var id in document["labels"]) {
            var labels = document["labels"][id];
            var sub = {};
            sub["group"] = labels["name"];
            sub["data"] = [];
            
            var names = getLabelNames(labels["labels"]);
            for(var i in names) {
                var d = getDataByName(labels["labels"], names[i]);
                sub["data"].push({"label": names[i], "data": d });
            }
            result_data.push(sub);
    }
    
    return result_data;

}


function loadCSVButton(evt) {
        loadCSV(evt.target.files);
}

    

function loadCSV(files, propagate = false) {
    console.log(files);
    var readerObj = new FileReader();

    function readFile(index) {
        if( index >= files.length ) { 
            refresh();
            return;
        }
        
        var file = files[index];
        
        // Only process csv files.
        if (file.type == "text/csv") {
            
            readerObj.onload = function(e) {  
                // get file content  
                var bin = e.target.result;

                var fileText = readerObj.result;
                var labels = Papa.parse(fileText);
            
                addLabels(files[index].name, labels);
                
                // next file
                readFile(index + 1);
            }
        }
        else
            readFile(index + 1);
            
        readerObj.readAsText(file);
        
    };
    
    readFile(0);
}


$(document).ready( function () {
        // loading a svg file will run the rendering process
        $("#loadCSV").on("change", loadCSVButton);

});
