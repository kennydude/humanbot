import Marionette from 'backbone.marionette';

let EmptyView = Marionette.ItemView.extend({
    template: require("core/templates/empty.html"),
    templateHelpers: function(){
        return {
            collection: this.options.collection
        }
    }
});

export default EmptyView;
