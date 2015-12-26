import BaseModel from 'core/models/base';

let ForModel = BaseModel.extend({
    url: function(){
        return "/api/humans/" + humanbot.human_id + "/measurements/for/" + this.get("id");
    }
});

export default ForModel;
