import BaseCollection from 'core/collections/base';

let ForCollection = BaseCollection.extend({
    url: function(){
        return "/api/humans/" + window.humanbot.human_id + "/measurements/for";
    }
});

export default ForCollection;
