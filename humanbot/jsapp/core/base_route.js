import SuperRouter from 'backbone.superrouter';

let BaseRoute = SuperRouter.Route.extend({
    tab: "none",
    show: function(view){
        window.humanbot.chrome.setTab(this.tab);
        window.humanbot.chrome.showChildView("content", view);
    }
});

export default BaseRoute;
