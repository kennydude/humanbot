import Marionette from 'backbone.marionette';
import Chart from 'chart.js';

let ChartView = Marionette.ItemView.extend({
    initialize: function(){
        this.listenTo(this.options.collection, 'sync', this.render);
    },
    ui: {
        "chart": ".chart"
    },
    template: function(){
        return `<canvas class="chart" width="400" height="200"></canvas>`;
    },
    onRender: function(){
        if(this.ui.chart == ".chart") return;
        let col = this.options.collection;
        let ctxt = this.ui.chart.get(0).getContext("2d");
        let data = {
            labels: col.map(function(item){
                return moment(item.get("created")).format("YYYY-MM-DD");
            }).reverse(),
            datasets: [
                {
                    label: "Data",
                    data: col.map(function(item){
                        return item.get("normalised_value")
                    }).reverse()
                }
            ]
        };
        let chart = new Chart(ctxt).Line(data, {
            responsive: true
        });
    }
});

export default ChartView;
