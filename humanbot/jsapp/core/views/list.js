import Marionette from 'backbone.marionette';
import EmptyView from 'core/views/empty';

let BaseListView = Marionette.CompositeView.extend({
    template: require("core/templates/list.html"),
    childViewContainer: ".list",
    emptyView: EmptyView,
    emptyViewOptions: function(){
        return {
            collection: this.collection
        }
    },
    collectionEvents: {
        "state": "render"
    },
    templateHelpers: function(){
        console.log(this.collection.hasNextPage());
        return {
            hasPrevPage: this.collection.hasPreviousPage(),
            hasNextPage: this.collection.hasNextPage()
        }
    }
});

export default BaseListView;
