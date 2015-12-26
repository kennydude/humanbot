import Backbone from 'backbone';

class BaseCollection extends Backbone.Collection {
    initialize(){
        this.setState("initial");
        this.on("sync", function(){
            this.setState("ready");
        });
    }

    setState(state){
        this.state = state;
        this.trigger('state');
    }

    fetch(){
        this.setState("loading");
        super.fetch();
    }
}

export default BaseCollection;
