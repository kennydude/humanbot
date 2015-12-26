import BaseCollection from 'core/collections/base';

let MeasurementCollection = BaseCollection.extend({
    url: function(){
        return "/api/humans/" + window.humanbot.human_id +
            "/measurements?measurement_for=" + this.id;
    }
});

export default MeasurementCollection;
