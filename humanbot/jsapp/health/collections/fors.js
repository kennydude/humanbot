import BaseCollection from 'core/collections/base';
import For from 'health/models/for';

let ForCollection = BaseCollection.extend({
    url: function(){
        return "/api/humans/" + window.humanbot.human_id + "/measurements/for";
    },
    model: For
});

export default ForCollection;
