import BaseRoute from 'core/base_route';

import ForCollection from 'health/collections/fors';
import MeasurementCollection from 'health/collections/measurements';

import ForView from 'health/views/fors';
import MeasurementListView from 'health/views/list';

BaseRoute.create({
    url: "health",
    tab: "health",
    route: function(){
        let col = new ForCollection();
        this.show(new ForView({
            collection: col
        }))
        col.fetch();
    }
})

BaseRoute.create({
    url: 'health/measurements/:for_id',
    tab: "health",
    route: function(for_id){
        let col = new MeasurementCollection();
        col.id = for_id;
        this.show(new MeasurementListView({
            collection: col
        }));
        col.fetch();
    }
});
