/*
humanbot jsapp
*/

// Get env setup
import Backbone from 'backbone';
import Marionette from 'backbone.marionette';
import _ from 'underscore';
window._ = _;
window.moment = require("moment");
Backbone.$ = require('jquery');

let s = document.location.search;
let human_id = s.substr(s.indexOf("human=") + 6);

// Get some routes running
require("health/router.js");

// Boot up app
var regions = new Marionette.RegionManager({
  regions: {
    body: "body"
  }
});

import ChromeView from 'core/views/chrome';
window.humanbot = {
    chrome: new ChromeView(),
    human_id: human_id
}
regions.get("body").show(window.humanbot.chrome);

if(Backbone.History.started != true){
  Backbone.history.start({pushState: false});
}
