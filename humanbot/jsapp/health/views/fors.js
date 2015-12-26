import Marionette from 'backbone.marionette';
import Backbone from 'backbone';
import EmptyView from 'core/views/empty';

let ForView = Marionette.ItemView.extend({
    template: require("health/templates/for.html"),
    className: "list-item",
    onRender: function(){
        this.$el.on("click", () => {
            this.onNavigate();
        });
    },
    onNavigate: function(){
        Backbone.history.navigate("health/measurements/" + this.model.get("id"), {
            "trigger": true
        })
    }
})

let ForListView = Marionette.CollectionView.extend({
    childView: ForView,
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

export default ForListView;
