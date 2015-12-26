import Marionette from 'backbone.marionette';
import Backbone from 'backbone';
import ChartView from 'core/views/chart';
import EmptyView from 'core/views/empty';

let MeasurementItemView = Marionette.ItemView.extend({
    template: require("health/templates/measurement.html"),
    className: "list-item",
    onRender: function(){
        this.$el.on("click", () => {
            this.onNavigate();
        });
    },
    onNavigate: function(){
        /*Backbone.history.navigate("health/measurements/" + this.model.get("id"), {
            "trigger": true
        })*/
    }
})

let MeasurementListView = Marionette.CollectionView.extend({
    childView: MeasurementItemView,
    emptyViewOptions: function(){
        return {
            collection: this.collection
        }
    },
    emptyView: EmptyView,
    collectionEvents: {
        "state": "render"
    }
});

let MeasurementChartView = ChartView.extend({

});

let MeasurementView = Marionette.LayoutView.extend({
    template: require("health/templates/measurement_layout.html"),
    regions: {
        "chart": ".chart",
        "list": ".list"
    },
    onRender: function(){
        let col = this.options.collection;
        this.showChildView('list', new MeasurementListView({
            collection: col
        }));
        this.showChildView('chart', new MeasurementChartView({
            collection: col
        }));
    }
})

export default MeasurementView;
