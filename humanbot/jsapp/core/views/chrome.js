import Marionette from 'backbone.marionette';
import Backbone from 'backbone';

let ChromeView = Marionette.LayoutView.extend({
    template: require("core/templates/chrome.html"),
    ui: {
        "icon": ".icon"
    },
    events: {
        "click @ui.icon": "onNavigate"
    },
    onNavigate: function(e){
        Backbone.history.navigate(this.$(e.currentTarget).data("href"), {
            trigger: true
        });
    },

    setTab: function(tab){
        this.tab = tab;
        this.render();
    },

    regions: {
        "content": ".content"
    },

    templateHelpers: function(){
        return {
            'tab': this.tab || "none"
        }
    }
});

export default ChromeView;
