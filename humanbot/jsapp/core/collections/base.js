import Backbone from 'backbone';
import PageableCollection from 'backbone.paginator';

class BaseCollection extends PageableCollection {
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

    parseRecords(response) {
      return response.results;
    }

    parseState(response, state) {
      var rtnState = {
        totalRecords: response.count,
        totalPages: response.page_count
      };

      if (response.per_page) {
        rtnState.pageSize = response.per_page;
      }

      return rtnState;
    }
}

BaseCollection.prototype.queryParams = {
    sortKey: 'ordering',
    totalRecords: null,
    totalPages: null
};
BaseCollection.prototype.state = {
    pageSize: 20,
    pagesInRange: 10
};

export default BaseCollection;
